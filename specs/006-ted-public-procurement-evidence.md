# Spec 006 — TED public procurement evidence slice

## Goal

Add one small, free, structurally different evidence source using the official EU Tenders Electronic Daily (TED) Search API.

This slice should test whether the existing weak `SourceObservation` envelope can honestly represent **institutional demand**: organisations explicitly procuring goods/services, often with classifications, buyers, geography, deadlines and monetary values.

This is an empirical slice, not a procurement analytics product.

## Why this source / why now

The project has already observed:

- Stack Exchange — articulated individual decision friction,
- CFPB — realised consumer financial pain,
- DataForSEO — a search-demand adapter, but no real paid run yet.

TED adds a materially different economic signal:

> organisations allocating budgets and publishing procurement demand.

This matters because Asymmetry Engine must not assume that exploitable asymmetries only originate in consumers explicitly asking questions or filing complaints.

Current first-party TED documentation states that:

- published procurement notices are available through the official TED Search API,
- the Search API supports analysis and reuse,
- the Search API does not require authentication,
- commercial organisations use TED data in added-value platforms for vendors and buyers,
- the API supports bounded pagination and explicit field selection.

Relevant first-party references:

- https://docs.ted.europa.eu/api/latest/search.html
- https://docs.ted.europa.eu/ODS/latest/reuse/search-api.html
- https://docs.ted.europa.eu/ODS/latest/reuse/field-list.html
- https://data.ted.europa.eu/

No scraping is required.

## Empirical question

> Can the same weak observation envelope represent a published procurement notice without pretending that institutional demand is the same kind of evidence as a question, complaint, or search measurement?

Secondary questions to inspect after the real run:

- Does procurement data expose economically useful problem categories directly enough to justify future exploration?
- Are monetary values present often enough to provide useful magnitude evidence?
- How concentrated are recent notices by buyer, CPV/category, geography, or notice type?
- Does a Czech-focused slice reveal opportunities with shorter commercialisation distance than US-centric evidence?

Do not answer these questions in code. The implementation only needs to preserve the source evidence well enough for the completion report to inspect them.

## Scope

Implement one collector using the official TED Search API v3 endpoint for published notices:

`POST https://api.ted.europa.eu/v3/notices/search`

Use anonymous access only. Do not require an API key.

The collector must make one bounded Search API request per CLI invocation.

### Real empirical slice

Retrieve **75 recent Czech Republic-associated published procurement notices**.

Prefer a source-native filter that represents either:

1. place of performance in Czechia, or
2. buyer country in Czechia,

with place of performance preferred if the official Search API supports it cleanly.

Codex should confirm the exact TED expert-query field names and syntax from current official documentation rather than guessing them.

Use a deterministic newest/recent ordering supported by TED so the identical command returns the same sample closely enough for the immediate deduplication check. If TED publication timing makes an exact repeated 75-row sample impossible, report the difference honestly rather than adding snapshot infrastructure.

No pagination or scroll mode is needed for this slice. Request exactly one page with a maximum of 75 notices.

## Source metadata

Add a `SignalSource` for TED public procurement with a stable source identity such as:

`ted:public-procurement`

Record at least:

- access method: official TED Search API,
- access cost: free / anonymous Search API,
- terms/reuse reference,
- geography: EU / European procurement, with this empirical run scoped to Czechia,
- evidence semantics: institutional procurement demand, not consumer demand,
- important selection biases:
  - only procurement that is published through TED,
  - thresholds/legal publication obligations affect coverage,
  - notice publication is not equivalent to completed purchase,
  - notice count is not independent demand count,
  - one procurement procedure may produce multiple notices/lots/updates,
  - monetary values can be missing, estimated, changed, or represented at different procedure/lot levels.

Do not create a generic legal/licensing subsystem.

## Observation identity

Each returned published notice must produce one `SourceObservation`.

Use the most stable source-native published notice identifier exposed by TED, preferably publication number / notice identifier as documented by the Search API.

Identity should have the form:

`ted:notice:<stable-source-id>`

Do not use title, buyer name, row position, or a locally generated UUID as identity.

If TED exposes version/revision semantics that materially affect identity, preserve the source-native identifiers in metadata and choose the simplest identity that prevents accidental collisions in this bounded experiment. Explain the choice in the completion report.

Keep the existing repository deduplication semantics unchanged.

## Timestamps

Use the TED publication date as `occurred_at` when available and source-native.

Use collection time as `observed_at`.

Do not invent a procurement occurrence timestamp from a deadline, award date, or other lifecycle field.

## `item_kind`

Use:

`procurement_notice`

Do not create subtypes in the domain model for this slice.

## Readable `content`

`SourceObservation.content` should be a readable, source-faithful projection of important returned fields.

Include available values such as:

- notice title,
- buyer / contracting authority,
- notice or form type,
- main procurement / CPV classification,
- place of performance / country,
- estimated or awarded value and currency if returned at a meaningful notice/procedure level,
- submission/tender deadline if available.

Omit unavailable fields rather than inventing values.

Do not summarise, classify, infer intent, infer opportunity, estimate missing spend, or translate the notice using an LLM.

If a title is multilingual or represented in a source-specific structure, use the simplest deterministic readable representation and preserve the relevant source-native form in metadata when practical.

