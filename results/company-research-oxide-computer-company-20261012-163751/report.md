# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T16:37:51
- Variables: `company=Oxide Computer Company`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2072 (contestants $0.1369, judge $0.0702)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 8.1 (7.8–8.4) | $0.0396 | 19.4s (19.3s–19.5s) | 5 (5–5) | 4 (4–5) | 2.0 |
| deepseek/deepseek-v4-pro | 7.2 (7.1–7.3) | $0.0103 | 46.3s (45.8s–46.8s) | 5 (5–5) | 6 (5–6) | 7.0 |
| google/gemini-3.8-flash | 7.0 (7.0–7.0) | $0.0185 | 22.4s (21.6s–23.2s) | 5 (5–5) | 6 (5–6) | 3.7 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: This is the most careful briefing: it distinguishes company claims from verified figures, acknowledges missing launch and competitor evidence, and turns the backlog into useful meeting questions.
- **deepseek/deepseek-v4-pro**: Current funding and manufacturing details make this useful, but several customer, competitor, and strategic assertions exceed the supplied excerpts, and some citation URLs contain typos.
- **google/gemini-3.8-flash**: It offers concrete, recent meeting context and a sourced employee figure, but adds numerous unsourced biographies and competitive details.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not establish customers in government or aerospace.
- **anthropic/claude-sonnet-5.5** (run 1): The $200M Series C amount is not present in the supplied excerpt.
- **anthropic/claude-sonnet-5.5** (run 1): The excerpts do not explicitly identify Bryan Cantrill as CTO.
- **anthropic/claude-sonnet-5.5** (run 1): Support for OpenShift, Rancher, and Terraform is not shown in the cited homepage excerpt.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish customers in government or aerospace.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not identify Bryan Cantrill as CTO.
- **deepseek/deepseek-v4-pro** (run 1): The named hyperscalers and OEMs, and the description of their on-premises offerings, are not substantiated by the excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not establish that the Series D is intended to preserve independence rather than precede an exit.
- **deepseek/deepseek-v4-pro** (run 1): The homepage says '2-hour setup,' not setup in under two hours.
- **deepseek/deepseek-v4-pro** (run 1): The characterization of the founders' public stewardship and the blog post's voice is not supported.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not establish customers in aerospace or government.
- **google/gemini-3.8-flash** (run 1): The $200M Series C is not stated in the supplied excerpts; presenting total funding as merely 'over $645M' omits the sourced $809M figure.
- **google/gemini-3.8-flash** (run 1): The founders' former Joyent positions, Cantrill's DTrace work, and his CTO title are not established by the excerpts.
- **google/gemini-3.8-flash** (run 1): The named OEM, virtualization, and cloud-appliance competitors are not identified in the excerpts.
- **google/gemini-3.8-flash** (run 1): Claims about Oxide's silicon integration, competitors' hypervisor fees, and post-Broadcom VMware price hikes are not supported.
- **google/gemini-3.8-flash** (run 1): The excerpts do not say manufacturing expanded particularly because of agentic-AI demand or establish plans for deeper AMD silicon integration.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not establish the full list of customer sectors, including government and aerospace.
- **anthropic/claude-sonnet-5.5** (run 2): The $200M Series C amount is not in the cited excerpt.
- **anthropic/claude-sonnet-5.5** (run 2): The supplied excerpts do not establish Cantrill’s CTO title, compatibility with Terraform, OpenShift and Rancher, or his statement that Oxide did not anticipate the agentic-AI surge.
- **anthropic/claude-sonnet-5.5** (run 2): Dell, HPE and Nutanix are proposed as rivals from expressly uncited background knowledge; the excerpts do not verify them.
- **anthropic/claude-sonnet-5.5** (run 2): The claim that Oxide made an early bet on AMD EPYC is not established by the cited excerpt.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish API/CLI/console provisioning or the full list of customer sectors, including government and aerospace.
- **deepseek/deepseek-v4-pro** (run 2): The excerpts support AMD Ventures joining the round, but not a deepened co-engineering partnership across the hardware and software stack.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts do not establish the descriptions of Dell and HPE systems or the asserted lock-in, egress fees and subscriptions of AWS Outposts and Azure Stack.
- **deepseek/deepseek-v4-pro** (run 2): The claim that Tuck and Cantrill founded the company in 2019 is not established by the cited excerpts, which separately identify the founding year and the co-founders.
- **deepseek/deepseek-v4-pro** (run 2): Selective entry into new verticals and AMD silicon-roadmap alignment are presented as priorities without supporting evidence.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not establish aerospace or government/defense customers, or the stated customer motivations of data sovereignty and predictable latency.
- **google/gemini-3.8-flash** (run 2): The excerpts do not support the claims of no support tiers, a $200M Series C, or AMD co-engineering and platform-enablement work.
- **google/gemini-3.8-flash** (run 2): The cited excerpts do not establish Tuck’s and Cantrill’s previous roles or Cantrill’s role in creating DTrace.
- **google/gemini-3.8-flash** (run 2): The descriptions of AWS and Azure appliances’ pricing and lock-in, and of legacy vendors’ cabling, licensing and maintenance, are not supported by the excerpts.
- **google/gemini-3.8-flash** (run 2): The excerpts do not establish a multi-quarter backlog or plans to improve memory and compute density through AMD.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0396

