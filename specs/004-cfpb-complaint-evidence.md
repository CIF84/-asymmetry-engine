# Spec 004 — CFPB Complaint Evidence Slice

## Goal

Add a second, structurally different signal source to Asymmetry Engine using the official CFPB Consumer Complaint Database API.

The purpose is not to detect or score asymmetries yet. It is to test whether the existing `SourceObservation` abstraction survives a source whose evidence is:

- regulatory / institutional rather than community Q&A,
- complaint-driven rather than question-driven,
- structured and categorical rather than primarily narrative,
- geographically concentrated in the United States,
- evidence of realized consumer pain rather than uncertainty before a decision.

The empirical question is:

> Can the same weak observation envelope represent both an individual Stack Exchange question and an individual CFPB complaint without lying about either source?

## Current external-source reality

As of August 2026, the CFPB still provides an official Consumer Complaint Database, an Open Data API, and downloadable complaint data. The CFPB states that all complaint data it publishes is freely available for anyone to use, analyze, and build on.

The database generally updates daily.

However, an important recent policy change must shape this implementation:

> On August 14, 2026, the CFPB announced that it was ceasing discretionary publication of unverified consumer complaint narratives and associated visualizations.

Therefore this implementation MUST NOT depend on complaint narratives being available.

Historical records may still expose narrative-related fields or older narrative text depending on current API behavior, but narrative text is optional evidence only. The collector must work correctly when no narrative is present.

The current official CFPB field reference includes structured fields such as:

- date received,
- product,
- sub-product,
- issue,
- sub-issue,
- company public response,
- company,
- state,
- ZIP code,
- tags,
- submitted via,
- date sent to company,
- company response to consumer,
- timely response,
- complaint ID.

The API documentation exposes a complaint search endpoint and lookup by complaint ID.

## Why this source is useful

Stack Exchange currently gives us evidence shaped like:

```text
person
  → uncertainty / problem
  → articulated question
```

CFPB gives us evidence shaped more like:

```text
consumer
  → financial product/service interaction
  → realized problem or harm
  → formal complaint
  → company response
```

The second source therefore tests whether our source-independent observation layer can hold materially different economic evidence before we invent downstream abstractions.

## Important source limitations

The collector and source metadata must explicitly preserve the following limitations rather than attempting to correct them:

- The database is not a statistical sample of consumer experience.
- Complaints are self-selected and skew toward consumers who choose to complain to the CFPB.
- Complaints are not necessarily representative of all consumers using a product or company.
- Complaint volume must not be interpreted without context such as company size, market share, product usage, and population.
- The CFPB does not verify every allegation made in consumer-submitted complaint material.
- Complaints referred to other regulators may not appear in this database; for example, certain complaints involving smaller depository institutions are excluded.
- The source is primarily US-specific and institutionally shaped by the CFPB complaint process.
- Recent complaints may not yet represent the complete publishable set because publication follows company response or the relevant publication delay.

These limitations are source metadata / provenance, not scoring logic.

## Scope

### 1. Add a CFPB source adapter

Implement a small `CFPBCollector` or equivalently named concrete collector using the official CFPB Consumer Complaint Database API.

Do not scrape CFPB web pages.

Do not download the entire dataset.

Use a bounded API request suitable for a small empirical sample.

The collector must remain persistence-agnostic, as the Stack Exchange collector is.

### 2. Source metadata

Add CFPB `SignalSource` metadata using the existing source model.

Use a stable source ID, for example:

```text
cfpb:consumer-complaints
```

The source metadata should record at minimum:

- human-readable source name,
- official API/access identity,
- official source/data-use reference,
- commercial/reuse considerations,
- major selection biases and representativeness limitations,
- geographic / institutional scope where useful.

Do not build a new source-governance subsystem.

### 3. Normalize each complaint into `SourceObservation`

Each individual CFPB complaint should become one `SourceObservation`.

Stable external identity must derive from the CFPB complaint ID.

For example:

```text
source_id: cfpb:consumer-complaints
external_id: cfpb:complaint:<complaint_id>
item_kind: complaint
```

Use the complaint's received date as the underlying source occurrence timestamp unless the API exposes a more semantically appropriate source event timestamp and there is a clear reason to prefer it.

