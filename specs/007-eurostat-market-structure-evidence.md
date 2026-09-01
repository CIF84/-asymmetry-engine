# Spec 007 — Eurostat market-structure evidence slice

## Goal

Add one small, free, structurally different evidence source using Eurostat’s official Statistics API and the current Structural Business Statistics dataset `sbs_ovw_act`.

This slice should test whether the existing weak `SourceObservation` envelope can honestly represent **market-structure / denominator evidence**: the size and economic weight of business sectors, rather than questions, complaints, searches, or procurement notices.

This is an empirical slice, not a market-sizing product.

## Why this source / why now

The project has already observed materially different economic signals:

- Stack Exchange — articulated individual decision friction,
- CFPB — realised consumer financial pain,
- TED — institutional procurement demand and explicit budgets,
- DataForSEO — search-demand/commercial-intent adapter implemented, but no real paid run yet.

Eurostat adds a new signal family:

> the underlying economic structure in which a candidate problem or demand exists.

That matters because an observed friction can be real but economically tiny, while another may sit inside a large, fragmented, high-value sector. Market-context evidence may eventually help distinguish those cases without pretending that market size itself proves an information asymmetry.

Eurostat describes Structural Business Statistics (SBS) as providing a detailed picture of the structure, economic activity and performance of European businesses. The current dataset `sbs_ovw_act` is “Enterprises by detailed NACE Rev. 2 activity and special aggregates”.

Current first-party Eurostat documentation also states that its Statistics API:

- is open for public use,
- provides REST access,
- returns JSON-stat 2.0,
- supports filtered subsets of datasets,
- and is part of Eurostat’s official programmatic data-access surface.

Relevant first-party references:

- https://ec.europa.eu/eurostat/web/structural-business-statistics
- https://ec.europa.eu/eurostat/web/products-datasets/-/sbs_ovw_act
- https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started
- https://ec.europa.eu/eurostat/help/copyright-notice

No scraping is required.

## Empirical question

> Can the same weak observation envelope represent official statistical measurements of market structure without pretending that a statistical cell is the same kind of evidence as a question, complaint, procurement notice, or search measurement?

Secondary questions to inspect after the real run:

- How economically concentrated is Czech business activity across broad sectors?
- Which broad sectors combine many enterprises with substantial economic value?
- Do the measurements provide useful denominator/context evidence that could later qualify friction or demand signals?
- Does this source expose a materially different persistence/identity problem because Eurostat values can be revised while the dimensional identity remains the same?

Do not answer these questions in code. The implementation only needs to preserve the source evidence well enough for the completion report to inspect them.

## Dataset

Use the current Eurostat Structural Business Statistics dataset:

`sbs_ovw_act`

Codex must confirm from current official Eurostat metadata/API responses the exact dimension names and indicator codes used by this dataset rather than guessing them from this specification.

The empirical slice should use **Czechia (`CZ`) only** and broad NACE Rev. 2 section-level activities rather than detailed classes/divisions.

For each available broad business-economy section, retrieve these source-native measures where the dataset exposes them cleanly:

1. number of enterprises,
2. number of persons employed,
3. net turnover,
4. value added.

If one of those concepts is represented by a slightly different current Eurostat variable name/code, use the current source-native equivalent and report it exactly.

Do not derive ratios, per-enterprise values, growth rates, rankings, or synthetic market-size metrics in the collector.

## Time scope

Use **reference year 2023** for this empirical slice, provided the current official dataset exposes 2023 for the required Czech measures.

If a required measure is genuinely unavailable for 2023, Codex may use the latest earlier year for which the requested Czech section-level measures are jointly available, but must:

- verify this from the live API/metadata,
- use one common reference year for the empirical slice,
- state the chosen year and reason in the completion report,
- and not build dynamic “latest year” discovery infrastructure merely for this experiment.

The purpose is a deterministic empirical snapshot, not a continuously updating Eurostat client.

## API

Use Eurostat’s official Statistics API / JSON-stat 2.0 endpoint for dataset `sbs_ovw_act`.

Use anonymous/public access only.

Prefer one bounded HTTP request containing only the dimensions required for this slice. If Eurostat’s API shape makes a small number of requests materially simpler or more reliable, keep the total request count minimal and explain the reason in the completion report.

Do not download the entire unfiltered dataset.

Do not use a third-party Eurostat mirror or DBnomics as the production source.

## Source metadata

Add a `SignalSource` for Eurostat Structural Business Statistics with a stable identity such as:

