# Model Bake-off: Spec

## What it is

A small command-line tool that sends one task to several LLMs through OpenRouter, has a separate judge model score every answer against a rubric, and reports quality, cost, and latency side by side.

Choosing a model should come from an eval on your own task, not from leaderboard vibes. This tool makes that eval take one command.

The first use case is **company research**: a short, sourced briefing on any company. Any other task can be added as a new task file without code changes.

## Who it's for

Developers and PMs who need to pick a model for a specific job and want evidence on the tradeoff: is the expensive model actually better on *this* task, and by how much per dollar and per second?

## Core flow

1. User writes a task file (YAML): the prompt, the models to compare, the judge model, a scoring rubric, and whether models get web search.
2. `bakeoff run tasks/company_research.yaml --var company="Stripe"`
3. The tool sends the prompt to every contestant model concurrently.
4. For each response it records the answer text, latency (wall clock), prompt and completion tokens, cost, and any web citations.
5. It sends all answers to the judge model, anonymized and in random order, with the rubric. The judge returns structured JSON scores.
6. It prints a ranked table in the terminal and saves full results to disk.

## Requirements

### Platform
- Python 3.10+
- OpenAI Python SDK pointed at `https://openrouter.ai/api/v1`, API key read from the `OPENROUTER_API_KEY` environment variable (support a `.env` file via python-dotenv; `.env` must be in `.gitignore`)
- `rich` for terminal tables, `pyyaml` for task files, `typer` (or argparse) for the CLI
- Send `extra_body={"usage": {"include": True}}` on every request so OpenRouter returns `usage.cost` and token counts in the response
- MIT license (`LICENSE` file in the repo root)

### Task file format

```yaml
name: company_research
description: A sourced one-page briefing on a company, for meeting or interview prep.
system: |
  You are a research analyst preparing a briefing for someone about to meet this company.
  Be specific and current. Cite a source for every factual claim. If you can't find
  something, say so rather than guessing.
user: |
  Write a briefing on {{var:company}} with these sections:
  1. What they do, who buys it, and how they make money
  2. Recent news and launches (last 6 months)
  3. Funding, size, and financial signals
  4. Leadership
  5. Main competitors and how they differ
  6. Likely strategic priorities and open questions
  Keep it under 500 words.
models:
  - <model-id>
  - <model-id>
  - <model-id>
judge: <model-id>
web:
  enabled: true
  engine: exa        # same engine for every model, so the comparison is between models, not search engines
  max_results: 5
max_tokens: 1200
temperature: 0.2
runs: 1
rubric:
  - name: grounding
    weight: 0.35
    description: Factual claims are supported by the cited sources; nothing invented or unsupported.
  - name: specificity
    weight: 0.25
    description: Concrete facts (names, numbers, dates, products) rather than generic statements.
  - name: recency
    weight: 0.2
    description: Reflects current information, not stale or outdated facts.
  - name: usefulness
    weight: 0.2
    description: Would genuinely prepare someone for a meeting; strategic section shows real insight. Length is not a virtue.
```

- `{{file:path}}` placeholders are replaced with that file's contents before sending.
- `{{var:name}}` placeholders are filled from `--var name=value` on the command line. Missing variables are an error that names the variable.
- Model IDs are never hardcoded in Python. They live only in task files.

### Web search

- When `web.enabled` is true, add the web plugin to each contestant request: `extra_body={"plugins": [{"id": "web", "engine": <engine>, "max_results": <n>}]}`. Pinning the engine keeps search results comparable across models.
- Extract citations from `message.annotations` entries of type `url_citation` (url, title, and content when present). Store them with the answer.
- The judge does not get web search. It receives each answer together with its citation list, including the cited excerpts, so it can check whether claims are supported by what was retrieved.
- Web search adds a small per-request cost even on free models; it's already included in `usage.cost`.

### Commands

- `bakeoff run <task.yaml>` runs the bake-off. Flags:
  - `--var name=value` (repeatable) fills `{{var:...}}` placeholders
  - `--runs N` repeats each model N times (default from task file, else 1) and reports mean and min/max for score and latency
  - `--free` ignores the task's model list and auto-selects up to 4 currently available free models (IDs ending in `:free`, fetched from `GET /api/v1/models`). Candidates exclude coding and safety models (IDs containing `code` or `safety`) and the judge, and are ranked by context length, largest first. Some listed free models can't actually be called (for example, OpenRouter restricts some to agentic harnesses and returns 403), and the model list doesn't say which. So if a candidate's first call fails with a permanent error (a 4xx other than 429), it is skipped and the next candidate takes its slot, until there are 4 models or no candidates left. Models that fail for other reasons (429, 5xx, timeouts, empty answers) keep their slot and show as failed. Skipped models and their errors are listed in a note under the table and saved in `results.json`.
  - `--no-web` disables web search for this run (useful to measure how much search helps)
  - `--no-judge` skips scoring and only collects answers, cost, and latency