## Metadata

Preserve useful source-native evidence returned by the selected Search API fields, including where available:

- publication / notice identifier,
- publication date,
- notice/form type,
- title,
- buyer name,
- buyer country,
- place of performance / NUTS,
- CPV/main classification,
- procedure type,
- estimated value,
- award value,
- currency,
- tender/submission deadline,
- links/URLs supplied by TED,
- any notice lifecycle/version identifier needed to interpret identity.

Keep metadata source-faithful. Do not create downstream concepts such as `DecisionProblem`, `Asymmetry`, `market_size`, `opportunity_score`, or `commercialisation_distance` here.

## Canonical URL

Use a TED-provided human-facing notice URL when the Search API returns one.

If the response provides multiple language/format URLs, choose one deterministic human-readable TED URL and preserve the available alternatives in metadata if simple.

Do not invent a URL pattern when TED already supplies canonical links.

## API request constraints

Use the official Search API only.

The request must:

- be one POST request per CLI invocation,
- request at most 75 notices,
- use pagination mode rather than scroll/iteration,
- request only the fields required by this experiment,
- use a Czech Republic-associated expert query,
- use deterministic recent ordering where supported,
- not download full XML notice bodies,
- not invoke the Visualisation API,
- not crawl notice pages,
- not retry through alternative endpoints.

If the first-party API requires a specific request header or documented client identification, follow it.

## CLI

Add a small CLI command consistent with existing collectors, for example:

`asymmetry-engine collect-ted --database <path>`

The empirical query and sample size may remain fixed for this slice unless a tiny local parameter improves testing without expanding scope.

Do not build a generic query-builder CLI.

## Persistence and deduplication

Reuse the existing pipeline, repository, SQLite schema, source transaction semantics, and `(source_id, external_id)` deduplication behavior.

Do not add migrations, time-series storage, aggregation tables, procurement-specific tables, or cross-source joins.

Use a fresh SQLite database for the empirical run.

Run the identical collection command twice:

- first run should insert the retrieved observations,
- second run should demonstrate deduplication for the same returned notices.

If the live source changes between the two calls, report exact fetched/inserted/duplicate counts rather than forcing an artificial result.

## Tests

Use mocked TED responses for automated tests. No live TED request should be required by the test suite.

Tests should cover at least:

- official endpoint and POST construction,
- exactly one API request per collector invocation,
- bounded limit of 75,
- Czech-focused expert query / target constraint,
- explicit selected fields rather than full-notice download,
- stable external identity,
- publication date → `occurred_at`,
- collection time → `observed_at`,
- readable content from returned source fields,
- preservation of important metadata,
- missing optional values,
- canonical TED URL selection,
- source metadata caveats,
- API-level failure handling,
- existing pipeline deduplication behavior.

Run the full test suite.

## Real run and completion report

After tests pass, perform one real bounded run against the official TED Search API using a fresh database, then immediately repeat the identical command.

The completion report must include:

1. commit SHA and message,
2. files changed,
3. exact official endpoint,
4. exact TED expert query used,
5. exact field list requested,
6. sample scope and ordering semantics,
7. identity semantics,
8. timestamp semantics,
9. first-run fetched / inserted / duplicate counts,
10. second-run fetched / inserted / duplicate counts,
11. full test result,
12. a 75-row manifest where available with compact columns such as:

   `external_id | publication_date | title | buyer | notice_type | CPV | value | currency | canonical_url`

13. ten representative observations with their readable `content`,
14. simple empirical distributions computed only for the report, not persisted as new domain objects:
   - top buyers,
   - top notice/form types,
   - top CPV/main classifications,
   - count with usable monetary value,
   - minimum/median/maximum usable monetary value where values are comparable without currency conversion,
15. obvious concentration or sampling artefacts,
16. whether the weak observation envelope felt honest or strained for procurement evidence,
17. any material departure from this spec.

If multiple currencies prevent a meaningful aggregate value summary, report values by currency or omit the aggregate rather than converting currencies or fabricating comparability.

Do not commit the real response corpus or SQLite database.

## Explicitly out of scope

Do **not** implement:

- procurement opportunity scoring,
- tender recommendation,
- supplier matching,
- CPV taxonomy expansion beyond preserving returned source values,
- lot-level relational modelling,
- buyer profiles,
- historical procurement analytics,
- pagination/scroll crawling,
- full XML notice ingestion,
- document/PDF parsing,
- LLM classification or summarisation,
- embeddings,
- clustering,
- cross-source matching,
- market sizing,
- currency conversion,
- commercialisation logic,
- alerts/scheduling,
- UI,
- generic source orchestration,
- changes to `SourceObservation` merely to accommodate anticipated future procurement analytics.

## Acceptance criteria

The slice passes when:

- the official anonymous TED Search API is used,
- one bounded Czech-focused request returns up to 75 published notices,
- each notice is represented as one source-faithful `SourceObservation`,
- stable TED identity and publication timestamps are preserved honestly,
- existing persistence and dedupe semantics are reused unchanged,
- mocked tests cover the critical contract and the full suite passes,
- the real run and immediate repeat are completed,
- the requested empirical report is produced,
- no downstream asymmetry/detection/commercialisation architecture is introduced.

After the completion report, stop. Do not begin another source or phase.
