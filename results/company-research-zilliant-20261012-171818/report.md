# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T17:18:18
- Variables: `company=Zilliant`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2179 (contestants $0.1455, judge $0.0724)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 8.2 (8.2–8.2) | $0.0373 | 16.0s (15.2s–16.8s) | 5 (5–5) | 5 (4–6) | 2.2 |
| google/gemini-3.8-flash | 7.2 (6.6–7.8) | $0.0207 | 23.0s (20.3s–25.7s) | 5 (5–5) | 6 (6–7) | 3.5 |
| deepseek/deepseek-v4-pro | 6.7 (6.4–7.0) | $0.0148 | 36.5s (30.3s–42.7s) | 5 (5–5) | 8 (7–8) | 4.5 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: It distinguishes sourced facts from uncertainty and gives meeting-ready questions, though several product-history and leadership details exceed the supplied excerpts.
- **google/gemini-3.8-flash**: The briefing has relevant questions and recent examples, but it presents several unsupported financial, leadership and technical specifics as fact.
- **deepseek/deepseek-v4-pro**: Concrete customer and survey details are useful, but unsupported business-model and competitor assertions, a misdated launch, and garbled leadership names weaken the briefing.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The October and November 2025 launch dates and the Pricing Plus name are not established by B's supplied excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): Pascal Yammine is CEO; his name does not appear in B's cited excerpt.
- **anthropic/claude-sonnet-5.5** (run 1): Pricing is held outside the ERP; the excerpt establishes Salesforce and SAP integration, but not that architecture.
- **anthropic/claude-sonnet-5.5** (run 1): Madison Dearborn Partners is the PE owner; the excerpt lists it as an investor but does not establish ownership.
- **google/gemini-3.8-flash** (run 1): Zilliant's revenue comes from enterprise SaaS subscriptions and implementation services tiered by modules, transaction volume and data scale.
- **google/gemini-3.8-flash** (run 1): Madison Dearborn Partners acquired Zilliant in late 2021.
- **google/gemini-3.8-flash** (run 1): Customer wins center on multi-billion-dollar global distributors; the excerpts establish FTZ's digital sales, not that broader characterization.
- **google/gemini-3.8-flash** (run 1): Pascal Yammine's CEO role, former Salesforce position and role in an API-first strategic shift are not established by C's cited excerpts.
- **google/gemini-3.8-flash** (run 1): Pricefx and Vendavo are named competitors in the cited CB Insights excerpt.
- **google/gemini-3.8-flash** (run 1): Zilliant delivers millisecond-level lookups without burdening ERP backends.
- **google/gemini-3.8-flash** (run 1): The MCP server lets external LLMs pull governed pricing logic without custom integrations; the excerpt describes broader integration of pricing intelligence but not those specifics.
- **deepseek/deepseek-v4-pro** (run 1): Zilliant sells annual or multi-year SaaS subscriptions, likely with implementation services.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts establish that typical buyers are large enterprises with high SKU counts.
- **deepseek/deepseek-v4-pro** (run 1): The Precision Pricing Platform consolidation, Agentic AI launch and MCP server occurred earlier in 2026; the supplied excerpts do not establish those claims, and the Agentic AI launch was in October 2025.
- **deepseek/deepseek-v4-pro** (run 1): Zilliant does not disclose employee count, is focused on a liquidity event, or may be near cash-flow break-even.
- **deepseek/deepseek-v4-pro** (run 1): Pascal Yammine is CEO; that name does not appear in A's cited excerpts.
- **deepseek/deepseek-v4-pro** (run 1): PROS spans B2B and B2C, Model N focuses on pharma and high-tech, Pactum provides autonomous negotiation, and Zilliant concentrates exclusively on B2B manufacturing and distribution.
- **deepseek/deepseek-v4-pro** (run 1): Zilliant's engines provide explainable pricing as a differentiator from the named competitors.
- **anthropic/claude-sonnet-5.5** (run 2): October 12, 2026 is the briefing's as-of date; no supplied source establishes that exact date.
- **anthropic/claude-sonnet-5.5** (run 2): The products are grouped under the 'Precision Pricing Platform'; the cited excerpt does not establish that name.
- **anthropic/claude-sonnet-5.5** (run 2): Pricing Plus launched in November 2025; that launch and date do not appear in the supplied excerpt.
- **anthropic/claude-sonnet-5.5** (run 2): Pascal Yammine is CEO; his name and title do not appear in the supplied excerpts.
- **anthropic/claude-sonnet-5.5** (run 2): Zilliant keeps pricing logic outside the ERP; the cited customer account establishes a Salesforce entry point and SAP integration, not that architecture generally.
- **anthropic/claude-sonnet-5.5** (run 2): Both cited customer wins are based in Europe; Denmark is established for FTZ, but the supplied Julius Hoesch excerpt does not state its location.
- **google/gemini-3.8-flash** (run 2): Zilliant earns revenue from SaaS subscriptions and professional implementation or advisory services; the excerpts do not establish its revenue model.
- **google/gemini-3.8-flash** (run 2): Mid-market buyers and the stated cloud-based characterization are not established by the excerpts.
- **google/gemini-3.8-flash** (run 2): The MCP Server lets autonomous agents retrieve live pricing data and query pricing guardrails; the excerpt only establishes integration of pricing intelligence into other AI tools.
- **google/gemini-3.8-flash** (run 2): Pascal Yammine's and Kylie Fuentes's names and titles do not appear in the supplied excerpts.
- **google/gemini-3.8-flash** (run 2): SAP, Microsoft and Oracle offer competing native ERP/CRM pricing functionality, and Zilliant's integrations avoid vendor lock-in; those comparisons are not established by the excerpts.
- **google/gemini-3.8-flash** (run 2): Employee headcount and revenue are 'kept private'; the excerpts provide no figures, but do not establish that characterization.
- **deepseek/deepseek-v4-pro** (run 2): The current products are grouped under a 'Precision Pricing Platform'; that name is not established by the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 2): Recurring SaaS subscriptions are presented as likely, but the excerpts do not establish commercial terms.
- **deepseek/deepseek-v4-pro** (run 2): Pascal Yammine is CEO; his name and title do not appear in the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The Crunchbase excerpt lists Pete Eppele and Greg Howe as key people, but does not establish that their roles are current.
- **deepseek/deepseek-v4-pro** (run 2): PROS's strength in airlines, Model N's focus on life sciences and high-tech, and Pactum's supplier-negotiation offering are not described in the excerpts.
- **deepseek/deepseek-v4-pro** (run 2): SAP, Oracle and Microsoft have competing pricing modules, or Zilliant is faster and more explainable than those modules; the excerpts do not substantiate these comparisons.
- **deepseek/deepseek-v4-pro** (run 2): The FTZ win indicates a solid enterprise customer base or bears on revenue concentration; neither follows from the cited customer sales figure.
- **deepseek/deepseek-v4-pro** (run 2): Zilliant is promoting agentic AI for autonomous cost-pass-through; the excerpts separately describe agentic AI and automated cost pass-through, not that combined use.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0373