- `bakeoff models [--free] [--search TEXT]` lists available models from `GET /api/v1/models` with ID, context length, and prompt/completion price per million tokens, so the user can pick IDs for a task file.

### Judging

- Answers are labeled A, B, C... in a random order per run, so the judge cannot see model names and position bias is reduced.
- The judge prompt includes the original task, the rubric, each answer with its citations, and an explicit instruction not to reward length.
- The judge must return JSON only: for each label, a 1-10 score per rubric criterion, a list of any claims it judged unsupported by the citations, and a one-sentence rationale. Parse it strictly, and retry once with a "return valid JSON only" reminder if parsing fails.
- Weighted score = sum of criterion scores x weights, on a 0-10 scale.
- If the judge model is also in the contestant list, print a warning about self-preference bias.
- The judge can't be a coding or safety model (ID containing `code` or `safety`); the run stops with an error before any requests are sent.

### Output

Terminal table, sorted by weighted score:

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |

- Free models with no web search show cost as `free` and "Score per cent" as `n/a`.
- Below the table, print total cost of the run (contestants plus judge) and each model's one-line judge rationale.

Saved to `results/<task-name>-<var-values>-<timestamp>/`:
- `results.json`: everything, including raw answers, citations, usage objects, judge output, the label-to-model mapping, and any `--free` models skipped with their errors
- `report.md`: the ranked table, rationales, and each model's full briefing with its sources under its own heading, readable on GitHub

### Reliability

- Concurrency capped at 3 simultaneous requests (free models are limited to 20 requests per minute).
- On 429 or 5xx, back off and retry up to 3 times, honoring `retry-after` if present.
- A model that fails after retries is recorded as failed with its error message and shown in the table; one failure never crashes the run.
- With `--free`, a permanent error (4xx other than 429) on a model's first call triggers backfill with the next free candidate instead (see `--free` above).
- 90-second timeout per request (web search adds latency).

### Repo contents

```
bakeoff/                 package code
tasks/
  hello.yaml             tiny smoke-test task (short prompt, free models, no web)
  company_research.yaml  the flagship example
results/                 gitignored except one committed sample run
tests/                   unit tests with the API mocked
README.md
SPEC.md
LICENSE                  MIT
.env.example
```

### Tests

- `{{file:}}` and `{{var:}}` substitution, including the missing-variable error
- Web plugin added to requests only when enabled, with the configured engine
- Citation extraction from `url_citation` annotations
- Judge JSON parsing, including the malformed-JSON retry path
- Weighted score math
- Label shuffling maps scores back to the correct models
- A failed model call is recorded, not raised

All tests mock the API and never make network calls.

### README

- One-paragraph pitch: why model selection should be an eval, not a guess
- The initial use case: company research, and why it's a good test (it rewards current, sourced facts and punishes confident invention)
- How to use the tool for other tasks: write a new task file, with a short example
- Quickstart: clone, install, set key, run `hello.yaml`, then `company_research.yaml --var company="..."`
- A pasted table from a real run
- How judging works, including the bias controls (anonymization, shuffling, length instruction, citation checking, self-judging warning)
- A "What I learned" section left for the author to fill in with findings from real runs
- Roadmap: council mode, fallbacks, local models

## Out of scope for v1 (roadmap)

- **Council mode**: `bakeoff council <task.yaml>` reuses the same fan-out answers, then sends them to a synthesizer model that combines them into one best answer and lists where the models disagreed. Should reuse the run machinery, not duplicate it.
- **Fallbacks**: per-model fallback lists using OpenRouter's `models` array.
- **Streaming and time-to-first-token** measurement.
- **Local models** via Ollama as an additional provider.
- A web UI.

## Done means

- `bakeoff run tasks/hello.yaml --free` works end to end on a fresh clone with only an API key set
- `bakeoff run tasks/company_research.yaml --var company="Stripe"` produces a ranked table with source counts and a `report.md`
- Tests pass with `pytest`
- README quickstart works exactly as written
