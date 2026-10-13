"""Write results.json and report.md for a run."""

from __future__ import annotations

import json
import re
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from .judge import Judgment
from .report import ModelSummary, format_cost, headers, sort_summaries, table_rows
from .runner import CallResult, Skipped
from .task import Task


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def results_dir(task: Task, now: datetime, root: Path = Path("results"), mode: str | None = None) -> Path:
    """results/<task-name>[-<mode>]-<var-values>-<timestamp>/"""
    parts = [slugify(task.name)]
    if mode:
        parts.append(mode)
    parts += [slugify(v)[:40] for v in task.vars.values() if slugify(v)]
    parts.append(now.strftime("%Y%m%d-%H%M%S"))
    return root / "-".join(parts)


def build_results(
    task: Task,
    *,
    started_at: datetime,
    flags: dict,
    judge_model: str | None,
    models: list[str],
    results: list[CallResult],
    judgments: list[Judgment],
    summaries: list[ModelSummary],
    skipped: list[Skipped],
    total_cost: float,
    warnings: list[str],
    council: dict | None = None,
) -> dict:
    data = {
        "task": {
            "name": task.name,
            "description": task.description,
            "path": task.path,
            "vars": task.vars,
            "system": task.system,
            "user": task.user,
            "rubric": [asdict(c) for c in task.rubric],
            "web": asdict(task.web),
            "max_tokens": task.max_tokens,
            "temperature": task.temperature,
        },
        "started_at": started_at.isoformat(timespec="seconds"),
        "flags": flags,
        "models": models,
        "judge": judge_model,
        "skipped_models": [asdict(s) for s in skipped],
        "warnings": warnings,
        "total_cost": total_cost,
        "contestant_cost": sum(r.cost or 0 for r in results),
        "judge_cost": sum(j.cost or 0 for j in judgments),
        "summary": [
            {
                "model": s.model,
                "runs": s.runs,
                "ok_runs": s.ok_runs,
                "scores": s.scores,
                "mean_score": s.mean_score,
                "latencies": s.latencies,
                "costs": s.costs,
                "mean_cost": s.mean_cost,
                "sources": s.sources,
                "unsupported_claims": s.unsupported,
                "score_per_cent": s.score_per_cent,
                "rationales": s.rationales,
                "errors": s.errors,
                "synthesis_probabilities": s.synth_probs,
                "synthesis_reasons": s.synth_reasons,
            }
            for s in sort_summaries(summaries)
        ],
        "contestants": [asdict(r) for r in results],
        "judgments": [asdict(j) for j in judgments],
    }
    if council is not None:
        data["council"] = council
    return data


def _chance(council: dict) -> str:
    sizes = sorted({len(g["label_map"]) for g in council["guesses"] if g["ok"]})
    if not sizes:
        return "no guess was made"
    return "chance is " + " or ".join(f"{100 / n:.0f}%" for n in sizes) + " with " + " or ".join(
        str(n) for n in sizes) + " answers"


def _md_cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def build_report(data: dict, summaries: list[ModelSummary], results: list[CallResult]) -> str:
    task = data["task"]
    council = data.get("council")
    lines = [f"# {'Council' if council else 'Bake-off'}: {task['name']}", ""]
    if task["description"]:
        lines += [task["description"], ""]
    meta = [f"- Run: {data['started_at']}"]
    if task["vars"]:
        meta.append("- Variables: " + ", ".join(f"`{k}={v}`" for k, v in task["vars"].items()))
    meta.append(f"- Judge: `{data['judge']}`" if data["judge"] else "- Judge: none (--no-judge)")
    if council:
        meta.append(f"- Synthesizer: `{council['synthesizer']}`")
    web = task["web"]
    if data["flags"].get("web"):
        meta.append(f"- Web search: on ({web.get('engine') or 'default'} engine, max {web.get('max_results') or 'default'} results)")
    else:
        meta.append("- Web search: off")
    meta.append(f"- Runs per model: {data['flags'].get('runs')}")
    if council:
        meta.append(
            f"- Total cost: ${data['total_cost']:.4f} (contestants ${data['contestant_cost']:.4f}, "
            f"synthesis ${council['synthesis_cost']:.4f}, judge ${data['judge_cost']:.4f}, "
            f"synthesis guess ${council['guess_cost']:.4f})"
        )
    else:
        meta.append(f"- Total cost: ${data['total_cost']:.4f} (contestants ${data['contestant_cost']:.4f}, judge ${data['judge_cost']:.4f})")
    lines += meta + [""]

    for w in data["warnings"]:
        lines += [f"> **Warning:** {w}", ""]

    cols = headers(bool(council))
    lines += ["## Results", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for row in table_rows(summaries, bool(council)):
        lines.append("| " + " | ".join(_md_cell(c) for c in row) + " |")
    lines.append("")
    if council:
        lines += [
            f"The council row is the synthesizer's merge of the other answers. Its cost includes every "
            f"contestant call plus the synthesis; its latency is the slowest contestant plus the synthesis. "
            f"\"Synthesis %\" is the judge's guess, in a separate call after scoring, that the row is the "
            f"merged answer ({_chance(council)}).",
            "",
        ]

    if data["skipped_models"]:
        lines += ["Skipped free models (backfilled with the next candidate):", ""]
        lines += [f"- `{s['model']}`: {_md_cell(s['error'])}" for s in data["skipped_models"]]
        lines.append("")

    ranked = sort_summaries(summaries)
    if any(s.rationales for s in ranked):
        lines += ["## Judge rationales", ""]
        for s in ranked:
            if s.rationales:
                lines.append(f"- **{s.model}**: {s.rationales[0]}")
        lines.append("")

    claims = [(s.model, j) for j in data["judgments"] for s in ranked if s.model in j["scores"]]
    if any(j["scores"][m]["unsupported_claims"] for m, j in claims):
        lines += ["## Unsupported claims", ""]
        for model, j in claims:
            for claim in j["scores"][model]["unsupported_claims"]:
                lines.append(f"- **{model}** (run {j['run']}): {claim}")
        lines.append("")

    if council:
        for syn in council["syntheses"]:
            if syn["ok"] and syn["disagreements"]:
                lines += [f"## Where the models disagreed (run {syn['run']})", ""]
                lines += [f"- {d}" for d in syn["disagreements"]]
                lines.append("")
            elif not syn["ok"]:
                lines += [f"> Synthesis failed for run {syn['run']}: {syn['error']}", ""]
        for g in council["guesses"]:
            if not g["ok"]:
                lines += [f"> Synthesis guess failed for run {g['run']}: {g['error']}", ""]

    failed_judgments = [j for j in data["judgments"] if not j["ok"]]
    for j in failed_judgments:
        lines += [f"> Judging failed for run {j['run']}: {j['error']}", ""]

    lines += ["## Answers", ""]
    for s in ranked:
        lines += [f"### {s.model}", ""]
        lines.append(f"Cost: {format_cost(s)}")
        lines.append("")
        for r in sorted((r for r in results if r.model == s.model), key=lambda r: r.run):
            if len(set(x.run for x in results)) > 1:
                lines += [f"#### Run {r.run}", ""]
            if not r.ok:
                lines += [f"**Failed:** {r.error}", ""]
                continue
            lines += [r.answer.strip(), ""]
            if r.citations:
                lines += ["**Sources**", ""]
                for i, c in enumerate(r.citations, 1):
                    title = c.get("title") or c["url"]
                    lines.append(f"{i}. [{_md_cell(title)}]({c['url']})")
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def save_results(out_dir: Path, data: dict, report_md: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "report.md").write_text(report_md, encoding="utf-8")
    return out_dir
