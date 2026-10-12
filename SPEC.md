# Model Bake-off: Spec

## What it is

A small command-line tool that sends one task to several LLMs through OpenRouter, has a separate judge model score every answer against a rubric, and reports quality, cost, and latency side by side.

Choosing a model should come from an eval on your own task, not from leaderboard vibes. This tool makes that eval take one command.

## Who it's for

Developers and PMs who need to pick a model for a specific job and want evidence on the tradeoff: is the expensive model actually better on *this* task, and by how much per dollar and per second?

## Core flow

1. User writes a task file (YAML): the prompt, the models to compare, the judge model, and a scoring rubric.
2. `bakeoff run tasks/job_fit.yaml`
3. The tool sends the prompt to every contestant model concurrently.
4. For each response it records the answer text, latency (wall clock), prompt and completion tokens, and cost.
5. It sends all answers to the judge model, anonymized and in random order, with the rubric. The judge returns structured JSON scores.
6. It prints a ranked table in the terminal and saves full results to disk.

## Requirements

### Platform
- Python 3.10+
- OpenAI Python SDK pointed at `https://openrouter.ai/api/v1`, API key read from the `OPENROUTER_API_KEY` environment variable (support a `.env` file via python-dotenv; `.env` must be in `.gitignore`)
- `rich` for terminal tables, `pyyaml` for task files, `typer` (or argparse) for the CLI
- Send `extra_body={"usage": {"include": True}}` on every request so OpenRouter returns `usage.cost` and token counts in the response

### Task file format

```yaml
name: job_fit
description: Score how well a resume fits a job description and name the top gaps.
system: |
  You are an expert technical recruiter...
user: |
  JOB DESCRIPTION:
  {{file:examples/job_description.md}}

  RESUME:
  {{file:examples/resume.md}}

  Return a fit score from 1-10, the three biggest gaps, and a one-sentence positioning angle.
models:
  - <model-id>
  - <model-id>
  - <model-id>
judge: <model-id>
max_tokens: 800
temperature: 0.2
runs: 1
rubric:
  - name: accuracy
    weight: 0.4
    description: Claims are grounded in the provided JD and resume; nothing invented.
  - name: insight
    weight: 0.4
    description: Identifies non-obvious gaps and a sharp positioning angle.
  - name: concision
    weight: 0.2
    description: Delivers the answer without padding. Length is not a virtue.
```

- `{{file:path}}` placeholders are replaced with that file's contents before sending.
- Model IDs are never hardcoded in Python. They live only in task files.

### Commands

- `bakeoff run <task.yaml>` runs the bake-off. Flags:
  - `--runs N` repeats each model N times (default from task file, else 1) and reports mean and min/max for score and latency
  - `--free` ignores the task's model list and auto-selects up to 4 currently available free models (IDs ending in `:free`, fetched from `GET /api/v1/models`)
  - `--no-judge` skips scoring and only collects answers, cost, and latency
- `bakeoff models [--free] [--search TEXT]` lists available models from `GET /api/v1/models` with ID, context length, and prompt/completion price per million tokens, so the user can pick IDs for a task file.

### Judging

- Answers are labeled A, B, C... in a random order per run, so the judge cannot see model names and position bias is reduced.
- The judge prompt includes the original task, the rubric, and an explicit instruction not to reward length.
- The judge must return JSON only: for each label, a 1-10 score per rubric criterion and a one-sentence rationale. Parse it strictly, and retry once with a "return valid JSON only" reminder if parsing fails.
- Weighted score = sum of criterion scores x weights, on a 0-10 scale.
- If the judge model is also in the contestant list, print a warning about self-preference bias.

### Output

Terminal table, sorted by weighted score:

| Model | Score | Cost | Latency | Tokens out | Score per cent |

- Free models show cost as `free` and "Score per cent" as `n/a`.
- Below the table, print total cost of the run (contestants plus judge) and each model's one-line judge rationale.

Saved to `results/<task-name>-<timestamp>/`:
- `results.json`: everything, including raw answers, usage objects, judge output, and the label-to-model mapping
- `report.md`: the ranked table, rationales, and each model's full answer under its own heading, readable on GitHub

### Reliability

- Concurrency capped at 3 simultaneous requests (free models are limited to 20 requests per minute).
- On 429 or 5xx, back off and retry up to 3 times, honoring `retry-after` if present.
- A model that fails after retries is recorded as failed with its error message and shown in the table; one failure never crashes the run.
- 60-second timeout per request.

### Repo contents

```
bakeoff/            package code
tasks/
  hello.yaml        tiny smoke-test task (short prompt, free models)
  job_fit.yaml      the flagship example
examples/
  job_description.md   fictional sample JD
  resume.md            fictional sample resume
private/            gitignored; for real personal files
results/            gitignored except one committed sample run
tests/              unit tests with the API mocked
README.md
SPEC.md
.env.example
```

Sample files in `examples/` must be fictional. Real resumes and JDs go in `private/`, which is gitignored.

### Tests

- Placeholder substitution in task files
- Judge JSON parsing, including the malformed-JSON retry path
- Weighted score math
- Label shuffling maps scores back to the correct models
- A failed model call is recorded, not raised

All tests mock the API and never make network calls.

### README

- One-paragraph pitch: why model selection should be an eval, not a guess
- Quickstart: clone, install, set key, run `hello.yaml`, then `job_fit.yaml`
- A screenshot or pasted table from a real run
- How judging works, including the bias controls (anonymization, shuffling, length instruction, self-judging warning)
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
- `bakeoff run tasks/job_fit.yaml` produces a ranked table and a `report.md`
- Tests pass with `pytest`
- README quickstart works exactly as written
