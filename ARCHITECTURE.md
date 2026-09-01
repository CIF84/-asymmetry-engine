# Architecture

## Purpose

Asymmetry Engine is an evidence-driven opportunity detection and commercialization system.

The architecture should support this loop:

```text
OBSERVE
   ↓
NORMALIZE
   ↓
EXTRACT
   ↓
DETECT
   ↓
PERSIST
   ↓
SCORE
   ↓
MONITOR
   ↓
EXPERIMENT
   ↓
MEASURE
   ↓
LEARN
   ↺
```

The architecture should optimize for rapid experimentation, traceability, longitudinal observation, source independence, low operational complexity, low cost, incremental automation, and economic learning.

## Architectural Principles

### Modular monolith first

Start with one repository and one deployable application. Do not introduce microservices unless real operational pressure requires them.

### Domain terminology over metaphors

Use concrete software and business concepts: signals, observations, decisions, asymmetries, scores, experiments, assets, outcomes.

Avoid forcing implementation into conceptual metaphors that no longer improve clarity.

### Immutable evidence, mutable interpretation

Observations should be append-only where practical. Interpretations such as clustering, scoring, and lifecycle state may change over time.

### Source independence

External source-specific structures must not leak into the core domain model.

### Explicit provenance

Every important derived field should be traceable to source, timestamp, transformation, model or rule version, and confidence where applicable.

### Economic observability

The system should eventually be able to answer:

- What did this asymmetry cost to discover?
- What did it cost to evaluate?
- What did its experiment cost?
- How much revenue did it generate?
- How much maintenance does it require?

## Initial Repository Shape

```text
asymmetry-engine/
│
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
│
├── src/
│   └── asymmetry_engine/
│       ├── signals/
│       ├── observations/
│       ├── decisions/
│       ├── asymmetries/
│       ├── scoring/
│       ├── monitoring/
│       ├── experiments/
│       ├── assets/
│       ├── outcomes/
│       ├── infrastructure/
│       └── cli/
│
├── tests/
├── config/
├── data/
└── scripts/
```

This structure is directional, not sacred. The codebase should evolve based on pressure from real use.

## High-Level Architecture

```text
                       EXTERNAL WORLD

        APIs          Open Data         Market Signals
         │                │                  │
         └────────────────┼──────────────────┘
                          ▼
                  Signal Acquisition
                          │
                          ▼
                     Observation
                          │
                          ▼
                  Decision Extraction
                          │
                          ▼
                  Asymmetry Detection
                          │
                          ▼
                  Asymmetry Registry
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       Monitoring + Scoring      Human Review
              │                       │
              └───────────┬───────────┘
                          ▼
                Commercial Experiment
                          │
                          ▼
                     Revenue Asset
                          │
                          ▼
                        Outcome
                          │
                          └────────────→ Registry
```

## Core Components

### Signal Acquisition

Responsibility: retrieve external signals through legitimate access mechanisms.

Examples include official APIs, open datasets, permitted feeds, aggregate search metrics, and public market data.

Possible structure:

```text
signals/
├── sources/
├── collectors/
├── policies/
└── pipeline.py
```

Each source should define:

```text
source_id
name
access_method
terms_reference
commercial_use_status
retention_policy
rate_limit
active
```

Collector interface:

```python
collect() -> list[ObservationInput]
```

Collectors independently handle authentication, pagination, throttling, retries, and source-specific schemas.

### Observations

An Observation is immutable evidence captured at a point in time.

Example fields:

```text
id
source_id
observed_at
external_reference
content_hash
signal_type
payload
provenance
```

The payload may be raw or derived depending on source policy. Large raw payload retention should be avoided unless genuinely useful.

### Decision Extraction

Responsibility: identify evidence of economically meaningful human decisions.

Example decision types:

```text
BUY_OR_WAIT
X_VS_Y
REPAIR_OR_REPLACE
SWITCH_OR_STAY
HOW_MUCH
BEST_FOR_CONSTRAINT
PRICE_FAIRNESS
RISK_ACCEPTANCE
```