#### Run 1

# Zilliant Briefing (as of 12 Oct 2026)

## 1. What they do, who buys it, how they make money
Zilliant sells AI-driven pricing and revenue optimization software for B2B companies. Its products cover price management, analytics, optimization, quoting and agreement management ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). It was founded in 1999 and is based in Austin, Texas. Its targets are manufacturers and distributors, mainly pricing and sales teams ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). Recent customers include Danish auto-parts supplier FTZ ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)) and chemical distributor Julius Hoesch ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). **Revenue model:** I found no source describing pricing or contract structure. It is presumably software licensing or subscription, but that is unconfirmed.

## 2. Recent news (last 6 months)
- **Sept 8, 2026:** FTZ, with 300,000+ SKUs and more than DKK 2B in digital sales, selected Price Manager, Real-Time Pricing Engine and Visual Analytics. Zilliant says FTZ's benchmark showed it ~3x faster sequentially and ~70x higher throughput ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). This is a vendor press release, so the benchmark claim is unverified independently.
- **Apr 28, 2026:** "Pricing Without Control" survey of 300 executives. 88% place pricing accountability with the CEO, CFO or CRO, 23% use AI pricing tools, and 18% still use spreadsheets ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
- **Earlier context (outside the window):** Agentic AI with an MCP Server (Oct 2025), Pricing Plus (Nov 2025), and the Precision Pricing Platform ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