Use the engine collection time as `observed_at`, preserving the distinction already established in Specs 001–003.

### 4. `SourceObservation.content` must remain readable but non-interpretive

CFPB no longer reliably exposes complaint narrative text, so the collector must create a readable source-faithful representation from the structured complaint fields.

A reasonable representation is something like:

```text
Product: <product>
Sub-product: <sub-product>
Issue: <issue>
Sub-issue: <sub-issue>
Company: <company>
Company response: <company response to consumer>
```

Exact formatting is a local implementation detail.

Requirements:

- `content` must be meaningful enough for human inspection without opening raw JSON,
- it must be composed from source-native values,
- it must not summarize, classify, infer harm, infer intent, assign severity, or create a product opportunity,
- missing source fields should be omitted or handled cleanly rather than rendered as misleading text,
- historical narrative text, if present in the API response, may be preserved in source-specific metadata and/or appended in a clearly source-faithful way, but the collector MUST NOT require it.

Do not change the generic `SourceObservation` schema solely because CFPB is structured.

### 5. Preserve source-native metadata

Preserve useful source-native fields in observation metadata, including where available:

- product,
- sub-product,
- issue,
- sub-issue,
- company,
- company public response,
- company response to consumer,
- timely response,
- state,
- ZIP code,
- tags,
- submitted via,
- date sent to company,
- any narrative field if still returned,
- any additional small source-native field that is directly useful for provenance or inspection.

Do not create generic domain fields for these values yet.

### 6. Canonical reference

Each observation should contain a stable inspectable reference.

Prefer an official CFPB complaint-detail URL if the API exposes or documents one cleanly.

If a stable human-facing detail URL is not reliably available, use a deterministic official CFPB API resource/reference based on complaint ID rather than inventing an unofficial URL.

The completion report should state exactly what canonical-reference strategy was chosen.

### 7. Identity and deduplication

Reuse the existing persistence behavior unchanged:

```text
UNIQUE(source_id, external_id)
```

A second collection of the same bounded complaint set should report duplicates rather than insert new rows.

Do not add content-hash dedupe, fuzzy dedupe, cross-source dedupe, or version history.

### 8. Bounded real sample

After tests pass, collect a real bounded sample of **75 CFPB complaints** into a fresh SQLite database.

Prefer a deterministic recent-sample strategy supported by the official API, such as a documented descending received/created-date sort.

The objective is inspection, not completeness or representativeness.

Run the exact same collection command a second time against the same database to reconfirm identity-based deduplication.

If the official API's current semantics prevent exactly 75 records in one request, choose the smallest reasonable bounded implementation and report the difference rather than adding crawler/pagination architecture.

### 9. Produce an inspection manifest

Do not commit the real complaint corpus or the generated SQLite database.

The completion report must contain a compact manifest of the collected sample with one row per complaint containing:

```text
external_id | date_received | product | sub_product | issue | sub_issue | company | state | company_response | timely
```

Use compact placeholders for missing values.

Also provide **10 representative stored observations**, chosen for variety rather than presumed commercial quality, containing:

- external identity,
- source occurrence date,
- readable `content`, or a concise excerpt if long,
- product / sub-product,
- issue / sub-issue,
- company,
- company response,
- state if available,
- canonical reference,
- whether narrative text was present in the API record.

Do not classify the examples as opportunities.

## Tests

Add focused automated tests using fixtures/mocks rather than live CFPB calls.

Tests should prove at minimum:

- bounded official API request construction,
- normalization of complaint ID into stable external identity,
- date normalization,
- readable non-interpretive content construction from structured fields,
- clean handling of missing optional fields,
- clean handling of absent narrative text,
- preservation of important CFPB metadata,
- source metadata includes the major selection-bias / representativeness caveat,
- collector/API failure is surfaced cleanly through the existing pipeline behavior,
- existing Stack Exchange and persistence tests continue to pass,
- second identical collection is deduplicated by the existing source/external identity rule.

Do not use a live CFPB request in automated tests.

## Important semantics

### A complaint is evidence, not truth

Do not encode complaint allegations as verified facts.

The observation means approximately:

> The CFPB published a complaint record with these source-native characteristics.

It does not mean:

> The alleged harm definitely occurred exactly as claimed.

