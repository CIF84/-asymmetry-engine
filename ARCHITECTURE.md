# Architecture

## Status and purpose

This document describes the architecture that exists now, the manual empirical system around it, and the evidence threshold for future implementation. It does not map every concept in the learned operating model to software.

Asymmetry Engine remains a modular monolith. The implemented software is a bounded evidence-ingestion and reasoning substrate; the wider RADAR/FORGE/INTERACT/MEASURE/LEARN loop is currently operated through specifications, artifacts, checkpoints, tools, and human governance.

## Actual system boundary

```text
EXTERNAL SOURCES
      ↓
BOUNDED SOURCE ADAPTERS
      ↓
NORMALIZED SOURCE OBSERVATIONS
      ↓
SQLITE RUN + REVISION-AWARE CAPTURE PERSISTENCE
      ↓
DOMAIN-SPECIFIC REASONING WHERE EARNED

──────────── manual empirical boundary ────────────

RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN
```

The lower loop is an operating practice, not an implemented orchestration pipeline. It may branch, stop early, or revisit prior evidence.

## Current repository implementation

```text
src/asymmetry_engine/
├── models.py
├── db.py
├── pipeline.py
├── reasoning.py
├── cli.py
└── sources/
    ├── stackexchange.py
    ├── cfpb.py
    ├── dataforseo.py
    ├── ted.py
    ├── eurostat.py
    ├── azure_prices.py
    ├── comext.py
    └── openalex.py

tests/
docs/
specs/
experiments/
```

### Source adapters

Each adapter owns source-specific request construction, response validation, normalization, stable external identity, access metadata, and semantic caveats. Adapters return `SourceObservation` objects and do not know about SQLite.

Collectors are intentionally bounded. Tests inject clocks and network openers, making normalization and failure behavior deterministic without live collection.

### Domain records

`SignalSource` records source identity, access method, terms reference, commercial-use considerations, selection biases, and source metadata.

`SourceObservation` is a frozen normalized capture input containing:

```text
source_id
external_id
observed_at
occurred_at
item_kind
content
canonical_url
metadata
```

Source-specific facts stay in metadata rather than leaking into generic columns. Source registry records currently represent mutable current metadata; historical source-policy snapshots are not implemented.

### Persistence

SQLite owns three tables:

- `signal_sources` — current source definitions and caveats;
- `pipeline_runs` — start, completion/failure, fetched/inserted/duplicate counts, and errors;
- `source_observations` — immutable first or changed captures associated with their observing run.

Logical and capture identity are separate:

```text
logical source item
    (source_id, external_id)

capture
    observation_id
    capture_sequence within logical item
    material evidence fields
    pipeline_run_id
```

Material equality compares `occurred_at`, item kind, content, canonical URL, and canonicalized metadata against the latest stored capture. `observed_at` and run identity do not by themselves create revisions.

```text
A → store sequence 1
A → duplicate
B → store sequence 2
B → duplicate
A → store sequence 3
```

Current readers select the highest sequence per logical item. Historical captures remain available without being interpreted as simultaneous current evidence.

Existing pre-038 databases receive one bounded transactional table migration. This is not a general migration framework, event store, or temporal database.

### Pipeline runs

`run_collection()` executes one collector. It creates a run before acquisition, commits a successful observation batch atomically, and records failure without leaving a partial capture batch.

Run accounting means:

- inserted: first sightings plus materially changed captures;
- duplicate: observations materially equal to their latest capture.

There is no multi-source scheduler. Source-level isolation arises from one collector per run.

### Domain-specific reasoning

The implemented reasoner handles one Czech CN75 trade slice. It produces explicit economic entities, measurements, source-native relationships, lineage, supported interpretations, unsupported claims, alternative explanations, and next evidence.

It is not a generic opportunity detector. Its decomposition condition does not score opportunity quality. It uses current/latest persisted observations so historical revisions are not double-counted.

### CLI and tests

The CLI exposes bounded source-collection commands and one CN75 reasoning command. There is no UI, scheduler, or service process.

Tests protect request bounds, source-native identity, missing-value discipline, timestamps, source caveats, failures, atomic rollback, revision transitions, safe legacy upgrade, current-view semantics, deterministic reasoning, lineage, and unsupported inference.

## Architectural principles earned by evidence

### Keep the architecture small

Use one repository, one Python package, SQLite, and a CLI until real operating pressure requires more. Complexity must shorten or strengthen the path to discriminating economic evidence.

### Immutable evidence, mutable interpretation

Materially changed observations append; they do not rewrite prior captures. Interpretations may change without changing evidence history. Persistent generic interpretation versioning is not yet implemented.

### Stable logical identity, explicit recapture

