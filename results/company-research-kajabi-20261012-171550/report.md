# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T17:15:50
- Variables: `company=Kajabi`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2258 (contestants $0.1508, judge $0.0750)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 7.7 (7.5–7.9) | $0.0384 | 19.9s (18.6s–21.1s) | 5 (5–5) | 4 (4–4) | 2.0 |
| google/gemini-3.8-flash | 6.4 (6.3–6.5) | $0.0213 | 27.2s (26.3s–28.2s) | 5 (5–5) | 5 (5–5) | 3.0 |
| deepseek/deepseek-v4-pro | 5.8 (5.8–5.8) | $0.0157 | 75.3s (62.3s–88.4s) | 5 (5–5) | 5 (4–6) | 3.7 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: It identifies a potentially recent launch, flags verification gaps, and offers useful meeting questions, though some funding, leadership, and competitor details lack support in the provided excerpts.
- **google/gemini-3.8-flash**: The briefing is specific and its strategic questions are useful, but it overstates several financial claims and treats late-2025 and early-2026 developments as recent.
- **deepseek/deepseek-v4-pro**: Concrete product and pricing details help, but several claims exceed the excerpts, the news is outside a six-month window ending in October 2026, and the answer stops before section 6.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not establish Tiger Global as lead investor, a valuation above $2 billion, or that the 2019 investment was Kajabi's first outside capital.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not substantiate the stated 2025 leadership transition.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not substantiate most of the competitor-by-competitor comparisons, including Skool's $99 monthly price.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not establish the dates given for Creator Studio, Cofounder, and Expert Agents.
- **google/gemini-3.8-flash** (run 1): The cited source labels the $100 million-plus figure as revenue, not ARR.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not establish approximately 390 employees or cumulative creator sales above $10 billion.
- **google/gemini-3.8-flash** (run 1): The source says no primary round has been disclosed since 2021; it does not establish that none was raised.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not substantiate the stated leadership transition or establish that the AI tools autonomously handle business operations.
- **google/gemini-3.8-flash** (run 1): The claim that Kajabi is much more economical above $2,000 per month is not supported by a cited comparison.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish the approximately 2.9% plus $0.30 Kajabi Payments charge.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not establish approximately 391 employees, the Irvine headquarters, cumulative creator sales above $10 billion, or the detailed 2021 investor list.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not substantiate the stated leadership transition.
- **deepseek/deepseek-v4-pro** (run 1): The cited excerpts do not substantiate several named competitors or the specific claim that Podia pressures Kajabi on price.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate the 2.9% + 30¢ Kajabi Payments rate.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate Creator Studio’s 2024 launch or Adobe involvement.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate the funding history before the 2021 round, the $10B cumulative creator-sales figure, or the named leadership changes.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate several competitor details, including Podia’s cheaper tier and Teachable’s historical transaction fees.
- **google/gemini-3.8-flash** (run 2): The supplied excerpts do not establish the 2.9% + 30¢ Kajabi Payments rate or payment processing as a source of Kajabi revenue.
- **google/gemini-3.8-flash** (run 2): The supplied excerpts do not establish that AI Cofounder and Expert Agents are autonomous digital teammates.
- **google/gemini-3.8-flash** (run 2): The supplied excerpts do not substantiate Tiger Global’s lead role, the $100M ARR at the 2021 round, $10B in cumulative GMV, approximately 390 employees, or the named leadership changes.
- **google/gemini-3.8-flash** (run 2): The supplied excerpts do not substantiate the full competitor list or the claim that fintech products are high-margin.
- **google/gemini-3.8-flash** (run 2): The cited late-2025 and early-2026 items are not shown to fall within the last six months of Answer A’s stated October 2026 reference date.
- **deepseek/deepseek-v4-pro** (run 2): The supplied excerpts do not establish the 2.9% + 30¢ Kajabi Payments rate or that this is the only fee charged when using it.
- **deepseek/deepseek-v4-pro** (run 2): The supplied excerpts do not establish that the AI agents are designed to slash content-creation time.
- **deepseek/deepseek-v4-pro** (run 2): No disclosed primary round since 2021 does not establish that no primary round occurred.
- **deepseek/deepseek-v4-pro** (run 2): The excerpts do not support a current $100M+ ARR estimate, stable headcount over time, or the conclusion that Kajabi is currently cash-generating.
- **deepseek/deepseek-v4-pro** (run 2): The supplied excerpts do not substantiate the $10B platform-sales figure, named leadership changes, or several competitor distinctions.
- **deepseek/deepseek-v4-pro** (run 2): The cited late-2025 and early-2026 items are not shown to fall within the last six months of Answer A’s stated October 2026 reference date.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0384

