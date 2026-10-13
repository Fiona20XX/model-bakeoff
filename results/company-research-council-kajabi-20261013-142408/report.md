# Council: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-13T14:24:08
- Variables: `company=Kajabi`
- Judge: `openai/gpt-6-sol`
- Synthesizer: `x-ai/grok-4.7`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.4144 (contestants $0.1404, synthesis $0.1499, judge $0.0935, synthesis guess $0.0305)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent | Synthesis % | Why (judge's guess) |
|---|---|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 8.0 (7.9–8.1) | $0.0390 | 18.9s (18.2s–19.5s) | 5 (5–5) | 6 (5–7) | 2.0 | 4% | Its broad competitor list and explicit fee-source conflict suggest synthesis, but it keeps a distinct October 2026 framing and says it found no news within that six-month window. |
| council (x-ai/grok-4.7) | 7.7 (7.7–7.7) | $0.1452 | 108.7s (105.6s–111.8s) | 5 (5–5) | 4 (4–5) | 0.5 | 94% | It combines both the 70-million reach and 85-million buyer figures, the conflicting fee descriptions, and unusually many launch and competitor details into one account. |
| deepseek/deepseek-v4-pro | 6.4 (6.1–6.8) | $0.0111 | 20.0s (18.1s–21.8s) | 5 (5–5) | 5 (4–6) | 5.8 | 1% | A focused account of Kajabi’s pricing, launches and strategy; it does not show the overlapping figures and qualifications characteristic of a merge. |
| google/gemini-3.8-flash | 5.8 (5.8–6.0) | $0.0201 | 25.8s (25.8s–25.9s) | 5 (5–5) | 6 (6–7) | 2.9 | 1% | It presents a comparatively streamlined account of the platform, funding and competitors, without combining competing scale figures. |

The council row is the synthesizer's merge of the other answers. Its cost includes every contestant call plus the synthesis; its latency is the slowest contestant plus the synthesis. "Synthesis %" is the judge's guess, in a separate call after scoring, that the row is the merged answer (chance is 25% with 4 answers).

## Judge rationales

- **anthropic/claude-sonnet-5.5**: It is specific and unusually clear that its sources lack news from the requested six-month window, but several funding, leadership, competitor, and product details cannot be checked against the supplied excerpts.
- **council (x-ai/grok-4.7)**: It gives a practical briefing and acknowledges the absence of launches dated after January 2026, although some specific financial, leadership, fee, and competitor claims exceed the supplied excerpts.
- **deepseek/deepseek-v4-pro**: The briefing has useful concrete details, but it presents items dated no later than early 2026 as last-six-month news without addressing that gap, and several prominent financial and leadership claims lack excerpt support.
- **google/gemini-3.8-flash**: The structure and questions are useful, but it neither flags the lack of news within the requested six-month window nor adequately supports several prominent metrics and comparisons.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpts do not substantiate the stated 13 October 2026 as-of date.
- **anthropic/claude-sonnet-5.5** (run 1): The Kajabi Payments fee of approximately 2.9% plus 30¢ is not visible in the cited excerpt; the claimed conflict with a 0% platform fee is not established.
- **anthropic/claude-sonnet-5.5** (run 1): The excerpts do not substantiate a 2019 Spectrum Equity investment, a Tiger Global-led round, or a valuation above $2 billion rather than approximately $2 billion.
- **anthropic/claude-sonnet-5.5** (run 1): The estimate of 391 employees and the $10 billion cumulative creator-sales figure are not in the provided excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): Ahad Khan’s departure and the appointments of Kenny Rueter and Jonathan Cronstedt are not substantiated by the provided excerpts.
- **anthropic/claude-sonnet-5.5** (run 1): The excerpts do not substantiate the specific competitor comparisons involving Teachable’s fees, Podia’s price, Kit, Mighty Networks, Circle, Skool, or Substack.
- **anthropic/claude-sonnet-5.5** (run 1): Creator Studio’s 2024 launch and Adobe involvement are not in the provided excerpts.
- **council (x-ai/grok-4.7)** (run 1): The approximately 2.9% plus 30¢ Kajabi Payments fee is not visible in the cited excerpt; its supposed conflict with a 0% platform fee is not established.
- **council (x-ai/grok-4.7)** (run 1): The excerpts do not substantiate a Tiger Global-led round, a valuation above $2 billion rather than approximately $2 billion, or a decade of bootstrapping.
- **council (x-ai/grok-4.7)** (run 1): The estimate of approximately 391 employees and the $10 billion cumulative creator-sales figure are not in the provided excerpts.
- **council (x-ai/grok-4.7)** (run 1): Ahad Khan’s departure and the appointments of Kenny Rueter and Jonathan Cronstedt are not substantiated by the provided excerpts.
- **council (x-ai/grok-4.7)** (run 1): The excerpts do not establish that Kajabi Evolved added Cofounder and Expert Agents specifically, or that Podia and Skool compete on price.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not substantiate a Tiger Global-led round, a valuation above $2 billion rather than approximately $2 billion, or roughly a decade without venture funding.
- **deepseek/deepseek-v4-pro** (run 1): The provided excerpts support a $100M+ revenue estimate, not $100M+ ARR; they do not show approximately 391 employees or an Irvine headquarters.
- **deepseek/deepseek-v4-pro** (run 1): The $10 billion cumulative creator-sales figure is not in the provided excerpts.
- **deepseek/deepseek-v4-pro** (run 1): Ahad Khan’s departure and the appointments of Kenny Rueter and Jonathan Cronstedt are not substantiated by the provided excerpts.
- **deepseek/deepseek-v4-pro** (run 1): The specific comparisons involving Teachable’s or Patreon’s revenue share, Podia’s price, and Circle’s and Mighty Networks’ positioning are not established by the provided excerpts.
- **deepseek/deepseek-v4-pro** (run 1): Shopify’s status as a competitor is not shown in the provided excerpts.
- **google/gemini-3.8-flash** (run 1): The approximately 2.9% plus 30¢ Kajabi Payments fee is not visible in the cited excerpt.
- **google/gemini-3.8-flash** (run 1): The excerpts do not establish that Kajabi Evolved introduced Cofounder, Expert Agents, and MCP together, or that these products act as automated operational teammates.
- **google/gemini-3.8-flash** (run 1): The provided excerpt describes Kajabi Capital as financing, not specifically working-capital loans.
- **google/gemini-3.8-flash** (run 1): The excerpts do not substantiate a Tiger Global-led round, a valuation above $2 billion rather than approximately $2 billion, or nearly a decade of bootstrapping.
- **google/gemini-3.8-flash** (run 1): The provided excerpts support a $100M+ revenue estimate, not $100M+ ARR; they do not establish that all 60,000 creators are active, the $10 billion GMV figure, or a 350–500 employee range.
- **google/gemini-3.8-flash** (run 1): Ahad Khan’s departure and the appointments of Kenny Rueter and Jonathan Cronstedt are not substantiated by the provided excerpts.
- **google/gemini-3.8-flash** (run 1): The excerpts do not establish the specific competitor comparisons involving Teachable’s revenue share, Circle’s and Mighty Networks’ relative community strength, or Podia’s and Skool’s prices and positioning.
- **anthropic/claude-sonnet-5.5** (run 2): The excerpts do not substantiate the 2019 Spectrum Equity investment, Tiger Global’s role in the 2021 round, or a valuation above $2 billion rather than approximately $2 billion.
- **anthropic/claude-sonnet-5.5** (run 2): The cited excerpts do not substantiate the estimate of 391 employees, cumulative creator sales above $10 billion, or the named leadership changes.
- **anthropic/claude-sonnet-5.5** (run 2): The provided excerpts do not substantiate the specific Kajabi Payments processing rate, Podia’s cheaper entry tier, or Teachable’s historical fees.
- **anthropic/claude-sonnet-5.5** (run 2): The provided excerpts do not identify several listed competitors or support the Creator Studio–Adobe connection.
- **anthropic/claude-sonnet-5.5** (run 2): The unqualified statement that existing customers received no grandfathering overlooks the excerpt’s exception for existing Kickstarter accounts.
- **council (x-ai/grok-4.7)** (run 2): The excerpts do not substantiate the 2019 Spectrum Equity minority stake, Tiger Global’s role in the 2021 round, or the estimate of 391 employees.
- **council (x-ai/grok-4.7)** (run 2): The provided excerpts do not substantiate cumulative creator sales above $10 billion or the named leadership changes.
- **council (x-ai/grok-4.7)** (run 2): The supplied excerpts do not establish the specific Kajabi Payments processing rate or identify several of the listed competitors.
- **council (x-ai/grok-4.7)** (run 2): The unqualified claim of no grandfathering overlooks the exception for existing Kickstarter accounts.
- **deepseek/deepseek-v4-pro** (run 2): The excerpts do not substantiate profitable growth for a decade, the 2019 Spectrum Equity investment, Tiger Global’s role in the 2021 round, or a valuation exceeding $2 billion.
- **deepseek/deepseek-v4-pro** (run 2): The provided excerpts do not establish Kajabi Payments as an additional revenue source, the estimate of 391 employees, or cumulative sales above $10 billion.
- **deepseek/deepseek-v4-pro** (run 2): The named 2025 leadership transition is absent from the supplied excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The supplied excerpts do not identify all the listed competitors or establish Teachable’s historical fees.
- **google/gemini-3.8-flash** (run 2): The excerpts do not establish that Kajabi earns revenue from payment processing or substantiate the stated processing rate.
- **google/gemini-3.8-flash** (run 2): The provided excerpts do not substantiate the 2019 minority round, Tiger Global’s role in the 2021 round, cumulative GMV above $10 billion, or approximately 390 employees.
- **google/gemini-3.8-flash** (run 2): The $100M+ figure appears as revenue in a source title, not as the asserted ARR figure.
- **google/gemini-3.8-flash** (run 2): The named leadership transition is absent from the supplied excerpts.
- **google/gemini-3.8-flash** (run 2): The excerpts do not support the $1,000–$2,000 monthly earnings threshold or the characterization of Skool and Circle as highly viral.
- **google/gemini-3.8-flash** (run 2): Calling the Kickstarter plan discontinued without limiting that statement to new customers omits the excerpt’s exception for existing accounts.

