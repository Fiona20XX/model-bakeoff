"""Command-line interface: `bakeoff run` and `bakeoff models`."""

from __future__ import annotations

from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.table import Table

from .openrouter import fetch_models, filter_models

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="Compare LLMs on your own task: quality, cost, and latency, via OpenRouter.",
)
console = Console()


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
def models(
    free: bool = typer.Option(False, "--free", help="Only show free models (IDs ending in :free)."),
    search: Optional[str] = typer.Option(None, "--search", help="Filter by text in the model ID or name."),
):
    """List available OpenRouter models so you can pick IDs for a task file."""
    try:
        found = filter_models(fetch_models(), free=free, search=search)
    except httpx.HTTPError as e:
        console.print(f"[red]Could not fetch models from OpenRouter:[/red] {e}")
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
