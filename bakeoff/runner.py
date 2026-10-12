"""Fan a task out to every contestant model concurrently and record what came back."""

from __future__ import annotations

import asyncio
import email.utils
import random
import time
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable

import openai
from openai import AsyncOpenAI

from .openrouter import BASE_URL
from .task import Task

MAX_CONCURRENCY = 3
MAX_RETRIES = 3
REQUEST_TIMEOUT = 90.0
MAX_RETRY_AFTER = 60.0


@dataclass
class CallResult:
    model: str
    run: int
    ok: bool
    answer: str = ""
    error: str | None = None
    latency: float | None = None  # seconds, wall clock, final attempt only
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    cost: float | None = None  # USD from usage.cost
    citations: list[dict] = field(default_factory=list)
    usage: dict | None = None
    finish_reason: str | None = None  # "length" means the answer was cut off at max_tokens
    attempts: int = 0
    status: int | None = None  # HTTP status of the final failed attempt, when there was one

    @property
    def permanent_failure(self) -> bool:
        """A 4xx other than 429: retrying or waiting won't help (e.g. model gated or unavailable)."""
        return not self.ok and self.status is not None and 400 <= self.status < 500 and self.status != 429


@dataclass
class Skipped:
    model: str
    error: str


def make_client(api_key: str) -> AsyncOpenAI:
    # Retries are handled here, not by the SDK, so we control backoff and retry-after.
    return AsyncOpenAI(base_url=BASE_URL, api_key=api_key, timeout=REQUEST_TIMEOUT, max_retries=0)


def build_messages(system: str | None, user: str) -> list[dict]:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": user})
    return messages


def build_request(task: Task, model: str, web: bool) -> dict[str, Any]:
    """Keyword arguments for chat.completions.create for one contestant call."""
    extra_body: dict[str, Any] = {"usage": {"include": True}}
    if web:
        plugin: dict[str, Any] = {"id": "web"}
        if task.web.engine:
            plugin["engine"] = task.web.engine
        if task.web.max_results is not None:
            plugin["max_results"] = task.web.max_results
        extra_body["plugins"] = [plugin]
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": build_messages(task.system, task.user),
        "extra_body": extra_body,
    }
    if task.max_tokens is not None:
        kwargs["max_tokens"] = task.max_tokens
    if task.temperature is not None:
        kwargs["temperature"] = task.temperature
    return kwargs


def extract_citations(message: dict) -> list[dict]:
    """Pull url_citation annotations out of a response message, de-duplicated by URL."""
    citations: list[dict] = []
    seen: set[str] = set()
    for ann in message.get("annotations") or []:
        if not isinstance(ann, dict) or ann.get("type") != "url_citation":
            continue
        cite = ann.get("url_citation") or {}
        url = cite.get("url")
        if not url or url in seen:
            continue
        seen.add(url)
        entry = {"url": url, "title": cite.get("title") or ""}
        if cite.get("content"):
            entry["content"] = cite["content"]
        citations.append(entry)
    return citations


def _retry_after(error: openai.APIStatusError) -> float | None:
    value = error.response.headers.get("retry-after") if error.response is not None else None
    if not value:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed is None:
            return None
        return max(0.0, parsed.timestamp() - time.time())


def _is_retryable(error: Exception) -> bool:
    return isinstance(error, openai.APIStatusError) and (
        error.status_code == 429 or error.status_code >= 500
    )


def _error_message(error: Exception) -> str:
    if isinstance(error, openai.APIStatusError):
        body = error.body if isinstance(error.body, dict) else {}
        message = body.get("message") or error.message
        raw = (body.get("metadata") or {}).get("raw")
        if raw and isinstance(raw, str):
            message = f"{message} ({raw[:200]})"
        return f"HTTP {error.status_code}: {message}"
    if isinstance(error, openai.APITimeoutError):
        return f"Timed out after {REQUEST_TIMEOUT:.0f}s"
    return f"{type(error).__name__}: {error}"


async def chat_with_retries(
    client: AsyncOpenAI,
    request: dict[str, Any],
    sleep: Callable[[float], Awaitable[None]] | None = None,
) -> tuple[Any, float, int]:
    """Call the API, retrying 429/5xx up to MAX_RETRIES times.

    Returns (response, latency_seconds, attempts). Raises the last error on failure.
    """
    attempt = 0
    while True:
        attempt += 1
        start = time.perf_counter()
        try:
            response = await client.chat.completions.create(**request)
            return response, time.perf_counter() - start, attempt
        except Exception as e:
            if not _is_retryable(e) or attempt > MAX_RETRIES:
                e.attempts = attempt  # type: ignore[attr-defined]
                raise
            wait = _retry_after(e)
            if wait is None:
                wait = 2 ** attempt + random.uniform(0, 1)
            await (sleep or asyncio.sleep)(min(wait, MAX_RETRY_AFTER))


