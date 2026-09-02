# Spec 012 — First Reasoning Vertical Slice

## Status

Implementation specification.

This spec is the first deliberate transition from **collecting evidence** to **reasoning over evidence**.

It must remain a small empirical vertical slice. Do not interpret this spec as authorization to build a general ontology, graph database, agent framework, scoring engine, or opportunity platform.

## Objective

Demonstrate that Asymmetry Engine can turn persisted source observations into an **inspectable economic argument** while preserving evidence lineage.

The slice should implement the smallest useful chain:

```text
SOURCE OBSERVATIONS
    ↓
MEASUREMENTS
    ↓
ECONOMIC ENTITY
    ↓
RELATIONSHIPS
    ↓
EVIDENCE RELATION
    ↓
DISEQUILIBRIUM
    ↓
STRUCTURED EXPLANATION
```

The purpose is not to prove that the economic interpretation is correct.

The purpose is to prove that the system can derive a bounded interpretation from evidence while making the derivation, assumptions, limitations, and alternatives inspectable.

## Why this slice now

Specs 009–011 created empirical pressure for reasoning structure:

- Comext showed that value and physical quantity must remain separate measurements.
- Comext drill-down showed that parent anomalies can be composition effects and that child contribution analysis materially changes interpretation.
- Partner drill-down showed that geography can reveal substitution, concentration, and supplier shifts invisible at aggregate level.
- OpenAlex showed that broad semantic categories can conceal sharply different trajectories and that source-native hierarchy is valuable without requiring graph infrastructure.
- Both sources reinforced that aggregation must not destroy lineage.

We now have enough evidence to test reasoning architecture directly instead of adding another connector.

## Selected empirical case

Use the strongest surviving Spec 010 case:

```text
CN75 — Nickel and articles thereof
Czechia imports
2023 → 2024
```

The broad evidence was:

```text
trade value: +26.74%
net mass:    +47.60%
derived value-per-mass diagnostic: -14.13%
```

Drill-down showed that the change was dominated by:

```text
CN8 75022000 — Unwrought nickel alloys
```

with strong contribution from France and Italy and increasing supplier concentration.

This case is deliberately selected because the anomaly **survived decomposition** rather than dissolving into pure composition noise.

## Core hypothesis

> A small explicit reasoning layer can convert raw Comext observations into an inspectable disequilibrium argument without losing provenance or prematurely generalizing the architecture.

## Required behavior

### 1. Work from persisted observations

The reasoning slice must consume `SourceObservation` records already persisted in SQLite.

Do not hard-code the 2023/2024 values from the research report into the reasoning output.

If the current production Comext collector does not yet persist the CN8/partner observations required for the CN75 case, the implementation may perform the smallest necessary bounded Comext collection extension to obtain them.

Any such extension must remain specific to this slice and must not become a generic hierarchical trade framework unless the existing code makes the generalization unavoidable.

### 2. Introduce only the minimal reasoning structures

The implementation may introduce small Python structures for concepts such as:

```text
EconomicEntity
Measurement
EvidenceRelationship
DisequilibriumArgument
```

Names may differ if the codebase suggests something clearer.

Do not create entities merely to match `docs/ECONOMIC_REASONING_MODEL.md`.

Every introduced structure must be required by the CN75 vertical slice.

### 3. Preserve source-native identity

The economic objects in this slice should preserve explicit source-native identifiers where relevant:

```text
CN2 75
CN8 75022000
partner FR
partner IT
```

Do not infer mappings to NACE, CPV, EPO, OpenAlex, industries, companies, or downstream applications.

### 4. Derive measurements explicitly

At minimum, derive and expose:

```text
2023 trade value
2024 trade value
value growth

2023 net mass
2024 net mass
mass growth

derived value-per-mass change

CN8 contribution to CN2 value change
CN8 contribution to CN2 mass change

selected partner contribution to CN8 change
supplier concentration for the selected CN8 product
```

The exact concentration metric may be HHI or a simpler concentration measure if justified by the available evidence.

Every derived measurement must retain enough lineage to identify the underlying observations used.

### 5. Represent relationships explicitly

At minimum, the reasoning layer must be able to express relationships equivalent to:

```text
CN8 75022000
    PART_OF
CN2 75

France
    SUPPLIES
CN8 75022000 → Czechia

Italy
    SUPPLIES
CN8 75022000 → Czechia
```

These relationships should be inspectable and should state whether they are:

```text
source-native / structural
or
interpretive / inferred
```

For this slice, CN hierarchy and reporter/partner trade relationships are source-native/structural.

Do not introduce a graph database.

### 6. Produce one structured disequilibrium argument

The output should be machine-readable in Python and printable through a small CLI command.

Suggested CLI shape:

```text
asymmetry-engine reason-cn75 --database <path>
```

The exact command name may differ if there is a better fit with the existing CLI.

The argument should expose at minimum:

