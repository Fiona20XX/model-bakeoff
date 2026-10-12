# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T16:33:44
- Variables: `company=OpenRouter`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2304 (contestants $0.1518, judge $0.0786)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 7.9 (7.5–8.3) | $0.0416 | 21.1s (20.9s–21.3s) | 5 (5–5) | 6 (4–7) | 1.9 |
| deepseek/deepseek-v4-pro | 7.5 (7.1–7.9) | $0.0120 | 34.1s (29.2s–39.0s) | 5 (5–5) | 6 (5–6) | 6.3 |
| google/gemini-3.8-flash | 5.9 (5.0–6.9) | $0.0223 | 28.6s (24.7s–32.4s) | 5 (5–5) | 6 (5–7) | 2.7 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: A concrete, timely briefing that distinguishes estimates from company figures and flags conflicting metrics, though several product, pricing, and deal details exceed its supplied excerpts.
- **deepseek/deepseek-v4-pro**: B covers all six sections with useful facts, but overstates the deal’s status, introduces unsupported customers, and presents conflicting token-volume figures without explanation.
- **google/gemini-3.8-flash**: C includes some current figures but ends mid-leadership section, omitting competitors and strategic questions, while making several claims its excerpts do not support.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not establish the 5.5% credit-purchase fee, $0.80 minimum, or 5% bring-your-own-key fee.
- **anthropic/claude-sonnet-5.5** (run 1): The cited Menlo excerpt does not establish that enterprise buyers seek spend controls or that OpenRouter launched an Enterprise product.
- **anthropic/claude-sonnet-5.5** (run 1): The cited Menlo excerpt does not substantiate the listed multimodal launches.
- **anthropic/claude-sonnet-5.5** (run 1): The supplied Sacra excerpt does not substantiate the reported $10B acquisition price or Stripe’s Metronome acquisition.
- **deepseek/deepseek-v4-pro** (run 1): The sources establish 10M+ global users, not 10M+ developers, and do not identify Uber or Microsoft as customers.
- **deepseek/deepseek-v4-pro** (run 1): The cited pricing excerpt does not show the 5.5% fee.
- **deepseek/deepseek-v4-pro** (run 1): The cited Menlo excerpt does not substantiate the multimodal expansion or its listed formats.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts establish an announced Stripe deal, not a completed acquisition or that Stripe already owns OpenRouter.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not establish a planned Stripe Connect-like integration or the specific priority of substituting cheaper models without quality loss.
- **google/gemini-3.8-flash** (run 1): Sacra describes Cursor and Vercel as platforms adding routing, not as OpenRouter buyers.
- **google/gemini-3.8-flash** (run 1): The excerpts do not substantiate Enterprise-plan SLAs, SSO, or custom governance.
- **google/gemini-3.8-flash** (run 1): The supplied sources support reported talks around $10B, not an agreed $7.5B–$10B acquisition.
- **google/gemini-3.8-flash** (run 1): The excerpts do not establish $154M total funding, a $40M Series A co-led by a16z, or the stated October 2025 and April 2026 revenue figures.
- **google/gemini-3.8-flash** (run 1): The supplied excerpts do not establish Alex Atallah’s CEO title.
- **anthropic/claude-sonnet-5.5** (run 2): OpenRouter had only two account executives as of April 2026.
- **anthropic/claude-sonnet-5.5** (run 2): The enterprise plan includes SSO, SLAs, and policy enforcement.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied Contrary excerpt reports a $7.5B Stripe acquisition agreement.
- **anthropic/claude-sonnet-5.5** (run 2): OpenRouter had raised about $154M total as of May 2026, including a $40M seed and Series A at a $500M valuation in June 2025.
- **anthropic/claude-sonnet-5.5** (run 2): Contrary reports ARR of $10M in October 2025 and $50M by April 2026.
- **anthropic/claude-sonnet-5.5** (run 2): Contrary dates the Series B to May or supplies a conflicting 2025 token baseline.
- **anthropic/claude-sonnet-5.5** (run 2): Stripe, Netflix, Adobe, SAP, and Twilio use LiteLLM.
- **deepseek/deepseek-v4-pro** (run 2): Microsoft and Uber are OpenRouter customers.
- **deepseek/deepseek-v4-pro** (run 2): OpenRouter charges a flat ~5% fee on every token; the cited pricing excerpt instead specifies a 5.5% fee on credit purchases.
- **deepseek/deepseek-v4-pro** (run 2): Stripe specifically plans to use OpenRouter to manage the spread between companies’ token costs and customer pricing.
- **deepseek/deepseek-v4-pro** (run 2): The Series B occurred a year before the August 2026 acquisition.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts establish Alex Atallah’s CEO title.
- **deepseek/deepseek-v4-pro** (run 2): Stripe acquired Metronome for $1B.
- **google/gemini-3.8-flash** (run 2): OpenRouter has 8–10 million developers; the excerpts give 8M+ developers and, separately, 10M+ global users.
- **google/gemini-3.8-flash** (run 2): The cited excerpts establish enterprise SLAs and data-compliance controls.
- **google/gemini-3.8-flash** (run 2): Stripe agreed to acquire OpenRouter for $7.5B or sought the deal specifically to anchor its AI usage-based billing infrastructure; its supplied Sacra excerpt reports talks at roughly $10B.
- **google/gemini-3.8-flash** (run 2): The $40M 2025 round was a Series A led by Menlo Ventures and a16z, and total funding reached approximately $154M.
- **google/gemini-3.8-flash** (run 2): Alex Atallah was OpenSea’s CTO.
- **google/gemini-3.8-flash** (run 2): The team generated more than $2M in net revenue per employee; the cited excerpt says approximately $2M.
- **google/gemini-3.8-flash** (run 2): OpenRouter’s minimal sales overhead and a planned Stripe Metronome integration are established by the cited excerpts.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0416