A DecisionSignal may contain:

```text
id
observation_id
decision_text
decision_type
economic_domain
transaction_proximity
confidence
extraction_version
```

LLMs may be used for semantic extraction. Deterministic rules should be used where they are simpler and more reliable.

### Asymmetry Detection

Multiple DecisionSignals may point to the same underlying problem.

```text
"Should I replace my iPhone now?"
"Should I wait for the next iPhone?"
"Is buying last year's model smarter?"
"When is the cheapest time to upgrade?"

                 ↓

ASYM-00121
Optimal smartphone replacement timing
```

Detection may combine semantic similarity, embeddings, shared taxonomy, deterministic matching, LLM judgment, and human correction.

The output is not a product idea. It is a persistent hypothesis that a recurring information asymmetry exists.

### Asymmetry Registry

The registry is the persistent memory of the system.

It owns asymmetry identity, description, decision context, history, evidence relationships, lifecycle state, score history, experiment relationships, and outcome relationships.

Example entity:

```text
Asymmetry

id
title
description
domain
decision_holder
economic_consequence
information_gap
created_at
last_observed_at
lifecycle_state
```

Possible lifecycle states:

```text
DISCOVERED
OBSERVED
WATCHING
EMERGING
VALIDATED
DECLINING
ARCHIVED
```

States should remain easy to change as evidence accumulates.

### Monitoring

Monitoring revisits known asymmetries over time.

It should track new evidence, signal volume, demand growth, search velocity, CPC changes, competition changes, regulatory changes, pricing changes, solution quality, and score trajectory.

The trajectory may be more useful than the absolute score.

### Scoring

Scoring should remain decomposable. Never retain only `score = 87`.

Store the underlying dimensions:

```text
signal_confidence
demand
transaction_proximity
economic_consequence
information_fragmentation
automation_feasibility
data_accessibility
answer_verifiability
competition
distribution_access
maintenance_burden
regulatory_risk
commercial_attractiveness
```

Historical scores should be stored as snapshots.

```text
ScoreSnapshot

id
asymmetry_id
calculated_at
scoring_version
dimension_values
final_score
```

Weights should live in configuration rather than code where practical:

```text
config/scoring.yaml
```

### Commercial Experiments

An Experiment tests a monetization hypothesis.

```text
id
asymmetry_id
model
hypothesis
price
distribution_channel
started_at
ended_at
status
```

Possible models:

```text
DIGITAL_PRODUCT
DECISION_TOOL
CONTENT_ENGINE
LEAD_ENGINE
INTELLIGENCE_PRODUCT
MICRO_SAAS
MARKETPLACE
```

The experiment layer should remain business-model agnostic. Its job is not to build apps. Its job is to test whether value can be converted into revenue.

### Revenue Assets

A successful experiment may become a persistent revenue-generating asset.

Examples include a report workflow, calculator, newsletter, affiliate property, alerting service, micro-SaaS, lead workflow, dataset, or API.

Asset metadata should eventually include:

```text
monthly_revenue
gross_margin
maintenance_hours
support_burden
automation_level
platform_dependencies
growth
risk
```

### Outcomes

Outcomes represent observable market evidence.

Examples:

```text
visitor
signup
usage
purchase
subscription
refund
repeat_purchase
revenue
churn
```

Example entity:

```text
Outcome

experiment_id
metric
value
timestamp
source
```

Outcomes must flow back into the registry. This closes the learning loop.

## Persistence

### Initial choice: SQLite

Reasons:

- zero infrastructure,
- relational domain,
- transactions,
- easy inspection,
- easy backup,
- strong enough for early scale,
- simple migration path.

Suggested initial tables:

```text
signal_sources
pipeline_runs
observations
decision_signals
asymmetries
asymmetry_observations
score_snapshots
experiments
outcomes
assets
```