#### Run 1

# Oxide Computer Company briefing (as of Oct 12, 2026)

## 1. What they do, who buys, how they make money
Oxide sells the Cloud Computer, a rack-scale system with co-designed compute, storage, networking and open-source software. It brings hyperscale-style cloud to a customer's own data center ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)). Customers span financial services, government, national laboratories, aerospace and other compute-intensive industries (same source). Revenue comes from hardware sales: the company says it is a one-time purchase with no licensing fees, and claims half the price of public cloud and traditional on-prem ([oxide.computer](https://oxide.computer/)). That pricing claim is Oxide's own and unverified.

## 2. Recent news (last 6 months)
- **Oct 9, 2026:** Announced a $445M Series D ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Spring 2026:** Paid income tax for the first time, from ordinary operations ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- **Manufacturing:** The CEO says capacity grew 20x over the past 12 months, and demand still exceeds supply ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Product launches:** I found no specific launches in the sources. The homepage shows "Rack 6 Initialized," but I can't tell what it refers to ([oxide.computer](https://oxide.computer/)).

## 3. Funding, size, financial signals
- The Series D was led by Eclipse. Existing investors USIT, Riot Ventures and Jane Street joined, and new investors include Atreides Management and AMD Ventures ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- CB Insights puts total raised at $809M ([cbinsights.com](https://www.cbinsights.com/company/oxide-computer)). The prior round was a $200M Series C ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- The company describes itself as profitable with a very large order backlog. It also has existing debt facilities, and cash is needed up front for components and manufacturing ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- **Not found:** revenue, valuation, headcount, customer counts.

## 4. Leadership
- **Steve Tuck**, co-founder and CEO.
- **Bryan Cantrill**, co-founder and CTO ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

I found no other executive information. The company was founded in 2019 and is based in Emeryville, CA.

## 5. Competitors
CB Insights names Mithril and "5 more" without listing them ([cbinsights.com](https://www.cbinsights.com/company/oxide-computer)). Oxide positions itself against public cloud and traditional on-prem, arguing for integrated hardware and software over assembled components, with no subscriptions or egress fees ([oxide.computer](https://oxide.computer/)). It also integrates with tools such as Kubernetes, OpenShift, Rancher and Terraform (same source). I found no sourced competitor comparison. Expect incumbent server and private-cloud vendors and the hyperscalers to come up, but verify that independently.

## 6. Likely priorities and open questions
**Priorities**
- Secure components and scale manufacturing to clear the backlog while still taking new orders ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- Ride demand for agentic AI and sovereign or on-prem compute.
- Deepen the AMD relationship. Oxide's systems use AMD EPYC processors, and AMD Ventures has now invested ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

**Questions to ask**
- How large is the backlog, and what are realistic delivery lead times?
- How exposed is Oxide to component supply shocks? Its own post flags this risk.
- How durable is profitability while it spends heavily on inventory?
- What are the AI-specific offerings, beyond the marketing language?
- Who are the real competitive alternatives in deals?

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)
5. [Oxide's Series D & The Power of Perseverance](https://www.counterpart.vc/news/oxides-series-d-the-power-of-perseverance)

#### Run 2

# Oxide Computer Company: Briefing (as of Oct 12, 2026)

## 1. What they do, who buys it, how they make money
Oxide makes the Oxide Cloud Computer, a rack-scale system with co-designed hardware and open-source software that brings hyperscale-style cloud to a customer's own data center ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)). Customers include financial services, government, national laboratories, aerospace, and other compute-intensive industries ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)). Oxide sells hardware as a one-time purchase with no licensing fees. It claims about half the cost of public cloud and traditional on-prem, and setup in about 2 hours ([oxide.computer](https://oxide.computer/)). Those are vendor claims, not independently verified.

## 2. Recent news (last 6 months)
- **Oct 9, 2026:** Announced a $445M Series D ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Spring 2026:** Paid income tax for the first time, because ordinary operations generated taxable income ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- **Capacity:** Manufacturing capacity grew 20x over the past 12 months, and demand still exceeds supply ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Product launches:** I found none in the search results.

## 3. Funding, size, financial signals
- **Series D:** $445M, led by Eclipse. Existing investors USIT, Riot Ventures, and Jane Street participated. New investors are Atreides Management and AMD Ventures ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Prior capital:** A $200M Series C, a Series B, and existing debt facilities ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- **Profitability and backlog:** Oxide describes itself as profitable with a very large order backlog. The new money is mainly working capital to buy components ahead of shipments ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- **Headcount:** About 122 employees, per [pitchbook.com](https://pitchbook.com/profiles/company/343384-66).
- **Not found:** Revenue, valuation, and customer counts.

## 4. Leadership
- **Steve Tuck:** Co-founder and CEO.
- **Bryan Cantrill:** Co-founder and CTO ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- **Other executives:** Not covered in the results.

## 5. Competitors and differentiation
The search results name no competitors. Oxide's own positioning contrasts it with public cloud and traditional on-prem infrastructure. It cites no subscriptions, egress fees, or licensing, and says it offers a hardware root of trust and open-source firmware ([oxide.computer](https://oxide.computer/)). It also lists compatibility with Kubernetes, Terraform, OpenShift, and Rancher, so these are tools it works with rather than rivals ([oxide.computer](https://oxide.computer/)). From my own background knowledge (uncited), likely rivals are traditional server and hyperconverged vendors such as Dell, HPE, and Nutanix, plus hyperscaler on-prem offerings. Verify before relying on this.

## 6. Likely priorities and open questions
**Priorities (inferred from the sources):**
- Scale manufacturing and secure component supply ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- Work through the backlog while still accepting new demand ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
- Ride demand from agentic AI workloads, though Cantrill said Oxide did not anticipate that surge ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
- Deepen the AMD relationship. AMD is now a strategic investor, and Oxide's early bet was on AMD EPYC ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).

**Open questions to ask:**
- What are lead times and backlog size?
- How exposed is Oxide to supply shocks, and to dependence on AMD?
- What is the AI/GPU roadmap? The site mentions AI workloads, but the sources give no hardware details.
- What are real customer count, revenue, and pricing?

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)
5. [Oxide Computer 2026 Company Profile: Valuation, Funding & Investors \| PitchBook](https://pitchbook.com/profiles/company/343384-66)

### deepseek/deepseek-v4-pro

Cost: $0.0103

#### Run 1

**Oxide Computer Company Briefing**  
*October 12, 2026*

### 1. What they do, who buys it, and how they make money
Oxide sells the **Oxide Cloud Computer**, a rack‑scale system that combines purpose‑built hardware with open‑source software to deliver a public‑cloud‑like experience inside an enterprise’s own data center. The system provides on‑demand virtual machines, Kubernetes orchestration, programmable networking, block storage, and API‑driven automation – all with a hardware root of trust and cryptographic isolation [oxide.computer](https://oxide.computer/).  
Customers span financial services, government, national laboratoris, aerospae, and other compute‑intensive industries that need security, sovereignty, and predictable costs [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html).  
Revenue comes from a **one‑time purchase of the hardware**; there are no subscriptions, licensing fees, or egress charges [oxide.computer](https://oxide.computer/).

### 2. Recent news and launches (last 6 months)
- **Series D funding ($445M)** was announced on October 9, 2026. The round was led by Eclipse, with participation from USIT, Riot Ventures, Jane Street, Atreides Management, and a strategic investment from AMD Ventures [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html).  
- Earlier in the spring of 2026, the company **achieved profitability** – paying income tax from ordinary operations – a rare milestone for a fast‑scaling hardware startup [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).  
- Over the last 12 months, manufacturing capacity has **scaled 20x** to keep pace with demand, yet the order backlog still exceeds supply [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html).

### 3. Funding, size, and financial signals
- **Total raised: $809 million** [cbinsights.com](https://www.cbinsights.com/company/oxide-computer).  
- The latest $445M Series D brings working capital to secure components, fill the substantial backlog, and expand manufacturing while continuing to accept new demand [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).  
- Oxied **reached profitability in early 2026**, generating taxable income solely from selling computers. Before the round, the company already had enough cash (from prior series and debt facilities) to meet its existing backlog, but the large absolute numbers required caution [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).  
- The company’s own description emphasizes an enduring, long‑haul mentality – the Series D is intended to assure longevity and independence, not a prelude to an exit [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).

### 4. Leadership
- **Steve Tuck – Co‑founder & CEO** [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-provies-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html).  
- **Bryan Cantrill – Co‑founder & CTO** [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-provies-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html).  
- Both have been vocal stewards of the company’s vision since founding in 2019; the Series D blog post is written in their characteristically frank voice [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).

###5. Main competitors and how they differ
- According to CB Insights, competitors include **Mithril and five others** [cbinsights.com](https://www.cbinsights.com/company/oxide-computer).  
- More broadly, Oxide competes against public cloud providers (AWS, Azure, GCP) that offer on‑premises extensions like Outposts or Azure Stack, and traditional on‑prem vendors (Dell, HPE) that sell disaggregated hardware plus software licenses.  
- Oxide’s key differentiation: a **fully co‑designed, full‑stack system** that provides cloud‑native elasticity and API‑driven control **without subscriptions, egress fees, or multi‑vendor integration complexity**. It claims to deliver this at roughly half the cost of public cloud or traditional on‑prem, with setup in under two hours [oxide.computer](https://oxide.computer/).

###6. Likely strategic priorities and open questions
- **Priorities**: Use Series D capital to convert backlog, secure component inventory, and continue scaling manufacturing. Deepen the AMD partnership (now a strategic investor) to support the **growing compute demands of agentic AI** [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-provies-vis-ion-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html). Preserve the company’s independent, long‑term orientation [oxide.computer/blog](https://oxide.computer/blog/our-445m-series-d).  
- **Open questions**: Can supply‑chain and manufacturing scaling keep pace with the20x expansion without introducing quality or delivery risks? How large is the adressable market for on‑prem “cloud computers” once the early adopter wave subsides? Will the incumbents (hyperscalers and legacy OEMs) accelerate their own integrated on‑prem offers, and how defensible is Oxide’s full‑stack approach? No public information on international expansion or the specifics of the AMD Ventures relationship beyond the strategic investment.

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide's Series D & The Power of Perseverance](https://www.counterpart.vc/news/oxides-series-d-the-power-of-perseverance)
5. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)

#### Run 2

### 1. What they do, who buys it, and how they make money
Oxide sells a rack-scale, on-premises cloud computer that combines co-designed hardware and open-source software to deliver public-cloud-like elasticity, programmability, and self-service to an enterprise’s own data center. Buyers get on-demand VMs, Kubernetes, and API/CLI/console provisioning on AMD EPYC processors, with a hardware root of trust, cryptographic isolation, and no subscription or egress fees. [oxide.computer](https://oxide.computer/)  
Customers are organizations with demanding infrastructure requirements: financial services firms, government agencies, national laboratories, aerospace, and other compute-intensive industries. [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)  
Revenue comes from one-time purchases of the integrated rack-scale systems—no licensing fees or recurring subscriptions—so the model is straightforward hardware sales.

### 2. Recent news and launches (last 6 months)
- **$445M Series D (Oct 2026):** Led by Eclipse, with participation from USITF, Riot Ventures, Jane Street, AMD Ventures (a new strategic investor), and others. The round provides working capital to secure components and scale manufacturing. [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)  
- **Profitability milestone:** Earlier in 2026 Oxide became profitabe, paying income tax from ordinary operations—a rare feat for a hardware company at this scale. [oxide.computer](https://oxide.computer/blog/our-445m-series-d)  
- **Manufacturing scale-up:** The company expanded manufacturing capacity 20x over the past 12 months, yet demand still exceeds supply. [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)  
- **AMD Ventures strategic investment:** Deepens the existing co-engineering partnership across the hardare/softeare stack, particularly as agentic AI drives new compute, memory, and networking demands. [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)

### 3. Funding, size, and financial signals
- **Total raised:** $809M, following the $445M Series D. [cbinsights.com](https://www.cbinsights.com/company/oxide-computer)  
- **Profitability:** Achieved earlier this year; the company generated taxable income from selling computers, not from one-off events. [oxide.computer](https://oxide.computer/blog/our-445m-series-d)  
- **Backlog and demand:** A “very large” order backlog exists, and demand continues to outstrip supply even after a 20x manufacturing ramp. The Series D explicitly addresses the need for cash to pre-purchase components. [oxide.computer](https://oxide.computer/blog/our-445m-series-d)  
- **Headcount:** Not publicly disclosed in these sources.

### 4. Leadership
- **Steve Tuck,** Co-founder & CEO  
- **Bryan Cantrill,** Co-founder & CTO  
The pair founded the company in 2019 and are credited with the original vision and “unwillingness to let this vision dissipate.” [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html) [counterpart.vc](https://www.counterpart.vc/news/oxides-series-d-the-power-of-perseverance)

### 5. Main competitors and how they differ
Competitors named by third-party data include Mithril and others, but Oxide’s differentiation is structural. [cbinsights.com](https://www.cbinsights.com/company/oxide-computer)  
- **Traditional on-prem vendors (Del, HPe):** Assemble discrete components; Oxide delivers a pre-integrated, cloud-native experience with unified hardare/softeare, no licensing complexity.  
- **Public-cloud hybrd solutions (AWS Outosts, Azure Stak):** Often come with vendor lock-in, egress fees, and ongoing subscriptions. Oxide offers a one-time purchase at roughly half the cost of public cloud, with no surprise bills. [oxide.computer](https://oxide.computer/)  
Oxide’s core moat is co-design: the rack-scale system includes compute, storage, networking, and open-source software, giving enterprises hyperscale cloud agility with full ownership and governance.

### 6. Likely strategic priorities and open questions
**Priorities:**
- Aggressively scale manufacturing and secure the component supply chain to fulfill the existing backlog and capture new demand, particularly from agentic AI workloads.
- Deepen the AMD relationship to ensure silicon roadma alignment and co-engineering advances.
- Continue to prove the model in financial services, government, and labs, while selectively entering new verticles.

**Open questions:**
- Can Oxide sustain (or grow) profitability while the capital-intensive hardware business doubles down on growth?
- How large is the total addressable market for on-prem cloud computers, and what is the competitive response from established sever OEMs and cloud hybrd solutions?
- How concentrated is supply risk on AMD, and could a shift in AMD’s strategy or external shocks disrupt Oxide’s manufacturing curve? The leadership acnowledges caution from the Dot Com bust and the possibility of “supply disruptions, economic shocks” [oxide.computer](https://oxide.computer/blog/our-445m-series-d), so this is very much on their radar.

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide's Series D & The Power of Perseverance](https://www.counterpart.vc/news/oxides-series-d-the-power-of-perseverance)
5. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)

### google/gemini-3.8-flash

Cost: $0.0185

#### Run 1

### 1. What They Do, Who Buys It, & How They Make Money
Oxide Computer Company designs and manufactures the "Cloud Computer," a vertically integrated, rack-scale system delivering hyperscale cloud functionality to on-premises data centers ([oxide.computer](https://oxide.computer/)). They co-design custom hardware (powered by AMD EPYC processors), networking, and open-source software/firmware into a unified appliance that installs in hours ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)). 

* **Buyers:** Compute-intensive enterprises in financial services, aerospace, government, national laboratories, and AI/data engineering seeking cloud agility without data sovereignty, security, or egress issues ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Monetization:** Outright hardware sales. Unlike traditional enterprise vendors, Oxide charges no recurring licensing, hypervisor, or subscription software fees ([oxide.computer](https://oxide.computer/)).

### 2. Recent News & Launches
* **$445M Series D (October 2026):** Raised a $445 million Series D led by Eclipse, with participation from USIT, Riot Ventures, Jane Street, Atreides Management, and a strategic investment from AMD Ventures ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Manufacturing Expansion:** Scaled manufacturing capacity 20x over the prior 12 months to meet demand surges, particularly for agentic AI workloads ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

### 3. Funding, Size, & Financial Signals
* **Funding:** Over $645M in total funding, following a $200M Series C and the recent $445M Series D ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
* **Size:** ~122 employees, based in Emeryville, California ([pitchbook.com](https://pitchbook.com/profiles/company/343384-66)).
* **Financial Signals:** Reached profitability in spring 2026, generating positive taxable income and cash flow from normal operations ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)). Demand currently far outstrips capacity, resulting in a large order backlog ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).

### 4. Leadership
* **Steve Tuck (Co-founder & CEO):** Former SVP of Sales and Solutions at Joyent ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Bryan Cantrill (Co-founder & CTO):** Former CTO of Joyent, systems software pioneer (co-creator of DTrace at Sun Microsystems) ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

### 5. Main Competitors & Differentiation
* **Competitors:** Legacy server OEMs (Dell, HPE), virtualization/private cloud software (VMware/Broadcom, Nutanix), and public cloud on-prem appliances (AWS Outposts, Azure Stack).
* **Differentiation:** 
  * *True vertical integration:* Rather than piecing together disparate OEM components and third-party hypervisors, Oxide builds the silicon integration, hardware root-of-trust, networking, and software stack from the ground up ([prnewswire.com](https://prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
  * *No subscription lock-in:* Avoids ongoing software licensing overhead (e.g., post-Broadcom VMware price hikes) and cloudy subscription tethering ([oxide.computer](https://oxide.computer/)).

### 6. Strategic Priorities & Open Questions
* **Priorities:** Deploying Series D capital into component purchasing and scaling manufacturing throughput to clear the order backlog; expanding deep integration with AMD silicon for agentic AI and HPC workloads ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
* **Open Questions:**
  * Can Oxide scale assembly and quality control quickly enough without hitting hardware supply chain bottlenecks?
  * What is their dedicated roadmap for specialized AI accelerators/GPUs to address GPU-heavy agentic training and inference?

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)
5. [Oxide Computer 2026 Company Profile: Valuation, Funding & Investors \| PitchBook](https://pitchbook.com/profiles/company/343384-66)

#### Run 2

### 1. What They Do, Who Buys It, and How They Make Money
Oxide builds the **Cloud Computer**, an integrated rack-scale server system co-designing hardware, firmware, and software to deliver a hyperscale public cloud operational model inside on-premises data centers ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)). 

* **Customers:** Compute-intensive enterprises in financial services, aerospace, government/defense, national laboratories, and AI engineering seeking data sovereignty and predictable latency ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Business Model:** Systems are purchased outright as a one-time capital investment—with zero software subscription licensing, support tiers, or egress fees ([oxide.computer](https://oxide.computer/)).

### 2. Recent News & Launches (Last 6 Months)
* **Series D Raise:** Closed a massive $445M Series D round in October 2026 led by Eclipse to fulfill an extensive order backlog ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
* **AMD Strategic Partnership:** AMD Ventures joined as a strategic investor, expanding co-engineering around AMD EPYC silicon and platform enablement software ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
* **Manufacturing Scale:** Scaled production capacity 20x over the prior year to address surging demand from cloud repatriation and agentic AI workloads ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

### 3. Funding, Size, and Financial Signals
* **Total Funding:** ~$809M raised across all rounds ([cbinsights.com](https://www.cbinsights.com/company/oxide-computer)), including the $445M Series D (2026) and prior $200M Series C ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).
* **Key Backers:** Eclipse, USIT, Jane Street, Riot Ventures, Atreides Management, and AMD Ventures ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Financial Signals:** Oxide turned cash-flow positive from operations and paid corporate income tax in early 2026, though working capital demands remain high to procure inventory against severe demand-supply imbalances ([oxide.computer](https://oxide.computer/blog/our-445m-series-d)).

### 4. Leadership
* **Steve Tuck (Co-Founder & CEO):** Former SVP of Joyent; experienced cloud infrastructure executive ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Bryan Cantrill (Co-Founder & CTO):** Systems pioneer, former Joyent CTO, and Sun Microsystems veteran known for co-creating DTrace ([prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).

### 5. Main Competitors & Key Differentiators
* **Hyperscaler Hybrid Appliances (AWS Outposts, Azure Stack):** These rely on rented hardware, perpetual operational fees, and vendor lock-in. Oxide is a customer-owned, open-source stack with no egress fees ([oxide.computer](https://oxide.computer/)).
* **Legacy OEMs (Dell, HPE, Cisco) + VMware:** Legacy vendors assemble piecemeal systems requiring fragile cabling, separate software licenses, and complex maintenance contracts. Oxide provides a unified, vertically integrated rack that deploys in under two hours with API-native control ([oxide.computer](https://oxide.computer/)).

### 6. Likely Strategic Priorities & Open Questions
* **Strategic Priorities:** Securing supply chain components and scaling manufacturing throughput to clear the multi-quarter backlog; deepening integration with AMD for memory/compute density in AI environments ([oxide.computer](https://oxide.computer/blog/our-445m-series-d), [prnewswire.com](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)).
* **Open Questions:**
  1. *Hardware Lead Times:* Can Oxide scale its supply chain fast enough to prevent customer churn to legacy OEMs?
  2. *AI Accelerator Strategy:* While built on AMD EPYC CPUs, how does Oxide plan to natively accommodate discrete GPU clusters and specialized accelerators demanded by frontier AI models?

**Sources**

1. [Our $445M Series D \| Oxide Computer Company](https://oxide.computer/blog/our-445m-series-d)
2. [Oxide Computer Company](https://oxide.computer/)
3. [Oxide Raises $445M Series D as the Company Proves Vision of Full-Stack Cloud Infrastructure Enterprises Can Own](https://www.prnewswire.com/news-releases/oxide-raises-445m-series-d-as-the-company-proves-vision-of-full-stack-cloud-infrastructure-enterprises-can-own-302903159.html)
4. [Oxide's Series D & The Power of Perseverance](https://www.counterpart.vc/news/oxides-series-d-the-power-of-perseverance)
5. [Oxide - Products, Competitors, Financials, Employees ...](https://www.cbinsights.com/company/oxide-computer)
