# Council: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-13T14:27:30
- Variables: `company=Zilliant`
- Judge: `openai/gpt-6-sol`
- Synthesizer: `x-ai/grok-4.7`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.4193 (contestants $0.1427, synthesis $0.1490, judge $0.0930, synthesis guess $0.0345)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent | Synthesis % | Why (judge's guess) |
|---|---|---|---|---|---|---|---|---|
| council (x-ai/grok-4.7) | 8.9 (8.8–9.0) | $0.1459 | 114.4s (89.7s–139.0s) | 6 (5–6) | 2 (2–2) | 0.6 | 49% | Its cautious treatment of funding, revenue, and competitor differences reads like a consistent independent assessment. |
| anthropic/claude-sonnet-5.5 | 8.1 (8.1–8.2) | $0.0382 | 19.8s (18.8s–20.7s) | 5 (5–5) | 4 (3–5) | 2.1 | 4% | It combines many details, but consistently flags source conflicts and separates older announcements from the six-month window. |
| google/gemini-3.8-flash | 6.6 (6.5–6.8) | $0.0204 | 25.2s (22.0s–28.3s) | 5 (5–5) | 6 (6–7) | 3.2 | 1% | Its distinctive competitor comparisons and confident monetization claims read more like an independent answer than a synthesis. |
| deepseek/deepseek-v4-pro | 6.5 (6.2–6.8) | $0.0128 | 24.5s (14.2s–34.8s) | 5 (5–5) | 6 (6–6) | 5.1 | 46% | It stacks details from across the other briefings—benchmark figures, survey results, Pricing Plus, investors, analyst recognition, and agentic AI—while smoothing over their funding conflict and date-window caveats. |

The council row is the synthesizer's merge of the other answers. Its cost includes every contestant call plus the synthesis; its latency is the slowest contestant plus the synthesis. "Synthesis %" is the judge's guess, in a separate call after scoring, that the row is the merged answer (chance is 25% with 4 answers).

## Judge rationales

- **council (x-ai/grok-4.7)**: Specific and well-calibrated about the six-month window, source conflicts, and unknowns, with only limited unsupported detail.
- **anthropic/claude-sonnet-5.5**: A useful, current briefing that flags uncertainty and conflicting funding figures, though a few details lack support and it cannot answer how competitors differ.
- **google/gemini-3.8-flash**: Concrete and current, but several confident business-model, leadership, and competitive claims exceed the cited excerpts.
- **deepseek/deepseek-v4-pro**: It contains useful facts but mixes out-of-window news into the six-month section and presents several unsupported inferences as established facts.

## Unsupported claims

- **council (x-ai/grok-4.7)** (run 1): The cited excerpts do not identify Pascal Yammine as CEO.
- **council (x-ai/grok-4.7)** (run 1): The cited excerpts do not explicitly establish that Zilliant positions its pricing software outside the ERP.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not identify Pascal Yammine as CEO.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not establish a November 2025 Pricing Plus launch.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not explicitly establish that Zilliant manages pricing outside the ERP.
- **google/gemini-3.8-flash** (run 1): Zilliant sells modular SaaS subscription tiers and implementation services.
- **google/gemini-3.8-flash** (run 1): Madison Dearborn acquired Zilliant in late 2021.
- **google/gemini-3.8-flash** (run 1): Pascal Yammine previously held a senior VP and GM role at Salesforce.
- **google/gemini-3.8-flash** (run 1): The MCP server lets autonomous agents execute pricing decisions directly.
- **google/gemini-3.8-flash** (run 1): PROS is Zilliant’s primary public competitor, has airline roots, and differs from Zilliant in the ways described.
- **google/gemini-3.8-flash** (run 1): Zilliant is easier to deploy alongside Salesforce than competitors, or its FTZ benchmark establishes an advantage over Vendavo and Pricefx.
- **deepseek/deepseek-v4-pro** (run 1): Zilliant operates on a B2B SaaS model.
- **deepseek/deepseek-v4-pro** (run 1): Pricing Plus launched in late 2025, and the portfolio was consolidated under the Precision Pricing Platform then; the excerpt dates that platform’s unveiling to April 2025.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish the Pricing Plus description or the MCP server’s stated data-retrieval function.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not identify Pascal Yammine as CEO or support the characterization of his role in announcements.
- **deepseek/deepseek-v4-pro** (run 1): Customer wins, investment pace, and analyst recognition demonstrate steady commercial traction.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not substantiate the asserted differences between Zilliant and its named competitors.
- **council (x-ai/grok-4.7)** (run 2): Pascal Yammine is CEO; his name does not appear in the supplied excerpts.
- **council (x-ai/grok-4.7)** (run 2): Julius Hoesch selected Zilliant on 27 January 2026; that is the announcement date, while the release calls it a customer addition from 2025.
- **anthropic/claude-sonnet-5.5** (run 2): Pascal Yammine is CEO; his name does not appear in the supplied excerpts.
- **anthropic/claude-sonnet-5.5** (run 2): Pricing Plus launched in November 2025; no supplied excerpt mentions it.
- **anthropic/claude-sonnet-5.5** (run 2): The Precision Pricing Platform was a late-2025 launch; the supplied source dates its unveiling to April 2025.
- **anthropic/claude-sonnet-5.5** (run 2): Gartner named Zilliant a Representative Vendor in its 2025 market guide; this does not appear in the supplied excerpts.
- **anthropic/claude-sonnet-5.5** (run 2): Zilliant centralizes pricing outside the ERP; the cited excerpt describes Salesforce and SAP integration but does not establish this broader positioning.
- **google/gemini-3.8-flash** (run 2): Zilliant's software is cloud-native, and it earns revenue specifically through enterprise SaaS subscriptions; the excerpts establish a SaaS model but not those details.
- **google/gemini-3.8-flash** (run 2): The FTZ benchmark was independent; the excerpt describes a test conducted by FTZ.
- **google/gemini-3.8-flash** (run 2): The MCP server enables autonomous pricing-data retrieval, and Zilliant unified its suite under the Precision Pricing Platform; neither detail appears in the cited excerpt.
- **google/gemini-3.8-flash** (run 2): Madison Dearborn acquired Zilliant via the listed buyout/LBO; the excerpt identifies it as an investor but does not identify the buyout acquirer.
- **google/gemini-3.8-flash** (run 2): The reported funding totals came from prior venture and growth rounds; the excerpts do not classify those funds that way.
- **google/gemini-3.8-flash** (run 2): Pascal Yammine is CEO; his name does not appear in the supplied excerpts.
- **google/gemini-3.8-flash** (run 2): Vendavo is a competitor, and the cited excerpts establish the stated competitive differentiation; neither is shown.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts establish list-price calculations, discount guardrails, and hundreds of thousands of SKUs as typical of Zilliant buyers.
- **deepseek/deepseek-v4-pro** (run 2): Revenue specifically comes from SaaS subscriptions; PitchBook establishes a SaaS model but does not specify subscription terms.
- **deepseek/deepseek-v4-pro** (run 2): Zilliant is now in a growth phase marked by platform consolidation and step-function launches.
- **deepseek/deepseek-v4-pro** (run 2): Pascal Yammine is CEO and made the quoted statement; neither appears in the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The three listed traits are unique to Zilliant, or its governance features prevent uncontrolled decisions; the excerpts do not establish either comparison.
- **deepseek/deepseek-v4-pro** (run 2): A buyout/LBO structure is ongoing; PitchBook lists a latest deal type, not an ongoing transaction.

## Where the models disagreed (run 1)

- Total capital raised: CB Insights says $130.85M (last round $35M about three years ago); The Pricing News says roughly $80M.
- Julius Hoesch: Zilliant’s release calls it a chemical distributor; The Pricing News calls it a German industrial manufacturer.
- Monetization: some accounts call it enterprise SaaS plus services; the cited sources do not state the revenue model, so that claim was dropped.
- Competitors and differentiation: one account added Vendavo, Pricefx, and PROS travel roots and treated Zilliant’s own benchmarks as competitive proof; the sourced list is PROS, Model N, Pactum, and Celerity (plus a mismatched RAPT Therapeutics), and the sources do not compare rivals.
- Ownership timing: one account said Madison Dearborn acquired Zilliant in late 2021; the excerpts only say it is a Madison Dearborn portfolio company with a private-equity round, not an acquisition date.
- CEO background: one account said Pascal Yammine was formerly a Salesforce SVP/GM; that bio is not in the cited excerpts.
- FTZ benchmark wording: the release says about 3x faster sequentially and about 70x higher pricing output at max throughput, not 70x faster.

## Where the models disagreed (run 2)

- Total capital raised conflicts across sources: PitchBook $101M, CB Insights $130.85M (last round $35M about three years ago), and The Pricing News roughly $80M.
- Monetization: two accounts treated PitchBook’s software-as-a-service description as a subscription revenue model; another said the commercial model and revenue were not stated.
- Headcount: PitchBook lists 242 employees, while one account said headcount was not found.
- Ownership: PitchBook says Madison Dearborn has invested and the latest deal type is buyout/LBO; The Pricing News calls Zilliant an MDP portfolio company; one account said MDP acquired the company, which the excerpts do not state outright.
- Competitor sets conflict: PitchBook’s sample includes Competera, Odoo, Intelligence Node, Accent Technologies, and PERQ; CB Insights lists PROS, Model N, Pactum, and Celerity Enterprises and also RAPT Therapeutics. Vendavo was named in one account but does not appear in the source excerpts.
- Julius Hoesch is a leading chemical distributor in Zilliant’s release, but The Pricing News calls it a German industrial manufacturer.

## Answers

### council (x-ai/grok-4.7)

Cost: $0.1459

#### Run 1

## 1. What they do, who buys it, how they make money
Zilliant sells AI-driven B2B pricing and revenue software—price management, analytics, optimization, and configure-price-quote—and calls this pricing lifecycle management, including Price Manager, a Real-Time Pricing Engine, and Visual Analytics ([CB Insights](https://www.cbinsights.com/company/zilliant), [Zilliant](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).

Shown buyers are manufacturers and distributors; users are pricing and sales teams. Recent logos: FTZ (Danish automotive aftermarket) and Julius Hoesch (chemical distribution) ([CB Insights](https://www.cbinsights.com/company/zilliant), [Zilliant](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [Zilliant](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). In Zilliant’s survey of 300 manufacturing and distribution executives, 88% place pricing accountability with the CEO, CFO, or CRO ([Zilliant](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)). Subscription packaging is not stated. Revenue is not disclosed.

## 2. Recent news (last ~6 months, through Sept 2026)
- **8 Sept 2026:** FTZ selected Zilliant after its benchmark of 1,000 randomized requests: about 3x faster sequentially and about 70x higher pricing output at max throughput. FTZ has 300,000+ SKUs and more than DKK 2 billion in digital sales. Vendor-published ([Zilliant](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
- **28 April 2026:** *Pricing Without Control*: nearly all firms are changing prices, but only about half are confident in the financial impact; 23% use AI pricing tools, 20% non-AI vendor tools, and 18% spreadsheets ([Zilliant](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).

Just outside that window: Julius Hoesch (27 Jan 2026) will use Zilliant in Salesforce with SAP S/4HANA during a cloud cutover ([Zilliant](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). Oct 2025: agentic AI and an industry-first Model Context Protocol server for pricing ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)).

## 3. Funding, size, and financial signals
Private; founded 1999; Austin, Texas ([CB Insights](https://www.cbinsights.com/company/zilliant)). Madison Dearborn Partners portfolio company ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)). CB Insights: $130.85M raised; last round $35M about three years ago; other investors include Goldman Sachs, Austin Ventures, and Trellis Partners ([CB Insights](https://www.cbinsights.com/company/zilliant)). The Pricing News says roughly $80M—totals conflict ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)). Headcount and profitability: not found. Named a Leader in QKS Group’s Nov 2024 SPARK Matrix for B2B Price Optimization & Management ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)).

## 4. Leadership
Pascal Yammine is CEO ([Zilliant](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). No other executives appear in these sources.

## 5. Main competitors and how they differ
CB Insights lists PROS, Model N, Pactum, and Celerity Enterprises, plus RAPT Therapeutics, which does not fit this market ([CB Insights](https://www.cbinsights.com/company/zilliant)). These sources do not explain how rivals differ. Zilliant stresses pricing outside the ERP, Salesforce as the work surface, SAP S/4HANA integration, and real-time scale ([Zilliant](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg), [Zilliant](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).

## 6. Likely strategic priorities and open questions
Inferred from announcements, not a stated plan: digital-channel throughput, ERP-cutover deals, governance versus spreadsheets, and agentic AI. Ask about revenue and growth; Madison Dearborn’s hold period and exit; whether the 70x result repeats against PROS or Model N; and whether MCP features are live with customers.

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

#### Run 2

## 1. What they do, who buys it, and how they make money
Zilliant sells AI-driven B2B pricing and revenue-optimization software: price management, analytics, optimization, configure-price-quote, and agreement tools. Founded in 1999 and based in Austin ([CB Insights](https://www.cbinsights.com/company/zilliant)). Recent wins name Price Manager, a Real-Time Pricing Engine, and Visual Analytics ([FTZ release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). Buyers are pricing and sales teams at manufacturers and distributors; examples are auto-parts distributor FTZ and chemical distributor Julius Hoesch ([FTZ release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale); [Hoesch release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). PitchBook describes a software-as-a-service model ([PitchBook](https://pitchbook.com/profiles/company/46191-79)). Fees, contract terms, and revenue were not found.

## 2. Recent news and launches (last 6 months)
On 8 Sep 2026, FTZ Autodele & Værktøj selected Zilliant. FTZ has 300,000+ SKUs and more than DKK 2 billion in digital sales. Zilliant says FTZ’s test—1,000 randomized requests, same client, full response time—was about 3x faster sequentially and about 70x higher throughput at max load ([FTZ release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). On 28 Apr 2026, its Pricing Without Control survey of 300 manufacturing and distribution executives found 88% place pricing accountability with the CEO, CFO, or CRO, only about half confident in the financial impact, 23% using AI pricing tools, 20% non-AI vendor tools, and 18% still on spreadsheets ([survey](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)). Just older: Julius Hoesch selected Zilliant on 27 Jan 2026 during a move to SAP S/4HANA Public Cloud, with Salesforce as the entry point ([Hoesch release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). The Pricing News dates a Precision Pricing Platform to 23 Apr 2025 and an agentic-AI Model Context Protocol server to Oct 2025 ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)).

## 3. Funding, size, and financial signals
Private and PE-backed. PitchBook lists 242 employees, latest deal type buyout/LBO, Madison Dearborn Partners as an investor, and $101M raised ([PitchBook](https://pitchbook.com/profiles/company/46191-79)). CB Insights lists $130.85M total, a $35M round about three years ago, and investors including Madison Dearborn and Goldman Sachs ([CB Insights](https://www.cbinsights.com/company/zilliant)). The Pricing News says roughly $80M and calls Zilliant a Madison Dearborn portfolio company ([The Pricing News](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)). Revenue, ARR, and profitability were not found.

## 4. Leadership
Pascal Yammine is CEO ([FTZ release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). Other executives were not in these sources.

## 5. Main competitors and how they differ
CB Insights names PROS, Model N, Pactum, and Celerity Enterprises, plus RAPT Therapeutics, which is not a pricing peer ([CB Insights](https://www.cbinsights.com/company/zilliant)). PitchBook lists 32 competitors, including Competera, Odoo, Intelligence Node, Accent Technologies, and PERQ ([PitchBook](https://pitchbook.com/profiles/company/46191-79)). Neither source compares features or price. Zilliant’s stated contrast is lifecycle pricing as a Salesforce entry point, integrated with SAP S/4HANA, with governed real-time execution ([Hoesch release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg); [FTZ release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).

## 6. Likely strategic priorities and open questions
Inferred from announcements, not management guidance: real-time pricing for digital commerce, governance versus uncontrolled AI, and European distribution wins. Ask which capital total is current, Madison Dearborn’s hold period, revenue and growth, the mix of real-time commerce versus classic pricing, how deals are won against PROS and Model N, and whether agentic features are in live use.

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)
6. [Zilliant 2026 Company Profile: Valuation, Funding & Investors \| PitchBook](https://pitchbook.com/profiles/company/46191-79)

### anthropic/claude-sonnet-5.5

Cost: $0.0382

#### Run 1

# Zilliant Briefing (as of Oct 13, 2026)

## 1. What they do, who buys it, how they make money
Zilliant sells AI-driven pricing and revenue optimization software for B2B companies. Its products cover price management, analytics, optimization, and configure-price-quote tools. It was founded in 1999 and is based in Austin, Texas ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). Its customers are manufacturers and distributors, such as the Danish auto-parts supplier FTZ and the chemical distributor Julius Hoesch ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). Pricing and sales teams use the products. Per its survey, accountability for pricing sits with the CEO, CFO, or CRO in 88% of organizations ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)). **Revenue model and pricing: not found in the sources.** Software licensing is the likely model, but that is my inference.

## 2. Recent news (last 6 months)
- **Sept 8, 2026:** FTZ Autodele & Værktøj chose Zilliant Price Manager, Real-Time Pricing Engine, and Visual Analytics. FTZ has more than 300,000 SKUs and more than DKK 2B in digital sales. In FTZ's benchmark, Zilliant was about 3x faster sequentially and delivered about 70x higher throughput at maximum load ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). This is a vendor-published result.
- **April 28, 2026:** Zilliant released the "Pricing Without Control" report, based on 300 executives. Nearly all are adjusting prices, but only half are confident they understand the financial impact. 23% use AI pricing tools and 18% still use spreadsheets ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
- **Earlier context:** Agentic AI with an MCP server (Oct 2025), Pricing Plus (Nov 2025), and the Julius Hoesch win (Jan 2026) ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

## 3. Funding, size, financials
- It is private equity-backed. Investors include Madison Dearborn Partners, Goldman Sachs, and Austin Ventures. CB Insights shows $130.85M raised in total, with the last round of $35M about three years ago ([cbinsights.com](https://www.cbinsights.com/company/zilliant)).
- **Conflict:** another outlet says roughly $80M raised ([thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)). Treat the total as unverified. That outlet also calls Julius Hoesch an "industrial manufacturer," while Zilliant calls it a chemical distributor.
- **Revenue, headcount, profitability: not found.**

## 4. Leadership
Pascal Yammine is CEO ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). I found no other executives in these sources.

## 5. Competitors
CB Insights lists PROS, Model N, Pactum, and Celerity Enterprises, among others ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). It also lists RAPT Therapeutics, a biotech, which looks like a data error. **The sources don't say how these competitors differ.** Zilliant's own positioning is pricing managed outside the ERP, embedded in Salesforce, with deep SAP S/4HANA integration ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). It also stresses real-time performance at scale. Check competitor comparisons independently.

## 6. Likely priorities and open questions
**Priorities (inferred from the announcements):**
- Real-time pricing for digital channels
- Governance and a "single source of pricing truth"
- Agentic AI
- European expansion (FTZ, Julius Hoesch)
- Using its own research to drive demand

**Questions to ask:**
- How large is the business, and what is its growth rate?
- What is the ownership and exit outlook, given that Madison Dearborn is the investor?
- How is agentic AI/MCP adoption going in practice?
- How does Zilliant fare against PROS and Model N in head-to-head deals beyond the FTZ benchmark?
- What does the FTZ rollout timeline look like?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

#### Run 2

# Zilliant Briefing (as of 13 Oct 2026)

## 1. What they do, who buys it, how they make money
Zilliant sells AI-driven pricing and revenue optimization software for B2B manufacturers and distributors. Its products cover price management, analytics, optimization, CPQ and agreement management; it was founded in 1999 and is based in Austin ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). Buyers are pricing and sales teams, and the company says pricing accountability increasingly sits with the CEO, CFO or CRO ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)). Recent customers include FTZ (Danish auto-parts distributor) and Julius Hoesch (chemical distributor).

**Revenue model:** The sources don't state it. Pricing, contract structure and revenue are undisclosed, so ask.

## 2. Recent news (last ~6 months)
- **8 Sep 2026:** FTZ Autodele & Værktøj selected Zilliant Price Manager, Real-Time Pricing Engine and Visual Analytics. FTZ has 300,000+ SKUs and over DKK 2B in digital sales. Zilliant cites an FTZ benchmark showing roughly 3x faster sequential responses and about 70x higher throughput ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). This is a customer-sourced claim, relayed by Zilliant.
- **28 Apr 2026:** "Pricing Without Control" survey of 300 executives. Nearly all companies are adjusting prices, but only half are confident they understand the financial impact. 23% use AI pricing tools and 18% still use spreadsheets ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
- **Earlier, for context:** The Julius Hoesch win (Jan 2026) involves a Salesforce front end with SAP S/4HANA integration. Late-2025 launches were an Agentic AI MCP server (Oct), Pricing Plus (Nov) and the Precision Pricing Platform ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

## 3. Funding, size, financial signals
- Zilliant is private equity-backed. Investors include Madison Dearborn Partners and Goldman Sachs. CB Insights shows $130.85M raised in total, with the last round of $35M about three years ago ([cbinsights.com](https://www.cbinsights.com/company/zilliant)).
- **Discrepancy:** Another outlet says roughly $80M raised ([thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)). Treat the funding figures as unverified.
- Revenue, headcount, profitability and ARR were not found.

## 4. Leadership
Pascal Yammine is CEO ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)). I found no other executives, or Yammine's background, in these sources.

## 5. Competitors
CB Insights lists PROS, Model N, Pactum and Celerity Enterprises, among others ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). It also lists RAPT Therapeutics, which is clearly a data-quality error. The sources don't compare features or pricing. Zilliant's own positioning is to centralize pricing outside the ERP, embed it in Salesforce, and cover the full pricing lifecycle ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). Gartner named it a Representative Vendor in its 2025 B2B Profit Optimization Software Market Guide (same source).

## 6. Likely priorities and open questions
**Priorities (inferred from the announcements above):**
- Agentic AI and the MCP server.
- Real-time pricing performance for digital commerce.
- Governance as the pitch against "AI on fragmented systems."
- European distribution wins (Denmark, Germany).

**Questions to ask:**
- What are the revenue, growth and ownership timeline? Madison Dearborn's hold period is unknown.
- How much of the business is real-time/e-commerce versus traditional pricing?
- What is the commercial model?
- How does Zilliant win against PROS and Model N in head-to-head deals?
- How much customer adoption of the agentic features is there?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

### google/gemini-3.8-flash

Cost: $0.0204

#### Run 1

### 1. What They Do, Who Buys It, & How They Make Money
Zilliant provides AI-driven pricing lifecycle management software for B2B enterprises, unifying price optimization, list-price management, real-time calculation engines, CPQ, and commercial analytics ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [cbinsights.com](https://www.cbinsights.com/company/zilliant)). 

* **Target Customers:** Large B2B manufacturers and distributors with complex catalogs and volatile input costs, especially across automotive, industrial, and chemical verticals (e.g., FTZ, Julius Hoesch) ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)). Buyers are typically C-level executives (CEOs, CFOs, CROs) and heads of pricing or commercial operations ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
* **Monetization:** Enterprise SaaS subscriptions priced across modular platform tiers (Price Manager, Real-Time Pricing Engine, Visual Analytics, CPQ) plus implementation services ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [cbinsights.com](https://www.cbinsights.com/company/zilliant)).

### 2. Recent News & Launches (Last 6 Months)
* **FTZ Enterprise Win (Sept 2026):** Denmark’s automotive supplier FTZ selected Zilliant to modernize pricing across 300,000+ SKUs following head-to-head testing where Zilliant’s engine delivered ~70x higher output under maximum throughput conditions ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
* **Executive Pricing Research (April 2026):** Released the *Pricing Without Control* survey of 300 manufacturing and distribution leaders, highlighting that while 88% centralize pricing ownership in the C-suite, only half are confident in their financial impact due to tooling fragmentation ([zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)).
* **Agentic AI & Precision Pricing:** Followed its Model Context Protocol (MCP) server launch to let autonomous agents execute pricing decisions directly, embedding external pricing logic outside ERPs like SAP S/4HANA ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg), [thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)).

### 3. Funding, Size, & Financial Signals
* **Ownership & Capital:** Private company backed by Madison Dearborn Partners (acquired late 2021); previously raised over $80M–$130M in venture funding ([cbinsights.com](https://www.cbinsights.com/company/zilliant), [thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)).
* **Headquarters & Scale:** Headquartered in Austin, Texas; founded in 1999 ([cbinsights.com](https://www.cbinsights.com/company/zilliant)). As a private equity portfolio company, exact revenue and valuation metrics are kept private.

### 4. Leadership
* **Chief Executive Officer:** Pascal Yammine (formerly Senior VP & GM at Salesforce, leading Zilliant's enterprise and integration-heavy roadmap) ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).

### 5. Main Competitors & How They Differ
* **PROS:** The primary public competitor in dynamic pricing and CPQ. PROS has deep travel and airline roots alongside B2B; Zilliant focuses heavily on distributor/wholesale use cases, low-latency API calls for digital webshops, and ease of deployment alongside Salesforce ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg), [cbinsights.com](https://www.cbinsights.com/company/zilliant)).
* **Vendavo & Pricefx:** Both target enterprise manufacturing and distribution. Zilliant differentiates with its Real-Time Pricing Engine throughput benchmarks and its recent agentic AI/MCP protocol infrastructure ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).

### 6. Likely Strategic Priorities & Open Questions
* **Strategic Priorities:** 
  1. Win ERP modernization cutovers by positioning Zilliant as the pricing calculation hub integrated into SAP S/4HANA and Salesforce ([zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)).
  2. Capitalize on high-throughput digital commerce requirements in B2B supply chains ([zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)).
* **Open Questions:**
  1. How will native pricing and AI features rolled out directly inside core ERP/CRM platforms impact stand-alone pricing engine adoption?
  2. What is Madison Dearborn’s timeline and exit strategy (strategic acquisition vs. secondary sale)?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

#### Run 2

### 1. What They Do, Who Buys It, & How They Make Money
* **What they do:** Zilliant offers cloud-native B2B pricing lifecycle management and revenue optimization software (including Price Manager, Real-Time Pricing Engine, and Visual Analytics) designed to replace manual spreadsheets with automated, dynamic pricing [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
* **Target buyers:** Pricing, commercial, and sales leaders at large B2B manufacturers and distributors (e.g., automotive aftermarket, chemical distribution) [cbinsights.com](https://www.cbinsights.com/company/zilliant), [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg).
* **Monetization:** Enterprise Software-as-a-Service (SaaS) subscription model [pitchbook.com](https://pitchbook.com/profiles/company/46191-79).

### 2. Recent News & Launches (Last 6 Months)
* **FTZ Customer Win (Sept 2026):** FTZ, Denmark’s largest automotive supplier, selected Zilliant after an independent benchmark showed Zilliant delivered ~70x higher pricing output under maximum-throughput conditions compared to alternatives [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
* **Executive Market Research (April 2026):** Released its *Pricing Without Control* survey of 300 executives, highlighting that while 88% of organizations place pricing ownership in the C-suite, execution remains fragmented across spreadsheets and siloed software [zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes).
* **Platform Innovation:** Preceding this window, Zilliant rolled out an Agentic AI Model Context Protocol (MCP) server for autonomous pricing data retrieval and unified its suite under the Precision Pricing Platform [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg).

### 3. Funding, Size, & Financial Signals
* **Ownership:** Private equity-backed; acquired by Madison Dearborn Partners via a buyout/LBO [pitchbook.com](https://pitchbook.com/profiles/company/46191-79).
* **Funding:** Raised approximately $101M to $130.8M historically across prior venture and growth rounds [pitchbook.com](https://pitchbook.com/profiles/company/46191-79), [cbinsights.com](https://www.cbinsights.com/company/zilliant).
* **Headcount & Base:** ~242 employees; founded in 1999 and headquartered in Austin, Texas [pitchbook.com](https://pitchbook.com/profiles/company/46191-79), [cbinsights.com](https://www.cbinsights.com/company/zilliant). Revenue figures remain private.

### 4. Leadership
* **Chief Executive Officer:** Pascal Yammine [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale). Further C-suite roster details are not disclosed in recent company announcements.

### 5. Main Competitors & Differentiation
* **Competitors:** PROS, Vendavo, and broader pricing platforms such as Competera [pitchbook.com](https://pitchbook.com/profiles/company/46191-79).
* **Differentiation:** 
  * **Real-time execution speed:** Optimized to calculate customer-specific prices instantly in high-throughput digital eCommerce environments [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
  * **Ecosystem positioning:** Deep integration embedding pricing directly into front-office tools like Salesforce while decoupling pricing logic from complex ERP migrations like SAP S/4HANA [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg).

### 6. Likely Strategic Priorities & Open Questions
* **Strategic Priorities:**
  * Capitalizing on digital B2B commerce demand where real-time, API-driven price quoting is essential [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale).
  * Monetizing its Agentic AI and MCP server capabilities to differentiate from legacy optimization software [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg).
* **Open Questions to Ask:**
  * How are prospective customers responding to the Agentic AI rollout—are agents actually executing pricing autonomously, or is it mostly assisted workflows?
  * What is the typical implementation timeline when integrating alongside major ERP transformations like SAP S/4HANA?
  * What is Madison Dearborn’s long-term holding horizon or bolt-on acquisition strategy for the platform?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant 2026 Company Profile: Valuation, Funding & Investors \| PitchBook](https://pitchbook.com/profiles/company/46191-79)

### deepseek/deepseek-v4-pro

Cost: $0.0128

#### Run 1

# Zilliant Briefing

## 1. What They Do, Who Buys It, and How They Make Money

Zilliant provides AI-driven pricing lifecycle management software for B2B companies, helping them automate pricing operations, strengthen governance, and deliver customer-specific prices across digital channels. Its core offerings include price management, pricing analytics, price optimization, and tools for configuring prices, quoting, and managing sales agreements. The company targets pricing and sales teams in manufacturing and distribution industries, with recent wins in automotive aftermarket (FTZ) and chemical distribution (Julius Hoesch). Zilliant operates on a B2B SaaS model, selling to enterprises that manage high-volume, complex pricing environments. [cbinsights.com](https://www.cbinsights.com/company/zilliant)

## 2. Recent News and Launches (Last 6 Months)

Zilliant has been highly active:

- **September 2026**: Won FTZ Autodele & Værktøj, Denmark’s largest automotive supplier, after a real-time benchmark showed Zilliant was ~3x faster on sequential requests and ~70x faster at maximum throughput. FTZ will deploy Price Manager, Real-Time Pricing Engine, and Visual Analytics. [zilliant.com](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)

- **April 2026**: Released the *Pricing Without Control* report, surveying 300 senior executives. It found 88% of organizations place pricing accountability with the CEO, CFO, or CRO, yet only 23% use AI-enabled pricing solutions and 18% still rely on spreadsheets. [zilliant.com](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)

- **January 2026**: Announced Julius Hoesch, a German chemical distributor, as a customer. The company will use Zilliant integrated with Salesforce and SAP S/4HANA to automate cost pass-throughs and unify pricing. [zilliant.com](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)

- **Late 2025**: Launched Agentic AI with an industry-first Model Context Protocol (MCP) Server for autonomous pricing data retrieval, plus *Pricing Plus* for spreadsheet-heavy companies, and consolidated its portfolio under the *Precision Pricing Platform*. [thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

## 3. Funding, Size, and Financial Signals

Zilliant has raised **$130.85M** total, with its last round being a **$35M private equity raise** approximately three years ago. It is a portfolio company of **Madison Dearborn Partners**. Other investors include Goldman Sachs, Austin Ventures, and Trellis Partners. The company is private and does not disclose revenue, but its continued customer wins, product investment pace, and analyst recognition (Leader in QKS Group’s 2024 SPARK Matrix) suggest steady commercial traction. [cbinsights.com](https://www.cbinsights.com/company/zilliant) [thepricingnews.com](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

## 4. Leadership

**Pascal Yammine** is the Chief Executive Officer. He has been the public face of recent announcements, emphasizing the shift from manual pricing to governed, AI-enabled commercial decision-making. No other C-suite names were surfaced in recent materials.

## 5. Main Competitors and How They Differ

Key competitors include **PROS**, **Model N**, **Pactum**, and **Celerity Enterprises**. Zilliant differentiates through its end-to-end “pricing lifecycle management” approach—spanning strategy, execution, and analytics—and its recent emphasis on real-time performance at scale, agentic AI, and deep ERP/CRM integration (notably SAP S/4HANA and Salesforce). Its Precision Pricing Platform positioning targets the gap between pricing strategy and governed execution. [cbinsights.com](https://www.cbinsights.com/company/zilliant)

## 6. Likely Strategic Priorities and Open Questions

**Priorities**: Deepening AI capabilities (agentic, autonomous pricing); expanding in chemical and automotive distribution; displacing spreadsheet-based pricing; and embedding pricing governance into digital commerce workflows.

**Open Questions**: Revenue scale and profitability are unknown. The company’s reliance on private equity backing raises questions about exit timeline. How defensible is the “70x faster” performance claim against well-funded competitors like PROS? Will the MCP Server and agentic AI features drive meaningful adoption, or remain niche differentiators?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
3. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant ships a "Precision Pricing Platform" and picks up fresh analyst recognition](https://thepricingnews.com/articles/zilliant-precision-pricing-platform-analyst-recognition)

#### Run 2

### 1. What they do, who buys it, and how they make money
Zilliant sells a cloud-based pricing lifecycle management platform that helps B2B companies automate, govern, and optimize prices across channels. Its tools – Price Manager, a Real‑Time Pricing Engine, and Visual Analytics – handle list‑price calculations, discount guardrails, and customer‑specific deal pricing. The typical buyer is a large distributor or manufacturer in industrial, automotive, or chemical sectors that manages hundreds of thousands of SKUs and complex customer agreements. Revenue comes from SaaS subscriptions. [zilliant.com]

### 2. Recent news and launches (last 6 months)
- **September 2026:** Danish auto‑parts leader FTZ selected Zilliant after a head‑to‑head benchmark. In maximum‑throughput tests, Zilliant’s real‑time pricing engine delivered ~70× the output of the rival system, confirming its ability to handle high‑volume digital commerce (300,000+ SKUs, >DKK2B in digital sales). [zilliant.com]
- **April 2026:** The “Pricing Without Control” survey of 300 manufacturing and distribution executives found that 88% now place pricing accountability in the C‑suite, yet only half feel confident in understanding the financial impact. Only 23% use AI‑enabled pricing tools, and 18% still rely on spreadsheets. The report urges a unified source of pricing truth, cross‑functional alignment, and governance investment. [zilliant.com]

###3. Funding, size, and financial signals
Zilliant is privately held and backed by private equity firm Madison Dearborn Partners. Employee count is 242. [pitchbook.com] Total funding reported differs across sources: Pitchbook shows $101M raised, while CB Insights lists $130.85M, with a $35M round about three years ago. [cbinsights.com] The company has gone through a buyout/ LBO and is now in a growth phase, marked by platform consolidation and step‑function product launches.

###4. Leadeership
Pascal Yammine is the CEO. He has positioned the company around the idea that “pricing performance is not a technical detail” but a strategic capability that reaches customers at the moment of decision. [zilliant.com] Other C‑level names were not provided in the search results.

###5. Main competitors and how they differ
Pitchbook lists 32 competitors, including Competera, Odoo, Intelligence Node, Accent Technologies, and PERQ. [pitchbook.com] The search results lack detailed competitive differentiation, but Zilliant’s public positioning stresses three unique traits: a dedicated real‑time pricing engine that proved ~70×faster in a customer benchmark, tight governance features that prevent “fast but uncontrolled” decisions, and deep integration with SAP S/4HANA and Salesforce. [zilliant.com]

###6. Likely strategic priorities and open questions
Based on its recent moves, Zilliant is likely to focus on:
- Embedding pricing governance directly into digital commerce workflows, so every online quote is automated but explainable.
- Expanding its foothold in chemical and automotive distribution, where raw‑material volatility and customer‑specific contracts make real‑time pricing critical.
- Reinforcing the “single source of pricing truth” message, as called out in its own survey.

Key open questions: How sustainable is its real‑time speed advantage as competitors adopt AI? Can it convert survey respondents who still use spreadsheets when budgets remain tight? And will the ongoing buyout/LBO structure push toward a near‑term exit or allow continued product investment?

**Sources**

1. [FTZ Selects Zilliant After Real-Time Benchmark Confirms Superior Pricing Performance at Scale \| press release](https://zilliant.com/press-releases/ftz-selects-zilliant-after-real-time-benchmark-confirms-superior-pricing-performance-at-scale)
2. [Zilliant Survey: Executives Are Adjusting Prices More Than Ever but Losing Control of the Outcomes \| press release](https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes)
3. [Zilliant Closes 2025 with Strategic Product Innovation and Major Customer Win with Julius Hoesch GmbH & Co. KG \| press release](https://zilliant.com/press-releases/zilliant-closes-2025-with-strategic-product-innovation-and-major-customer-win-with-julius-hoesch-gmbh-co-kg)
4. [Zilliant - Products, Competitors, Financials, Employees, Headquarters Locations](https://www.cbinsights.com/company/zilliant)
5. [Zilliant 2026 Company Profile: Valuation, Funding & Investors \| PitchBook](https://pitchbook.com/profiles/company/46191-79)
