# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T16:31:28
- Variables: `company=Stripe`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2087 (contestants $0.1374, judge $0.0713)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| google/gemini-3.8-flash | 7.1 (6.6–7.5) | $0.0185 | 23.0s (22.5s–23.5s) | 5 (5–5) | 4 (4–5) | 3.8 |
| anthropic/claude-sonnet-5.5 | 7.1 (6.0–8.1) | $0.0391 | 20.0s (19.8s–20.1s) | 5 (5–5) | 4 (4–5) | 1.8 |
| deepseek/deepseek-v4-pro | 6.2 (5.8–6.7) | $0.0111 | 57.4s (49.8s–64.9s) | 5 (5–5) | 5 (5–5) | 5.6 |

## Judge rationales

- **google/gemini-3.8-flash**: B covers the requested topics with useful specifics, but overstates profitability, makes unsupported comparisons, and presents older launches as recent.
- **anthropic/claude-sonnet-5.5**: A timely, meeting-ready briefing that distinguishes estimates and inferences, but several financial and competitive details are not supported by its provided excerpts.
- **deepseek/deepseek-v4-pro**: C identifies relevant strategic themes, but incorrectly calls an agreed acquisition completed and adds several financial and product details beyond the provided evidence.

## Unsupported claims

- **google/gemini-3.8-flash** (run 1): The cited excerpts establish the $159B tender valuation, its named backers, $1.9T payment volume, or the $8.6B revenue estimate and breakdown.
- **google/gemini-3.8-flash** (run 1): Stripe as a whole returned to net profitability in 2024; the claim also treats a Dublin entity's pre-tax profit as group net profit.
- **google/gemini-3.8-flash** (run 1): Stripe has superior API flexibility, payout orchestration, and AI tooling relative to PayPal/Braintree.
- **google/gemini-3.8-flash** (run 1): Periodic tender liquidity is satisfying staff.
- **google/gemini-3.8-flash** (run 1): The branded-stablecoin and ChatGPT features were launched within the last six months.
- **anthropic/claude-sonnet-5.5** (run 1): OpenRouter has billed on Stripe since January 2026.
- **anthropic/claude-sonnet-5.5** (run 1): The February 2026 tender valued Stripe at $159B, and 2025 payment volume was $1.9T, up 34%.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts establish the stated 2024 net revenue, Dublin-entity profit, and conflicting 2025 revenue estimates.
- **anthropic/claude-sonnet-5.5** (run 1): Adyen had no self-serve SMB option as of August 2025.
- **anthropic/claude-sonnet-5.5** (run 1): The OpenRouter price was about 50 times revenue.
- **deepseek/deepseek-v4-pro** (run 1): Stripe completed the OpenRouter acquisition; the excerpt says it signed a deal to buy it.
- **deepseek/deepseek-v4-pro** (run 1): OUSD is a Stripe-launched stablecoin that lets businesses issue and transact in dollar-pegged tokens as described.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts establish the $1.9T payment volume, 34% growth, $159B valuation, revenue estimates, or Dublin-entity financial figures.
- **deepseek/deepseek-v4-pro** (run 1): Adyen's market capitalization, lack of a self-serve tier, and Stripe's reach to small businesses through Shopify.
- **deepseek/deepseek-v4-pro** (run 1): Stripe earns from stablecoin and AI-commerce services, and expanding the Revenue & Finance Automation suite toward $1B is a stated focus.
- **google/gemini-3.8-flash** (run 2): The supplied excerpts do not establish the stated $1.4 trillion 2024 payment volume, $5.1 billion 2024 group net revenue, $8.6 billion revenue projection, or $1 billion Revenue & Finance Automation run rate.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not substantiate the $91.5 billion valuation or $101.9 million 2024 Dublin-entity pre-tax profit.
- **google/gemini-3.8-flash** (run 2): The detailed Adyen comparison and the claim that PayPal/Braintree and Square lack Stripe’s developer modularity and enterprise extensibility are not supported by the supplied excerpts.
- **google/gemini-3.8-flash** (run 2): The excerpts support ChatGPT checkout and Stablecoin Financial Accounts, but date those developments to 2025 or August 2025; they do not establish them as launches within the last six months.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied Stripe Tour excerpt does not establish the figures of more than 15,000 SaaS platforms and over 10 million businesses.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied Stripe Tour excerpt does not substantiate real-time credit burn-down, stablecoin-backed Visa cards, custom stablecoin issuance, or planned tax collection in 102 countries.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied Sacra excerpt does not list the competitors attributed to it.
- **anthropic/claude-sonnet-5.5** (run 2): The assertion that nothing was found from the last six months leaves the recent OpenRouter deal and September 2026 OUSD announcement present in the supplied material unaddressed.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish that the $159 billion valuation came from a February 2026 tender offer or that it was a 74% increase from a $91.5 billion February 2025 valuation.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not substantiate the dates and details given for the USDC re-enablement, Bridge acquisition, and June 2025 Privy acquisition.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not support the $5.12 billion Dublin-entity revenue, $102 million pre-tax profit, $6.93 billion 2025 group-revenue estimate, or 17.9× valuation multiple.
- **deepseek/deepseek-v4-pro** (run 2): The competitor volume, margin, take-rate, and market-position comparisons are not established by the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The claim that an IPO is a matter of when rather than if goes beyond the cited evidence.

