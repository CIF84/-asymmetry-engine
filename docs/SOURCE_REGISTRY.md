# Signal Source Registry

## Purpose

Asymmetry Engine should not confuse **publicly visible information** with **data we can safely depend on for a commercial system**.

Before evaluating signal quality, every candidate source should pass an access-and-reuse gate.

This document is a research registry, not an implementation roadmap. It records what we currently know about candidate sources, where uncertainty remains, and which sources are plausible foundations for the Engine.

## Source Gate

A candidate source should be evaluated in this order:

1. **Legitimate access** — Is there an official API, downloadable dataset, feed, or clearly permitted automated access path?
2. **Commercial reuse** — Can data or derived outputs be used in a commercial product/workflow without case-by-case permission?
3. **Retention / derivation** — May we persist the evidence or derived signal needed by the Engine?
4. **Operational reliability** — Are quotas, approval requirements, rate limits, access instability, or platform policy changes acceptable?
5. **Signal value** — Only after the above: does the source provide useful, independent evidence of economic friction, demand, intent, pain, market state, or supply-side structure?

A source can therefore have excellent signal quality and still be rejected as foundational infrastructure.

## Status labels

- **GREEN — structural**: plausible foundational source; legitimate access and reuse appear compatible with the project.
- **YELLOW — opportunistic / gated**: potentially valuable, but access, policy, retention, licensing, or dependency risk prevents treating it as structural today.
- **RED — exclude as foundation**: commercial restrictions, scraping dependency, or platform-control risk make it unsuitable as a core source.
- **RESEARCH — not yet verified**: promising signal family, but terms/access still require first-party verification.

## Current candidate registry