Source-native identity groups observations across time. Capture sequence records material state transitions without treating collection time alone as change.

### Source independence and source honesty

Generic persistence must not acquire source-specific semantics. Every adapter states its access method, limitations, and selection biases. Public visibility is not equivalent to permission for ingestion, retention, reuse, contact, or commercialization.

### Explicit provenance proportional to consequence

The code retains source/run/timestamp/content metadata and the reasoner retains observation lineage. Later manual decision artifacts strengthen provenance, evidence classes, freshness, estimates, and unknowns as consequence increases. A generic provenance graph is not implied.

### Determinism where appropriate

Use deterministic normalization, arithmetic, identity, serialization, and tests when semantic inference is unnecessary. Keep judgment visible when equivalence, relevance, or decision effect cannot be reduced safely.

### Evidence pressure before abstraction

Implement only when a problem is repeatedly observed, mechanically reusable, likely to improve experiment economics, and solvable with a small reversible change.

## Manual empirical architecture

The learned operating loop is:

```text
OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN
```

Repository artifacts currently implement the durable boundary:

- specs preregister questions, evidence, controls, budgets, stops, and verdicts;
- experiment artifacts preserve execution and outcomes;
- checkpoints consolidate learning without rewriting prior results;
- Git records revisions and supports independent review;
- human authorization governs consequential external action.

This arrangement is considered current architecture even though most of it is documentary and procedural rather than runtime software.

## Opportunity selection and scoring

The early design proposed additive ranking across demand, consequence, accessibility, competition, automation, and other dimensions. That is superseded as primary selection policy.

Current practice first tests fatal constraints:

```text
live decision?
economic consequence?
recoverable information?
inadequate exact resolution?
legitimate actor access?
observable effect?
controls permit the experiment?
```

One failed necessary condition can dominate attractive characteristics elsewhere. Ranking may eventually help among candidates that pass hard gates, but no generic scoring engine or stable score model is implemented or earned.

## Exact-resolution and decision compression

Exact functional resolution checking is a repeated early discriminator. It compares actor, decision, inputs, output, timing, and residual gap. The comparison remains semantic and manual; no resolver service, competition database, ontology, or embedding system is justified.

FORGE has repeatedly compressed unstructured uncertainty into options, discriminators, and testable next questions. This is a provisional reusable practice, not a generic decision engine.

## Interaction, controls, and authorization

Delivery, exposure, engagement, decision effect, value creation, value capture, and repeatability are distinct states. No software currently measures or automates them.

The governing invariant is:

```text
SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS
```

Consequential external action requires explicit user authorization. Controls remain procedural and proportional to consequence. There is no permission service, policy engine, autonomous action layer, or regulatory rules database.

## Operational telemetry

Experiment 036 established a partial historical baseline and a prospective manual logging standard. Experiment artifacts should record active time, spend, human attention, controls, interactions, verdict, uncertainty change, and evidence yield where useful.

Pipeline-run timestamps and counts are ingestion telemetry, not experiment economics. A telemetry database or dashboard is not earned.

## Deliberately unimplemented

Current evidence does not justify:

- generic opportunity detection, clustering, or registry software;
- additive or learned opportunity scoring;
- generic monitoring and scheduled orchestration;
- experiment, outcome, asset, or portfolio databases;
- automated research-policy selection;
- generic FORGE or decision software;
- automated interaction, outreach, response tracking, or attribution;
- permission, governance, or regulatory services;
- generic ontology, graph, vector store, or ATLAS knowledge system;
- telemetry infrastructure;
- microservices, event streaming, or a web application.

Absence is not unfinished negligence. Several concepts remain unimplemented because manual evidence work is cheaper, safer, and more adaptable today.

## Evolution rule

Future changes follow:

```text
repeated observed problem?
→ mechanically reusable?
→ improves experiment economics?
→ small and reversible?
→ specify, implement, validate, and measure
```

If any answer is no, document, keep manual, or defer. Automation should multiply validated asymmetries and repeated mechanical work, not compensate for weak opportunities or unresolved assumptions.

## Economic direction

The architectural objective remains to support discovery and resolution mechanisms capable of creating and eventually capturing repeatable economic value. The code has not validated revenue, willingness to pay, repeatability, or autonomous operation. Portfolio and FREEDOM language describes the long-term economic target, not current software.

## Historical design note

The original architecture described automatic decision extraction, generic asymmetry detection, a persistent registry, additive score snapshots, monitoring, experiment/outcome persistence, scheduling, and revenue assets as a staged system. Experiments 013–038 showed that hard discriminators, semantic judgment, accessible decision surfaces, explicit authorization, and disposable resolutions often matter before those components. Git preserves the original architecture; this file now describes the system that exists and the rules governing evidence-earned evolution.
