# Spec 040 — Agentic Operating Model

## Status

READY FOR EXECUTION

## Type

Bounded operating-model experiment. No product architecture change. No runtime implementation. No external actor interaction.

## Baseline

Execute from synchronized `main` at or after:

`12dd7cef27c338fb01af8e52bc44688249bf082f`

Experiment 039 is closed and accepted. Top-level documentation reflects current Engine truth at this baseline.

Experiments 030 and 035 remain historically important actor-facing experiments. Their external state MUST NOT be inspected or refreshed during this experiment.

## Why this experiment is earned

Asymmetry Engine has progressively reduced the cost of producing useful economic evidence by using bounded specifications, cheap discriminators, disposable resolution work, adversarial challenge, explicit authorization boundaries, and repository-preserved learning.

The current operating model still has a potentially important serial dependency:

```text
human frames work
  ↓
agent executes
  ↓
human interprets/reviews
  ↓
next work is framed
```

AI-assisted implementation is already fast enough that human attention, review, context reconstruction, delegation, and synthesis may increasingly dominate the critical path.

A plausible next operating hypothesis is that several isolated agents can perform bounded production, review, adversarial challenge, and synthesis concurrently while the repository acts as the shared state boundary.

That hypothesis is NOT yet validated.

Adding an orchestration framework, queue, database, permission service, autonomous scheduler, or agent-specific product architecture before validating the operating economics would contradict the Engine's learned automation policy.

Therefore Experiment 040 tests the operating model before implementing orchestration software.

## Primary hypothesis

> A bounded multi-agent workflow can reduce human attention required per unit of validated learning without materially degrading evidence quality, truth preservation, scope discipline, or repository integrity.

## Null hypothesis

> Multi-agent orchestration adds coordination cost, duplicate work, review burden, ambiguity, or false confidence such that it does not materially improve human-attention efficiency relative to the current single-agent workflow.

## Primary question

For one frozen, reversible, repository-only workload, does a small multi-agent treatment outperform the current single-agent control on human attention per accepted evidence outcome while preserving or improving output quality?

## Governing principles

1. **Agents optimize the experiment, not the project.**
2. **Repository artifacts are the shared state boundary.** Important findings must not depend on invisible inter-agent conversation history.
3. **Canonical project truth is read-only during this experiment.** Evidence may suggest future changes, but 040 does not authorize them.
4. **Multi-agent execution must be earned.** More agents are not automatically better.
5. **Fail closed.** Disagreement, ambiguity, missing evidence, or unverifiable claims must escalate rather than be averaged away.
6. **Human attention is the scarce resource under test.** Agent activity volume is not success.
7. **No consequential external action.** This experiment is entirely repository-local.

## Explicit non-goals

Experiment 040 does NOT attempt to:

- agentify Asymmetry Engine;
- implement autonomous RADAR;
- implement autonomous FORGE;
- implement an orchestration service;
- create an agent queue/database;
- add an agent SDK or framework;
- create persistent agent identities;
- automate authorization;
- automate external interaction;
- modify the opportunity model;
- modify the economic reasoning model;
- redefine the project architecture;
- prove 10× or 100× end-to-end project acceleration;
- prove commercial value from agent orchestration.

It tests one small operating-model hypothesis only.

## Frozen canonical surfaces

During Experiment 040, do NOT modify:

