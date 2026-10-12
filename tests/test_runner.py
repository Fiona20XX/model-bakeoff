import asyncio
from types import SimpleNamespace

import httpx
import openai
import pytest

from bakeoff import runner
from bakeoff.openrouter import ModelInfo, free_candidates
from bakeoff.runner import (
    build_request,
    call_model,
    chat_with_retries,
    extract_citations,
    parse_response,
    run_free_with_backfill,
)
from bakeoff.task import Criterion, Task, WebConfig


def make_task(web=False):
    return Task(
        name="t",
        user="hello",
        system="be brief",
        models=["a/m", "b/m"],
        judge="j/m",
        rubric=[Criterion("x", 1.0, "")],
        web=WebConfig(enabled=web, engine="exa", max_results=5),
        max_tokens=100,
        temperature=0.2,
    )


def status_error(code, headers=None):
    request = httpx.Request("POST", "https://openrouter.ai/api/v1/chat/completions")
    response = httpx.Response(code, headers=headers or {}, request=request)
    return openai.APIStatusError("boom", response=response, body={"message": "boom"})


class FakeCompletions:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    async def create(self, **kwargs):
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def fake_client(outcomes):
    completions = FakeCompletions(outcomes)
    return SimpleNamespace(chat=SimpleNamespace(completions=completions)), completions


def ok_response(content="hi", annotations=None, cost=0.001):
    return {
        "choices": [{"finish_reason": "stop", "message": {"content": content, "annotations": annotations}}],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "cost": cost},
    }


async def no_sleep(_):
    return None


def test_usage_always_requested_and_no_web_plugin_when_disabled():
    req = build_request(make_task(web=False), "a/m", web=False)
    assert req["extra_body"] == {"usage": {"include": True}}
    assert req["messages"][0] == {"role": "system", "content": "be brief"}
    assert req["max_tokens"] == 100 and req["temperature"] == 0.2


def test_web_plugin_added_with_configured_engine():
    req = build_request(make_task(web=True), "a/m", web=True)
    assert req["extra_body"]["plugins"] == [{"id": "web", "engine": "exa", "max_results": 5}]
    assert req["extra_body"]["usage"] == {"include": True}


def test_no_web_flag_overrides_task():
    req = build_request(make_task(web=True), "a/m", web=False)
    assert "plugins" not in req["extra_body"]


def test_extract_citations():
    message = {
        "annotations": [
            {"type": "url_citation", "url_citation": {"url": "https://a.com", "title": "A", "content": "excerpt"}},
            {"type": "url_citation", "url_citation": {"url": "https://a.com", "title": "dup"}},
            {"type": "url_citation", "url_citation": {"url": "https://b.com"}},
            {"type": "file", "file": {}},
        ]
    }
    assert extract_citations(message) == [
        {"url": "https://a.com", "title": "A", "content": "excerpt"},
        {"url": "https://b.com", "title": ""},
    ]
    assert extract_citations({"annotations": None}) == []


def test_parse_response_records_usage_and_citations():
    ann = [{"type": "url_citation", "url_citation": {"url": "https://a.com", "title": "A"}}]
    r = parse_response("a/m", 1, ok_response("answer", ann), 1.5, 1)
    assert r.ok and r.answer == "answer" and r.cost == 0.001
    assert r.prompt_tokens == 10 and r.completion_tokens == 5
    assert r.citations == [{"url": "https://a.com", "title": "A"}]


def test_empty_answer_and_error_body_are_failures():
    empty = ok_response(content="")
    empty["choices"][0]["finish_reason"] = "length"
    r = parse_response("a/m", 1, empty, 1.0, 1)
    assert not r.ok and "length" in r.error
    r = parse_response("a/m", 1, {"error": {"message": "provider down"}, "choices": None}, 1.0, 1)
    assert not r.ok and r.error == "provider down"


