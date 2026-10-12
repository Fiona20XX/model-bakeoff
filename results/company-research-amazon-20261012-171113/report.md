# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T17:11:13
- Variables: `company=Amazon`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2078 (contestants $0.1402, judge $0.0676)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 7.3 (7.3–7.3) | $0.0386 | 18.0s (15.9s–20.1s) | 5 (5–5) | 5 (5–5) | 1.9 |
| deepseek/deepseek-v4-pro | 7.2 (7.0–7.4) | $0.0101 | 48.9s (46.2s–51.7s) | 5 (5–5) | 6 (5–6) | 7.1 |
| google/gemini-3.8-flash | 6.9 (6.8–7.0) | $0.0214 | 28.0s (24.5s–31.4s) | 5 (5–5) | 5 (5–5) | 3.2 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: Its revenue breakdown and explicit caveats are useful, but many current operational and strategic details rely on information not present in the supplied excerpts.
- **deepseek/deepseek-v4-pro**: The supplied excerpts support its business overview, employee count, Leo update, and some cloud positioning, but leave many specific financial, leadership, and operational claims unverified.
- **google/gemini-3.8-flash**: The briefing is concrete and timely, but several of its most meeting-relevant figures and competitive claims cannot be verified from the supplied excerpts.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The $5.9B Other revenue figure is not visible in the supplied revenue-table excerpt.
- **anthropic/claude-sonnet-5.5** (run 1): The AWS and custom-chip/AI run rates, Amazon Now reach, and dated Zoox and Leo updates are not established by the cited excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The $220B capex forecast, earlier $200B estimate, hardware break-even period, and data-center lifespan are not in the cited excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The detailed competitor comparisons, delivery-growth figure, robotic-arm fleet plan, and chip, power, and regulatory exposures are not established by the cited excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The statement that Amazon has no funding rounds is not sourced.
- **deepseek/deepseek-v4-pro** (run 1): The claim that Amazon has millions of third-party sellers is not established by the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The airport expansion and several details of Zoox’s paid launch are not fully established by the supplied Zoox excerpt.
- **deepseek/deepseek-v4-pro** (run 1): The delivery-growth, Amazon Now, robotic-arm, AWS run-rate, AWS quarterly financial, and $220B capex figures are absent from the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 1): Being publicly listed and self-funding, the AWS hardware break-even estimate, and the data-center lifespan are not established by the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The supplied excerpts identify Jassy as CEO but do not establish Bezos’s and Garman’s listed roles or the 12-director board.
- **deepseek/deepseek-v4-pro** (run 1): Most detailed retail competitor comparisons and the claim that advertising is a high-margin revenue stream are not established by the cited excerpts.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not establish Zoox’s paid-ride launch, airport expansion, or regulatory exemption.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not give Amazon Leo’s satellite count, mission count, or rollout status.
- **google/gemini-3.8-flash** (run 1): The AWS Q2 2026 revenue, growth, operating income, and $25B chip and AI run-rate figures are absent from the cited excerpts.
- **google/gemini-3.8-flash** (run 1): The $220B capex forecast and its stated uses are absent from the cited excerpts.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not substantiate the competitor comparisons or the claim that cloud and advertising profits subsidize logistics automation.
- **anthropic/claude-sonnet-5.5** (run 2): The cited Investopedia excerpt does not support the claimed May 2026 launch of “Alexa for Shopping.”
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not establish the July 30 call date, Amazon Now footprint, satellite count, $220 billion capex guidance or its comparison with a $200 billion plan.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied Investopedia excerpt supports Q1 total sales and net income, but not the stated AWS sales, operating income or share of company operating income.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not establish the Q2 AWS and AI run rates, AWS’s roughly one-third global cloud share, or the robotic-arms forecast.
- **anthropic/claude-sonnet-5.5** (run 2): The claims about chip and power constraints and several competitor distinctions are not supported by the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish Amazon Now’s nine-country, 250-plus-city footprint or the 40% delivery-growth figure.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish the Q2 2026 AWS revenue, operating-income and run-rate figures, the two $25 billion AI-related run rates, or the $220 billion capex plan and its comparison with an earlier estimate.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish the satellite count, mission count or expected Amazon Leo rollout date.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not support the claims about free-cash-flow allocation, server and data-center economics, or the robotic-arms fleet doubling.
- **deepseek/deepseek-v4-pro** (run 2): The competitor descriptions and the claim that Amazon’s integrated offerings create a deep moat go beyond the cited excerpts.
- **google/gemini-3.8-flash** (run 2): The cited excerpt does not establish the Zoox regulatory exemption, paid Las Vegas launch or airport expansion.
- **google/gemini-3.8-flash** (run 2): The cited excerpt does not establish Amazon Leo’s satellite and mission counts or rollout timing.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not establish the $169 billion AWS run rate, the two $25 billion AI-related run rates, or the $220 billion FY2026 capex projection.
- **google/gemini-3.8-flash** (run 2): The description of advertising as high-margin is not supported by the cited excerpt.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not substantiate several competitor distinctions, unmatched delivery speeds, the Trainium/Inferentia comparison, or enterprise multi-cloud adoption.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0386