- `README.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `docs/OPERATING_MODEL.md`
- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_REASONING_MODEL.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- `docs/SOURCE_STRATEGY.md`
- `docs/SOURCE_REGISTRY.md`
- source code under `src/`
- tests under `tests/`
- prior specs or experiment artifacts
- Experiment 030 state/artifacts
- Experiment 035 state/artifacts

The only permitted persistent project changes are the Experiment 040 specification and its explicitly required result artifacts.

## Authority model

### Autonomous within isolated experiment work

Agents may:

- read repository files;
- inspect Git history already present in the repository;
- search repository text;
- calculate deterministic metrics from repository evidence;
- create temporary working files in isolated worktrees or temporary directories;
- produce candidate Experiment 040 output artifacts;
- review another agent's persisted output artifact;
- challenge claims using repository evidence;
- run read-only checks and existing tests if useful;
- discard isolated work without consequence.

### Proposal only

Agents may identify and describe possible future changes to:

- operating model;
- architecture;
- telemetry;
- agent contracts;
- repository structure;
- automation policy.

Such proposals MUST NOT be applied during 040.

### Forbidden

Agents MUST NOT:

- merge or push experiment-generated project changes other than the final accepted 040 artifacts;
- modify canonical project truth;
- weaken evidence standards to make the treatment look successful;
- inspect live external state for 030 or 035;
- contact actors;
- post, message, email, comment, submit, buy, subscribe, or publish externally;
- use paid external services beyond ordinary already-authorized Codex/model execution without explicit approval;
- create hidden retries intended to select a favorable result;
- share treatment conclusions with the control before both outputs are frozen.

## Experimental design

Use a matched control-versus-treatment design on the same frozen baseline and same shadow-workload contract.

```text
                    FROZEN BASELINE
                          │
                same workload contract
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
       CONTROL ARM                TREATMENT ARM
       single agent               multi-agent
             │                         │
             ▼                         ▼
      frozen output A             frozen output B
             └────────────┬────────────┘
                          ▼
                  blind-ish comparison
                          │
                          ▼
                 operational verdict
```

The two arms must remain isolated until their final candidate outputs are frozen.

Do not let the treatment read the control output or vice versa before freeze.

## Shadow workload

The workload must be useful enough to require judgment but low-consequence enough that failure cannot compromise the project.

### Task

Reconstruct and audit the operational telemetry for this fixed experiment set:

```text
020
021
025
026
030
031
032
033
034
035
```

Use repository evidence only.

Produce a compact structured answer to:

1. What active-time evidence exists for each selected experiment?
2. What monetary-spend evidence exists?
3. What human-intervention / authorization / control evidence exists?
4. What experiment-flow counts or interaction counts exist?
5. What evidence-yield statement exists, if any?
6. What is RECORDED versus DERIVED versus ESTIMATED versus UNKNOWN?
7. Where do source artifacts contradict or ambiguously describe the same field?
8. What conclusions about operating efficiency are supported by these selected experiments?
9. What tempting efficiency conclusions are NOT supported?

This deliberately overlaps the subject matter of Experiment 036 but is NOT permission to copy its conclusions as ground truth.

Experiment 036 may be used only as a cross-check after the arm has independently reconstructed its own result from primary experiment/checkpoint evidence.

The workload is therefore an evidence-reconstruction and epistemic-discipline test, not a novel economic experiment.

## Required arm output schema

Each arm must produce a machine-readable or rigid Markdown artifact containing exactly these conceptual sections:

```text
ARM
BASELINE
START/END TELEMETRY
EVIDENCE SOURCES READ
EXPERIMENT TABLE
CONTRADICTIONS / AMBIGUITIES
SUPPORTED CONCLUSIONS
UNSUPPORTED CONCLUSIONS
CONFIDENCE / LIMITATIONS
FINAL VERDICT
```

The experiment table must contain, for every selected experiment:

```text
experiment_id
active_time
active_time_quality
spend
spend_quality
flow_or_interaction
flow_quality
human_controls
human_controls_quality
evidence_yield
evidence_yield_quality
source_references
notes
```

Allowed quality vocabulary:

```text
RECORDED
DERIVED
ESTIMATED
UNKNOWN
N/A
```

UNKNOWN is never zero.

## Control arm

### Structure

One Codex agent receives:

- this spec;
- the frozen repository baseline;
- the shadow-workload contract.

It performs the complete workload alone.

It may inspect repository evidence and perform deterministic calculations, but it receives no independent reviewer/adversary before freezing its output.

### Required control artifact

Create only in isolated experiment work until final acceptance:

`experiments/040/control.md`

or an equivalent structured JSON artifact plus a short Markdown wrapper.

### Control telemetry

Record prospectively where available:

- wall-clock start/end;
- agent execution/runtime if available;
- human active minutes required to initiate, clarify, inspect, correct, and accept/reject;
- number of human interventions;
- retries;
- context restarts;
- approximate tool/model cost if the environment exposes it;
- output size;
- number of material factual corrections required before acceptance.

Do not fabricate unavailable telemetry.

## Treatment arm

### Minimum viable multi-agent structure

Use four logical roles:

```text
PRODUCER
   ↓ persisted candidate artifact
REVIEWER
   ↓ persisted review artifact
