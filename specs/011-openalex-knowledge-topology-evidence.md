# Spec 011 — OpenAlex knowledge-topology evidence slice

## Goal

Add one small OpenAlex evidence slice to test whether Asymmetry Engine can honestly represent **research activity plus fine-grained semantic topic structure** without prematurely building a knowledge graph, ontology framework, or generic research-intelligence system.

This slice is specifically intended to test the empirical pressure discovered during historical backtesting:

> broad technology categories can hide economically important capability/application intersections, and research topology may be more informative than raw publication counts.

The implementation should preserve enough source-native evidence to inspect research velocity and topic structure after the run. It must not infer commercial opportunities in code.

## Why this source / why now

The project now has evidence sources for:

- articulated friction — Stack Exchange,
- realized pain — CFPB,
- institutional demand and budgets — TED,
- market structure — Eurostat SBS,
- search-demand adapter — DataForSEO,
- supplier pricing — Azure Retail Prices,
- physical trade flow — Comext.

Comext Specs 009–010 also established that hierarchical decomposition materially changes economic interpretation. The remaining major evidence family already supported by historical research is **knowledge formation and semantic decomposition**.

OpenAlex contributes something structurally different:

```text
research works
    ↓
source-native topics
    ↓
subfields / fields / domains
    ↓
changes in research activity
    ↓
possible cross-topic / cross-domain convergence
```

The purpose of Spec 011 is not to prove that publication growth predicts commercial opportunity. It is to determine whether OpenAlex can become a reliable substrate for later knowledge-topology reasoning.

## Empirical questions

Primary question:

> Can the current weak observation model represent historical research measurements and topic semantics honestly enough to inspect knowledge velocity and semantic decomposition?

Secondary questions for the completion report:

1. Does fine-grained topic structure reveal information hidden by broad field-level counts?
2. Can a small historical slice reproduce the previously observed distinction between broad AI/computing growth and more specific hardware/AI intersections?
3. Which source-native relationships are truly provided by OpenAlex, and which would require our own later inference?
4. Does this source create new pressure for measurement-history, semantic mapping, or model-version provenance?
5. Is OpenAlex valuable primarily as a velocity source, a semantic-resolution source, a topology source, or some combination?

Do not answer these questions inside production logic.

## Source and access

Use the current official OpenAlex API only.

Codex must verify current first-party API documentation before implementation, including:

- supported filtering/grouping required by this slice,
- authentication/API-key requirements if any,
- rate limits or polite-pool guidance,
- current terms/reuse position,
- source-native topic hierarchy semantics,
- any known caveats about topic assignment/model revisions.

Do not scrape the OpenAlex website.

Do not use third-party mirrors.

If the current API requires an API key for reasonable use, support an environment variable but do not commit credentials.

## Historical cutoff and leakage discipline

This slice intentionally examines historical works around the pre-2020 period because the project has already used 2019 as a backtest boundary.

Use publication years:

```text
2017
2018
2019
```

The completion report must explicitly distinguish:

### Data-time leakage

Using works, citations, publication dates, or metadata that did not exist by the historical cutoff to claim that the Engine could have known them then.

This is not acceptable for historical predictive claims.

### Model-time leakage

Applying OpenAlex's current topic-classification model retrospectively to works published in 2017–2019.

This may be acceptable for the narrower empirical question:

> did the historical corpus contain semantic structure that a modern classifier can expose?

But it must not be represented as a classification that was actually available in 2019.

Store/report this caveat explicitly.

## Empirical domain

Use a deliberately bounded **AI/computing knowledge slice**.

The slice should be anchored in current OpenAlex source-native topic/subfield metadata, not hand-created keyword buckets.

Codex should use current API metadata to identify a small set of relevant fine-grained topics representing at least these conceptual areas where source-native topics exist cleanly:

```text
artificial intelligence / machine learning
neural networks / deep learning
computer vision or natural-language processing
hardware / VLSI / FPGA / computing architecture
memory / neuromorphic / in-memory computing where available
```

Do not force an exact one-to-one match if OpenAlex's current topic system names or scopes differ.

Select approximately **6–12 source-native topics** total. The goal is a compact empirical slice, not broad AI coverage.

The completion report must list the selected topic IDs, labels and hierarchy placement exactly as returned by OpenAlex.

## Measurement design