### Complaint frequency is not market prevalence

Do not infer in code that more complaints means proportionally more harm or a larger opportunity.

The CFPB explicitly warns that complaint counts must be interpreted in context and that the database is not representative of the whole consumer market.

### Structured evidence is still evidence

Do not force CFPB into Stack Exchange's textual shape.

The absence of narrative text is not an implementation failure. This is part of the architectural experiment.

### Geography is metadata, not exclusion

CFPB is US-specific. Preserve that fact.

Do not encode a rule that US-specific evidence is commercially unattractive or should be discarded.

Commercialization distance and market transferability remain downstream hypotheses.

### No downstream interpretation yet

Do not introduce:

- friction categories,
- `FrictionPattern`,
- `DecisionSignal`,
- `DecisionProblem`,
- generic `Evidence`,
- asymmetry detection,
- severity,
- opportunity quality,
- commercial potential,
- commercialization distance,
- monetization mechanism.

The question for this slice is whether the observation abstraction survives the source.

## Explicitly out of scope

Do not implement:

- FCA or another new source,
- Google Ads / search demand,
- Google Trends,
- Reddit or social scraping,
- LLM calls,
- narrative classification,
- clustering,
- embeddings,
- vector database,
- cross-source matching,
- complaint-volume normalization,
- company market-share enrichment,
- demographic normalization,
- scoring,
- Asymmetry Strength,
- Commercial Attractiveness,
- Commercialization Distance,
- product generation,
- workflow generation,
- agent orchestration,
- scheduling,
- continuous monitoring,
- observation version history,
- migrations framework,
- UI/web app,
- broad architecture refactors.

Do not update README.md, ARCHITECTURE.md, ROADMAP.md, or SOURCE_REGISTRY.md merely to mirror implementation unless a genuine contradiction is discovered. Report contradictions instead of silently expanding scope.

## Acceptance criteria

Spec 004 is complete when:

1. A CFPB collector uses the official Consumer Complaint Database API without scraping.
2. CFPB source metadata records the official access/reuse context and major source biases.
3. Each complaint becomes one weak `SourceObservation` with stable complaint-ID identity.
4. `content` is readable and source-faithful even when no narrative exists.
5. Important CFPB fields remain available in source-specific metadata.
6. Narrative publication is treated as optional / non-required given the August 2026 policy change.
7. Existing `SourceObservation` schema remains unchanged unless Codex finds a genuine unavoidable constraint and reports it first.
8. Existing SQLite identity/dedup semantics remain unchanged.
9. Automated tests cover the new collector and the full suite passes.
10. A fresh real run collects a bounded sample of 75 CFPB complaints.
11. Running the same collection again inserts zero duplicate identities and reports the duplicate count correctly.
12. The completion report contains the requested 75-record manifest and 10 representative observations.
13. No real complaint corpus or SQLite database is committed to GitHub.
14. No downstream interpretation, scoring, classification, or commercialization logic is introduced.

## Requested completion report

When finished, report:

1. Full commit SHA and commit message.
2. Files changed.
3. Official CFPB endpoint / API mechanism used.
4. Exact bounded-request strategy and sort/order semantics.
5. Source metadata created, including the key selection-bias wording.
6. Exact stable identity format.
7. Representation chosen for `SourceObservation.content`.
8. Canonical-reference strategy.
9. Which source-native fields are preserved in metadata.
10. Current observed API behavior around complaint narratives, explicitly noting whether narrative text appeared in the real 75-record sample.
11. Test command and result/count.
12. Exact CLI command for the fresh 75-record real run.
13. First-run fetched/inserted/duplicate counts.
14. Second-run fetched/inserted/duplicate counts.
15. Ten representative stored observations with the requested fields.
16. The complete compact 75-complaint inspection manifest:

```text
external_id | date_received | product | sub_product | issue | sub_issue | company | state | company_response | timely
```

17. Any API behavior, field semantics, source restrictions, or data-shape surprises that differed materially from assumptions.
18. Any architectural pressure discovered on `SourceObservation`, particularly whether structured complaint evidence fits naturally or exposes a real limitation.
19. Any material departure from this specification and why.

Then stop.

Do not choose the next source or implement downstream analysis. The next step is ChatGPT review of the implementation and real CFPB evidence.