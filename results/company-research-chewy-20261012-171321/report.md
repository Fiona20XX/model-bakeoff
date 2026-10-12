# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T17:13:21
- Variables: `company=Chewy`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2030 (contestants $0.1376, judge $0.0654)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 7.1 (7.1–7.1) | $0.0390 | 19.2s (18.6s–19.9s) | 5 (5–5) | 6 (5–6) | 1.8 |
| google/gemini-3.8-flash | 6.3 (6.0–6.7) | $0.0179 | 22.9s (20.8s–25.0s) | 5 (5–5) | 7 (7–7) | 3.5 |
| deepseek/deepseek-v4-pro | 5.7 (4.7–6.8) | $0.0119 | 59.8s (20.4s–99.2s) | 5 (5–5) | 6 (5–7) | 4.8 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: The dated briefing has useful supported Autoship, customer, and balance-sheet signals, but several detailed claims lack excerpt support and it does not identify leaders or named competitors.
- **google/gemini-3.8-flash**: It offers concrete meeting questions and supported scale figures, but many acquisition, financing, leadership, and competitive details are not backed by the supplied excerpts.
- **deepseek/deepseek-v4-pro**: Recent customer and Autoship figures are supported, but several prominent claims lack excerpt support and the briefing cuts off before completing competitors or strategic priorities.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The supplied SEC excerpt does not substantiate the largest-U.S.-pet-e-tailer claim or the 190,000-product and 4,000-brand figures.
- **anthropic/claude-sonnet-5.5** (run 1): The supplied SEC excerpt does not substantiate the Modern Animal agreement and closing dates, or the SmartPak acquisition, goodwill, and transaction-cost figures.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not show that management raised guidance on September 9, 2026.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not show the $47.9 million capex, $89.5 million free cash flow, $24.0 million legal-settlement gain, or first-half repurchases and debt issuance.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpt gives $602 in net sales per active customer but does not explicitly establish the answer’s annual spending period or its 1.9% growth figure.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpt does not establish that growth excluding the acquisitions was weaker than reported growth.
- **google/gemini-3.8-flash** (run 1): The excerpts do not establish a customer base of farm and exotic-animal owners or the listed pet-insurance and telehealth services.
- **google/gemini-3.8-flash** (run 1): The excerpts do not substantiate the Modern Animal closing date or $378.0 million price, or SmartPak’s $174.8 million price.
- **google/gemini-3.8-flash** (run 1): SmartPak’s February 2, 2026 closing date in the cited excerpt does not place it within the stated last-six-month window.
- **google/gemini-3.8-flash** (run 1): The $600 million June 2026 loan, its seven-year term, and the $611.0 million cash balance are not shown in the excerpts.
- **google/gemini-3.8-flash** (run 1): The excerpt does not substantiate triple-digit veterinary-clinic revenue growth.
- **google/gemini-3.8-flash** (run 1): The excerpts do not substantiate Sumit Singh’s tenure, David Reeder’s role, or the claims about Amazon, Petco, and PetSmart and how they differ from Chewy.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not establish expansion into fresh or frozen food, superior digital UI, lower overhead, or automated fulfillment centers.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish that Chewy is the largest U.S. pet e-tailer or offers 190,000 products from 4,000 brands.
- **deepseek/deepseek-v4-pro** (run 1): The cited SEC excerpt does not substantiate either acquisition or its timing.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not substantiate the named leadership team or Ryan Cohen’s current involvement.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish that Chewy is navigating inflationary pressures and economic uncertainty.
- **deepseek/deepseek-v4-pro** (run 1): The claim that Autoship’s sales share demonstrates customer loyalty goes beyond the cited figures.
- **anthropic/claude-sonnet-5.5** (run 2): Chewy is the largest U.S. pet e-tailer and offers about 190,000 products from roughly 4,000 brands plus private brands.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate the Modern Animal transaction, its dates, or the SmartPak acquisition and associated costs.
- **anthropic/claude-sonnet-5.5** (run 2): The self-service chat excerpt does not establish that the feature uses AI.
- **anthropic/claude-sonnet-5.5** (run 2): The excerpts do not substantiate the September guidance increase, $47.9 million quarterly capex, $89.5 million free cash flow, or $24.0 million legal-settlement gain.
- **anthropic/claude-sonnet-5.5** (run 2): The excerpts do not establish that growth including acquisitions exceeded growth excluding them.
- **google/gemini-3.8-flash** (run 2): Chewy is the largest pure-play U.S. pet e-tailer and offers approximately 190,000 products from 4,000 brands plus private labels.
- **google/gemini-3.8-flash** (run 2): The excerpts do not substantiate the Modern Animal acquisition or SmartPak integration and its $7.4 million expense.
- **google/gemini-3.8-flash** (run 2): The excerpts do not establish that the app chat feature was rolled out in mid-2026 or resolves inquiries autonomously.
- **google/gemini-3.8-flash** (run 2): The September guidance increase and the 1.9% year-over-year increase in sales per active customer are not shown.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not show $588.7 million in debt, $89.5 million in quarterly free cash flow, or $47.9 million in capex.
- **google/gemini-3.8-flash** (run 2): Neither leadership name, title, nor Singh's tenure is supported by a cited excerpt.
- **google/gemini-3.8-flash** (run 2): The named Amazon, Petco, and PetSmart comparisons—including relative catalog depth, service capabilities, and Autoship retention—are not supported by the excerpts.
- **deepseek/deepseek-v4-pro** (run 2): Chewy is the largest U.S. pet e-tailer and offers approximately 190,000 products from 4,000 brands plus private brands.
- **deepseek/deepseek-v4-pro** (run 2): The excerpts do not substantiate the Modern Animal or SmartPak acquisitions or their described businesses.
- **deepseek/deepseek-v4-pro** (run 2): The chat excerpt supports self-service resolution, but not that the feature is AI-powered or newly launched.
- **deepseek/deepseek-v4-pro** (run 2): The claim that expansion is pressuring liquidity is not established by the cited balance-sheet figures.
- **deepseek/deepseek-v4-pro** (run 2): The $89.5 million free-cash-flow and $47.9 million capex figures, and the assertion that capex reduced free cash flow, are not supported by the excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The September guidance increase is not shown in the excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The assertion that Chewy's model goes beyond that of many competitors lacks a supported competitor comparison.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0390