#### Run 1

# Kajabi Briefing (as of 2026-10-12)

## 1. What they do, who buys it, how they make money
Kajabi is an all-in-one platform for experts and creators to build and sell courses, memberships, coaching, newsletters, and podcasts, with marketing and payment tools ([cbinsights.com](https://www.cbinsights.com/company/kajabi)). Its customers skew toward mid-sized experts: 89% of full-time creators have 50,000 or fewer Instagram followers, and Kajabi reports 60,000+ creators ([yespress.io](https://yespress.io/kajabi)). Revenue is mainly subscriptions, plus an optional paid branded mobile app ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).

**Source conflict to verify:** akta.pro says Basic is $179/month with 0% transaction fees. yespress.io says plans run from roughly $55 to $319/month, with an optional ~2.9% + 30¢ fee on Kajabi Payments. These may reflect different dates or tier names, so confirm current pricing directly.

## 2. Recent news and launches
- Kajabi announced five new products for expert-led businesses ([linkedin.com](https://www.linkedin.com/posts/kajabi_this-isnt-the-kajabi-youve-come-to-know-activity-7462552804268654592-J2Iv)). I couldn't confirm the exact date or the full list.
- A Kajabi MCP connects Kajabi to tools like Claude or ChatGPT and drafts courses, sales pages, and email sequences from a prompt. A 50% off, six-month promo ran through June 5 ([linkedin.com](https://www.linkedin.com/posts/kajabi_this-isnt-the-kajabi-youve-come-to-know-activity-7462552804268654592-J2Iv)). The year isn't stated.
- Just outside the window, Kajabi Capital launched with Parafin in December 2025, offering financing for U.S. creators ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).

## 3. Funding, size, financial signals
- Kajabi raised a $550M round in May 2021 led by Tiger Global, at a valuation above $2B. Spectrum Equity made a minority investment in 2019, the first outside capital ([dot.la](https://dot.la/kajabi-president-sean-kim-2656529729.html)).
- There has been no disclosed primary round since, and headcount is in the 251–500 range ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- The company said it was profitable with record ARR in 2021 but declined to share revenue ([dot.la](https://dot.la/kajabi-president-sean-kim-2656529729.html)). I found no current revenue or profitability data.

## 4. Leadership
- Ahad Khan became CEO in 2021 and left in 2025. Co-founder Kenny Rueter returned as Co-CEO alongside longtime president Jonathan Cronstedt ([yespress.io](https://yespress.io/kajabi)).
- Sean Kim, ex-TikTok, was hired in 2022 as president and chief product officer ([dot.la](https://dot.la/kajabi-president-sean-kim-2656529729.html)). I couldn't confirm his current status, given that Cronstedt is described as president.
- The CB Insights profile lists Newport Beach as the base, while the 2022 dot.la article says Irvine ([cbinsights.com](https://www.cbinsights.com/company/kajabi)). Check the current location.

## 5. Main competitors
Per [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi):
- **Thinkific, Teachable:** course-focused. Teachable historically charged transaction fees.
- **Podia:** cheaper entry tier, which pressures Kajabi's higher entry price.
- **Kit (ConvertKit), Substack:** email- and newsletter-led.
- **Mighty Networks, Circle, Patreon:** community and membership-led.
- **Skool:** gamified all-in-one at $99/month, called one of Kajabi's most credible emerging threats.

## 6. Likely priorities and open questions
Priorities (my inference from the sources):
- AI-led product work: Creator Studio (2024), Cofounder and Expert Agents (2025) ([yespress.io](https://yespress.io/kajabi)), and the MCP.
- Fintech expansion through Kajabi Capital.
- Defending against low-cost rivals such as Skool and Podia, with heavy promotions.

Open questions:
- What is the current pricing and fee structure?
- What drove the 2025 CEO change?
- What is the revenue and profitability trajectory, given no round since 2021?
- Which products were in the five-product launch, and how are they performing?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi Launches New Products for Expert-Led Businesses - LinkedIn](https://www.linkedin.com/posts/kajabi_this-isnt-the-kajabi-youve-come-to-know-activity-7462552804268654592-J2Iv)
3. [Kajabi - Products, Competitors, Financials, Employees ... - CB Insights](https://www.cbinsights.com/company/kajabi)
4. [Knowledge Creator Platform Kajabi Raids TikTok for New President](https://dot.la/kajabi-president-sean-kim-2656529729.html)
5. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)

#### Run 2

# Kajabi Briefing (as of 12 Oct 2026)

## 1. What they do, who buys it, how they make money
Kajabi is an all-in-one platform for solo experts. One account covers a website, courses, coaching, memberships and community, podcasts, digital downloads, email, funnels and payments ([yespress.io](https://yespress.io/kajabi)). It targets mid-sized creators: 89% of full-time creators have 50,000 or fewer Instagram followers. Kajabi claims 60,000+ creators and about 85 million cumulative buyers ([yespress.io](https://yespress.io/kajabi)).

Revenue is mainly subscriptions, plus an optional branded mobile app add-on ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Current pricing is Basic $179/mo, Growth $249 and Pro $499, with lower annual rates. Kickstarter is no longer sold to new customers ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

**Conflict to verify:** one source says Kajabi takes 0% transaction fees ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Another says Kajabi Payments adds about 2.9% + 30¢ if you don't use Stripe or PayPal ([yespress.io](https://yespress.io/kajabi)). Ask which applies.

## 2. Recent news and launches
I found no items clearly dated within the last six months (April–October 2026). The most recent items I could find are:
- **Dec 2025:** Kajabi Capital, embedded financing built with Parafin for eligible US creators ([askcyborg.com](https://askcyborg.com/company/kajabi)).
- **Late 2025 to early 2026:** the "Kajabi Evolved" update added a visual automation builder, affiliate tools, an open API and communities across plans ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)).
- **Jan 2026:** price increases of +$30 (Basic), +$50 (Growth) and +$100 (Pro). Basic's contact limit fell from 10,000 to 2,500. Existing customers had no grandfathering. Basic includes no AI credits ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **AI:** Creator Studio (2024, built with Adobe) and Cofounder plus Expert Agents (rolling out from 2025) ([yespress.io](https://yespress.io/kajabi)).

## 3. Funding, size, financial signals
- Bootstrapped and profitable for about a decade. Spectrum Equity invested in 2019. A $550M round in May 2021, led by Tiger Global, valued the company at over $2B ([yespress.io](https://yespress.io/kajabi)).
- No primary round disclosed since 2021. Headcount is 251–500 ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)); another source says 391 ([askcyborg.com](https://askcyborg.com/company/kajabi)).
- One source reports revenue of $100M+ and says the company hit $100M ARR in 2021 ([askcyborg.com](https://askcyborg.com/company/kajabi)). I found no current audited figures.
- Cumulative creator sales passed $10B ([yespress.io](https://yespress.io/kajabi)).

## 4. Leadership
Co-founder Kenny Rueter and longtime president Jonathan Cronstedt are Co-CEOs. Ahad Khan, CEO since 2021, left in 2025 ([yespress.io](https://yespress.io/kajabi)). I found no other executive details.

## 5. Competitors
- **Thinkific, Teachable:** course-focused rivals. Kajabi publishes Thinkific migration guides, and Teachable historically charged transaction fees.
- **Podia:** cheaper entry tier pressures Kajabi's higher entry price.
- **Patreon, Kit, Mighty Networks, Circle:** membership, email and community overlap. Kajabi publishes Patreon migration content.
- **Emerging:** Skool and Substack. **Broad incumbent:** Shopify ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- Another source also lists Hotmart, HoneyBook and ClickFunnels ([askcyborg.com](https://askcyborg.com/company/kajabi)).

Kajabi's pitch is consolidation and fixed pricing rather than revenue share.

## 6. Likely priorities and open questions
**Priorities (my inference from the sources):**
- Moving upmarket toward established creators, based on the price rises and removal of the entry plan.
- AI as a differentiator, with credits gating some features.
- Expanding into financial services, via Kajabi Capital.

**Open questions:**
- Has churn risen after the January price rises, especially among small creators?
- How is the Co-CEO structure working, and what has the 2025 leadership change meant for strategy?
- What is the transaction-fee reality?
- Are there any funding, liquidity or IPO plans five years after the 2021 round?
- What has shipped since early 2026? I couldn't confirm.

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

### google/gemini-3.8-flash

Cost: $0.0213

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
* **What they do:** Kajabi is an all-in-one SaaS platform enabling knowledge entrepreneurs to build websites, host courses and communities, offer coaching, send marketing emails, and process payments without code ([yespress.io](https://yespress.io/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).
* **Who buys it:** Mid-market "expert creators"—consultants, niche educators, and coaches; 89% of full-time Kajabi creators have 50,000 or fewer Instagram followers ([yespress.io](https://yespress.io/kajabi)). Kajabi serves over 60,000 creators reaching 70 million users ([yespress.io](https://yespress.io/kajabi)).
* **How they make money:** Flat-rate SaaS subscription tiers (Basic at $179/mo, Growth at $249/mo, Pro at $499/mo) charging **0% transaction fees** on creator GMV ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). Secondary revenue stems from native Kajabi Payments processing (~2.9% + $0.30) ([yespress.io](https://yespress.io/kajabi)), branded mobile app add-ons ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)), and AI usage credits ($15 per 500 credits) ([thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

### 2. Recent News and Launches
* **January 2026 Pricing Overhaul:** Eliminated the low-cost $89/mo Kickstarter tier for new users, increased core subscription pricing across the board, tightened Basic contact limits to 2,500, and moved AI features to a credit model ([thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **Kajabi Evolved & AI Rollout:** Introduced an open API, visual automation builder, and autonomous "Expert Agents" / "Cofounder" tools designed to handle business operations for solopreneurs ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/), [yespress.io](https://yespress.io/kajabi)).
* **Kajabi Capital (December 2025):** Partnered with Parafin to offer embedded working capital financing to eligible U.S. creators directly via dashboard ([askcyborg.com](https://askcyborg.com/company/kajabi)).

### 3. Funding, Size, and Financial Signals
* **Funding & Valuation:** Bootstrapped for nearly a decade before raising a $550 million Series D in May 2021 led by Tiger Global at a $2.0 billion valuation ([yespress.io](https://yespress.io/kajabi), [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). No primary equity rounds have been raised since ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Financials & Scale:** $100M+ ARR ([askcyborg.com](https://askcyborg.com/company/kajabi)); cumulative creator GMV surpassed $10 billion ([yespress.io](https://yespress.io/kajabi)). 
* **Headcount:** ~390 employees ([askcyborg.com](https://askcyborg.com/company/kajabi)), maintaining disciplined, post-hypergrowth operational sizing ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).

### 4. Leadership
Following the departure of CEO Ahad Khan in 2025, co-founder **Kenny Rueter** returned as Co-CEO alongside longtime President **Jonathan Cronstedt** ([yespress.io](https://yespress.io/kajabi)).

### 5. Main Competitors and Differentiation
* **Competitors:** Thinkific, Teachable, Podia, Circle, Mighty Networks, Kit (formerly ConvertKit), and Skool ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Differentiation:** 
  * *No GMV 'tax':* Unlike Teachable or Patreon, Kajabi takes 0% cut of sales, making it much more economical for creators earning over $2,000/month ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).
  * *Consolidated stack:* Rather than stitching together separate tools for community (Circle), email (Kit), and courses (Thinkific), Kajabi provides the entire operating system in one platform ([yespress.io](https://yespress.io/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).

### 6. Likely Strategic Priorities and Open Questions
* **Priorities:** Expand platform ARPU through embedded fintech (Kajabi Capital, Kajabi Payments) and agentic AI tools ([askcyborg.com](https://askcyborg.com/company/kajabi), [yespress.io](https://yespress.io/kajabi)); move upmarket to prioritize high-earning, established creators over hobbyists ([thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500), [askcyborg.com](https://askcyborg.com/company/kajabi)).
* **Open Questions:** 
  * How has customer retention responded to the early-2026 price hikes, tightened contact limits, and sunset of the sub-$100 Kickstarter tier ([thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500))?
  * What is the eventual liquidity path or timeline for Tiger Global/TPG given the peak $2 billion 2021 valuation ([yespress.io](https://yespress.io/kajabi))?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

### 1. What They Do, Who Buys, and Monetization
Kajabi is an all-in-one business platform for “knowledge entrepreneurs”—such as consultants, niche coaches, and course creators—allowing them to build websites, host online courses, run communities, send marketing emails, and manage checkouts without stitching together multiple tools ([yespress.io](https://yespress.io/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)). Its core audience comprises mid-sized solo experts rather than mega-influencers; 89% of its full-time creators have fewer than 50,000 Instagram followers ([yespress.io](https://yespress.io/kajabi)).

Kajabi monetizes primarily via fixed-subscription SaaS tiers (Basic at $179/mo, Growth at $249/mo, Pro at $499/mo) and charges a 0% platform transaction fee on creator sales ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). Secondary revenue stems from branded mobile app add-ons, payment processing via Kajabi Payments (~2.9% + 30¢), and AI usage credits ($15 per 500 credits) ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [yespress.io](https://yespress.io/kajabi), [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

### 2. Recent News & Launches
* **Pricing & Packaging Restructure (Jan 2026):** Retired its low-cost $89/month "Kickstarter" plan for new users, increased monthly prices across all standard tiers (+$30 to +$100/mo), reduced Basic contact caps to 2,500, and moved AI usage to a pay-per-credit model ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **Kajabi Evolved & AI Agents (Late 2025–2026):** Rolled out a platform update with an open API, visual automation builder, and autonomous "Cofounder" AI/Expert Agents acting as digital teammates ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/), [yespress.io](https://yespress.io/kajabi)).
* **Kajabi Capital (Dec 2025):** Partnered with Parafin to launch an embedded lending program offering financing to creators directly within their dashboard ([askcyborg.com](https://askcyborg.com/company/kajabi)).

### 3. Funding, Size, and Financial Signals
* **Valuation & Funding:** Bootstrapped for its first nine years before a 2019 minority check from Spectrum Equity ([yespress.io](https://yespress.io/kajabi)). Last raised a $550 million Series D in May 2021 led by Tiger Global at a $2 billion valuation on roughly $100 million ARR ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)). 
* **Scale:** Serves over 60,000 creators who have collectively processed more than $10 billion in GMV ([yespress.io](https://yespress.io/kajabi)). Headcount is approximately 390 employees ([askcyborg.com](https://askcyborg.com/company/kajabi)).

### 4. Leadership
In 2025, CEO Ahad Khan departed the company ([yespress.io](https://yespress.io/kajabi)). Co-founder Kenny Rueter returned to executive leadership as Co-CEO alongside longtime President Jonathan Cronstedt ([yespress.io](https://yespress.io/kajabi)). 

### 5. Main Competitors & Differentiation
* **Competitors:** Direct rivals include Teachable, Thinkific, and Podia (course/commerce software), Circle and Skool (community-first platforms), and Kit or Patreon (monetization/newsletters) ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Differentiation:** Unlike competitors that take transaction cuts (typically 3%–30%) or focus on a single vertical, Kajabi offers a fully consolidated tech stack for a premium flat subscription, targeting higher-earning, established creators looking to reduce software sprawl ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).

### 6. Likely Strategic Priorities & Open Questions
* **Priorities:** Pushing ARPU higher by shedding entry-tier users, embedding high-margin fintech products (Kajabi Capital/Payments), and integrating AI workflows to reduce creator churn ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500), [askcyborg.com](https://askcyborg.com/company/kajabi)).
* **Questions to Ask:** 
  * How has creator retention responded to the January 2026 pricing hike and contact cap reductions ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500))?
  * What is the early adoption and default rate for Kajabi Capital ([askcyborg.com](https://askcyborg.com/company/kajabi))?
  * What are the co-CEOs' plans regarding liquidity or an eventual IPO following the 2021 funding ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [yespress.io](https://yespress.io/kajabi))?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

### deepseek/deepseek-v4-pro

Cost: $0.0157

#### Run 1

**1. What they do, who buys it, and how they make money**  
Kajabi is an all-in-one SaaS platform for knowledge entrepreneurs: websites, courses, coaching, memberships/communities, podcasts, digital downloads, email, funnels, and payments. Its core buyer is the mid-sized expert, not mega-influencers; Kajabi says 89% of full-time creators have 50,000 or fewer Instagram followers, and it reports 60,000+ creators reaching ~70 million people and ~85 million cumulative buyers [yespress.io](https://yespress.io/kajabi). Revenue is subscription-first: current tiers are Basic $179/month, Growth $249/month, Pro $499/month, with annual discounts [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500). Kajabi takes 0% revenue share on creator sales, but native Kajabi Payments charges ~2.9% + $0.30 if creators don’t use their own Stripe/PayPal [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi) [yespress.io](https://yespress.io/kajabi). A branded mobile app is an add-on [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi).

**2. Recent news and launches (last 6 months)**  
Late 2025/early 2026 brought “Kajabi Evolved”: visual automation, checkout customization, affiliate tools, community changes, mobile updates, and an open API [theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/). Its AI push includes Cofounder and Expert Agents, framed as AI teammates for one-person businesses [yespress.io](https://yespress.io/kajabi). In December 2025, Kajabi launched Kajabi Capital with Parafin for embedded creator financing [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi) [askcyborg.com](https://askcyborg.com/company/kajabi). In January 2026, it removed the Kickstarter entry plan, raised prices, cut Basic contacts from 10,000 to 2,500, and made Basic include zero AI credits while others pay $15 per 500 [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500).

**3. Funding, size, and financial signals**  
Founded 2010, Irvine HQ, ~391 employees, reported $100M+ revenue [askcyborg.com](https://askcyborg.com/company/kajabi). It bootstrapped profitably for years; Spectrum Equity took a minority stake in 2019, then a $550 million growth round in May 2021 led by Tiger Global with TPG, Tidemark, Owl Rock, Meritech, and Spectrum valued it at over $2 billion [yespress.io](https://yespress.io/kajabi). No primary funding has been disclosed since [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi). Cumulative creator sales have passed $10 billion [yespress.io](https://yespress.io/kajabi).

**4. Leadership**  
Ahad Khan, CEO from 2021, departed in 2025. Co-founder Kenny Rueter returned as Co-CEO alongside longtime president Jonathan Cronstedt [yespress.io](https://yespress.io/kajabi).

**5. Main competitors and how they differ**  
Direct peers include Thinkific, Patreon, Podia, Kit/ConvertKit, Mighty Networks, Teachable, and Circle; emerging players include Skool and Substack, with Shopify as a broad incumbent [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi). Kajabi differentiates by consolidating course, community, email, funnels, and payments into one subscription with 0% platform revenue share, versus transaction-based models like Patreon or Teachable. Thinkific is the closest all-in-one rival; Podia pressures on price [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi). Other listed competitors include Hotmart, HoneyBook, and ClickFunnels [askcyborg.com](https://askcyborg.com/company/kajabi).

**6

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

**1. What they do, who buys it, and how they make money**  
Kajabi is an all-in-one SaaS platform that lets knowledge entrepreneurs build a branded website, sell online courses, run membership communities, coach, host podcasts, send emails, and process payments — all without code. The core user is the mid‑scale expert: 89% of full‑time creators have fewer than 50,000 Instagram followers, and the platform supports over 60,000 creators who have collectively sold to ~85 million buyers [yespress.io](https://yespress.io/kajabi).  
Revenue comes primarily from tiered subscriptions (Basic $179/mo, Growth $249/mo, Pro $499/mo) and an optional branded mobile‑app add‑on. Kajabi takes 0% of creators’ sales revenue, a deliberate differentiator; it only charges a standard processing fee (2.9% + 30¢) when users adopt its native Kajabi Payments instead of Stripe or PayPal [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)[yespress.io](https://yespress.io/kajabi)[thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500).

**2. Recent news and launches (last 6 months)**  
In early 2026 Kajabi rolled out the “Evolved” platform update, including AI Cofounder and domain‑trained Expert Agents designed to slash content‑creation time, a visual automation builder, and an open API for custom integrations [theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/). In January 2026 it restructured pricing: the entry Kickstarter tier was removed, prices rose $30‑$100/mo across plans, and the Basic plan’s contact limit dropped from10,000 to2,500. AI credits were monetised at $15 per500 for non‑Kickstarter customers [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500). In late2025, Kajabi Capital launched with Parafin, offering embedded financing to U.S. creators directly from the dashboard [askcyborg.com](https://askcyborg.com/company/kajabi).

**3. Funding, size, and financial signals**  
After bootstrapping profitably for a decade, Kajabi raised a $550M Series D in May2021 led by Tiger Global at a $2B+ valuation. No primary round has followed [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)[yespress.io](https://yespress.io/kajabi). Revenue is an estimated $100M+ ARR, with roughly391 employees [askcyborg.com](https://askcyborg.com/company/kajabi). Cumulatively, creators have crossed $10B in platform sales [yespress.io](https://yespress.io/kajabi). The absence of new funding, stable headcount (251‑500 range), and recent price hikes suggest a mature, cash‑generating company optimising unit economics.

**4. Leadership**  
Co‑founder Kenny Rueter returned as Co‑CEO alongside longime president Jonathan Cronstedt in 2025, after previous CEO Ahad Khan departed. This brought founder‑led leadership back to the top [yespress.io](https://yespress.io/kajabi).

**5. Main competitors and how they differ**  
Direct rivals: Thinkific (all‑in‑one course platform; Kajabi publishes migration guides), Teachable (historically charges transaction fees, Kajabi charges 0%), Podia (lower‑priced starter tier), Patreon, Kit (formerly ConvertKit), Mighty Networks, and Circle [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi). Emerging threats include Skool and Substack; Shopify is a broad incumbent. Kajabi differentiates by consolidating a full business suite in one subscription without revenue‑share, and now by embedding AI and fintech.

**6. Likely strategic priorities and open questions**  
Priorities: monetise AI (Cofounder, agents) to justify higher tiers; lift ARPU through price increases and add‑ons like Kajabi Capital; open the API to attract larger businesses; and defend against low‑cost alternatives.  
Open questions: Will the price hikes churn the small‑creator base? Can the AI‑credits model gain acceptance? Is a new funding round or exit on the horizon after years without primary capital? And will founder‑led management accelerate product velocity or slow decisions?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)
