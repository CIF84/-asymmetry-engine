# Spec 005 — DataForSEO Search-Demand Evidence Slice

## Goal

Add a third, structurally different evidence family to Asymmetry Engine using DataForSEO's official API product for Google Ads keyword search-volume data.

The purpose is not to score opportunities or infer asymmetries yet. It is to test whether the Engine can represent **aggregate search-demand / paid-market evidence** alongside:

- Stack Exchange: individual expressed friction,
- CFPB: individual structured realized pain,
- DataForSEO: aggregate keyword demand and advertiser-market metrics.

The empirical question is:

> Can the existing weak observation layer honestly represent a keyword-market measurement whose evidence is aggregate, geographic, temporal, approximate, and vendor-mediated?

A second question is deliberately architectural:

> Does one `SourceObservation` per keyword measurement still make semantic sense, or does this source expose a real limit in the current observation abstraction?

Do not answer that question by redesigning the model in advance. Implement the smallest honest slice and report any pressure discovered.

## Source-gate conclusion

DataForSEO is acceptable for this empirical slice as a paid third-party data provider, with vendor dependency explicitly preserved as provenance.

Current first-party evidence supporting this decision:

- DataForSEO markets its APIs as building blocks for production SEO tools and commercial analytics products.
- DataForSEO explicitly describes some API output as raw / white-label data that can be shipped inside customers' own tools.
- DataForSEO documentation for Live endpoints tells customers whose projects require retaining results to store retrieved data on their own side.
- Current Terms of Service (updated 12 June 2026) define the Service as including data/content made available through or developed via the API. The explicit data-usage restriction found in Section 7 concerns use of SERP data to compete with or adversely affect originating search-engine providers.

This is materially different from the direct Google Ads API access concern: DataForSEO sells programmatic data access as the product rather than granting an advertising-management API under a permissible-use approval regime.

However, DataForSEO remains a **vendor dependency**, not an open/public structural source. Source metadata must preserve that distinction. Terms and product policies can change and should be rechecked before any future large-scale commercial dependence or raw-data redistribution model.

This specification is not legal advice and does not authorize unrestricted redistribution of raw provider data.

## Official API mechanism

Use DataForSEO API v3 and specifically the current Google Ads Search Volume Live endpoint:

```text
POST https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live
```

Current documentation states that this endpoint can return, for up to 1,000 supplied keywords per request:

- keyword,
- location,
- language,
- search volume,
- monthly searches,
- paid-search competition,
- competition index,
- low top-of-page bid,
- high top-of-page bid,
- CPC,
- spelling normalization where applicable.

Historical monthly data can cover up to four years; the default is approximately the past 12 months.

Current documented rate limit for Google Ads Live endpoints is 12 requests per minute per account.

Do not use SERP scraping endpoints for this slice.

## Important semantic limits

### Search volume is an estimate, not observed unique people

Do not encode search volume as exact demand, unique users, customers, or willingness to pay.

The provider describes search volume as an approximate average number of searches for a keyword under the specified targeting.

### CPC / bids are market signals, not product economics

Do not interpret CPC, competition, or bid ranges as proof that our hypothetical product can acquire customers profitably.

They are source-native paid-advertising market evidence only.

### Keywords are not problems

Do not classify keywords into friction categories, problems, asymmetries, products, or opportunities.

### Vendor-mediated data must remain visible

The observation means approximately:

> DataForSEO returned these Google Ads-derived keyword metrics for this query, location, language, and collection context at this time.

It does not mean the Engine directly observed Google searches.

### Geography is part of the measurement

Search demand changes by target market. Location/language must be preserved as first-class source-specific metadata and incorporated into stable identity where required to avoid treating different market measurements as the same observation.

## Scope

### 1. Add a DataForSEO keyword-demand collector

Implement a small concrete collector, e.g. `DataForSEOKeywordCollector`, using the official DataForSEO v3 endpoint above.