## 3. Funding, size, financial signals
CB Insights lists it as private equity-backed, with $130.85M raised in total, including $35M about three years ago. Investors include Madison Dearborn Partners, Goldman Sachs, Trellis Partners and Austin Ventures ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). **Not found:** revenue, headcount, profitability, valuation. Customer wins are the only visible health signal.

## 4. Leadership
- **Pascal Yammine**, CEO ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
- Crunchbase lists Pete Eppele (SVP Products & Science) and Greg Howe (SVP Worldwide Sales) ([crunchbase.com](https://www.crunchbase.com/organization/zilliant)). That profile may be dated, so confirm they are still in role.

## 5. Competitors
CB Insights names PROS, Model N and Pactum, among others ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). Its list also includes RAPT Therapeutics, a biotech, which looks like an error. The sources I found don't compare features, so I can't substantiate how these rivals differ. Zilliant's own positioning is:
- pricing "lifecycle management" with a unified platform
- pricing held outside the ERP and embedded in Salesforce
- deep SAP integration
- real-time execution

Treat those as marketing claims ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

## 6. Likely priorities and open questions
**Priorities (inferred from the announcements):**
- Agentic and AI pricing capabilities
- Real-time pricing for digital B2B commerce
- European distribution wins (Denmark, Germany)
- Governance and explainability as the pitch against spreadsheets and tool sprawl

**Open questions:**
- Scale, growth and profitability?
- Where is the PE owner in its hold period, and is a sale likely?
- How is it priced, and how much is recurring revenue?
- Can the benchmark advantage be reproduced in other customers' environments?
- How does it win against PROS and Model N in head-to-head deals?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
4. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
5. [Zilliant - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/zilliant)

#### Run 2

# Zilliant Briefing (as of Oct 12, 2026)

## 1. What they do, who buys it, how they make money
Zilliant sells AI-driven pricing and revenue optimization software for B2B companies. Its products cover price management, analytics, optimization, quoting, and sales agreements. Its customers are in manufacturing and distribution, and its users are pricing and sales teams ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). It was founded in 1999 and is based in Austin, Texas. The products are now grouped under the "Precision Pricing Platform" ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). **Pricing model:** I found nothing on it. It is probably software licensing or subscription, but that is my inference and I could not confirm it.

## 2. Recent news (last 6 months)
- **Sept 8, 2026:** FTZ Autodele & Værktøj, Denmark's largest automotive aftermarket supplier, selected Zilliant. FTZ has 300,000+ SKUs and DKK 2B+ in digital sales. It will deploy Price Manager, Real-Time Pricing Engine and Visual Analytics. In FTZ's benchmark, Zilliant was about 3x faster sequentially and delivered about 70x higher throughput at maximum load ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). The benchmark is as reported in Zilliant's own press release.
- **April 28, 2026:** Zilliant published its "Pricing Without Control" survey of 300 executives. Nearly all adjust prices, but only half are confident they understand the financial impact. 23% use AI pricing tools and 18% still use spreadsheets ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).

Earlier context: Agentic AI and an "industry-first" MCP Server launched in Oct 2025 ([zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)). Pricing Plus launched in Nov 2025, and Julius Hoesch (a chemical distributor) was announced as a customer in Jan 2026 ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

## 3. Funding, size, financial signals
CB Insights lists Zilliant as private equity-backed, with $130.85M raised in total. The last raise was $35M, about three years ago. Investors include Madison Dearborn Partners, Goldman Sachs, Trellis Partners and Austin Ventures ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). **Not found:** revenue, headcount, profitability, and valuation.

