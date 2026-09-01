# Roadmap

## Objective

This roadmap exists to prevent Asymmetry Engine from becoming an interesting research project that never generates revenue.

The overriding optimization target is:

> **Minimize time to first independent revenue while building reusable infrastructure that compounds over time.**

Architecture, tooling, automation, and research are subordinate to that objective.

## Core Constraints

### Revenue is evidence

The system is not validated by code volume, architectural sophistication, number of signals collected, number of asymmetries detected, number of generated assets, GitHub stars, or model accuracy in isolation.

The strongest early evidence is:

```text
someone paid
```

### Do not build a platform before a business experiment needs one

Avoid authentication, multi-user accounts, dashboards, billing systems, complex frontends, and distributed infrastructure.

CSV, SQLite, scripts, static pages, hosted checkout, and external analytics are acceptable.

### No speculative product building

Every commercial experiment must reference an observed asymmetry with evidence.

Do not build products because they sound interesting.

### Automate volume, not uncertainty

Automate collection, normalization, extraction, classification, clustering, scoring, monitoring, reporting, and repetitive publishing.

Do not automate unresolved assumptions merely because orchestration is possible.

### Prefer reversible bets

Initial experiments should be cheap, fast, independently deployable, easy to kill, low maintenance, low capital, and low compliance.

### Prefer self-service economics

Initial preference:

- B2C,
- prosumer,
- self-service,
- low-friction checkout,
- direct economic value,
- automated delivery.

Avoid dependence on enterprise procurement, long sales cycles, account management, custom implementation, and networking-heavy acquisition.

### Advertising is allowed, but not assumed

Ads, affiliate revenue, sponsorships, referrals, subscriptions, and direct sales are all valid.

Do not force every asymmetry into a direct-payment model. Do not force every asymmetry into content. The experiment model should follow the economics of the problem.

## Phase 0 — Repository Skeleton

Goal: create only enough structure to begin automated discovery.

Deliverables:

```text
README.md
ROADMAP.md
ARCHITECTURE.md

src/
tests/
config/
data/
```

Technology preference:

- Python,
- SQLite,
- CSV/Parquet,
- simple CLI,
- APIs,
- LLM APIs only where useful.

No UI required.

Exit condition:

```text
python -m asymmetry_engine
```

runs successfully.

## Phase 1 — Signal Acquisition v0

Goal: collect real evidence from legitimate public sources.

Start with 2–3 sources.

Good candidates:

- Stack Exchange API,
- Hacker News API,
- YouTube Data API,
- government/open datasets.

Do not wait for ideal coverage.

Deliverables:

- source abstraction,
- collectors,
- source metadata,
- pipeline-run tracking,
- persisted observations.

Exit condition:

At least `1,000 observations` have been collected and persisted from more than one independent source.

## Phase 2 — Decision Extraction v0

Goal: turn raw observations into candidate decision demand.

Detect patterns such as:

```text
Should I buy X?
X vs Y?
Is X worth it?
Should I repair or replace?
Should I switch?
When should I buy?
How much do I need?
What is best for my constraints?
```

Deliverables:

- decision taxonomy,
- extraction pipeline,
- transaction-proximity score,
- confidence score,
- provenance for derived fields.

Exit condition:

At least `100 plausible decision signals` are extracted automatically from real observations.

## Phase 3 — Asymmetry Detection v0

Goal: cluster decision signals into persistent economic problems.

Example:

```text
"Should I replace my iPhone?"
"Should I wait for the next model?"
"When is the cheapest time to upgrade?"

              ↓

Optimal smartphone replacement timing
```

Deliverables:

- asymmetry entity,
- clustering logic,
- deduplication,
- evidence relationships,
- basic lifecycle.

Exit condition:

Produce approximately `20 evidence-backed candidate asymmetries` without manually inventing them.

## Phase 4 — Asymmetry Registry v0

Goal: make asymmetries persistent and longitudinal.

Minimum entities:

```text
SignalSource
PipelineRun
Observation
DecisionSignal
Asymmetry
AsymmetryObservation
ScoreSnapshot
```

Minimum lifecycle:

```text
DISCOVERED
OBSERVED
WATCHING
EMERGING
VALIDATED
DECLINING
ARCHIVED
```

Exit condition:

A second pipeline run updates existing asymmetries rather than simply duplicating them.

## Phase 5 — Economic Scoring v0

Goal: rank asymmetries by commercial attractiveness.

Initial dimensions:

- signal confidence,
- demand,
- transaction proximity,
- economic consequence,
- information fragmentation,
- automation feasibility,
- data accessibility,
- answer verifiability,
- competition,
- distribution accessibility,
- maintenance burden,
- regulatory risk.

Keep scoring decomposable. Do not optimize the formula prematurely.

Exit condition:

The system produces a ranked `TOP 10` worth human review.

## Phase 6 — Monitoring v0

Goal: track how asymmetries evolve.

Measure where possible:

- new evidence,
- demand velocity,
- search growth,
- CPC change,
- complaint frequency,
- competition change,
- regulatory change,
- score trajectory.

Exit condition:

Known asymmetries accumulate historical snapshots and can be classified as rising, stable, or declining.

