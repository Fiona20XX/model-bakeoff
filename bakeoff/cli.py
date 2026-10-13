"""Command-line interface: `bakeoff run`, `bakeoff council`, and `bakeoff models`."""

from __future__ import annotations

import asyncio
import random
from dataclasses import asdict
from datetime import datetime
from typing import List, Optional

import httpx
import typer
from rich.console import Console
from rich.markup import escape
from rich.table import Table

from .openrouter import (
    ConfigError,
    fetch_models,
    filter_models,
    get_api_key,
    is_specialist,
    free_candidates,
)
from .council import Guess, Synthesis, council_name, council_result, guess_synthesis, synthesize
from .judge import Judgment, judge_run
from .report import print_summary, summarize
from .results import build_report, build_results, results_dir, save_results
from .runner import CallResult, Skipped, make_client, run_contestants, run_free_with_backfill
from .task import TaskError, load_task, parse_vars

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Compare LLMs on your own task: quality, cost, and latency, via OpenRouter.",
)
console = Console(emoji=False)  # model IDs like "x:free:" must not turn into emoji

FREE_MODEL_LIMIT = 4


@app.callback()
def main():
    """Compare LLMs on your own task: quality, cost, and latency, via OpenRouter."""


def _price(value: float | None) -> str:
    if value is None:
        return "?"
    if value < 0:
        return "varies"
    if value == 0:
        return "free"
    if value < 0.01:
        return f"${value:.4f}"
    return f"${value:,.2f}"


TASK_ARG = typer.Argument(..., help="Path to a task YAML file.")
VAR_OPT = typer.Option([], "--var", help="Fill a {{var:name}} placeholder: --var name=value. Repeatable.")
RUNS_OPT = typer.Option(None, "--runs", min=1, help="Repeat each model N times (default: task file, else 1).")
FREE_OPT = typer.Option(False, "--free", help="Ignore the task's models and auto-pick up to 4 free models.")
NO_WEB_OPT = typer.Option(False, "--no-web", help="Disable web search for this run.")
NO_JUDGE_OPT = typer.Option(False, "--no-judge", help="Skip scoring; only collect answers, cost, and latency.")


def _fail(message: str) -> None:
    console.print(f"[red]Error:[/red] {escape(message)}")
    raise typer.Exit(1)


def _load(task_file: str, var: list[str]):
    try:
        return load_task(task_file, parse_vars(var)), get_api_key()
    except (TaskError, ConfigError) as e:
        _fail(str(e))


def _fan_out(
    api_key: str, task, *, free: bool, n_runs: int, web: bool, exclude: list[str], label: str
) -> tuple[list[CallResult], list[str], list[Skipped]]:
    """Pick the contestants and run them. Shared by `run` and `council`."""
    candidates: list[str] = []
    if free:
        try:
            candidates = [m for m in free_candidates(fetch_models()) if m not in exclude]
        except httpx.HTTPError as e:
            console.print(f"[red]Could not fetch free models from OpenRouter:[/red] {escape(str(e))}")
            raise typer.Exit(1)
    elif task.models:
        candidates = task.models
    if not candidates:
        _fail("no models to run. Add some under 'models:' or use --free.")

    count = f"up to {FREE_MODEL_LIMIT} free model(s)" if free else f"{len(candidates)} model(s)"
    console.print(f"[bold]{task.name}[/bold] ({label}): {count} x {n_runs} run(s), web search {'on' if web else 'off'}")
    if not free:
        for m in candidates:
            console.print(f"  - {m}")

    def on_done(r: CallResult) -> None:
        if r.ok:
            console.print(f"  [green]done[/green] {r.model} (run {r.run}) in {r.latency:.1f}s")
        else:
            console.print(f"  [red]failed[/red] {r.model} (run {r.run}): {escape(str(r.error))}")

    def on_skip(s: Skipped) -> None:
        console.print(f"  [yellow]skipped[/yellow] {s.model}: {escape(str(s.error))}")

    async def go() -> tuple[list[CallResult], list[str], list[Skipped]]:
        async with make_client(api_key) as client:
            if free:
                return await run_free_with_backfill(
                    client, task, candidates, n_runs, web, FREE_MODEL_LIMIT, on_done, on_skip
                )
            results = await run_contestants(client, task, candidates, n_runs, web, on_done)
            return results, candidates, []

    return asyncio.run(go())