```text
DETECTED
- what changed

WHY IT IS UNUSUAL
- value and mass changed at materially different rates

DECOMPOSITION
- which CN8 child explains the parent movement
- whether the parent anomaly survives decomposition

GEOGRAPHY
- which partner changes explain the selected CN8 movement
- whether concentration changed

SUPPORTED INTERPRETATION
- narrow statement justified by the evidence

NOT SUPPORTED
- claims the evidence cannot establish

ALTERNATIVE EXPLANATIONS
- plausible unresolved explanations

NEXT BEST EVIDENCE
- what source family would most reduce uncertainty

LINEAGE
- exact source observations supporting each major derived claim
```

### 7. Keep interpretation narrow

The supported interpretation should remain close to the evidence, for example:

> Czech imports of nickel expanded materially in physical terms from 2023 to 2024. The increase was dominated by unwrought nickel alloys, especially supply from France and Italy, while derived value per unit mass declined and supplier concentration increased.

It must **not** claim without further evidence that:

```text
nickel prices fell
Czech industrial demand increased
inventories were rebuilt
EV/battery demand caused the change
French or Italian production expanded
this is a commercial opportunity
```

Those belong in alternatives / unknowns / next evidence.

### 8. Explainability must come from lineage

Do not generate explanation prose independently of the measurements.

The printed explanation should be constructed from the structured reasoning object so that the prose is a view over inspectable evidence.

Principle:

> Explainability is reconstructed from preserved evidence and derivation, not pasted onto a score.

## Storage policy

Default: keep the reasoning objects **ephemeral/in-memory** for this slice.

Do not add persistent reasoning tables unless implementation demonstrates that the slice cannot remain inspectable without them.

If persistence pressure emerges, report it as an architectural finding rather than solving it automatically.

The existing observation schema remains the source of truth for evidence.

## Revision pressure

The known observation-vs-measurement-revision problem remains explicitly deferred.

Do not redesign observation identity in this spec.

If revised Comext values affect reproducibility, document the consequence in the completion report.

## Tests

Tests should cover at minimum:

1. Correct extraction of the required CN75 observations from the repository.
2. Correct 2023→2024 growth calculations.
3. Correct value/mass contribution calculations.
4. Correct partner contribution/concentration calculation.
5. Explicit CN2→CN8 parent/child relationship.
6. Lineage retains exact source observation identifiers.
7. Interpretation does not claim market price from derived value-per-mass.
8. Missing required evidence fails clearly rather than fabricating a complete argument.
9. CLI output is deterministic for a fixed evidence set.
10. Existing tests remain green.

## Live empirical run

Run the complete slice against live official Comext evidence in a fresh temporary SQLite database outside the repository.

The live run should demonstrate:

```text
collect evidence
    ↓
persist observations
    ↓
construct reasoning argument
    ↓
print inspectable explanation
```

Record the actual evidence counts and request count.

Do not commit the live database or downloaded source payloads.

## Required completion report

Return:

### 1. Implementation

- commit SHA
- files changed
- tests passed
- working-tree status

### 2. Evidence acquisition

- exact Comext request scope
- number of successful requests
- number of observations persisted
- first-run / repeat-run dedupe behavior
- any deviation from the existing Comext collector

### 3. Reasoning structures introduced

For every new production structure, explain:

```text
why it exists
which real requirement forced it
why a simpler representation was insufficient
```

### 4. Actual CN75 argument

Return the complete human-readable argument produced by the implementation.

### 5. Lineage example

For at least three major claims, show the exact chain:

```text
claim
→ derived measurement
→ source observation IDs
```

### 6. Architecture assessment

Answer:

- Did ephemeral reasoning objects remain sufficient?
- Did the slice create real pressure for persistent entity/relationship tables?
- Which relationship types were genuinely required?
- Which reasoning concepts in `ECONOMIC_REASONING_MODEL.md` were still unnecessary?
- Did explainability emerge naturally from lineage, or require duplicated prose logic?

### 7. Empirical verdict

Choose one:

```text
A — The reasoning vertical slice works and the minimal architecture is sufficient.
B — The reasoning chain is useful, but one specific missing abstraction is now forced.
C — The architecture is premature; raw/source-specific analysis remains more honest.
D — The selected case does not support a useful reasoning vertical slice.
```

Explain what reality taught us.

## Explicit non-goals

Do not implement:

```text
graph database
generic ontology framework
cross-source concept mapping
OpenAlex ↔ Comext mapping
opportunity scoring
LLM interpretation
agent orchestration
web UI
dashboard
vector database
embeddings
persistent belief/version tables
commercial recommendation engine
```

## Decision after Spec 012

Do not assume the next step.

After reviewing the live reasoning output, decide whether to:

```text
persist reasoning structures
add a second evidence family
add semantic mapping
add policy evidence
add commercial validation
or simplify the reasoning model
```

The architecture must continue to be earned empirically.