The collector must remain persistence-agnostic.

Use only Python standard-library HTTP functionality unless an existing dependency already solves the requirement. Do not add a large SDK solely for one request.

### 2. Authentication

Use credentials supplied through environment variables, for example:

```text
DATAFORSEO_LOGIN
DATAFORSEO_PASSWORD
```

Exact names may differ if there is a compelling local convention, but:

- credentials must never be committed,
- credentials must never appear in logs, observations, source metadata, errors, manifests, fixtures, or completion reports,
- missing credentials should produce a clear actionable CLI/runtime error,
- automated tests must use mocks/fakes and must not require real credentials.

### 3. Source metadata

Add a `SignalSource` using the existing source model.

Use a stable source ID such as:

```text
dataforseo:google-ads-keyword-demand
```

Record at minimum:

- provider/source name,
- official API endpoint/product identity,
- terms reference,
- paid/vendor-mediated access,
- commercial/reuse context described above,
- provider dependency,
- Google Ads-derived nature of the metrics,
- approximation / non-unique-user caveat,
- geography/language dependence,
- CPC/competition semantic caveat,
- collection cost as an operational consideration if useful.

Do not create a generic source-governance subsystem.

### 4. Seed keywords for the empirical slice

This slice should measure a **small explicit set of source-faithful search queries**, not invent an automated keyword-generation pipeline.

Use a checked-in text or Python fixture/list of approximately **20–30 seed queries** selected manually from recurring friction visible in the already-inspected Stack Exchange Money.SE sample.

The seeds should span several observed themes, for example:

- life insurance coverage calculation,
- budgeting / variable expenses,
- credit-card foreign transaction fees,
- ACH / bank transfer timing or failure,
- tax reporting / side-income / investment tax questions,
- Roth / retirement contribution questions,
- mortgage / home-equity questions,
- scam / suspicious charge / stolen-check concerns,
- ETF / investing-choice questions,
- selling old shares / precious metals.

Requirements:

- seeds must be ordinary search phrases, not copied question bodies,
- keep the list small and human-inspectable,
- do not use an LLM, embeddings, automatic expansion, Google autocomplete scraping, or DataForSEO keyword-suggestion endpoints yet,
- record the final exact seed list in the completion report.

The point is to ask whether already-observed friction has measurable search-demand / advertising evidence, not to maximize keyword coverage.

### 5. Target market

For the first empirical run, use **United States + English** targeting unless current DataForSEO semantics make a different explicit code/name preferable.

Why US first:

- the Google Ads-derived metrics are well supported there,
- CFPB gives us a US realized-pain comparison source,
- this is an evidence experiment, not a declaration that US opportunities are preferred.

Preserve exact location and language identifiers returned/used by the API.

Do not add multi-country orchestration yet.

### 6. Normalize each returned keyword measurement into `SourceObservation`

Attempt the smallest honest representation using the existing model.

A reasonable identity shape is:

```text
source_id: dataforseo:google-ads-keyword-demand
external_id: dataforseo:keyword:<normalized-keyword>:<location>:<language>
item_kind: keyword_demand
```

Exact escaping/hashing is a local engineering decision, but identity must be deterministic and collision-safe for keyword + target market.

Important: the current persistence model is first-capture / identity-deduplicating. Do not silently pretend this supports time-series monitoring. For this bounded slice, stable identity should make the second identical run deduplicate. Report explicitly that future repeated measurements over time may require version/history semantics if we choose to monitor demand changes.

Use collection time as `observed_at`.

There may be no source-native event timestamp equivalent to a question/complaint occurrence. Do **not invent one**. If `SourceObservation.occurred_at` is nullable, use `None`; if it is currently required, report the architectural pressure and choose the least misleading existing representation without broad schema redesign unless absolutely necessary.

### 7. Readable non-interpretive `content`

Create human-readable content from source-native values, for example:

