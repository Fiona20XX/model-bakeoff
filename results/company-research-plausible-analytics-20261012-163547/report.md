# Bake-off: company_research

A sourced one-page briefing on a company, for meeting or interview prep.

- Run: 2026-10-12T16:35:47
- Variables: `company=Plausible Analytics`
- Judge: `openai/gpt-6-sol`
- Web search: on (exa engine, max 5 results)
- Runs per model: 2
- Total cost: $0.2025 (contestants $0.1286, judge $0.0739)

## Results

| Model | Score | Cost | Latency | Sources | Unsupported claims | Score per cent |
|---|---|---|---|---|---|---|
| anthropic/claude-sonnet-5.5 | 8.0 (7.8–8.2) | $0.0365 | 18.2s (17.8s–18.5s) | 5 (5–5) | 4 (3–5) | 2.2 |
| deepseek/deepseek-v4-pro | 6.2 (6.0–6.5) | $0.0099 | 38.0s (32.9s–43.1s) | 5 (5–5) | 5 (5–5) | 6.3 |
| google/gemini-3.8-flash | 5.9 (5.8–6.0) | $0.0180 | 23.0s (22.6s–23.4s) | 5 (5–5) | 6 (6–6) | 3.3 |

## Judge rationales

- **anthropic/claude-sonnet-5.5**: A gives a concrete, meeting-useful briefing and correctly declines to date undated features as launches, though several product and competitor details exceed the supplied excerpts.
- **deepseek/deepseek-v4-pro**: B contains useful figures, but its invented refresh framing and internally contradictory pricing description weaken an otherwise specific briefing.
- **google/gemini-3.8-flash**: C is concrete and offers useful questions, but it presents undated features as recent launches and adds several unsupported technical and operational specifics.

## Unsupported claims

- **anthropic/claude-sonnet-5.5** (run 1): The supplied excerpts do not establish the AGPLv3 license or the availability of self-hosting.
- **anthropic/claude-sonnet-5.5** (run 1): The supplied excerpts do not establish that Fathom is closed-source and cloud-only, or substantiate the detailed Matomo and PostHog comparisons.
- **anthropic/claude-sonnet-5.5** (run 1): The cited excerpt does not establish that Plausible built its brand specifically around Google Analytics alternative content.
- **deepseek/deepseek-v4-pro** (run 1): No supplied excerpt dates a homepage refresh to 2026 or establishes April–October 2026 as the relevant six-month window.
- **deepseek/deepseek-v4-pro** (run 1): The claim that every plan has the entire feature set conflicts with the cited SaaSTracker excerpt, which gates funnels, revenue attribution, and API access to Business.
- **deepseek/deepseek-v4-pro** (run 1): The excerpts do not establish that higher tiers add 50 Fathom sites per plan, that agencies favor Fathom, or that Plausible wins EU-sovereignty buyers over it.
- **deepseek/deepseek-v4-pro** (run 1): The supplied excerpts do not establish Umami's MIT license or Postgres requirement.
- **deepseek/deepseek-v4-pro** (run 1): A high bottom-line margin and sustained growth are asserted without current margin or post-2024 growth figures.
- **google/gemini-3.8-flash** (run 1): The supplied excerpts do not substantiate the sub-1.4 KB script size or GDPR and ePrivacy compliance out of the box.
- **google/gemini-3.8-flash** (run 1): The supplied excerpts support pageview-based pricing, but not the assertion that custom events also determine price.
- **google/gemini-3.8-flash** (run 1): The homepage lists AI-referral and codeless tracking features but does not date their introduction; calling them recent releases is unsupported.
- **google/gemini-3.8-flash** (run 1): The source says the team has 10 people, not that all 10 are full-time employees.
- **google/gemini-3.8-flash** (run 1): The cited excerpts do not establish zero dollars spent on paid advertising.
- **google/gemini-3.8-flash** (run 1): The supplied excerpts do not establish that GA4 requires cookie banners, that Fathom is cloud-only, or that Plausible offers a self-hostable version.
- **anthropic/claude-sonnet-5.5** (run 2): The provided excerpts establish that Plausible's code is AGPLv3 and can be self-hosted or forked.
- **anthropic/claude-sonnet-5.5** (run 2): Both leaders are listed as co-founders in the cited homepage excerpt.
- **anthropic/claude-sonnet-5.5** (run 2): The provided excerpts substantiate the specific Fathom, Matomo, and PostHog feature comparisons.
- **anthropic/claude-sonnet-5.5** (run 2): Plausible says it has never spent on affiliates; that statement is not in the cited excerpt.
- **anthropic/claude-sonnet-5.5** (run 2): The cited checkthat.ai excerpt describes pricing tiers through Enterprise.
- **deepseek/deepseek-v4-pro** (run 2): The script is under 1.4 KB and about 45 times smaller than Google Analytics.
- **deepseek/deepseek-v4-pro** (run 2): Both Uku Taht and Marko Saric are identified as co-founders in the cited excerpts.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts establish that Fathom is cloud-only, Matomo is more complex, or PostHog offers session replay.
- **deepseek/deepseek-v4-pro** (run 2): The cited excerpts establish the AGPLv3 license or self-hosting.
- **deepseek/deepseek-v4-pro** (run 2): “Ummi” is a competitor; the retrieved source names Umami.
- **google/gemini-3.8-flash** (run 2): The script is under 1 KB, and the cited excerpts establish its AGPLv3 license.
- **google/gemini-3.8-flash** (run 2): Collecting no personal data means customers do not require GDPR/ePrivacy cookie-consent banners.
- **google/gemini-3.8-flash** (run 2): Recent six-month activity included Community Edition updates and ClickHouse-cluster optimizations.
- **google/gemini-3.8-flash** (run 2): Uku Taht holds the CEO title and leads engineering and product; Marko Saric handles developer advocacy.
- **google/gemini-3.8-flash** (run 2): The cited excerpts establish Fathom as closed-source and cloud-only or detail PostHog's session replay and feature flags.
- **google/gemini-3.8-flash** (run 2): Enterprise interest is growing.

