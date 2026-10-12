"""Anonymized, shuffled judging of contestant answers against a rubric."""

from __future__ import annotations

import json
import random
import re
import string
from dataclasses import dataclass, field
from typing import Any

from openai import AsyncOpenAI

from .runner import CallResult, _error_message, chat_with_retries
from .task import Criterion, Task

JUDGE_MAX_TOKENS = 4000
EXCERPT_LIMIT = 1500  # characters of each cited excerpt shown to the judge

JUDGE_SYSTEM = """You are an impartial evaluator comparing anonymous answers to the same task.
Score each answer against the rubric on its merits. Do not reward length: a shorter answer
that fully does the job beats a longer one that pads. Ignore the order the answers appear in.
{claims_rule} Return JSON only, with no prose and no code fences."""

# With web search, claims are checked against what each model retrieved.
CLAIMS_RULE_WEB = """Each answer comes with the sources its model retrieved. Check its factual claims against
the cited excerpts and list any claim the excerpts do not support. An answer with no sources
has nothing backing its claims."""
# Without web search there are no sources to check, and their absence is not a fault.
CLAIMS_RULE_NO_WEB = """The models had no web access, so answers have no sources and that is not a fault.
List any factual claim that is wrong or looks invented."""

RETRY_REMINDER = (
    "Your previous reply was not valid JSON in the required shape. "
    "Return valid JSON only, exactly matching the schema, with no other text."
)


class JudgeParseError(ValueError):
    pass


@dataclass
class Judgment:
    """One judge call covering every successful answer in one run."""

    run: int
    label_map: dict[str, str]  # label -> model
    ok: bool = False
    scores: dict[str, dict] = field(default_factory=dict)  # model -> parsed entry + weighted score
    raw_outputs: list[str] = field(default_factory=list)
    error: str | None = None
    cost: float | None = None
    latency: float | None = None
    usage: list[dict] = field(default_factory=list)


def assign_labels(results: list[CallResult], rng: random.Random) -> dict[str, CallResult]:
    """Shuffle answers and label them A, B, C... so the judge can't see model names."""
    shuffled = list(results)
    rng.shuffle(shuffled)
    return {_label(i): r for i, r in enumerate(shuffled)}