#### Run 1

# Chewy Briefing (as of Oct 12, 2026)

## 1. What they do, who buys it, how they make money
Chewy calls itself the largest U.S. pet e-tailer. It has about 190,000 products from roughly 4,000 brands, plus its own private brands ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)). Buyers are pet parents: 21.7M active customers (+3.8% YoY), each spending $602 a year ([exa.ai](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)). Revenue comes mainly from product sales, increasingly through Autoship subscriptions. Autoship sales grew 9.3% to $2,817.2M, or 84.6% of net sales ([tenq.co](https://tenq.co/report/CHWY/story)). That implies quarterly net sales of about $3.3B (my calculation). I did not find a margin breakdown or a separate healthcare revenue line.

## 2. Recent news (last 6 months)
- **Modern Animal:** The agreement was signed April 1, 2026 and the deal closed May 21. Modern Animal is a technology-forward veterinary platform, framed as a step toward an "integrated pet healthcare ecosystem" ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).
- **SmartPak:** Chewy also acquired SmartPak, recording $73.1M of goodwill and $7.4M of transaction costs in the first half ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)). I couldn't confirm the closing date.
- **AI support:** About 30% of mobile-app chats are now resolved through self-service ([fool.com](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)).
- **Guidance:** Management raised revenue and profitability expectations on September 9, 2026 ([tenq.co](https://tenq.co/report/CHWY/story)).

## 3. Funding, size, financial signals
- **Ownership:** Chewy IPO'd June 18, 2019 ([tenq.co](https://tenq.co/report/CHWY/story)). It is a "controlled company," with BC Partners, CDPQ, GIC affiliates, StepStone and Longview holding majority voting power ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).
- **Balance sheet (Aug 2, 2026):** Current assets were $1,845.3M against current liabilities of $2,202.4M. Long-term debt was $588.7M ([tenq.co](https://tenq.co/report/CHWY/story)).
- **Cash flow:** Capex of $47.9M reduced quarterly free cash flow to $89.5M.
- **Earnings quality:** Results included a $24.0M legal settlement gain. Acquisitions, repurchases and debt issuance all occurred in the first half ([tenq.co](https://tenq.co/report/CHWY/story)).
- I did not find total revenue, net income or headcount in the sources.

## 4. Leadership
I couldn't find leadership information in the sources reviewed. Check the latest proxy or investor relations page before the meeting.

## 5. Competitors
The sources name categories rather than companies: online retailers, physical stores, suppliers' own websites, and veterinary providers. Chewy competes on price, availability, delivery and service ([tenq.co](https://tenq.co/report/CHWY/story)). Its Autoship base and veterinary push are its differentiators. I found no named-competitor comparison.

## 6. Strategic priorities and open questions
**Likely priorities**
- Build a care-plus-commerce healthcare ecosystem.
- Deepen Autoship.
- Scale AI-driven service.
- Integrate acquisitions.

**Open questions**
- **Organic growth:** Reported growth including SmartPak and Modern Animal was stronger than growth excluding them. How much momentum is organic? ([tenq.co](https://tenq.co/report/CHWY/story))
- **Customers:** Active customers grew 3.8% and spend per customer 1.9%. Can customer growth keep pace with Autoship depth?
- **Liquidity:** Current liabilities exceed current assets. How will acquisitions, buybacks and capex be funded?
- **Healthcare:** Services differ from shipping pet supplies. What does the execution plan and economics look like?

**Sources**

1. [Chewy, Inc. Form 10-Q for the period ended August 2, 2026](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
2. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
3. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
4. [CHWY Earnings Call Transcript — Fiscal Q1 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q1/transcript)
5. [Chewy (CHWY) stock story: what drives it, what the price assumes and the risks \| TenQ](https://tenq.co/report/CHWY/story)

#### Run 2

# Chewy Briefing

## 1. What they do, who buys it, how they make money
Chewy is primarily an e-commerce business for pet products and services, sold through its websites and mobile apps. It emphasizes Autoship subscriptions, fast shipping and easy returns ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)). It calls itself the largest US pet e-tailer, with about 190,000 products from roughly 4,000 brands plus its own private brands ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).

Buyers are pet parents: 21.7M active customers (+3.8% YoY), each spending $602 net sales per year. Autoship sales grew 9.3% and were 84.6% of net sales ([exa.ai](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)). Revenue comes mainly from product sales, with healthcare services a growing addition. I found no revenue-mix breakdown beyond this.

## 2. Recent news and launches
- **Modern Animal:** The deal was signed April 1, 2026 and closed May 21, 2026. Modern Animal is a tech-forward veterinary platform, framed as a step toward an integrated pet healthcare ecosystem ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).
- **SmartPak:** Chewy acquired it, recording $73.1M of goodwill and $7.4M of transaction costs in the 26 weeks ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).
- **AI support:** About 30% of chats in the mobile app are resolved through self-service ([fool.com](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)).
- **Guidance:** Management raised revenue and profitability expectations on September 9, 2026 ([tenq.co](https://tenq.co/report/CHWY/story)).

## 3. Funding, size, financial signals
- Chewy IPO'd June 18, 2019 ([tenq.co](https://tenq.co/report/CHWY/story)). It is a "controlled company": BC Partners, CDPQ, GIC affiliates, StepStone and Longview-advised funds hold majority voting power ([sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)).
- Autoship sales of $2,817.2M at 84.6% of net sales imply roughly $3.3B quarterly net sales (my calculation).
- At Aug 2, 2026, current assets were $1,845.3M against current liabilities of $2,202.4M, and net long-term debt was $588.7M. Quarterly capex was $47.9M and free cash flow $89.5M. Earnings included a $24.0M legal settlement gain ([tenq.co](https://tenq.co/report/CHWY/story)).
- The first half included acquisitions, repurchases and debt issuance ([tenq.co](https://tenq.co/report/CHWY/story)).

## 4. Leadership
Not found in the sources I retrieved. Verify the current CEO, CFO and healthcare leads before the meeting.

## 5. Competitors
The sources name no specific rivals. They list the categories: online retailers, physical stores, suppliers' own websites and veterinary providers ([tenq.co](https://tenq.co/report/CHWY/story)). Chewy says it competes on price, availability, delivery and service, and Autoship plus the vet push are its main differentiators. Named-competitor comparisons would need further research.

## 6. Likely priorities and open questions
**Priorities**
- Integrate SmartPak and Modern Animal.
- Deepen Autoship use.
- Grow active customers.
- Use AI to improve service.

**Open questions**
- How much growth is organic? Growth including the acquisitions was stronger than growth excluding them ([tenq.co](https://tenq.co/report/CHWY/story)).
- How will Chewy fund further acquisitions and buybacks given the working-capital position? ([tenq.co](https://tenq.co/report/CHWY/story))
- Can thin operating margins absorb shipping, supplier or customer-acquisition cost shocks? ([tenq.co](https://tenq.co/report/CHWY/story))
- How will the vet and services business scale beyond shipping pet supplies?

**Sources**

1. [Chewy, Inc. Form 10-Q for the period ended August 2, 2026](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
2. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
3. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
4. [CHWY Earnings Call Transcript — Fiscal Q1 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q1/transcript)
5. [Chewy (CHWY) stock story: what drives it, what the price assumes and the risks \| TenQ](https://tenq.co/report/CHWY/story)

### google/gemini-3.8-flash

Cost: $0.0179

#### Run 1

### 1. What They Do, Who Buys, & Revenue Model
Chewy is the largest pure-play pet e-tailer in the U.S., offering ~190,000 products from 4,000 partner brands alongside private labels according to its [Form 10-Q](https://www.stocktitan.net/sec-filings/CHWY/10-q-chewy-inc-quarterly-earnings-report-cc169525ddef.html). Its customers are retail pet parents and specialty animal owners (equine, farm, exotics). 

Chewy generates revenue primarily by selling pet consumables (food, treats), hard goods (crates, toys), and healthcare items (Rx pharmacy, supplements). Its business model heavily relies on recurring revenue via its "Autoship" subscription delivery program, complemented by emerging services such as pet insurance, telehealth, and physical veterinary care according to [Stock Titan](https://www.stocktitan.net/sec-filings/CHWY/10-q-chewy-inc-quarterly-earnings-report-cc169525ddef.html).

### 2. Recent News & Launches (Last 6 Months)
* **Modern Animal Acquisition:** Completed on May 21, 2026, for $378.0 million in cash, bringing the tech-forward clinic platform into Chewy’s healthcare ecosystem, as reported in its [Form 10-Q filing](https://www.publicnow.com/view/A3C3235618841B1AAA702BBC7CABB83B97784FE3).
* **SmartPak Integration:** Finalized its $174.8 million acquisition of SmartPak Equine to strengthen horse health and nutrition offerings, per [Public Now](https://www.publicnow.com/view/A3C3235618841B1AAA702BBC7CABB83B97784FE3).
* **$600M Debt Financing:** Secured a 7-year senior secured term loan facility in June 2026 maturing in 2033 to bolster liquidity, per [Stock Titan](https://www.stocktitan.net/sec-filings/CHWY/10-q-chewy-inc-quarterly-earnings-report-cc169525ddef.html).
* **Chewy Vet Care Expansion:** Scaled physical veterinary clinics, delivering triple-digit revenue growth in clinic operations according to its [Q2 2026 earnings transcript](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript).

### 3. Funding, Size, & Financial Signals
* **Financials & Scale:** Annual net sales stand at ~$12.6 billion, with 13,668 employees reported in an [earnings transcript](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript). Chewy held $611.0 million in cash and cash equivalents as of August 2026, noted in its [Form 10-Q](https://www.publicnow.com/view/A3C3235618841B1AAA702BBC7CABB83B97784FE3).
* **Ownership:** Publicly traded (NYSE: CHWY; IPO in 2019), but remains a "controlled company" dominated by sponsor voting power including BC Partners, per [Stock Titan](https://www.stocktitan.net/sec-filings/CHWY/10-q-chewy-inc-quarterly-earnings-report-cc169525ddef.html).

### 4. Leadership
* **CEO:** Sumit Singh has served as CEO since 2018, leading Chewy through its IPO and shift into healthcare.
* **CFO:** David Reeder manages financial operations and capital allocation.

### 5. Main Competitors & Differentiation
* **Amazon:** Broader general selection and faster one-day logistics, but lacks specialized pet pharmacy capabilities, high-touch customer service (e.g., hand-written cards), and veterinary care integrations.
* **Petco & PetSmart:** Strong brick-and-mortar store footprints offering grooming and in-store adoption; Chewy counters with superior pure-play digital UI, higher Autoship penetration, automated fulfillment centers, and lower overhead.

### 6. Strategic Priorities & Open Questions
* **Veterinary & Healthcare Integration:** Scaling Chewy Vet Care and integrating Modern Animal to create a full-lifecycle healthcare ecosystem. *Question:* Can Chewy operate physical clinics at high margins without diluting overall return on capital?
* **Category Expansion:** Building out specialty equine/farm segments (via SmartPak) and fresh/frozen pet food according to [its earnings transcript](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript). *Question:* Will higher fulfillment costs for cold-chain fresh food compress gross margins?
* **AI & Self-Service Efficiency:** Rolling out conversational self-service tools, which already resolve ~30% of chat interactions according to [The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/). *Question:* Can automation lower customer service OpEx without eroding Chewy's signature white-glove brand loyalty?

**Sources**

1. [Chewy Inc. (via Public) / Quarterly Report for Quarter Ending August 2, 2026 (Form 10-Q)](https://www.publicnow.com/view/A3C3235618841B1AAA702BBC7CABB83B97784FE3)
2. [Chewy, Inc. (CHWY) 10-Q Quarterly Report September 2026](https://last10k.com/sec-filings/chwy/0001628280-26-061018.htm)
3. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
4. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
5. [Chewy quarterly net income rises to $80.5M \| CHWY Quarterly Report (10-Q)](https://www.stocktitan.net/sec-filings/CHWY/10-q-chewy-inc-quarterly-earnings-report-cc169525ddef.html)

#### Run 2

### 1. What They Do, Who Buys, and How They Make Money
Chewy is the largest pure-play pet e-tailer in the U.S., offering ~190,000 products from 4,000 partner brands alongside private labels, pet medications, and telehealth services [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm). Its primary buyers are retail pet owners (~21.7 million active customers) [exa.ai](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript). Chewy generates revenue through direct product and pharmacy sales, heavily underpinned by its automated subscription program, "Autoship," which represents 84.6% of net sales [tenq.co](https://tenq.co/report/CHWY/story).

### 2. Recent News and Launches (Last 6 Months)
* **Modern Animal Acquisition:** On May 21, 2026, Chewy completed the acquisition of Modern Animal, a tech-enabled veterinary clinic platform, expanding its physical and digital healthcare footprint [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm).
* **SmartPak Integration:** Chewy integrated equine supplement and supplies business SmartPak, incurring $7.4 million in transaction-related expenses during the first half of fiscal 2026 [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm).
* **Customer Service Automation:** In mid-2026, Chewy rolled out self-service app chat features, resolving ~30% of routine inquiries (autoship, tracking, returns) autonomously [fool.com](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/).
* **Guidance Increase:** In September 2026, management raised full-year FY2026 net sales and profitability targets [tenq.co](https://tenq.co/report/CHWY/story).

### 3. Funding, Size, and Financial Signals
* **Structure & Ownership:** Publicly traded (NYSE: CHWY); classified as a "controlled company" dominated by BC Partners and affiliated sponsor entities [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm).
* **Key Metrics (Q2 2026):** Active customers reached 21.7 million (+3.8% YoY), with net sales per active customer climbing to $602 (+1.9% YoY) [exa.ai](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript), [tenq.co](https://tenq.co/report/CHWY/story). Autoship sales totaled $2.82 billion for the quarter [tenq.co](https://tenq.co/report/CHWY/story).
* **Balance Sheet:** Long-term debt stood at $588.7 million against $1.85 billion in current assets and $2.20 billion in current liabilities as of August 2, 2026 [tenq.co](https://tenq.co/report/CHWY/story). Free cash flow was $89.5 million in Q2, constrained by $47.9 million in capex [tenq.co](https://tenq.co/report/CHWY/story).

### 4. Leadership
* **Sumit Singh:** Chief Executive Officer and Board Director (leading Chewy’s operational execution and pet healthcare expansion since 2018).
* **David Reeder:** Chief Financial Officer.

### 5. Main Competitors and Differentiation
* **Amazon:** Broader distribution and Prime shipping speed, but lacks Chewy's specialized pet pharmacy compounding, dedicated customer service, and veterinary software integrations.
* **Petco & PetSmart:** Established brick-and-mortar presence with in-store grooming and vet care; Chewy counters with superior digital Autoship retention (84.6% of sales) [tenq.co](https://tenq.co/report/CHWY/story), larger catalog depth, and newly acquired physical veterinary clinics.

### 6. Likely Strategic Priorities and Open Questions
* **Strategic Priorities:** Scaling its integrated healthcare ecosystem (Chewy Vet Care, CarePlus insurance, and Modern Animal clinics) [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [tenq.co](https://tenq.co/report/CHWY/story); driving higher basket sizes ($600+) through cross-selling veterinary care and private brands [exa.ai](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript).
* **Open Questions:** How will the capital expenditure requirements of physical veterinary clinics impact free cash flow margins? Can organic active customer growth accelerate beyond mid-single digits without dilutive promotional spending?

**Sources**

1. [Chewy, Inc. Form 10-Q for the period ended August 2, 2026](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
2. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
3. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
4. [CHWY Earnings Call Transcript — Fiscal Q1 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q1/transcript)
5. [Chewy (CHWY) stock story: what drives it, what the price assumes and the risks \| TenQ](https://tenq.co/report/CHWY/story)

### deepseek/deepseek-v4-pro

Cost: $0.0119

#### Run 1

**1. What they do, who buys it, and how they make money**  
Chewy is the largest pet e-tailer in the U.S., offering approximately 190,000 products from 4,000 brands through its websites and mobile apps [sec.gov]. It serves pet parents with food, treats, supplies, and healthcare products. Revenue comes primarily from direct online sales of consumables and hardgoods, anchored by the recurring Autoship subscription program. In its most recent quarter, Autoship represented 84.6% of net sales, the company had 21.7 million active customers, and net sales per active customer reached $602 [exa.ai]. Chewy also generates revenue through its pharmacy, Chewy Health, and veterinary services [weissratings.com].

**2. Recent news and launches (last 6 months)**  
- Acquired Modern Animal (completed May 2026), a technology-forward veterinary platform, to build an integrated pet healthcare ecosystem [sec.gov].  
- Completed the SmartPak acquisition (first half of fiscal 2026), adding customer relationships, trademarks, and a supplements portfolio [sec.gov].  
- Launched self-service chat in the mobile app; early results show about 30% of common inquiries (orders, returns, Autoship) resolved automatically [fool.com].

**3. Funding, size, and financial signals**  
Chewy went public in 2019 and remains a controlled company, with BC Partners and other sponsors holding majority voting power [sec.gov]. It is the largest U.S. pet e-tailer [sec.gov]. Key signals: 21.7 million active customers, $602 net sales per active customer, and Autoship penetration at 84.6% [exa.ai]. The company is investing in healthcare acquisitions while navigating inflationary pressures and economic uncertainty [sec.gov]. The high Autoship share points to strong recurring revenue and customer loyalty.

**4. Leadership**  
- Sumit Singh – Chief Executive Officer  
- David Reeder – Chief Financial Officer  
- Satish Mehta – Chief Technology Officer  
- Mita Malhotra – Chief Merchandising Officer  
- Jess Holtz – Chief People Officer  
- Barbara Messing – Chief Marketing Officer [weissratings.com]  
Founder Ryan Cohen is no longer involved in day-to-day management [weissratings.com].

**5. Main competitors and how they differ**  
The provided materials do not list competitors, but Chewy’s position as the largest U.S. pet e-tailer [sec.gov] places it against Amazon,

**Sources**

1. [Chewy, Inc. Form 10-Q for the period ended August 2, 2026](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
2. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
3. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
4. [CHWY Earnings Call Transcript — Fiscal Q1 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q1/transcript)
5. [Company Overview - CHWY - NYSE - Weiss Ratings](https://weissratings.com/en/stock/chwy-nyse/company-overview)

#### Run 2

Based on the latest available information, here is a briefing on Chewy, Inc.

### 1. What they do, who buys it, and how they make money
Chewy is the largest pet e-tailer in the United States, offering a broad selection of pet products and services through its websites and mobile apps. It provides approximately 190,000 products from around 4,000 partner brands, alongside its own private brands. The company’s core proposition combines competitive prices, fast shipping, and a high-touch customer service model. Chewy makes money primarily through the direct sale of pet food, treats, supplies, and healthcare products. A dominant 84.6% of its total net sales come through its Autoship subscription program, where customers schedule automatic reorders, creating a highly predictable revenue stream. As of the quarter ending August 2, 2026, Chewy served 21.7 million active customers, with net sales per active customer reaching $602. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [tenq.co](https://tenq.co/report/CHWY/story)

### 2. Recent news and launches (last 6 months)
Chewy has made significant moves to expand its pet healthcare ecosystem. On May 21, 2026, it completed the acquisition of Modern Animal, Inc., a technology-forward veterinary platform. This follows an earlier acquisition of SmartPak, a leader in equine and pet supplements. The company is also integrating technology into its customer service; early results from a new AI-powered self-service chat feature in its mobile app show approximately 30% of common inquiries are now resolved without human intervention. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [fool.com](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)

### 3. Funding, size, and financial signals
Chewy is a publicly traded company controlled by a consortium of sponsors including BC Partners. The company is in an active investment phase, funding acquisitions and share repurchases. For the quarter ended August 2, 2026, Autoship customer sales grew 9.3% to $2.82 billion. However, this expansion is pressuring liquidity; current liabilities of $2.20 billion exceeded current assets of $1.85 billion. Free cash flow was reduced to $89.5 million due to $47.9 million in capital expenditures. Management raised its revenue and profitability outlook on September 9, 2026, but thin operating margins leave little room for cost surprises. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [tenq.co](https://tenq.co/report/CHWY/story)

### 4. Leadership
Specific details on the current executive leadership team were not found in the provided search results. The documents focus on the company’s status as a "controlled company" under NYSE standards, with its Sponsors holding a majority of voting power. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)

### 5. Main competitors and how they differ
Chewy’s competition is broad, including online retailers, physical pet stores, suppliers’ own direct-to-consumer websites, and veterinary providers. While Chewy differentiates itself through its high-touch customer service and dominant Autoship program, it competes directly on price, product availability, and delivery speed. Its recent acquisitions of veterinary platforms like Modern Animal signal a strategic differentiation toward an integrated pet healthcare ecosystem that combines care, commerce, and services, a move that goes beyond the traditional retail model of many competitors. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [tenq.co](https://tenq.co/report/CHWY/story)

### 6. Likely strategic priorities and open questions
Chewy’s strategic priority is clearly to evolve into a fully integrated pet healthcare ecosystem, as evidenced by the acquisitions of SmartPak and Modern Animal. A key open question is how effectively it can integrate these healthcare services with its core e-commerce platform. Other priorities include deepening Autoship penetration while growing its active customer base and managing the financial strain of its expansion. Future disclosures will need to clarify how much growth is organic versus acquisition-driven and whether capital spending will continue to constrain free cash flow. [sec.gov](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm), [tenq.co](https://tenq.co/report/CHWY/story)

**Sources**

1. [Chewy, Inc. Form 10-Q for the period ended August 2, 2026](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
2. [CHWY Earnings Call Transcript — Fiscal Q2 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q2/transcript)
3. [Chewy (CHWY) Q2 2026 Earnings Call Transcript \| The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/chewy-chwy-q2-2026-earnings-call-transcript/)
4. [CHWY Earnings Call Transcript — Fiscal Q1 2027](https://exa.ai/library/markets/stocks/CHWY/earnings/FY2027/Q1/transcript)
5. [Chewy (CHWY) stock story: what drives it, what the price assumes and the risks \| TenQ](https://tenq.co/report/CHWY/story)