`eurostat:sbs-market-structure`

Record at least:

- access method: official Eurostat Statistics API,
- access cost: free/public API,
- dataset code: `sbs_ovw_act`,
- terms/reuse reference,
- geography: European statistics; empirical run scoped to Czechia,
- evidence semantics: official aggregate market-structure measurement, not individual demand or friction,
- important selection/interpretation caveats:
  - SBS covers the defined business economy / market producers rather than every economic activity,
  - statistical definitions and NACE coverage matter,
  - values can be revised after first publication,
  - confidentiality/suppression can create missing cells,
  - monetary variables may use dataset-specific units/scales,
  - a large sector is not evidence of an information asymmetry,
  - one statistical cell is not an independent human or firm-level observation.

Do not create a generic statistical-source metadata subsystem.

## Observation granularity

Represent each returned **source-native statistical cell** as one `SourceObservation`.

A cell should correspond to a unique combination of the dimensions that define the measurement, including at minimum:

- dataset,
- geography,
- NACE activity,
- measure/indicator,
- reference year,
- and any unit dimension necessary to distinguish the value honestly.

Do not combine several indicators into one synthetic observation solely to reduce row count.

Do not split one source-native value into multiple observations.

## Observation identity

Use deterministic identity derived only from stable source dimensions, for example conceptually:

`eurostat:sbs_ovw_act:<geo>:<nace>:<indicator>:<unit>:<time>`

The exact encoding may follow existing project conventions, but it must be deterministic and collision-resistant within this dataset.

Do not include the measured numeric value or collection timestamp in identity.

This intentionally means that if Eurostat later revises the same dimensional cell, the current repository’s first-capture deduplication semantics would treat it as the same identity. **Do not fix that limitation in Spec 007.** Report it as architectural pressure if the real source makes it material.

Keep the existing repository deduplication semantics unchanged.

## Timestamps

Use collection time as `observed_at`.

For `occurred_at`, do **not** invent a precise datetime from an annual reference period.

Prefer `occurred_at=None` unless the existing domain model has an already-established honest convention for year-only statistical periods. Preserve the source reference year explicitly in metadata and readable content.

This is deliberate: an annual statistical reference period is not an event timestamp.

## `item_kind`

Use:

`market_statistic`

Do not create indicator-specific item kinds.

## Readable `content`

`SourceObservation.content` should be a concise, readable, source-faithful representation of the statistical cell.

Include available values such as:

- dataset / statistic family,
- geography,
- NACE activity code and label if available from source metadata,
- measure/indicator code and label if practical,
- value,
- unit,
- reference year,
- observation/status flag where relevant.

Do not infer market attractiveness, fragmentation, opportunity, asymmetry, growth, commercial value, or any downstream interpretation.

Do not silently rescale monetary values. If Eurostat reports a value in millions of euro or another source-native unit, preserve and display that unit honestly.

## Metadata

Preserve useful source-native evidence needed to reconstruct the meaning of the cell, including where available:

- dataset code,
- geo code,
- NACE code,
- measure/indicator code,
- unit code,
- reference year,
- numeric value,
- observation/status flags,
- source labels/descriptions used for readable output,
- API endpoint/query parameters sufficient to identify the source slice.

Keep metadata source-faithful. Do not create downstream concepts such as `market_size`, `sector_score`, `Asymmetry`, `commercialisation_distance`, or `DecisionProblem`.

## Missing / suppressed data

Eurostat statistical data can contain unavailable, confidential, provisional, estimated, or otherwise flagged cells.

Handle source-native missing values and status flags explicitly and honestly.

Do not coerce missing/suppressed values to zero.

For this bounded slice, it is acceptable either to:

- persist a returned flagged/missing cell with no numeric value if that is the natural JSON-stat representation, or
- omit cells that Eurostat does not return at all.

Whichever behavior follows naturally from the API response must be documented in the completion report and covered by tests.

## API / JSON-stat parsing constraints

Implement only the minimum JSON-stat parsing needed for this dataset and slice.

Tests must demonstrate that multidimensional indexes are mapped to the correct dimension combinations rather than assuming response-array position manually without reference to JSON-stat dimension metadata.

Do not introduce a generic JSON-stat framework unless the smallest correct implementation naturally produces one tiny reusable helper.

Do not add pandas, pyjstat, or another dependency solely for this slice unless the existing standard-library approach would be materially brittle; if adding a dependency, justify it in the completion report.

## CLI

