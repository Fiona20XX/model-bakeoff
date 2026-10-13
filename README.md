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
bakeoff run tasks/company_research.yaml --var company="Zilliant"
```

Results are saved to `results/<task>-<vars>-<timestamp>/` as `results.json` (everything) and `report.md` (the table, judge rationales, unsupported claims, and each model's full answer with its sources).

## A real run

`bakeoff run tasks/company_research.yaml --var company="Zilliant" --runs 2`, judged by `openai/gpt-6-sol`, web search via exa with 5 results ([full report](results/company-research-zilliant-20261012-171818/report.md)):

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 8.2 (8.2–8.2) | $0.0373 | 16.0s (15.2s–16.8s) | 5 (5–5) | 5 (4–6) | 2.2 |
| google/gemini-3.8-flash | 7.2 (6.6–7.8) | $0.0207 | 23.0s (20.3s–25.7s) | 5 (5–5) | 6 (6–7) | 3.5 |
| deepseek/deepseek-v4-pro | 6.7 (6.4–7.0) | $0.0148 | 36.5s (30.3s–42.7s) | 5 (5–5) | 8 (7–8) | 4.5 |

Total cost of run: $0.2179 (contestants $0.1455, judge $0.0724). With `--runs 2`, each cell shows the mean and then the (min–max) across runs.

## Commands

```bash
bakeoff run <task.yaml> [--var name=value ...] [--runs N] [--free] [--no-web] [--no-judge]
bakeoff council <task.yaml> [same flags as run]
bakeoff models [--free] [--search TEXT]
```

- `--var name=value` fills `{{var:name}}` placeholders. Repeatable. A missing variable is an error that names it.
- `--runs N` runs each model N times and reports mean (min–max) for score and latency.
- `--free` ignores the task's model list and picks up to 4 free models (largest context first, skipping coding and safety models and the judge). If one turns out not to be callable (a 4xx other than 429, for example a model OpenRouter restricts to agentic apps), it is skipped and the next candidate takes its place. Skipped models are listed under the table.
- `--no-web` turns off web search, to measure how much search helps.
- `--no-judge` only collects answers, cost, and latency.
- `bakeoff council` runs [council mode](#council-mode-v110): the same fan-out, then a synthesizer merges the answers and the judge scores all of them, merge included, blind.
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

### Worked example

Gemini 3.8 Flash on Zilliant, from the [run above](results/company-research-zilliant-20261012-171818/report.md):

| Run | grounding (0.35) | specificity (0.25) | recency (0.2) | usefulness (0.2) | Weighted score |
|---|---|---|---|---|---|
| 1 | 5 | 8 | 7 | 7 | 0.35·5 + 0.25·8 + 0.2·7 + 0.2·7 = **6.55** |
| 2 | 6 | 9 | 9 | 8 | 0.35·6 + 0.25·9 + 0.2·9 + 0.2·8 = **7.75** |

The table shows `7.2 (6.6–7.8)`: the mean, then the min–max across runs, rounded to one decimal. Score per cent is the mean score divided by the mean cost of one answer in cents (7.15 ÷ 2.07 ≈ 3.5). It counts the contestant's cost only, not the judge's.

### Trade-offs in this scoring

The scoring is deliberately simple. That makes it cheap and easy to read, but you should know what it doesn't do:

- **Unsupported claims are reported, not subtracted.** The "Unsupported claims" column counts the claims the judge listed. It is not part of the formula. It lowers the score only as far as the judge lowered `grounding` for them, and the judge isn't consistent about that: in the first Amazon run, Sonnet had fewer unsupported claims than DeepSeek (5 vs 6) but a lower grounding score (4 vs 5). Read the column alongside the score, not instead of it.
- **Scores are relative within a run.** The judge sees all answers together, so a 7 means "a 7 next to these other answers", not an absolute standard. Compare models within a task, not scores across different tasks.
- **Variance comes from both sides.** Every run generates a fresh answer from a fresh search, at the task's temperature. The judge runs at temperature 0, which still isn't fully deterministic. In the example above, Gemini gained 1.2 points between runs because its second answer was better on every criterion. On Chewy, DeepSeek scored 4.7 and then 6.75, because its first answer was cut off at `max_tokens`. Use `--runs` and look at the range.
- **Scores are coarse.** Each criterion is a whole number from 1 to 10, so one point of grounding moves the total by 0.35. Differences under about half a point between models are noise.
- **One judge, uncalibrated.** Anonymising, shuffling, the length instruction and the self-judging warning reduce known biases, but nothing checks the judge against a human or a second judge. Its taste becomes your ranking. Spot-check a few answers in `report.md` against your own reading.
- **The judge is part of the bill.** It reads every answer plus every retrieved excerpt, so it can be a large share of a run's cost; see the cost line under each table.

## Council mode (v1.1.0)

A bake-off tells you which model to use for a job. Council mode is for when you want the best possible answer to *this* question: it merges several models' answers into one, and measures whether the merge actually beats the individual answers.

```bash
bakeoff council tasks/company_research.yaml --var company="Zilliant"
```

It needs one extra line in the task file, the model that writes the merge:

```yaml
synthesizer: x-ai/grok-4.7
```

What happens, per run:

1. **Fan-out.** The same as `bakeoff run`: every contestant answers, with web search, retries and cost capture.
2. **Synthesis.** The answers and their sources go to the synthesizer, without model names. It writes one best answer to the original task, using only facts from the answers and their sources, and lists every point where the answers disagreed.
3. **Blind scoring of all four.** The merged answer joins the three originals in the normal judging call, labelled and shuffled like the rest, with all of the contestants' sources. The judge isn't told that one of the answers is a merge.
4. **Synthesis guess.** In a separate call after scoring, the judge sees the same answers (reshuffled) and is told that one of them is a merge. It gives each one a probability of being the merge and a short reason. It's separate so the scores stay blind: if the judge knew a merge was in the set, it might mark that answer up or down for it. Chance is 25% with three contestants.

The table gets a council row and two extra columns, **Synthesis %** and **Why (judge's guess)**, and `report.md` adds the merged answer and the disagreement list. The council row's cost is everything it took to produce it (all contestant calls plus the synthesis), so its score per cent compares fairly with the single models.

Rules: the synthesizer can't be the judge (the judge would be scoring its own writing), and you get a warning if it's also a contestant. A run needs at least two successful answers to synthesize.

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

### v1.0.0: model bake-off

Which single model writes the best company briefing, and is it worth the price? From `company_research` with `--runs 2` on four companies: two big (Amazon, Chewy) and two small (Kajabi, Zilliant). That's 24 briefings and 8 judge calls, $0.85 in total. The contestants were Claude Sonnet 5.5, Gemini 3.8 Flash and DeepSeek V4 Pro, judged by GPT-6 Sol. The full reports are in [`results/`](results/).

1. **The most expensive model won, but the cheapest one gave the most score per dollar.** Sonnet won 7 of 8 runs and averaged 7.6, against 6.7 for Gemini and 6.3 for DeepSeek. It also cost 2.9x as much as DeepSeek per briefing ($0.038 vs $0.013). That gives DeepSeek 4.8 points per cent, Gemini 3.3 and Sonnet 2.0. DeepSeek was also the slowest by far: 55s per briefing, against 25s for Gemini and 18s for Sonnet.
2. **The gap is in grounding, not detail.** All three models were about equally specific, averaging 8.3–8.6 out of 10 on specificity. They split on grounding, meaning whether claims match the retrieved sources: Sonnet averaged 6.5, and Gemini and DeepSeek 5.0 each. Sonnet's lead also roughly doubled on the small companies: 1.1 points over the next model on Kajabi and Zilliant, against 0.6 on Amazon and Chewy. That's where sources are thin and it's tempting to fill gaps.
3. **Every briefing contained claims its sources didn't back.** All 24 had between 4 and 8 claims the judge couldn't match to the model's own retrieved excerpts. The average was 4.9 for Sonnet, 5.9 for Gemini and 6.0 for DeepSeek, even though each model had 5 sources. Most were financial figures and competitor comparisons. "Unsupported" doesn't mean false, but it is what you'd need to fact-check before a meeting.
4. **Budget for the hidden costs.** The judge was 33% of the total spend ($0.28 of $0.85), because it reads every answer plus every retrieved excerpt. Reasoning tokens also count against `max_tokens`: even at 4,000, DeepSeek used up the whole budget twice and was cut off mid-briefing (Chewy and Kajabi, run 1). The Chewy one scored 4.7, the lowest of all 24 answers, against 6.75 for its complete second attempt.

### v1.1.0: council mode

_Pending: findings from `bakeoff council` runs on the same four companies._

## Roadmap

- **Fallbacks**: per-model fallback lists using OpenRouter's `models` array.
- **Local models** via Ollama as an additional provider.

## License

[MIT](LICENSE)
