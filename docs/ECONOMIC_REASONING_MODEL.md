# Economic Reasoning Model

## Status

This document captures the first reasoning model derived from empirical source research and historical backtesting. It is a conceptual contract, not an implementation mandate.

Do not build every entity described here merely because it exists in this model. New domain objects should enter code only when a real vertical slice requires them.

## Core Thesis

Asymmetry Engine should not merely collect signals and assign scores.

It should construct inspectable economic arguments:

```text
OBSERVATIONS
    ↓
MEASUREMENTS
    ↓
ECONOMIC ENTITIES
    ↓
RELATIONSHIPS
    ↓
EVIDENCE RELATIONS
    ↓
DISEQUILIBRIUM
    ↓
ECONOMIC CONSEQUENCE
    ↓
ASYMMETRY
    ↓
RESOLUTION HYPOTHESES
    ↓
COMMERCIAL MECHANISMS
    ↓
OPPORTUNITY
    ↓
EXPERIMENT
    ↓
OUTCOME
    ↓
LEARNING
```

The system should eventually be able to answer not only **what** it believes, but **why**, **based on which evidence**, **under which assumptions**, **what would falsify the interpretation**, and **what happened after acting on it**.

## Empirical Origin

Historical backtests exposed several failure modes in a flat trend-and-score architecture:

- fast patent growth can occur inside a contracting physical market;
- a major future transition can be invisible in the direct series while dependent systems accelerate around it;
- broad source taxonomies can combine multiple economically distinct concepts;
- research data can be more valuable for semantic decomposition and topology than for raw publication counts;
- trade data can change the interpretation of a signal rather than merely increase confidence;
- policy can causally alter rights, obligations, access, deadlines, costs, and market structure before commercial outcomes appear.

These failures imply that cross-source reasoning must preserve semantic and causal structure.

## Architectural Invariants

### Immutable evidence, explicit relationships, versioned interpretations

Observations should remain immutable where practical.

Relationships used to connect observations, concepts, and economic claims must be explicit and inspectable.

Interpretations must be versionable because the Engine should be able to change its beliefs without rewriting history.

```text
EVIDENCE: unchanged
RELATIONSHIPS: inspectable
INTERPRETATION v3: confidence 31%
INTERPRETATION v4: confidence 79%
REASON FOR CHANGE: new model + new evidence
```

### Never destroy reasoning through aggregation

A score may be useful as a view, but it must not replace the components beneath it.

Persist or reconstruct, where justified:

```text
evidence
measurement
concept mapping
relationship
assumption
uncertainty
alternative explanation
interpretation version
decision
outcome
```

### Operator is abstract

The operator may be a human, ChatGPT, an autonomous agent, a model committee, or a hybrid system.

Architecture must not hard-code human review as the only valid decision boundary.

### Relevance is conditional on the economic object

Not every evidence family applies to every opportunity.

Trade is important for physical goods and often irrelevant for software. App-store supply may matter for consumer software and not for industrial commodities.

Missing evidence should reduce confidence only when that evidence is expected for the type of entity and hypothesis being evaluated.

## Economic Entity Model

Source taxonomies should not be joined merely because labels sound similar.

The Engine should reason over explicit economic concepts and relationships.

Useful conceptual entity types currently include:

```text
TECHNOLOGY
CAPABILITY
APPLICATION
PRODUCT
MARKET
ACTOR
ORGANISATION
REGULATION
RESOURCE
INFRASTRUCTURE
```

Examples:

```text
machine learning      = capability
semiconductor         = technology
AI inference          = application
GPU                    = product
cloud compute          = market/service
bank                   = actor / organisation
PSD2                   = regulation
```

The exact taxonomy is not frozen.

## Relationship Model

Useful relationship semantics discovered so far include:

```text
enables
depends_on
requires
embodied_in
produced_as
supplied_by
bought_by
competes_with
substitutes_for
regulated_by
mandated_for
benefits_from
exposed_to
```

Relationships may have provenance, confidence, direction, temporal validity, and interpretation version.

Example:

```text
5G infrastructure
    depends_on
semiconductors
```

That relationship allows the Engine to reason about semiconductor dependency pressure even when semiconductor sales themselves temporarily decline.

## Measurements

A source observation may support one or more measurements.

At minimum, future reasoning should distinguish:

```text
LEVEL
VELOCITY
ACCELERATION
RELATIVE VELOCITY
CONCENTRATION
DISPERSION
```

Examples:

```text
imports_value
imports_quantity
implied_unit_value
patent_count
research_work_count
procurement_value
installed_base
solution_count
```

Measurements need clear units, time windows, geography, entity mapping, and provenance.

## Evidence Relations

The historical research produced several recurring cross-signal structures.

### Confirmation

Independent evidence families move in mutually consistent directions.

```text
patents ↑
trade ↑
sales ↑
```

### Contradiction

Evidence families imply different interpretations.

```text
patents ↑
orders ↓
production ↓
```

Contradiction is not automatically an error. It may indicate a cyclical downturn, defensive innovation, taxonomy mismatch, or structural transition.

### Divergence

Economically related variables move at materially different rates.

```text
demand ↑↑
supply →
price ↑
```

### Dependency

Several growing systems depend on a node whose direct signal is weak or flat.

```text
A ↑↑
B ↑↑
C ↑↑
all depend on X
X →
```

