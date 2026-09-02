# Spec 009 — Comext physical-flow evidence slice

## Goal

Add one small, free, structurally orthogonal evidence source using Eurostat's official Comext API.

This slice should test whether the current `SourceObservation` envelope can honestly represent **physical economic flow**: goods crossing borders with product, direction, value, quantity, geography, and time dimensions.

The empirical purpose is not to build a trade dashboard. It is to test whether physical-flow evidence changes opportunity interpretation in ways that the current evidence portfolio cannot.

## Why this source / why now

Historical backtesting produced a concrete marginal-information result:

- patent growth alone created false positives such as machine tools in 2019;
- direct commitment evidence helped but was not sufficient for every case;
- physical-flow evidence strongly contradicted the machine-tool growth interpretation and exposed supply-chain/import-dependence structure in digital communications;
- trade value and quantity together can distinguish physical expansion from price-driven value changes.

Comext therefore earns implementation because it contributes a signal family not represented by the current codebase:

```text
PHYSICAL FLOW

trade value
trade quantity
origin / destination
product identity
import / export direction
partner concentration
implied unit-value pressure
```

This is an empirical slice. Do not implement disequilibrium detection, opportunity generation, semantic graphs, trade analytics infrastructure, or automated cross-source joins in Spec 009.

## First-party source position

Use Eurostat's official Comext dissemination API.

Current Eurostat documentation states that:

- Comext is the reference database for detailed international trade in goods statistics;
- Comext and Prodcom use the dedicated `https://ec.europa.eu/eurostat/api/comext/dissemination` API base;
- complete Comext datasets cannot be requested unfiltered because of their size;
- filtered subsets are supported through official Eurostat API surfaces;
- statistical data may generally be reused for commercial and non-commercial purposes with source acknowledgement, subject to dataset/country exceptions.

Relevant first-party references:

- https://ec.europa.eu/eurostat/web/international-trade-in-goods/database
- https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/comext-database
- https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/prefixed-datasets
- https://ec.europa.eu/eurostat/help/copyright-notice

No scraping is required.

## Important reuse constraint

Eurostat's copyright notice contains exceptions for some trade data, including certain declaring-country / classification combinations and non-EU country data.

For this empirical slice:

- use **Czechia as declaring country**;
- use EU/Eurostat source-native data only;
- do not include Austria as declaring country at CN8 detail;
- do not persist or redistribute unrelated non-EU declaring-country statistics merely because they are available;
- preserve Eurostat attribution information in source metadata.

Codex must re-check the current first-party copyright notice before implementation and report any material change or ambiguity.

## Empirical question

> Can a bounded Comext slice add honest physical-flow evidence to the existing observation model and expose economically meaningful change without prematurely building trade-domain abstractions?

Secondary questions for the completion report:

- Which broad Czech import categories show the largest year-over-year value increases or decreases?
- Which categories show value movement that differs materially from physical quantity movement?
- Which categories are economically large enough that movement could plausibly matter to opportunity discovery?
- Does the current observation identity handle revisions and repeated measurements honestly?
- Does Comext create pressure for explicit concept mapping between CN product categories and other source taxonomies?

Do not encode answers to these questions into the collector.

## Dataset discovery

Comext uses `DS-` prefixed datasets and the available dataflows can change.

Codex must discover and confirm from the current official Comext dataflow/metadata endpoints the exact dataset code and dimension names needed for a **detailed or aggregated trade-in-goods dataset that supports Czech declaring country, trade flow, product classification, partner, time, trade value, and a physical quantity measure**.

Do not guess a dataset code from stale examples.

Prefer the simplest current dataset that can provide broad Combined Nomenclature product categories without requiring retrieval of the complete detailed CN8 universe.

If the cleanest dataset exposes CN2 directly, use CN2.

If only finer CN detail is exposed, request a bounded official aggregation or the smallest query that can be deterministically aggregated to CN2 in memory. Do not download the entire Comext corpus.

The completion report must state:

- dataset code,
- dimensions used,
- product classification/version,
- measures used,
- exact query scope,
- and why that dataset was chosen.

## Empirical scope

Use a deliberately broad but bounded Czech snapshot so that the result is not preselected around a known success story.

Target scope:

```text
DECLARANT: Czechia (CZ)
FLOW: imports
PARTNER: world / total partner where the dataset provides it
PRODUCT: broad CN2 chapters
TIME: two adjacent complete annual periods
```

Preferred annual periods:

```text
2023
2024
```

If the selected official dataset does not expose comparable complete annual values for those years, use the latest two adjacent complete annual periods that are jointly available and explain the choice.

Do not use partial 2026 data merely because it is newer.

