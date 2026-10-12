# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T16:16:16
- Variables: `company=Stripe`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 1
- Total cost: $0.1068 (contestants $0.0699, judge $0.0370)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| google/gemini-3.8-flash | 7.8 | $0.0235 | 29.8s | 5 | 4 | 3.3 |
| deepseek/deepseek-v4-pro | 6.5 | $0.0102 | 43.0s | 5 | 5 | 6.4 |
| anthropic/claude-sonnet-5.5 | 5.7 | $0.0363 | 18.8s | 5 | 4 | 1.6 |

## Judge rationales

- **google/gemini-3.8-flash**: Concrete, timely developments make this meeting-useful, but several financial and competitive details go beyond the supplied evidence.
- **deepseek/deepseek-v4-pro**: The briefing is specific and strategically framed, but a material valuation-multiple error and several unsupported assertions weaken its reliability.
- **anthropic/claude-sonnet-5.5**: It carefully labels estimates and information gaps, but omits verifiable recent news and leadership and gives little competitor differentiation.

## Unsupported claims

- **google/gemini-3.8-flash** (run 1): OpenAI is a Stripe customer; the cited excerpts identify other customers but do not establish this.
- **google/gemini-3.8-flash** (run 1): Stripe closed the OpenRouter acquisition in August 2026; the excerpt says it finalized a deal to acquire OpenRouter, not that the acquisition closed.
- **google/gemini-3.8-flash** (run 1): Stripe had positive net earnings in 2024 and its Revenue & Finance suite was estimated to reach a $1 billion annual run rate in 2026; neither is established by the supplied excerpts.
- **google/gemini-3.8-flash** (run 1): The specific competitor comparisons—including Adyen’s interchange-plus pricing and the named specialist competitors—are not substantiated by the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 1): OUSD is Stripe’s own stablecoin; the cited newsroom excerpt says only that OUSD is available on Stripe.
- **deepseek/deepseek-v4-pro** (run 1): A $159 billion valuation is approximately 17.9 times $5.1 billion of revenue; the calculation is approximately 31.2 times.
- **deepseek/deepseek-v4-pro** (run 1): The Dublin entity’s profit and loss figures, the estimated 2025 group revenue range, and the Revenue suite’s near-$1 billion run rate are not established by the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The claims that Marqeta offers greater customizability and Plaid has more bank integrations are not supported by the excerpts.
- **deepseek/deepseek-v4-pro** (run 1): February 2026 is presented under news from the last six months, although it falls outside that window relative to the answer’s September 2026 news.
- **anthropic/claude-sonnet-5.5** (run 1): More than 15,000 SaaS platforms use Stripe to serve more than 10 million businesses; those figures do not appear in the supplied blog excerpt.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not substantiate the claimed 102-country tax support, stablecoin-backed Visa cards, or custom stablecoins via Open Issuance.
- **anthropic/claude-sonnet-5.5** (run 1): The competitor list is attributed to Sacra, but the supplied Sacra excerpt does not identify those competitors.
- **anthropic/claude-sonnet-5.5** (run 1): The Stripe Tour New York event 'appears to be from 2025'; its year is not established by the cited excerpt.

## Answers

### google/gemini-3.8-flash

Cost: $0.0235