def _label(i: int) -> str:
    letters = string.ascii_uppercase
    return letters[i] if i < 26 else letters[i // 26 - 1] + letters[i % 26]


def weighted_score(criteria: dict[str, float], rubric: list[Criterion]) -> float:
    """Sum of criterion score x weight, on the same 0-10 scale as the scores."""
    return sum(criteria[c.name] * c.weight for c in rubric)


def format_citations(citations: list[dict]) -> str:
    if not citations:
        return "Sources: none"
    lines = ["Sources:"]
    for i, c in enumerate(citations, 1):
        lines.append(f"[{i}] {c.get('title') or '(untitled)'} - {c['url']}")
        excerpt = (c.get("content") or "").strip()
        if excerpt:
            if len(excerpt) > EXCERPT_LIMIT:
                excerpt = excerpt[:EXCERPT_LIMIT] + " [...]"
            lines.append(f"    Excerpt: {excerpt}")
    return "\n".join(lines)


def judge_system_prompt(web: bool) -> str:
    return JUDGE_SYSTEM.format(claims_rule=CLAIMS_RULE_WEB if web else CLAIMS_RULE_NO_WEB)


def build_judge_prompt(task: Task, labeled: dict[str, CallResult], web: bool = True) -> str:
    rubric_lines = "\n".join(
        f"- {c.name} (weight {c.weight:g}): {c.description}" for c in task.rubric
    )
    criteria_example = ", ".join(f'"{c.name}": <1-10>' for c in task.rubric)
    parts = ["# Task given to every model"]
    if task.system:
        parts.append(f"## System prompt\n{task.system.strip()}")
    parts.append(f"## User prompt\n{task.user.strip()}")
    parts.append(f"# Rubric (score each criterion 1-10)\n{rubric_lines}")
    parts.append("# Answers")
    for label, result in labeled.items():
        section = f"## Answer {label}\n{result.answer.strip()}"
        if web:
            section += f"\n\n{format_citations(result.citations)}"
        parts.append(section)
    labels = ", ".join(labeled)
    parts.append(
        "# Output\n"
        f"Return one JSON object with a key for every answer label ({labels}):\n"
        "{\n"
        f'  "<label>": {{"scores": {{{criteria_example}}}, '
        '"unsupported_claims": ["<claim>", ...], "rationale": "<one sentence>"}\n'
        "}\n"
        "Scores are integers from 1 to 10. Use an empty list when every claim is supported. "
        "Length is not a virtue; do not reward longer answers."
    )
    return "\n\n".join(parts)


def parse_judge_output(text: str, labels: list[str], rubric: list[Criterion]) -> dict[str, dict]:
    """Strictly parse and validate the judge's JSON. Raises JudgeParseError."""
    body = (text or "").strip()
    fence = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", body, re.DOTALL)
    if fence:
        body = fence.group(1)
    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        raise JudgeParseError(f"not valid JSON: {e}") from e
    if not isinstance(data, dict):
        raise JudgeParseError("top level must be an object keyed by answer label")

    parsed: dict[str, dict] = {}
    for label in labels:
        entry = data.get(label)
        if not isinstance(entry, dict):
            raise JudgeParseError(f"missing entry for answer {label}")
        scores = entry.get("scores")
        if not isinstance(scores, dict):
            raise JudgeParseError(f"answer {label}: 'scores' must be an object")
        criteria: dict[str, float] = {}
        for c in rubric:
            value = scores.get(c.name)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise JudgeParseError(f"answer {label}: score for '{c.name}' must be a number")
            if not 1 <= value <= 10:
                raise JudgeParseError(f"answer {label}: score for '{c.name}' is {value}, outside 1-10")
            criteria[c.name] = float(value)
        claims = entry.get("unsupported_claims", [])
        if not isinstance(claims, list) or not all(isinstance(x, str) for x in claims):
            raise JudgeParseError(f"answer {label}: 'unsupported_claims' must be a list of strings")
        rationale = entry.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            raise JudgeParseError(f"answer {label}: 'rationale' must be a non-empty string")
        parsed[label] = {
            "criteria": criteria,
            "unsupported_claims": claims,
            "rationale": rationale.strip(),
        }
    return parsed


def _content(response: Any) -> tuple[str, dict]:
    data = response.model_dump() if hasattr(response, "model_dump") else dict(response)
    usage = data.get("usage") or {}
    choices = data.get("choices") or []
    if data.get("error") or not choices:
        err = data.get("error")
        message = err.get("message") if isinstance(err, dict) else err
        raise RuntimeError(message or "judge response contained no choices")
    return (choices[0].get("message") or {}).get("content") or "", usage


async def judge_run(
    client: AsyncOpenAI,
    task: Task,
    judge_model: str,
    run: int,
    results: list[CallResult],
    rng: random.Random,
    web: bool = True,
) -> Judgment:
    """Judge one run's successful answers. Never raises: failures come back as ok=False."""
    labeled = assign_labels(results, rng)
    judgment = Judgment(run=run, label_map={label: r.model for label, r in labeled.items()})
    messages = [
        {"role": "system", "content": judge_system_prompt(web)},
        {"role": "user", "content": build_judge_prompt(task, labeled, web)},
    ]
    request = {
        "model": judge_model,
        "messages": messages,
        "max_tokens": JUDGE_MAX_TOKENS,
        "temperature": 0,
        "extra_body": {"usage": {"include": True}},
    }

    for attempt in range(2):  # one retry with a "valid JSON only" reminder
        try:
            response, latency, _ = await chat_with_retries(client, request)
            text, usage = _content(response)
        except Exception as e:
            judgment.error = f"Judge call failed: {_error_message(e)}"
            return judgment
        judgment.raw_outputs.append(text)
        judgment.usage.append(usage)
        judgment.cost = (judgment.cost or 0) + (usage.get("cost") or 0)
        judgment.latency = (judgment.latency or 0) + latency
        try:
            parsed = parse_judge_output(text, list(labeled), task.rubric)
        except JudgeParseError as e:
            judgment.error = f"Judge returned invalid JSON: {e}"
            request = {
                **request,
                "messages": messages
                + [
                    {"role": "assistant", "content": text},
                    {"role": "user", "content": RETRY_REMINDER},
                ],
            }
            continue
        judgment.error = None
        judgment.ok = True
        for label, entry in parsed.items():
            entry["weighted_score"] = weighted_score(entry["criteria"], task.rubric)
            entry["label"] = label
            judgment.scores[judgment.label_map[label]] = entry
        return judgment
    return judgment