## Phase 7 — First Commercial Experiment

Goal: attempt the first real monetization.

Choose one highly ranked asymmetry.

Generate candidate commercialization models:

```text
digital product
decision tool
content engine
affiliate workflow
lead engine
intelligence product
micro-SaaS
marketplace
```

Score each by time to launch, cost, automation, revenue potential, distribution, maintenance, and platform dependency.

Choose the cheapest credible test.

Target build time:

```text
≤ 7 days
```

Preferred shape:

```text
one decision
one user type
one outcome
one monetization mechanism
```

Exit condition:

A real user can exchange money, attention, or economically meaningful intent for value.

Direct payment is preferred where sensible, but affiliate, referral, ad, or lead economics are valid if they match the opportunity.

## Phase 8 — First Real Revenue

Primary objective:

```text
€0 → €1
```

The purpose is not income replacement. The purpose is proving the ownership loop:

```text
problem
  ↓
solution
  ↓
distribution
  ↓
customer
  ↓
money
```

Measure traffic, acquisition source, conversion, price, usage, abandonment, revenue, refund, and repeat behaviour.

If evidence is weak:

```text
mutate once
```

then:

```text
kill
```

Avoid indefinite polishing.

## Phase 9 — Outcome Feedback

Every experiment returns structured evidence to the registry.

Example:

```text
ASYM-00142

MODEL:
decision_tool

PRICE:
€7

VISITORS:
243

PURCHASES:
11

CONVERSION:
4.5%

REVENUE:
€77

RESULT:
PROMISING
```

Failed experiments are equally useful.

The registry should eventually learn:

```text
asymmetry type
        ×
commercialization model
        ×
distribution channel
        ↓
observed outcome
```

## Phase 10 — Second Independent Asset

Do not immediately spend months scaling the first success.

Return to the registry, select another opportunity, and launch a second independent experiment.

Exit condition:

Revenue or other meaningful commercial value has been generated from at least two independently discovered asymmetries.

This tests whether the system is repeatable rather than lucky.

## Phase 11 — Workflow Automation

Only automate commercialization patterns after repeated evidence shows that the pattern works.

Possible reusable workflows:

- research,
- landing-page generation,
- report generation,
- digital-product generation,
- content generation,
- publishing,
- checkout,
- fulfillment,
- analytics,
- marketing asset generation,
- monitoring.

The goal is not to automate everything. The goal is to reduce marginal human effort for proven economic processes.

## Phase 12 — Revenue Asset Portfolio

Successful experiments become persistent assets.

Possible categories:

```text
decision tools
digital products
affiliate properties
content engines
data products
alerts
micro-SaaS
lead workflows
APIs
marketplaces
```

Track each asset on:

```text
monthly revenue
growth
gross margin
maintenance hours
support burden
automation level
platform dependency
concentration risk
```

Kill or sell assets whose operational burden exceeds strategic value.

## Phase 13 — Asymmetry Registry as Product

Only consider this after the registry contains meaningful longitudinal evidence.

Possible products:

- opportunity database,
- emerging-friction alerts,
- sector intelligence,
- founder research,
- investor intelligence,
- Decision Demand Index,
- API access,
- research reports.

This is a secondary monetization path. Do not allow it to delay the first commercial experiments.

## Time Discipline

### First 7 days

Repository skeleton, first source collectors, persisted observations.

### First 14 days

Automated decision extraction, first asymmetry clusters, ranked preliminary output.

### First 30 days

Persistent registry, initial economic scoring, top candidates selected.

### First 45 days

First commercialization experiment live.

### First 60 days

At least one meaningful demand test completed.

Result must be one of:

```text
SCALE
MUTATE
KILL
```

Never:

```text
KEEP POLISHING
```

### First 90 days

Target:

- repeatable multi-source signal pipeline,
- living asymmetry registry,
- longitudinal monitoring,
- multiple scored opportunities,
- at least one commercial experiment,
- first reusable commercialization workflow,
- ideally first revenue.

## Anti-Roadmap

The following are explicitly not priorities until required:

- beautiful UI,
- mobile application,
- Kubernetes,
- microservices,
- event streaming,
- enterprise collaboration,
- elaborate user management,
- custom ML infrastructure,
- custom foundation models,
- vector databases without demonstrated need,
- complex orchestration frameworks,
- perfect taxonomy,
- perfect scoring,
- full internet coverage,
- massive scraping infrastructure.

## Success Hierarchy

From weakest to strongest evidence:

```text
code exists
    ↓
pipeline runs
    ↓
signals collected
    ↓
decision demand extracted
    ↓
asymmetry detected
    ↓
asymmetry persists over time
    ↓
user sees experiment
    ↓
user interacts
    ↓
user returns
    ↓
economic value captured
    ↓
revenue repeats
    ↓
multiple assets produce value
    ↓
portfolio operates with little human intervention
```

The roadmap should always prioritize moving one step downward in this hierarchy.

## Roadmap Rule

When choosing between two tasks, prefer the one that more directly improves:

```text
signal → asymmetry → experiment → payment → learning
```

If a task does not strengthen that loop, it should require explicit justification.