## Where the models disagreed (run 1)

- Platform fees: two answers, citing akta.pro, say Kajabi charges 0% transaction fees on creator sales; one of those and the third, citing YesPress, also describe Kajabi Payments at about 2.9% + 30¢ if Stripe or PayPal is not used.
- Older vs current pricing: YesPress describes a Kickstarter tier around $55/mo and Pro around $319; The Course Times says Kickstarter was $89/mo and, after January 2026, Pro is $499/mo.
- Headcount: one answer says about 350–500, another about 391, and akta.pro says 251–500.
- Recency: two answers treat January 2026 and late 2025 items as the recent-news section; the third says nothing in the sources is dated in the six months before 13 Oct 2026.
- Pre-2021 capital: one answer says Spectrum Equity invested in 2019 and that the company was profitable while bootstrapped; the other two say it was bootstrapped until the 2021 Tiger round and do not mention Spectrum or profitability.
- Competitor lists differ: shared names are Thinkific, Teachable, Podia, Circle, Mighty Networks, and Patreon; one adds Skool, another Shopify, another Kit and Substack, and AskCyborg adds Hotmart, HoneyBook, and ClickFunnels.
- Only one answer states headquarters in Irvine, CA, and only one mentions a 2024 Creator Studio built with Adobe; the others do not.

