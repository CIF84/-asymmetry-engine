# Spec 037 — Architecture Gap Audit

## Status

Architecture / engineering audit.

This is a **parallel technical track** while Experiments 030 and 035 remain in their observation windows.

It must not generate new opportunity candidates, modify the frozen opportunity model, inspect live 030/035 response evidence, contact external actors, or implement speculative architecture.

The purpose is to determine whether the software created primarily during Experiments 001–012 still supports the operating model learned empirically through Experiment 036.

---

## Primary question

> **Does the current software architecture still support the Engine we have empirically discovered, and which gaps—if any—have accumulated enough repeated evidence to justify small, reversible implementation?**

---

## Context

The early software architecture was approximately:

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
```

Later experiments shifted the economic operating model toward:

```text
WORLD
  ↓
OBSERVE
  ↓
RADAR
  ↓
DISCRIMINATE
  ↓
FORGE
  ↓
INTERACT
  ↓
MEASURE
  ↓
LEARN
  ↺
ATLAS
```

with a cross-cutting control plane for:

```text
EVIDENCE
PROVENANCE
FRESHNESS
REGULATION
PERMISSIONS
AUTHORIZATION
RESOURCES
STOP RULES
ADVERSARIAL CHALLENGE
ESCALATION
```

This target model is conceptual. It is **not authorization to build those concepts as services, schemas, agents, or infrastructure**.

The audit must test the code against observed needs rather than map every conceptual box to a software component.

---

## Governing implementation filter

For every proposed change ask, in order:

```text
REPEATED OBSERVED PROBLEM?
        │
       no ──→ DOCUMENT ONLY
        │
       yes
        ↓
MECHANICALLY REUSABLE?
        │
       no ──→ KEEP MANUAL
        │
       yes
        ↓
IMPROVES FUTURE EXPERIMENT ECONOMICS?
        │
       no ──→ DEFER
        │
       yes
        ↓
SMALL + REVERSIBLE IMPLEMENTATION?
        │
       no ──→ WAIT
        │
       yes
        ↓
