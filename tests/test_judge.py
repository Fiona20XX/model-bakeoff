import asyncio
import json
import random
from types import SimpleNamespace

import pytest

from bakeoff.judge import (
    JudgeParseError,
    assign_labels,
    build_judge_prompt,
    judge_run,
    parse_judge_output,
    weighted_score,
)
from bakeoff.runner import CallResult
from bakeoff.task import Criterion, Task

RUBRIC = [Criterion("grounding", 0.5, "g"), Criterion("specificity", 0.3, "s"), Criterion("usefulness", 0.2, "u")]


def make_task():
    return Task(name="t", user="Brief on Acme", system="Be careful", models=[], judge="j/m", rubric=RUBRIC)


def answer(model, text=None, citations=None):
    return CallResult(model=model, run=1, ok=True, answer=text or f"answer from {model}", citations=citations or [])


def entry(g, s, u, claims=(), rationale="fine"):
    return {"scores": {"grounding": g, "specificity": s, "usefulness": u}, "unsupported_claims": list(claims), "rationale": rationale}


def judge_response(content, cost=0.01):
    return {"choices": [{"message": {"content": content}}], "usage": {"completion_tokens": 50, "cost": cost}}


class ScriptedJudge:
    def __init__(self, replies):
        self.replies = list(replies)
        self.requests = []

    async def create(self, **kwargs):
        self.requests.append(kwargs)
        return self.replies.pop(0)


def client_for(judge):
    return SimpleNamespace(chat=SimpleNamespace(completions=judge))


# --- weighted score -------------------------------------------------------

def test_weighted_score_math():
    assert weighted_score({"grounding": 8, "specificity": 6, "usefulness": 10}, RUBRIC) == pytest.approx(7.8)
    assert weighted_score({"grounding": 10, "specificity": 10, "usefulness": 10}, RUBRIC) == pytest.approx(10)
    assert weighted_score({"grounding": 1, "specificity": 1, "usefulness": 1}, RUBRIC) == pytest.approx(1)


# --- parsing --------------------------------------------------------------

def test_parse_valid_output_and_code_fence():
    text = json.dumps({"A": entry(8, 6, 10, ["Acme has 9,000 staff"]), "B": entry(5, 5, 5)})
    parsed = parse_judge_output(f"```json\n{text}\n```", ["A", "B"], RUBRIC)
    assert parsed["A"]["criteria"] == {"grounding": 8.0, "specificity": 6.0, "usefulness": 10.0}
    assert parsed["A"]["unsupported_claims"] == ["Acme has 9,000 staff"]
    assert parsed["B"]["rationale"] == "fine"


@pytest.mark.parametrize(
    "payload",
    [
        "Here are the scores: {}",
        json.dumps({"A": entry(8, 6, 10)}),  # missing B
        json.dumps({"A": entry(11, 6, 10), "B": entry(5, 5, 5)}),  # out of range
        json.dumps({"A": {"scores": {"grounding": 8}, "unsupported_claims": [], "rationale": "x"}, "B": entry(5, 5, 5)}),
        json.dumps({"A": entry("8", 6, 10), "B": entry(5, 5, 5)}),  # string score
        json.dumps({"A": entry(8, 6, 10, rationale=""), "B": entry(5, 5, 5)}),
        json.dumps({"A": {**entry(8, 6, 10), "unsupported_claims": "none"}, "B": entry(5, 5, 5)}),
    ],
)
def test_parse_rejects_malformed_output(payload):
    with pytest.raises(JudgeParseError):
        parse_judge_output(payload, ["A", "B"], RUBRIC)


# --- label shuffling ------------------------------------------------------

def test_labels_are_shuffled_and_cover_every_answer():
    results = [answer(f"m{i}") for i in range(6)]
    orders = {tuple(r.model for r in assign_labels(results, random.Random(seed)).values()) for seed in range(20)}
    assert len(orders) > 1  # order actually varies
    labeled = assign_labels(results, random.Random(1))
    assert list(labeled) == ["A", "B", "C", "D", "E", "F"]
    assert sorted(r.model for r in labeled.values()) == sorted(r.model for r in results)


def test_scores_map_back_to_the_right_models():
    results = [answer("alpha/model"), answer("beta/model"), answer("gamma/model")]
    rng = random.Random(7)
    labeled = assign_labels(results, random.Random(7))
    # Give each label a distinct score so we can see where it lands.
    by_label = {label: entry(i + 2, i + 2, i + 2, rationale=f"label {label}") for i, label in enumerate(labeled)}
    judge = ScriptedJudge([judge_response(json.dumps(by_label))])

    j = asyncio.run(judge_run(client_for(judge), make_task(), "j/m", 1, results, rng))
    assert j.ok
    for i, (label, result) in enumerate(labeled.items()):
        assert j.label_map[label] == result.model
        assert j.scores[result.model]["weighted_score"] == pytest.approx(i + 2)
        assert j.scores[result.model]["rationale"] == f"label {label}"


def test_judge_prompt_is_anonymized_and_includes_citations():
    results = [answer("secret/model-x", text="Acme is a startup.", citations=[{"url": "https://ex.com", "title": "Ex", "content": "Acme raised $5M"}])]
    prompt = build_judge_prompt(make_task(), assign_labels(results, random.Random(0)))
    assert "secret/model-x" not in prompt
    assert "https://ex.com" in prompt and "Acme raised $5M" in prompt
    assert "Brief on Acme" in prompt and "Be careful" in prompt
    assert "grounding (weight 0.5)" in prompt
    assert "Length is not a virtue" in prompt


# --- retry path -----------------------------------------------------------

def test_malformed_json_retries_once_with_reminder():
    results = [answer("a/m"), answer("b/m")]
    good = json.dumps({"A": entry(7, 7, 7), "B": entry(4, 4, 4)})
    judge = ScriptedJudge([judge_response("Sure! A is better."), judge_response(good)])

    j = asyncio.run(judge_run(client_for(judge), make_task(), "j/m", 1, results, random.Random(0)))
    assert j.ok and j.error is None
    assert len(judge.requests) == 2
    retry_messages = judge.requests[1]["messages"]
    assert retry_messages[-2] == {"role": "assistant", "content": "Sure! A is better."}
    assert "valid JSON only" in retry_messages[-1]["content"]
    assert j.cost == pytest.approx(0.02)  # both judge calls are counted
    assert j.raw_outputs == ["Sure! A is better.", good]


def test_judge_gives_up_after_one_retry():
    results = [answer("a/m")]
    judge = ScriptedJudge([judge_response("nope"), judge_response("still nope")])
    j = asyncio.run(judge_run(client_for(judge), make_task(), "j/m", 1, results, random.Random(0)))
    assert not j.ok and "invalid JSON" in j.error
    assert len(judge.requests) == 2 and j.scores == {}


def test_judge_prompt_without_web_has_no_source_checks():
    from bakeoff.judge import judge_system_prompt

    results = [answer("a/m", text="Rate limits cap requests.")]
    prompt = build_judge_prompt(make_task(), assign_labels(results, random.Random(0)), web=False)
    assert "Sources:" not in prompt
    assert "not a fault" in judge_system_prompt(False)
    assert "cited excerpts" in judge_system_prompt(True)