def _warn(warnings: list[str], message: str) -> None:
    warnings.append(message)
    console.print(f"[yellow]Warning:[/yellow] {escape(message)}")


def _check_judge(judge: str | None) -> None:
    if judge and is_specialist(judge):
        _fail(f"judge '{judge}' looks like a coding or safety model; pick a general model.")


def _save(task, started_at, data, summaries, report_results, mode=None) -> None:
    out_dir = save_results(
        results_dir(task, started_at, mode=mode), data, build_report(data, summaries, report_results)
    )
    console.print(f"Saved [bold]{out_dir}/results.json[/bold] and [bold]{out_dir}/report.md[/bold]")


@app.command()
def run(
    task_file: str = TASK_ARG,
    var: List[str] = VAR_OPT,
    runs: Optional[int] = RUNS_OPT,
    free: bool = FREE_OPT,
    no_web: bool = NO_WEB_OPT,
    no_judge: bool = NO_JUDGE_OPT,
):
    """Run a bake-off: send the task to every model and compare the answers."""
    task, api_key = _load(task_file, var)
    judge = None if no_judge else task.judge
    _check_judge(judge)
    n_runs = runs or task.runs
    web = task.web.enabled and not no_web
    started_at = datetime.now()

    results, models_used, skipped = _fan_out(
        api_key, task, free=free, n_runs=n_runs, web=web, exclude=[judge] if judge else [], label="bake-off"
    )

    warnings: list[str] = []
    if judge and judge in models_used:
        _warn(warnings, f"The judge ({judge}) is also a contestant; models tend to prefer their own answers "
              "(self-preference bias).")

    judgments: list[Judgment] = []
    if judge:
        judgments = asyncio.run(judge_all(api_key, task, judge, results, n_runs, web))

    summaries = summarize(results, models_used, judgments)
    total_cost = sum(r.cost or 0 for r in results) + sum(j.cost or 0 for j in judgments)
    print_summary(console, summaries, f"{task.name} results", total_cost, skipped)

    data = build_results(
        task,
        started_at=started_at,
        flags={"runs": n_runs, "free": free, "web": web, "judge": not no_judge},
        judge_model=judge,
        models=models_used,
        results=results,
        judgments=judgments,
        summaries=summaries,
        skipped=skipped,
        total_cost=total_cost,
        warnings=warnings,
    )
    _save(task, started_at, data, summaries, results)


