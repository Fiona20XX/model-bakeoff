"""Load task files and fill {{file:...}} and {{var:...}} placeholders."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

PLACEHOLDER = re.compile(r"\{\{\s*(file|var)\s*:\s*([^}]+?)\s*\}\}")


class TaskError(Exception):
    """A task file is missing, malformed, or references something that doesn't exist."""


@dataclass
class Criterion:
    name: str
    weight: float
    description: str


@dataclass
class WebConfig:
    enabled: bool = False
    engine: str | None = None
    max_results: int | None = None


@dataclass
class Task:
    name: str
    user: str
    models: list[str]
    judge: str | None
    rubric: list[Criterion]
    description: str = ""
    system: str | None = None
    web: WebConfig = field(default_factory=WebConfig)
    max_tokens: int | None = None
    temperature: float | None = None
    runs: int = 1
    vars: dict[str, str] = field(default_factory=dict)
    path: str = ""


def substitute(text: str, variables: dict[str, str], base_dirs: list[Path]) -> str:
    """Replace placeholders in a single pass, so inserted file contents are not re-scanned."""

    def replace(match: re.Match) -> str:
        kind, key = match.group(1), match.group(2)
        if kind == "var":
            if key not in variables:
                raise TaskError(
                    f"Missing variable '{key}'. Pass it with --var {key}=VALUE"
                )
            return variables[key]
        return _read_file(key, base_dirs)

    return PLACEHOLDER.sub(replace, text)


def _read_file(ref: str, base_dirs: list[Path]) -> str:
    candidate = Path(ref).expanduser()
    candidates = [candidate] if candidate.is_absolute() else [d / candidate for d in base_dirs]
    for path in candidates:
        if path.is_file():
            return path.read_text(encoding="utf-8")
    tried = ", ".join(str(p) for p in candidates)
    raise TaskError(f"File placeholder '{{{{file:{ref}}}}}' not found (tried: {tried})")


def parse_vars(pairs: list[str]) -> dict[str, str]:
    """Turn ['company=Stripe', ...] into a dict."""
    out: dict[str, str] = {}
    for pair in pairs:
        if "=" not in pair:
            raise TaskError(f"--var must look like name=value, got '{pair}'")
        key, value = pair.split("=", 1)
        key = key.strip()
        if not key:
            raise TaskError(f"--var is missing a name: '{pair}'")
        out[key] = value
    return out


def load_task(path: str | Path, variables: dict[str, str] | None = None) -> Task:
    """Read a task YAML file and resolve its placeholders.

    {{file:path}} is resolved relative to the current directory first, then the
    task file's directory. {{var:name}} comes from `variables` (the --var flags).
    """
    path = Path(path)
    variables = variables or {}
    if not path.is_file():
        raise TaskError(f"Task file not found: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        raise TaskError(f"Could not parse {path}: {e}") from e
    if not isinstance(data, dict):
        raise TaskError(f"{path} must be a YAML mapping")

    for key in ("name", "user"):
        if not data.get(key):
            raise TaskError(f"{path}: '{key}' is required")

    base_dirs = [Path.cwd(), path.parent.resolve()]
    system = data.get("system")
    user = substitute(str(data["user"]), variables, base_dirs)
    if system:
        system = substitute(str(system), variables, base_dirs)

    models = data.get("models") or []
    if not isinstance(models, list) or not all(isinstance(m, str) for m in models):
        raise TaskError(f"{path}: 'models' must be a list of model IDs")

    rubric = []
    for i, item in enumerate(data.get("rubric") or []):
        try:
            rubric.append(
                Criterion(
                    name=str(item["name"]),
                    weight=float(item["weight"]),
                    description=str(item.get("description", "")),
                )
            )
        except (KeyError, TypeError, ValueError) as e:
            raise TaskError(f"{path}: rubric item {i + 1} needs a name and numeric weight") from e
    if rubric:
        total = sum(c.weight for c in rubric)
        if abs(total - 1.0) > 1e-6:
            raise TaskError(f"{path}: rubric weights must sum to 1.0 (they sum to {total:g})")

    web_data = data.get("web") or {}
    if not isinstance(web_data, dict):
        raise TaskError(f"{path}: 'web' must be a mapping")
    web = WebConfig(
        enabled=bool(web_data.get("enabled", False)),
        engine=web_data.get("engine"),
        max_results=web_data.get("max_results"),
    )

    runs = data.get("runs", 1)
    if not isinstance(runs, int) or runs < 1:
        raise TaskError(f"{path}: 'runs' must be a positive integer")

    return Task(
        name=str(data["name"]),
        description=str(data.get("description", "")),
        system=system,
        user=user,
        models=models,
        judge=data.get("judge"),
        rubric=rubric,
        web=web,
        max_tokens=data.get("max_tokens"),
        temperature=data.get("temperature"),
        runs=runs,
        vars=dict(variables),
        path=str(path),
    )
