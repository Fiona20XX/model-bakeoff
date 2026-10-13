"""Council mode: merge the contestants' answers into one, then guess which answer is the merge."""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass, field
from typing import Any

from openai import AsyncOpenAI

from .judge import RETRY_REMINDER, _content, assign_labels, format_citations
from .runner import CallResult, _error_message, chat_with_retries
from .task import Task

GUESS_MAX_TOKENS = 2000
# A synthesis reads every answer and wraps a full answer in JSON, and reasoning models think first,
# so it gets at least this many tokens even when the task's max_tokens is smaller.
SYNTH_MIN_TOKENS = 4000
GUESS_SUM_TOLERANCE = 5  # probabilities must add up to 100 +/- this, then are normalized

SYNTH_SYSTEM = """You combine several independent answers to the same task into one best answer.
Keep what is strongest and best supported in each answer, resolve overlaps, and drop padding.
Only use facts that appear in the answers or their sources; never add new facts. Where you keep
a factual claim, keep it tied to its source with a markdown link to the source URL. Where the
answers conflict, prefer the better-supported side and record the conflict. Return JSON only,
with no prose and no code fences."""

GUESS_SYSTEM = """You are reviewing anonymous answers to the same task. Exactly one of them was not
written independently: it was produced by merging the other answers into one. For each answer,
estimate the probability (0-100) that it is the merged one, and give a one-to-two-line reason
based on what you see in the text. The labels are private to you, so in each reason describe
the answers' content instead of referring to other answers by their letter. Probabilities must
add up to 100. Return JSON only, with no prose and no code fences."""


class CouncilParseError(ValueError):
    pass


def council_name(synthesizer: str) -> str:
    """How the council answer appears in tables and results."""
    return f"council ({synthesizer})"


@dataclass
class Synthesis:
    """One synthesizer call covering one run."""

    run: int
    ok: bool = False
    answer: str = ""
    disagreements: list[str] = field(default_factory=list)
    label_map: dict[str, str] = field(default_factory=dict)  # label shown to the synthesizer -> model
    raw_outputs: list[str] = field(default_factory=list)
    error: str | None = None
    cost: float | None = None
    latency: float | None = None
    usage: list[dict] = field(default_factory=list)


@dataclass
class Guess:
    """One synthesis-guess call covering one run."""

    run: int
    label_map: dict[str, str] = field(default_factory=dict)  # label -> model
    ok: bool = False
    probabilities: dict[str, float] = field(default_factory=dict)  # model -> 0-100
    reasons: dict[str, str] = field(default_factory=dict)  # model -> reason
    raw_outputs: list[str] = field(default_factory=list)
    error: str | None = None
    cost: float | None = None
    latency: float | None = None
    usage: list[dict] = field(default_factory=list)


def _strip_fence(text: str) -> str:
    body = (text or "").strip()
    fence = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", body, re.DOTALL)
    return fence.group(1) if fence else body


def _load_object(text: str) -> dict:
    try:
        data = json.loads(_strip_fence(text))
    except json.JSONDecodeError as e:
        raise CouncilParseError(f"not valid JSON: {e}") from e
    if not isinstance(data, dict):
        raise CouncilParseError("top level must be a JSON object")
    return data


# --- synthesis --------------------------------------------------------------

def build_synth_prompt(task: Task, labeled: dict[str, CallResult], web: bool) -> str:
    parts = ["# Task given to every model"]
    if task.system:
        parts.append(f"## System prompt\n{task.system.strip()}")
    parts.append(f"## User prompt\n{task.user.strip()}")
    parts.append("# Answers to combine")
    for label, result in labeled.items():
        section = f"## Answer {label}\n{result.answer.strip()}"
        if web:
            section += f"\n\n{format_citations(result.citations)}"
        parts.append(section)
    parts.append(
        "# Output\n"
        "Write one best answer to the original task, following its instructions (including any "
        "length limit). Return one JSON object:\n"
        '{"answer": "<the combined answer, in markdown>", '
        '"disagreements": ["<one line per point where the answers conflicted, and what each said>", ...]}\n'
        "Use an empty list when the answers did not conflict. Do not mention the answer labels "
        "or that the answer was combined from others in the answer itself."
    )
    return "\n\n".join(parts)


def parse_synth_output(text: str) -> tuple[str, list[str]]:
    data = _load_object(text)
    answer = data.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise CouncilParseError("'answer' must be a non-empty string")
    disagreements = data.get("disagreements", [])
    if not isinstance(disagreements, list) or not all(isinstance(x, str) for x in disagreements):
        raise CouncilParseError("'disagreements' must be a list of strings")
    return answer.strip(), [d.strip() for d in disagreements if d.strip()]


async def _call_json(client: AsyncOpenAI, request: dict, record, parse) -> Any:
    """Call, parse, and retry once with a JSON reminder. Records outputs/cost/latency on `record`.

    Returns the parsed value, or None with record.error set.
    """
    messages = request["messages"]
    for _ in range(2):
        try:
            response, latency, _ = await chat_with_retries(client, request)
            text, usage = _content(response)
        except Exception as e:
            record.error = f"Call failed: {_error_message(e)}"
            return None
        record.raw_outputs.append(text)
        record.usage.append(usage)
        record.cost = (record.cost or 0) + (usage.get("cost") or 0)
        record.latency = (record.latency or 0) + latency
        if not text.strip():
            # Usually the whole max_tokens budget went on reasoning; asking again won't help.
            record.error = (
                f"Empty reply ({usage.get('completion_tokens')} tokens used; "
                "the model probably spent its whole max_tokens budget reasoning)"
            )
            return None
        try:
            value = parse(text)
        except CouncilParseError as e:
            record.error = f"Returned invalid JSON: {e}"
            request = {
                **request,
                "messages": messages
                + [{"role": "assistant", "content": text}, {"role": "user", "content": RETRY_REMINDER}],
            }
            continue
        record.error = None
        return value
    return None


