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
    attempts: int = 0


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
        result.error = err.get("message", str(err)) if isinstance(err, dict) else str(err)
        return result
    choices = data.get("choices") or []
    if not choices:
        result.error = "Response contained no choices"
        return result
    choice = choices[0]
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

    async def one(model: str, run: int) -> CallResult:
        result = await call_model(client, semaphore, task, model, run, web)
        if on_done:
            on_done(result)
        return result

    jobs = [one(model, run) for run in range(1, runs + 1) for model in models]
    return list(await asyncio.gather(*jobs))
