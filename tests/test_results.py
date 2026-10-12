from datetime import datetime
from pathlib import Path

from bakeoff.judge import Judgment
from bakeoff.report import summarize
from bakeoff.results import build_report, build_results, results_dir
from bakeoff.runner import CallResult, Skipped
from bakeoff.task import Criterion, Task


def make_task():
    return Task(
        name="company_research",
        user="Brief on Stripe",
        models=["a/m", "b/m"],
        judge="j/m",
        rubric=[Criterion("grounding", 1.0, "")],
        vars={"company": "Stripe, Inc."},
    )


def test_results_dir_includes_task_vars_and_timestamp():
    path = results_dir(make_task(), datetime(2026, 10, 12, 9, 5, 3))
    assert path == Path("results/company-research-stripe-inc-20261012-090503")


def test_report_and_results_contain_everything():
    task = make_task()
    results = [
        CallResult("a/m", 1, True, answer="Stripe does payments.", latency=2.0, cost=0.02,
                   citations=[{"url": "https://stripe.com", "title": "Stripe"}]),
        CallResult("b/m", 1, False, error="HTTP 500: boom", cost=None),
    ]
    j = Judgment(run=1, label_map={"A": "a/m"}, ok=True, cost=0.01, scores={
        "a/m": {"label": "A", "criteria": {"grounding": 8.0}, "weighted_score": 8.0,
                "unsupported_claims": ["Stripe has 1M staff"], "rationale": "Well sourced."}})
    summaries = summarize(results, ["a/m", "b/m"], [j])
    data = build_results(
        task, started_at=datetime(2026, 10, 12), flags={"runs": 1, "web": True}, judge_model="j/m",
        models=["a/m", "b/m"], results=results, judgments=[j], summaries=summaries,
        skipped=[Skipped("gated:free", "HTTP 403: nope")], total_cost=0.03, warnings=[],
    )
    assert data["skipped_models"] == [{"model": "gated:free", "error": "HTTP 403: nope"}]
    assert data["judgments"][0]["label_map"] == {"A": "a/m"}
    assert data["contestants"][0]["citations"][0]["url"] == "https://stripe.com"

    md = build_report(data, summaries, results)
    assert "| a/m | 8.0 | $0.0200 | 2.0s | 1 | 1 | 4.0 |" in md
    assert "| b/m | FAILED |" in md
    assert "Well sourced." in md and "Stripe has 1M staff" in md
    assert "### a/m" in md and "1. [Stripe](https://stripe.com)" in md
    assert "**Failed:** HTTP 500: boom" in md
    assert "`gated:free`: HTTP 403: nope" in md