## 4. Leadership
Pascal Yammine is CEO ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). I found no other executive names in these sources.

## 5. Competitors
CB Insights names PROS, Model N and Pactum, plus others ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). It also lists RAPT Therapeutics, a biotech, which looks like a data error. The sources don't compare these companies in detail, so I can't verify how they differ. Zilliant's own positioning is:
- pricing lifecycle management
- pricing logic kept outside the ERP, with Salesforce embedding
- explainable, governed pricing
- real-time performance at scale

Treat these as claims, not independent assessments.

## 6. Likely priorities and open questions
**Priorities (inferred from the news above):**
- Winning digital-commerce and distribution customers, especially in Europe, where both recent customer wins are based
- Selling AI and agentic capabilities as an alternative to spreadsheets
- Selling governance and control as a theme, based on the survey

**Questions to ask:**
- How is revenue split between licensing, services and usage?
- With PE ownership and the last raise about three years ago, what is the ownership or exit outlook?
- How does Zilliant differentiate from PROS and Model N in competitive deals?
- Are the benchmark and AI claims backed by customer results?
- How broad is its customer base beyond the announced wins?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant Launches Agentic AI with Industry-First MCP Server to End Spreadsheet Pricing \| press release](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)

### google/gemini-3.8-flash

Cost: $0.0207

#### Run 1

### 1. What They Do, Who Buys It, & Business Model
* **What they do:** Zilliant offers cloud-based pricing lifecycle management software—including Price Manager, Real-Time Pricing Engine, and Visual Analytics—to automate price setting, guardrails, and margin optimization ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
* **Who buys it:** B2B enterprises in distribution, manufacturing, and chemicals managing complex, high-SKU catalogs and volatile input costs (e.g., FTZ, Julius Hoesch) ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).
* **How they make money:** Enterprise SaaS subscriptions and implementation services, tiered by platform modules, transaction volume, and data scale.

### 2. Recent News & Launches (Last ~6 Months)
* **FTZ Deal (Sept. 2026):** FTZ, Denmark’s largest automotive aftermarket supplier, selected Zilliant for 300,000+ SKUs after a benchmark test showed Zilliant generated ~70x higher throughput under peak real-time quoting load ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
* **"Pricing Without Control" Report (Apr. 2026):** A survey of 300 B2B executives revealed that while 88% place pricing accountability in the C-suite, only 23% use AI-enabled tools and nearly half lack confidence in their price adjustments due to fragmented ERP/spreadsheet workflows ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
* **Agentic AI & MCP Server:** Zilliant recently rolled out Agentic AI with an industry-first Model Context Protocol (MCP) Server to allow autonomous AI agents and enterprise workflows to retrieve pricing logic directly ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

### 3. Funding, Size, & Financial Signals
* **Ownership & Funding:** Private equity-backed by Madison Dearborn Partners (acquired in late 2021) ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). Prior funding totaled ~$130.8M ([cbinsights.com](https://www.cbinsights.com/company/zilliant)).
* **Scale:** Founded in 1999 and headquartered in Austin, Texas ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). As a private company, revenue is not disclosed, but customer wins center on multi-billion-dollar global distributors.

### 4. Leadership
* **Chief Executive Officer:** Pascal Yammine (formerly Senior VP & GM of Salesforce Revenue Cloud), leading the company's shift toward high-speed, API-first execution integrated with modern CRM and ERP ecosystems ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).

### 5. Main Competitors & Differentiation
* **Competitors:** PROS, Pricefx, Vendavo, and Model N ([cbinsights.com](https://www.cbinsights.com/company/zilliant)).
* **Differentiation:**
  * **Real-time execution speed:** Optimized for high-throughput, millisecond-level digital channel lookups without burdening ERP backends ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
  * **Ecosystem integration:** Strong embedded positioning within Salesforce and SAP S/4HANA environments ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).
  * **Agentic architecture:** Open connectivity through its MCP server, letting external LLMs/agents pull governed pricing without custom integrations ([zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)).

### 6. Likely Strategic Priorities & Open Questions
* **Strategic Priorities:** Driving displacement of legacy ERP pricing rules in European and North American B2B distribution; monetizing MCP/Agentic AI integrations; capitalizing on tariff and inflation-driven re-pricing needs ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).
* **Open Questions to Ask:**
  * How are enterprise customers operationalizing the MCP Server today—is it primarily feeding sales chatbots or automated agent-to-agent procurement?
  * What is the typical deployment timeline when co-migrating with an ERP overhaul (like SAP S/4HANA)?
  * How is the company balancing core R&D against profitability benchmarks under Madison Dearborn Partners?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant Launches Agentic AI with Industry-First MCP Server to End Spreadsheet Pricing \| press release](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)