Use CSV or Parquet for analytical exports when useful. Raw large payloads can move to object storage later if justified.

## Pipeline Runs

Every execution should have a run record.

```text
PipelineRun

id
started_at
completed_at
status
sources_attempted
observations_created
decision_signals_created
asymmetries_created
asymmetries_updated
errors
api_cost
llm_cost
```

A failed source should not invalidate successful work from other sources. Prefer source-level transactional isolation.

## Data Flow

```text
external source
      ↓
collector
      ↓
Observation
      ↓
DecisionSignal
      ↓
candidate cluster
      ↓
Asymmetry
      ↓
ScoreSnapshot
      ↓
monitoring
      ↓
Experiment
      ↓
Outcome
      ↓
Asymmetry history
```

## LLM Usage

LLMs are useful for semantic extraction, classification, summarization, clustering assistance, asymmetry descriptions, and hypothesis generation.

Each LLM-derived result should retain:

```text
provider
model
prompt_version
timestamp
confidence
```

where practical.

This allows later reprocessing when prompts or models improve.

Do not use an LLM when deterministic computation is simpler.

## Scheduling

Start with the simplest mechanism that works:

```text
local scheduler
cron
GitHub Actions
```

Only add orchestration frameworks if recurring pipelines become operationally difficult.

Potential later options:

```text
Prefect
Dagster
Temporal
```

None are initial requirements.

## Interfaces

Initial interface:

```text
CLI
```

Potential commands:

```text
asymmetry-engine signals collect
asymmetry-engine detect run
asymmetry-engine asymmetries list
asymmetry-engine asymmetries show ASYM-00142
asymmetry-engine monitor run
asymmetry-engine experiments evaluate ASYM-00142
```

Initial outputs:

```text
terminal
CSV
JSON
SQLite
```

A web interface should appear only when interactive exploration creates real value.

## Testing Strategy

Prioritize source normalization, deduplication, deterministic scoring, asymmetry identity, persistence, lifecycle transitions, experiment attribution, and outcome attribution.

Avoid excessive testing of throwaway integrations.

## Data Ethics and Source Policy

Prefer, in order:

1. official APIs,
2. open datasets,
3. explicitly licensed sources,
4. aggregate public signals.

Scraping must not be a foundational dependency.

For each source record, capture:

```text
commercial_use_status
terms_reference
retention_policy
rate_limits
data_scope
```

Where possible, retain derived economic signals rather than unnecessary copies of user-generated content.

## Source Convergence

No high-confidence opportunity should depend on one signal source.

Prefer convergence:

```text
search demand
      +
question frequency
      +
commercial CPC
      +
complaint data
      +
poor incumbent solutions
      ↓
higher confidence
```

Source diversity should contribute directly to confidence scoring.

## Human Role

Automate collection, normalization, extraction, clustering, monitoring, scoring, and reporting.

Reserve human attention for strategy, ambiguous interpretation, opportunity selection, ethical judgment, product taste, capital allocation, and scale / mutate / kill decisions.

The goal is not removing humans. The goal is concentrating human judgment where it has the highest economic value.

## Evolution Path

```text
Phase 1
Python + SQLite + CLI
        ↓
Phase 2
multi-source signal collection
persistent asymmetry registry
        ↓
Phase 3
scheduled monitoring
economic scoring
        ↓
Phase 4
commercial experiments
payment + analytics integrations
        ↓
Phase 5
multiple live revenue assets
        ↓
Phase 6
portfolio monitoring
        ↓
Phase 7
interactive registry / API
        ↓
Phase 8
data-driven prediction of promising
asymmetry × monetization combinations
```

## Architectural North Star

The shortest meaningful system loop is:

```text
PUBLIC SIGNAL
     ↓
ASYMMETRY
     ↓
EXPERIMENT
     ↓
PAYMENT
     ↓
LEARNING
```

Any architectural component that does not strengthen or shorten this loop should require strong justification.
