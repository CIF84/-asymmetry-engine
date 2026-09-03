# Spec 039 — Documentation Truth Alignment

## Status

READY FOR EXECUTION

## Type

Bounded documentation maintenance. No runtime implementation. No empirical opportunity work.

## Baseline

Execute from synchronized `main` at or after:

`75594590896f21d9a8b1fb2c4c1285a3ef7a4190`

Experiment 038 is closed and accepted after independent review.

Experiments 030 and 035 remain live observation windows. Their response/reaction state MUST NOT be inspected during this work.

## Why this work is earned

The architecture audit in 037 found a second material adaptation need beyond revision-aware persistence: early top-level documentation still presents several original design hypotheses as current architecture or current strategy even though experiments 013–038 materially changed the Engine's operating model.

This is now a reconstructability problem.

Examples visible in current top-level docs include:

- a fixed `OBSERVE → NORMALIZE → EXTRACT → DETECT → PERSIST → SCORE → MONITOR → EXPERIMENT → MEASURE → LEARN` architecture;
- a first-class Asymmetry Registry assumed before repeated evidence justified one;
- additive economic scoring presented as the primary opportunity selector;
- automated decision extraction and clustering treated as required pipeline stages;
- `Automate discovery aggressively` presented as a design principle;
- milestone targets based on counts such as 1,000 observations, 100 decision signals, 20 asymmetries and TOP 10 ranking;
- a phase roadmap that implies the original pipeline remains the intended route to economic evidence;
- automation of collection/extraction/clustering/scoring/monitoring presented more strongly than the learned rule that automation should multiply validated patterns rather than compensate for unresolved uncertainty.

These documents are historically useful, but some statements are misleading when read as present-tense truth.

The purpose of 039 is not to rewrite history. It is to make the repository accurately distinguish:

1. current purpose and learned operating model;
2. current implemented software;
3. provisional hypotheses and unearned future capabilities;
4. historical design assumptions that have been superseded.

## Primary question

Can the top-level repository documentation be aligned with the empirically learned Engine without inventing new architecture, changing frozen empirical models, or erasing the history that produced the current design?

## Governing principle

Documentation should describe what the Engine **is**, what the code **currently does**, what evidence has **earned**, and what remains **hypothetical**.

It must not make aspirational architecture look implemented or empirically validated.

## Scope

Review and, where necessary, update only:

- `README.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`

Create the required Experiment 039 result artifact.

Do not modify any other documentation unless a broken direct reference created by these edits makes a tiny correction unavoidable. If so, report it explicitly.

## Explicitly frozen / prohibited

Do NOT modify:

- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- Experiment 030 artifacts or state
- Experiment 035 artifacts or state
- source code
- tests
- database schemas
- source adapters
- specifications other than the existence of this already-written spec

Do NOT:

- generate new opportunity candidates;
- perform RADAR or FORGE research;
- inspect live 030 Reddit state;
- inspect live 035 GitHub issue, comments, reactions, PR state, or related response state;
- contact any external actor;
- create a new conceptual architecture;
- create a new scoring model;
- create a new opportunity model;
- introduce new phase names merely for aesthetic completeness;
- add speculative components to make the docs look comprehensive.

## Evidence hierarchy

Use these sources in this order:

1. current repository code for what is implemented;
2. accepted experiment/checkpoint artifacts through 038 for what has been learned;
3. `docs/OPERATING_MODEL.md`, strategic/operational checkpoints, architecture audit and economic telemetry baseline for current operating constraints;
4. the existing README/ARCHITECTURE/ROADMAP as historical material to preserve where still valid.

If sources conflict, do not silently reconcile them. Prefer later empirical evidence and explicitly classify the earlier statement as historical/superseded where useful.

## Current purpose to preserve

The Engine remains oriented toward the broader ATLAS → RADAR → FORGE → PORTFOLIO → FREEDOM objective and toward discovering mechanisms capable of creating repeatable economic value.

Do not reduce the project to a research toy or remove commercialization/value-capture intent merely because willingness-to-pay and repeatability remain unproven.

At the same time, do not state revenue generation, willingness to pay, repeatability, scalable economics, or autonomous operation as established capabilities.

## Current learned definition

Where a concise current definition is useful, use this accepted formulation or a semantically equivalent shorter version:

> Asymmetry Engine is an experimental system for discovering economically consequential decisions under resolvable uncertainty, cheaply testing whether better information improves those decisions, and learning which resolution mechanisms can create and eventually capture repeatable value.

Do not silently broaden this definition.

## Current learned economic loop

The docs should no longer imply that one fixed automated pipeline is the validated architecture.

The current empirical loop is approximately:

```text
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
```

This is an operating/research loop, not a claim that every stage is implemented in software.

Make that distinction explicit.

The more detailed learned opportunity lifecycle may be referenced where useful:

```text
observe signal
  ↓
identify actor + live decision
  ↓
check intervention topology
  ↓
economic consequence
  ↓
meaningful uncertainty
  ↓
recoverability
  ↓
exact-resolution gap
  ↓
cheapest discriminator
  ↓
disposable resolution
  ↓
adversarial challenge
  ↓
authorized interaction
  ↓
measure effect
  ↓
value / capture / repeatability?
```

Do not turn this into a rigid software pipeline.

## Opportunity anatomy

The current conceptual anatomy is:

```text
ECONOMICALLY CONSEQUENTIAL UNCERTAINTY
× RECOVERABLE INFORMATION
× INADEQUATE EXISTING RESOLUTION
× RESOLUTION FEASIBILITY
× ACCESSIBLE DECISION SURFACE
× OBSERVABLE EFFECT
× PLAUSIBLE VALUE CAPTURE
```

Fatal constraints can dominate. This is why the old additive scoring-first worldview is not current policy.

Do not implement or document a new numeric score.

## Automation policy

Replace aggressive automation language with the empirically learned policy:

> Automation should multiply validated asymmetries and repeated mechanical work, not compensate for weak opportunities or unresolved assumptions.

Manual semantic judgment remains appropriate when it is the cheapest reliable discriminator.

Automation must be earned by repeated observed problems, mechanical reusability, improved future experiment economics, and small reversible implementation.

## Current software truth

The docs must accurately state that the implemented software is intentionally smaller than the learned conceptual Engine.

At baseline 039 it consists principally of:

- bounded public-source collectors/adapters;
- normalized source observations;
- SQLite persistence and pipeline-run records;
- revision-aware append-only observation captures from 038;
- deterministic latest/current observation retrieval;
- source metadata/provenance primitives;
- one domain-specific CN75 economic reasoner;
- CLI/test infrastructure.

There is currently NO generic software implementation for:

- opportunity detection;
- generic RADAR;
- additive or learned opportunity scoring;
- monitoring engine;
- experiment database;
- interaction engine;
- generic FORGE/decision engine;
- autonomous research policy;
- autonomous authorization;
- revenue-asset management;
- portfolio management.

Do not make absence sound like unfinished negligence. Several absences are deliberate because evidence has not earned implementation.

## Persistence truth after 038

Update any persistence descriptions that would now mislead readers.

Current observation semantics include:

```text
logical source item = (source_id, external_id)

materially unchanged recapture
    → suppressed as duplicate

materially changed recapture
    → append new capture_sequence

current reader
    → highest capture_sequence per logical item
```

Do not claim generic event sourcing, temporal database semantics, or complete provenance infrastructure.

Source-registry history remains explicitly unresolved/deferred.

## Scoring truth

The old additive scoring model is superseded as primary selection logic.

Where historical scoring concepts are retained, label them clearly as early design hypotheses rather than current architecture.

Current learned policy:

- use fatal gates where one missing condition destroys the opportunity;
- use the cheapest discriminator capable of changing the decision;
- do not aggregate away decisive uncertainty;
- do not implement a generic scoring engine yet.

## Exact-resolution truth

Exact-resolution checking has repeatedly been economically useful and is now a core research policy.

However, it remains substantially semantic and manual.

Do not invent a resolver service, competition database, ontology, embedding pipeline, or automated semantic comparison system.

## FORGE truth

FORGE has repeatedly produced a useful pattern:

```text
UNSTRUCTURED UNCERTAINTY
        ↓
STRUCTURED UNCERTAINTY
        ↓
OPTIONS
        ↓
DISCRIMINATORS
        ↓
TESTABLE NEXT QUESTION
        ↓
DECISION-READY RESOLUTION
```

This supports decision compression as a provisional reusable capability.

It does NOT justify a generic decision engine.

## INTERACT truth