def parse_response(model: str, run: int, response: Any, latency: float, attempts: int) -> CallResult:
    data = response.model_dump() if hasattr(response, "model_dump") else dict(response)
    usage = data.get("usage") or {}
    result = CallResult(
        model=model,
        run=run,
        ok=False,
        latency=latency,
        attempts=attempts,
        usage=usage or None,
        prompt_tokens=usage.get("prompt_tokens"),
        completion_tokens=usage.get("completion_tokens"),
        cost=usage.get("cost"),
    )
    # OpenRouter can return an error object with HTTP 200 instead of choices.
    if data.get("error"):
        err = data["error"]
        if isinstance(err, dict):
            result.error = err.get("message", str(err))
            if isinstance(err.get("code"), int):
                result.status = err["code"]
        else:
            result.error = str(err)
        return result
    choices = data.get("choices") or []
    if not choices:
        result.error = "Response contained no choices"
        return result
    choice = choices[0]
    result.finish_reason = choice.get("finish_reason")
    message = choice.get("message") or {}
    result.citations = extract_citations(message)
    answer = (message.get("content") or "").strip()
    if not answer:
        reason = choice.get("finish_reason")
        result.error = f"Empty answer (finish_reason={reason})"
        return result
    result.answer = answer
    result.ok = True
    return result


async def call_model(
    client: AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    task: Task,
    model: str,
    run: int,
    web: bool,
) -> CallResult:
    """One contestant call. Never raises: failures come back as ok=False."""
    request = build_request(task, model, web)
    async with semaphore:
        try:
            response, latency, attempts = await chat_with_retries(client, request)
        except Exception as e:
            return CallResult(
                model=model,
                run=run,
                ok=False,
                error=_error_message(e),
                attempts=getattr(e, "attempts", 1),
                status=e.status_code if isinstance(e, openai.APIStatusError) else None,
            )
    try:
        return parse_response(model, run, response, latency, attempts)
    except Exception as e:
        return CallResult(model=model, run=run, ok=False, error=f"Bad response: {e}", latency=latency)


async def run_contestants(
    client: AsyncOpenAI,
    task: Task,
    models: list[str],
    runs: int,
    web: bool,
    on_done: Callable[[CallResult], None] | None = None,
) -> list[CallResult]:
    """Run every model `runs` times, at most MAX_CONCURRENCY requests at once."""
    semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
    return await _run_all(client, semaphore, task, models, range(1, runs + 1), web, on_done)


async def run_free_with_backfill(
    client: AsyncOpenAI,
    task: Task,
    candidates: list[str],
    runs: int,
    web: bool,
    limit: int = 4,
    on_done: Callable[[CallResult], None] | None = None,
    on_skip: Callable[[Skipped], None] | None = None,
) -> tuple[list[CallResult], list[str], list[Skipped]]:
    """Run up to `limit` free models, replacing any whose first call fails permanently.

    Candidates are tried in order. A model whose first run fails with a 4xx other
    than 429 is skipped and the next candidate takes its slot. Models that fail for
    other reasons (rate limits, 5xx, timeouts, empty answers) keep their slot and
    show as failed. Returns (results, models used, skipped models).
    """
    semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
    queue = list(candidates)
    used: list[str] = []
    skipped: list[Skipped] = []
    results: list[CallResult] = []

    async def fill_slot() -> None:
        while queue:
            model = queue.pop(0)
            result = await call_model(client, semaphore, task, model, 1, web)
            if result.permanent_failure:
                entry = Skipped(model=model, error=result.error or "unknown error")
                skipped.append(entry)
                if on_skip:
                    on_skip(entry)
                continue
            used.append(model)
            results.append(result)
            if on_done:
                on_done(result)
            return

    await asyncio.gather(*(fill_slot() for _ in range(min(limit, len(queue)))))
    # Keep the candidate ranking order, not completion order.
    used.sort(key=candidates.index)
    if runs > 1:
        results += await _run_all(client, semaphore, task, used, range(2, runs + 1), web, on_done)
    return results, used, skipped


async def _run_all(client, semaphore, task, models, run_numbers, web, on_done) -> list[CallResult]:
    async def one(model: str, run: int) -> CallResult:
        result = await call_model(client, semaphore, task, model, run, web)
        if on_done:
            on_done(result)
        return result

    return list(await asyncio.gather(*(one(m, r) for r in run_numbers for m in models)))