| Source | Evidence type | Access path | Commercial / reuse position | Geography | Independence from Stack Exchange | Current status | Notes |
|---|---|---|---|---|---|---|---|
| Stack Exchange | Explicit questions, problems, decision friction | Official Stack Exchange API | Usable subject to API terms, applicable content licence and attribution requirements | Global-ish, community dependent | Baseline source | **GREEN** | Already implemented. Rich individual textual evidence; strong self-selection and technical/prosumer bias. |
| CFPB Consumer Complaint Database | Realized consumer financial pain; complaints and structured product/problem fields | Official complaint API + downloads | CFPB states published complaint data is freely available for anyone to use, analyze and build on | US | Very high | **GREEN** | Implemented in Spec 004. Structured individual complaint evidence; newest-first publication order can be highly batch-concentrated and must not be treated as representative prevalence. https://www.consumerfinance.gov/data-research/consumer-complaints/ |
| FCA complaints data | Aggregated regulated complaints by firm/product/cause | Official downloadable datasets | Numerical FCA datasets owned by FCA are generally reusable under the UK Open Government Licence; verify each dataset/third-party exception | UK | Very high | **GREEN** | Strong aggregated population-level evidence; less narrative richness than Stack Exchange/CFPB. https://www.fca.org.uk/data/complaints-data |
| Eurostat | Economic, demographic, business and market-state statistics | Official downloads/APIs | Eurostat permits reuse of statistical data for commercial and non-commercial purposes with source acknowledgement, subject to stated exceptions | EU / Europe | Very high | **GREEN** | Not direct friction evidence, but strong contextual denominator/market-state source. https://ec.europa.eu/eurostat/help/copyright-notice |
| EU Data Portal / EU open datasets | Broad government/open datasets | Official catalogue/APIs/downloads | Licence varies by dataset; EU-owned material is often openly reusable, but dataset-level verification is mandatory | EU / Europe | High | **GREEN / DATASET-SPECIFIC** | Treat licence as dataset metadata, never inherit permission merely because a dataset appears in the portal. https://data.europa.eu/ |
| US SEC EDGAR | Company filings, disclosures, XBRL financial data | Official REST APIs and archives | Public access supported; automated use must comply with SEC Fair Access policy | US / global issuers | Very high | **GREEN** | Valuable supply-side/company-change evidence rather than direct consumer friction. SEC currently documents unauthenticated JSON APIs and fair-access limits. https://www.sec.gov/search-filings/edgar-application-programming-interfaces |
| Google Ads Keyword Planner / Google Ads API | Search demand, keyword ideas, competition, historical search volumes, bid ranges/CPC | Official Google Ads API | Developer token required. KeywordPlanIdeaService is restricted under Explorer access and requires Basic/Standard access with the appropriate permissible-use approval. Google describes the keyword-research permissible use as supporting suggestions that facilitate creation and management of Google Ads campaigns. | Broad / geo-targetable | Very high | **RED AS FOUNDATION / YELLOW ONLY IF EXPLICITLY APPROVED** | Excellent signal, but our intended use is independent market/asymmetry research rather than campaign creation. Do not build the Engine around this API unless Google explicitly approves this use for the developer token. https://developers.google.com/google-ads/api/docs/api-policy/access-levels |
| DataForSEO keyword/search-volume APIs | Search demand, monthly volume, CPC, paid competition, bid ranges, historical trends | Commercial API with account credentials | Paid API product intended for programmatic SEO/search-data consumption; exact downstream redistribution/derived-data rights still require contractual verification before implementation | Broad / geo-targetable | Very high | **RESEARCH — HIGH PRIORITY SUBSTITUTE** | Technically well aligned and avoids needing our own Google Ads KeywordPlanIdeaService approval. Current endpoints expose up to 1,000 keywords/request for Google Ads search-volume data, including monthly searches, CPC, competition and bid ranges. Need explicit terms review for retention/derived commercial use before Spec 005. https://docs.dataforseo.com/v3/keywords_data-google_ads-search_volume-live/ |
| Google Trends API | Search-interest trajectory, geography, seasonality | Official API | Official API exists only in limited alpha access as of 2026-09 | Global / regional | Very high | **YELLOW — WAIT** | Strategically excellent temporal signal, but not available broadly enough to become structural today. https://developers.google.com/search/apis/trends |
| YouTube Data API | Attention, videos, metadata, comments, creator/audience signals | Official API | Commercial API clients are possible, but data aggregation, storage, derived metrics and scraping are tightly restricted by YouTube policy | Global | High | **YELLOW / LIKELY NON-FOUNDATIONAL** | Useful only for narrowly compliant enrichment. Do not design the Engine around bulk aggregation/retention of YouTube data. https://developers.google.com/youtube/terms/developer-policies |
| Reddit | Broad consumer discussion, complaints, recommendations and intent | Approval-gated API; no scraping fallback should be assumed | Commercial use of Reddit data requires explicit approval/contractual permission; unauthorized scraping is prohibited | Global-ish | High | **RED** | Potentially excellent signal, but unsuitable as foundational infrastructure because commercial exploitation depends on Reddit permission. |
| Hacker News | Technical/startup discussion, problems, product/workflow friction | Official public API | Technical access is easy; commercial reuse/retention position still needs first-party policy verification before foundational use | Global-ish, technical | Medium | **RESEARCH** | Likely more useful for technical/prosumer demand than broad consumer demand; not sufficiently orthogonal to Stack Exchange to prioritize now. |
| Financial Ombudsman Service decisions | Resolved financial disputes with reasoning/outcomes | Public searchable decisions; structured machine access not yet verified | Reuse/access position needs first-party verification | UK | Very high | **RESEARCH** | Potentially exceptional evidence because it combines situation → complaint → adjudication → outcome. Access mechanism may be the limiting factor. |
| UK Companies House | Company registrations, officers, filings and corporate events | Official Companies House API | Open-data/reuse position and relevant API terms should be verified before implementation | UK | Very high | **RESEARCH** | Useful supply-side/company-formation and market-structure signal; not direct friction evidence. |
| US Census / Census Data API | Population, income, households, business/demographic context | Official APIs/downloads | Public-government data; verify dataset-specific attribution/licensing where relevant | US | Very high | **RESEARCH** | Useful denominator and addressable-market context, not direct demand evidence. |
| Data.gov / US agency open data | Broad public datasets | Official catalogue + agency APIs/downloads | Dataset-specific; federal public-data status does not remove need to inspect metadata/licence and agency terms | US | High | **RESEARCH** | Discovery layer rather than one source. Potential source family for domain-specific evidence. |
| Czech / EU national open-data portals | Local economic, pricing, regulatory, mobility, health, procurement or business datasets | Government APIs/downloads vary by publisher | Typically dataset-specific open-data licences; must be verified per source | Czechia / EU | Very high | **RESEARCH — HIGH STRATEGIC FIT** | Potentially short commercialization distance for locally exploitable opportunities. Worth deliberate survey rather than ad hoc scraping. |
| Product/pricing feeds and retailer APIs | Supply, price dispersion, availability, promotions | Highly provider-specific | Terms vary; many retailers prohibit scraping and provide no reusable public API | Market-specific | Very high | **RESEARCH / OFTEN YELLOW-RED** | Economically powerful if legitimate feeds exist. Never infer permission from public product pages. |
| Public procurement / tender datasets | Institutional demand, contract values, repeated purchasing problems | Government procurement APIs/downloads where available | Often open government data; verify dataset licence and retention | EU / national | Very high | **RESEARCH** | Could reveal B2B/institutional demand and recurring expensive workflows. Potentially strong non-consumer source family. |
| Patent / trademark open data | New technical/commercial activity, category formation, ownership | EPO/EUIPO/USPTO APIs/downloads vary | Public-data access exists; exact reuse terms need verification per provider | Global / regional | Very high | **RESEARCH** | More useful as market-change/supply signal than direct friction signal. |
| Official recall / product-safety databases | Realized product failure/harm | Government/EU datasets/APIs where available | Usually public/open-data oriented; verify specific licence | EU / US / national | Very high | **RESEARCH** | Interesting realized-pain evidence outside finance; could expose product categories with recurring failure/information problems. |
| App-store / marketplace reviews | Product dissatisfaction, missing features, willingness/expectation signals | Platform-dependent APIs or web pages | Often restrictive; scraping/public visibility is not enough | Global | High | **RESEARCH / LIKELY YELLOW-RED** | Signal is attractive, but terms/access must be decisive. Do not build around unofficial scrapers. |
| News / GDELT-style event feeds | Market/regulatory change, shocks, emerging topics | Provider feeds/APIs | Varies substantially by provider and underlying content rights | Global | High | **RESEARCH** | Better as contextual/event evidence than primary friction evidence. |

