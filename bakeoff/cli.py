"""Command-line interface: `bakeoff run` and `bakeoff models`."""

from __future__ import annotations

import asyncio
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
from .report import print_summary, summarize
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


@app.command()
def run(
    task_file: str = typer.Argument(..., help="Path to a task YAML file."),
    var: List[str] = typer.Option([], "--var", help="Fill a {{var:name}} placeholder: --var name=value. Repeatable."),
    runs: Optional[int] = typer.Option(None, "--runs", min=1, help="Repeat each model N times (default: task file, else 1)."),
    free: bool = typer.Option(False, "--free", help="Ignore the task's models and auto-pick up to 4 free models."),
    no_web: bool = typer.Option(False, "--no-web", help="Disable web search for this run."),
    no_judge: bool = typer.Option(False, "--no-judge", help="Skip scoring; only collect answers, cost, and latency."),
):
    """Run a bake-off: send the task to every model and compare the answers."""
    try:
        task = load_task(task_file, parse_vars(var))
        api_key = get_api_key()
    except (TaskError, ConfigError) as e:
        console.print(f"[red]Error:[/red] {escape(str(e))}")
        raise typer.Exit(1)

    judge = None if no_judge else task.judge
    if judge and is_specialist(judge):
        console.print(f"[red]Error:[/red] judge '{judge}' looks like a coding or safety model; pick a general model.")
        raise typer.Exit(1)

    n_runs = runs or task.runs
    web = task.web.enabled and not no_web

    candidates: list[str] = []
    if free:
        try:
            candidates = free_candidates(fetch_models(), judge=judge)
        except httpx.HTTPError as e:
            console.print(f"[red]Could not fetch free models from OpenRouter:[/red] {escape(str(e))}")
            raise typer.Exit(1)
    elif task.models:
        candidates = task.models
    if not candidates:
        console.print("[red]Error:[/red] no models to run. Add some under 'models:' or use --free.")
        raise typer.Exit(1)

    if free:
        console.print(
            f"[bold]{task.name}[/bold]: up to {FREE_MODEL_LIMIT} free model(s) x {n_runs} run(s), "
            f"web search {'on' if web else 'off'}"
        )
    else:
        console.print(
            f"[bold]{task.name}[/bold]: {len(candidates)} model(s) x {n_runs} run(s), "
            f"web search {'on' if web else 'off'}"
        )
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

    results, models_used, skipped = asyncio.run(go())
    summaries = summarize(results, models_used)
    total_cost = sum(r.cost or 0 for r in results)
    if judge:
        console.print("[yellow]Judging is not implemented yet (milestone 3); showing answers without scores.[/yellow]")
    print_summary(console, summaries, f"{task.name} results", total_cost, skipped)


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