@app.command()
def council(
    task_file: str = TASK_ARG,
    var: List[str] = VAR_OPT,
    runs: Optional[int] = RUNS_OPT,
    free: bool = FREE_OPT,
    no_web: bool = NO_WEB_OPT,
    no_judge: bool = NO_JUDGE_OPT,
):
    """Council mode: merge every model's answer into one, then judge all of them blind."""
    task, api_key = _load(task_file, var)
    synthesizer = task.synthesizer
    if not synthesizer:
        _fail(f"{task_file} has no 'synthesizer:' model; council mode needs one.")
    if is_specialist(synthesizer):
        _fail(f"synthesizer '{synthesizer}' looks like a coding or safety model; pick a general model.")
    judge = None if no_judge else task.judge
    _check_judge(judge)
    if judge and judge == synthesizer:
        _fail(f"the synthesizer and the judge are both '{judge}'; the judge would be scoring its own "
              "writing. Use a different model for one of them.")
    n_runs = runs or task.runs
    web = task.web.enabled and not no_web
    started_at = datetime.now()

    exclude = [m for m in (judge, synthesizer) if m]
    results, models_used, skipped = _fan_out(
        api_key, task, free=free, n_runs=n_runs, web=web, exclude=exclude, label="council"
    )

    warnings: list[str] = []
    if judge and judge in models_used:
        _warn(warnings, f"The judge ({judge}) is also a contestant; models tend to prefer their own answers "
              "(self-preference bias).")
    if synthesizer in models_used:
        _warn(warnings, f"The synthesizer ({synthesizer}) is also a contestant, so the merge may lean "
              "toward its own answer.")

    rng = random.Random()

    async def merge() -> list[Synthesis]:
        async with make_client(api_key) as client:
            console.print(f"Synthesizing with {synthesizer}...")
            return list(await asyncio.gather(*(
                synthesize(
                    client, task, synthesizer, n,
                    [r for r in results if r.run == n and r.ok], rng, web,
                )
                for n in range(1, n_runs + 1)
            )))

    syntheses = asyncio.run(merge())
    for syn in syntheses:
        if not syn.ok:
            console.print(f"  [red]synthesis failed[/red] (run {syn.run}): {escape(str(syn.error))}")
    council_rows = [council_result(syn, synthesizer, results) for syn in syntheses]
    everyone = results + council_rows
    names = models_used + [council_name(synthesizer)]

    judgments: list[Judgment] = []
    guesses: list[Guess] = []
    if judge:
        judgments = asyncio.run(judge_all(api_key, task, judge, everyone, n_runs, web))
        guesses = asyncio.run(guess_all(api_key, task, judge, everyone, syntheses, n_runs))

    summaries = summarize(everyone, names, judgments, guesses)
    synthesis_cost = sum(s.cost or 0 for s in syntheses)
    guess_cost = sum(g.cost or 0 for g in guesses)
    total_cost = (
        sum(r.cost or 0 for r in results) + synthesis_cost
        + sum(j.cost or 0 for j in judgments) + guess_cost
    )
    first_ok = next((s for s in syntheses if s.ok), None)
    print_summary(console, summaries, f"{task.name} council results", total_cost, skipped,
                  council=True,
                  disagreements=first_ok.disagreements if first_ok else None,
                  disagreements_run=first_ok.run if first_ok else None)

    data = build_results(
        task,
        started_at=started_at,
        flags={"runs": n_runs, "free": free, "web": web, "judge": not no_judge},
        judge_model=judge,
        models=models_used,
        results=results,
        judgments=judgments,
        summaries=summaries,
        skipped=skipped,
        total_cost=total_cost,
        warnings=warnings,
        council={
            "synthesizer": synthesizer,
            "name": council_name(synthesizer),
            "synthesis_cost": synthesis_cost,
            "guess_cost": guess_cost,
            "answers": [asdict(r) for r in council_rows],
            "syntheses": [asdict(s) for s in syntheses],
            "guesses": [asdict(g) for g in guesses],
        },
    )
    _save(task, started_at, data, summaries, everyone, mode="council")


async def guess_all(
    api_key: str, task, judge: str, everyone: list[CallResult], syntheses: list[Synthesis], n_runs: int
) -> list[Guess]:
    rng = random.Random()
    guesses = []
    async with make_client(api_key) as client:
        for syn in syntheses:
            if not syn.ok:
                continue
            answers = [r for r in everyone if r.run == syn.run and r.ok]
            console.print(f"Guessing the synthesis for run {syn.run} with {judge}...")
            g = await guess_synthesis(client, task, judge, syn.run, answers, rng)
            if not g.ok:
                console.print(f"  [red]synthesis guess failed[/red]: {escape(str(g.error))}")
            guesses.append(g)
    return guesses


async def judge_all(
    api_key: str, task, judge: str, results: list[CallResult], n_runs: int, web: bool
) -> list[Judgment]:
    rng = random.Random()
    judgments = []
    async with make_client(api_key) as client:
        for run_number in range(1, n_runs + 1):
            answers = [r for r in results if r.run == run_number and r.ok]
            if not answers:
                continue
            console.print(f"Judging run {run_number} ({len(answers)} answer(s)) with {judge}...")
            j = await judge_run(client, task, judge, run_number, answers, rng, web)
            if not j.ok:
                console.print(f"  [red]judging failed[/red]: {escape(str(j.error))}")
            judgments.append(j)
    return judgments


@app.command()
def models(
    free: bool = typer.Option(False, "--free", help="Only show free models (IDs ending in :free)."),
    search: Optional[str] = typer.Option(None, "--search", help="Filter by text in the model ID or name."),
):
    """List available OpenRouter models so you can pick IDs for a task file."""
    try:
        found = filter_models(fetch_models(), free=free, search=search)
    except httpx.HTTPError as e:
        console.print(f"[red]Could not fetch models from OpenRouter:[/red] {escape(str(e))}")
        raise typer.Exit(1)

    table = Table(title=f"OpenRouter models ({len(found)})")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Context", justify="right")
    table.add_column("Prompt $/M", justify="right")
    table.add_column("Completion $/M", justify="right")
    for m in found:
        table.add_row(
            m.id,
            f"{m.context_length:,}" if m.context_length else "?",
            _price(m.prompt_price),
            _price(m.completion_price),
        )
    console.print(table)


if __name__ == "__main__":
    app()
