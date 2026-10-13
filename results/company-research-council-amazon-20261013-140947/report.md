# Council: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-13T14:09:47
- Variables: `company=Amazon`
- Judge: `openai/gpt-6-sol`
- Synthesizer: `x-ai/grok-4.7`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.6804 (contestants $0.1529, synthesis $0.4110, judge $0.0859, synthesis guess $0.0307)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent | Synthesis % | Why (judge's guess) |
|---|---|---|---|---|---|---|---|---|
| council (x-ai/grok-4.7) | 6.8 (6.7–7.0) | $0.2819 | 337.6s (184.6s–490.5s) | 8 (5–10) | 6 (6–7) | 0.2 | 99% | It combines the detailed AWS and Zoox figures, the high-margin-services framing, and the shareholder list, while adding qualifications to claims that appear elsewhere without them. |
| anthropic/claude-sonnet-5.5 | 6.6 (6.4–6.8) | $0.0401 | 22.1s (21.9s–22.4s) | 5 (5–5) | 6 (5–6) | 1.6 | 0% | The briefing is detailed, but its caveats about unverified revenue mix and missing financial figures read as a consistent source-checking approach. |
| deepseek/deepseek-v4-pro | 6.4 (6.0–6.8) | $0.0136 | 62.9s (42.3s–83.6s) | 5 (5–5) | 6 (5–6) | 4.7 | 0% | This is a more general briefing, with a distinct emphasis on business lines and institutional shareholders. |
| google/gemini-3.8-flash | 6.1 (5.7–6.4) | $0.0228 | 25.0s (22.8s–27.1s) | 5 (5–5) | 6 (5–6) | 2.7 | 0% | This is a shorter, more selective briefing focused on AWS, Zoox, and logistics, without the broader collection of caveats and details. |

The council row is the synthesizer's merge of the other answers. Its cost includes every contestant call plus the synthesis; its latency is the slowest contestant plus the synthesis. "Synthesis %" is the judge's guess, in a separate call after scoring, that the row is the merged answer (chance is 25% with 4 answers).

## Judge rationales

- **council (x-ai/grok-4.7)**: Its financial caveats and strategic questions are useful, but much of the precise recent reporting rests on cited material absent from the provided excerpts.
- **anthropic/claude-sonnet-5.5**: C clearly separates estimates from verified filings and offers useful questions, but numerous current claims cannot be checked against the supplied excerpts and the briefing appears to exceed the word limit.
- **deepseek/deepseek-v4-pro**: D is compact and covers all requested sections, but its strongest recent and strategic specifics lack support in the supplied excerpts.
- **google/gemini-3.8-flash**: A concise, concrete briefing, but many of its most meeting-relevant 2026 figures and developments are not verifiable from the supplied excerpts.

## Unsupported claims

- **council (x-ai/grok-4.7)** (run 1): The excerpts do not substantiate the H1 2026 delivery growth, Amazon Now footprint, Q2 AWS results, AI and chip run rates, or robotic-arm expansion.
- **council (x-ai/grok-4.7)** (run 1): The supplied excerpt supports the Supply Chain Services launch, but not the stated Leo or Zoox milestones.
- **council (x-ai/grok-4.7)** (run 1): The $220B capex guidance, earlier $200B estimate, and server break-even claim do not appear in the excerpts.
- **council (x-ai/grok-4.7)** (run 1): The excerpts do not establish Bezos's or Garman's roles or the 12-director board.
- **council (x-ai/grok-4.7)** (run 1): The cited PitchGrade excerpt does not name Vanguard, BlackRock or State Street as Amazon holders.
- **council (x-ai/grok-4.7)** (run 1): The detailed competitor comparisons and claimed chip, power and multi-cloud constraints are not supported by the excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The excerpts do not substantiate the Zoox and Leo milestones or Amazon Now's stated footprint.
- **anthropic/claude-sonnet-5.5** (run 1): The Q2 AWS results, AI and chip run rates, and FY2026 capex figures do not appear in the excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The excerpts do not establish Bezos's or Garman's roles or the board's size.
- **anthropic/claude-sonnet-5.5** (run 1): The detailed competitor comparisons and delivery-platform challenge are not established by the excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The H1 delivery-growth figure, robotic-arm plan, server break-even estimate, and identified chip, power and multi-cloud risks do not appear in the excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not substantiate the delivery-growth and Amazon Now figures, Q2 AWS and AI run rates, Leo and Zoox milestones, or robotic-arm expansion.
- **deepseek/deepseek-v4-pro** (run 1): The $220B capex guidance and earlier $200B estimate do not appear in the excerpts.
- **deepseek/deepseek-v4-pro** (run 1): PitchGrade's excerpt describes typical institutional holders, not verified Amazon-specific stakes for Vanguard, BlackRock and State Street.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not establish Bezos's or Garman's roles or the board's size.
- **deepseek/deepseek-v4-pro** (run 1): The detailed competitor comparisons, Amazon's claimed unique integration, and the assertion that competitors can underprice individual services are not established by the excerpts.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not substantiate the Q2 2026 AWS revenue, growth, run-rate, or AI and chip run-rate figures.
- **google/gemini-3.8-flash** (run 1): The supplied excerpts do not substantiate Zoox's exemption, paid-ride launch or airport expansion, or Leo's satellite count and rollout.
- **google/gemini-3.8-flash** (run 1): The $220B FY2026 capex projection and earlier $200B estimate do not appear in the excerpts.
- **google/gemini-3.8-flash** (run 1): The excerpts do not establish Bezos's or Garman's stated roles or the board's size.
- **google/gemini-3.8-flash** (run 1): The specific competitor comparisons and regional-fulfillment robotics priority are not established by the excerpts.
- **council (x-ai/grok-4.7)** (run 2): The May 2026 Alexa for Shopping launch and Rufus–Alexa+ merger.
- **council (x-ai/grok-4.7)** (run 2): The Zoox exemption and paid-ride dates, Leo satellite count and service timing, Amazon Now reach, and more-than-40% delivery growth.
- **council (x-ai/grok-4.7)** (run 2): The Corning fiber agreement is not shown in this answer's DYOR HQ excerpt.
- **council (x-ai/grok-4.7)** (run 2): The cited excerpt does not identify $716.9 billion specifically as FY2025 sales; the PitchGrade excerpt labels a similar figure as trailing-twelve-month revenue.
- **council (x-ai/grok-4.7)** (run 2): Q1 AWS sales and operating income, the Q2 AWS and AI run rates, and the $220 billion capex guidance.
- **council (x-ai/grok-4.7)** (run 2): The claimed $1.2 billion trailing free-cash-flow figure is absent from the supplied excerpt, so the stated conflict is not demonstrated.
- **council (x-ai/grok-4.7)** (run 2): The named leadership roles and board size, Shopify comparison, robotic-arm expansion plan, and specific bundling and self-preferencing concerns are not established by the excerpts cited for them.
- **anthropic/claude-sonnet-5.5** (run 2): The Zoox exemption, paid-ride dates, airport extension, and lack of disclosed Zoox financial results.
- **anthropic/claude-sonnet-5.5** (run 2): Amazon Leo's nearly 400 satellites and planned initial-service timing.
- **anthropic/claude-sonnet-5.5** (run 2): Amazon Now's reach and the more-than-40% growth in same-day and overnight items.
- **anthropic/claude-sonnet-5.5** (run 2): The approximately $220 billion capex expectation, AWS's $169 billion run rate, the two $25 billion run rates, and server and data-center lifetimes.
- **anthropic/claude-sonnet-5.5** (run 2): The named leadership roles and 12-director board are not visible in this answer's supplied Signals.AI excerpt.
- **anthropic/claude-sonnet-5.5** (run 2): Most of the specific retail, cloud, and delivery competitor comparisons attributed to Signals.AI, and the plan to more than double the robotic-arm fleet.
- **deepseek/deepseek-v4-pro** (run 2): Q1 2026 online- and physical-store sales of $64.3 billion and $5.8 billion, and AWS sales of $37.6 billion with $14.2 billion in operating income representing 59% of the company total.
- **deepseek/deepseek-v4-pro** (run 2): The May 2026 Alexa for Shopping launch and its described features.
- **deepseek/deepseek-v4-pro** (run 2): The Q2 AWS $169 billion run rate, separate $25 billion AI and chip run rates, nearly 400 Kuiper satellites, Amazon Now's geographic reach, and delivery growth above 40%.
- **deepseek/deepseek-v4-pro** (run 2): The $220 billion FY2026 capex plan and its stated allocation.
- **deepseek/deepseek-v4-pro** (run 2): AWS's roughly one-third global cloud share and expanding margins.
- **deepseek/deepseek-v4-pro** (run 2): Walmart's store-density advantage and the claim that Amazon's integrated businesses allow it to subsidize retail are not established by the excerpts cited for those particulars.
- **google/gemini-3.8-flash** (run 2): Third-party sellers account for about 62% of units sold.
- **google/gemini-3.8-flash** (run 2): Zoox began paid Las Vegas rides in August 2026 and extended service to the airport in September; Amazon Leo had nearly 400 satellites across 14 missions.
- **google/gemini-3.8-flash** (run 2): Q2 2026 revenue, operating income, AWS growth and revenue, and the two $25 billion AI-related run rates.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not substantiate $220 billion in 2026 capex; one instead estimates $125 billion–$145 billion.
- **google/gemini-3.8-flash** (run 2): The upper end of the $2.35 trillion–$2.85 trillion market-cap range, the roughly 30% AWS share, the $8 billion Anthropic partnership, and same-day perishable delivery in more than 2,300 cities.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not establish the specific FTC, bundling, and self-preferencing scrutiny described.

## Where the models disagreed (run 1)

- Zoox airport timing: two accounts say paid Las Vegas service later extended to the airport without a month; one says the airport expansion was by September 2026.
- Profit mix: one account stays qualitative (AWS a significant profit engine; ads and third-party services high-margin); others cite PitchGrade figures of about 50% e-commerce revenue, AWS about 17% of revenue and most operating profit at about a 37% margin, and one explicitly says those figures were not verified against filings.
- Leo's former name: one account says formerly Kuiper; another says formerly Project Kuiper.
- Shareholders: one account lists Vanguard, BlackRock, and State Street as major Amazon holders; the PitchGrade excerpt says they typically are the largest holders and often hold 15-25% of US public companies generally, not an Amazon-specific stake.

## Where the models disagreed (run 2)

- Satellite name: Answer A called it Project Kuiper; Answers B and C, and Investomine, call it Amazon Leo (formerly Project Kuiper). Briefing uses Amazon Leo.
- Q1 2026 sales growth: Answer A/Investopedia said +16.61%; Answer C/Deep Research Global said about +17%. Briefing uses 16.61%.
- 2026 capex: Answers A–C, citing Signals.ai, said about $220 billion of cash capex; Deep Research Global estimated $125–$145 billion of AI capex. Briefing uses $220 billion and does not treat the lower figure as the same measure.
- Free cash flow: Deep Research Global said trailing FCF fell to $1.2 billion from $25.9 billion; PitchGrade said $23.79 billion. Both are reported as unresolved.
- Cloud share: Answer A said roughly one-third; Answer C said about 30%. Briefing states only that AWS has the largest share and does not pick a percentage.
- Q2 consolidated results: Answer C reported revenue of $200.6 billion, operating income of $27.5 billion, and AWS revenue of $42.23 billion, up 36.7%; Answer B said those company totals were not found. They were omitted; the shared Q2 AWS $169 billion and $25 billion chip/AI run rates were kept.
- Market cap: PitchGrade states $2.35 trillion; Answer C gave $2.35–$2.85 trillion. Briefing uses $2.35 trillion.
- Zoox airport timing: Answer B said service was later extended to the airport; Answer C said September. Briefing does not name a month.
- Grocery pivot: Answer C said Fresh and Go closures were to focus on Whole Foods; the visible Investomine excerpt confirms the closures but not that Whole Foods-only plan. Briefing states the closures only.

## Answers

### council (x-ai/grok-4.7)

Cost: $0.2819

#### Run 1

# Amazon briefing
*As of October 2026*

## 1. What they do, who buys it, and how they make money
Amazon is a Seattle-based platform founded in 1994, with North America, International, and AWS segments, serving consumers, sellers, developers, enterprises, content creators, and advertisers ([signals.ai](https://signals.ai/reports/amzn)). It books gross sales on goods it owns and service fees—commissions, fulfillment, and shipping—on third-party sales, not sellers' merchandise value ([signals.ai](https://signals.ai/reports/amzn)). Prime fees are recognized over the membership; ads on clicks or impressions; AWS mainly on usage, plus some contracts ([signals.ai](https://signals.ai/reports/amzn)). AWS is a significant profit engine; advertising and third-party services are high-margin ([signals.ai](https://signals.ai/reports/amzn)). A filing-based revenue mix was not in these sources.

## 2. Recent news and launches (last 6 months)
Same-day and overnight deliveries grew more than 40% year over year in H1 2026; Amazon Now is in 9 countries and 250+ cities and towns ([signals.ai](https://signals.ai/reports/amzn)). In Q2 2026 AWS revenue was $42.23B, up 36.7%, operating income was $16.62B, and the run rate was $169B; AI and custom-chip revenue each topped a $25B run rate ([signals.ai](https://signals.ai/reports/amzn)). Supply Chain Services launched for outside customers in Q2 2026, with no separate results ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). Leo (formerly Kuiper) has nearly 400 satellites; initial service is planned later in 2026, and mass-market service is not established ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). Zoox received a U.S. exemption in July, started paid Las Vegas rides on 10 August 2026, and later added the airport ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). Robotic arms are set to more than double in FY2026 ([signals.ai](https://signals.ai/reports/amzn)).

## 3. Funding, size, and financial signals
Amazon is public (NASDAQ: AMZN); there is no venture round to report. These sources omit total revenue, net income, and market cap. About 1,576,000 people worked there on 31 December 2025 ([signals.ai](https://signals.ai/reports/amzn)). FY2026 cash capex is guided to about $220B, up from about $200B, mostly for AI and AWS ([signals.ai](https://signals.ai/reports/amzn)). Vanguard, BlackRock, and State Street are named as typical large holders, without an Amazon-specific stake ([pitchgrade.com](https://pitchgrade.com/companies/amazon)).

## 4. Leadership
Andrew R. Jassy is president and CEO; Jeffrey P. Bezos is executive chair of a 12-director board; Matthew S. Garman is AWS CEO ([signals.ai](https://signals.ai/reports/amzn)). CFO and retail leadership were not in these sources.

## 5. Main competitors and how they differ
Walmart competes with stores, everyday low prices, and fulfillment or pickup; Shopify leaves the storefront and customer relationship with the merchant; Alibaba, Temu, and Shein compete on selection and price ([signals.ai](https://signals.ai/reports/amzn)). Azure and Google Cloud are the main cloud rivals; Oracle and specialists contest selected workloads ([signals.ai](https://signals.ai/reports/amzn)). Amazon differs by combining Prime, the marketplace, fulfillment, ads, and AWS ([signals.ai](https://signals.ai/reports/amzn)).

## 6. Likely strategic priorities and open questions
Priorities in these sources: AI build-out (Bedrock, Trainium, and capacity), faster delivery, robotics, and early commercialization of Leo, Zoox, and external logistics ([signals.ai](https://signals.ai/reports/amzn); [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc); [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

Open questions include whether about $220B of capex still supports free cash flow—management says servers break even in slightly under three years ([signals.ai](https://signals.ai/reports/amzn)); chip, power, and multi-cloud constraints ([signals.ai](https://signals.ai/reports/amzn)); regulatory treatment of scale; and whether Leo hits its window and Zoox economics become material, since neither is separately disclosed ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
4. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

#### Run 2

## 1. What they do, who buys it, and how they make money

Amazon’s mission is to make customers’ lives better and easier by inventing on their behalf ([aboutamazon.com](https://www.aboutamazon.com/about-us)). It sells consumer products online and in stores, AWS cloud, seller services, advertising, subscriptions, and digital content ([signals.ai](https://signals.ai/reports/amzn)). Customers include consumers, sellers, developers, enterprises, content creators, and advertisers ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)).

FY2025 net sales were $716.9 billion ([deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)): online stores $269.3B (37.6%), third-party seller services $172.2B (24.0%), AWS $128.7B (18.0%), advertising $68.6B (9.6%), subscriptions $49.6B (6.9%), and physical stores $22.6B (3.1%) ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)). Third-party revenue is fees only ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)). Retail is the largest revenue source; AWS generates most operating income ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)).

## 2. Recent news and launches (last 6 months)

May 2026: Alexa for Shopping merged Rufus with Alexa+ ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). Q2, Supply Chain Services launched for external customers; Zoox received a July U.S. exemption, began paid Las Vegas rides on 10 August, and later added the airport; Amazon Leo (formerly Project Kuiper) has nearly 400 satellites, with initial service planned later in 2026 and mass-market service not yet established ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). Amazon Now is in nine countries and 250+ cities; same-day and overnight items grew over 40% year over year in H1 ([signals.ai](https://signals.ai/reports/amzn)). Standalone Fresh and Go stores closed ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). A multi-billion-dollar Corning fiber agreement supports data-center buildouts ([dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)).

## 3. Funding, size, and financial signals

Amazon is publicly traded (AMZN) ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). Market cap is $2.35 trillion ([pitchgrade.com](https://pitchgrade.com/companies/amazon)); headcount was about 1,576,000 at year-end 2025 ([signals.ai](https://signals.ai/reports/amzn)). Q1 2026 net sales were $181.5 billion, up 16.61%, and net income $30.3 billion, up 76.65% ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). AWS sales were $37.6 billion, up 28% ([deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)), with operating income of $14.2 billion, 59% of the total ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). In Q2, AWS hit a $169 billion annualized run rate, and chips and AI each exceeded $25 billion ([signals.ai](https://signals.ai/reports/amzn)). Guided 2026 cash capex is about $220 billion, mostly for AI and AWS ([signals.ai](https://signals.ai/reports/amzn)). Free-cash-flow figures conflict ($1.2B trailing vs $23.79B) ([deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report); [pitchgrade.com](https://pitchgrade.com/companies/amazon)).

## 4. Leadership

Andrew R. Jassy is president and CEO, Jeffrey P. Bezos executive chair, and Matthew S. Garman AWS CEO. The board has 12 directors ([signals.ai](https://signals.ai/reports/amzn)).

## 5. Main competitors and how they differ

Amazon has 40.5% of U.S. online sales, Walmart 9.2%, and eBay about 3% ([bbc.com](https://www.bbc.com/news/articles/cg7p5nr307mo)). Walmart competes on store density and low prices; Temu and Shein on ultra-low prices; eBay on auctions and second-hand goods ([bbc.com](https://www.bbc.com/news/articles/cg7p5nr307mo)). Shopify lets merchants own the customer ([signals.ai](https://signals.ai/reports/amzn)). Azure is the main public cloud rival, Google Cloud the other scaled rival; AWS has the largest share ([dyorhq.ai](https://dyorhq.ai/reports/amazoncominc); [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)). AWS profit funds retail ([bbc.com](https://www.bbc.com/news/articles/cg7p5nr307mo)).

## 6. Likely strategic priorities and open questions

Priorities include AI and custom chips (Bedrock, Trainium), faster delivery, more than doubling the robotic-arm fleet in 2026, and Rufus and agentic shopping ([signals.ai](https://signals.ai/reports/amzn); [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)). Open questions: whether about $220 billion of capex pays off before depreciation and energy costs compress margins ([signals.ai](https://signals.ai/reports/amzn)); whether Zoox, Leo, and Supply Chain Services become material without separate financials ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)); and how regulators respond to bundling, self-preferencing, and cross-market scale ([dyorhq.ai](https://dyorhq.ai/reports/amazoncominc); [signals.ai](https://signals.ai/reports/amzn)).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)
6. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)
7. [About Amazon: Mission, businesses, and innovation](https://www.aboutamazon.com/about-us)
8. [Amazon (company)](https://en.wikipedia.org/wiki/Amazon_(company))
9. [How Amazon Makes Money](https://www.investopedia.com/how-amazon-makes-money-4587523)
10. [Why does Amazon have no Western rivals?](https://www.bbc.com/news/articles/cg7p5nr307mo)

### anthropic/claude-sonnet-5.5

Cost: $0.0401

#### Run 1

# Amazon briefing (as of 13 Oct 2026)

## 1. What they do, who buys it, how they make money
Amazon is a Seattle-based platform founded in 1994 with about 1,576,000 employees at end-2025. It reports three segments: North America, International and AWS. Its customers are consumers, sellers, developers, enterprises, content creators and advertisers ([signals.ai](https://signals.ai/reports/amzn)).

Revenue comes from several models:
- **First-party retail:** Amazon resells products and records the gross sale.
- **Third-party sellers:** Amazon earns commissions plus fulfillment and shipping fees.
- **Prime:** membership fees are recognized over the subscription period.
- **Advertising:** revenue is recognized on clicks or impressions.
- **AWS:** billed mainly on usage, with some fixed-term contracts ([signals.ai](https://signals.ai/reports/amzn)).

One secondary source estimates e-commerce at about 50% of revenue on thin margins. It puts AWS at roughly 17% of revenue but the majority of operating profit, at around 37% margin ([pitchgrade.com](https://pitchgrade.com/companies/amazon)). I could not verify these figures against filings.

## 2. Recent news and launches
- **Amazon Supply Chain Services:** launched in Q2 2026 for external business customers. Its returns are not separately reported ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Zoox:** a US regulatory exemption in July allowed paid rides. Paid Las Vegas service began 10 August and has since extended to the airport ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Amazon Leo (formerly Kuiper):** nearly 400 satellites are in orbit. Initial service is planned for later in 2026, and mass-market service is not yet established ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Amazon Now:** available in 9 countries and over 250 cities and towns ([signals.ai](https://signals.ai/reports/amzn)).

## 3. Funding, size and financial signals
Amazon is a public company, so there is no venture funding to report. My sources did not include total revenue, net income or market cap, so I can't give those.

What the sources do show:
- **AWS Q2 2026:** revenue was $42.23B, up 36.7%, with operating income of $16.62B and a $169B annualized run rate.
- **AWS chips and AI:** each has a run rate above $25B.
- **Capex:** FY2026 cash capex is guided to about $220B, up from about $200B, mostly for AI and AWS ([signals.ai](https://signals.ai/reports/amzn)).

## 4. Leadership
- Andrew Jassy is president and CEO.
- Jeff Bezos is executive chair.
- Matt Garman is CEO of AWS.
- The board has 12 directors ([signals.ai](https://signals.ai/reports/amzn)).

I found nothing on other executives, such as the CFO or retail leadership.

## 5. Main competitors and how they differ
- **Retail:** Walmart competes on store density, everyday low prices and its fulfillment services. Shopify lets merchants own the customer relationship. Alibaba, Temu and Shein compete on selection and low prices ([signals.ai](https://signals.ai/reports/amzn)).
- **Cloud:** Microsoft Azure and Google Cloud are the main scaled rivals. Oracle and specialist providers compete for select workloads ([signals.ai](https://signals.ai/reports/amzn)).
- **Convenience:** delivery platforms challenge Amazon on last-mile delivery.
- **Amazon's edge:** it integrates Prime, the marketplace, fulfillment, advertising and AWS in one company.

## 6. Likely priorities and open questions
**Priorities**
- **AI infrastructure:** Bedrock, Trainium chips and capacity build-out.
- **Faster delivery:** same-day and overnight items grew more than 40% in the first half of 2026.
- **Warehouse robotics:** management plans to more than double its fleet of robotic arms.
- **New bets:** Leo, Zoox and supply chain services ([signals.ai](https://signals.ai/reports/amzn); [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)).

**Open questions**
- Will returns justify $220B of capex? Management says servers break even in slightly under three years ([signals.ai](https://signals.ai/reports/amzn)).
- How constrained are chip and power supplies, and how far will customers spread work across multiple clouds? Both are flagged as risks ([signals.ai](https://signals.ai/reports/amzn)).
- How will regulators treat Amazon's scale across adjacent markets?
- Can Leo reach commercial service on schedule, and what are the Zoox economics? Neither is separately disclosed ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
4. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

#### Run 2

# Amazon briefing (as of 13 Oct 2026)

## 1. What they do, who buys it, how they make money
Amazon sells consumer products through online and physical stores. It also sells AWS cloud infrastructure and monetizes traffic through seller services, advertising, subscriptions and digital content ([signals.ai](https://signals.ai/reports/amzn)). Its customers fall into seven groups: consumers, sellers, developers, enterprises, content creators, advertisers and employees ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)).

FY2025 net sales by line ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)):
- Online stores: $269.3B (37.6%)
- Third-party seller services: $172.2B (24.0%)
- AWS: $128.7B (18.0%)
- Advertising: $68.6B (9.6%)
- Subscriptions: $49.6B (6.9%)
- Physical stores: $22.6B (3.1%)

Amazon books gross revenue on goods it owns. On third-party goods it books only fees, so reported revenue understates merchandise volume ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)).

## 2. Recent news and launches
- **Q2 2026:** Amazon launched Amazon Supply Chain Services for external business customers. Its returns are not separately reported ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Zoox:** A US regulatory exemption in July allowed paid rides. Paid Las Vegas service launched 10 August and later extended to the airport. Fare revenue and profit are not disclosed ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Amazon Leo (formerly Kuiper):** Nearly 400 satellites are in orbit. Initial service is planned for later in 2026, and mass-market service is not yet established ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Q2 call (30 July):** Amazon Now is in 9 countries and more than 250 cities and towns. Same-day and overnight items grew more than 40% year over year in H1 ([signals.ai](https://signals.ai/reports/amzn)).

## 3. Funding, size, financial signals
Amazon is public, so there is no funding round to report. Signals:
- Management expects about $220B of 2026 cash capex, up from about $200B, mostly for AI and AWS ([signals.ai](https://signals.ai/reports/amzn)).
- AWS reached a $169B annualized run rate in Q2. AWS chips and AI revenue each run above $25B annually ([signals.ai](https://signals.ai/reports/amzn)).
- Servers and networking typically break even in slightly under three years. Data centers are expected to last more than 30 years ([signals.ai](https://signals.ai/reports/amzn)).

I did not find total revenue, operating income or free cash flow figures in the sources reviewed.

## 4. Leadership
The 2026 Form 10-K lists Andrew Jassy as president and CEO, Jeffrey Bezos as executive chair, and Matthew Garman as AWS CEO. The board has 12 directors ([signals.ai](https://signals.ai/reports/amzn)).

## 5. Main competitors
- **Retail:** Walmart competes on store density, low prices and fulfillment services. Shopify lets merchants own the customer relationship. Alibaba, Temu and Shein compete on selection and price ([signals.ai](https://signals.ai/reports/amzn)).
- **Cloud and AI:** Microsoft Azure and Google Cloud are the main scaled rivals. Oracle and specialized providers compete for selected workloads ([signals.ai](https://signals.ai/reports/amzn)). Azure is described as the principal public competitor for cloud workloads ([dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)).
- **Delivery:** Delivery platforms challenge Amazon on convenience and last-mile density ([signals.ai](https://signals.ai/reports/amzn)).

Amazon's differentiator is integration: Prime, the marketplace, fulfillment, advertising and AWS reinforce one another ([signals.ai](https://signals.ai/reports/amzn)).

## 6. Likely priorities and open questions
**Priorities** (stated):
- AI and custom chips
- Faster delivery
- Robotics: management plans to more than double its robotic arm fleet in 2026 ([signals.ai](https://signals.ai/reports/amzn))
- Free cash flow
- Product lines including Bedrock, Trainium, Rufus and agentic shopping ([dyorhq.ai](https://dyorhq.ai/reports/amazoncominc))

**Open questions** (my inference, not from the sources):
- When will the ~$220B capex show up as returns?
- Can Zoox, Leo and Supply Chain Services become material, given that none reports separate financials?
- How will competitive and regulatory pressure on its scale play out? The sources flag cross-market regulatory challenges and multi-cloud customers as exposures ([signals.ai](https://signals.ai/reports/amzn)).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)

### deepseek/deepseek-v4-pro

Cost: $0.0136

#### Run 1

# Amazon Briefing
*Prepared for an upcoming meeting – October 2026*

## 1. What they do, who buys it, and how they make money
Amazon is a multi‑business platform combining a vast retail marketplace, cloud infrastructure (AWS), advertising, subscriptions (Prime), digital content, and logistics services. Customers include consumers, third‑party sellers, developers, enterprises, governments, and advertisers.  
- **Retail**: Amazon sells products it owns (first‑party) and earns fees when third‑party sellers use its marketplace, fulfillment, and shipping services. Third‑party seller services are recognized as service revenue, not gross merchandise value. [signals.ai](https://signals.ai/reports/amzn)  
- **AWS**: Provides compute, storage, AI, and other cloud services on a pay‑as‑you‑go or contract basis. [signals.ai](https://signals.ai/reports/amzn)  
- **Subscriptions & advertising**: Prime fees are recognized over the membership period; advertising revenue is generated from clicks/impressions on sponsored, display, and video ads. [signals.ai](https://signals.ai/reports/amzn)  
- **Newer bets**: Amazon Leo (satellite broadband) and Zoox (autonomous ride service) are early‑stage revenue opportunities. [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)

## 2. Recent news and launches (last 6 months)
- **Delivery & convenience**: Same‑day/overnight deliveries grew >40% YoY in H1 2026; Amazon Now (ultra‑fast delivery) is live in 9 countries and 250+ cities. [signals.ai](https://signals.ai/reports/amzn)  
- **AWS & AI**: AWS hit a $169B annualized revenue run rate in Q2 2026; AI revenue and custom chip revenue each surpassed a $25B annual run rate. [signals.ai](https://signals.ai/reports/amzn)  
- **Satellite broadband**: Nearly 400 Leo satellites in orbit; initial service rollout expected later in 2026. [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)  
- **Autonomous rides**: Zoox launched paid rides in Las Vegas in August 2026, later extending to the airport. [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)  
- **Logistics & robotics**: Amazon Supply Chain Services opened to external businesses; the fleet of robotic arms is set to more than double in FY2026. [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained) [signals.ai](https://signals.ai/reports/amzn)

## 3. Funding, size, and financial signals
Amazon is a publicly traded company (NASDAQ: AMZN). Major institutional shareholders include Vanguard, BlackRock, and State Street. [pitchgrade.com](https://pitchgrade.com/companies/amazon)  
- **Scale**: ~1,576,000 full‑ and part‑time employees as of Dec. 31, 2025. [signals.ai](https://signals.ai/reports/amzn)  
- **Capital intensity**: Management raised FY2026 capex guidance to ~$220B (up from ~$200B), with the majority directed to AI and AWS. [signals.ai](https://signals.ai/reports/amzn)  
- **Profit drivers**: AWS is a significant profit engine; advertising and third‑party seller services are high‑margin. The company emphasizes long‑term free cash flow generation to fund infrastructure. [signals.ai](https://signals.ai/reports/amzn)

## 4. Leadership
- **CEO**: Andrew R. Jassy (President & CEO)  
- **Executive Chair**: Jeffrey P. Bezos  
- **AWS CEO**: Matthew S. Garman  
- **Board**: 12 directors, with Bezos as executive chair and Jassy as CEO. [signals.ai](https://signals.ai/reports/amzn)

## 5. Main competitors and how they differ
- **Retail**: Walmart (store density, everyday‑low‑price, Walmart Fulfillment Services); Shopify (merchant‑owned storefronts); cross‑border platforms like Temu, Shein, and Alibaba. [signals.ai](https://signals.ai/reports/amzn)  
- **Cloud**: Microsoft Azure and Google Cloud are the primary scaled rivals; Oracle and specialized providers compete for specific workloads. [signals.ai](https://signals.ai/reports/amzn)  
- **Differentiation**: Amazon’s model is uniquely integrated—Prime bundles shipping and content, the marketplace adds selection, fulfillment speeds delivery, advertising monetizes shopping intent, and AWS provides a separate enterprise platform. Competitors can underprice individual services, and enterprises often use multiple clouds. [signals.ai](https://signals.ai/reports/amzn)

## 6. Likely strategic priorities and open questions
- **Priorities**: Massive AI/cloud infrastructure build‑out ($220B capex); expanding ultra‑fast delivery and Amazon Now; monetizing Leo satellite broadband and Zoox robotaxi service; growing high‑margin advertising and third‑party services; deploying robotics to lower unit costs. [signals.ai](https://signals.ai/reports/amzn) [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)  
- **Open questions**: Can Amazon sustain such high capex while preserving free cash flow? How will regulatory scrutiny of its scale across markets evolve? Will Leo and Zoox become material revenue streams? How will intensifying retail and cloud competition affect margins?

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
4. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)
5. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)

#### Run 2

**1. What they do, who buys it, and how they make money**  
Amazon strives “to make customers’ lives better and easier every day by relentlessly inventing on their behalf” [aboutamazon.com]. It operates the world’s largest online retail marketplace, cloud computing (AWS), a growing advertising business, subscription services including Prime, and devices like Alexa and Kindle. Consumers, businesses, and governments all buy from or through Amazon. In Q1 2026, total net sales reached $181.5 billion, with online‑store sales at $64.3 billion and physical‑store sales at $5.8 billion [investopedia.com]. AWS generated $37.6 billion in sales and a $14.2 billion operating income—59 % of the company’s total—making it the primary profit engine [investopedia.com]. Third‑party seller services, subscriptions, and advertising also contribute substantially, while Amazon’s model blends products it owns with a marketplace for independent sellers [signals.ai, investopedia.com].

**2. Recent news and launches (last 6 months)**  
- **May 2026:** Amazon launched “Alexa for Shopping,” an AI‑powered shopping assistant that merges the Rufus chatbot with Alexa + to compare products, track prices, and automate purchases across its app, site, and Echo devices [investopedia.com].  
- **July 2026 (Q2 earnings):** AWS reached a $169 billion annualised revenue run rate; AI and custom‑chip revenues each surpassed a $25 billion run rate [signals.ai]. Project Kuiper has nearly 400 satellites in orbit, building toward a global satellite internet service [signals.ai]. Same‑day/overnight deliveries grew over 40 % year‑over‑year in the first half of 2026, and Amazon Now expanded to nine countries and 250 + cities [signals.ai]. Capital expenditure guidance was raised to ~$220 billion for FY2026, mostly for AI and AWS infrastructure [signals.ai].

**3. Funding, size, and financial signals**  
Amazon is publicly traded (AMZN). Q1 2026 net income surged 76.65 % to $30.3 billion, driven by revenue growth and disciplined operating‑expense growth [investopedia.com]. The company’s planned $220 billion capex for FY2026 signals massive commitment to AI, cloud, and logistics capacity [signals.ai]. AWS’s roughly one‑third share of the global cloud market and its expanding margins provide a durable cash‑flow foundation.

**4. Leadership**  
- **Andrew R. Jassy:** President and CEO  
- **Jeffrey P. Bezos:** Executive Chair  
- **Matthew S. Garman:** CEO of Amazon Web Services  
The board comprises 12 directors, with Bezos as executive chair and Jassy as CEO [signals.ai].

**5. Main competitors and how they differ**  
In U.S. e‑commerce, Amazon commands 40.5 % of online sales vs. Walmart’s 9.2 % and eBays ~3 % [bbc.com]. Walmart leverages store density and everyday‑low‑price; Temu and Shein compete on rock‑bottom prices for cross‑border goods [bbc.com, signals.ai]. In cloud, Microsoft Azure and Google Cloud are the principal scaled rivals, though AWS retains roughly a third of the market [investopedia.com]. Amazon’s advantage is its integrated ecosytem: Prime combines fast shipping and content, the marketplace widens selection, fulfillment underpins speed, advertising monetises intent, and AWS supplies enterprise infrastructure—allowing it to subsidise lower‑margin retail with cloud profits. Competitors can underprice single services, but few can replicate this breadth [signals.ai, bbc.com].

**6. Likely strategic priorities and open questions**  
Priorities include rapidly scaling AI and cloud capacity (the $220 billion capex plan), monetising generative AI through shopping assistants and AWS services, delivering global broadband via Project Kuiper, and driving further delivery speed and cost efficiency with robotics [signals.ai]. Key open questions: Can Kuiper compete against Starlink and become a meaningful revenue stream? Will the heavy AI‑infrastructure spending compress margins or pay off quickly? Can Amazon hold its retail lead as Temu, Shein, and Walmart sharpen their offerings? And how will regulators in multiple markets respond to its growing power across adjacent sectors? [signals.ai]

**Sources**

1. [About Amazon: Mission, businesses, and innovation](https://www.aboutamazon.com/about-us)
2. [Amazon (company)](https://en.wikipedia.org/wiki/Amazon_(company))
3. [How Amazon Makes Money](https://www.investopedia.com/how-amazon-makes-money-4587523)
4. [Why does Amazon have no Western rivals?](https://www.bbc.com/news/articles/cg7p5nr307mo)
5. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)

### google/gemini-3.8-flash

Cost: $0.0228

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
Amazon operates a global commerce, cloud, and digital services platform serving consumers, third-party merchants, enterprises, developers, and advertisers ([signals.ai](https://signals.ai/reports/amzn)). Revenue streams include:
* **Retail & Marketplace:** Direct first-party product sales and commissions/fulfillment fees (Fulfillment by Amazon) from third-party sellers ([signals.ai](https://signals.ai/reports/amzn)).
* **Cloud (AWS):** Compute, storage, database, and AI capacity sold via usage-based billing or multi-year enterprise contracts ([signals.ai](https://signals.ai/reports/amzn)).
* **Advertising & Subscriptions:** High-margin sponsored search/video ad placements and Prime membership recurring fees ([signals.ai](https://signals.ai/reports/amzn)).

### 2. Recent News and Launches (Last 6 Months)
* **AWS & Custom Silicon:** Both AWS AI revenue and in-house AWS chip offerings reached annualized run rates above $25B in Q2 2026 ([signals.ai](https://signals.ai/reports/amzn)).
* **Autonomous Mobility:** Subsidiary Zoox secured a U.S. regulatory exemption and launched paid commercial robotaxi operations in Las Vegas in August 2026, expanding to the airport by September 2026 ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
* **Logistics & Satellites:** Launched external logistics offering "Amazon Supply Chain Services" ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)). Amazon Leo (formerly Project Kuiper) expanded to nearly 400 low-Earth-orbit satellites ahead of commercial rollout ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

### 3. Funding, Size, and Financial Signals
* **Workforce:** Employed approximately 1,576,000 full- and part-time workers as of year-end 2025 ([signals.ai](https://signals.ai/reports/amzn)).
* **AWS Performance:** AWS hit a $169B annualized run rate in Q2 2026, generating $42.23B in quarterly revenue (up 36.7% YoY) ([signals.ai](https://signals.ai/reports/amzn)). AWS drives the majority of operating income with margins near 37% ([pitchgrade.com](https://pitchgrade.com/companies/amazon)).
* **Capital Expenditures:** Projecting cash capex of roughly $220B in FY2026, raised from an earlier $200B estimate, directed largely into AI and AWS data center infrastructure ([signals.ai](https://signals.ai/reports/amzn)).

### 4. Leadership
* **Andrew R. Jassy:** President and Chief Executive Officer ([signals.ai](https://signals.ai/reports/amzn)).
* **Jeffrey P. Bezos:** Founder and Executive Chair of the 12-member board ([signals.ai](https://signals.ai/reports/amzn)).
* **Matthew S. Garman:** Chief Executive Officer of Amazon Web Services ([signals.ai](https://signals.ai/reports/amzn)).

### 5. Main Competitors and How They Differ
* **Retail & Marketplaces:** Walmart challenges Amazon via physical store density and store-based pickup ([signals.ai](https://signals.ai/reports/amzn)); Temu and Shein undercut on direct-from-China retail pricing ([signals.ai](https://signals.ai/reports/amzn)); Shopify powers direct-to-consumer stores where merchants retain full customer data ([signals.ai](https://signals.ai/reports/amzn)).
* **Cloud & AI Infrastructure:** Microsoft Azure and Google Cloud compete aggressively for enterprise AI and cloud workloads, leveraging their existing business software ecosystems ([signals.ai](https://signals.ai/reports/amzn), [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)).

### 6. Likely Strategic Priorities and Open Questions
* **Strategic Priorities:** Scaling AI infrastructure and proprietary Trainium chips ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)); expanding regional fulfillment robotics to lower unit delivery costs ([signals.ai](https://signals.ai/reports/amzn)); commercializing Amazon Leo satellite broadband ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
* **Open Questions:** Can Amazon generate adequate free cash flow returns to justify a massive $220B capex pace in FY2026 ([signals.ai](https://signals.ai/reports/amzn))? How will cross-border e-commerce discounters impact retail marketplace take rates?

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
4. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

#### Run 2

### 1. What They Do, Who Buys It, & How They Make Money
Amazon operates a global retail, cloud, advertising, logistics, and digital services platform [signals.ai](https://signals.ai/reports/amzn). Customers comprise individual consumers (shopping, Prime media), third-party (3P) sellers, advertisers, and enterprises/developers utilizing cloud infrastructure [signals.ai](https://signals.ai/reports/amzn). 

Amazon generates revenue through:
* **First-Party Retail & 3P Seller Services:** Direct online/physical store sales and 3P commissions/fulfillment fees (3P sellers account for ~62% of units sold) [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report).
* **AWS:** Enterprise cloud infrastructure, computing, storage, database, and AI model hosting [signals.ai](https://signals.ai/reports/amzn).
* **Advertising & Subscriptions:** Search-intent product advertising, video ads, and Prime recurring membership fees [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained), [pitchgrade.com](https://pitchgrade.com/companies/amazon).

### 2. Recent News & Launches
* **Autonomous Mobility:** Zoox launched commercial, paid robotaxi operations in Las Vegas in August 2026, extending service to the airport in September under a U.S. regulatory exemption [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Satellite Broadband:** Amazon Leo (formerly Project Kuiper) expanded its low-Earth-orbit constellation to nearly 400 satellites in orbit across 14 missions by September 2026 ahead of commercial rollouts [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Physical Grocery Pivot:** Amazon closed standalone Amazon Fresh and Amazon Go stores to focus physical grocery expansion around Whole Foods Market formats [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **AI Infrastructure:** Amazon entered a multi-billion-dollar optical fiber supply agreement with Corning to support data center buildouts [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc).

### 3. Funding, Size, & Financial Signals
* **Size:** Market capitalization sits around $2.35T–$2.85T [pitchgrade.com](https://pitchgrade.com/companies/amazon), [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report), employing ~1,576,000 workers as of year-end 2025 [signals.ai](https://signals.ai/reports/amzn).
* **Revenue & Profitability:** Net sales reached $716.9B in FY2025 [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report). In Q2 FY2026, revenue totaled $200.6B with $27.5B in operating income, driven by AWS revenue surging 36.7% year-over-year to $42.23B [signals.ai](https://signals.ai/reports/amzn).
* **Capital Intensity:** Full-year 2026 cash capital expenditures are projected at approximately $220B, weighted heavily toward AI hardware and AWS infrastructure, creating near-term pressure on free cash flow [signals.ai](https://signals.ai/reports/amzn), [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report).

### 4. Leadership
* **Andrew (Andy) R. Jassy:** President and Chief Executive Officer [signals.ai](https://signals.ai/reports/amzn).
* **Jeff Bezos:** Founder and Executive Chair [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report).

### 5. Main Competitors & Differentiation
* **Cloud/AI (Microsoft Azure, Google Cloud):** AWS leads in market share (~30%) [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report) and differentiates via proprietary silicon (Trainium/Inferentia), Bedrock model optionality, and an $8B strategic partnership with Anthropic [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report).
* **Retail (Walmart, Shopify, Temu/Shein):** Walmart competes on physical store proximity and groceries [signals.ai](https://signals.ai/reports/amzn); Temu/Shein compete on low prices [signals.ai](https://signals.ai/reports/amzn). Amazon counters with Prime delivery speed, regionalized fulfillment density, and same-day perishable delivery in over 2,300 cities [signals.ai](https://signals.ai/reports/amzn).
* **Digital Advertising (Google, Meta):** Amazon differentiates with bottom-of-the-funnel, closed-loop consumer purchase data [deepresearchglobal.com](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report).

### 6. Likely Strategic Priorities & Open Questions
* **AI Capacity & Silicon Return:** Both AWS custom chips and AWS AI reached $25B annualized revenue run rates in Q2 2026 [signals.ai](https://signals.ai/reports/amzn). *Open question:* Can Amazon monetize capacity quickly enough to justify $220B in 2026 capex without margin compression from depreciation and energy costs [signals.ai](https://signals.ai/reports/amzn)?
* **Monetizing Strategic Bets:** Scaling paid Zoox commercial rides [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained) and activating enterprise/government contracts for Amazon Leo [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained). *Open question:* When will satellite broadband and autonomous mobility generate standalone operating profits [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)?
* **Regulatory Headwinds:** Persistent scrutiny from the FTC and international competition regulators concerning marketplace bundling and self-preferencing [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
4. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)