ADVERSARY
   ↓ persisted challenge artifact
SYNTHESIZER
   ↓ treatment candidate
```

REVIEWER and ADVERSARY should operate independently after the producer output is frozen and may run concurrently if the environment supports it.

The SYNTHESIZER may read only persisted artifacts and the repository evidence needed to resolve disagreements.

Persistent agent identity is not required. Roles belong to work packages, not to long-lived personas.

### Producer responsibility

Independently reconstruct the requested telemetry from repository evidence and produce the first candidate result.

### Reviewer responsibility

Check:

- factual correctness;
- source support;
- RECORDED/DERIVED/ESTIMATED/UNKNOWN classification;
- arithmetic;
- completeness;
- scope compliance;
- unsupported inference;
- leakage from Experiment 036 before independent reconstruction.

Return PASS, FIX, or ESCALATE with concrete findings.

### Adversary responsibility

Attempt to falsify the producer's strongest efficiency conclusions.

Look specifically for:

- incomparable denominators;
- approximate time treated as exact;
- missing historical spend treated as zero;
- heterogeneous experiment phases aggregated as one funnel;
- delivery conflated with exposure/effect/value;
- human authorization conflated with human active work;
- commit timestamps treated as active-time evidence;
- later checkpoint interpretation silently replacing primary evidence;
- ambiguity hidden by a synthetic score.

Return PASS, CHALLENGE, or ESCALATE and preserve the strongest surviving challenge.

### Synthesizer responsibility

Integrate the frozen Producer, Reviewer, and Adversary artifacts.

The synthesizer MUST NOT average disagreement away.

If a material conflict cannot be resolved from repository evidence, classify it explicitly and escalate it.

The synthesizer produces:

`experiments/040/treatment.md`

plus the preserved role artifacts if useful for auditability.

### Treatment telemetry

Record prospectively where available:

- wall-clock start/end by role;
- dependency waits;
- parallel overlap;
- agent execution/runtime if available;
- human active minutes;
- human interventions;
- retries;
- duplicate research observed;
- contradictions caught by reviewer;
- contradictions caught by adversary;
- synthesis corrections;
- unresolved disagreements;
- approximate tool/model cost if exposed;
- total generated output size;
- final human-facing synthesis size.

Do not infer unavailable fields.

## Human-attention accounting

The central resource under test is human active attention, not elapsed clock time.

Human active minutes should include time spent:

- launching or delegating beyond the initial standardized experiment start;
- answering agent clarification questions;
- resolving permission/context problems;
- reading substantive outputs for acceptance;
- correcting material errors;
- reconciling agent disagreement;
- manually integrating or rewriting the result.

Do not include unattended agent runtime.

If exact minute tracking is impractical, use a prospectively declared approximation method and label the result ESTIMATED.

## Primary metric

Define:

```text
HAL = human active minutes / accepted material learning units
```

For 040, both arms target one accepted material learning unit: a defensible reconstruction answering the shadow-workload questions.

Therefore the primary comparison reduces to human active minutes required to obtain an accepted output of adequate quality.

If an arm fails acceptance, it produces zero accepted learning units and HAL is not meaningfully finite; report the failure directly rather than forcing a numeric ratio.

## Secondary metrics

Compare:

```text
wall_clock_elapsed
human_active_minutes
human_interventions
agent_runs
retries
output_size
human_facing_output_size
material_errors_before_acceptance
material_errors_after_review
contradictions_found
unsupported_claims_found
unresolved_disagreements
repository_drift_or_scope_violations
compute_or_credit_cost_if_available
```

Also calculate, only when inputs are defensible:

```text
attention_speedup = control_human_minutes / treatment_human_minutes

elapsed_speedup = control_elapsed / treatment_elapsed

