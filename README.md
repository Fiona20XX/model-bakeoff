# model-bakeoff

Compare LLMs on your own task: quality, cost, and latency, via OpenRouter.

Picking a model from a leaderboard is picking it for someone else's task. The only number that tells you whether the expensive model is worth it is how it does on *your* prompt, against *your* definition of good, next to what it costs and how long it makes you wait. `bakeoff` turns that eval into one command: it sends the same task to several models at once, has a separate judge model score every answer blind against your rubric, and prints quality, cost, and latency side by side, so the choice comes from evidence instead of a guess.

## The first use case: company research

The flagship task is a short, sourced briefing on any company, the kind you'd read before a sales call or an interview. It makes a good test because it rewards exactly what separates models in practice: finding current facts (with web search), citing them, and saying "I couldn't find this" instead of inventing it. The judge sees each answer's citations, including the retrieved excerpts, and lists every claim the sources don't support, so confident invention costs points instead of looking impressive.

## Quickstart

```bash
git clone https://github.com/Fiona20XX/model-bakeoff.git
cd model-bakeoff
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env    # then put your key in .env: OPENROUTER_API_KEY=sk-or-...
```

Get a key at [openrouter.ai/keys](https://openrouter.ai/keys). `.env` is gitignored.

Smoke test with free models (no web search, costs nothing):

```bash
bakeoff run tasks/hello.yaml --free
```

Then the real thing (paid models plus web search, about $0.10 per run):

```bash
bakeoff run tasks/company_research.yaml --var company="Stripe"
```

Results are saved to `results/<task>-<vars>-<timestamp>/` as `results.json` (everything) and `report.md` (the table, judge rationales, unsupported claims, and each model's full answer with its sources).

## A real run

`bakeoff run tasks/company_research.yaml --var company="Stripe"`, judged by `openai/gpt-6-sol`, web search via exa with 5 results ([full report](results/company-research-stripe-20261012-161616/report.md)):

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| google/gemini-3.8-flash | 7.8 | $0.0235 | 29.8s | 5 | 4 | 3.3 |
| deepseek/deepseek-v4-pro | 6.5 | $0.0102 | 43.0s | 5 | 5 | 6.4 |
| anthropic/claude-sonnet-5.5 | 5.7 | $0.0363 | 18.8s | 5 | 4 | 1.6 |

Total cost of run: $0.1068 (contestants $0.0699, judge $0.0370).

## Commands

```bash
bakeoff run <task.yaml> [--var name=value ...] [--runs N] [--free] [--no-web] [--no-judge]
bakeoff models [--free] [--search TEXT]
```

- `--var name=value` fills `{{var:name}}` placeholders. Repeatable. A missing variable is an error that names it.
- `--runs N` runs each model N times and reports mean (min–max) for score and latency.
- `--free` ignores the task's model list and picks up to 4 free models (largest context first, skipping coding and safety models and the judge). If one turns out not to be callable (a 4xx other than 429, for example a model OpenRouter restricts to agentic apps), it is skipped and the next candidate takes its place. Skipped models are listed under the table.
- `--no-web` turns off web search, to measure how much search helps.
- `--no-judge` only collects answers, cost, and latency.
- `bakeoff models` lists model IDs, context length, and $ per million prompt/completion tokens, for picking models for a task file.

## Using it for other tasks

A task is a YAML file; no code changes needed. For example, `tasks/support_reply.yaml`:

```yaml
name: support_reply
description: Draft a reply to an angry customer ticket.
system: You are a senior support agent. Be warm, specific, and brief.
user: |
  Draft a reply to this ticket:
  {{file:private/ticket.txt}}
models:
  - anthropic/claude-haiku-5.5
  - openai/gpt-6-luna
  - google/gemini-3.8-flash
judge: openai/gpt-6-sol
web:
  enabled: false
max_tokens: 2000
temperature: 0.2
rubric:
  - name: resolution
    weight: 0.5
    description: Addresses the actual problem with a concrete next step.
  - name: tone
    weight: 0.3
    description: Calm and empathetic without grovelling.
  - name: concision
    weight: 0.2
    description: Says it in as few words as possible. Length is not a virtue.
```

- `{{file:path}}` inserts a file's contents (resolved from the current directory, then the task file's directory).
- `{{var:name}}` is filled from `--var name=value`.
- Rubric weights must add up to 1.0, so the weighted score stays on a 0-10 scale.
- `web.enabled: true` gives every contestant OpenRouter's web plugin with the same `engine` and `max_results`, so the comparison is between models, not search engines.
- Reasoning models spend part of `max_tokens` thinking before they write; leave headroom or answers come back cut off.

Find model IDs with `bakeoff models --search <text>`. Model IDs live only in task files.

## How judging works

1. Every successful answer in a run is shuffled into a random order and labelled A, B, C… The judge never sees model names, and the random order per run reduces position bias.
2. The judge prompt contains the original system and user prompts, the rubric with weights, and each answer with its citation list, including the excerpts the web search retrieved.
3. The judge is told explicitly not to reward length, to check each answer's factual claims against its cited excerpts, and to list every unsupported claim.
4. It must return JSON only: per label, a 1-10 score for each rubric criterion, a list of unsupported claims, and a one-sentence rationale. The output is parsed strictly (every label and every criterion must be present, scores must be numbers from 1 to 10). If it doesn't parse, the judge gets one retry with a "return valid JSON only" reminder; if that fails too, the run is reported unscored rather than crashing.
5. Weighted score = sum of criterion score x weight, on a 0-10 scale. Scores are mapped back from labels to models only after parsing.
6. If the judge is also one of the contestants, the run prints a self-preference bias warning (models tend to rate their own writing higher). The judge also can't be a coding or safety model.

The judge doesn't get web search itself. It checks claims against what each model actually retrieved, so "Unsupported claims" means "not backed by the model's own sources", not "false".

## Reliability

- At most 3 requests in flight (free models are limited to 20 requests per minute).
- 429s and 5xx responses are retried up to 3 times with backoff, honouring `retry-after`.
- A model that still fails is shown as FAILED with its error; one failure never stops the run.
- 90-second timeout per request (web search adds latency).

## Tests

```bash
pytest
```

All tests mock the API; none make network calls.

## What I learned

_To fill in after real runs: which models won on which tasks, whether the expensive ones earned their price, how much web search helped, and where the judge disagreed with my own reading._

## Roadmap

- **Council mode**: `bakeoff council <task.yaml>` reuses the same fan-out answers, then has a synthesizer model combine them into one best answer and list where the models disagreed.
- **Fallbacks**: per-model fallback lists using OpenRouter's `models` array.
- **Local models** via Ollama as an additional provider.

## License

[MIT](LICENSE)