#### Run 1

# Amazon Briefing (as of 12 Oct 2026)

## 1. What they do, who buys it, and how they make money
Amazon sells to consumers, sellers, developers, enterprises, content creators and advertisers ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)). FY2025 net sales were $716.9B:
- Online stores: $269.3B (37.6%), recognized gross on owned inventory.
- Third-party seller services: $172.2B (24.0%), recognized as commissions and fulfillment fees.
- AWS: $128.7B (18.0%).
- Advertising: $68.6B (9.6%).
- Subscriptions (Prime and others): $49.6B (6.9%).
- Physical stores: $22.6B (3.1%).
- Other: $5.9B (0.8%).

All figures are from [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026). Because Amazon books only its fees on third-party sales, reported revenue understates the merchandise flowing through its stores ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)). One secondary source says AWS generates most of the operating profit, at roughly 37% margins ([pitchgrade.com](https://pitchgrade.com/companies/amazon)). I did not verify that against filings.

## 2. Recent news and launches
- **Q2 FY2026 results (30 Jul):** AWS reached a $169B annualized run rate. AWS chips and AI revenue each passed a $25B run rate ([signals.ai](https://signals.ai/reports/amzn)).
- **Delivery:** Amazon Now is in 9 countries and more than 250 cities and towns ([signals.ai](https://signals.ai/reports/amzn)).
- **Logistics:** Amazon launched Amazon Supply Chain Services for external business customers in Q2 2026. Its financial return isn't reported separately ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Zoox:** Paid Las Vegas rides began on 10 August and later extended to the airport ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).
- **Amazon Leo:** Nearly 400 satellites are in orbit. Initial service is planned for later in 2026, but mass-market service isn't yet established ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

## 3. Funding, size, and financial signals
Amazon is public, so there are no funding rounds. Management expects about $220B of cash capex in FY2026, up from an earlier estimate of about $200B, mostly for AI and AWS ([signals.ai](https://signals.ai/reports/amzn)). Servers and networking typically break even in slightly less than three years, and data centers are expected to run for more than 30 years ([signals.ai](https://signals.ai/reports/amzn)). I did not find net income, operating income or free cash flow figures in the sources, so I'm not citing any.

## 4. Leadership
- Andrew Jassy is president and CEO.
- Jeffrey Bezos is executive chair.
- Matthew Garman is CEO of AWS.
- The board has 12 directors.

All from the 2026 Form 10-K via [signals.ai](https://signals.ai/reports/amzn). I did not find other executives, such as the CFO, in the sources.

## 5. Main competitors and how they differ
- **Retail:** Walmart competes on store density, low prices and Walmart Fulfillment Services. Shopify lets merchants own the customer relationship. Alibaba, Temu and Shein compete on selection and price ([signals.ai](https://signals.ai/reports/amzn)).
- **Cloud and AI:** Microsoft Azure and Google Cloud are the main scaled rivals. Oracle and specialized providers compete for selected workloads ([signals.ai](https://signals.ai/reports/amzn)).
- **Convenience:** Delivery platforms challenge last-mile density ([signals.ai](https://signals.ai/reports/amzn)).
- **Amazon's edge:** It integrates Prime, marketplace, fulfillment, advertising and AWS ([signals.ai](https://signals.ai/reports/amzn)).

## 6. Likely strategic priorities and open questions
**Priorities** (stated by management):
- Faster delivery: same-day and overnight items grew more than 40% year over year in H1 FY2026.
- More robotics: the robotic arm fleet is set to more than double in FY2026.
- AI and custom chips.
- Free cash flow.

Sources: [signals.ai](https://signals.ai/reports/amzn).

**Open questions:**
- Will $220B of capex earn adequate returns? Management says returns depend on bringing capacity online ahead of demand ([signals.ai](https://signals.ai/reports/amzn)).
- Can chip and power supply keep up, and will regulators challenge Amazon's scale across markets? Both are flagged as exposures ([signals.ai](https://signals.ai/reports/amzn)).
- Can Leo, Zoox and Supply Chain Services become material? Their financial contribution isn't yet disclosed ([investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained)).

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

#### Run 2

# Amazon Briefing (as of Oct 12, 2026)

## 1. What they do, who buys it, how they make money
Amazon's mission is to make customers' lives better and easier through broad selection, value, and convenience, spanning online shopping and cloud computing ([aboutamazon.com](https://www.aboutamazon.com/about-us)). It reports three segments: North America, International (both retail), and AWS ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). Revenue comes from:
- **Retail:** first-party resale, plus commissions and fulfillment fees from third-party sellers.
- **Prime subscriptions.**
- **Advertising.**
- **AWS:** usage-based cloud billing ([signals.ai](https://signals.ai/reports/amzn)).

Buyers include consumers, sellers, advertisers, and businesses, government agencies, and academic institutions using AWS ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)).

## 2. Recent news and launches
- **April 2026:** Amazon invested $5B more in Anthropic ([wikipedia.org](https://en.wikipedia.org/wiki/Amazon_(company))).
- **May 2026:** It launched "Alexa for Shopping," combining Rufus and Alexa+ ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)).
- **Q2 FY2026 call (July 30):** Amazon Now was in 9 countries and 250+ cities, nearly 400 Amazon Leo satellites were in orbit, and capex guidance rose to about $220B ([signals.ai](https://signals.ai/reports/amzn)).

## 3. Funding, size, and financial signals
Amazon is public, so I found no funding rounds. It is an investor, notably in Anthropic.
- **Q1 2026:** Net sales were $181.5B (+16.6%) and net income was $30.3B ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)). AWS sales were $37.6B (+28%), and AWS operating income was $14.2B, about 59% of the company total ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)).
- **Q2 2026:** AWS hit a $169B annualized run rate. AWS chips and AI each exceeded a $25B run rate ([signals.ai](https://signals.ai/reports/amzn)).
- **Capex:** About $220B is planned for FY2026, mostly AI and AWS, up from about $200B ([signals.ai](https://signals.ai/reports/amzn)).
- **Not found:** Q2 total revenue and income figures were not in my sources.

## 4. Leadership
Andrew Jassy is president and CEO, Jeff Bezos is executive chair, and Matt Garman is AWS CEO. The board has 12 directors ([signals.ai](https://signals.ai/reports/amzn)). I did not find retail or advertising leadership in these sources.

## 5. Main competitors and how they differ
- **Retail:** Walmart competes on store density and everyday low prices. Shopify lets merchants own the customer relationship. Alibaba, Temu, and Shein compete on selection and low prices ([signals.ai](https://signals.ai/reports/amzn)).
- **Cloud:** Microsoft Azure and Google Cloud are the main scaled rivals. Oracle and specialized providers compete for select workloads ([signals.ai](https://signals.ai/reports/amzn)). AWS holds roughly a third of the global cloud market ([investopedia.com](https://www.investopedia.com/how-amazon-makes-money-4587523)).
- **Amazon's differentiator:** Prime, marketplace, fulfillment, advertising, and AWS are integrated ([signals.ai](https://signals.ai/reports/amzn)).

## 6. Likely strategic priorities and open questions
**Priorities:**
- Scaling AI and cloud capacity, including custom chips.
- Faster, cheaper retail fulfillment, with robotic arms expected to more than double in FY2026.
- Embedding generative AI in shopping.
- Longer-term bets such as satellites and quick commerce ([signals.ai](https://signals.ai/reports/amzn)).

**Open questions:**
- **Returns on capex:** Cash returns depend on bringing capacity online ahead of demand ([signals.ai](https://signals.ai/reports/amzn)). Management says servers break even in just under three years, while data centers last 30+ years.
- **Constraints:** Chip and power supply could limit capacity.
- **Multi-cloud:** Customers may spread workloads across providers.
- **Regulation:** Regulators may challenge Amazon's scale across adjacent markets ([signals.ai](https://signals.ai/reports/amzn)).
- **AI partner concentration:** Amazon has deep ties to Anthropic, and OpenAI agreed in November 2025 to pay AWS $38B ([britannica.com](https://www.britannica.com/money/Amazoncom)). It is unclear how these relationships balance.

**Sources**

1. [About Amazon: Mission, businesses, and innovation](https://www.aboutamazon.com/about-us)
2. [Amazon (company)](https://en.wikipedia.org/wiki/Amazon_(company))
3. [How Amazon Makes Money](https://www.investopedia.com/how-amazon-makes-money-4587523)
4. [Amazon \| E-commerce, Amazon Web Services, History, & ...](https://www.britannica.com/money/Amazoncom)
5. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)

### deepseek/deepseek-v4-pro

Cost: $0.0101

#### Run 1

# Amazon Briefing (October 2026)

## 1. What they do, who buys it, and how they make money
Amazon operates a massive, multi‑faceted platform spanning e‑commerce, cloud computing, advertising, subscriptions and logistics. It sells products directly (gross sales) and enables millions of third‑party sellers to list goods, earning commissions and fees from services like Fulfillment by Amazon [signals.ai](https://signals.ai/reports/amzn), [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained). Consumers, enterprises, developers, content creators and advertisers buy through online and physical stores, Alexa devices, streaming services and AWS [signals.ai](https://signals.ai/reports/amzn).  

Retail (~50% of revenue) has thin margins, while AWS (~17% of revenue) delivers the majority of operating profit with margins around 37% [pitchgrade.com](https://pitchgrade.com/companies/amazon). Prime subscriptions, advertising (sponsored, display, video) and AWS consumption‑based services layer additional high‑margin revenue streams [signals.ai](https://signals.ai/reports/amzn).

## 2. Recent news and launches (last 6 months)
- **Zoox robotaxi service:** In July 2026, Amazon obtained a U.S. regulatory exemption to charge for rides. Paid operations launched in Las Vegas on 10 August, and by September the service had expanded to the Las Vegas airport [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
- **Amazon Leo satellite broadband:** As of September 2026, nearly 400 satellites were in orbit, with initial service rollout expected later in the year [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).  
- **Operational acceleration:** In Q2 FY2026 (July call), the company reported >40% YoY growth in same‑day/overnight deliveries, Amazon Now quick commerce available in 9 countries and >250 cities, and a plan to more than double its robotic arm fleet. AWS annualized revenue reached $169 bn and the AI annual revenue run rate topped $25 bn [signals.ai](https://signals.ai/reports/amzn).

## 3. Funding, size, and financial signals
Amazon is self‑funding and publicly listed. It employed ~1.576 million people at end‑2025 [signals.ai](https://signals.ai/reports/amzn). The company has guided a massive ~$220 bn in cash capex for FY2026, predominantly for AI/cloud infrastructure [signals.ai](https://signals.ai/reports/amzn). AWS remains the financial engine: Q2 FY2026 revenue of $42.23 bn (+36.7% YoY) generated $16.62 bn in operating income [signals.ai](https://signals.ai/reports/amzn). The retail business remains capital‑intensive but is becoming more efficient; management expects AWS hardware to break‑even in under three years and data centers to operate for 30+ years [signals.ai](https://signals.ai/reports/amzn).

## 4. Leadership
- **President & CEO:** Andrew R. Jassy  
- **Executive Chair:** Jeffrey P. Bezos  
- **CEO, Amazon Web Services:** Matthew S. Garman  
- **Board:** 12 directors, including Bezos as executive chair [signals.ai](https://signals.ai/reports/amzn).

## 5. Main competitors and how they differ
Competition plays out by segment, not as a single rival [signals.ai](https://signals.ai/reports/amzn).  
- **Retail:** Walmart (store density, everyday‑low‑price, Walmart Fulfillment Services), Shopify (merchant‑owned storefronts), and cross‑border platforms like Temu and Shein [signals.ai](https://signals.ai/reports/amzn).  
- **Cloud:** Microsoft Azure and Google Cloud are the primary scaled rivals; Azure is cited as the “principal public competitor” for cloud workloads [dyorhq.ai](https://dyorhq.ai/reports/amazoncominc)[signals.ai](https://signals.ai/reports/amzn).  
- **Convenience/last‑mile:** Delivery platforms challenge Amazon’s speed ambitions [signals.ai](https://signals.ai/reports/amzn).  
Amazon’s integration of Prime, marketplace, fulfillment, advertising and AWS creates a unique bundle; competitors can underprice individual services, but the breadth is hard to replicate [signals.ai](https://signals.ai/reports/amzn).

## 6. Likely strategic priorities and open questions
The strategic arc centers on making retail more efficient (regional inventory, automation, faster delivery), feeding cloud and AI growth (custom chips, generative‑AI services, new data centres), and layering advertising across the platform [signals.ai](https://signals.ai/reports/amzn).  

**Open questions:**  
- Can the historic $220 bn capex build generate adequate returns, especially if AI demand moderates?  
- Will Amazon Leo satellite broadband move from initial rollout to a profitable mass‑market service?  
- Can Zoox scale paid autonomous rides beyond Las Vegas?  
- How will regulators respond to Amazon’s combined scale in retail, logistics, cloud and advertising?

**Sources**

1. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
2. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
3. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [DYOR HQ - Amazon.com Inc (AMZN) \| 2026-10-04](https://dyorhq.ai/reports/amazoncominc)

#### Run 2

**Briefing: Amazon.com, Inc. (AMZN)**  
Prepared October 2026 — based on public disclosures and announcements through early Q4 2026.

### 1. What they do, who buys it, and how they make money
Amazon serves consumers, sellers, enterprises, developers, content creators, advertisers, and employees. Revenue recognition differs by business line — online stores and physical stores record gross merchandise sales, while third‑party seller services record only the net fees Amazon earns (commissions, fulfilment, shipping). In FY2025 (ended December 2025), consolidated net sales were $716.9 bn, led by online stores (37.6%), third‑party seller services (24.0%), AWS (18.0%), advertising (9.6%), subscriptions (6.9%), and physical stores (3.1%). [sec-api.io] This structure means reported revenue understates the total value of goods moving through Amazon because third‑party sales are recorded net. [signals.ai] AWS, the largest public cloud, sells compute, storage, AI, and databases on a consumption or contract basis. Advertising monetizes shopping intent; Prime bundles shipping, video, music, and more for a recurring fee.

### 2. Recent news and launches (last six months)
**Delivery & convenience**: Amazon Now, the ultrafast delivery service, was live in nine countries and more than 250 cities/towns by the end of Q2 FY2026. Items delivered same day or overnight grew more than 40% year‑over‑year in the first half of FY2026. [signals.ai]  
**AWS & AI**: AWS reached a $169 bn annualised revenue run rate in Q2, with AI and custom‑chip revenue each above a $25 bn annual run rate. Management announced plans for approximately $220 bn in cash capital expenditures in FY2026 (up from a prior estimate of $100 bn?), mainly for AI and cloud data centres. [signals.ai]  
**Satellite broadband (Amazon Leo)**: Nearly 400 satellites were in orbit by September 2026, with 14 completed missions and initial service rollout expected later in 2026, though mass‑market service had not yet been confirmed. [investomine.substack.com]  
**Supply chain as a service**: Amazon Supply Chain Services was launched for external business customers, using its fulfilment network beyond Amazon’s own marketplace. [investomine.substack.com]

###3. Funding, size, and financial signals
Amazon is a public company with approximately 10.73 bn shares outstanding and a stock price of $218.94 as of early 2026. [pitchgrade.com] The business is generating substantial cash but is in a heavy investment cycle. Q2 FY2026 AWS operating income was $16.62 bn on revenue of $42.23 bn (36.7% YoY growth). [signals.ai] Management expects cash capex of ~$220 bn in FY2026, driven by AI and cloud infrastructure — a step‑up from earlier plans, with the expectation that servers break even in slightly under three years and data centres operate for more than30 years. [signals.ai] Free cash flow is being directed toward this long‑cycle expansion while operating income growth supports the investment.

###4. Leadership
- **Andrew R. Jassy** – President and Chief Executive Officer  
- **Jeffrey P. Bezos** – Executive Chair of the Board  
- **Matthew S. Garman** – Chief Executive Officer, Amazon Web Services  
The board consists of12 directors, with Bezos and Jassy serving in their respective roles. [signals.ai]

###5. Main competitors and how they differ
- **Retail**: Walmart (store density, everyday‑low‑price, marketplace and fulfilment services); Shopify (direct‑to‑consumer storefronts); cross‑border platforms Alibaba, Temu, Shein (low‑cost selection).  
- **Cloud**: Microsoft Azure and Google Cloud are the primary scaled rivals; Oracle competes for certain workloads.  
- **Digital offering**: Amazon’s integration of Prime, marketplace, fulfilment, advertising, and AWS creates a deep moat, but competitors can attack individual service lines, and enterprise customers often use multiple clouds. [signals.ai]

###6. Likely strategic priorities and open questions
**Priorities**: (a) Scale AWS and AI infrastructure while maintaining unit‑cost discipline and capacity ahead of demand. (b) broaden Amazon Now’s ultrafast delivery footprint. (c) Monetise Amazon Leo and new supply‑chain services. (d) Continue robotics‑led operational efficiencies (robotic arms fleet more than doubled in FY2026). [signals.ai]  

**Open questions**: Will the $220 bn capex cycle generate adequate returns if AI demand shifts? Can Amazon price Leo competitively against Starlink? How will regulators view the company’s combination of scale across retail, cloud, and advertising? Are competitors like Temu and Walmart eroding marketplace seller economics?

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

### google/gemini-3.8-flash

Cost: $0.0214

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
Amazon operates a global ecosystem spanning retail, cloud infrastructure, advertising, and digital services [signals.ai](https://signals.ai/reports/amzn). Its monetization models include:
* **Consumers:** Direct retail sales (recognized gross), digital media, and Prime subscriptions recognized over time [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026).
* **Third-Party Sellers:** Commissions, storage, picking, packing, and shipping fees (e.g., Fulfillment by Amazon), recognized net as service revenue [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Enterprises & Developers:** Amazon Web Services (AWS) bills for compute, storage, databases, and AI models via consumption and fixed-term contracts [signals.ai](https://signals.ai/reports/amzn).
* **Advertisers:** Pay-per-click and impression-based sponsored ads, display, and video placements across retail and streaming platforms [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026).

### 2. Recent News and Launches
* **Autonomous Rides Commercialized:** Zoox received a U.S. regulatory exemption and launched paid robotaxi rides in Las Vegas in August 2026, expanding commercial trips to the airport in September [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Amazon Leo (Project Kuiper):** Surpassed 400 low-Earth-orbit satellites across 14 missions, preparing for an initial commercial broadband rollout [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **External Logistics Expansion:** Rolled out Amazon Supply Chain Services to fulfill orders for business clients off Amazon’s marketplace [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **AI & Silicon Run Rates:** AWS disclosed that its proprietary custom chip revenue and overall AI revenue run rates each exceeded $25B annualized in Q2 2026 [signals.ai](https://signals.ai/reports/amzn).

### 3. Funding, Size, and Financial Signals
* **Revenue Scale:** Total net sales reached $716.9B in FY2025 [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026). 
* **Cloud Outperformance:** In Q2 2026, AWS grew 36.7% year-over-year to $42.23B in quarterly revenue ($169B run rate), delivering $16.62B in operating income [signals.ai](https://signals.ai/reports/amzn).
* **Massive CapEx Commitments:** Raised expected FY2026 cash capital expenditures to ~$220B (up from $200B), primarily directed toward AI, custom chips, and data center capacity [signals.ai](https://signals.ai/reports/amzn).

### 4. Leadership
* **Jeffrey P. Bezos:** Founder & Executive Chair [signals.ai](https://signals.ai/reports/amzn).
* **Andrew R. Jassy:** President & Chief Executive Officer [signals.ai](https://signals.ai/reports/amzn).
* **Matthew S. Garman:** Chief Executive Officer, Amazon Web Services [signals.ai](https://signals.ai/reports/amzn).

### 5. Main Competitors and How They Differ
* **Retail & Marketplace:** Walmart (competes via physical store density and grocery strength), Shopify (empowers independent merchant-owned stores), and Temu/Shein (ultra-low-cost, direct-from-manufacturer supply chains) [signals.ai](https://signals.ai/reports/amzn).
* **Cloud & AI:** Microsoft Azure and Google Cloud [signals.ai](https://signals.ai/reports/amzn).
* **Differentiator:** Amazon's integrated flywheel: high-margin cloud and advertising profits subsidize massive logistics automation, driving delivery speeds that competitors struggle to match profitably [signals.ai](https://signals.ai/reports/amzn).

### 6. Likely Strategic Priorities and Open Questions
* **Priorities:** Bringing massive generative AI computing capacity online ahead of demand; scaling custom silicon to reduce reliance on third-party GPUs; and automating fulfillment centers with robotics to reduce cost per unit [signals.ai](https://signals.ai/reports/amzn).
* **Open Questions:**
  * How quickly will the ~$220B CapEx cycle translate into sustained free cash flow amidst rising power and facility constraints?
  * What is the timeline for Amazon Leo and Zoox to deliver material, standalone operating profitability?
  * How will consumer retail margins hold up against aggressive discount cross-border apps?

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)

#### Run 2

### 1. What They Do, Who Buys It, & How They Make Money
Amazon operates a global commerce, cloud, and digital services ecosystem serving consumers, third-party sellers, enterprises, developers, and advertisers [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026). It monetizes via:
* **Retail & Marketplace:** Direct first-party product sales (gross revenue) and commissions, fulfillment (FBA), and shipping fees charged to third-party merchants [signals.ai](https://signals.ai/reports/amzn).
* **AWS:** Consumption- and subscription-based enterprise cloud infrastructure, compute, storage, databases, and AI services [signals.ai](https://signals.ai/reports/amzn).
* **Advertising & Subscriptions:** High-margin sponsored ads, video/display impressions, and Prime membership subscriptions [signals.ai](https://signals.ai/reports/amzn).

### 2. Recent News & Launches
* **Zoox Commercial Launch:** Following a July 2026 U.S. regulatory exemption, autonomous vehicle unit Zoox launched paid robotaxi rides in Las Vegas in August 2026, expanding routes to the Las Vegas airport by September [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Amazon Leo (Project Kuiper):** Surpassed nearly 400 satellites in orbit across 14 missions by September 2026 ahead of an initial commercial satellite broadband rollout [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).
* **Amazon Supply Chain Services:** Expanded logistics offerings in Q2 2026 to service external business customers outside Amazon's own marketplace [investomine.substack.com](https://investomine.substack.com/p/business-breakdown-amazon-explained).

### 3. Funding, Size, & Financial Signals
* **Revenue Base:** Generated $716.9B in net sales in FY2025, led by Online Stores ($269.3B), 3P Seller Services ($172.2B), and AWS ($128.7B) [sec-api.io](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026).
* **AWS & AI Scale:** AWS reached a $169B annualized revenue run rate in Q2 2026 [signals.ai](https://signals.ai/reports/amzn). Both AWS custom chips and dedicated AI services reached individual annual run rates exceeding $25B [signals.ai](https://signals.ai/reports/amzn).
* **CapEx Acceleration:** Management raised projected FY2026 cash capital expenditures to approximately $220B, driven heavily by cloud and AI data center infrastructure [signals.ai](https://signals.ai/reports/amzn).

### 4. Leadership
* **Andy Jassy:** President and Chief Executive Officer [signals.ai](https://signals.ai/reports/amzn).
* **Jeff Bezos:** Founder and Executive Chair of the 12-member Board of Directors [signals.ai](https://signals.ai/reports/amzn).
* **Matt Garman:** Chief Executive Officer of Amazon Web Services (AWS) [signals.ai](https://signals.ai/reports/amzn).

### 5. Main Competitors & How They Differ
* **Retail & Marketplace:** Walmart (competes via store density and everyday low prices), Shopify (enables direct-to-consumer independence), and low-price cross-border platforms like Temu and Shein [signals.ai](https://signals.ai/reports/amzn). Amazon differentiates through unmatched delivery speeds and integrated Prime ecosystem benefits [signals.ai](https://signals.ai/reports/amzn).
* **Cloud & AI:** Microsoft Azure and Google Cloud [signals.ai](https://signals.ai/reports/amzn). Amazon differentiates with proprietary silicon (Trainium/Inferentia) and extensive enterprise infrastructure breadth, though enterprise multi-cloud adoption remains a challenge [signals.ai](https://signals.ai/reports/amzn).

### 6. Likely Strategic Priorities & Open Questions
* **Strategic Priorities:** Accelerating AI hardware/model infrastructure deployments; commercializing Amazon Leo satellite connectivity; and continuing warehouse robotics automation to lower per-unit fulfillment costs [signals.ai](https://signals.ai/reports/amzn).
* **Open Questions:** How quickly will the massive ~$220B FY2026 CapEx deliver accretive free cash flow returns [signals.ai](https://signals.ai/reports/amzn)? How will retail margins hold up against intense discounting from cross-border e-commerce platforms [signals.ai](https://signals.ai/reports/amzn)?

**Sources**

1. [Amazon.com, Inc. (AMZN) Deep Dive Research Report \| Signals.AI](https://signals.ai/reports/amzn)
2. [Business Breakdown: Amazon Explained: Stores, Sellers, AWS, Media and New Bets](https://investomine.substack.com/p/business-breakdown-amazon-explained)
3. [Financial analysis of Amazon, FY2025 and the first half of 2026](https://sec-api.io/insights/financial-analysis-of-amazon-fy2025-and-the-first-half-of-2026)
4. [Amazon (AMZN) - Fundamental Analysis Report 2026 (Updated)](https://www.deepresearchglobal.com/p/amazon-amzn-fundamental-analysis-report)
5. [Amazon: Business Model, SWOT Analysis, and Competitors 2026 - PitchGrade](https://pitchgrade.com/companies/amazon)