For each selected topic and each year 2017–2019, obtain a source-faithful annual research-activity measurement.

Preferred primary measurement:

```text
works_count
```

If the current OpenAlex API exposes a reliable grouped count directly, use that rather than downloading every work.

If an API response supplies other cheap source-native counts useful for interpretation, such as cited-by count, they may be preserved as metadata but should not expand the scope materially.

Do not build citation-network analysis in this slice.

## Observation granularity

Represent each source-native annual topic measurement as one `SourceObservation`.

Conceptually:

```text
OpenAlex topic X
× publication year Y
× works_count
= one observation
```

Use:

```text
item_kind=research_statistic
```

Do not persist one observation per individual academic work unless the current API makes grouped counts impossible and Codex can justify the additional volume.

## Observation identity

Use deterministic identity derived from stable source dimensions, conceptually:

```text
openalex:<topic_id>:works_count:<year>
```

Do not include the measured count or collection timestamp in identity.

This intentionally leaves the same revision-history limitation already observed with Eurostat/Comext: if OpenAlex later changes historical counts or classification results for the same topic/year identity, current first-capture deduplication would suppress the revised value.

Do not fix that in Spec 011.

## Timestamps

Use collection time as `observed_at`.

Use `occurred_at=None` for annual count measurements. Do not fabricate a date such as 31 December merely to populate an event timestamp.

Preserve publication year explicitly in metadata/content.

## Content

`SourceObservation.content` should be concise and readable. Include where available:

```text
source
OpenAlex topic ID
OpenAlex topic label
subfield
field
domain
publication year
works count
```

Do not infer:

```text
emerging technology
commercial opportunity
knowledge convergence
market attractiveness
asymmetry
```

Those are downstream interpretations.

## Metadata

Preserve enough source-native metadata to reconstruct what was measured, including where available:

```text
topic ID
topic display name
topic hierarchy IDs / labels
publication year
works count
API endpoint/query
collection method
topic-classification caveat
```

If OpenAlex exposes a topic description or keywords cheaply and directly as source metadata, preserving them is acceptable, but do not add extra API requests solely for cosmetic enrichment.

## Topic hierarchy

Preserve the source-native hierarchy available from OpenAlex, for example:

```text
TOPIC
    child of
SUBFIELD
    child of
FIELD
    child of
DOMAIN
```

Do not map these nodes to EPO fields, CN codes, NACE, CPV or internal economic concepts in production code.

The source hierarchy is evidence; cross-source semantic mapping is a separate future reasoning operation.

## Minimal topology test

The completion report should perform one **analysis-only** topology/convergence exercise using the selected topics.

The implementation does not need to persist a graph.

At minimum, inspect whether historically separate conceptual groups in the selected slice show signs of increasing overlap by 2019.

Prefer a cheap source-faithful mechanism supported by OpenAlex, such as counts of works jointly associated with two selected topics or another direct co-occurrence/grouping mechanism.

Focus on a very small number of pairs, approximately **3–6**, chosen to test economically interesting intersections such as:

```text
neural networks ↔ hardware/VLSI
AI/ML ↔ memory/in-memory computing
computer vision/NLP ↔ neural networks
```

Do not download or construct the full OpenAlex citation graph.

For each tested pair, report annual 2017–2019 overlap counts if obtainable.

If the API cannot support a bounded overlap query cleanly, do not build a workaround-heavy system. State the limitation and perform the smallest alternative semantic test that preserves the spirit of the experiment.

## Derived analysis

Growth rates, overlap changes and simple shares may be computed after collection for the completion report.

Do not persist them unless the existing observation model naturally requires it.

Useful analysis includes:

```text
2017 → 2019 topic growth
2018 → 2019 velocity
pairwise overlap growth
share of selected-topic works involved in tested intersections
```

The report must distinguish counts from interpretations.

## Source metadata

Add one `SignalSource`, stable identity such as:

```text
openalex:knowledge-topology
```

Record at least:

- official OpenAlex API access,
- current access/reuse terms reference,
- evidence semantics: scholarly/research activity plus source-native semantic classification,
- geography: global scholarly corpus,
- major caveats:
  - publication coverage varies by field/source/language/year,
  - counts can change as OpenAlex updates records,
  - topic assignments are model-generated rather than author-provided ground truth,
  - current topic classifications applied retrospectively create model-time leakage in historical backtests,
  - publication volume is not commercial demand,
  - publication count alone does not prove technological importance,
  - some works may lack topic classification.

