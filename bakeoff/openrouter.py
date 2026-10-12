"""OpenRouter access: API key, client, and the public model list."""

from __future__ import annotations

import os
from dataclasses import dataclass

import httpx
from dotenv import load_dotenv

BASE_URL = "https://openrouter.ai/api/v1"


class ConfigError(Exception):
    """Missing or invalid local configuration (e.g. no API key)."""


def get_api_key() -> str:
    load_dotenv()
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        raise ConfigError(
            "OPENROUTER_API_KEY is not set. Copy .env.example to .env and add your key, "
            "or export OPENROUTER_API_KEY."
        )
    return key


@dataclass
class ModelInfo:
    id: str
    name: str
    context_length: int | None
    prompt_price: float | None  # USD per million tokens
    completion_price: float | None  # USD per million tokens

    @property
    def is_free(self) -> bool:
        return self.id.endswith(":free")


def _per_million(value) -> float | None:
    try:
        return float(value) * 1_000_000
    except (TypeError, ValueError):
        return None


def parse_models(payload: dict) -> list[ModelInfo]:
    models = []
    for m in payload.get("data", []):
        pricing = m.get("pricing") or {}
        models.append(
            ModelInfo(
                id=m["id"],
                name=m.get("name", ""),
                context_length=m.get("context_length"),
                prompt_price=_per_million(pricing.get("prompt")),
                completion_price=_per_million(pricing.get("completion")),
            )
        )
    return sorted(models, key=lambda m: m.id)


def fetch_models(timeout: float = 30.0) -> list[ModelInfo]:
    """GET /api/v1/models. Works without a key; sends one if available."""
    load_dotenv()
    headers = {}
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        headers["Authorization"] = f"Bearer {key}"
    resp = httpx.get(f"{BASE_URL}/models", headers=headers, timeout=timeout)
    resp.raise_for_status()
    return parse_models(resp.json())


def filter_models(
    models: list[ModelInfo], free: bool = False, search: str | None = None
) -> list[ModelInfo]:
    out = models
    if free:
        out = [m for m in out if m.is_free]
    if search:
        needle = search.lower()
        out = [m for m in out if needle in m.id.lower() or needle in m.name.lower()]
    return out


SPECIALIST_MARKERS = ("code", "safety")


def is_specialist(model_id: str) -> bool:
    """Coding and safety-classifier models aren't general chat models; skip them as contestants or judge."""
    lowered = model_id.lower()
    return any(marker in lowered for marker in SPECIALIST_MARKERS)


def free_candidates(models: list[ModelInfo], judge: str | None = None) -> list[str]:
    """Free general-purpose models, largest context first, never the judge.

    `bakeoff run --free` tries these in order until it has up to 4 that work.
    """
    candidates = [
        m for m in models if m.is_free and not is_specialist(m.id) and m.id != judge
    ]
    candidates.sort(key=lambda m: (-(m.context_length or 0), m.id))
    return [m.id for m in candidates]
