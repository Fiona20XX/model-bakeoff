import asyncio
import json
import random
from types import SimpleNamespace

import pytest
from typer.testing import CliRunner

from bakeoff.cli import app
from bakeoff.council import (
    CouncilParseError,
    Synthesis,
    build_synth_prompt,
    council_name,
    council_result,
    guess_synthesis,
    parse_guess_output,
    parse_synth_output,
    synthesize,
    union_citations,
)
from bakeoff.judge import assign_labels, build_judge_prompt, judge_run
from bakeoff.report import summarize, table_rows
from bakeoff.runner import CallResult
from bakeoff.task import Criterion, Task

RUBRIC = [Criterion("grounding", 0.6, "g"), Criterion("usefulness", 0.4, "u")]


def make_task():
    return Task(
        name="t", user="Brief on Acme", system="Be careful", models=["a/m", "b/m", "c/m"],
        judge="j/m", synthesizer="s/m", rubric=RUBRIC, max_tokens=4000, temperature=0.2,
    )


def answer(model, run=1, cost=0.01, latency=10.0, citations=None, text=None):
    return CallResult(
        model=model, run=run, ok=True, answer=text or f"Acme answer {model}", cost=cost,
        latency=latency, citations=citations or [],
    )


def reply(content, cost=0.02):
    return {"choices": [{"message": {"content": content}}], "usage": {"completion_tokens": 50, "cost": cost}}


class Scripted:
    def __init__(self, replies):
        self.replies = list(replies)
        self.requests = []

    async def create(self, **kwargs):
        self.requests.append(kwargs)
        return self.replies.pop(0)


def client_for(scripted):
    return SimpleNamespace(chat=SimpleNamespace(completions=scripted))


SYNTH_OK = json.dumps({"answer": "Merged Acme briefing.", "disagreements": ["Headcount: A says 50, B says 80."]})


# --- synthesis parsing and retry ------------------------------------------

def test_parse_synth_output():
    answer_text, disagreements = parse_synth_output(f"```json\n{SYNTH_OK}\n```")
    assert answer_text == "Merged Acme briefing."
    assert disagreements == ["Headcount: A says 50, B says 80."]


@pytest.mark.parametrize("payload", [
    "Here you go: merged!",
    json.dumps({"answer": "", "disagreements": []}),
    json.dumps({"answer": "x", "disagreements": "none"}),
    json.dumps(["answer"]),
])
def test_parse_synth_rejects_malformed(payload):
    with pytest.raises(CouncilParseError):
        parse_synth_output(payload)


def test_synthesis_retries_once_then_succeeds():
    scripted = Scripted([reply("not json"), reply(SYNTH_OK)])
    answers = [answer("a/m"), answer("b/m")]
    syn = asyncio.run(synthesize(client_for(scripted), make_task(), "s/m", 1, answers, random.Random(0)))
    assert syn.ok and syn.answer == "Merged Acme briefing."
    assert len(scripted.requests) == 2
    assert "valid JSON only" in scripted.requests[1]["messages"][-1]["content"]
    assert syn.cost == pytest.approx(0.04)
    req = scripted.requests[0]
    assert req["model"] == "s/m" and req["max_tokens"] == 4000 and req["temperature"] == 0.2
    assert "plugins" not in req["extra_body"]  # the synthesizer gets no web search


def test_synthesis_gives_up_after_one_retry():
    scripted = Scripted([reply("nope"), reply("still nope")])
    syn = asyncio.run(synthesize(client_for(scripted), make_task(), "s/m", 1,
                                 [answer("a/m"), answer("b/m")], random.Random(0)))
    assert not syn.ok and "invalid JSON" in syn.error


def test_synthesis_needs_two_answers():
    scripted = Scripted([])
    syn = asyncio.run(synthesize(client_for(scripted), make_task(), "s/m", 1, [answer("a/m")], random.Random(0)))
    assert not syn.ok and "at least 2" in syn.error and scripted.requests == []


def test_synth_prompt_is_anonymized_and_has_sources():
    answers = [answer("secret/model", text="Acme raised $5M.",
                      citations=[{"url": "https://ex.com", "title": "Ex", "content": "Acme raised $5M"}])]
    prompt = build_synth_prompt(make_task(), assign_labels(answers, random.Random(0)), web=True)
    assert "secret/model" not in prompt
    assert "https://ex.com" in prompt and "Brief on Acme" in prompt


# --- council answer: cost, latency, sources --------------------------------

def test_council_cost_latency_and_union_of_sources():
    c1 = {"url": "https://a.com", "title": "A"}
    c2 = {"url": "https://b.com", "title": "B"}
    contestants = [
        answer("a/m", cost=0.01, latency=12.0, citations=[c1]),
        answer("b/m", cost=0.03, latency=30.0, citations=[c1, c2]),
        CallResult(model="c/m", run=1, ok=False, error="boom", cost=0.005, latency=None),
        answer("a/m", run=2, cost=0.5, latency=99.0),  # other run: must not count
    ]
    syn = Synthesis(run=1, ok=True, answer="Merged.", cost=0.02, latency=8.0)
    row = council_result(syn, "s/m", contestants)
    assert row.model == council_name("s/m") == "council (s/m)"
    assert row.cost == pytest.approx(0.01 + 0.03 + 0.005 + 0.02)
    assert row.latency == pytest.approx(30.0 + 8.0)
    assert row.citations == [c1, c2]
    assert union_citations(contestants[:2]) == [c1, c2]


def test_failed_synthesis_gives_failed_council_row():
    syn = Synthesis(run=1, ok=False, error="Returned invalid JSON")
    row = council_result(syn, "s/m", [answer("a/m")])
    assert not row.ok and row.error == "Returned invalid JSON" and row.latency is None