Public decision surfaces have become important because they may function as both sensor and intervention surface.

But Experiments 030 and 035 are still live during this spec.

Therefore:

- describe same-surface intervention/effect observability as an active empirical hypothesis/policy direction;
- do not claim actor-facing effect is validated;
- do not inspect those experiments to update the wording;
- do not document response outcomes before their observation windows close.

## Controls and authorization truth

Preserve the learned invariant:

```text
SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS
```

Consequential external action requires explicit user authorization.

The current control model is procedural/manual. Do not imply a permission service, policy engine or autonomous action layer exists.

## Economic telemetry truth

Experiment 036 established only a partial baseline.

The docs may say that prospective active time, spend, human attention, controls, interactions, verdicts and yield should be captured manually in experiment artifacts where useful.

Do not claim the Engine is quantitatively faster, cheaper, economically productive, or compounding revenue unless evidence supports it.

Do not add telemetry software to the roadmap as an earned near-term implementation.

## README requirements

README should become the best concise entry point for a new reader.

It should answer, without requiring historical knowledge:

1. What is Asymmetry Engine now?
2. What problem is it trying to solve?
3. What has the project learned about opportunity discovery?
4. What is actually implemented today?
5. What is deliberately still manual?
6. How does empirical development work?
7. What does success ultimately mean?

Preserve useful ideas from the current README where still true, especially:

- implementation is becoming less scarce;
- valuable problem selection remains important;
- software is not the default answer;
- public signals can produce proprietary learning;
- source independence;
- fail cheaply;
- commercialization remains part of the objective.

Remove or reframe unsupported current-tense claims about Asymmetry Registry, aggressive automation, additive scoring, automatic discovery/ranking and cash-flowing assets.

README should distinguish clearly between:

```text
CURRENT SOFTWARE
CURRENT OPERATING MODEL
LONG-TERM DIRECTION
```

without becoming a giant historical report.

## ARCHITECTURE requirements

ARCHITECTURE.md should primarily describe:

1. the architecture that actually exists;
2. the boundaries that are intentionally manual;
3. architectural principles learned from experiments;
4. what implementation is earned versus explicitly unearned;
5. how the code may evolve under evidence pressure.

Replace the old aspirational directory tree and component inventory where it falsely implies implemented modules.

A useful distinction is:

```text
WORLD
  ↓
SOURCE ADAPTERS
  ↓
OBSERVATION / RUN PERSISTENCE
  ↓
DOMAIN-SPECIFIC REASONING WHERE EARNED

---------------- manual empirical boundary ----------------

RADAR / DISCRIMINATION / FORGE / INTERACT / MEASURE / LEARN
```

This is illustrative, not mandatory formatting.

Preserve valid architectural principles such as modular monolith, source independence, explicit provenance, low complexity, SQLite, deterministic computation where appropriate, and evidence-driven evolution.

Explicitly retire as current architecture:

- generic DecisionSignal pipeline;
- generic Asymmetry Registry;
- ScoreSnapshot infrastructure;
- generic monitoring engine;
- generic Experiment/Outcome/Asset persistence;
- automatic clustering/embeddings taxonomy pipeline;
- scheduled orchestration as a near-term assumption.

These may be mentioned only as historical or future possibilities requiring new evidence.

## ROADMAP requirements

The existing numbered phase roadmap has been overtaken by empirical development and should not continue to imply that the project must sequentially build extraction → registry → scoring → monitoring → commercialization.

Replace it with an evidence-gated roadmap.

The roadmap should express that future work is selected by unresolved uncertainty and observed scar tissue, not by filling predetermined architecture boxes.

Recommended conceptual structure:

```text
NOW
- complete already-authorized empirical observation windows;
- preserve evidence quality and reconstructability;
- make only small evidence-earned technical adaptations.

NEXT GATE
- interpret 030/035 only after their windows close;
- update strategic/operational hypotheses based on observed world response;
- choose the cheapest next experiment capable of resolving the dominant uncertainty.

WHEN EARNED
- automate repeated mechanical work;
- improve reusable resolution support;
- test value creation;
- test value capture;
- test repeatability;
- only then scale validated workflows/assets.

LONG TERM
- portfolio of low-maintenance economically useful assets;
- reusable research/resolution infrastructure;
- progressively lower cost to economic evidence;
- FREEDOM rather than software volume as terminal objective.
```