#### Run 2

### 1. What They Do, Who Buys It, and How They Make Money
Zilliant provides cloud-based B2B pricing lifecycle management and revenue optimization software, including price management, real-time pricing engines, analytics, and CPQ (configure, price, quote) capabilities [cbinsights.com](https://www.cbinsights.com/company/zilliant), [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale). 
* **Buyers:** Pricing, sales, and commercial operations leaders (often overseen by the CEO, CFO, or CRO) at mid-market and enterprise B2B distributors and manufacturers in sectors like automotive aftermarket and chemicals [zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes), [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
* **Revenue Model:** Enterprise B2B SaaS software subscriptions alongside professional implementation and advisory services (specific contractual terms are not publicly disclosed).

### 2. Recent News and Launches (Past 6 Months)
* **FTZ Automotive Win (September 2026):** FTZ, Denmark’s largest automotive supplier, selected Zilliant after benchmark testing demonstrated 70x higher output under peak throughput and 3x faster sequential pricing responses [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
* **"Pricing Without Control" Research (April 2026):** Surveyed 300 enterprise executives, reporting that while 88% place pricing accountability in the C-suite, only 23% use AI-enabled pricing platforms and 18% still run pricing via spreadsheets [zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes).
* **Agentic AI Expansion:** Follows Zilliant’s rollout of its industry-first Model Context Protocol (MCP) Server, enabling autonomous enterprise AI agents to retrieve live pricing data without manual integration [zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing).

### 3. Funding, Size, and Financial Signals
* **Ownership & Capital:** Founded in 1999 in Austin, Texas, Zilliant is private equity-backed by Madison Dearborn Partners [cbinsights.com](https://www.cbinsights.com/company/zilliant). It has raised $130.85M in total funding [cbinsights.com](https://www.cbinsights.com/company/zilliant).
* **Size:** Exact employee headcount and financial revenues are kept private, but customer deployments handle high transaction volumes (e.g., FTZ's 300,000+ SKUs and >DKK 2B in digital sales) [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).

### 4. Leadership
* **Pascal Yammine:** Chief Executive Officer [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
* **Kylie Fuentes:** Chief Product & Marketing Officer [zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)

### 5. Main Competitors and Differentiation
* **Competitors:** PROS, Model N, and native ERP/CRM pricing functionality within SAP, Microsoft, and Oracle [cbinsights.com](https://www.cbinsights.com/company/zilliant).
* **Differentiators:** 
  * Extreme low-latency, real-time pricing execution designed for complex, high-SKU distribution environments [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
  * System neutrality: Deep integration with both SAP S/4HANA and Salesforce, avoiding ERP vendor lock-in [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg).
  * An open MCP Server architecture allowing 3rd-party AI agents to query pricing guardrails [zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing).

### 6. Likely Strategic Priorities and Open Questions
* **Priorities:** Converting B2B distributors migrating to cloud ERPs (like SAP S/4HANA) into Zilliant pricing hubs [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg), and driving enterprise adoption of autonomous Agentic AI tools [zilliant.com](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing).
* **Open Questions to Ask:**
  * How are customers using the new MCP server—are enterprise clients deploying custom agents to manage quote approvals autonomously?
  * How is Zilliant positioning against ERP vendors building more advanced native pricing modules?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant Launches Agentic AI with Industry-First MCP Server to End Spreadsheet Pricing \| press release](https://zilliant.com/press-releases/zilliant-launches-agentic-ai-with-industry-first-mcp-server-to-end-spreadsheet-pricing)

### deepseek/deepseek-v4-pro

Cost: $0.0148

#### Run 1

**1. What they do, who buys it, and how they make money**  
Zilliant provides AI-driven pricing lifecycle management software for B2B companies. Its Precision Pricing Platform helps manufacturers, distributors, and industrial service firms automate price setting, optimize deals, and enforce governance across digital and sales channels. Typical buyers are large enterprises with high SKU counts—recent wins include automotive parts distributor FTZ (300,000+ SKUs) and chemical distributor Julius Hoesch [zilliant.com]. The company sells annual or multi-year SaaS subscriptions, likely with implementation services.

**2. Recent news and launches (last 6 months)**  
- **September 8, 2026:** FTZ Autodele & Værktøj, Denmark’s largest automotive aftermarket supplier, selected Zilliant after a real-time benchmark. Zilliant delivered ~70x higher throughput under maximum load versus the alternative [zilliant.com].  
- **April 28, 2026:** Zilliant released its *Pricing Without Control* report surveying 300 executives, revealing that 88% of organizations now vest pricing accountability in the C-suite, yet only half are confident they understand the financial impact. Only 23% use AI pricing tools, highlighting a governance gap [zilliant.com].  
Earlier in 2026, the company consolidated its portfolio under the Precision Pricing Platform and launched Agentic AI with an industry-first MCP server for autonomous data retrieval, plus a streamlined “ricing Plus” offering targeting spreadsheet-dependent companies [zilliant.com].

**3. Funding, size, and financial signals**  
Zilliant has raised approximately $130.85 million in total funding, with the most recent round of $35 million closed about three years ago. Investors include Madison Dearborn Partners, Goldman Sachs, Austin Ventures, and others [cbinsights.com]. The company is private and does not disclose revenue or employee count. The presence of private equity (Madison Dearborn) suggests a focus on scaling efficiently toward a liquidity event. No recent funding rounds indicate the business may be operating near cash-flow break-even, though that is unconfirmed.

**4. Leadership**  
- **ascal Yammine** – Chief Executive Officer [zilliant.com]  
- **ete Eppele** – SV, Products & Science [crunchbase.com]  
- **reg Howe** – Senior Vice President of Worldwide Sales [crunchbase.com]  
No other C-suite names were found in the provided sources.

**5. Main competitors and how they differ**  
Key competitors include PROS (AI-powered pricing and revenue optimization), Model N (revenue management for pharma and high-tech), and Pactum (A-driven autonomous negotiation). Unlike PROS, which spans both B2B and B2C, Zilliant concentrates exclusively on B2B manufacturing and distribution. Its recent emphasis on real-time, explainable pricing through dedicated engines and agentic AI differentiates it from spread-sheet or rule-based tools, while the MCP server integrates directly with autonomous workflows [zilliant.com][cbinsights.com].

**6. Likely strategic priorities and open questions**  
Priorities:  
- Deploy the Precision Pricing Platform deeper into Europe, following the FTZ and Julius Hoesch wins.  
- Extend Agentic AI capabilities to capture the 77% of companies still not using AI for pricing (per its own survey).  
- Tighten integrations with SAP S/4HANA and Salesforce to become the embedded pricing layer for complex distributors.

Open questions:  
- Can Zilliant maintain the performance advantage demonstrated in benchmarks as its customer base scales?  
- How will it defend against ERP vendors adding native pricing modules?  
- Is the company profitable, or will it require further funding amid macroeconomic uncertainty?  
- What is the actual employee headcount and sustained revenue growth rate?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
4. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
5. [Zilliant - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/zilliant)

#### Run 2

**Briefing: Zilliant (Pricing Lifecycle Management)**

### 1. What they do, who buys it, and how they make money
Zilliant provides AI‑driven price optimization and management software for B2B manufacturing, distribution, high‑tech and industrial service companies. Its “Precision Pricing Platform” consolidates list‑price management, real‑time deal pricing, visual analytics, agreement management and campaign tools, aiming to replace spreadsheet‑based processes. Typical buyers are large SKU‑intensive distributors (e.g., auto parts, chemicals) that need governed, explainable pricing across digital channels. Zilliant likely sells recurring SaaS subscriptions, though exact commercial terms are not public.

### 2. Recent news and launches (last 6 months)
- **FTZ partnership (Sep 2026):** Denmark’s largest automotive aftermarket supplier chose Zilliant Price Manager, Real‑Time Pricing Engine and Visual Analytics after a rigorous benchmark. Zilliant delivered ~3x faster sequential response times and ~70x higher throughput than the competitor. FTZ will use Zilliant to automate customer‑specific prices for its 300k‑SKU digital business [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).  
- **Pricing Without Control survey (Apr 2026):** Zilliant released research among 300 manufacturing/distribution executives showing that 88% of pricing accountability now sits with the CEO, CFO or CRO, yet only 23% use AI‑enabled solutions and 18% still rely on spreadsheets. The study underscored that speed without governance compounds complexity, highlighting the need for a unified pricing truth [zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes).

### 3. Funding, size, and financial signals
Zilliant is private‑equity‑backed and has raised **$130.85 M** in total; its most recent round was $35 M about three years ago [cbinsights.com](https://www.cbinsights.com/company/zilliant). Key investors include **Madison Dearborn Partners, Goldman Sachs, Trellis Partners and Austin Ventures**. The company is classified as a “Challenger” in its segment alongside giants like Microsoft, Oracle and SAP. While revenue is undisclosed, large‑deal wins (e.g., FTZ with over DKK 2 B in digital sales) suggest a solid enterprise customer base.

### 4. Leadership
- **Pascal Yammine**, Chief Executive Officer (quoted in recent press releases) [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).  
- **Pete Eppele**, SVP Products & Science (previously at Stamford Industrial Group) [crunchbase.com](https://www.crunchbase.com/organization/zilliant).  
- **Greg Howe**, Senior Vice President of Worldwide Sales [crunchbase.com](https://www.crunchbase.com/organization/zilliant).  
Further C‑suite roles (CFO, CRO) not identified in the provided sources.

### 5. Main competitors and how they differ
- **PROS:** Also AI‑focused, strong in airlines and B2B, but Zilliant differentiates with a real‑time pricing engine that showed a 70x throughput advantage in a customer benchmark and a deep focus on governance for complex distributors.  
- **Model N:** Concentrates on revenue management and compliance for life sciences and high-tech, whereas Zilliant serves broad manufacturing/distribution with an emphasis on price lifecycle automation.  
- **Pactum:** AI‑driven supplier negotiation, not a full lifecycle pricing suite.  
- **SAP/Oracle/Microsoft:** Offer broader ERP suites with pricing modules; Zilliant positions itself as a specialist that complements (and integrates with) those platforms, providing faster, more explainable pricing.  
Named a “Challenger” to these large players [cbinsights.com](https://www.cbinsights.com/company/zilliant).

### 6. Likely strategic priorities and open questions
**Priorities:**  
- Deepen European distribution wins (FTZ, Julius Hoesch) and promote agentic AI capabilities for autonomous cost‑pass‑through.  
- Leverage survey findings to drive governance‑first messaging, selling the “unified pricing truth” concept.  
- Extend integrations with cloud ERPs (especially SAP S/4HANA) and CRMs (Salesforce).  

**Open questions:**  
- With no new funding in three years, will Zilliant seek another round or an exit to sustain growth against larger platform vendors?  
- How large is the revenue concentration risk from a few anchor customers?  
- Can Zilliant maintain its technical edge as competitors embed AI pricing natively into ERP suites?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/zilliant)