### Measures

Retrieve, where source-native and consistently available:

1. trade value,
2. net mass or the most comparable source-native physical quantity measure.

Do not combine incompatible supplementary units across product categories.

If net mass is unavailable for a returned category, preserve the missing state honestly rather than substituting zero.

## Observation granularity

Represent each returned **source-native measurement cell** as one `SourceObservation`.

A cell should correspond to a unique combination including at minimum:

```text
dataset
reporter / declarant
flow
partner
product code
measure
reference period
unit where required
```

Do not combine value and quantity into one observation.

Do not persist derived growth rates or implied unit values as new observations in this slice.

## Observation identity

Use deterministic identity derived from stable source dimensions, conceptually:

```text
comext:<dataset>:<reporter>:<flow>:<partner>:<product>:<measure>:<unit>:<time>
```

The exact encoding may follow repository conventions.

Do not include:

- numeric value,
- collection timestamp,
- calculated growth,
- calculated unit value

in identity.

As with the existing Eurostat slice, this means a later source revision of the same dimensional cell will collide with the current first-capture deduplication semantics.

**Do not solve historical measurement revision in Spec 009.** Report the pressure.

## Timestamps

Use collection time as `observed_at`.

Do not invent a precise event timestamp for an annual trade statistic.

Prefer `occurred_at=None` and preserve the reference period in metadata/content unless the current model already has a truthful period convention.

## `item_kind`

Use:

```text
trade_statistic
```

Do not create product-specific item kinds.

## Readable `content`

Create a concise source-faithful representation containing available fields such as:

```text
Eurostat Comext
Czechia imports
partner: world
product: 85 — Electrical machinery and equipment ...
measure: trade value
value: ...
unit: ...
period: 2024
```

For quantity cells, display the physical measure and unit.

Do not infer:

- market attractiveness,
- import shock,
- shortage,
- opportunity,
- asymmetry,
- supplier gap,
- price decline,
- domestic weakness.

Those are downstream interpretations.

## Metadata

Preserve enough source-native structure to reconstruct the meaning of the measurement, including where available:

```text
dataset code
reporter/declarant code + label
flow code + label
partner code + label
product classification
product code + label
measure code + label
unit code + label
reference period
numeric value
status / confidentiality / estimate flags
API query parameters
```

Keep the metadata source-faithful.

Do not add speculative canonical technology or market mappings in this slice.

## Missing, confidential, estimated, and revised values

Trade statistics may contain source flags or missing values.

Handle them explicitly:

- never coerce missing values to zero;
- preserve relevant source status flags;
- if a cell is absent from the API response, do not fabricate it;
- if the source returns a flagged value, preserve the flag with the observation where practical.

Tests should cover at least one missing/flagged-value behavior if the response format exposes it.

## API implementation

Use the official Comext endpoint only.

Prefer the API format that yields the smallest correct implementation within the existing repository. JSON-stat 2.0 or SDMX-CSV are both acceptable if supported by the selected dataset/query.

If reusing the small JSON-stat parsing approach from `sources/eurostat.py` is natural, do so only where the response semantics genuinely match.

Do not create a generic Eurostat/SDMX framework in this slice.

Do not add pandas or another heavy dependency solely for this connector unless standard-library parsing would be materially brittle; justify any new dependency.

The HTTP request must be bounded by explicit filters. Comext documentation explicitly disallows unfiltered complete-dataset retrieval because of dataset size.

## Source metadata

Add a stable source identity such as:

```text
eurostat:comext-physical-flow
```

Record at least:

```text
access_method: official Eurostat Comext API
access_cost: free/public
geography: EU/European trade statistics; empirical slice = Czechia
commercial_use_status: reusable with attribution subject to Eurostat exceptions
terms_reference: current Eurostat copyright notice
source_role: structural / physical economic flow
```

Interpretation caveats should include:

- trade is not identical to final consumer demand;
- gross trade value can move because of quantity, price, product mix, or exchange-rate effects;
- net mass is not economically comparable across all product types;
- broad CN2 categories can hide important subcategory divergence;
- partner=`world` hides origin concentration;
- trade does not cover pure software/services;
- revisions can occur;
- classification changes can affect longitudinal comparisons;
- one statistical cell is not one independent economic actor.

## CLI

Add a small CLI command consistent with the current collectors, for example:

```text
asymmetry-engine collect-comext --database <path>
```

The empirical dataset, country, flow, partner, product granularity, measures and years may remain fixed in this slice.

Do not build a general trade-query CLI.

## Persistence and deduplication

Reuse the existing:

- source abstraction,
- pipeline,
- SQLite schema,
- source transaction semantics,
- `(source_id, external_id)` deduplication behavior.

