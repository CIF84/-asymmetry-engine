# Spec 001 — Stack Exchange Observation Slice

## Goal

Create the first executable empirical vertical slice for Asymmetry Engine:

```text
Stack Exchange API
        ↓
StackExchangeCollector
        ↓
SourceObservation
        ↓
SQLite
        ↓
inspect real observations
```

The purpose of this slice is not to implement the downstream opportunity-discovery architecture. It is to establish a minimal, real-data ingestion loop and learn what abstraction survives contact with an actual source.

The implementation should remain deliberately compact. Architecture documents are directional, not sacred; prefer the smallest design that satisfies the behavior below.

## Context

Asymmetry Engine is intended to observe real economic decision friction, detect persistent information asymmetries, rank them, run cheap commercialization experiments, and feed actual economic outcomes back into the system.

Development is explicitly empirical:

```text
hypothesis
→ smallest implementation
→ real data
→ inspect
→ learn
→ revise abstraction
→ next implementation
```

This first slice should therefore capture source evidence faithfully without prematurely interpreting it as a decision, pain signal, evidence taxonomy, or asymmetry.

Stack Exchange is the first source because it provides explicit public questions/problems with stable source identities and useful engagement metadata. It also has known selection bias: users are self-selecting, comparatively technical/prosumer-oriented, and the population represented by a Stack Exchange site should not be treated as representative of the general population.

Source-selection bias should be recorded as source metadata, not “corrected” away.

The likely second source is the CFPB Consumer Complaint Database, which is structurally different. Do not design this implementation around assumptions about CFPB beyond preserving source independence.

## Scope

Implement only the minimum needed for one real Stack Exchange ingestion run.

### Project/package setup

Add a minimal Python project/package structure suitable for local development and pytest-based testing.

Keep the package compact. A reasonable initial shape is:

```text
src/asymmetry_engine/
    __init__.py
    __main__.py
    models.py
    db.py
    pipeline.py
    cli.py
    sources/
        __init__.py
        stackexchange.py

tests/
```

This shape is guidance, not a rigid requirement. Do not create additional architectural layers without a demonstrated need.

### SignalSource

Represent source-level metadata separately from individual observations.

At minimum, source metadata should make it possible to identify:

- stable source ID
- human-readable source name
- access method / API identity
- source or terms reference
- known commercial-use / licensing considerations if applicable
- known selection biases / population limitations

For Stack Exchange, explicitly capture that the source is self-selected and comparatively technical/prosumer-oriented rather than globally representative.

Do not build a source-governance subsystem. This is metadata sufficient for provenance and later interpretation.

### SourceObservation

Create a source-independent observation representation that is intentionally semantically weak.

It should preserve the common facts needed to inspect what was observed without introducing downstream interpretations.

At minimum, observations should preserve:

- source identity
- stable external identity
- when the engine observed the record
- when the underlying source event/item occurred, when available
- source-native item kind/type where useful
- human-readable content sufficient for inspection
- canonical source URL/reference when available
- source-specific metadata that should not be forced into premature universal fields
- association with the pipeline run that captured it

Preserve the distinction between:

- `observed_at`: when Asymmetry Engine saw the record
- source/occurrence timestamp: when the source says the underlying item was created/occurred

Do not add interpretive fields such as decision type, pain, transaction proximity, economic domain, confidence, asymmetry, or commercial score.

Do not introduce `DecisionSignal`, `DecisionProblem`, or a generic `Evidence` abstraction in this specification.

### Stack Exchange collector

Implement a collector using the official Stack Exchange API.

Requirements:

- use an official API endpoint rather than scraping
- use a bounded retrieval size; this is a sample, not a crawler
- default to a financially/economically relevant Stack Exchange site such as Personal Finance & Money (`money`), unless implementation constraints reveal a better equivalent
- preserve stable Stack Exchange question identity
- normalize source timestamps consistently
- retain useful source-native metadata such as tags and engagement/count fields when available
- handle normal HTTP/API failures cleanly
- respect API-directed backoff behavior if returned
- do not build scheduling or continuous crawling

The collector should not know about SQLite persistence.

Avoid introducing an abstract base-class hierarchy for collectors unless there is a concrete implementation need. There is only one collector in this specification.

### Provenance

For this slice, provenance should be concrete rather than an opaque catch-all object.

The persisted record should make it possible to answer:

- which source produced this observation?
- what stable external item did it refer to?
- where can the source item be inspected?
- when did the source item occur/create, if known?
- when did Asymmetry Engine observe it?
- what content/metadata did the normalized observation preserve?
- which pipeline run captured it?

Source-specific details that do not belong in the common envelope may be stored as structured metadata (for example JSON) rather than promoted into universal columns prematurely.

### Stable identity and deduplication

Use the external system's stable identity rather than fuzzy or content-based matching when possible.

For Stack Exchange, question identity should derive from the source/site namespace plus the stable question ID.

Persistence must enforce uniqueness at the source/external-identity boundary so that re-running the same bounded sample does not create duplicate observations.

Do not use title matching, fuzzy matching, or downstream semantic similarity for this purpose.

This slice is about deduplicating the same source item, not detecting semantically duplicate questions.