Do not hard-code future experiment numbers beyond already existing 030/035/038 context.

Remove stale calendar promises such as first 7/14/30/45/60/90-day targets unless retained explicitly as historical initial planning assumptions.

## History preservation

Do not erase the fact that the project began with a different model.

Where helpful, include a short section such as `Historical design note` explaining that early documents assumed a generic signal→decision→asymmetry→score pipeline, while experiments falsified or weakened several assumptions.

Do not preserve large obsolete sections merely for archaeology; Git already preserves exact history.

The current files should optimize for present truth.

## Documentation consistency checks

After editing, verify that the three top-level docs do not materially contradict one another on:

- project definition;
- operating loop;
- current software capabilities;
- scoring policy;
- automation policy;
- role of manual judgment;
- external-action authorization;
- economic validation status;
- long-term objective.

Search the edited files for stale present-tense phrases/concepts including:

```text
Automate discovery aggressively
Asymmetry Registry
ScoreSnapshot
TOP 10
1,000 observations
100 plausible decision signals
20 evidence-backed candidate asymmetries
persistent asymmetry registry
Monitoring + Scoring
detect run
asymmetries list
```

A phrase may remain only if clearly historical, explicitly unearned, or otherwise accurately qualified.

## Adversarial review

Before finalizing, ask:

1. Did we accidentally turn the latest conceptual model into another rigid architecture?
2. Did we describe manual empirical practice as implemented software?
3. Did we overclaim what 030/035 prove before their windows close?
4. Did we erase commercialization/value capture because it remains unproven?
5. Did we preserve obsolete scoring/automation assumptions through vague wording?
6. Did we introduce any new system not earned by experiment evidence?
7. Could a new contributor distinguish current code from current research process after reading these files?

Correct any failure before completion.

## Validation

No source-code change is permitted, but run the existing test suite after documentation edits as a repository-integrity check.

Record the result.

Also run an appropriate repository diff/status check and confirm only allowed documentation/result files changed.

## Required result artifact

Create:

`experiments/039/documentation-truth-alignment.md`

It must record:

- baseline commit;
- prospective active-work timing;
- spend;
- isolation confirmation;
- files reviewed;
- files changed;
- stale assumptions found;
- how each was resolved;
- important current truths preserved;
- historical material intentionally removed/reframed;
- contradictions discovered across docs;
- contradictions remaining, if any;
- test result;
- diff/status result;
- what was explicitly not changed;
- overall verdict;
- exactly one recommended next action.

## Verdicts

### A — DOCUMENTATION ALIGNED

The three top-level documents accurately distinguish current software, learned operating model, unproven hypotheses and long-term direction; no material stale present-tense architecture remains.

### B — MATERIAL IMPROVEMENT, RESIDUAL AMBIGUITY

Major stale claims were corrected but at least one meaningful ambiguity remains and is explicitly identified.

### C — NO MATERIAL CHANGE NEEDED

Audit shows the docs were already sufficiently aligned. This verdict requires strong evidence because 037 identified staleness.

### D — INVALID

Scope, isolation, evidence, or repository-integrity requirements were violated.

## Budget

Target active work: 20–35 minutes.

Hard ceiling: 50 active minutes.

Incremental external spend: €0.

Use a prospective timer. Stop early if the three documents are clearly aligned and validation passes. Do not fill the time budget.

## Completion report

Return exactly these 25 sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. README assessment before
7. README changes
8. ARCHITECTURE assessment before
9. ARCHITECTURE changes
10. ROADMAP assessment before
11. ROADMAP changes
12. Current project definition after
13. Current operating loop after
14. Current software truth after
15. Manual/unimplemented boundaries after
16. Scoring policy after
17. Automation policy after
18. Authorization/control policy after
19. Historical assumptions preserved or reframed
20. Cross-document consistency result
21. Stale-term search result
22. Test-suite result
23. Files changed
24. Artifact path and commit SHA
25. Exactly one recommended next action

## Success criterion

A new technically literate reader should be able to read README, ARCHITECTURE and ROADMAP and correctly understand:

```text
what exists
what has been learned
what remains manual
what remains unproven
what could be built later
and why the Engine is deliberately not larger yet
```

The result is successful if it improves repository truthfulness and reconstructability without creating any new architecture.