cost_multiplier = treatment_compute_cost / control_compute_cost
```

Do not calculate ratios when either denominator is unknown or semantically incomparable.

## Quality gate

Faster output is not better if epistemic quality falls.

Each final arm output must be evaluated against the same acceptance checklist:

1. All ten fixed experiments represented.
2. No live external state inspected.
3. Every populated telemetry field has an evidence-quality classification.
4. UNKNOWN is not silently converted to zero.
5. Recorded and estimated time are distinguished.
6. Different experiment phases are not aggregated into a false homogeneous efficiency series.
7. Delivery is not treated as exposure, effect, value, or revenue.
8. Strongest supported efficiency conclusion is appropriately bounded.
9. Strongest unsupported tempting conclusion is explicitly stated.
10. Material repository contradictions/ambiguities are surfaced rather than hidden.
11. No canonical project file changed.
12. Final claims remain reconstructable from repository evidence.

A final output failing any material item cannot win on speed.

## Independent comparison

After both final arm outputs are frozen, compare them without giving either arm an opportunity to rewrite itself in response to the other.

The comparison should score only observable properties:

- acceptance checklist result;
- factual corrections required;
- evidence discipline;
- contradictions found;
- unsupported claims avoided;
- human active minutes;
- elapsed time;
- cost where known;
- review burden;
- clarity of final human-facing result.

Do not use raw word count, number of agents, number of tool calls, or number of intermediate artifacts as quality signals.

## Decision-compression metric

Record:

```text
total_agent_output
final_human_facing_output
```

If token counts are available, calculate:

```text
compression_ratio = total_agent_output_tokens / final_human_facing_tokens
```

This is descriptive only.

A high ratio is useful only if the final synthesis preserves all material disagreement and evidence required for the human decision.

The treatment fails the human-attention objective if parallel agents produce substantially more material that the human must manually read and reconcile.

## Stop conditions

Stop the treatment and record a failure if any of these occur:

- an agent attempts consequential external action;
- an agent modifies a frozen canonical file;
- treatment/control isolation is materially broken before output freeze;
- orchestration requires implementing new persistent runtime infrastructure;
- agent outputs cannot be reconstructed from persisted artifacts;
- material disagreement is silently suppressed;
- human coordination burden clearly exceeds the single-agent control before a valid output is produced;
- unbounded retry loops emerge;
- costs cannot be bounded under ordinary existing tool use;
- completion would require inspecting live 030/035 external state.

## Orchestration constraints

Use the simplest mechanisms already available in Codex/Git.

Preferred primitives:

- isolated threads;
- isolated Git worktrees or equivalent temporary workspaces;
- repository files as context/output contracts;
- deterministic file-based handoffs;
- ordinary Git diff/status for integrity.

Do NOT implement during 040:

- message brokers;
- orchestration servers;
- workflow engines;
- task databases;
- long-lived agent memory services;
- agent permission infrastructure;
- autonomous schedulers;
- custom dashboards.

If the experiment succeeds, these remain future hypotheses requiring separate evidence.

## Context discipline

Each role should receive the minimum context needed to perform its bounded task.

Do not copy the entire project history into every prompt.

Repository-local sources of truth should be referenced directly.

`AGENTS.md`, if used, should remain navigation/invariant context rather than becoming a transcript or giant procedure manual.

The experiment should record any context that agents repeatedly failed to discover without human help. Such friction is evidence for later operating-model improvement, not permission to expand global context indiscriminately.

## No-delegation rule

The treatment must explicitly preserve the possibility that a work package should remain single-agent.

Before creating parallel sub-work, ask:

1. Can the task be decomposed without destroying semantic context?
2. Can outputs be independently verified?
3. Can sub-agents operate without mutating shared state?
4. Is coordination cost plausibly lower than the expected learning benefit?
5. Does concurrency reduce a real critical path rather than merely increase activity?

If these are materially false, use one agent for that work package and record why.

The experiment is not invalid merely because some treatment steps remain serial.

## Required Experiment 040 artifacts

Create under:

`experiments/040/`

At minimum:

```text
control.md
treatment.md
comparison.md
result.md
```

Treatment may additionally preserve:

```text
producer.md
reviewer.md
adversary.md
synthesizer.md
```

if separate files improve auditability.

Do not create persistent orchestration infrastructure elsewhere in the repository.

## Required `comparison.md`

Record:

- frozen baseline;
- workload identity;
- control output status;
- treatment output status;
- acceptance checklist for both;
- human active minutes for both or UNKNOWN;
- wall-clock time for both or UNKNOWN;
- agent/tool cost for both or UNKNOWN;
- errors requiring correction;
- contradictions surfaced;
- unsupported claims prevented;
- human interventions;
- treatment coordination failures;
- decision-compression observations;
- defensible speedup ratios if available;
- whether the multi-agent treatment improved HAL;
- whether quality was preserved or improved;
- whether cost increased and by how much if measurable.

## Required `result.md`

Record:

- baseline commit;
- prospective timing method;
- spend/cost method;
- isolation method;
- agents/roles actually used;
- whether worktrees or equivalent isolation were used;
- files created;
- canonical files confirmed unchanged;
- primary metric result;
- secondary metrics;
- strongest positive result;
- strongest negative result;
- strongest unresolved uncertainty;
- any false-PASS or coordination failure;
- whether repository-mediated handoff was sufficient;
- whether human attention decreased;
- whether wall-clock time decreased;
- whether cost materially increased;
- whether quality changed;
- overall verdict;
- exactly one recommended next action.

## Verdicts

### A — MULTI-AGENT OPERATING MODEL EARNED FOR NEXT BOUNDED TEST

Use only when:

- both arms satisfy the quality gate;
- treatment human active minutes are lower than control by a practically meaningful amount;
- no material truth/scope/integrity regression occurs;
- treatment does not require persistent orchestration infrastructure;
- added compute/coordination cost appears proportionate to the attention saved;
- reviewer/adversary work contributes useful independent error detection or confidence.

This verdict authorizes only another bounded operating-model experiment. It does NOT authorize agentification of AE architecture.

### B — PROMISING BUT INCONCLUSIVE

Use when quality is preserved and some operational benefit appears, but telemetry is incomplete, workload is too small, attention savings are modest, or treatment cost/coordination remains ambiguous.

Next work should improve measurement or test a second matched workload, not build orchestration infrastructure.

### C — NO MATERIAL ADVANTAGE

Use when treatment quality is comparable but human attention, elapsed time, or total operating burden does not improve enough to justify added complexity.

Preserve the existing single-agent operating model.

### D — MULTI-AGENT TREATMENT WORSE

Use when treatment causes material quality degradation, hidden disagreement, drift, excessive coordination, higher human burden, or unbounded cost.

Do not proceed to broader agent orchestration without a new hypothesis explaining the failure.

### E — INVALID EXPERIMENT

Use when isolation was broken, telemetry was retrospectively invented, workload differed materially between arms, live external state contaminated the test, canonical project state was changed, or another design failure prevents interpretation.

## Acceptance criteria for Experiment 040 itself

040 is complete only when:

1. control and treatment execute from the same frozen baseline/workload contract;
2. arm isolation is preserved until freeze;
3. required artifacts exist;
4. no prohibited external action occurs;
5. canonical project truth remains unchanged;
6. human-attention telemetry is prospectively captured to the extent practicable;
7. both arms are judged against the same quality gate;
8. comparison separates quality, attention, elapsed time, and cost rather than collapsing them into one score;
9. unsupported speedup claims are rejected;
10. the result selects exactly one next action.

## Interpretation boundary

One positive run does not prove a general multi-agent operating system.

The strongest positive conclusion available from 040 is approximately:

> On one bounded repository-evidence workload, a small role-separated multi-agent workflow reduced human attention while preserving or improving accepted output quality.

It does not establish:

- general 10×/100× acceleration;
- better performance on coding tasks;
- better performance on external research;
- better economic opportunity selection;
- autonomous project management;
- profitable autonomous operation;
- safe autonomous external interaction.

Those require separate experiments.

## If A or B

Do not build an orchestration platform next by default.

Prefer a second experiment with a different workload topology, for example two genuinely parallel bounded work packages with an explicit dependency edge, to test whether the result generalizes beyond review parallelism.

## If C or D

Preserve the existing operating model and inspect the specific coordination bottleneck before proposing any additional agent mechanism.

## If E

Repair experiment design only. Do not infer anything about multi-agent value.

## Strategic significance

If a sequence of bounded experiments eventually supports the hypothesis, the operating model may progressively evolve from:

```text
human → agent → human → agent
```

toward:

```text
human objective
      ↓
bounded orchestration
      ↓
parallel production / review / falsification
      ↓
machine synthesis
      ↓
human exception or consequential decision
```

Only repeated evidence could justify later convergence with the wider Engine.

The long-run hypothesis is that Asymmetry Engine might eventually use agentic execution to reduce human attention per economically relevant uncertainty retired.

Experiment 040 does not assume that hypothesis is true.

It creates the first controlled measurement capable of rejecting it.