This may indicate latent dependency pressure.

### Knowledge convergence

Previously weakly connected research or technology domains increasingly intersect around an application, capability, or enabling technology.

The topology may change before aggregate publication volume becomes exceptional.

### Absence

A signal expected under a hypothesis fails to appear.

Absence is meaningful only when expectation is explicit. Missing irrelevant evidence is not negative evidence.

## Commitment

Commitment is distinct from attention, announcements, narrative, and intent.

Useful commitment evidence may include:

```text
purchases
orders
contracts
procurement awards
installed capacity
factory construction
production
imports
employment
business formation
paid subscriptions
final investment decisions
```

Three useful forms emerged from the backtest:

### Direct commitment

Actors directly buy, build, deploy, or contract for X.

### Enabling commitment

Actors build complementary infrastructure or standards required for X.

### Dependency commitment

Systems that depend on X are becoming economically important even if X itself is in a temporary cyclical slump.

## Policy as a Causal Signal

EUR-Lex research shows that policy deserves a distinct role from ordinary attention or narrative signals.

Legal acts can change:

```text
rights
obligations
access
compliance costs
deadlines
technical interfaces
market entry conditions
liability
incentives
```

Policy therefore can alter the feasible economic state before demand data catches up.

The policy signal must preserve legal lifecycle state. At minimum distinguish:

```text
proposal
adoption
entry_into_force
application
transposition_deadline
technical_standard_effective
amendment
repeal
```

A proposal is not economically equivalent to an enacted regulation.

Two historically useful archetypes:

### Obligation shock

```text
binding rule
    ↓
affected actors must act by deadline
    ↓
capability / information gap
    ↓
compliance demand
```

GDPR is a strong example: the regulation was adopted in 2016 and applied from 25 May 2018, creating a known future compliance deadline.

### Market-design shock

```text
new legal right / access rule
    ↓
previously closed interface opens
    ↓
new actor class becomes viable
    ↓
new products / intermediaries / infrastructure
```

PSD2 is a strong example: it created rights for payment initiation and account-information services and imposed secure access-interface obligations on account-servicing providers.

Policy alone does not prove commercial success. It should be interpreted with affected actors, required action, deadline, enforcement, commitment, and solution supply.

## Disequilibrium Archetypes

The current vocabulary is provisional.

```text
KNOWLEDGE LEADS MARKET
research/patents ↑↑ while commercial supply/attention lag

DEMAND OUTRUNS SUPPLY
demand ↑↑ while supply → and prices ↑

SUPPLY OUTRUNS AWARENESS
imports/availability ↑↑ and prices ↓ while attention →

POLICY CREATES DISCONTINUITY
binding rule changes economics while information/solutions lag

COMPLEXITY OUTRUNS INFORMATION
options/price dispersion ↑ while decision quality/tools lag

TECHNOLOGY OUTRUNS SERVICES
installed base ↑↑ while service capacity →

DOMESTIC DEMAND OUTRUNS PRODUCTION
consumption/imports ↑↑ while domestic production →

NARRATIVE OUTRUNS COMMITMENT
attention/capital/announcements ↑↑ while transactions/deployment lag

LATENT DEPENDENCY PRESSURE
dependent systems ↑↑ while required node appears flat or constrained

KNOWLEDGE CONVERGENCE
previously separate domains increasingly intersect around a new stack
```

These are hypotheses to test, not frozen classes.

## From Disequilibrium to Opportunity

A detected anomaly is not itself a business opportunity.

The reasoning chain should remain explicit:

```text
DISEQUILIBRIUM
    ↓
ECONOMIC CONSEQUENCE
    ↓
WHO IS AFFECTED?
    ↓
WHAT INFORMATION / CAPABILITY / ACCESS GAP EXISTS?
    ↓
ASYMMETRY
    ↓
POSSIBLE RESOLUTIONS
    ↓
POSSIBLE VALUE-CAPTURE MECHANISMS
    ↓
OPPORTUNITY
```

This prevents a common failure mode where a trend is converted directly into a product idea.

## Explainability Contract

A future opportunity view should be able to expose:

```text
what was detected
why it is unusual
which entities are involved
which observations support it
which observations contradict it
how source taxonomies were mapped
what causal interpretation is proposed
what assumptions are being made
what important evidence is missing
what alternative explanations exist
what would falsify the hypothesis
which resolutions are plausible
which monetization mechanisms are plausible
why the opportunity ranking changed over time
```

Explainability should be a consequence of preserved lineage, not generated prose pasted onto a score.

## Learning Loop

The strongest future asset is not a catalogue of static opportunities.

It is a history of economic beliefs and outcomes:

```text
what the Engine observed
what it inferred
why it inferred it
what decision followed
what evidence was purchased next
what experiment was run
what reality did
```

That history can later support empirical statements such as:

```text
when policy leads solution supply by X months
and commitment begins rising
historically Y% of similar cases produced monetizable demand
```

The system should eventually be able to re-evaluate historical evidence under newer interpretation models.

## Architectural Restraint

This document does not authorize building a graph database, ontology framework, vector database, or agent orchestration platform.

For the present modular monolith, concepts and relationships may remain simple Python structures and SQLite tables when a real vertical slice requires them.

The architecture should grow from empirical pressure.