## Strategic signal families

The Engine should seek **orthogonal evidence**, not simply more websites containing text.

```text
EXPRESSED FRICTION
Stack Exchange / similar legitimate sources
        │
        ├───────────────┐
        ▼               ▼
REALIZED PAIN       SEARCH DEMAND
CFPB / FCA          approved/licensed provider
        │               │
        │               ▼
        │          COMMERCIAL INTENT
        │          competition / CPC
        │
        ├───────────────┐
        ▼               ▼
MARKET CONTEXT      SUPPLY-SIDE CHANGE
Eurostat / Census   SEC / company data
        │               │
        └───────┬───────┘
                ▼
        EVIDENCE CONVERGENCE
```

The strongest future asymmetry candidates should ideally be supported by multiple structurally independent signal families.

## Important design implications

### Public does not mean reusable

A page being readable in a browser says almost nothing about whether it should be collected, retained, transformed, or used commercially by the Engine.

### Scraping is an exception, not the default

Foundational sources should preferably expose an official API, feed, bulk download, or explicitly permitted automated access mechanism. A business should not depend on evading platform controls.

### Commercial-use permission is source metadata

Every implemented `SignalSource` should eventually retain enough provenance to answer:

- how we access it,
- what terms/licence govern the data,
- whether commercial reuse is permitted,
- what attribution is required,
- what retention/derivation constraints apply,
- what known selection biases exist.

This should remain lightweight until a second source proves what metadata is genuinely common.

### Derived intelligence should become the durable asset

Even for permissive sources, the long-term portfolio should depend less on redistributing raw source data and more on accumulated derived knowledge: recurring friction structures, cross-source convergence, market trajectories, experiment outcomes, conversion, payment behaviour and successful commercialization mechanisms.

## Current recommendation

Do **not** implement Google Ads Keyword Planner directly as a foundational source under current policy assumptions.

The access feasibility check found a substantive mismatch rather than merely credential friction:

1. Google Ads API requires a developer token tied to a Google Ads manager account.
2. `KeywordPlanIdeaService` is restricted under Explorer access, so production keyword-planning use requires Basic or Standard access.
3. Basic/Standard tokens have permissible-use scopes allocated by Google.
4. Google's documented keyword-research permissible use is for tools requiring keyword suggestions to facilitate creation and management of Google Ads campaigns.
5. Asymmetry Engine's intended use is independent market/opportunity research, so we should not assume this scope covers us.

This is exactly the kind of platform dependency the Source Gate exists to catch.

For the next search-demand experiment, investigate a licensed commercial data provider whose product is explicitly designed for programmatic search/SEO intelligence. DataForSEO is currently the strongest candidate because its API exposes the desired search-volume/CPC/competition evidence without requiring our own Google Ads planning-service approval. Before implementation, verify its current terms for storage, derived analytics, internal commercial use, and downstream product use.

If that contractual gate passes, the next empirical slice should use a very small paid request seeded from observed friction terms rather than bulk keyword discovery.

If it does not pass, return to GREEN sources rather than weakening the Source Gate. FCA remains the strongest ready-to-implement fallback.

Google Trends should remain on the shortlist but is blocked as a structural source until general API access improves.

Reddit should remain excluded from foundational architecture unless its commercial-data policy materially changes or explicit commercial permission is obtained.

## Research discipline

This registry is not legal advice and should not be treated as frozen truth. Platform terms and API policies change.

Before implementing any new source:

1. re-check current first-party documentation,
2. record access/reuse/retention constraints in the implementation spec,
3. prefer official source documentation over blogs or third-party summaries,
4. explicitly state unresolved ambiguity rather than assuming permission,
5. reject the source if the business model would depend on an access interpretation we are uncomfortable defending.