#### Run 1

# OpenRouter Briefing (as of Oct 12, 2026)

## 1. What they do, who buys, how they earn
OpenRouter is a unified API and marketplace for LLMs. It started in early 2023 and claims 500+ models, 80+ providers and 10M+ users ([openrouter.ai](https://openrouter.ai/about)). Developers buy credits, call one OpenAI-compatible endpoint, and get automatic failover across providers ([openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)). Buyers include individual developers and, increasingly, enterprises that want spend controls and cheaper models for easier tasks ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).

**Revenue:** Provider pricing passes through at 0% markup. OpenRouter charges a 5.5% fee on credit purchases ($0.80 minimum) and 5% on bring-your-own-key usage ([openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)).

## 2. Recent news
- **Stripe acquisition:** Announced Aug 19, 2026. Stripe is paying $7.5B, per a person familiar with the deal: $1.5B to founders and $6B to investors ([nytimes.com](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html)). I found no source on closing status.
- **Usage shift:** Chinese open-source models have grown to 50%+ of usage, led by DeepSeek, Tencent, Xiaomi and Z.ai ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)).
- **Product direction:** Multimodal models (image, audio, embeddings, video), OpenRouter Enterprise, and smarter routing ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).

## 3. Funding, size, financials
- **Funding:** $40M from Menlo about a year before its post, then a $113M Series B at a $1.3B valuation led by CapitalG ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
- **Team:** About 50 people, per the same Menlo post.
- **Revenue:** Sacra estimates $140M annualized in July 2026, growing 29% MoM over four months. Per-token monetization has fallen ~60% as cheaper tokens dominate ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)). These are third-party estimates, not company-reported.
- **Data conflicts:** Token volume figures differ by source: ~250T/month (Sacra), 600T+/month (OpenRouter's own page), and a ~1.5 quadrillion/year run rate (Menlo, undated). Sacra also cited a ~$10B reported price, while the NYT reports $7.5B. The NYT figure is later and reflects the announced deal. Ask which metrics they use.

## 4. Leadership
- **Alex Atallah:** Founder, previously started OpenSea ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)). The NYT describes him as "a founder" ([nytimes.com](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html)).
- **Chris Clark:** COO, previously a two-time founder ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
- **Not found:** Formal CEO title and other executives. Also unknown is how leadership roles change under Stripe.

## 5. Competitors
Sacra describes the category as split into wholesale token marketplaces (OpenRouter), public gateways (Vercel), and behind-the-firewall options (Kong) ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)). Model routing is also becoming a built-in feature in Cursor, Databricks and Ramp (same source).
- **Portkey:** A governance and observability control plane that sits over keys you already hold. It is now part of Palo Alto Networks. OpenRouter owns the path to the model and holds the provider relationships ([openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)).

## 6. Strategic priorities and open questions
**Likely priorities (inferred from the sources):**
- Integrating with Stripe, pairing routing with usage-based billing. Sacra points to Stripe's Metronome acquisition.
- Enterprise spend management.
- Multimodal expansion.
- Intelligent routing.