### 1. What They Do, Who Buys It, and How They Make Money
Stripe provides developer-first payment processing APIs and financial infrastructure [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.). Customers range from seed-stage startups to global enterprises, including Amazon, Google, Shopify, and OpenAI [forbes.com](https://www.forbes.com/companies/stripe/), [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.). 

Stripe charges merchants a standard card transaction fee (typically 2.9% + $0.30 in the US), capturing an estimated net take rate of ~0.40% after interchange and network pass-through fees [theteardown.co](https://theteardown.co/stripe). It drives margin expansion by layering software products across the transaction lifecycle—such as Stripe Billing (0.7% fee), Stripe Tax, Radar for fraud prevention, and embedded banking/issuing tools [research.contrary.com](https://research.contrary.com/company/stripe), [theteardown.co](https://theteardown.co/stripe).

### 2. Recent News and Launches (Last 6 Months)
* **PayPal Buyout Bid:** In July 2026, Stripe teamed with private equity firm Advent International on a $53 billion joint acquisition bid for PayPal [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **OpenRouter Acquisition:** In August 2026, Stripe closed a deal to acquire AI model router OpenRouter for more than $7 billion [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **Stablecoin Integrations:** In September 2026, Stripe made OUSD available on its network [stripe.com](https://stripe.com/newsroom), building out its stablecoin payment infrastructure [forbes.com](https://www.forbes.com/companies/stripe/).

### 3. Funding, Size, and Financial Signals
* **Valuation & Capital:** Raised ~$2.2 billion in venture capital from Sequoia, Founders Fund, and General Catalyst [forbes.com](https://www.forbes.com/companies/stripe/). It was valued at $159 billion in a February 2026 tender offer, up 70% from $91.5 billion in early 2025 [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **Scale:** Processed $1.9 trillion in payment volume in 2025 (34% YoY growth) [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.). 
* **Revenue:** Net revenue surpassed $5.1 billion in 2024 with positive net earnings [research.contrary.com](https://research.contrary.com/company/stripe), [theteardown.co](https://theteardown.co/stripe). Its software-based Revenue & Finance suite alone was estimated to hit a $1 billion annual run-rate in 2026 [research.contrary.com](https://research.contrary.com/company/stripe).

### 4. Leadership
* **Patrick Collison:** Co-founder and Chief Executive Officer [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **John Collison:** Co-founder and President [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).

### 5. Main Competitors and How They Differ
* **Adyen:** Stripe’s chief enterprise rival [research.contrary.com](https://research.contrary.com/company/stripe). Adyen historically targets pure enterprise unified commerce with single-platform processing and interchange-plus pricing, while Stripe started with self-serve developer APIs and moved upmarket [research.contrary.com](https://research.contrary.com/company/stripe).
* **PayPal / Braintree & Checkout.com:** Compete directly in digital wallet checkout and enterprise payment gateway processing [research.contrary.com](https://research.contrary.com/company/stripe).
* **Specialized Fintechs:** Competes against Marqeta (issuing), Plaid (financial data access), and Chargebee (subscription billing) [research.contrary.com](https://research.contrary.com/company/stripe). Stripe's advantage is providing an integrated, single-vendor ecosystem that raises customer switching costs [research.contrary.com](https://research.contrary.com/company/stripe).

### 6. Likely Strategic Priorities and Open Questions
* **AI / Agentic Commerce:** Expanding infrastructure to monetize automated AI purchasing flows following its OpenRouter acquisition and ChatGPT checkout protocol rollouts [forbes.com](https://www.forbes.com/companies/stripe/), [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **Mega-M&A Execution:** How Stripe will finance and navigate regulatory scrutiny surrounding its $53 billion bid for PayPal [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).
* **Public Market Liquidity:** Open question remains whether Stripe will finally pursue a direct listing/IPO or continue satisfying employee equity demand via secondary tenders at massive private valuations [wikipedia.org](https://en.wikipedia.org/wiki/Stripe,_Inc.).

**Sources**

1. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
2. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
3. [Stripe, Inc. - Wikipedia](https://en.wikipedia.org/wiki/Stripe,_Inc.)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Stripe — The Teardown](https://theteardown.co/stripe)

### deepseek/deepseek-v4-pro

Cost: $0.0102

**Stripe at a Glance**

**1. What they do, who buys it, and how they make money**  
Stripe sells the software and financial infastructure that lets businesses accept and move money online. Its core is a payments API (2.9% + $0.30 per US online card transaction), but the platform now spans billing, fraud detection, card issuing, embedded banking, tax, and in‑person terminals. Half the Fortune 100 and millions of startups use Stripe, from Amazon and Shopify to AI‑native companies [theteardown.co]. Revenue comes mainly from a thin ~0.4% net take rate on payment volume, layered with higher‑margin software products — for example, Billing charges 0.7% of billing volume and the Revenue suite is nearing a $1 billion run rate [research.contrary.com][theteardown.co]. Stripe also earns interchange, interest, and loan fees from Issuing, Treasury, and Capital.

**2. Recent news and launches (last 6 months)**  
- **September 30, 2026:** OUSD, Stripe’s own stablecoin, became available on the platform [stripe.com].  
- **Late 2026:** Signed a deal to acquire OpenRouter for more than $7 billion, giving Stripe an API that routes AI inference across 400+ models and a 7.5% take rate on AI‑model spending [fintechbrainfood.com].  
- **February 2026:** Reported $1.9 trillion in total volume (up 34%) and an employee tender offer that valued the company at $159 billion [research.contrary.com].

**3. Funding, size, and financial signals**  
Stripe has raised $2.2 billion from Sequoia, General Catalyst, Founders Fund, Thrive, and others [forbes.com]. The most recent valuation, a $159 billion tender, implies a ~17.9x multiple on 2024 net revenue of $5.1 billion [theteardown.co]. A Dublin entity (not the whole group) swung to a $102 million pre‑tax profit in 2024 after a $1.2 billion loss the prior year, signaling a turn toward profitability [theteardown.co]. Analysts estimate 2025 group net revenue of $6.93–$8.6 billion, driven by volume growth and software attach [research.contrary.com][theteardown.co].

**4. Leadership**  
Stripe remains founder‑led: Patrick Collison (CEO) and John Collison (President). Steffan Tomlinson, CFO since 2023, previously held finance chief roles at Confluent, Google Cloud, and Palo Alto Networks — a hire widely seen as IPO‑readiness scaffolding [theteardown.co].

**5. Main competitors and how they differ**  
- **Payments:** Adyen (strong in enterprise, unified global platform) and PayPal/Braintree (broad consumer acceptance) [research.contrary.com].  
- **Issuing:** Marqeta offers greater customizability, but Stripe’s Issuing is deeply integrated with its payments stack.  
- **Financial connections:** Plaid has more bank integrations, while Stripe’s Financial Connections is far smaller.  
Stripe differentiates by bundling payments, billing, fraud, issuing, and now stablecoins/AI in a single developer‑first stack, whereas competitors often excel in narrower slices.

**6. Likely strategic priorities and open questions**  
Priorities center on capturing the AI and stablecoin economy — the OpenRouter acquisition and OUSD launch let Stripe own both sides of AI companies’ P&L and programmable money movement. The longstanding land‑and‑expand motion also continues, pushing Billing, Tax, and Revenue tools to boost take rates. Open questions: Can stablecoin‑based payments and AI‑agent commerce achieve material scale without eroding the core payment margin? Will the recent profitability hold as R&D spend ramps? And with a CFO recruited from public‑company environments, is an IPO now firmly on the horizon?

**Sources**

1. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
2. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
3. [Stripe — The Teardown](https://theteardown.co/stripe)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Why Stripe Is Buying OpenRouter for $7bn \| Brainfood](https://www.fintechbrainfood.com/p/stripe-buying-ai)

### anthropic/claude-sonnet-5.5

Cost: $0.0363

# Stripe briefing (as of 2026-10-12)

## 1. What they do, who buys it, how they make money
Stripe is building an end-to-end commerce platform. Payments is the core, with card issuing, Treasury, Terminal, Capital and Atlas layered on ([sacra.com](https://sacra.com/c/stripe/)). Buyers range from online businesses to platforms. More than 15,000 SaaS platforms use Stripe to offer payments and financial services to more than 10 million businesses ([stripe.com](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)).

**Monetization:** The US headline rate is 2.9% + $0.30 per card charge, but Stripe's net take rate is estimated at about 0.4% ([theteardown.co](https://theteardown.co/stripe)). Higher-margin products sit on top: Billing at 0.7% of billing volume, Connect at 0.25% plus fees, and Issuing, Treasury and Capital ([theteardown.co](https://theteardown.co/stripe)).

## 2. Recent news and launches
**Gap:** I found nothing dated within the last 6 months (roughly April to October 2026). The most recent items below are older, so check for newer news before the meeting.
- **Stripe Tour New York:** More than 40 products and features were announced. The event is undated in the source, but it appears to be from 2025.
  - **Agentic commerce:** The Agentic Commerce Protocol, co-developed with OpenAI, and Shared Payment Tokens, which power Instant Checkout in ChatGPT.
  - **AI billing:** Billing for LLM tokens and hybrid pricing models.
  - **Stablecoins:** Bridge and Privy offerings, including stablecoin-backed Visa cards and custom stablecoins via Open Issuance.
  - **Tax:** Support for 102 countries for physical goods ([stripe.com](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)).

## 3. Funding, size, financial signals
- **Revenue:** Sacra estimates $6.8B in 2025, up 33% from $5.1B, with $1.2B EBITDA. Stripe confirmed it stayed profitable through 2025 ([sacra.com](https://sacra.com/c/stripe/)). These are estimates, not company-reported figures.
- **Cash:** The Information reports Stripe generated $3.2B in cash in 2025, setting up an acquisition hunt. I only saw the headline, not the article body ([theinformation.com](https://www.theinformation.com/articles/stripe-minted-3-2-billion-cash-2025-setting-acquisition-hunt)).
- **Valuation:** A February 2026 employee tender offer was launched at $159B, backed mainly by Thrive Capital, Coatue and Andreessen Horowitz. That compares with $91.5B in February 2025. Total funding is about $9.4B ([sacra.com](https://sacra.com/c/stripe/)).

## 4. Leadership
Not covered in the sources I found, so I can't verify current executives or any changes. Confirm via Stripe's website or recent press.

## 5. Main competitors and how they differ
- **Public players:** PayPal (Braintree), Adyen, Worldpay, Global Payments and Fiserv (First Data).
- **Private players:** Revolut and Checkout.com ([sacra.com](https://sacra.com/c/stripe/)).
- **Differentiation:** The sources don't compare these rivals feature by feature. Stripe's stated angle is a broad platform, with software and financial products layered on thin-margin payments ([theteardown.co](https://theteardown.co/stripe)).

## 6. Likely strategic priorities and open questions
These are inferences from the sources, not company statements.
- **Priorities:**
  - AI and agentic commerce.
  - Usage-based billing for AI companies.
  - Stablecoin and crypto infrastructure.
  - Embedded finance for platforms.
  - International tax expansion.
  - Possible acquisitions, given the cash generation.
- **Open questions:**
  - What has launched since the Tour New York announcements?
  - What are the acquisition targets?
  - Is there any IPO or liquidity plan beyond tender offers? Nothing in the sources addresses this.
  - Who is on the current leadership team?
  - How material are the stablecoin and agentic products to revenue? No figures were found.

**Sources**

1. [Stripe Business Breakdown & Founding Story - Contrary Research](https://research.contrary.com/company/stripe)
2. [All our product updates from Stripe Tour New York](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)
3. [Stripe Minted $3.2 Billion in Cash in 2025, Setting Up Acquisition Hunt](https://www.theinformation.com/articles/stripe-minted-3-2-billion-cash-2025-setting-acquisition-hunt)
4. [Stripe revenue, valuation & funding \| Sacra](https://sacra.com/c/stripe/)
5. [Stripe — The Teardown](https://theteardown.co/stripe)