### SQLite persistence

Use SQLite for local persistence.

Persist at minimum:

- source metadata
- pipeline runs
- source observations

Keep the schema small and explicit.

A heavyweight ORM or migration framework is not required for this first slice unless a strong local engineering reason emerges.

The observation persistence model may treat the first captured version of a source item as the immutable observation for this slice. If mutable source attributes such as score/view count change later, do not invent monitoring/version-history semantics yet merely to capture those updates.

In other words: satisfying “no duplicate unchanged observations” is required; implementing observation history or source-state monitoring is not.

### PipelineRun

Represent each collection execution explicitly.

A run should record enough information to determine whether it succeeded or failed and what happened, including at minimum:

- source
- start time
- completion time when finished
- status
- fetched count
- inserted count
- duplicate count or equivalent deduplication result
- error information when failed

Source-level failure isolation is required.

A failed Stack Exchange collection/persistence attempt must be represented as a failed Stack Exchange run without leaving an accidentally successful-looking partial run.

The implementation should use a sensible transactional boundary so that observation persistence for a source run is not left partially committed on persistence failure.

Do not build cross-source orchestration yet.

### CLI

Provide a tiny CLI that can run the Stack Exchange ingestion slice with one command.

The exact command syntax is an implementation choice, but it should allow at least:

- invoking Stack Exchange collection
- selecting or defaulting the Stack Exchange site
- setting a bounded sample size
- choosing or clearly locating the SQLite database

The command should print a concise completion summary including the run outcome and useful counts.

Running the same command again against the same database and unchanged source items should demonstrate deduplication.

### Tests

Add focused tests around the boundaries that matter for this slice.

At minimum test:

- representative Stack Exchange response normalization into `SourceObservation`
- stable source/external identity generation
- timestamp normalization
- persistence of source metadata / observations / pipeline runs as applicable
- duplicate insertion behavior
- successful pipeline-run counts/status
- collector or pipeline failure behavior
- no partial observation batch after a persistence failure, if that is the chosen transaction model

Automated tests should not depend on the live Stack Exchange API. Use representative fixtures/mocks/fakes for deterministic tests.

A manual real-source run is part of completion evidence.

## Important semantics and constraints

Preserve these project principles during implementation:

- observable behavior before ideation
- immutable evidence, mutable interpretation
- source independence and provenance
- selection bias is source metadata, not something to pretend we can perfectly correct
- architecture documents are directional, not sacred
- infrastructure is not the business
- do not implement abstractions because they merely seem plausible

Keep the implementation small enough that adding a structurally different second source can genuinely challenge the current abstraction.

Do not optimize for a hypothetical large-scale crawler, distributed system, or production platform.

## Explicitly out of scope

Do **not** implement any of the following in Spec 001:

- LLM extraction
- `DecisionSignal`
- `DecisionProblem`
- generic `Evidence` abstraction/taxonomy
- asymmetry detection
- clustering
- embeddings
- vector database
- scoring
- `Asymmetry Strength`
- `Commercial Attractiveness`
- monitoring / observation version history
- CFPB collector
- scheduling / cron / workflow orchestration
- UI / web application
- custom machine-learning models
- product or commercialization logic

Do not update README.md, ARCHITECTURE.md, or ROADMAP.md merely to make them mirror implementation details unless implementation exposes a genuine contradiction that needs explicit reporting first.

## Acceptance criteria

Spec 001 is complete when all of the following are true:

1. A fresh local checkout can install/run the minimal Python package and its tests.
2. One CLI command creates a `PipelineRun` and fetches a bounded real sample from the official Stack Exchange API.
3. The source sample is normalized into provenance-preserving `SourceObservation` records.
4. Source metadata includes the known Stack Exchange selection-bias limitation.
5. Observations and the pipeline run are persisted in SQLite.
6. Stable source/external identity is enforced by persistence.
7. Re-running the same bounded sample against the same database does not create duplicate observations for unchanged source items.
8. The second run reports deduplication/insert counts clearly enough to verify the behavior.
9. A source or persistence failure is recorded as a failed run and does not masquerade as success or leave an unintended partial successful batch.
10. Focused automated tests for normalization, persistence, deduplication, and failure behavior pass.
11. A manual real-source run has been performed and representative stored observations have been inspected.

## Requested completion report

When implementation is complete, Codex should return a concise report containing:

1. Commit SHA and commit message.
2. Files added/changed.
3. Exact CLI command used for the real Stack Exchange run.
4. Test command and test result/count.
5. First-run summary: fetched / inserted / duplicate counts.
6. Second-run summary demonstrating deduplication.
7. 3–5 representative stored observations, showing the normalized common fields plus selected source-specific metadata.
8. SQLite tables/schema actually implemented.
9. Any API/source behavior that differed materially from the assumptions in this specification.
10. Architectural pressure discovered from the real source, especially anything suggesting that `SourceObservation` is too broad, too narrow, misleading, or awkward.
11. Any implementation choice that materially departed from the spec, with the reason.

After this report, stop. Do not proceed automatically to CFPB or downstream extraction. The next step is a ChatGPT review of the implementation and real observations to decide what reality taught us.