Do not create a general licensing subsystem.

## API efficiency

Keep requests bounded and cheap.

Prefer metadata lookups plus grouped/count queries over downloading large work corpora.

The empirical run should use a modest number of requests. If more than roughly 30 HTTP requests are required, Codex should stop and reconsider the query strategy before proceeding.

Report successful request count and approximate response volume where practical.

## CLI

Add one small command consistent with existing collectors, for example:

```text
asymmetry-engine collect-openalex --database <path>
```

The selected topics and historical years may remain fixed in this empirical slice.

Do not build a generic OpenAlex query CLI.

## Persistence and deduplication

Reuse the existing pipeline, repository, SQLite schema and `(source_id, external_id)` deduplication semantics.

Use a fresh SQLite database for the live empirical run.

Run the identical collection twice:

- first run inserts the annual topic measurements,
- second run demonstrates deduplication.

Do not add:

- graph tables,
- topic mapping tables,
- hierarchy tables,
- semantic embedding storage,
- vector databases,
- citation-edge storage,
- generic measurement/revision tables.

## Tests

Add focused tests for at least:

1. the collector makes only the intended bounded official API requests;
2. source-native topic hierarchy is preserved correctly;
3. annual counts become separate `research_statistic` observations;
4. deterministic identity excludes measured count and collection timestamp;
5. annual periods do not fabricate `occurred_at` event timestamps;
6. malformed/API responses fail clearly;
7. repeated identical collection deduplicates correctly;
8. current topic/model-time caveat is retained in source metadata;
9. any response grouping/index parsing used by the implementation maps counts to the correct topic/year.

Do not over-test OpenAlex itself.

## Out of scope

Do not implement:

```text
cross-source concept mapping
EPO ↔ OpenAlex mapping
knowledge graph
citation graph
embeddings
semantic search
LLM classification
opportunity generation
disequilibrium scoring
agentic research planning
research-topic forecasting
web UI
scheduled collection
```

## Live empirical run

After tests pass, run the collector twice against a fresh database.

Then perform the analysis-only inspection described above.

The purpose is to answer:

> Does OpenAlex add genuinely useful semantic/topological evidence beyond a flat publication-growth series?

## Completion report

Return:

### 1. Implementation

- commit SHA,
- files changed,
- test result,
- working-tree status.

### 2. Source verification

- official endpoints used,
- current authentication/access behavior,
- terms/reuse position,
- successful request count,
- any material deviation from this spec.

### 3. Selected topic set

Table with:

```text
topic ID
topic label
subfield
field
domain
reason included
```

### 4. Annual measurements

For every selected topic:

```text
2017 works
2018 works
2019 works
2018→2019 change
2017→2019 change
```

### 5. Semantic decomposition

Explain whether broad AI/computing activity decomposes into materially different fine-grained trajectories.

Identify any topics that would have been hidden or misinterpreted by a broad field-level count.

### 6. Topology / convergence test

For each selected pair:

```text
pair
2017 overlap
2018 overlap
2019 overlap
change
interpretation
```

Clearly separate source evidence from interpretation.

### 7. Historical leakage assessment

Explicitly state:

- what evidence genuinely existed by 31 Dec 2019,
- what classifications/metadata are supplied by today's OpenAlex model,
- which conclusions are safe historical claims,
- which are only retrospective semantic reconstruction.

### 8. Architectural assessment

Answer:

- Does `SourceObservation` still represent this evidence honestly?
- Does source-native hierarchy need first-class persistence yet?
- Does the topology test create pressure for explicit relationships?
- Is OpenAlex mainly a velocity, semantic-resolution or topology source?
- What should remain deliberately unresolved?

### 9. Empirical verdict

Choose one:

```text
A — OpenAlex materially improves semantic/topological reasoning and earns continued use
B — useful mainly as research-velocity confirmation; semantic gain is limited
C — adds little incremental information relative to implementation cost
D — source/model caveats make it unsuitable for the Engine
```

Explain the verdict.

## Success condition

Spec 011 succeeds if we learn whether OpenAlex provides **incremental semantic/topological information that changes how the Engine interprets broad knowledge signals**.

Success does not require finding an opportunity.

The key question remains:

> **What did reality teach us that we could not see before this source?**