## Answers

### google/gemini-3.8-flash

Cost: $0.0185

#### Run 1

### 1. What They Do, Who Buys, and How They Make Money
Stripe builds economic infrastructure for internet commerce, offering APIs and software for payment acceptance, billing, fraud prevention, embedded finance, and payouts [[theteardown.co](https://theteardown.co/stripe)]. 

* **Customers:** Over 2 million US businesses [[research.contrary.com](https://research.contrary.com/company/stripe)], spanning startups to enterprise giants including Amazon, Google, and Shopify [[forbes.com](https://www.forbes.com/companies/stripe/)]. Stripe powers 50% of the Fortune 100 and 78% of the Forbes AI 50 [[research.contrary.com](https://research.contrary.com/company/stripe)].
* **Monetization:** Standard US payments cost 2.9% + $0.30 per card transaction [[theteardown.co](https://theteardown.co/stripe)]. After interchange and network fees, Stripe retains a ~0.40% net take rate [[theteardown.co](https://theteardown.co/stripe)]. It layers higher-margin software on top, including Stripe Billing (0.7% volume fee), Connect, Radar, and Tax [[theteardown.co](https://theteardown.co/stripe)].

### 2. Recent News and Launches
* **AI Infrastructure:** Stripe agreed to acquire AI model router OpenRouter for over $7 billion, gaining a direct fee mechanism on token consumption across 400+ AI models [[fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)].
* **Stablecoin Expansion:** Stripe integrated OUSD support [[stripe.com](https://stripe.com/newsroom)] and rolled out tools allowing enterprises to issue their own branded stablecoins [[forbes.com](https://www.forbes.com/companies/stripe/)].
* **Agentic Commerce:** Launched native payment features that allow ChatGPT users to purchase products directly within conversations [[forbes.com](https://www.forbes.com/companies/stripe/)].

### 3. Funding, Size, and Financial Signals
* **Valuation & Funding:** Valued at $159 billion in a February 2026 employee tender offer backed by Thrive Capital, Coatue, and a16z [[research.contrary.com](https://research.contrary.com/company/stripe)]. Total equity funding exceeds $2.2 billion [[forbes.com](https://www.forbes.com/companies/stripe/)].
* **Volume & Revenue:** Handled $1.9 trillion in total payment volume in 2025 (~1.6% of global GDP) [[research.contrary.com](https://research.contrary.com/company/stripe)]. Total estimated net revenue reached ~$8.6 billion ($7.6 billion core payments, ~$1 billion Revenue suite) [[research.contrary.com](https://research.contrary.com/company/stripe)]. 
* **Profitability:** Rebounded to net profitability in 2024, generating $101.9 million in pre-tax profit via its primary Dublin entity [[theteardown.co](https://theteardown.co/stripe)].

### 4. Leadership
* **Founders:** Patrick Collison (CEO) and John Collison (President), who founded the company in 2009 [[forbes.com](https://www.forbes.com/companies/stripe/), [theteardown.co](https://theteardown.co/stripe)].
* **Finance:** Steffan Tomlinson serves as Chief Financial Officer, hired in 2023 to oversee public-readiness financial infrastructure [[theteardown.co](https://theteardown.co/stripe)].

### 5. Main Competitors and Differentiation
* **Adyen:** Stripe’s primary enterprise payments rival [[research.contrary.com](https://research.contrary.com/company/stripe)]. Adyen focuses on unified enterprise in-store/online commerce with no self-serve tier, whereas Stripe leads in self-serve, startup distribution, and software-led developer tools [[research.contrary.com](https://research.contrary.com/company/stripe)].
* **PayPal / Braintree:** Strong consumer wallet presence, but Stripe maintains superior API flexibility, marketplace payout orchestration (Connect), and AI tooling [[theteardown.co](https://theteardown.co/stripe), [research.contrary.com](https://research.contrary.com/company/stripe)].
* **Point Solutions:** Competes with Plaid (bank connections), Marqeta (card issuing), and Chargebee/Zuora (billing) across unbundled slices of its platform [[research.contrary.com](https://research.contrary.com/company/stripe)].

### 6. Strategic Priorities and Open Questions
* **Priorities:** Controlling both sides of the AI economy P&L: metering and collecting AI revenue (via Metronome/Payments) and routing AI compute costs (via OpenRouter) [[fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)]. Scaling programmable stablecoin cross-border rails [[research.contrary.com](https://research.contrary.com/company/stripe)].
* **Open Questions:** How quickly will the $7B+ OpenRouter acquisition generate accretive margins [[fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)]? With periodic tender liquidity satisfying staff [[research.contrary.com](https://research.contrary.com/company/stripe)], what is the actual timeline and catalyst for an IPO?

**Sources**

1. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
2. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
3. [Stripe — The Teardown](https://theteardown.co/stripe)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Why Stripe Is Buying OpenRouter for $7bn \| Brainfood](https://www.fintechbrainfood.com/p/stripe-buying-ai)

#### Run 2

### 1. What They Do, Who Buys It, & How They Make Money
Stripe builds payment and financial software infrastructure. Customers range from startups and platforms like Shopify to half of the Fortune 100, including Amazon and Google ([forbes.com](https://www.forbes.com/companies/stripe), [theteardown.co](https://theteardown.co/stripe)). 

Stripe charges a gross fee (typically 2.9% + $0.30 for standard US transactions) and nets an estimated ~0.40% take rate after interchange and network pass-through fees ([theteardown.co](https://theteardown.co/stripe)). To expand margins beyond commoditized processing, it layers on higher-margin SaaS products like Billing (0.7% fee), Radar fraud detection, Connect for marketplace payouts, and card issuing ([theteardown.co](https://theteardown.co/stripe)).

### 2. Recent News & Launches
* **AI Infrastructure Push:** Stripe agreed to acquire AI model router OpenRouter for more than $7 billion to capture token routing alongside its previous acquisition of usage-based billing platform Metronome ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)).
* **Crypto Rails Expansion:** Following its $1.1 billion purchase of stablecoin platform Bridge, Stripe rolled out support for tokens like OUSD and expanded Stablecoin Financial Accounts across more than 100 countries ([stripe.com](https://stripe.com/newsroom), [research.contrary.com](https://research.contrary.com/company/stripe)).
* **AI Agent Commerce:** Rolled out native checkout capabilities inside ChatGPT to power direct agentic transactions ([forbes.com](https://www.forbes.com/companies/stripe)).

### 3. Funding, Size, & Financial Signals
Stripe processed $1.9 trillion in payment volume in 2025 (~1.6% of global GDP), up from $1.4 trillion in 2024 ([research.contrary.com](https://research.contrary.com/company/stripe)). Group net revenue reached an estimated $5.1 billion in 2024, with projections topping $8.6 billion as its non-payment Revenue & Finance Automation suite hits $1 billion run-rate ([research.contrary.com](https://research.contrary.com/company/stripe)). Private market valuations have hovered near $91.5 billion, and its Dublin holding entity reported positive pre-tax profits of $101.9 million for 2024 ([theteardown.co](https://theteardown.co/stripe)). 

### 4. Leadership
* **Patrick Collison:** Co-founder & CEO ([theteardown.co](https://theteardown.co/stripe))
* **John Collison:** Co-founder & President ([theteardown.co](https://theteardown.co/stripe))
* **Steffan Tomlinson:** CFO (hired from Confluent/Palo Alto Networks to strengthen public-market readiness) ([theteardown.co](https://theteardown.co/stripe))

### 5. Main Competitors & Differentiation
* **Adyen:** Stripe’s primary global competitor. While Adyen grew strictly enterprise-first on a single unified platform without a self-serve tier, Stripe scaled upmarket from developers and SMBs, offering broader software tooling and marketplace APIs ([research.contrary.com](https://research.contrary.com/company/stripe)).
* **PayPal / Braintree & Square:** Retain huge consumer and SMB footprints, but lack Stripe’s developer modularity and enterprise platform extensibility ([research.contrary.com](https://research.contrary.com/company/stripe)).
* **Niche Specialists:** Faces point-solution pressure from Marqeta (card issuing), Plaid (open banking), and Chargebee (billing) ([research.contrary.com](https://research.contrary.com/company/stripe)).

### 6. Strategic Priorities & Open Questions
* **The AI Tech Stack:** Stripe is aggressively aiming to monetize the AI economy by capturing metered billing (Metronome) and token routing (OpenRouter) on top of raw payments ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)). 
* **Stablecoin Rails:** Scaling cross-border settlements and programmable accounts to bypass traditional banking fees ([research.contrary.com](https://research.contrary.com/company/stripe)).
* **Open Questions:** How quickly will multi-billion-dollar AI acquisitions yield returns? When will leadership pursue a public listing given recurring IPO speculation?

**Sources**

1. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
2. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
3. [Stripe — The Teardown](https://theteardown.co/stripe)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Why Stripe Is Buying OpenRouter for $7bn \| Brainfood](https://www.fintechbrainfood.com/p/stripe-buying-ai)

### anthropic/claude-sonnet-5.5

Cost: $0.0391

#### Run 1

# Stripe Briefing (as of 12 Oct 2026)

## 1. What they do, who buys it, how they make money
Stripe sells the software and financial plumbing for accepting and moving money online. It started with developer-friendly payments and expanded into billing, fraud, card issuing, embedded banking, tax, terminals, stablecoins and AI-agent commerce ([theteardown.co](https://theteardown.co/stripe)). Customers range from startups to large enterprises, including 50% of the Fortune 100 and 78% of the Forbes AI 50 as of August 2025 ([research.contrary.com](https://research.contrary.com/company/stripe)).

The headline US price is 2.9% + $0.30 per online card transaction. After interchange and network costs, Stripe keeps an estimated ~0.40% of volume. The strategy is to layer higher-margin software on top, such as Billing at 0.7% of billing volume ([theteardown.co](https://theteardown.co/stripe)).

## 2. Recent news (last ~6 months)
- **OpenRouter:** Stripe signed a deal to buy the AI-model routing API for more than $7bn, per Bloomberg. That is reportedly its largest acquisition ever, and OpenRouter has billed on Stripe since January 2026 ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)).
- **Investor letter:** H1 net revenue grew 41% year over year and free cash flow grew 43%. Stripe expects more than ten products to each clear $100M net revenue by year-end ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)).
- **OUSD:** Stripe's newsroom lists "OUSD is now available on Stripe" (30 Sept 2026). I could not see details beyond the headline ([stripe.com](https://stripe.com/newsroom)).

## 3. Funding, size, financial signals
- **Valuation:** A February 2026 employee tender offer reportedly valued Stripe at $159B ([research.contrary.com](https://research.contrary.com/company/stripe)). Forbes still shows an older $107B figure and $2.2B raised ([forbes.com](https://www.forbes.com/companies/stripe/)).
- **Volume:** $1.9T in 2025, up 34% ([research.contrary.com](https://research.contrary.com/company/stripe)).
- **Revenue:** Net revenue was about $5.1B in 2024. Stripe publishes no audited group accounts, but its Dublin entity reported a $101.88m pre-tax profit ([theteardown.co](https://theteardown.co/stripe)).
- **2025 estimates conflict:** Sacra puts 2025 at $6.93B ([theteardown.co](https://theteardown.co/stripe)), while Contrary estimates $8.6B ([research.contrary.com](https://research.contrary.com/company/stripe)). Treat both as estimates.

## 4. Leadership
Irish brothers Patrick and John Collison founded Stripe in 2009 ([forbes.com](https://www.forbes.com/companies/stripe/)). My sources don't confirm current titles or the wider executive team, so verify those before the meeting.

## 5. Main competitors
- **Payments:** Adyen, PayPal/Braintree, Checkout.com, Square and FIS ([research.contrary.com](https://research.contrary.com/company/stripe)). Adyen is enterprise-focused and, as of August 2025, had no self-serve SMB option. Stripe started with SMBs and is moving upmarket.
- **Specialists:** Marqeta (more customizable card issuing), Plaid (more bank integrations), and Chargebee, Recurly and Zuora in billing ([research.contrary.com](https://research.contrary.com/company/stripe)).

## 6. Likely priorities and open questions
My inferences from the above:
- **AI monetization:** Stripe is assembling payments (Stripe Payments), usage billing (Metronome) and token routing (OpenRouter) into one stack for AI companies ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)).
- **Stablecoins:** Bridge (acquired for $1.1B in February 2025) and Privy are the foundation, and OUSD may extend this ([research.contrary.com](https://research.contrary.com/company/stripe), [forbes.com](https://www.forbes.com/companies/stripe/)).
- **Open questions:**
  - Will the OpenRouter deal close, and how will Stripe integrate it? The price reportedly fell from ~$10bn in talks to over $7bn, about 50x revenue ([fintechbrainfood.com](https://www.fintechbrainfood.com/p/stripe-buying-ai)).
  - What do OUSD's terms look like?
  - Is there an IPO plan? My sources say nothing on this.
  - Are the 2025 revenue figures accurate, given the conflicting estimates?

**Sources**

1. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
2. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
3. [Stripe — The Teardown](https://theteardown.co/stripe)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Why Stripe Is Buying OpenRouter for $7bn \| Brainfood](https://www.fintechbrainfood.com/p/stripe-buying-ai)

#### Run 2

# Stripe Briefing (as of 2026-10-12)

## 1. What they do, who buys it, and how they make money
Stripe is an end-to-end commerce platform. Payments is the core, with card issuing, Treasury (banking-as-a-service), Terminal, Capital and Atlas built on top ([sacra.com](https://sacra.com/c/stripe/)). Buyers range from online merchants to platforms: more than 15,000 SaaS platforms use Stripe to serve over 10 million businesses ([stripe.com](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)).

Revenue comes from usage-based fees. The US headline rate is 2.9% + $0.30 per card charge, with custom pricing at high volume ([research.contrary.com](https://research.contrary.com/company/stripe)). Billing is about 0.7% of billing volume and Connect adds about 0.25% ([theteardown.co](https://theteardown.co/stripe)). Net take rate is estimated at about 0.4% ([research.contrary.com](https://research.contrary.com/company/stripe)). The strategy is to layer higher-margin software on thin-margin payments ([theteardown.co](https://theteardown.co/stripe)).

## 2. Recent news and launches
**Caveat:** I found nothing dated within the last six months. The newest items are from February 2026 (see section 3). The Stripe Tour New York post is undated in my results. It refers to 2024 as past and to "early next year," so it likely dates from 2025. Its announcements:
- **Agentic commerce:** the Agentic Commerce Protocol, co-developed with OpenAI, and Shared Payment Tokens, which power Instant Checkout in ChatGPT.
- **AI billing:** billing for LLM tokens, hybrid pricing plans and real-time credit burn-down.
- **Stablecoins:** products via Bridge and Privy, including stablecoin-backed Visa cards and custom stablecoin issuance.
- **Tax:** collection planned in 102 countries.

Source: [stripe.com](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)

## 3. Funding, size, and financial signals
- **Volume:** $1.9T in total volume, reported February 2026 ([research.contrary.com](https://research.contrary.com/company/stripe)).
- **Revenue:** Sacra estimates $6.8B in 2025, up 33% from $5.1B, with $1.2B EBITDA. Stripe confirmed it stayed profitable through 2025 ([sacra.com](https://sacra.com/c/stripe/)).
- **Valuation:** a February 2026 employee tender at $159B, backed mainly by Thrive, Coatue and a16z. That compares with $91.5B in February 2025 ([sacra.com](https://sacra.com/c/stripe/)).
- **Funding:** about $9.4B raised since 2010 ([sacra.com](https://sacra.com/c/stripe/)).
- **Cash:** The Information reports Stripe generated $3.2B in cash in 2025, "setting up" an acquisition hunt. I only saw the headline, not the article ([theinformation.com](https://www.theinformation.com/articles/stripe-minted-3-2-billion-cash-2025-setting-acquisition-hunt)).

## 4. Leadership
My search results contained no leadership information, so I can't cite any. Verify the current executive team on Stripe's site or LinkedIn before the meeting.

## 5. Main competitors and how they differ
Sacra lists PayPal (Braintree), Adyen, Worldpay, Global Payments and Fiserv (First Data) among public competitors, and Revolut and Checkout.com among private ones ([sacra.com](https://sacra.com/c/stripe/)). The sources don't offer a detailed head-to-head. The differentiator they support is Stripe's breadth: software, billing, embedded finance and crypto layered on payments ([theteardown.co](https://theteardown.co/stripe)).

## 6. Likely strategic priorities and open questions
These are my inferences from the sources above.
- **Priorities:**
  - AI and agentic commerce.
  - Stablecoin and crypto infrastructure.
  - Moving customers up the stack into billing and revenue software, which already manages nearly 200M subscriptions ([theteardown.co](https://theteardown.co/stripe)).
- **Questions to ask:**
  - What will the $3.2B in cash be used for: acquisitions or something else?
  - Do they plan to stay private, given the tender-offer pattern?
  - How fast is agentic commerce adoption actually moving?
  - What is the current executive team, and what has launched since February 2026?

**Sources**

1. [Stripe Business Breakdown & Founding Story - Contrary Research](https://research.contrary.com/company/stripe)
2. [All our product updates from Stripe Tour New York](https://stripe.com/blog/all-our-product-updates-from-stripe-tour-new-york)
3. [Stripe Minted $3.2 Billion in Cash in 2025, Setting Up Acquisition Hunt](https://www.theinformation.com/articles/stripe-minted-3-2-billion-cash-2025-setting-acquisition-hunt)
4. [Stripe revenue, valuation & funding \| Sacra](https://sacra.com/c/stripe/)
5. [Stripe — The Teardown](https://theteardown.co/stripe)

### deepseek/deepseek-v4-pro

Cost: $0.0111

#### Run 1

**1. What they do, who buys it, and how they make money**  
Stripe provides payments and financial infrastructure software. Businesses of every size—from startups to half the Fortune 100 (including Amazon, Google, Shopify)—use it to accept payments, manage billing, issue cards, and handle tax. [forbes.com][theteardown.co] Its US online card rate is 2.9% + $0.30, but after interchange and network pass‑throughs the net take rate is about 0.40%. [theteardown.co] Higher‑margin software layers (Billing 0.7%, Connect, Radar, Issuing, Tax) drive profitability; Stripe lands with payments and expands merchants into these tools. [theteardown.co] The company also earns from stablecoin and AI‑commerce services.

**2. Recent news and launches (last 6 months)**  
- Acquired **OpenRouter** for more than $7bn—the largest deal in Stripe’s history. OpenRouter’s API gives access to 400+ AI models and lets developers route each request to the cheapest model. The acquisition gives Stripe a view of both revenue collection and token spending for AI companies. [fintechbrainfood.com]  
- Launched **OUSD**, a stablecoin now available on Stripe, letting businesses issue and transact with dollar‑pegged tokens directly through the platform. [stripe.com]  
- The company told investors that **H1 2026 net revenue grew 41%** year‑over‑year and that by year‑end more than ten products would each surpass $100M in net revenue. [fintechbrainfood.com]

**3. Funding, size, and financial signals**  
Stripe has raised $2.2B from Sequoia, General Catalyst, Founders Fund, and others. [forbes.com] It processed **$1.9 trillion** in payment volume in 2025 (+34%), equivalent to ~1.6% of global GDP. [contrary.com] Estimated 2025 payments net revenue was $7.6B, and the Revenue suite (Billing, Invoicing, Tax) is expected to reach $1B annually in 2026. [contrary.com] A Dublin holding entity reported 2024 revenue of $5.12B and a pre‑tax profit of $101.8M, reversing prior losses. [theteardown.co] In February 2026 an employee tender offer priced Stripe at **$159B**. [contrary.com]

**4. Leadership**  
The company is led by co‑founders **Patrick and John Collison**. [forbes.com]

**5. Main competitors and how they differ**  
- **Adyen** (market cap ~$53.5B) focuses on large enterprises with a single unified platform and no self‑serve SMB tier; Stripe started with startups and moved upmarket, and reaches many small businesses via platforms like Shopify. [contrary.com]  
- **PayPal / Braintree** and **Checkout.com** also compete in payments. Stripe’s original advantage was developer experience—a few lines of code to accept a card—and it now differentiates with a broad stack that includes billing, issuing, stablecoins, and AI routing. [theteardown.co][contrary.com]  
- In specific adjacencies, Plad rivals Financial Connections, Marqeta competes with Issuing, and Avalara with Tax. [contrary.com]

**6. Likely strategic priorities and open questions**  
Stripe is embedding itself deeper into the **AI economy**: the OpenRouter deal (plus the earlier Metronome acquisition) lets it meter and route AI token spending, raising its effective take rate on AI transactions. [fintechbrainfood.com] **Stablecoins** are another pillar—through the Bridge acquisition and the OUSD launch, Stripe aims to make stablecoin‑based payouts and commerce a core rail. [stripe.com][contrary.com] Expanding the Revenue & Finance Automation suite toward $1B remains a focus.  
Open questions: integration risk of a $7B acquisition, the evolving regulatory environment for stablecoins, whether 40%+ revenue growth is sustainable, and if the company will eventually pursue an IPO given its soaring private valuation.

**Sources**

1. [Stripe Newsroom: The Latest News & Announcements](https://stripe.com/newsroom)
2. [Stripe \| Company Overview & News - Forbes](https://www.forbes.com/companies/stripe/)
3. [Stripe — The Teardown](https://theteardown.co/stripe)
4. [Report: Stripe Business Breakdown & Founding Story - Contrary](https://research.contrary.com/company/stripe)
5. [Why Stripe Is Buying OpenRouter for $7bn \| Brainfood](https://www.fintechbrainfood.com/p/stripe-buying-ai)

#### Run 2

**1. What they do, who buys it, and how they make money**  
Stripe provides the financial infrastructure for online payments, billing, and a growing stack of software services. Its original wedge was a developer‑friendly API that lets a business accept card payments with just a few lines of code [stripe.com][technically.dev]. The company has since expanded into Billing (subscriptions/invoicing), Connect (platform payments), Radar (fraud prevention), Issuing (card issuing), Treasury, Tax, Terminal (in‑person), and most recently stablecoins and agentic commerce [theteardown.co]. Half of the Fortune 100 use Stripe, alongside millions of startups and platforms [stripe.com][theteardown.co]; it handled $1.9 trillion in payment volume for 5 million businesses in 2025 [wikipedia].

The core revenue engine is a 2.9% + $0.30 per‑transaction fee on US card payments, but after passing through interchange and network fees, Stripe’s net take rate is estimated at ~0.40% of volume [theteardown.co][technically.dev]. Higher‑margin software layers (e.g., Billing at0.7% of billing volume, Radar, Issuing interchange, Connect fees) lift the blended margin and drive the land‑and‑expand model [theteardown.co].The company is profitable [youtube.com].

**2. Recent news and launches (last6 months)**  
- **Valuation jump:** In February2026, a tender offer valed Stripe at $159 billion, a74% increase from the $91.5 billion mark in early2025 [wikipedia].  
- **2025 annual letter release:** Stressed continued profitability, over350 product updates in the past year, and crossed 200 million end‑users [youtube.com].  
- **Agentic Commerce Suite:** Launched as a new bet on AI‑driven transactions, enabling agents to execute payments on behalf of users [youtube.com][theteardown.co].  
- **Crypto/stablcoin push:** Followed up on the2024 USDC pay‑ins re‑enablement and the2025 acquisition of stablecoin platform Bridge ($1.1B) by acquiring wallet provider Privy in June2025 [wikipedia].

**3. Funding, size, and financial signals**  
Stripe remains private. Its valuation has swung from $95B (2021) to $50B (2023) and now $159B (2026) [theteardown.co][wikipedia]. A Dublin holding entity filed2024 revenue of $5.12B (+34%) and a pre‑tax profit of $102M, reversing a prior‑year loss [theteardown.co]. Independent estimates put group net revenue near $5.1B (2024) and $6.93B (2025), implying a ~17.9x 2024 net‑revenue multiple at the $91.5B mark [theteardown.co]. Headcount stood at8,500 in2025 [wikipedia]. The2026 tender offer provided employee liquidity, and the earlier hire of CFO Steffan Tomlinson is widely seen as IPO‑readiness scaffolding [theteardown.co].

**4. Leadership**  
Cofounders Patrick Collison (CEO) and John Collison (President) still lead the company [wikipedia]. Steffan Tomlinson, who joined as CFO in2023 from Confluent and Google Cloud, is viewed as a key step toward a potential public listing [theteardown.co]. Culture is described as introverted but demanding; ~40% of staff work remote, though Glassdoor reviews note a challenging pace [theteardown.co].

**5. Main competitors and how they differ**  
- **Adyen** – publicly listed, enterprise‑focused, 50% EBITDA margin and a lower take rate (∼16bps) but a narrower product suite [theteardown.co].  
- **PayPal/Braintree** – larger volume ($1.68T TPV) with a consumer wallet; stronger in‑person presence [theteardown.co].  
- **Block (Square)** – dominates SMB and card‑present, an area where Stripe is weaker [theteardown.co].  
- **Legacy acquirers** (Fiserv, Global Payments, Worldpay) – $3.7T combined volume and deep bank distribution [theteardown.co].  
- **Shopify Payments** – built on Stripe but captures the merchant relationship, acting as both partner and rival [theteardown.co].  
- **Regional leaders** – Razorpay (India), Mercado Pago (LatAm) hold sway in key growth markets [theteardown.co].  

Stripe’s edge is the broadest ecosystem and a developer‑first motion that spans startups to the Fortune100 [theteardown.co].

**6. Likely strategic priorities and open questions**  
- **Move up the software stack:** Drive adoption of Billing, Radar, Issuing, and the Revenue & Finance Automation suite to raise blended margins and increase switching costs [theteardown.co].  
- **Bet on stablecoins and agentic commerce:** Early, high‑conviction moves via Bridge, Privy, and the Agentic Commerce Suite; monetisation models remain unproven [theteardown.co][youtube.com].  
- **IPO runway:** With a CFO in place, profitability, and surging volume, the question is not *if* but *when* a public offering happens – and whether the premium valuation can be sustained against public‑market multiples [theteardown.co].  
- **Competitive and regulatory pressure:** Adyen’s cost advantage, merchant orchestration layers, and stablecoin/crypto regulations pose ongoing risks. Retention of talent in a high‑pressure culture is another open question [theteardown.co].

**Sources**

1. [Stripe \| Financial Infrastructure to Grow Your Revenue](https://stripe.com/)
2. [Stripe, Inc.](https://en.wikipedia.org/wiki/Stripe,_Inc.)
3. [Stripe's 2025 annual letter](https://www.youtube.com/watch?v=_duV2ZXuiAs)
4. [Stripe — The Teardown](https://theteardown.co/stripe)
5. [What does Stripe do? - Technically](https://technically.dev/posts/what-does-stripe-do)