```text
Keyword: how much life insurance do i need
Search volume: 5400
Competition: HIGH
Competition index: 87
CPC: 4.12 USD
Low top-of-page bid: 2.35 USD
High top-of-page bid: 8.40 USD
```

Exact formatting is local.

Requirements:

- source-native values only,
- omit missing values cleanly,
- no opportunity score,
- no demand-quality judgment,
- no profitability inference,
- no conversion estimate,
- no classification of search intent unless directly returned by this endpoint (and even then preserve only as source metadata; do not interpret it).

### 8. Preserve source-native metadata

Preserve useful returned fields where available, including:

- keyword,
- spell/corrected spelling,
- location code,
- language code,
- search partners flag,
- competition,
- competition index,
- search volume,
- low top-of-page bid,
- high top-of-page bid,
- CPC,
- monthly searches,
- relevant request targeting context,
- provider task/result metadata only where useful for provenance.

Do not preserve credentials or unnecessarily large raw envelopes.

### 9. Canonical reference

A keyword-demand measurement may not have a human-facing canonical detail page analogous to Stack Exchange or CFPB.

Do not invent one.

Use the official DataForSEO endpoint/documentation URL as the canonical source reference if that is the most honest inspectable reference under the current `SourceObservation` schema, and report this semantic difference.

### 10. Cost awareness

This is a paid API.

The collector should not accidentally generate multiple paid requests for one bounded CLI invocation.

For this slice:

- all 20–30 seeds should fit into one documented request,
- one CLI collection invocation should make one paid Live request,
- the completion report must state provider-reported request cost if returned,
- tests must not call the live API.

Do not build budgets, billing infrastructure, retries that can multiply charges, scheduling, or automated loops.

### 11. CLI

Add a bounded CLI command, e.g.:

```text
asymmetry-engine collect-keyword-demand
```

It should accept at minimum:

- database path,
- optional explicit seed-file or built-in bounded seed set if useful,
- location/language only if doing so remains simple and does not create orchestration scope.

Prefer the smallest interface necessary for the required empirical run.

### 12. Real empirical run

After tests pass and **only if valid DataForSEO credentials are available in the local environment**, run the collector against a fresh SQLite database using the fixed 20–30 seed set.

Run the exact same command a second time against the same database to verify identity deduplication.

Expected semantics:

```text
first run: returned keyword measurements inserted
second run: same identities become duplicates
```

If DataForSEO omits some seeds or returns null/no-data metrics, preserve and report that behavior rather than manufacturing values.

If credentials are not available, implementation and mocked tests may still be completed and committed, but **Spec 005 is not empirically complete**. Stop and report `BLOCKED ON CREDENTIALS` rather than fabricating a real-run result or changing source.

Do not ask Codex to register an account or obtain credentials automatically.

### 13. Inspection report

Do not commit API response corpora or generated SQLite databases.

Completion report must include one compact row per returned keyword:

```text
keyword | search_volume | competition | competition_index | cpc | low_bid | high_bid | location | language
```

Also include the monthly-search series for **5 representative keywords** chosen for variety, not commercial attractiveness.

Then provide a short factual inspection section answering only:

- how many seeds returned measurements,
- how many had non-null search volume,
- how many had non-null CPC,
- range of search volumes,
- range of CPC values,
- whether obvious monthly seasonality/volatility is visible in the five displayed series,
- whether spelling normalization changed any seed,
- provider-reported API cost,
- any surprising response semantics.

Do not rank keywords or call any of them opportunities.

## Tests

Add focused mocked tests proving at minimum:

- authentication header/request construction without leaking credentials,
- exact official endpoint,
- one bounded request for the seed set,
- US/English targeting construction,
- normalization into deterministic source/external identity,
- identity distinguishes different locations/languages,
- `observed_at` handling,
- honest handling of missing/no source occurrence timestamp,
- readable content construction,
- preservation of monthly searches and important metrics,
- clean handling of null metrics,
- clean provider/API/task-level error propagation through existing pipeline behavior,
- missing credentials fail clearly,
- second identical collection deduplicates using existing persistence semantics,
- existing Stack Exchange, CFPB, and persistence tests continue to pass.