def test_retries_429_then_succeeds_honoring_retry_after():
    client, completions = fake_client([status_error(429, {"retry-after": "7"}), ok_response()])
    waits = []

    async def record(seconds):
        waits.append(seconds)

    response, _, attempts = asyncio.run(chat_with_retries(client, {"model": "a/m"}, sleep=record))
    assert attempts == 2 and waits == [7.0]


def test_does_not_retry_4xx():
    client, completions = fake_client([status_error(403)])
    with pytest.raises(openai.APIStatusError):
        asyncio.run(chat_with_retries(client, {"model": "a/m"}, sleep=no_sleep))
    assert len(completions.calls) == 1


def test_failed_call_is_recorded_not_raised(monkeypatch):
    errors = [status_error(503)] * 4  # first try + 3 retries
    client, completions = fake_client(errors)
    monkeypatch.setattr(runner.asyncio, "sleep", no_sleep)
    result = asyncio.run(call_model(client, asyncio.Semaphore(1), make_task(), "a/m", 1, False))
    assert not result.ok and "503" in result.error
    assert result.attempts == 4 and len(completions.calls) == 4


def test_free_candidates_skip_specialists_and_judge():
    models = [
        ModelInfo("big/chat:free", "", 1_000_000, 0, 0),
        ModelInfo("x/coder-code:free", "", 2_000_000, 0, 0),
        ModelInfo("x/content-safety:free", "", 2_000_000, 0, 0),
        ModelInfo("judge/model:free", "", 3_000_000, 0, 0),
        ModelInfo("paid/model", "", 4_000_000, 1, 1),
        ModelInfo("small/chat:free", "", 8_000, 0, 0),
    ]
    assert free_candidates(models, judge="judge/model:free") == ["big/chat:free", "small/chat:free"]


class RoutedCompletions:
    """Answers per model: an exception to raise, or a response dict."""

    def __init__(self, by_model):
        self.by_model = by_model
        self.calls = []

    async def create(self, **kwargs):
        self.calls.append(kwargs["model"])
        outcome = self.by_model[kwargs["model"]]
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def routed_client(by_model):
    completions = RoutedCompletions(by_model)
    return SimpleNamespace(chat=SimpleNamespace(completions=completions)), completions


def test_backfill_replaces_permanent_failures(monkeypatch):
    monkeypatch.setattr(runner.asyncio, "sleep", no_sleep)
    client, completions = routed_client(
        {
            "gated:free": status_error(403),
            "a:free": ok_response("a"),
            "b:free": ok_response("b"),
            "c:free": ok_response("c"),
        }
    )
    results, used, skipped = asyncio.run(
        run_free_with_backfill(client, make_task(), ["gated:free", "a:free", "b:free", "c:free"], 1, False, limit=2)
    )
    assert used == ["a:free", "b:free"]
    assert [s.model for s in skipped] == ["gated:free"] and "403" in skipped[0].error
    assert "c:free" not in completions.calls
    assert all(r.ok for r in results)


def test_backfill_keeps_rate_limited_and_server_errors(monkeypatch):
    monkeypatch.setattr(runner.asyncio, "sleep", no_sleep)
    client, _ = routed_client(
        {"busy:free": status_error(429), "down:free": status_error(502), "spare:free": ok_response()}
    )
    results, used, skipped = asyncio.run(
        run_free_with_backfill(client, make_task(), ["busy:free", "down:free", "spare:free"], 1, False, limit=2)
    )
    assert used == ["busy:free", "down:free"] and skipped == []
    assert not any(r.ok for r in results)


def test_backfill_runs_remaining_runs_only_for_used_models(monkeypatch):
    client, completions = routed_client({"gated:free": status_error(404), "a:free": ok_response()})
    results, used, _ = asyncio.run(
        run_free_with_backfill(client, make_task(), ["gated:free", "a:free"], 3, False, limit=4)
    )
    assert used == ["a:free"]
    assert sorted(r.run for r in results) == [1, 2, 3]
    assert completions.calls.count("gated:free") == 1