def test_council_answer_is_judged_as_an_anonymous_extra_answer():
    contestants = [answer("a/m"), answer("b/m"), answer("c/m")]
    council = council_result(Synthesis(run=1, ok=True, answer="Combined Acme briefing.", latency=1.0),
                             "s/m", contestants)
    everyone = contestants + [council]
    labeled = assign_labels(everyone, random.Random(3))
    prompt = build_judge_prompt(make_task(), labeled, web=True)
    assert "council" not in prompt.lower() and "synthes" not in prompt.lower() and "merge" not in prompt.lower()
    assert "Combined Acme briefing." in prompt

    scores = {label: {"scores": {"grounding": 5 + i, "usefulness": 5}, "unsupported_claims": [],
                      "rationale": f"r{label}"} for i, label in enumerate(labeled)}
    scripted = Scripted([reply(json.dumps(scores))])
    j = asyncio.run(judge_run(client_for(scripted), make_task(), "j/m", 1, everyone, random.Random(3)))
    assert j.ok and set(j.scores) == {"a/m", "b/m", "c/m", "council (s/m)"}


# --- synthesis guess -------------------------------------------------------

def test_parse_guess_normalizes_to_100():
    text = json.dumps({"A": {"probability": 60, "reason": "covers everything"},
                       "B": {"probability": 20, "reason": "x"},
                       "C": {"probability": 22, "reason": "y"}})  # sums to 102: allowed, normalized
    parsed = parse_guess_output(text, ["A", "B", "C"])
    assert sum(e["probability"] for e in parsed.values()) == pytest.approx(100)
    assert parsed["A"]["probability"] == pytest.approx(60 * 100 / 102)


@pytest.mark.parametrize("payload", [
    json.dumps({"A": {"probability": 50, "reason": "x"}, "B": {"probability": 20, "reason": "y"}}),  # sums to 70
    json.dumps({"A": {"probability": 120, "reason": "x"}, "B": {"probability": -20, "reason": "y"}}),
    json.dumps({"A": {"probability": 100, "reason": ""}, "B": {"probability": 0, "reason": "y"}}),
    json.dumps({"A": {"probability": 100, "reason": "x"}}),  # missing B
    "A is the merge",
])
def test_parse_guess_rejects_malformed(payload):
    with pytest.raises(CouncilParseError):
        parse_guess_output(payload, ["A", "B"])


def test_guess_maps_probabilities_back_to_models_and_never_sees_scores():
    everyone = [answer("a/m"), answer("b/m"), answer("council (s/m)", text="Merged.")]
    rng = random.Random(5)
    labeled = assign_labels(everyone, random.Random(5))
    probs = {label: (80 if r.model == "council (s/m)" else 10) for label, r in labeled.items()}
    body = {label: {"probability": p, "reason": f"why {label}"} for label, p in probs.items()}
    scripted = Scripted([reply("oops"), reply(json.dumps(body))])

    g = asyncio.run(guess_synthesis(client_for(scripted), make_task(), "j/m", 1, everyone, rng))
    assert g.ok
    assert g.probabilities["council (s/m)"] == pytest.approx(80)
    assert g.probabilities["a/m"] == pytest.approx(10)
    council_label = next(lbl for lbl, m in g.label_map.items() if m == "council (s/m)")
    assert g.reasons["council (s/m)"] == f"why {council_label}"
    prompt = scripted.requests[0]["messages"][1]["content"]
    assert "council" not in prompt and "score" not in prompt.lower()
    assert len(scripted.requests) == 2  # one retry after the malformed reply


def test_table_has_synthesis_columns():
    everyone = [answer("a/m"), answer("council (s/m)")]
    g = SimpleNamespace(probabilities={"a/m": 30.0, "council (s/m)": 70.0},
                        reasons={"a/m": "terse", "council (s/m)": "covers every section"})
    rows = table_rows(summarize(everyone, ["a/m", "council (s/m)"], [], [g]), council=True)
    council_row = next(r for r in rows if r[0] == "council (s/m)")
    assert council_row[-2:] == ["70%", "covers every section"]


# --- rules -----------------------------------------------------------------

def _write_task(tmp_path, synthesizer):
    body = (
        "name: t\nuser: hi\nmodels: [a/m]\njudge: j/m\n"
        + (f"synthesizer: {synthesizer}\n" if synthesizer else "")
        + "rubric:\n  - {name: x, weight: 1.0}\n"
    )
    path = tmp_path / "t.yaml"
    path.write_text(body)
    return path


def test_synthesizer_equal_to_judge_is_an_error(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    result = CliRunner().invoke(app, ["council", str(_write_task(tmp_path, "j/m"))])
    assert result.exit_code == 1
    assert "judge would be scoring its own" in " ".join(result.output.split())


def test_council_requires_a_synthesizer(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    result = CliRunner().invoke(app, ["council", str(_write_task(tmp_path, None))])
    assert result.exit_code == 1 and "synthesizer" in result.output


def test_synthesizer_gets_a_minimum_token_budget_and_empty_reply_is_not_retried():
    task = make_task()
    task.max_tokens = 1000
    scripted = Scripted([{"choices": [{"message": {"content": ""}}], "usage": {"completion_tokens": 4000, "cost": 0}}])
    syn = asyncio.run(synthesize(client_for(scripted), task, "s/m", 1, [answer("a/m"), answer("b/m")], random.Random(0)))
    assert scripted.requests[0]["max_tokens"] == 4000
    assert not syn.ok and "Empty reply" in syn.error and len(scripted.requests) == 1