## Answers

### anthropic/claude-sonnet-5.5

Cost: $0.0365

#### Run 1

# Plausible Analytics: Briefing

## 1. What they do, who buys it, how they make money
Plausible is a lightweight, privacy-focused web analytics tool and a Google Analytics alternative. It uses no cookies and collects no personal data, and it is hosted in the EU ([plausible.io](https://plausible.io/)). Named users include Stripe, Mozilla, Basecamp, Ghost, Hugging Face, MongoDB and Harvard ([plausible.io/about](https://plausible.io/about)). The buyer profile is mostly small businesses, bloggers and privacy-conscious organizations ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).

Subscriptions are the only revenue. Pricing is by monthly pageviews, from about $9/month up to several hundred, with all features on every plan ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). The product is open source under AGPLv3, and a self-hosted option exists ([plausible.io/about](https://plausible.io/about)).

## 2. Recent news and launches (last 6 months)
I found no dated news or press releases in my sources, so I can't confirm what shipped in the last six months. The current homepage highlights these features, without launch dates:
- Automatic scroll-depth tracking
- AI-referral traffic monitoring (ChatGPT, Perplexity, Claude)
- Search Console integration
- Automatic UTM channel grouping
- Codeless goals and revenue tracking ([plausible.io](https://plausible.io/))

Check the changelog and blog directly for recent releases.

## 3. Funding, size, financial signals
- **Funding:** None. The company is self-funded and profitable, with no outside investors and no plans to sell ([plausible.io/about](https://plausible.io/about)).
- **Team:** 10 people ([plausible.io/about](https://plausible.io/about)).
- **Revenue:** $1M ARR in 2022 ([plausible.io/about](https://plausible.io/about)). Third-party estimates put it at about $2.1M in 2023 and $3.1M in 2024 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)), with the $3.1M figure reported as publicly stated by the company ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). I found no 2025–26 revenue figure.
- **Customers:** The company claims 21,000+ paying subscribers ([plausible.io/about](https://plausible.io/about)). An older third-party figure says 16,000+ ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)), which is likely just growth over time.

## 4. Leadership
- **Uku Taht** started Plausible in December 2018 and built it alone ([plausible.io/about](https://plausible.io/about)).
- **Marko Saric** joined in 2020 for marketing and communications ([plausible.io/about](https://plausible.io/about)).

Both are listed as co-founders ([plausible.io](https://plausible.io/)). I found no formal titles such as CEO or CTO.

## 5. Main competitors and differences
- **Fathom:** Also privacy-focused, but closed-source and cloud-only ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **Matomo:** More features and customization, but needs more setup and ongoing management ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **PostHog:** Product analytics (session recordings, feature flags), which goes beyond Plausible's deliberately narrow scope ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **Simple Analytics and Umami:** Also named as rivals in the same source, but I found no detail on how they differ.
- **Google Analytics 4:** Plausible concedes GA4 has more depth for custom attribution, enterprise reporting with BigQuery, and Google Ads integration ([plausible.io/vs-google-analytics](https://plausible.io/vs-google-analytics)).

## 6. Likely strategic priorities and open questions
These are my inferences, not company statements.

**Priorities**
- Staying independent and profitable.
- Pulling in GA4 switchers, since the company has built its brand around "Google Analytics alternative" content ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)).
- Adding marketing-oriented features such as AI-referral tracking, SEO and campaign attribution, while keeping the product simple.
- Emphasizing EU hosting and data sovereignty.

**Open questions**
- Is growth holding up? Growth slowed from 110% to 48% between 2023 and 2024 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)), and I found no later data.
- How far will they push into deeper features without losing their simplicity?
- Is there any enterprise or agency strategy?
- What is the self-hosted versus cloud revenue split?

**Sources**

1. [About - Plausible Analytics](https://plausible.io/about)
2. [Plausible Analytics \| Simple, privacy-friendly Google ...](https://plausible.io/)
3. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
4. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
5. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)

#### Run 2

# Plausible Analytics Briefing

## 1. What they do, who buys it, and how they make money
Plausible is a lightweight, open-source web analytics product, positioned as a privacy-friendly alternative to Google Analytics. It uses no cookies and no persistent identifiers, and it hosts data on EU-owned infrastructure ([plausible.io](https://plausible.io/)). Named users include Stripe, Mozilla, MongoDB, Harvard and Sentry ([plausible.io](https://plausible.io/)). Subscription revenue is its only revenue ([plausible.io/about](https://plausible.io/about)). Pricing is by traffic volume, starting around $9/month ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). The code is AGPLv3, so customers can self-host or fork ([plausible.io/about](https://plausible.io/about)).

## 2. Recent news and launches (last 6 months)
I found no dated news or launch announcements in my sources, so I can't confirm what is new in the past six months. The homepage currently promotes these features, but without dates:
- Automatic scroll-depth tracking
- Monitoring of traffic from AI tools such as ChatGPT, Perplexity and Claude
- Search Console integration
- Automatic UTM channel grouping

([plausible.io](https://plausible.io/)). Check their changelog or blog for timing.

## 3. Funding, size, and financial signals
- **Funding:** None external. The company is self-funded and profitable, with no plans to sell ([plausible.io/about](https://plausible.io/about)).
- **Revenue:** It crossed $1M ARR in 2022 ([plausible.io/about](https://plausible.io/about)). Latka figures put it at roughly $2.1M in 2023 and $3.1M in 2024 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)). I found no 2025 or 2026 revenue figure.
- **Customers:** More than 21,000 paying subscribers ([plausible.io/about](https://plausible.io/about)). An older third-party figure is 16,000+ ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **Team:** 10 people ([plausible.io/about](https://plausible.io/about)).

## 4. Leadership
- **Uku Taht** started Plausible in December 2018 and built it alone. Paid subscriptions launched in 2019 ([plausible.io/about](https://plausible.io/about)).
- **Marko Saric** joined in 2020 to handle marketing and communications ([plausible.io/about](https://plausible.io/about)).
- Both are listed as co-founders ([plausible.io](https://plausible.io/)). I did not find formal titles.

## 5. Main competitors and how they differ
- **Google Analytics 4:** It offers deeper attribution and BigQuery/SQL reporting, plus tight Google Ads integration. Plausible argues it is simpler and independent of an ad-funded model ([plausible.io/vs-google-analytics](https://plausible.io/vs-google-analytics)).
- **Fathom:** Closed-source and cloud-only, while Plausible is open source and self-hostable ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **Matomo:** More features and customization, but it takes more setup and maintenance ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **PostHog:** Product analytics with session recordings and feature flags, which goes beyond Plausible's deliberately narrow scope ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- **Others:** Simple Analytics and Umami ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).

## 6. Likely strategic priorities and open questions
These are my inferences, not stated plans.

**Likely priorities**
- Staying independent and profitable ([plausible.io/about](https://plausible.io/about)).
- Adding marketing-oriented features such as AI-referral tracking, Search Console data and campaign attribution, to close gaps with GA4.
- Continuing to grow through content and word of mouth. The company says it has never spent on advertising or affiliates ([plausible.io/about](https://plausible.io/about)).

**Open questions**
- What is current ARR? Growth slowed from 110% to 48% between 2022–23 and 2023–24 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- How does pricing work today? One source says every feature is on every plan ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)), while another describes tiered plans through Enterprise ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
- How will they handle growing interest in product analytics and AI-traffic measurement without losing their simplicity?
- Is there an enterprise or self-hosted commercial strategy?

**Sources**

1. [About - Plausible Analytics](https://plausible.io/about)
2. [Plausible Analytics \| Simple, privacy-friendly Google ...](https://plausible.io/)
3. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
4. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
5. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)

### deepseek/deepseek-v4-pro

Cost: $0.0099

#### Run 1

Here’s a concise briefing on Plausible Analytics, based on the provided sources.

### 1. What they do, who buys it, and how they make money
Plausible is a privacy-first, open‑source web analytics tool that replaces Google Analytics with a simple, lightweight dashboard. It’s built for website owners who want essential traffic insights without cookies, consent banners, or data sharing.

The customer base spans solo bloggers to engineering‑led brands like Basecamp, Ghost, Hugging Face, MongoDB, and Harvard [saastracker.org]. The sole revenue stream is subscription fees, tiered by monthly pageviews—not by features or seats. Plans start at $9/month (Starter) and scale to custom Enterprise pricing; the entire feature set is available on every plan, with higher tiers adding more sites, users, and capabilities like funnels and API access [tinyempires.substack.com, saastracker.org]. The company explicitly rejects freemium, ad‑funded models, and affiliate spam [newname.ai].

### 2. Recent news and launches (last 6 months)
No specific product launches were found in the search results for April–October 2026. The most notable public update is the 2026 homepage refresh, which now reports 20,000+ paying subscribers, 260 billion lifetime pageviews tracked, 99.99% uptime (last 90 days), and a team of 10 [newname.ai]. Otherwise, the product continues to iterate quietly on its established privacy‑centric and self‑hosting‑friendly positioning.

### 3. Funding, size, and financial signals
Plausible has never taken outside funding. It is a fully bootstrapped Estonian company [checkthat.ai]. Revenue has grown organically:
- $1M ARR in 2022 (4 years after launch)
- ~$2.1M ARR in 2023 (110% YoY growth)
- $3.1M ARR in 2024 (48% growth) [checkthat.ai, tinyempires.substack.com]

The business operates profitably with a small remote team (~10 people) and minimal overhead. With 20,000+ paying customers and zero advertising spend, the model demonstrates strong product‑market fit and a high bottom‑line margin [tinyempires.substack.com, checkthat.ai].

### 4. Leadership
- **Uku Taht** – Founder, started Plausible in December 2018.
- **Marko Saric** – Joined as co‑founder (or business lead) in 2020, often the public voice of the company [saastracker.org, tinyempires.substack.com].

Both have maintained a transparent, community‑led approach, with the open‑source repository and content marketing (SEO, Hacker News, GitHub) driving early and sustained growth [tinyempires.substack.com].

### 5. Main competitors and how they differ
- **Google Analytics 4** – Free but complex; built on surveillance‑advertising feedback loops. Plausible offers EU‑hosted, cookie‑free, subscription‑only simplicity [plausible.io, newname.ai].
- **Fathom Analytics** – Closed‑source, flat‑price by traffic, includes 50 sites on every plan. Agencies favor it; open‑source and EU‑sovereignty buyers lean toward Plausible [saastracker.org, newname.ai].
- **Matomo** – More feature‑rich and self‑hostable, but demands technical setup. Plausible trades power for a zero‑config dashboard [checkthat.ai].
- **Umami** – MIT‑licensed self‑host on Postgres, attractive for developer cost control. Plausible counters with a managed EU cloud and brand trust [newname.ai].
- **PostHog** – Product analytics (session recordings, feature flags). Plausible deliberately stays limited to website metrics, avoiding feature overload [checkthat.ai].

### 6. Likely strategic priorities and open questions
- **Priorities:** Sustain the bootstrapped, high‑margin subscription model; defend the “Google Analytics alternative” SEO moat; deepen EU‑only data‑custody positioning and self‑hosting flexibility [tinyempires.substack.com, newname.ai].
- **Open questions:** Can the small team maintain growth while avoiding feature bloat? Will enterprise needs (funnels, revenue attribution) push them toward more complex plans, risking the simplicity that attracts users? How will they counter competitors if search‑ranking dynamics shift? No indications of a shift toward paid ads or external funding—but the bootstrapped scale remains modest relative to VC‑backed alternatives [checkthat.ai, tinyempires.substack.com].

**Sources**

1. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
2. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
3. [Plausible Analytics Review: Pricing, Features, Alternatives (2026) · SaaSTracker](https://saastracker.org/products/plausible)
4. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)
5. [Plausible Sells Subscriptions, Not Surveillance - NewName.ai Blog](https://newname.ai/blog/plausible)

#### Run 2

# Briefing: Plausible Analytics

**1. What they do, who buys it, and how they make money**  
Plausible is a privacy-first, open‑source web analytics platform. It provides a single‑page dashboard showing visitors, sources, pages, devices, goals and revenue—without cookies, personal data collection, or cross‑site tracking. The script is under 1.4 KB, about 45× smaller than Google Analytics, and all data is processed on European‑owned servers [plausible.io](https://plausible.io/).  
Customers range from solo bloggers to large organisations like Stripe, Mozilla, Basecamp, Hugging Face and Harvard University, with more than 21,000 paying subscribers [plausible.io/about](https://plausible.io/about). Revenue comes entirely from subscriptions based on monthly pageviews, not feature gates. Every plan gives access to the full feature set, and the company does not sell data or run ads [plausible.io/about](https://plausible.io/about).

**2. Recent news and launches (last 6 months)**  
No major product launches from the past six months were identified in the provided search results. The public homepage highlights features like automatic scroll‑depth tracking, AI‑tool referral monitoring (ChatGPT, Perplexity, etc.), Search Console integration, and real‑time dashboard updates, but the timing of these additions is not dated in the source material [plausible.io](https://plausible.io/). The company appears to iterate continuously rather than making splashy announcements.

**3. Funding, size, and financial signals**  
Plausible has never taken outside funding and remains entirely bootstrapped [checkthat.ai](https://checkthat.ai/brands/plausible-analytics). After launching in 2018, it reached $1 M ARR in 2022, roughly $2.1 M in 2023, and $3.1 M by late 2024—a 48% year‑over‑year increase [checkthat.ai](https://checkthat.ai/brands/plausible-analytics), [tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics). The team is 10 people, and the business is profitable, with all costs covered by subscription income [plausible.io/about](https://plausible.io/about).

**4. Leadership**  
The company was founded by Uku Taht, who built the product solo from December 2018. Marko Saric joined in 2020 to lead marketing and communications. Both are identified as co‑founders [plausible.io](https://plausible.io/). No other executives are highlighted; the entire team is listed on the company’s team page [plausible.io/about](https://plausible.io/about).

**5. Main competitors and how they differ**  
Key competitors include Fathom Analytics (cloud‑only, closed‑source), Matomo (feature‑rich but complex, self‑hosted), PostHog (product analytics with session replay), and open‑source options like Ummi.  
Plausible differentiates on three fronts:  
- **Radical simplicity** – a single‑page dashboard without configuration.  
- **Open‑source transarency** (AGPLv3), allowing self‑hosting and audits that closed competitors lack.  
- **Extreme performance** – the lightweight script and EU‑hosted, cookieless design make it the easiest privacy‑compliant migration from Google Analytics [checkthat.ai](https://checkthat.ai/brands/plausible-analytics), [plausible.io/vs‑google‑analytics](https://plausible.io/vs-google‑analytics).

**6. Likely strategic priorities and open questions**  
Priorities probably include: deepening AI‑referral analytics to capture the shift toward LLM‑driven traffic; defending the SEO/content moat around “Google Analytics alternative”; and adding lightweight features (e.g., funnels) without sacrificing simplicity. The business model’s alignment with customer interests remains a core strength [tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics).  
Open questions: Can subscription‑only growth be sustained as the privacy‑analytics space becomes more crowded? Will the team remain content with a modest $3M‑$4M ARR, or might acquisition pressure eventually appear? How will evolving AI‑generated traffic measurement be handled while staying cookieless? No clear answers exist in the public record.

**Sources**

1. [About - Plausible Analytics](https://plausible.io/about)
2. [Plausible Analytics \| Simple, privacy-friendly Google ...](https://plausible.io/)
3. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
4. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
5. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)

### google/gemini-3.8-flash

Cost: $0.0180

#### Run 1

### 1. What They Do, Who Buys It, and How They Make Money
* **What they do:** Plausible Analytics provides a lightweight (sub-1.4 KB script), cookie-free, privacy-first web analytics platform that complies with GDPR and ePrivacy out of the box ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)). It processes and hosts all data entirely within the EU ([plausible.io](https://plausible.io/)).
* **Who buys it:** Over 21,000 paying customers, ranging from individual creators to major tech organizations and institutions including Stripe, Mozilla, Harvard University, Hugging Face, and Basecamp ([plausible.io](https://plausible.io/about)).
* **Business model:** Pure subscription SaaS priced on monthly traffic volume (pageviews and custom events), starting at $9/month ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)). All tiers have access to the same core features ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). Plausible sells no data, shows no ads, and offers no affiliate kickbacks ([plausible.io](https://plausible.io/about)).

### 2. Recent News and Launches
Specific press releases from the last six months are limited, but recent product releases focus on modern traffic trends:
* **AI Tool Tracking:** Added automated tracking to detect and isolate inbound referral traffic originating from AI tools like ChatGPT, Claude, and Perplexity ([plausible.io](https://plausible.io/)).
* **Codeless Event Enhancements:** Introduced automatic 1–100% scroll depth tracking and codeless revenue/goal setups for file downloads and outbound links ([plausible.io](https://plausible.io/)).

### 3. Funding, Size, and Financial Signals
* **Funding:** Bootstrapped with zero outside institutional funding; fully self-funded from cash flow ([plausible.io](https://plausible.io/about), [checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
* **Team size:** 10 full-time employees ([plausible.io](https://plausible.io/about)).
* **Financial performance:** Profitable. Reached $1M ARR in 2022 ([plausible.io](https://plausible.io/about)), ~$2.1M in 2023, and hit $3.1M ARR in 2024 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics), [tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). The company has achieved this with $0 spent on paid advertising ([plausible.io](https://plausible.io/about)).

### 4. Leadership
* **Uku Taht (Co-Founder):** Founded the company solo in December 2018 and engineered the core platform ([plausible.io](https://plausible.io/about)).
* **Marko Saric (Co-Founder):** Joined in 2020 to lead marketing, organic search positioning, and communications ([plausible.io](https://plausible.io/about)).

### 5. Main Competitors and Differentiation
* **Google Analytics 4 (GA4):** Plausible offers a single-page dashboard without cookie banners or surveillance capitalism, whereas GA4 requires cookie banners, complex setup, and integrates directly into Google's ad ecosystem ([plausible.io](https://plausible.io/about), [plausible.io](https://plausible.io/vs-google-analytics)).
* **Fathom Analytics:** A close privacy-first peer, but Plausible is open source under AGPLv3 and offers a self-hostable version, while Fathom is proprietary and cloud-only ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
* **Matomo & PostHog:** Matomo offers heavier, on-prem enterprise customization that requires technical upkeep; PostHog focuses broadly on product analytics (session replays, feature flags). Plausible deliberately focuses strictly on high-level website traffic metrics ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).

### 6. Strategic Priorities and Open Questions
* **Priorities:** Measuring new forms of web interaction (such as AI tool attribution) ([plausible.io](https://plausible.io/)), scaling EU-native cloud infrastructure to service high-traffic enterprise sites, and holding strong organic SEO dominance against copycat privacy tools ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)).
* **Questions for the meeting:** 
  1. As enterprise accounts increase, how will you handle requests for advanced features (e.g., custom SQL access or complex multi-touch attribution) without compromising simplicity?
  2. How is Plausible adapting its tracking methodology as AI agents and scrapers increasingly replace human pageviews?

**Sources**

1. [About - Plausible Analytics](https://plausible.io/about)
2. [Plausible Analytics \| Simple, privacy-friendly Google ...](https://plausible.io/)
3. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
4. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
5. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)

#### Run 2

### 1. What They Do, Who Buys It, and How They Make Money
Plausible Analytics provides a lightweight (<1 KB script), open-source (AGPLv3), cookie-free web analytics tool built as an alternative to Google Analytics ([saastracker.org](https://saastracker.org/products/plausible), [newname.ai](https://newname.ai/blog/plausible)). Because it collects no personal data, users do not require GDPR/ePrivacy cookie consent banners ([plausible.io](https://plausible.io/vs-google-analytics)). 

* **Buyers:** Privacy-conscious organizations, developers, and European businesses requiring strict EU data residency—notable customers include Basecamp, Ghost, Hugging Face, and Harvard ([saastracker.org](https://saastracker.org/products/plausible)).
* **Monetization:** Fully subscription-based; tiers scale primarily by monthly pageviews (Starter from $9/month, Growth from $14/month, Business from $19/month, and custom Enterprise) ([saastracker.org](https://saastracker.org/products/plausible)). Higher tiers gate features such as funnels, ecommerce attribution, and API access ([saastracker.org](https://saastracker.org/products/plausible)). 

### 2. Recent News and Launches (Last 6 Months)
No major funding events, acquisitions, or dramatic product pivots have been publicly reported in the last six months. Recent momentum has centered on incremental updates to their self-hosted Community Edition, infrastructure optimizations for ClickHouse clusters, and crossing over 20,000–21,000 active paying subscribers with more than 260 billion lifetime pageviews tracked ([saastracker.org](https://saastracker.org/products/plausible), [newname.ai](https://newname.ai/blog/plausible)).

### 3. Funding, Size, and Financial Signals
* **Funding:** $0 external capital raised; 100% bootstrapped and customer-funded ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
* **Headcount:** Lean team of approximately 10 remote employees ([saastracker.org](https://saastracker.org/products/plausible), [newname.ai](https://newname.ai/blog/plausible)).
* **Financials:** Reached $1M ARR in 2022, ~$2.1M in 2023, and hit ~$3.1M ARR in 2024 ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)). High gross margins and structural profitability stem from running zero paid marketing campaigns (relying entirely on SEO, GitHub, and organic developer word-of-mouth) ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)). The company donates 5% of gross revenue to environmental and open-source initiatives ([newname.ai](https://newname.ai/blog/plausible)).

### 4. Leadership
* **Uku Taht:** Founder & CEO (started the company in December 2018; leads engineering and product) ([saastracker.org](https://saastracker.org/products/plausible)).
* **Marko Saric:** Co-founder (joined in 2020; drives marketing, developer advocacy, and content strategy) ([saastracker.org](https://saastracker.org/products/plausible)).

### 5. Main Competitors and How They Differ
* **Google Analytics 4 (GA4):** Free and feature-packed, but GA4 carries steep GDPR legal risks in the EU, complex reporting, and integration into surveillance advertising ([plausible.io](https://plausible.io/vs-google-analytics), [newname.ai](https://newname.ai/blog/plausible)). Plausible offers simplicity, no tracking cookies, and complete EU data sovereignty ([newname.ai](https://newname.ai/blog/plausible)).
* **Fathom Analytics:** Plausible’s closest direct privacy SaaS peer. Fathom is closed-source and cloud-only, whereas Plausible is open source and offers an AGPL self-hostable version ([saastracker.org](https://saastracker.org/products/plausible), [checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).
* **PostHog & Matomo:** Matomo provides deeper on-prem enterprise configurability, and PostHog delivers full product analytics (session replays, feature flags) ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)). Plausible intentionally limits scope to high-level traffic metrics to avoid dashboard clutter ([checkthat.ai](https://checkthat.ai/brands/plausible-analytics)).

### 6. Likely Strategic Priorities and Open Questions
* **Strategic Priorities:** Maintaining strict operational efficiency, scaling EU infrastructure to lower compute costs per million events, and expanding Business-tier adoption (funnels, API access) to raise average revenue per user (ARPU) without taking outside capital ([tinyempires.substack.com](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics), [saastracker.org](https://saastracker.org/products/plausible)).
* **Open Questions:** 
  1. As generative search engines disrupt traditional top-of-funnel organic search, how will Plausible maintain acquisition without paid marketing?
  2. With enterprise interest growing, how long can a ~10-person team support rigorous enterprise SLAs and custom security requests without hiring bloat?

**Sources**

1. [Plausible vs Google Analytics 4 (GA4): What changed and why people are switching \| Plausible Analytics](https://plausible.io/vs-google-analytics)
2. [Inside a Tiny Empire: Plausible Analytics](https://tinyempires.substack.com/p/inside-a-tiny-empire-plausible-analytics)
3. [Plausible Analytics Review: Pricing, Features, Alternatives (2026) · SaaSTracker](https://saastracker.org/products/plausible)
4. [Plausible Analytics](https://checkthat.ai/brands/plausible-analytics)
5. [Plausible Sells Subscriptions, Not Surveillance - NewName.ai Blog](https://newname.ai/blog/plausible)