No live network calls in automated tests.

## Explicitly out of scope

Do not implement:

- Google Ads API direct access,
- Google Trends,
- DataForSEO keyword suggestions/expansion,
- SERP scraping,
- DataForSEO Labs search intent,
- automated mapping from Stack Exchange/CFPB observations to keywords,
- cross-source matching,
- friction taxonomy,
- `DecisionSignal`,
- `DecisionProblem`,
- generic `Evidence`,
- `FrictionPattern`,
- asymmetry detection,
- evidence-strength scoring,
- independence scoring,
- commercialization distance,
- commercial-attractiveness scoring,
- opportunity ranking,
- CPC-based profitability assumptions,
- LLM calls,
- embeddings,
- clustering,
- vector database,
- time-series monitoring architecture,
- scheduled collection,
- multi-country sweeps,
- retries that can unexpectedly incur additional API cost,
- UI/web app,
- broad refactors.

Do not update README.md, ARCHITECTURE.md, ROADMAP.md, or SOURCE_REGISTRY.md merely to mirror implementation. Report contradictions instead.

## Acceptance criteria

Spec 005 is implementation-complete when:

1. A bounded DataForSEO collector uses the official v3 Google Ads Search Volume Live endpoint.
2. Credentials are externalized and never committed/logged/persisted.
3. Source metadata records vendor dependency, reuse context, metric provenance, and major semantic limitations.
4. A fixed manually selected 20–30 keyword seed set is used for the empirical slice.
5. One keyword-market measurement becomes one weak `SourceObservation` without downstream interpretation.
6. Stable identity includes enough market context to distinguish keyword/location/language measurements.
7. `content` is readable and source-faithful.
8. Important keyword metrics and monthly searches remain available in source-specific metadata.
9. No fake source event timestamp is invented without reporting why the current model forced it.
10. One CLI invocation makes at most one paid Live request for the bounded seed set.
11. Mocked automated tests cover the collector and the full suite passes.
12. No downstream scoring, matching, taxonomy, or commercialization logic is introduced.

Spec 005 is **empirically complete** only when, in addition:

13. Valid local DataForSEO credentials were available.
14. A fresh real run was completed using the fixed seed set.
15. The identical second run reconfirmed deduplication.
16. The completion report includes the full keyword manifest, five monthly series, factual summary statistics, and provider-reported request cost.
17. No real response corpus or SQLite database was committed.

If 13–16 cannot be completed because credentials are unavailable, report `BLOCKED ON CREDENTIALS` and stop. That is not permission to broaden scope or choose another source.

## Requested completion report

When finished, report:

1. Full commit SHA and message.
2. Files changed.
3. Exact DataForSEO endpoint.
4. Authentication/environment-variable strategy, without exposing values.
5. Exact seed keyword list.
6. Exact target location/language.
7. Stable source and external identity format.
8. How `occurred_at` was represented and whether this exposed architectural pressure.
9. `content` representation.
10. Preserved source-native metadata.
11. Canonical-reference strategy.
12. Test command and full result/count.
13. Whether real credentials were available.
14. If available: exact real-run CLI command, first/second run counts, provider-reported request cost, full keyword manifest, and five monthly series.
15. If unavailable: state `BLOCKED ON CREDENTIALS`; do not fabricate empirical output.
16. Any provider response behavior or source semantics that materially differed from assumptions.
17. Any architectural pressure discovered on `SourceObservation`, especially aggregate measurements, absent occurrence timestamps, market-target identity, or future time-series monitoring.
18. Any material departure from the specification and why.

Then stop.

Do not choose the next source or implement downstream interpretation. The next step is ChatGPT review of the implementation and real evidence (or credential blocker).