## Where the models disagreed (run 2)

- Transaction fees: some accounts treat 0% of creator GMV as the model (akta.pro) and separately cite Kajabi Payments at about 2.9% + $0.30 (YesPress); another treats the two figures as an unresolved conflict rather than platform cut versus processing.
- List prices: YesPress still describes an entry Kickstarter tier around $55 and Pro around $319; The Course Times gives January 2026 prices of Basic $179, Growth $249, and Pro $499, with the $89 Kickstarter plan removed for new customers. The dated Course Times figures were used.
- Valuation wording: YesPress says over/exceeding $2 billion; akta.pro says approximately $2 billion.
- Headcount: akta.pro gives 251–500; AskCyborg estimates about 391 (another account about 390). The point estimate sits inside the range.
- Recency: two accounts present December 2025–January 2026 items as the recent-news set; a third, dated 2026-10-13, says nothing fell in the prior six months and flags a gap after early 2026.
- Scale wording: one account says over $10 billion cumulative GMV; others say cumulative creator sales passed $10 billion.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0390

#### Run 1

# Kajabi Briefing (as of 13 Oct 2026)

## 1. What they do, who buys it, how they make money
Kajabi is an all-in-one platform for experts to build sites, courses, coaching, memberships, podcasts, email, funnels and payments without code ([yespress.io](https://yespress.io/kajabi)). Customers skew mid-sized: 89% of full-time creators have 50,000 or fewer Instagram followers. Kajabi reports 60,000+ creators and roughly 85 million buyers served ([yespress.io](https://yespress.io/kajabi)).

Revenue is mainly subscriptions, plus an optional branded mobile app add-on ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). After the January 2026 repricing, Basic is $179/month, Growth $249 and Pro $499 (monthly billing) ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

**Source conflict:** One source says Kajabi takes 0% of creator revenue ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Another says Kajabi Payments carries an optional fee of about 2.9% + 30¢ if you don't use Stripe or PayPal ([yespress.io](https://yespress.io/kajabi)). Confirm which applies.

## 2. Recent news and launches
I found nothing dated within the last six months (April–October 2026). The most recent items in my sources are:
- **Jan 2026:** Kickstarter plan removed for new customers, with price increases of +$30 (Basic), +$50 (Growth) and +$100 (Pro). Basic's contact limit fell from 10,000 to 2,500. Existing customers got no grandfathering. AI features now run on credits, and the cheapest tier gets none ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **Late 2025–early 2026:** "Kajabi Evolved" added a visual automation builder, checkout customization, affiliate tools and community changes ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)).
- **Dec 2025:** Kajabi Capital, embedded financing with Parafin for eligible U.S. creators ([askcyborg.com](https://askcyborg.com/company/kajabi)).

## 3. Funding, size, financial signals
- Bootstrapped and profitable for about a decade. Spectrum Equity invested in 2019, then a $550M round led by Tiger Global in May 2021 valued it at over $2B ([yespress.io](https://yespress.io/kajabi)).
- No primary round disclosed since. Headcount is 251–500 ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)), with one estimate of 391 employees and $100M+ revenue ([askcyborg.com](https://askcyborg.com/company/kajabi)). These are third-party estimates, not audited figures.
- Cumulative creator sales passed $10B ([yespress.io](https://yespress.io/kajabi)).
- The price hikes suggest a push on monetization and margin. That is my inference, not a stated reason.

## 4. Leadership
CEO Ahad Khan (since 2021) left in 2025. Co-founder Kenny Rueter returned as Co-CEO alongside longtime president Jonathan Cronstedt ([yespress.io](https://yespress.io/kajabi)). I found no other executive details.

## 5. Competitors
- **Thinkific, Teachable:** closest course-platform rivals. Teachable historically charged transaction fees.
- **Podia:** cheaper entry tier pressures Kajabi's higher price point.
- **Kit (ConvertKit):** email-first, adding commerce.
- **Mighty Networks, Circle:** community-first, expanding into courses.
- **Patreon:** membership monetization. Kajabi publishes migration content aimed at it.
- Emerging: Skool and Substack ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Another source also lists Hotmart, HoneyBook and ClickFunnels ([askcyborg.com](https://askcyborg.com/company/kajabi)).

Kajabi's differentiator is breadth and a flat subscription aimed at established creators, rather than a revenue share.

## 6. Likely priorities and open questions
**Priorities (inferred):**
- AI as a product and revenue lever. Creator Studio (2024, built with Adobe), Cofounder and Expert Agents ([yespress.io](https://yespress.io/kajabi)).
- Moving upmarket and expanding into fintech.

**Questions to ask:**
- How has churn held up after the January repricing, especially among small creators?
- Does the AI credit gating drive upgrades or push users to Podia and similar?
- What is the Co-CEO division of responsibilities?
- Is there any plan for new capital or an exit, given the 2021 investors?
- What is the actual transaction fee structure?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

# Kajabi Briefing (as of 2026-10-13)

## 1. What they do, who buys it, how they make money
Kajabi is an all-in-one platform where experts build a website, courses, coaching, memberships and communities, podcasts, email and funnels, and take payment without code ([yespress.io](https://yespress.io/kajabi)). It targets mid-sized experts, not mega-influencers: 89% of full-time creators have 50,000 or fewer Instagram followers. It reports 60,000+ creators ([yespress.io](https://yespress.io/kajabi)).

Revenue is mainly tiered subscriptions plus an optional branded mobile app add-on ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Current list prices are Basic $179/mo, Growth $249 and Pro $499 ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). **Sources conflict on fees:** one says 0% transaction fees ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)), while another says Kajabi Payments adds an optional ~2.9% + 30¢ ([yespress.io](https://yespress.io/kajabi)). Confirm this directly.

## 2. Recent news and launches
I found nothing dated within the last six months (April–October 2026). The most recent items I found are:
- **Jan 2026:** Pricing overhaul. The $89 Kickstarter plan was removed for new customers, Basic rose $30, Growth $50 and Pro $100, and Basic's contact limit fell from 10,000 to 2,500. Existing customers got no grandfathering ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **AI credits:** Basic gets none, while Cofounder chat and MCP are on every plan ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **Late 2025–early 2026:** "Kajabi Evolved" added a visual automation builder, checkout customization, affiliate tools and community changes ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)).
- **Dec 2025:** Kajabi Capital, embedded financing with Parafin for eligible U.S. creators ([askcyborg.com](https://askcyborg.com/company/kajabi)).

## 3. Funding, size, financial signals
- The company was bootstrapped for about a decade. Spectrum Equity invested in 2019, then a $550M round led by Tiger Global in May 2021 valued it at over $2B ([yespress.io](https://yespress.io/kajabi)).
- No new primary round has been disclosed since; headcount is 251–500 ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)), with one estimate of 391 ([askcyborg.com](https://askcyborg.com/company/kajabi)).
- Revenue is estimated at $100M+ ([askcyborg.com](https://askcyborg.com/company/kajabi)), a third-party figure that is not audited.
- Cumulative creator sales passed $10B ([yespress.io](https://yespress.io/kajabi)).
- The price rises and AI credit gating suggest a push on monetization and margin. This is my inference, not a stated company aim.

## 4. Leadership
Co-founder Kenny Rueter and longtime president Jonathan Cronstedt are Co-CEOs. Ahad Khan, CEO since 2021, left in 2025 ([yespress.io](https://yespress.io/kajabi)). I did not find other executives.

## 5. Competitors
- **Thinkific, Teachable:** Closest course-platform rivals. Teachable historically charged transaction fees ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- **Podia:** Cheaper entry tier, which pressures Kajabi's higher entry price ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- **Kit (ConvertKit), Circle, Mighty Networks, Patreon:** Email-, community- or membership-first, overlapping Kajabi's bundle ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- **Skool, Substack:** Emerging players ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
- **Hotmart, HoneyBook, ClickFunnels:** Also named ([askcyborg.com](https://askcyborg.com/company/kajabi)).

Kajabi's pitch is consolidation and flat pricing aimed at established creators.

## 6. Likely priorities and open questions
**Priorities (inferred):** AI-led product (Cofounder, Expert Agents, Creator Studio, the last built with Adobe) ([yespress.io](https://yespress.io/kajabi)), fintech expansion, and higher revenue per customer.

**Open questions:**
- How did the January price rises affect churn, especially among small creators?
- What is the actual transaction-fee policy?
- What is the co-CEO split of responsibilities?
- Is a new funding round, or an exit, planned given the 2021 valuation?
- What has launched since early 2026? My sources have a gap.

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

### council (x-ai/grok-4.7)

Cost: $0.1452

#### Run 1

## 1. What they do, who buys it, and how they make money
Kajabi is an all-in-one platform for knowledge entrepreneurs—coaches, consultants, and course creators—to build sites, sell courses, run communities, deliver coaching, host podcasts, send email, build funnels, and take payment without code ([YesPress](https://yespress.io/kajabi)). Buyers are mid-sized experts: 89% of full-time creators have 50,000 or fewer Instagram followers. It reports 60,000+ creators reaching about 70 million people, with sales to roughly 85 million buyers ([YesPress](https://yespress.io/kajabi)).

Revenue is mainly subscriptions. After January 2026, monthly prices are Basic $179, Growth $249, and Pro $499 (annual $143 / $199 / $399) ([The Course Times](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). It markets 0% platform fees on creator sales ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Another account puts native Kajabi Payments at about 2.9% + 30¢ if Stripe or PayPal is not used ([YesPress](https://yespress.io/kajabi)); those fee claims conflict—confirm which applies. Also: a branded-app add-on ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)) and AI credits at $15 per 500 ([The Course Times](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

## 2. Recent news and launches (last 6 months)
No source here dates a launch after January 2026.
- **January 2026:** The $89/mo Kickstarter plan was removed for new customers (existing accounts kept it). Prices rose $30, $50, and $100. Basic contacts fell from 10,000 to 2,500. Credit-based AI is off Basic; Cofounder and MCP stay on every plan ([The Course Times](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **Late 2025–early 2026:** Kajabi Evolved added a visual automation builder, checkout and affiliate tools, community and mobile updates, plus Cofounder and Expert Agents ([TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)).
- **December 2025:** Kajabi Capital with Parafin offers embedded financing to eligible U.S. creators ([AskCyborg](https://askcyborg.com/company/kajabi)).

## 3. Funding, size, and financial signals
Bootstrapped for about a decade, then a $550 million Series D led by Tiger Global in May 2021 at above a $2 billion valuation. No primary round disclosed since ([YesPress](https://yespress.io/kajabi); [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Third-party estimates, not audited filings: $100M+ revenue and about 391 employees, with headcount also given as 251–500 ([AskCyborg](https://askcyborg.com/company/kajabi); [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Cumulative creator sales are described as past $10 billion ([YesPress](https://yespress.io/kajabi)).

## 4. Leadership
In 2025, CEO Ahad Khan left. Co-founder Kenny Rueter returned as Co-CEO with longtime president Jonathan Cronstedt ([YesPress](https://yespress.io/kajabi)). No other current executives were identified in these sources.

## 5. Main competitors and how they differ
Thinkific and Teachable are the closest course-platform rivals; Kajabi sells a broader suite and publishes Thinkific migration guides ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Podia and Skool compete on price. Circle and Mighty Networks are community-first. Patreon is membership-led ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Also named: Hotmart, HoneyBook, and ClickFunnels ([AskCyborg](https://askcyborg.com/company/kajabi)).

## 6. Likely strategic priorities and open questions
Likely priorities: AI credits and agents as an upgrade lever, creator fintech via payments and Kajabi Capital, and a higher price floor. Ask about post-January churn and acquisition, whether credit gates upgrade or lose small creators, Capital repayment, the Co-CEO split, and any liquidity path for 2021 investors.

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

## 1. What they do, who buys it, and how they make money
Kajabi is an all-in-one platform for knowledge entrepreneurs: websites, courses, coaching, memberships, podcasts, email, funnels, and checkout, without code ([YesPress](https://yespress.io/kajabi)). Buyers are mid-sized experts, not mega-influencers—89% of full-time creators have 50,000 or fewer Instagram followers. It reports 60,000+ creators ([YesPress](https://yespress.io/kajabi)).

Revenue is mainly tiered subscriptions. After a January 2026 change, list prices are Basic $179/month, Growth $249, and Pro $499 ([The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). A branded mobile app is an optional add-on ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). **Fees conflict:** akta.pro says Kajabi takes 0% of creator GMV ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)); Kajabi Payments is also described as charging about 2.9% + $0.30 ([YesPress](https://yespress.io/kajabi)). Credit-gated AI is $15 per 500 credits ([The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).

## 2. Recent news and launches
These sources’ newest items are late 2025 through early 2026; nothing later was found.
- **January 2026:** The $89 Kickstarter plan was removed for new customers. Basic rose $30, Growth $50, and Pro $100; Basic contacts fell from 10,000 to 2,500, with no grandfathering ([The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- Basic gets zero AI credits; Cofounder chat and MCP stay on every plan ([The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
- **Kajabi Evolved** added a visual automation builder, checkout customization, affiliate tools, community changes, and a more connected mobile experience, alongside AI branded as Cofounder and Expert Agents ([TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)).
- **December 2025:** Kajabi Capital with Parafin, embedded financing for eligible U.S. creators ([AskCyborg](https://askcyborg.com/company/kajabi)).

## 3. Funding, size, and financial signals
Kajabi bootstrapped for about a decade, took a 2019 Spectrum Equity minority stake, then raised $550 million in May 2021 led by Tiger Global at about $2 billion ([YesPress](https://yespress.io/kajabi); [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). No later primary round is disclosed ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)). Headcount is 251–500, with one estimate near 391 ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi); [AskCyborg](https://askcyborg.com/company/kajabi)). Revenue is a third-party $100M+ estimate, not audited ([AskCyborg](https://askcyborg.com/company/kajabi)). Cumulative creator sales are reported above $10 billion ([YesPress](https://yespress.io/kajabi)).

## 4. Leadership
Co-founder Kenny Rueter returned with longtime president Jonathan Cronstedt as Co-CEOs after Ahad Khan, CEO since 2021, left in 2025 ([YesPress](https://yespress.io/kajabi)). Other executives were not found.

## 5. Main competitors and how they differ
Named rivals include Thinkific (closest all-in-one), Teachable, Podia, Circle, Skool, Mighty Networks, Patreon, and Kit/ConvertKit ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)), plus Hotmart, HoneyBook, and ClickFunnels ([AskCyborg](https://askcyborg.com/company/kajabi)). Kajabi’s pitch is a subscription bundle and a stated 0% platform cut, versus fee-taking course tools or separate funnel, email, and community products ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi); [YesPress](https://yespress.io/kajabi)).

## 6. Likely strategic priorities and open questions
Priorities look like AI teammates, creator fintech, and higher revenue per account. Open questions: churn after the January increases; whether “0% fees” excludes card processing; the co-CEO split; and any new round or exit after the 2021 valuation. Post–early-2026 launches were not in these sources.

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

### deepseek/deepseek-v4-pro

Cost: $0.0111

#### Run 1

**1. What they do, who buys it, and how they make money**
Kajabi is an all-in-one SaaS platform for knowledge entrepreneurs to build websites, sell courses, run memberships/communities, deliver coaching, host podcasts, send email, and process payments without code [yespress.io](https://yespress.io/kajabi). Its core customer is the mid-sized expert—consultants, coaches, course authors—not mega-influencers; 89% of full-time creators have under 50,000 Instagram followers. Kajabi serves 60,000+ creators reaching ~70 million people [yespress.io](https://yespress.io/kajabi). Revenue is subscription-based (Basic $179/mo, Growth $249/mo, Pro $499/mo monthly billing), with 0% platform transaction fees as a differentiator, plus an optional branded mobile app add-on [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500).

**2. Recent news and launches (last 6 months)**
In late 2025/early 2026, Kajabi rolled out “Kajabi Evolved,” including a visual automation builder, stronger checkout customization, affiliate tools, and community updates [theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/). In December 2025, it launched **Kajabi Capital** with Parafin, offering embedded financing to eligible U.S. creators [askcyborg.com](https://askcyborg.com/company/kajabi). In January 2026, it restructured pricing: the Kickstarter entry plan was removed for new customers, prices rose $30–$100/mo across tiers, and Basic's contact limit dropped from 10,000 to 2,500. AI features now run on credits; Basic includes zero credits, while other tiers pay $15 per 500 [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500).

**3. Funding, size, and financial signals**
Kajabi took no venture money for roughly a decade, then raised a $550M Series D in May 2021 led by Tiger Global at a $2B+ valuation [yespress.io](https://yespress.io/kajabi). Revenue is reported at $100M+ ARR, with ~391 employees and headquarters in Irvine, CA [askcyborg.com](https://askcyborg.com/company/kajabi). Cumulative creator sales have passed $10B [yespress.io](https://yespress.io/kajabi). No primary funding round has been disclosed since 2021, suggesting a post-hyper-growth, profitability-focused operating profile [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi).

**4. Leadership**
Co-founder Kenny Rueter and longtime president Jonathan Cronstedt stepped in as Co-CEOs in 2025, replacing Ahad Khan, who had led since 2021 [yespress.io](https://yespress.io/kajabi).

**5. Main competitors and how they differ**
Direct competitors include Thinkific, Teachable, Podia, Mighty Networks, Circle, and Patreon. Kajabi differentiates via its all-in-one consolidation, 0% transaction fees (vs. Teachable/Patreon's revenue share), and now embedded fintech. Podia pressures on price; Circle/Mighty compete on community-first positioning [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi). Shopify is a broad incumbent [akta.pro](https://akta.pro/company-profiles/00004mf/kajabi).

**6. Likely strategic priorities and open questions**
Priorities: expanding AI (Cofounder, Expert Agents, MCP) as a retention lever; monetizing via AI credits; scaling Kajabi Capital into creator fintech; and moving upmarket with higher-priced tiers. Open questions: Will the January 2026 price hikes and removal of the entry plan slow new-creator acquisition? Can AI credits become a meaningful revenue line without alienating users? How will returning co-founders balance profitability with growth after the Tiger-era expansion?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

Here is a briefing on Kajabi.

**1. What they do, who buys it, and how they make money**
Kajabi is an all-in-one business platform for knowledge creators, allowing them to build websites, sell online courses, run coaching, host communities, send marketing emails, and process payments without code [yespress.io]. The core customer is not a mega-influencer but a mid-sized expert—89% of full-time creators on the platform have 50,000 or fewer Instagram followers [yespress.io]. The company reports serving over 60,000 creators [yespress.io]. Kajabi makes money primarily through SaaS subscriptions, charging 0% transaction fees on creator revenue, a key differentiator from platforms that take a percentage cut [akta.pro]. As of January 2026, pricing tiers are Basic ($179/mo), Growth ($249/mo), and Pro ($499/mo) [thecoursetimes.com]. Additional revenue comes from a branded mobile app add-on and Kajabi Payments, its native checkout [akta.pro][yespress.io].

**2. Recent news and launches (last 6 months)**
Kajabi has undergone significant platform and pricing shifts. In late 2025 and early 2026, it rolled out “Kajabi Evolved,” featuring a visual automation builder, enhanced checkout, and a more connected mobile experience [theeduassist.com]. In December 2025, it launched **Kajabi Capital** with Parafin, offering embedded financing to eligible U.S. creators directly from the dashboard [askcyborg.com]. In January 2026, a major pricing restructure took effect: the entry-level Kickstarter plan was removed for new customers, prices rose by $30-$100/mo across tiers, and the Basic plan’s contact limit was cut from 10,000 to 2,500 [thecoursetimes.com]. AI features are now largely credit-gated, with Basic plans receiving zero AI credits and other tiers paying $15 per 500 credits [thecoursetimes.com].

**3. Funding, size, and financial signals**
Kajabi grew profitably for a decade before taking a minority investment from Spectrum Equity in 2019 [yespress.io]. In May 2021, it raised a $550M Series D led by Tiger Global at a valuation exceeding $2 billion [yespress.io]. No primary funding rounds have been disclosed since [akta.pro]. The company’s headcount is estimated at 391, with revenue around $100M+ [askcyborg.com]. Cumulative sales on the platform have passed $10 billion [yespress.io].

**4. Leadership**
Co-founder Kenny Rueter returned as Co-CEO in 2025 alongside longtime president Jonathan Cronstedt, following the departure of Ahad Khan, who had led the company since 2021 [yespress.io].

**5. Main competitors and how they differ**
Direct competitors include Thinkific, Teachable, Podia, and Mighty Networks [akta.pro]. Kajabi’s primary differentiator is its 0% transaction fee model, contrasting with platforms like Teachable that historically charged fees [akta.pro]. It also competes with membership platform Patreon and email-commerce tool Kit (formerly ConvertKit), positioning itself as a consolidated “operating system” that replaces a patchwork of separate tools [akta.pro][yespress.io].

**6. Likely strategic priorities and open questions**
Kajabi is prioritizing AI integration, framing tools like “Cofounder” and “Expert Agents” as AI teammates to absorb busywork [yespress.io]. Its move into fintech with Kajabi Capital signals an expansion beyond software into financial services [askcyborg.com]. Key open questions include how the removal of the entry-level plan and the new AI credit paywall will affect its core mid-tier creator base, and whether the return of the founder-CEO signals a strategic pivot or a return to its bootstrapped ethos.

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

### google/gemini-3.8-flash

Cost: $0.0201

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
Kajabi is an all-in-one business platform for "knowledge entrepreneurs"—coaches, consultants, course creators, and authors—allowing them to build websites, sell courses, run communities, and manage marketing funnels without stitching together separate tools ([yespress.io](https://yespress.io/kajabi)). Rather than mega-influencers, its core customer base is mid-sized experts; 89% of full-time Kajabi creators have under 50,000 Instagram followers ([yespress.io](https://yespress.io/kajabi)). 

Kajabi operates a SaaS subscription model (Basic at $179/mo, Growth at $249/mo, Pro at $499/mo) and differentiates by charging **0% transaction fees** on creator sales ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). It also monetizes branded mobile apps and native payment processing (Kajabi Payments at ~2.9% + 30¢) ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [yespress.io](https://yespress.io/kajabi)).

### 2. Recent News and Launches
* **January 2026 Pricing Overhaul:** Kajabi eliminated its entry-level Kickstarter tier, raised prices across all plans, lowered Basic contact limits, and introduced metered AI credits ($15 per 500 credits), completely gating credits on the Basic tier ([thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **AI Agents & "Cofounder":** Rolled out "Kajabi Evolved," introducing Kajabi Cofounder, Expert Agents, and MCP integration to act as automated operational teammates for solo creators ([theeduassist.com](https://theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/), [thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **Fintech Expansion (Dec 2025):** Partnered with Parafin to launch *Kajabi Capital*, offering embedded working capital loans to U.S. creators ([askcyborg.com](https://askcyborg.com/company/kajabi)).

### 3. Funding, Size, and Financial Signals
* **Valuation & Funding:** Bootstrapped for nearly a decade before raising a $550 million Series D led by Tiger Global in May 2021 at a >$2 billion valuation ([yespress.io](https://yespress.io/kajabi)).
* **Scale:** Generates $100M+ ARR, with over 60,000 active creators who have facilitated more than $10 billion in cumulative GMV ([askcyborg.com](https://askcyborg.com/company/kajabi), [yespress.io](https://yespress.io/kajabi)).
* **Headcount:** Approximately 350–500 employees, reflecting disciplined post-hypergrowth operations ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).

### 4. Leadership
In 2025, CEO Ahad Khan departed. Co-founder Kenny Rueter returned as Co-CEO alongside longtime company president Jonathan Cronstedt, returning the company to founder-led executive management ([yespress.io](https://yespress.io/kajabi)).

### 5. Main Competitors and How They Differ
* **Thinkific & Teachable:** Direct course-hosting competitors. Kajabi positions as a more comprehensive, premium, all-in-one suite and does not charge platform revenue-share percentages ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Circle & Mighty Networks:** Stronger in community-first engagement; Kajabi counters by bundling marketing funnels and automation into community offerings ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Podia & Skool:** Compete aggressively on price and ease of use. Podia undercuts Kajabi’s high price floor, while Skool captures community-based monetization ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).

### 6. Likely Strategic Priorities and Open Questions
* **Priorities:** Monetizing creator fintech (Kajabi Capital and native payments) and upselling AI agents to drive higher ARPU beyond pure SaaS subscriptions ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **Questions to Ask:**
  * How are customer churn and conversion trending following the January 2026 price hikes and the removal of the sub-$100 entry tier?
  * What is the adoption and repayment performance for the newly launched Kajabi Capital?
  * What is the Co-CEOs' timeline and preferred route for investor liquidity following the 2021 valuation?

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)

#### Run 2

### 1. What They Do, Who Buys It, and How They Make Money
Kajabi is an all-in-one operating platform for knowledge entrepreneurs, consolidating course hosting, community, website creation, marketing funnels, email automation, coaching, and checkout into one system ([yespress.io](https://yespress.io/kajabi)). Its core buyers are solo experts, consultants, and creators (89% have fewer than 50,000 Instagram followers) who monetize specialized knowledge ([yespress.io](https://yespress.io/kajabi)). 

Kajabi monetizes through tiered SaaS subscriptions: Basic ($179/month), Growth ($249/month), and Pro ($499/month) ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)). Unlike many creator platforms, Kajabi charges 0% platform transaction fees on creator GMV, though it monetizes payment processing via Kajabi Payments (~2.9% + $0.30) and sells add-ons like branded mobile apps and AI credits ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500), [yespress.io](https://yespress.io/kajabi)).

### 2. Recent News and Launches
* **Pricing & Packaging Overhaul (January 2026):** Discontinued the entry-level $89/month "Kickstarter" plan, raised monthly prices across existing tiers, reduced Basic contact limits, and introduced tiered AI usage credits ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)).
* **Kajabi Evolved & AI Agents (Late 2025–Early 2026):** Rolled out platform upgrades including visual automations and "Cofounder," an AI teammate and chat system providing business insights and content creation workflows ([theeduassist.com](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/), [yespress.io](https://yespress.io/kajabi)).
* **Kajabi Capital (December 2025):** Partnered with Parafin to offer embedded working capital and financing directly within the creator dashboard ([askcyborg.com](https://askcyborg.com/company/kajabi)).

### 3. Funding, Size, and Financial Signals
* **Funding:** Bootstrapped for nearly a decade before raising a minority round in 2019 and a $550 million growth round in May 2021 led by Tiger Global at a ~$2 billion valuation ([yespress.io](https://yespress.io/kajabi)). No new primary rounds have been disclosed ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Scale:** Serves over 60,000 creators, supports over $10 billion in cumulative GMV, generates $100M+ in ARR, and employs approximately 390 people ([askcyborg.com](https://askcyborg.com/company/kajabi), [yespress.io](https://yespress.io/kajabi)).

### 4. Leadership
Following the 2025 departure of CEO Ahad Khan, co-founder Kenny Rueter returned to operational leadership alongside longtime President Jonathan Cronstedt as Co-CEOs ([yespress.io](https://yespress.io/kajabi)).

### 5. Main Competitors and Differentiation
* **Competitors:** Thinkific, Teachable, Podia, Circle, Skool, and Mighty Networks ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).
* **Differentiation:** 
  * **0% Platform Fees:** Unlike Teachable or Patreon, Kajabi does not take a percentage cut of creator sales, making it economically attractive for established creators earning $1,000–$2,000+ monthly ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).
  * **All-in-One Breadth:** Consolidates marketing funnels, full email marketing, and product delivery to prevent creators from stitching together point solutions like ClickFunnels and ConvertKit ([yespress.io](https://yespress.io/kajabi)).

### 6. Likely Strategic Priorities and Open Questions
* **Fintech & ARPU Expansion:** Expanding creator monetization through native financial tools like Kajabi Capital and Kajabi Payments ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi), [askcyborg.com](https://askcyborg.com/company/kajabi)).
* **Retention vs. Price Hikes:** How will creator retention fare following the elimination of the sub-$100 entry tier and price hikes on core plans ([thecoursetimes.com](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500))?
* **Community Competition:** How Kajabi plans to fend off community-led disruptions from lighter, highly viral platforms such as Skool and Circle ([akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)).

**Sources**

1. [Kajabi company profile: firmographics, business model, customers, competitors \| akta.pro](https://akta.pro/company-profiles/00004mf/kajabi)
2. [Kajabi: The Operating System for Human Expertise \| YesPress](https://yespress.io/kajabi)
3. [Kajabi Major Updates 2026: AI Cofounder, Expert Agents,... \| TheEduAssist](https://www.theeduassist.com/blog/kajabi-major-updates-2026-ai-cofounder-expert-agents-amplify-more/)
4. [Kajabi's Entry Plan Now Includes Zero AI Credits. Everyone Else Pays $15 Per 500. \| The Course Times](https://www.thecoursetimes.com/story/kajabis-entry-plan-now-includes-zero-ai-credits-everyone-else-pays-15-per-500)
5. [Kajabi company overview 2026: revenue $100M+, Cyborg Score 8/10 \| AskCyborg](https://askcyborg.com/company/kajabi)
