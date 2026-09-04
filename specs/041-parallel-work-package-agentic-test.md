# Spec 041 — Parallel Work-Package Agentic Test

## Status

READY FOR EXECUTION

## Type

Bounded operating-model replication. Repository-only shadow work. No product architecture change. No runtime implementation. No external actor interaction.

## Baseline

Execute from synchronized `main` at or after:

`44f7fb11c3f3a039aa87f52a9828111a1928bc4b`

Experiment 040 is complete with Verdict B — PROMISING BUT INCONCLUSIVE.

Experiments 030 and 035 remain live external observation windows and MUST NOT be inspected, refreshed, inferred, or modified during 041.

## Why this experiment is earned

Experiment 040 established a narrow but real mechanism:

- a Producer intermediate returned PASS;
- independent Reviewer and Adversary roles found material overclaim/citation/comparability problems;
- synthesis repaired those issues before human review;
- both final blind packets were accepted with High clarity/confidence and no human correction;
- treatment human review time was only 3 seconds lower than control, too small to establish practical HAL benefit;
- treatment successful-path elapsed time was 361 seconds versus 117 seconds for control, 3.09× worse;
- compute/model cost remained UNKNOWN.

Therefore 040 did **not** establish that more agents improve operating economics.

It did establish that role-separated machine disagreement can provide quality protection without forcing the human to inspect intermediate work.

The next distinct hypothesis is not more epistemic redundancy. It is whether **genuinely parallel independent work packages can shorten a real critical path while preserving the compressed human interface**.

041 isolates that mechanism.

## Primary hypothesis

> For a frozen repository-only workload with two genuinely independent evidence packages, parallel agent execution can reduce accepted-output wall-clock time without materially increasing human attention or degrading output quality.

## Null hypothesis

> Decomposition, coordination, duplicated context reconstruction, and integration overhead erase the parallelism benefit, so the multi-agent treatment provides no practically meaningful operating advantage over one agent completing the same packages sequentially.

## What 041 is NOT testing

041 does not test:

- multi-agent epistemic redundancy as the primary mechanism;
- Reviewer/Adversary value again;
- autonomous project management;
- autonomous RADAR/FORGE;
- external research concurrency;
- coding concurrency;
- long-lived agents;
- persistent orchestration;
- automatic delegation policy;
- commercial value from agents;
- 10×/100× acceleration.

Do not attach Producer → Reviewer → Adversary chains to each package. That would confound the mechanism under test.

## Governing agent principle under test

Candidate principle only:

> Agent count should follow independent uncertainty structure, not task size.

041 may support, weaken, or reject this principle. It must not be promoted to canonical operating policy during this experiment.

## Frozen canonical surfaces

Do NOT modify:

- `README.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `docs/OPERATING_MODEL.md`
- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_REASONING_MODEL.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- `docs/ARCHITECTURE_GAP_AUDIT_001_036.md`
- source code under `src/`
- tests under `tests/`
- prior specs
- prior experiment artifacts
- Experiment 030 artifacts/state
- Experiment 035 artifacts/state
- Experiment 040 artifacts

Only Experiment 041 artifacts may be persistently added.

## Authority boundary

Agents may read repository evidence, inspect Git history already in the repository, perform deterministic calculations, create isolated temporary outputs, and persist final Experiment 041 artifacts.

Agents may not contact actors, browse or refresh live 030/035 external state, mutate canonical truth, push/merge unrelated changes, build orchestration infrastructure, or use paid external services beyond ordinary already-authorized model execution without explicit approval.

## Matched workload

### Overall task

Produce a **Repository Reconstructability Packet** answering:

> Can a technically literate new operator reconstruct both the implemented software truth and the empirical operating/governance truth of Asymmetry Engine from the repository alone, and where are the remaining material reconstruction ambiguities?

The final packet must distinguish:

```text
WHAT EXISTS IN SOFTWARE
WHAT EXISTS AS MANUAL / DOCUMENTARY OPERATING PRACTICE
WHAT IS EMPIRICALLY LEARNED BUT NOT IMPLEMENTED
WHAT REMAINS UNPROVEN
WHAT A NEW OPERATOR MUST NOT INFER
```

This workload is useful but shadow-only. Its output does not become canonical project truth.

### Work Package A — Implemented Software Truth

Using repository-local code/tests/docs only, reconstruct:

1. implemented modules and current entry points;
2. source-adapter boundary and responsibilities;
3. current SQLite tables and transaction boundary;
4. revision-aware observation semantics from Experiment 038;
5. current/latest read semantics;
6. implemented domain-specific reasoning capability;
7. tests/invariants protecting the implementation;
8. explicitly absent generic software capabilities;
9. any material discrepancy between code and current `ARCHITECTURE.md`;
10. confidence/unknowns.

Primary evidence should come from current code and tests, with documentation used as a cross-check rather than source of implementation truth.

### Work Package B — Empirical Operating and Governance Truth

Using repository-local docs/specs/experiments only, reconstruct:

1. current empirical operating loop;
2. opportunity-discrimination policy;
3. exact-resolution role;
4. FORGE/decision-compression status;
5. interaction/exposure/effect distinctions;
6. specification/authorization/capability/access boundary;
7. prospective telemetry policy;
8. evidence-earned automation rule;
9. current evidence boundary: what is supported vs still unproven;
10. any material discrepancy among README, ROADMAP, operating-model/checkpoint artifacts;
11. confidence/unknowns.

Do not inspect live 030/035 external state. Use only already-persisted artifacts.

## Independence test before treatment execution

Before delegating the treatment, explicitly verify:

1. Package A can be answered without Package B output.
2. Package B can be answered without Package A output.
3. Neither package mutates shared state.
4. Each package can produce a frozen artifact independently.
5. Integration requires comparison/reconciliation but not re-execution of both packages from scratch.

If these conditions materially fail, stop with INVALID DESIGN rather than manufacturing parallelism.

## Required final packet schema

Both arms must produce an equivalent final packet containing exactly these conceptual sections:

```text
ARM
BASELINE
START/END TELEMETRY
PACKAGE A SUMMARY
PACKAGE B SUMMARY
CROSS-BOUNDARY RECONCILIATION
MATERIAL RECONSTRUCTION AMBIGUITIES
WHAT A NEW OPERATOR MUST NOT INFER
CONFIDENCE / LIMITATIONS
FINAL VERDICT
```

The final verdict must classify repository reconstructability as one of:

```text
STRONG
ADEQUATE WITH BOUNDED AMBIGUITIES
WEAK
INVALID ASSESSMENT
```

No final packet may modify canonical docs or recommend immediate architecture changes.

## Control arm — sequential single agent

One Codex agent receives the full frozen workload.

It must:

1. complete Package A;
2. complete Package B;
3. reconcile them;
4. produce the final control packet.

It may choose its internal ordering but may not delegate.

Record prospectively:

- overall start/end;
- Package A start/end if practicable;
- Package B start/end if practicable;
- synthesis/reconciliation interval if practicable;
- retrieval retries;
- human clarifications/interventions;
- context restarts;
- output bytes/tokens if exposed;
- compute/model cost if exposed.

Required frozen control artifact:

`experiments/041/control.md`

## Treatment arm — parallel packages + integrator

Use exactly three logical roles unless an environment failure requires a documented retry:

```text
PACKAGE-A AGENT ─┐
                 ├→ INTEGRATOR