Add a small CLI command consistent with existing collectors, for example:

`asymmetry-engine collect-eurostat --database <path>`

The dataset, geography, measures and reference year may remain fixed for this empirical slice.

Do not build a generic Eurostat query CLI.

## Persistence and deduplication

Reuse the existing pipeline, repository, SQLite schema, source transaction semantics, and `(source_id, external_id)` deduplication behavior.

Do not add migrations, time-series tables, statistical cubes, sector tables, aggregation tables, or cross-source joins.

Use a fresh SQLite database for the empirical run.

Run the identical collection command twice:

- first run should insert the retrieved cells,
- second run should demonstrate deduplication for the same dimensional identities.

If Eurostat changes/revises data between the two immediate calls, report what happened honestly rather than adding versioning infrastructure.

## Tests

Use mocked Eurostat JSON-stat responses for automated tests. No live Eurostat request should be required by the test suite.

Tests should cover at least:

- official Eurostat endpoint / dataset selection,
- Czech-only empirical scope,
- fixed reference year / chosen measures,
- bounded filtered request rather than full dataset download,
- correct JSON-stat multidimensional index decoding,
- stable external identity from source dimensions,
- measured value excluded from identity,
- `occurred_at` year-only semantics handled honestly,
- collection time → `observed_at`,
- readable content,
- preservation of important metadata and status flags,
- source-native units preserved without silent rescaling,
- missing/suppressed optional value behavior,
- API/network/malformed-response failure handling,
- existing pipeline deduplication behavior.

Run the full test suite.

## Real run and completion report

After tests pass, perform one real bounded run against the official Eurostat API using a fresh database, then immediately repeat the identical command.

The completion report must include:

1. commit SHA and message,
2. files changed,
3. exact official endpoint / URL pattern used,
4. exact dataset code,
5. exact dimensions/query parameters,
6. exact indicator/measure codes and their source-native meanings,
7. exact unit codes and meanings,
8. chosen reference year and why,
9. NACE level / activities represented,
10. observation identity semantics,
11. timestamp semantics,
12. first-run fetched / inserted / duplicate counts,
13. second-run fetched / inserted / duplicate counts,
14. full test result,
15. a compact full manifest of the stored cells with columns such as:

   `external_id | geo | nace | indicator | value | unit | year | status`

16. simple empirical summaries computed only for the report, not persisted as domain objects:
   - count of represented NACE sections,
   - count of available vs missing/suppressed values by measure,
   - top five Czech sectors by number of enterprises,
   - top five by persons employed,
   - top five by net turnover where comparable,
   - top five by value added where comparable,
17. five to ten representative stored observations with readable `content`,
18. obvious statistical-definition, concentration, unit, missing-data, or sampling caveats,
19. whether the weak observation envelope felt honest or strained for aggregate statistical measurements,
20. whether revision/time-series semantics expose material architectural pressure,
21. any material departure from this spec.

Do not commit the real API response corpus or SQLite database.

## Explicitly out of scope

Do **not** implement:

- market opportunity scoring,
- market sizing beyond preserving source-native measurements,
- growth calculations,
- year-over-year comparisons,
- ratios such as turnover per enterprise,
- sector attractiveness rankings in application code,
- cross-country comparison logic,
- detailed NACE taxonomy expansion beyond source labels required for readable evidence,
- time-series history infrastructure,
- revised-observation versioning,
- cross-source matching,
- TED/Stack Exchange/CFPB joins,
- asymmetry detection,
- LLM classification,
- clustering,
- embeddings,
- commercialization logic,
- alerts/scheduling,
- UI,
- generic source orchestration,
- a generic statistical-cube abstraction,
- changes to `SourceObservation` merely to accommodate anticipated future analytics.

## Acceptance criteria

The slice passes when:

- the official Eurostat public API is used,
- the current `sbs_ovw_act` dataset is queried for one bounded Czech market-structure slice,
- broad NACE section-level measurements for enterprises, employment, turnover and value added are preserved where available,
- each source-native statistical cell is represented honestly as one `SourceObservation`,
- annual-period semantics are not fabricated into precise occurrence timestamps,
- units and source flags are preserved,
- existing persistence and dedupe semantics are reused unchanged,
- mocked tests cover the critical JSON-stat and identity contract and the full suite passes,
- the real run and immediate repeat are completed,
- the requested empirical report is produced,
- no downstream market-scoring/detection/commercialization architecture is introduced.

After the completion report, stop. Do not begin another source or phase.