**Questions to ask:**
- Does the deal close, and how independent will OpenRouter stay, including neutrality toward providers?
- How will margins hold as the per-token fee base shrinks?
- How exposed is the business to Chinese open-source models, now over half of usage?
- Will bundled routing from platforms like Vercel, Cursor and Databricks erode demand?

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
3. [Stripe Buys A.I. Start-Up OpenRouter for $7.5 Billion - The ...](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html)
4. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
5. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)

#### Run 2

# OpenRouter Briefing (as of 2026-10-12)

## 1. What they do, who buys, how they earn
OpenRouter, started in early 2023, calls itself the largest AI gateway: [one API to many LLMs](https://openrouter.ai/about). It routes across 70+ providers with automatic failover, and users [never hold a provider key](https://openrouter.ai/blog/insights/openrouter-vs-portkey/). Buyers are mainly developers and product/engineering teams. It is [product-led, with only two account executives as of April 2026](https://research.contrary.com/company/openrouter). Revenue comes from a [5.5% fee on credit purchases ($0.80 minimum), with provider pricing passed through at 0% markup; bring-your-own-key carries a 5% fee](https://openrouter.ai/blog/insights/openrouter-vs-portkey/). Plans are free, usage-based, and enterprise (SSO, SLAs, policy enforcement) per [Contrary](https://research.contrary.com/company/openrouter).

## 2. Recent news (last ~6 months)
- **Series B:** $113M at a $1.3B valuation, led by CapitalG ([Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
- **Reported Stripe acquisition:** [Contrary reports](https://research.contrary.com/company/openrouter) that Stripe agreed in August 2026 to acquire OpenRouter for $7.5B. I found no second source, so confirm the status before the meeting.
- **Model mix:** Chinese open-source models rose [from a small fraction to 50%+ of usage since March](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/).
- **Product expansion:** image, audio, embedding, and video models, plus an enterprise push ([Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).

## 3. Funding, size, financials
- **Funding:** about [$154M total as of May 2026](https://research.contrary.com/company/openrouter), after a $40M seed and Series A at a $500M valuation in June 2025.
- **Revenue:** Sacra estimates [$140M annualized in July 2026, growing 29% MoM over four months](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/). Contrary cites [ARR of $10M in October 2025 and $50M by April 2026](https://research.contrary.com/company/openrouter). These are third-party estimates, not company-confirmed figures.
- **Volume and team:** 8M+ developers, a ~1.5 quadrillion tokens/year run rate, and about 50 employees ([Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
- **Pricing pressure:** cheaper tokens pushed monetization per token [down ~60%](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/).
- **Source discrepancy:** Menlo says the Series B closed in "February," while Contrary says May. Contrary's 2025 token baseline also differs from Menlo's.

## 4. Leadership
- **Alex Atallah:** a [3x founder who previously started OpenSea](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). His exact title isn't stated in the sources I have.
- **Chris Clark:** COO and a 2x founder ([Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
- **Team:** remote-friendly, with a cluster in NYC. I found no other executive names.

## 5. Competitors
- **LiteLLM:** an open-source, self-hosted proxy that gives teams custom routing and keeps data in their own environment. It is used by [Stripe, Netflix, Adobe, SAP, and Twilio](https://research.contrary.com/company/openrouter). OpenRouter is a managed cloud service with simpler, model- or provider-level routing.
- **Portkey:** a [control plane for governance, guardrails, and observability that sits in front of your own provider keys, and is now part of Palo Alto Networks after a 2026 acquisition](https://openrouter.ai/blog/insights/openrouter-vs-portkey/).
- **Hyperscaler platforms:** Menlo compares OpenRouter's volume to Azure Foundry, but I found no direct competitive analysis.

## 6. Strategic priorities and open questions
**Likely priorities** (from [Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)):
- Enterprise spend management.
- Multimodal expansion.
- Observability-driven routing that finds where a cheaper model would do.

**Open questions:**
- Is the Stripe deal real, has it closed, and what does it mean for independence and neutrality?
- Can token volume outgrow falling per-token prices?
- Can a PLG motion win enterprises that need self-hosting or data control?
- Is dependence on Chinese open-source models a risk?
- How do the competing revenue and ARR figures reconcile?

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
3. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
4. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)
5. [Report: OpenRouter Business Breakdown & Founding Story ...](https://research.contrary.com/company/openrouter)

### deepseek/deepseek-v4-pro

Cost: $0.0120

#### Run 1

Here is the briefing on OpenRouter.

### 1. What they do, who buys it, and how they make money
OpenRouter is a unified interface and marketplace that lets developers access over 500 models from 80+ providers through a single API, eliminating the need to manage multiple provider keys. Its core users are over 10 million developers and enterprises, including companies like Uber and Microsoft, who use it to avoid vendor lock-in and optimize AI spending by routing prompts to the most cost-effective model for a given task [openrouter.ai](https://openrouter.ai/about), [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). The company makes money by applying a 5.5% platform fee on credit purchases, passing through the underlying provider’s token pricing with no markup [openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/).

### 2. Recent news and launches (last 6 months)
The most significant recent event is Stripe’s announced acquisition of OpenRouter for $7.5 billion in August 2026 [nytimes.com](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html). In the months leading up to the acquisition, the platform saw explosive growth driven by the adoption of Chinese open-source models, which grew from a small fraction to over 50% of all usage since March [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/). The company also expanded beyond text models to offer multimodal capabilities, including image, audio, and video models [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

### 3. Funding, size, and financial signals
Before its acquisition, OpenRouter was growing at 29% month-over-month, reaching an estimated $140 million in annualized revenue by July 2026 [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/). It processes over 600 trillion tokens monthly and recently hit a run rate of roughly 1.5 quadrillion tokens per year [openrouter.ai](https://openrouter.ai/about), [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). The company had raised a $113 million Series B at a $1.3 billion valuation and, despite its high growth, operated with a lean team of approximately 50 people, generating about $2 million in net revenue per employee [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

### 4. Leadership
OpenRouter was co-founded by Alex Atallah, a serial entrepreneur who previously co-founded the $13 billion NFT marketplace OpenSea. The COO is Chris Clark, a two-time founder with experience leading a public company [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). Following the acquisition by Stripe, the leadership’s future roles within the larger organization are not yet publicly detailed.

### 5. Main competitors and how they differ
A key competitor is Portkey, now part of Palo Alto Networks. Portkey functions as an AI control plane, adding a governance and observability layer over the provider keys a company already owns, whereas OpenRouter is a managed routing network that abstracts away the keys and provider management entirely [openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/). The two can be complementary, with users pointing Portkey at OpenRouter to combine governance with automated routing. Other competition comes from model routing features being built directly into deployment platforms like Vercel and enterprise API infrastructure like Kong [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/).

### 6. Likely strategic priorities and open questions
The acquisition by Stripe suggests OpenRouter will become a core part of Stripe’s strategy to create infrastructure for the AI economy, analogous to Stripe Connect for marketplace payments. This will likely involve tighter integration of usage-based billing for AI spending. A key priority will be advancing its intelligent routing capabilities to automatically identify where cheaper models can be substituted without quality loss [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). An open question is whether OpenRouter can maintain its model-agnostic, neutral marketplace position now that it is owned by a single, non-AI company like Stripe.

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [Stripe Buys A.I. Start-Up OpenRouter for $7.5 Billion - The ...](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html)
3. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
4. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
5. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)

#### Run 2

Here is a briefing on OpenRouter, synthesized from recent reports.

### 1. What they do, who buys it, and how they make money
OpenRouter is a unified interface and marketplace that lets developers access over 500 models from 80+ providers through a single API, eliminating the need to manage multiple vendor accounts [openrouter.ai](https://openrouter.ai/about). It automatically routes requests based on cost, uptime, or other parameters, with built-in failover. Its users range from individual developers to large enterprises like Microsoft and Uber, who use it to manage and optimize AI token spend [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). The company’s primary revenue model is a flat ~5% fee it applies to every token routed through its platform. For enterprises, it offers spend management and observability tools to control costs and intelligently route simpler tasks to cheaper models [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/), [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

### 2. Recent news and launches (last 6 months)
The most significant development is OpenRouter’s **acquisition by Stripe for $7.5 billion**, announced on August 19, 2026 [nytimes.com](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html). Stripe’s plan is to create an infrastructure for the AI economy, mirroring its payments product Stripe Connect, to help companies manage the “spread” between their token costs and their own customer pricing [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/). The company also expanded beyond text models to support image, audio, video, and embedding models, and began developing an intelligent router that can automatically identify enterprise callsites where a cheaper model would yield the same quality [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

### 3. Funding, size, and financial signals
A year before the acquisition, OpenRouter raised a $113M Series B at a $1.3B valuation, led by CapitalG [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). At the time, it had ~50 employees processing over 1.5 quadrillion tokens a year, generating roughly $2M in net revenue per employee [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/). By July 2026, just before the deal, Sacra estimated its annualized revenue hit $140M, growing 29% month-over-month, placing the $7.5B Stripe acquisition at roughly a 54x revenue multiple [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/). The deal allocates $1.5 billion to founders and $6 billion to investors [nytimes.com](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html). The platform’s growth has been fueled by Chinese open-source models, which grew from a small fraction to over 50% of usage in the last year, led by labs like DeepSeek and Tencent [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/).

### 4. Leadership
OpenRouter was co-founded by CEO **Alex Atallah**, a 3x entrepreneur who previously co-founded the $13B NFT marketplace OpenSea. COO **Chris Clark** is also a 2x former founder who previously led a public company. The ~50-person team is lean, remote-friendly, and prioritizes startup experience, with most engineers having built products from “0 to 1” [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

### 5. Main competitors and how they differ
OpenRouter directly competed with the AI control plane **Portkey** (acquired by Palo Alto Networks in 2026). The core difference is ownership: OpenRouter is a managed routing network where you buy credits and never manage provider keys, whereas Portkey is a governance layer that sits in front of a company’s own existing provider keys. Portkey is better for those who need guardrails and observability over accounts they run; OpenRouter was better for pure access and failover without infrastructure [openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/). AI gateways are also becoming embedded into platforms like Vercel and data platforms like Databricks as standard features [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/).

### 6. Likely strategic priorities and open questions
Under Stripe, OpenRouter’s priority will likely be integration into Stripe’s billing and developer ecosystem to become the financial backbone for AI companies, not just a model router. A key question is whether deep integration with Stripe’s payment and billing tools (including its $1B Metronome acquisition) will accelerate adoption or create friction for non-Stripe users. Another is how its model-agnostic routing will evolve to help enterprises automatically optimize for cost-per-unit-of-intelligence, turning model selection into a gross-margin management tool [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/), [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/).

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
3. [Stripe Buys A.I. Start-Up OpenRouter for $7.5 Billion - The ...](https://www.nytimes.com/2026/08/19/business/stripe-openrouter-ai.html)
4. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
5. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)

### google/gemini-3.8-flash

Cost: $0.0223

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
OpenRouter is a unified AI routing gateway providing an OpenAI-compatible API to access hundreds of models across 80+ providers with automatic failover, uptime optimization, and load balancing ([openrouter.ai](https://openrouter.ai/about)). 

* **Buyers:** Independent developers, AI startups, coding platforms (e.g., Cursor, Vercel), and enterprises seeking token spend controls ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)).
* **Monetization:** OpenRouter passes provider pricing through at 0% markup and takes a 5.5% platform fee on inference spend ($0.80 minimum), charges a 5% fee on Bring-Your-Own-Key (BYOK) volume, and sells an Enterprise plan with custom governance, SLAs, and SSO ([openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/), [research.contrary.com](https://research.contrary.com/company/openrouter)).

### 2. Recent News and Launches
* **Reported Stripe Acquisition:** Stripe agreed to/entered advanced talks to acquire OpenRouter for between $7.5B and $10B to pair routing infrastructure with usage-based billing ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/), [research.contrary.com](https://research.contrary.com/company/openrouter)).
* **Multimodal Expansion:** Expanded beyond text LLMs into image, speech, audio, and video inference models ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)).
* **Open-Source Model Surge:** Driven by DeepSeek, Tencent, and Xiaomi, open-source model volume grew to represent over 50% of platform traffic ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)).

### 3. Funding, Size, and Financial Signals
* **Funding:** ~$154M total raised, including a $40M Series A (co-led by a16z and Menlo Ventures) and a $113M Series B led by CapitalG at a $1.3B valuation ([research.contrary.com](https://research.contrary.com/company/openrouter)).
* **Financials:** Reached an estimated $140M annualized revenue run-rate in July 2026 (up from $10M in October 2025 and $50M in April 2026), growing ~29% MoM ([sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/), [research.contrary.com](https://research.contrary.com/company/openrouter)). 
* **Scale:** Lean team of ~50 people supporting over 8M–10M users and processing tokens at a run rate exceeding 1.5 quadrillion tokens/year ([menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/), [openrouter.ai](https://openrouter.ai/about)).

### 4. Leadership
* **Alex Atallah (Co-founder & CEO):** 3x founder

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
3. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
4. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)
5. [Report: OpenRouter Business Breakdown & Founding Story ...](https://research.contrary.com/company/openrouter)

#### Run 2

### 1. What They Do, Who Buys It, and How They Make Money
* **What they do:** OpenRouter operates a unified API gateway and marketplace for LLMs. Developers integrate a single OpenAI-compatible endpoint that intelligently routes prompts across 80+ providers and hundreds of models for optimal price, performance, and uptime [[openrouter.ai](https://openrouter.ai/about), [research.contrary.com](https://research.contrary.com/company/openrouter)].
* **Who buys it:** Over 8–10 million developers, AI startups, and enterprises seeking to avoid vendor lock-in and optimize inference costs [[openrouter.ai](https://openrouter.ai/about), [menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)].
* **Monetization:** OpenRouter passes raw provider costs through at a 0% markup and monetizes via a 5.5% platform fee on usage/credit purchases, alongside enterprise tiers offering SLA and data compliance controls [[openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/), [research.contrary.com](https://research.contrary.com/company/openrouter)].

### 2. Recent News and Launches (Last 6 Months)
* **Stripe Acquisition Talks/Agreement:** Stripe agreed/entered talks to acquire OpenRouter for $7.5B–$10B to anchor its AI usage-based billing infrastructure [[research.contrary.com](https://research.contrary.com/company/openrouter), [sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)].
* **Shift to Open-Source/Chinese Models:** Cheaper open-source models (DeepSeek, Tencent, Xiaomi) surged to over 50% of platform token volume, nearly tripling overall token throughput [[sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)].
* **Multimodal Expansion:** Expanded beyond text into image, audio (transcription/speech), embeddings, and video model routing [[menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)].

### 3. Funding, Size, and Financial Signals
* **Funding:** Raised a $113M Series B led by CapitalG at a $1.3B valuation in mid-2026, bringing total funding to ~$154M (following a $40M Series A in 2025 led by Menlo Ventures and a16z) [[research.contrary.com](https://research.contrary.com/company/openrouter)].
* **Financials:** Reached a ~1.5 quadrillion tokens/year run rate [[menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)]. Annualized revenue hit an estimated $140M in July 2026, growing 29% MoM [[sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)]. 
* **Team Size:** Extremely lean at ~50 employees (~$2M+ net revenue per employee) [[menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)].

### 4. Leadership
* **Alex Atallah (Founder):** 3x founder; previously co-founder and CTO of OpenSea [[menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)].
* **Chris Clark (COO):** 2x former founder of a public company [[menlovc.com](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)].

### 5. Main Competitors and How They Differ
* **Portkey (Palo Alto Networks):** Operates as an AI control plane where enterprises manage their own provider API keys and governance rules, whereas OpenRouter is a managed routing network where users never need to hold individual provider keys [[openrouter.ai](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)].
* **LiteLLM:** An open-source, self-hosted proxy/SDK that requires engineering teams to manage their own infrastructure and routing logic, contrasting with OpenRouter’s fully managed cloud API [[research.contrary.com](https://research.contrary.com/company/openrouter)].

### 6. Likely Strategic Priorities and Open Questions
* **Deflation vs. Volume:** As token costs drop rapidly and traffic migrates to cheap open-source models, per-token monetization has dropped ~60% [[sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)]. OpenRouter must sustain explosive volume growth to outpace declining inference prices [[research.contrary.com](https://research.contrary.com/company/openrouter)].
* **Enterprise Direct Sales:** Currently product-led with minimal sales overhead [[research.contrary.com](https://research.contrary.com/company/openrouter)]; a key priority is operationalizing enterprise go-to-market.
* **Stripe Integration:** How quickly OpenRouter will bundle with Stripe’s usage billing (Metronome) to dominate end-to-end AI billing and inference settlement [[sacra.com](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)].

**Sources**

1. [OpenRouter growing 29% MoM at $140M/year \| Sacra](https://sacra.com/research/openrouter-growing-29-mom-at-140m-year/)
2. [About - The Unified Interface For LLMs \| OpenRouter](https://openrouter.ai/about)
3. [OpenRouter vs Portkey: Routing Network vs Control Plane](https://openrouter.ai/blog/insights/openrouter-vs-portkey/)
4. [OpenRouter Now Processes More Than a Quadrillion Tokens a Year \| Menlo Ventures](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/)
5. [Report: OpenRouter Business Breakdown & Founding Story ...](https://research.contrary.com/company/openrouter)
