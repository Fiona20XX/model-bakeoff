"""Summarize results per model and render the terminal table."""

from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean

from rich.console import Console
from rich.markup import escape
from rich.table import Table

from .runner import CallResult, Skipped


@dataclass
class ModelSummary:
    model: str
    runs: int
    ok_runs: int
    latencies: list[float] = field(default_factory=list)
    costs: list[float] = field(default_factory=list)
    sources: list[int] = field(default_factory=list)
    scores: list[float] = field(default_factory=list)
    unsupported: list[int] = field(default_factory=list)
    rationales: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    synth_probs: list[float] = field(default_factory=list)  # council mode: judge's guess, 0-100
    synth_reasons: list[str] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return self.ok_runs == 0

    @property
    def mean_score(self) -> float | None:
        return mean(self.scores) if self.scores else None

    @property
    def mean_cost(self) -> float | None:
        return mean(self.costs) if self.costs else None

    @property
    def is_free(self) -> bool:
        return bool(self.costs) and all(c == 0 for c in self.costs)

    @property
    def score_per_cent(self) -> float | None:
        score, cost = self.mean_score, self.mean_cost
        if score is None or not cost:
            return None
        return score / (cost * 100)


def summarize(
    results: list[CallResult],
    models: list[str],
    judgments: list | None = None,
    guesses: list | None = None,
) -> list[ModelSummary]:
    """One row per model. `judgments` is a list of judge.Judgment (one per run);
    `guesses` (council mode) a list of council.Guess."""
    summaries = []
    for model in models:
        rows = [r for r in results if r.model == model]
        s = ModelSummary(model=model, runs=len(rows), ok_runs=sum(r.ok for r in rows))
        for r in rows:
            if r.cost is not None:
                s.costs.append(r.cost)
            if r.ok:
                if r.latency is not None:
                    s.latencies.append(r.latency)
                s.sources.append(len(r.citations))
            elif r.error:
                s.errors.append(r.error)
        for j in judgments or []:
            entry = j.scores.get(model)
            if entry:
                s.scores.append(entry["weighted_score"])
                s.unsupported.append(len(entry["unsupported_claims"]))
                s.rationales.append(entry["rationale"])
        for g in guesses or []:
            if model in g.probabilities:
                s.synth_probs.append(g.probabilities[model])
                s.synth_reasons.append(g.reasons[model])
        summaries.append(s)
    return summaries


def sort_summaries(summaries: list[ModelSummary]) -> list[ModelSummary]:
    """Best score first; unscored after scored; failures last. Stable otherwise."""
    def key(s: ModelSummary):
        score = s.mean_score
        return (s.failed, score is None, -(score or 0))

    return sorted(summaries, key=key)


def _spread(values: list[float], fmt: str) -> str:
    if not values:
        return "—"
    if len(values) == 1:
        return fmt.format(values[0])
    return f"{fmt.format(mean(values))} ({fmt.format(min(values))}–{fmt.format(max(values))})"


def format_cost(s: ModelSummary) -> str:
    if s.mean_cost is None:
        return "?"
    if s.is_free:
        return "free"
    return f"${s.mean_cost:.4f}"


def format_score_per_cent(s: ModelSummary) -> str:
    if s.is_free:
        return "n/a"
    value = s.score_per_cent
    return "—" if value is None else f"{value:.1f}"


def format_synth_prob(s: ModelSummary) -> str:
    return f"{mean(s.synth_probs):.0f}%" if s.synth_probs else "—"


def table_rows(summaries: list[ModelSummary], council: bool = False) -> list[list[str]]:
    rows = []
    for s in sort_summaries(summaries):
        if s.failed:
            row = [s.model, "FAILED", format_cost(s), "—", "—", "—", "—"]
        else:
            row = [
                s.model,
                _spread(s.scores, "{:.1f}"),
                format_cost(s),
                _spread(s.latencies, "{:.1f}s"),
                _spread([float(x) for x in s.sources], "{:.0f}") if s.sources else "0",
                _spread([float(x) for x in s.unsupported], "{:.0f}"),
                format_score_per_cent(s),
            ]
        if council:
            row += [format_synth_prob(s), s.synth_reasons[0] if s.synth_reasons else "—"]
        rows.append(row)
    return rows


HEADERS = ["Model", "Score", "Cost", "Latency", "Sources", "Unsupported claims", "Score per cent"]
COUNCIL_HEADERS = HEADERS + ["Synthesis %", "Why (judge's guess)"]


def headers(council: bool = False) -> list[str]:
    return COUNCIL_HEADERS if council else HEADERS


def render_table(summaries: list[ModelSummary], title: str, council: bool = False) -> Table:
    table = Table(title=title)
    cols = headers(council)
    for i, h in enumerate(cols):
        left = i == 0 or h == "Why (judge's guess)"
        table.add_column(
            h,
            style="cyan" if i == 0 else None,
            justify="left" if left else "right",
            min_width=30 if h == "Why (judge's guess)" else None,
        )
    for row in table_rows(summaries, council):
        style = "red" if row[1] == "FAILED" else None
        table.add_row(*(escape(c) for c in row), style=style)
    return table


def print_summary(
    console: Console,
    summaries: list[ModelSummary],
    title: str,
    total_cost: float,
    skipped: list[Skipped] | None = None,
    council: bool = False,
    disagreements: list[str] | None = None,
    disagreements_run: int | None = None,
) -> None:
    console.print(render_table(summaries, title, council))
    if skipped:
        console.print(f"[yellow]Note:[/yellow] skipped {len(skipped)} free model(s) that can't be used, and backfilled with the next candidate:")
        for s in skipped:
            console.print(f"  [yellow]{s.model}[/yellow]: {escape(str(s.error))}")
    console.print(f"Total cost of run: [bold]${total_cost:.4f}[/bold]")
    for s in sort_summaries(summaries):
        if s.rationales:
            console.print(f"[cyan]{s.model}[/cyan]: {escape(str(s.rationales[0]))}")
        for err in dict.fromkeys(s.errors):
            console.print(f"[red]{s.model} failed:[/red] {escape(str(err))}")
    if disagreements:
        console.print(f"[bold]Where the models disagreed[/bold] (from the synthesizer, run {disagreements_run}):")
        for d in disagreements:
            console.print(f"  - {escape(d)}")