PACKAGE-B AGENT ─┘
```

Package A and Package B agents must:

- start from the same frozen baseline;
- run independently;
- not read each other;
- write only isolated persisted artifacts;
- be launched as close to concurrently as the environment permits.

Required frozen package artifacts:

- `experiments/041/treatment-A.md`
- `experiments/041/treatment-B.md`

### Integrator

The Integrator reads only:

- the frozen Package A artifact;
- the frozen Package B artifact;
- repository evidence needed to resolve a concrete conflict, citation question, or cross-boundary discrepancy.

It must not silently redo both packages from scratch.

For every direct repository read performed by the Integrator, record the reason:

```text
CONFLICT RESOLUTION
CITATION VERIFICATION
CROSS-BOUNDARY RECONCILIATION
OTHER — explain
```

If the Integrator requires broad independent re-research of both packages, record that as a coordination failure.

Required frozen treatment artifact:

`experiments/041/treatment.md`

## No extra reviewer/adversary in treatment

Do not add reviewer or adversary roles before the final packet freezes.

Quality is measured by the same blind human acceptance gate used for both arms.

This isolates the parallel-decomposition mechanism from Experiment 040's epistemic-redundancy mechanism.

If both outputs are poor, that is evidence. Do not rescue the treatment by adding more agents.

## Human acceptance interface

Use the Experiment 040 learning directly.

The normal human interface is only the standardized final acceptance packet for each arm.

Intermediate treatment package artifacts are machine-side evidence. The human does not read them during normal acceptance.

If an exception forces the human to inspect intermediate treatment artifacts, record the time and reason as treatment HAL/escalation cost.

## Blind comparison

After both arm outputs freeze, create structurally equivalent packets labeled only:

- `acceptance-A.md`
- `acceptance-B.md`

Seal arm identity before execution and reveal it only after human measurements freeze.

The human records separately for each packet:

```text
Accept/reject
Material corrections required
Additional evidence required
Clarity assessment
Confidence assessment
Human review minutes
```

Do not reveal process telemetry, agent count, or arm identity inside the blind packet.

## Quality gate

Both final packets are assessed against the same checklist:

1. Package A implemented truth is materially correct.
2. Package B operating/governance truth is materially correct.
3. Current software is not confused with manual operating practice.
4. Learned policy is not confused with implemented automation.
5. Historical design is not presented as current truth.
6. Live 030/035 state was not inspected.
7. Revision-aware persistence semantics are represented accurately.
8. Authorization boundary is represented accurately.
9. Commercial/repeatability claims remain appropriately unproven.
10. Material repository ambiguities are surfaced rather than smoothed over.
11. Claims are reconstructable from repository evidence.
12. No canonical project file changed.

An arm that materially fails the quality gate produces zero accepted learning units regardless of speed.

## Primary metric — accepted-output elapsed time

041 tests parallel critical-path reduction.

Define:

```text
AEL = successful-path wall-clock elapsed seconds / accepted material learning units
```

Each accepted arm targets one learning unit: a defensible reconstructability packet.

If an arm fails acceptance, AEL is not meaningfully finite; report failure directly.

For treatment, successful-path elapsed begins at the earliest of Package A/Package B start and ends when the Integrator freezes the final treatment artifact.

For control, successful-path elapsed begins when the control starts and ends when its final control artifact freezes.

## Human-attention guardrail

HAL remains a critical guardrail:

```text
HAL = human active minutes / accepted material learning units
```

A treatment cannot earn the strongest positive verdict by reducing elapsed time while materially increasing human active attention.

Count the same categories as Experiment 040:

- clarifications;
- permission/context resolution;
- substantive blind packet review;
- correction;
- disagreement resolution;
- intermediate inspection on exception;
- manual integration/rewriting.

Exclude standardized initial launch and unattended model runtime.

## Secondary telemetry

Capture prospectively where exposed:

```text
package_A_elapsed
package_B_elapsed
parallel_overlap
integrator_elapsed
control_A_elapsed
control_B_elapsed
control_synthesis_elapsed
human_active_minutes
human_interventions
human_escalations
agent_runs
retries
context_restarts
integrator_repository_reads
integrator_reresearch_events
working_output_size
human_packet_size
compute_or_credit_cost
external_spend
```

Do not invent unavailable telemetry.

## Parallelism diagnostics

Calculate where defensible:

```text
control_elapsed
parallel_treatment_elapsed
elapsed_speedup = control_elapsed / treatment_elapsed
parallel_overlap_fraction
integration_overhead
```

Also report the theoretical package-only critical path when possible:

```text
max(package_A_elapsed, package_B_elapsed)
```

Compare this with actual treatment elapsed to expose integration/coordination overhead.

## Practical interpretation threshold

Because one run is noisy, do not treat a trivial timing difference as meaningful.

For Verdict A, treatment should normally show at least approximately **20% lower successful-path elapsed time** than control while:

- both arms pass quality;
- treatment HAL is not materially worse;
- no material coordination/integrity failure occurs;
- integration does not require broad re-research;
- cost appears proportionate where measurable.

The 20% threshold is a practical discriminator for this experiment, not a universal operating-policy constant.

A smaller improvement may support Verdict B if other evidence is favorable.

## Cost discipline

Record incremental external spend separately from model/compute/credit cost.

If model/credit cost is exposed, report absolute values and treatment/control multiplier.

If unavailable, leave UNKNOWN.

Do not infer cost from agent count or output volume, though these may be described as likely cost drivers.

## Stop conditions

Stop and classify the treatment as failed/invalid where appropriate if:

- package independence materially fails;
- control/treatment isolation is broken before freeze;
- any role inspects live 030/035 external state;
- any role mutates canonical files;
- parallel execution requires persistent orchestration infrastructure;
- package agents cannot persist reconstructable outputs;
- Integrator must broadly redo both packages;
- unbounded retries emerge;
- human coordination is required merely to route normal package outputs;
- costs cannot remain bounded under ordinary authorized model execution.

## Required Experiment 041 artifacts

Create under:

`experiments/041/`

At minimum:

```text
preregistration.md
control.md
treatment-A.md
treatment-B.md
treatment.md
acceptance-A.md
acceptance-B.md
comparison.md
result.md
```

No persistent orchestration code or infrastructure elsewhere in the repository.

## `comparison.md` requirements

Record:

- frozen baseline;
- sealed arm mapping and reveal timing;
- package independence result;
- quality gate for both arms;
- control successful-path elapsed;
- treatment successful-path elapsed;
- package times and overlap where known;
- integration overhead;
- AEL comparison;
- HAL comparison;
- human interventions/escalations;
- retries/context restarts;
- Integrator repository reads and reasons;
- broad rere-search yes/no;
- cost comparison where measurable;
- output/compression observations;
- quality differences/corrections;
- coordination failures;
- defensible speedup;
- whether parallelism reduced a real critical path.

## Verdicts

### A — PARALLEL DECOMPOSITION EARNED FOR ANOTHER BOUNDED TEST

Use only when:

- both arms pass quality;
- treatment successful-path elapsed is practically meaningfully lower, normally at least ~20%;
- treatment HAL is not materially worse;
- integration does not require broad package re-research;
- no truth/scope/integrity regression occurs;
- added compute/coordination cost appears proportionate where measurable.

A authorizes only another bounded operating-model experiment. It does not authorize orchestration software or canonical operating-model change.

### B — PROMISING BUT INCONCLUSIVE

Use when quality is preserved and some parallelism benefit appears, but timing advantage is modest/noisy, cost is unknown, integration burden is ambiguous, or one workload is insufficient.

### C — NO MATERIAL PARALLELISM ADVANTAGE

Use when quality is comparable but elapsed/HAL/coordination economics do not materially improve.

### D — PARALLEL TREATMENT WORSE

Use when decomposition causes quality loss, coordination failure, broader integration work, materially higher human burden, or substantially worse elapsed time without compensating evidence.

### E — INVALID EXPERIMENT

Use when workload equivalence, package independence, isolation, timing, or integrity failure prevents interpretation.

## Interpretation boundary

One positive 041 run would establish at most:

> On one repository-only workload with two independent evidence packages, parallel package execution reduced successful-path elapsed time while preserving accepted quality and the compressed human interface.

It would not establish:

- general multi-agent superiority;
- autonomous delegation;
- coding parallelism value;
- external research parallelism value;
- optimal agent count;
- safe autonomous project management;
- economic opportunity improvement;
- orchestration-platform need.

## If A or B

Do not build orchestration infrastructure next by default.

The next experiment should choose whichever uncertainty is then dominant, for example:

- adaptive delegation: machine decides single-agent vs parallel vs redundancy from a bounded work contract;
- a coding workload with isolated modules;
- a repository-research workload with a real dependency edge;
- measured compute-cost proportionality.

Only one should be tested next.

## If C or D

Preserve parallel execution as optional/manual and investigate the observed coordination bottleneck before proposing another mechanism.

## If E

Repair design only.

## Required `result.md`

Record:

- baseline;
- prospective timing method;
- package-independence check;
- roles actually used;
- arm mapping after reveal;
- accepted units;
- AEL;
- HAL;
- elapsed speedup;
- package overlap;
- integration overhead;
- human interventions;
- quality result;
- compute/cost result;
- strongest positive result;
- strongest negative result;
- strongest unresolved uncertainty;
- overall verdict;
- exactly one recommended next action.

## Success condition

041 succeeds as an experiment if it cleanly answers:

> Does genuine parallel decomposition improve the operating economics of one bounded AE repository task, independently of the epistemic-redundancy mechanism tested in 040?

A negative answer is valid evidence.