async def synthesize(
    client: AsyncOpenAI,
    task: Task,
    synthesizer: str,
    run: int,
    answers: list[CallResult],
    rng: random.Random,
    web: bool = True,
) -> Synthesis:
    """Merge one run's successful answers. Never raises: failures come back as ok=False."""
    synthesis = Synthesis(run=run)
    if len(answers) < 2:
        synthesis.error = f"Need at least 2 successful answers to synthesize, got {len(answers)}"
        return synthesis
    labeled = assign_labels(answers, rng)
    synthesis.label_map = {label: r.model for label, r in labeled.items()}
    request: dict[str, Any] = {
        "model": synthesizer,
        "messages": [
            {"role": "system", "content": SYNTH_SYSTEM},
            {"role": "user", "content": build_synth_prompt(task, labeled, web)},
        ],
        "extra_body": {"usage": {"include": True}},
    }
    request["max_tokens"] = max(task.max_tokens or 0, SYNTH_MIN_TOKENS)
    if task.temperature is not None:
        request["temperature"] = task.temperature
    parsed = await _call_json(client, request, synthesis, parse_synth_output)
    if parsed is not None:
        synthesis.answer, synthesis.disagreements = parsed
        synthesis.ok = True
    return synthesis


def union_citations(answers: list[CallResult]) -> list[dict]:
    """Every source the contestants retrieved, de-duplicated by URL, in order."""
    seen: set[str] = set()
    out: list[dict] = []
    for r in answers:
        for c in r.citations:
            if c["url"] not in seen:
                seen.add(c["url"])
                out.append(c)
    return out


def council_result(synthesis: Synthesis, synthesizer: str, contestants: list[CallResult]) -> CallResult:
    """The council answer as one more CallResult, so the normal judge and report can use it.

    Cost = every contestant call in the run + the synthesis. Latency = slowest contestant + synthesis.
    """
    run_rows = [r for r in contestants if r.run == synthesis.run]
    contestant_cost = sum(r.cost or 0 for r in run_rows)
    slowest = max((r.latency or 0 for r in run_rows), default=0)
    ok_rows = [r for r in run_rows if r.ok]
    return CallResult(
        model=council_name(synthesizer),
        run=synthesis.run,
        ok=synthesis.ok,
        answer=synthesis.answer,
        error=None if synthesis.ok else synthesis.error,
        latency=slowest + (synthesis.latency or 0) if synthesis.ok else None,
        cost=contestant_cost + (synthesis.cost or 0),
        citations=union_citations(ok_rows),
        usage=None,
        finish_reason="stop" if synthesis.ok else None,
    )


# --- synthesis guess --------------------------------------------------------

def build_guess_prompt(task: Task, labeled: dict[str, CallResult]) -> str:
    parts = ["# Task given to every model"]
    if task.system:
        parts.append(f"## System prompt\n{task.system.strip()}")
    parts.append(f"## User prompt\n{task.user.strip()}")
    parts.append("# Answers")
    for label, result in labeled.items():
        parts.append(f"## Answer {label}\n{result.answer.strip()}")
    labels = ", ".join(labeled)
    parts.append(
        "# Output\n"
        f"Return one JSON object with a key for every answer label ({labels}):\n"
        '{"<label>": {"probability": <0-100>, "reason": "<1-2 lines>"}}\n'
        "Probabilities must add up to 100."
    )
    return "\n\n".join(parts)


def parse_guess_output(text: str, labels: list[str]) -> dict[str, dict]:
    """Strictly parse the guess and normalize probabilities to sum to exactly 100."""
    data = _load_object(text)
    parsed: dict[str, dict] = {}
    for label in labels:
        entry = data.get(label)
        if not isinstance(entry, dict):
            raise CouncilParseError(f"missing entry for answer {label}")
        p = entry.get("probability")
        if isinstance(p, bool) or not isinstance(p, (int, float)) or not 0 <= p <= 100:
            raise CouncilParseError(f"answer {label}: probability must be a number from 0 to 100")
        reason = entry.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise CouncilParseError(f"answer {label}: 'reason' must be a non-empty string")
        parsed[label] = {"probability": float(p), "reason": reason.strip()}
    total = sum(e["probability"] for e in parsed.values())
    if abs(total - 100) > GUESS_SUM_TOLERANCE:
        raise CouncilParseError(f"probabilities add up to {total:g}, not 100")
    for e in parsed.values():
        e["probability"] = e["probability"] * 100 / total
    return parsed


async def guess_synthesis(
    client: AsyncOpenAI,
    task: Task,
    judge_model: str,
    run: int,
    answers: list[CallResult],
    rng: random.Random,
) -> Guess:
    """Ask the judge which answer is the merge. Separate from scoring; never sees scores."""
    labeled = assign_labels(answers, rng)
    guess = Guess(run=run, label_map={label: r.model for label, r in labeled.items()})
    request = {
        "model": judge_model,
        "messages": [
            {"role": "system", "content": GUESS_SYSTEM},
            {"role": "user", "content": build_guess_prompt(task, labeled)},
        ],
        "max_tokens": GUESS_MAX_TOKENS,
        "temperature": 0,
        "extra_body": {"usage": {"include": True}},
    }
    parsed = await _call_json(client, request, guess, lambda t: parse_guess_output(t, list(labeled)))
    if parsed is not None:
        guess.ok = True
        for label, entry in parsed.items():
            model = guess.label_map[label]
            guess.probabilities[model] = entry["probability"]
            guess.reasons[model] = entry["reason"]
    return guess