Do not add migrations, time-series tables, product tables, economic-entity tables, relationship tables, graph storage, or derived-measure tables in Spec 009.

Use a fresh SQLite database for the empirical run.

Run the identical command twice:

- first run should insert the bounded observation set;
- second run should demonstrate deterministic deduplication.

## Post-run empirical analysis

After implementation and the two real runs, produce a completion report that calculates **outside the persistence model** the following diagnostics from the collected observations:

### 1. Category value change

For each product category with both years available:

```text
value_growth = value_t2 / value_t1 - 1
```

Report the largest positive and negative changes, while also showing baseline value so tiny categories do not masquerade as economically important.

### 2. Value vs quantity disagreement

For categories with comparable physical quantity in both periods, identify examples where:

```text
trade value direction != quantity direction
```

or their growth magnitudes differ substantially.

The purpose is to demonstrate that value change alone can hide price/mix effects.

### 3. Simple implied value-per-mass diagnostic

Where trade value and net mass are both positive and genuinely comparable for the same category/year, the completion report may calculate:

```text
implied_value_per_mass = trade_value / net_mass
```

This is a diagnostic only.

Do **not** persist it as truth or label it as a product price. Product mix within a CN2 chapter can change substantially.

### 4. Economic interpretation

Identify 3–5 categories that appear worth further investigation and explain why using only cautious language such as:

- large physical expansion,
- large value expansion,
- value/quantity divergence,
- economically large category with unusual movement.

Do not claim a commercial opportunity without other evidence.

## Tests

Add focused tests for:

- source registration / identity,
- query construction and bounded filters,
- API response parsing,
- deterministic external identity,
- correct mapping of dimensions to observations,
- value and quantity kept as separate observations,
- period preserved without invented event timestamp,
- missing/flagged values handled honestly,
- pipeline persistence,
- second-run deduplication,
- existing tests remain green.

Mock external HTTP in unit tests.

Do not make ordinary test execution depend on live Eurostat availability.

## Non-goals

Spec 009 does **not** implement:

- opportunity detection,
- disequilibrium scoring,
- CN ↔ NACE ↔ patent ↔ OpenAlex mappings,
- partner concentration analysis,
- origin-country analysis,
- import-shock alerts,
- Prodcom joins,
- domestic production comparison,
- historical backtesting framework,
- dashboards,
- graph databases,
- knowledge graphs,
- LLM interpretation,
- autonomous agents,
- scheduled monitoring.

If the real data creates pressure for any of these, report it rather than expanding scope.

## Expected files

The exact shape should follow the repository, but likely changes include:

```text
src/asymmetry_engine/sources/comext.py
src/asymmetry_engine/cli.py
relevant source registration / pipeline wiring
tests/test_comext.py
```

Reuse existing abstractions rather than restructuring the project.

## Acceptance criteria

Spec 009 is complete when:

1. the implementation uses a current official Comext `DS-` dataset confirmed at implementation time;
2. the live empirical query is explicitly bounded to Czech imports, world/total partner, broad product categories, two complete annual periods, and the requested source-native measures;
3. source-native trade measurements are represented honestly as `SourceObservation` records;
4. deterministic identity excludes numeric values and collection timestamps;
5. value and physical quantity remain separate evidence cells;
6. missing/status semantics are not silently converted to zero;
7. the existing persistence and deduplication model is reused unchanged;
8. the same live collection run twice shows deterministic deduplication;
9. existing tests and new Comext tests pass;
10. the completion report performs the requested value/quantity diagnostics and identifies a small number of categories worth further evidence gathering;
11. no speculative economic graph, derived-opportunity model, or generic trade infrastructure is introduced.

## Stop conditions

Stop and report rather than silently changing scope if:

- the current official Comext API does not expose a bounded dataset supporting the required dimensions;
- current Eurostat reuse terms materially conflict with this commercial research use;
- Czech world-import data cannot be queried without retrieving an unreasonably large corpus;
- comparable physical quantity is unavailable at the chosen broad product granularity;
- implementation would require major schema redesign merely to store this evidence.

A failed source feasibility test is a valid result.

## Completion report

Codex should return:

1. files changed,
2. dataset/dimensions/years/measures actually used,
3. live command executed,
4. first-run insert count,
5. second-run duplicate count,
6. test result count,
7. top positive/negative value changes with baseline scale,
8. examples of value-versus-quantity disagreement,
9. 3–5 categories worth further investigation,
10. any source/API/licensing caveats,
11. any architectural pressure discovered,
12. anything deliberately left unresolved because it belongs to the next evidence slice.