IMPLEMENTATION MAY BE EARNED
```

The audit may conclude that zero code changes are earned.

---

## Required evidence sources

Inspect the current repository implementation, including as applicable:

- `src/`
- `tests/`
- CLI / entry points
- persistence/schema/migrations
- source adapters
- normalization/extraction/detection/scoring code
- configuration
- `ARCHITECTURE.md`
- `README.md`
- `ROADMAP.md`
- relevant docs and checkpoints
- experiment artifacts only where needed to establish repeated operational pain

Use current code as the source of truth for implemented behavior.

Use empirical documents as the source of truth for learned operating needs.

Do not infer implementation from architecture documentation if code contradicts it.

---

## Isolation requirements

Do not:

- inspect live Reddit state for Experiment 030;
- inspect live GitHub issue/reaction/state evidence for Experiment 035;
- modify 030 or 035 artifacts;
- modify `docs/OPPORTUNITY_MODEL_001_035.md`;
- modify `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`;
- perform external outreach or interaction;
- create new opportunity hypotheses;
- start a new RADAR/FORGE/INTERACT experiment;
- implement code during the audit.

This spec produces an audit and implementation recommendation only.

---

## Classification model

Every material architecture capability or mismatch must be classified into exactly one primary category.

### KEEP

Current implementation remains useful and consistent with learned needs.

### ADAPT

The underlying primitive is useful, but its abstraction, boundary, naming, or assumptions no longer fit the learned operating model.

### MISSING BUT EARNED

Repeated empirical need exists; the capability is mechanically reusable; implementing it would plausibly reduce future experiment cost/error; and a small reversible implementation is identifiable.

### MISSING BUT UNEARNED

The capability is conceptually attractive but repeated empirical evidence does not yet justify implementation.

### OBSOLETE / CONTRADICTED

The implementation encodes an assumption materially weakened or contradicted by later experiments and risks steering future work incorrectly.

Do not use `OBSOLETE` merely because a module has not recently been exercised.

---

## Audit dimensions

### 1. Source observation and adapters

Ask:

- Are source adapters appropriately persistence-agnostic?
- Does source identity remain stable enough for provenance?
- Can freshness/effective-date information be represented where relevant?
- Are source-specific assumptions leaking into generic layers?
- Did later experiments repeatedly require evidence primitives the source layer cannot preserve?

Do not propose a generic source platform without repeated need.

---

### 2. Evidence and provenance

Later experiments repeatedly distinguished:

```text
KNOWN
PUBLIC / AUTHORITATIVE FACT
DERIVED / ESTIMATED
UNKNOWN / VERIFY
```

and required source provenance, freshness, effective dates, caveats, and unsupported-claim discipline.

Ask whether current persistence and domain objects can preserve the evidence required to reproduce or challenge a conclusion.

Distinguish:

- raw observation evidence;
- normalized facts;
- derived interpretation;
- mutable current belief/state.

Do not assume these need separate services or databases.

---

### 3. Persistence

Audit the current SQLite model and transaction boundaries against learned principles:

- immutable evidence versus mutable interpretation;
- source/run isolation;
- reproducibility;
- lifecycle state;
- event/change history;
- provenance;
- revision identity;
- incomplete/failed source runs.

Identify whether the persistence model is genuinely blocking current experiments or simply incomplete relative to an aspirational target.

---

### 4. Detection / opportunity abstraction

Inspect what `DETECT` currently means in code.

Ask whether it still represents a useful mechanical transformation or whether later evidence has made the abstraction misleading.

Specifically test for assumptions such as:

- signal automatically implies opportunity;
- friction implies demand;
- novelty implies residual opportunity;
- information dispersion implies asymmetry;
- detection can happen without actor/decision context.

Do not replace it with a generic opportunity engine unless earned.

---

### 5. Scoring

This deserves explicit adversarial review.

Later experiments repeatedly found fatal or near-fatal constraints:

```text
no live decision
no consequence
unrecoverable information
adequate exact resolver
no legitimate actor access
unobservable effect
control/regulatory block
```

Ask:

- What does current scoring code actually score?
- Is it used operationally?
- Does additive scoring permit a candidate with a fatal constraint to appear attractive?
- Is scoring still a useful ranking primitive after hard gates?
- Is it dead code, useful code, or a contradicted abstraction?

Do not automatically delete scoring. Determine the evidence-supported role first.

---

### 6. Exact-resolution / competition checking

Experiments 020 onward repeatedly used exact functional resolution as an early discriminator.

Ask:

- Is any reusable code justified?
- Which parts were repeated mechanically versus requiring semantic judgment?
- Could a small evidence-recording or search-support primitive reduce repeated work without pretending to automate functional competition analysis?

Bias toward keeping semantic judgment manual unless repetition clearly supports code.

---

### 7. Experiment contracts

Experiments increasingly rely on specs as preregistration containing:

- question;
- hypothesis;
- decision affected;
- method;
- evidence requirements;
- controls;
- budgets;
- stop rules;
- prohibited actions;
- authorization boundary;
- verdict definitions.

Ask whether any software representation is earned.

Markdown may remain the correct implementation.

Do not create an experiment database/schema merely because experiments are conceptually first-class objects.

---

### 8. Authorization and consequential actions

Repeated incidents established:

```text
SPECIFICATION ≠ AUTHORIZATION
AUTHORIZATION ≠ CAPABILITY
CAPABILITY ≠ ACCESS
```

Ask whether the current software can accidentally blur these boundaries.

Determine whether a small reusable guard/contract is warranted for future external-action executors, or whether explicit procedural control remains sufficient.

Do not implement autonomous authorization.

---

### 9. Controls and regulation

Review whether repeated controls justify software support for:

- prohibited actions;
- external-interaction limits;
- spend ceilings;
- source/platform restrictions;
- stop conditions;
- review-required states.

Do not build a regulatory rules engine, policy engine, or permission service unless the audit finds evidence that the smallest useful capability requires it.

---

### 10. Operational telemetry

Experiment 036 concluded that prospective telemetry is warranted but implementation is not yet earned.

Audit whether any existing code or CLI makes the minimum telemetry block unusually cheap to capture without adding infrastructure.

Preserve the 036 conclusion unless code inspection reveals a materially cheaper zero/near-zero-complexity mechanism.

Do not build a database/dashboard.

---

### 11. Research policy

The discovery policy evolved through:

```text
ASYMMETRY-FIRST
→ BEHAVIOR-FIRST
→ SIGNAL-NATIVE
→ PRE-CONSOLIDATION
→ ACCESSIBLE-SURFACE-FIRST
→ ACTOR + EFFECT OBSERVABILITY FIRST
```

Ask whether any of this belongs in code today.

Default assumption: research policy remains learned/manual until repeated stable mechanical operations emerge.

Challenge that assumption with code evidence, but do not encode conceptual gates merely because they exist in documentation.

---

### 12. FORGE / decision compression

Experiments 025, 029, 033, and 034 suggest a recurring transformation:

```text
UNSTRUCTURED UNCERTAINTY
→ STRUCTURED UNCERTAINTY
→ OPTIONS
→ DISCRIMINATORS
→ TESTABLE NEXT QUESTION
→ DECISION-READY RESOLUTION
```

Ask which parts, if any, are mechanically reusable today.

Distinguish reusable document/evidence structure from domain reasoning.

Do not build a generic decision engine without evidence.

---

### 13. Interaction / measurement

Experiments 026, 030, and 035 exposed delivery/exposure/effect distinctions.

Ask whether the current software has any relevant primitives and whether implementation is earned before final 030/035 results exist.

Because those experiments remain open, treat effect-measurement implementation as especially likely to be premature.

---

### 14. ATLAS / learned state

The repository currently uses docs/checkpoints/history as durable learned state.

Ask:

- Can a fresh operator reconstruct what the Engine believes and why?
- Are important learned policies discoverable?
- Is knowledge fragmented enough to impose repeated operational cost?
- Would software improve this today, or is documentation/indexing sufficient?

Do not build a knowledge graph or vector store without repeated evidence.

---

### 15. Tests and developer ergonomics

Audit:

- whether existing tests protect meaningful invariants;
- stale tests protecting obsolete abstractions;
- gaps around persistence/provenance/source isolation;
- CLI usability;
- repository identity safeguards;
- deterministic/reproducible execution where appropriate.

Small test/invariant improvements may be among the safest earned implementation candidates.

---

## Architecture scar-tissue map

For each material gap, identify the experiment(s) that created the scar tissue.

Format:

| Observed problem | Evidence | Current code implication | Classification |
|---|---|---|---|

A gap without empirical provenance should normally be `MISSING BUT UNEARNED`.

---

## Required current-code map

Produce a concise map of actual current implementation:

```text
MODULE / COMPONENT
→ responsibility
→ persisted state if any
→ callers / entry path
→ tests
→ current operational use
```

The purpose is to compare reality with architecture documentation, not produce exhaustive API documentation.

---

## Required stale-assumption audit

Explicitly search current code/docs for assumptions materially challenged by later evidence, including:

- additive opportunity scoring;
- generic asymmetry detection;
- fixed opportunity taxonomy;
- friction/demand conflation;
- signal/opportunity conflation;
- source hierarchy as semantics;
- derived value as market price;
- generic survival thresholds;
- automation-before-validation;
- external action without separate authorization;
- mutable evidence;
- current-state records without provenance/history.

For each match distinguish:

```text
CODE RISK
DOCS-ONLY STALENESS
HISTORICAL BUT HARMLESS
NOT PRESENT
```

---

## Required implementation candidate ranking

If any `MISSING BUT EARNED`, `ADAPT`, or `OBSOLETE` items warrant code changes, rank at most **five** candidates using qualitative dimensions:

- repeated empirical pain;
- expected reduction in experiment cost/error;
- implementation size;
- reversibility;
- coupling risk;
- dependence on unresolved 030/035 evidence.

Do not assign synthetic numeric scores.

For each candidate provide:

```text
problem
observed evidence
smallest useful change
what it deliberately does NOT solve
expected benefit
main risk
030/035 dependency
implementation verdict
```

---

## Implementation verdicts

Each candidate must receive one:

### BUILD NOW

Repeated, mechanical, useful, small, reversible, and independent of pending evidence.

### SPEC NEXT

Likely earned but requires a bounded implementation spec before code.

### KEEP MANUAL

Repeated but judgment-heavy or cheaper manually.

### DEFER

Potentially useful but evidence/economics insufficient.

### REMOVE / RETIRE

Current implementation creates meaningful risk because its assumptions are contradicted and it no longer provides compensating value.

---

## Required artifact

Create:

`docs/ARCHITECTURE_GAP_AUDIT_001_036.md`

Required sections:

1. Executive verdict
2. Scope and isolation
3. Actual current-code map
4. Learned operating-model requirements
5. KEEP inventory
6. ADAPT inventory
7. MISSING BUT EARNED inventory
8. MISSING BUT UNEARNED inventory
9. OBSOLETE / CONTRADICTED inventory
10. Architecture scar-tissue map
11. Source/adapters assessment
12. Evidence/provenance assessment
13. Persistence assessment
14. Detection/opportunity assessment
15. Scoring assessment
16. Exact-resolution assessment
17. Experiment-contract assessment
18. Authorization/control assessment
19. Telemetry assessment
20. Research-policy assessment
21. FORGE/decision-compression assessment
22. INTERACT/measurement assessment
23. ATLAS/durable-learning assessment
24. Tests/developer-ergonomics assessment
25. Stale-assumption audit
26. Ranked implementation candidates, maximum five
27. What must explicitly NOT be built now
28. Architecture changes dependent on 030/035
29. Overall code-health conclusion
30. Exactly one recommended next action

---

## Prohibited implementation proposals unless extraordinary evidence is found

The burden of proof is intentionally high for:

- orchestration engine;
- autonomous research scheduler;
- multi-agent critic framework;
- regulatory rules database;
- generic policy engine;
- permission service;
- experiment database;
- generic opportunity scoring engine;
- governance UI;
- telemetry dashboard;
- knowledge graph;
- vector-store ATLAS;
- automated Codex launcher;
- autonomous outreach;
- generic decision engine;
- generic ontology/graph layer.

If the audit nevertheless recommends one, it must cite repeated empirical evidence showing why a smaller solution cannot address the observed problem.

---

## Verdicts

### A — ARCHITECTURE FITS WITH MINOR EARNED CHANGES

Core architecture remains useful and only bounded changes are justified.

### B — MATERIAL ADAPTATION EARNED

Repeated evidence shows one or more current abstractions materially impede the learned operating model, and small/reversible adaptation is justified.

### C — DOCUMENTATION / MANUAL MODEL AHEAD OF CODE, BUT CODE CHANGE NOT YET EARNED

The conceptual operating model has evolved substantially, but current software is not yet blocking experiments enough to justify implementation.

### D — CURRENT ARCHITECTURE MATERIALLY CONTRADICTS LEARNED MODEL

Existing code actively steers the Engine toward invalid assumptions and requires bounded corrective work before further software-dependent experiments.

### E — INVALID / INSUFFICIENT AUDIT

Repository evidence or isolation is insufficient for a defensible conclusion.

---

## Resource budget

Target active time: **45–60 minutes**.

Hard ceiling: **90 minutes**.

Incremental spend: **€0**.

Use a prospective active-work timer from the beginning and record the timing method.

No external interaction.

No code changes.

---

## Stop rules

Stop when:

- actual current architecture is mapped sufficiently to identify material mismatches;
- each major learned requirement is classified;
- implementation candidates are reduced to at most five;
- every candidate passes through the governing implementation filter;
- further code archaeology is unlikely to change the verdict or top recommendation.

Do not exhaustively document the codebase.

---

## Success condition

Success means answering:

> **What should we keep, adapt, build, keep manual, defer, or retire so that the software supports the empirically learned Engine without prematurely encoding the still-uncertain parts of the model?**

A zero-code recommendation is a valid success.

---

## Required completion report

Return exactly:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Current architecture summary
7. Strongest KEEP finding
8. Strongest ADAPT finding
9. Strongest MISSING BUT EARNED finding
10. Strongest MISSING BUT UNEARNED finding
11. Strongest OBSOLETE / CONTRADICTED finding
12. Source/adapters conclusion
13. Evidence/provenance conclusion
14. Persistence conclusion
15. Detection/opportunity conclusion
16. Scoring conclusion
17. Exact-resolution conclusion
18. Experiment-contract conclusion
19. Authorization/control conclusion
20. Telemetry conclusion
21. Research-policy conclusion
22. FORGE conclusion
23. INTERACT conclusion
24. ATLAS conclusion
25. Tests/developer-ergonomics conclusion
26. Stale-assumption risks
27. Ranked implementation candidates
28. What must not be built
29. 030/035-dependent changes
30. Overall code-health conclusion
31. Artifact path
32. Commit SHA
33. Exactly one recommended next action
