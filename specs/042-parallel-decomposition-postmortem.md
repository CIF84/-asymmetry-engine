# Spec 042 — Parallel Decomposition Postmortem

## Status

READY FOR EXECUTION

## Type

Bounded operating-model postmortem. Repository-only. No external interaction. No new agentic treatment. No architecture change.

## Baseline

Execute from synchronized `main` at or after:

`b922ce0f23bfbb31dac3bc752014e8226442e7c7`

Experiment 041 is complete and closed with:

`D — PARALLEL TREATMENT WORSE`

Experiments 030 and 035 remain protected external observation windows and MUST NOT be inspected or refreshed.

## Why this experiment is earned

Experiment 041 tested genuine parallel decomposition rather than epistemic redundancy.

The treatment achieved:

```text
Package A: 169 s
Package B: 159 s
Parallel overlap: 159 s
Overlap fraction: 94.1%
Package critical path: 169 s
```

The treatment therefore demonstrated real concurrency.

Yet accepted-output elapsed time was:

```text
Control:   202 s
Treatment: 301 s
```

Treatment was 99 seconds / 49.0% slower despite preserved quality.

Measured treatment overhead above its package critical path was:

```text
50 s routing / dependency wait
82 s integration
----------------------------
132 s total
```

Even removing the entire 50-second routing gap leaves 251 seconds, still slower than the 202-second control. Even omitting integration entirely leaves a 169-second package critical path, only 16.3% faster than control and below SPEC-041's predeclared ~20% strong-positive threshold.

Therefore another parallel-agent trial is not earned merely by reducing launch/routing latency.

A postmortem is required to determine whether the failure came primarily from:

1. **INCIDENTAL ORCHESTRATION FRICTION** — avoidable routing/tooling latency;
2. **CONTRACT / INTERFACE FAILURE** — packages were independently producible, but the package contract forced unnecessary reconciliation or reformatting;
3. **STRUCTURAL SEMANTIC COUPLING** — the supposedly independent packages duplicated context/meaning such that integration cost is inherent at this decomposition boundary;
4. **WORKLOAD SIZE / GRANULARITY MISMATCH** — the packages were too small for parallelism to amortize fixed coordination cost;
5. **MIXED / INSUFFICIENT EVIDENCE**.

The purpose of 042 is diagnosis, not optimization.

## Primary question

> **Why did Experiment 041's genuinely concurrent package decomposition fail to reduce accepted-output elapsed time?**

## Secondary questions

1. How much of the measured 132-second post-package overhead was necessary semantic reconciliation versus avoidable routing/tooling delay?
2. Did the decomposition duplicate context, evidence gathering, explanation, formatting, or boundary reasoning that the control performed only once?
3. Could a materially narrower package contract have reduced integration work without simply moving work into the packages or Integrator?
4. Was the workload too small for fixed agent startup/coordination costs to amortize?
5. What observable conditions should determine whether future work is delegated to parallel agents at all?
6. Does 041 earn another parallel-agent experiment? If yes, what exactly must be different?

## Governing principle

Do not respond to a failed treatment by optimizing the desired architecture.

First determine whether the failure mechanism is:

```text
incidental
vs
interface-driven
vs
structural
vs
granularity-driven
```

Only then may another agentic experiment be proposed.

## Explicit non-goals

042 does NOT attempt to:

- run another control-versus-treatment experiment;
- spawn parallel work packages as treatment;
- optimize Codex startup latency;
- implement orchestration;
- build an agent scheduler;
- build a task graph;
- create a routing service;
- create standardized agent APIs;
- change AE architecture;
- change AE operating-model truth;
- modify Experiment 041 evidence;
- prove or disprove multi-agent operation generally;
- inspect live 030/035 state;
- contact any actor.

## Required evidence

Use repository evidence only.

Primary evidence:

- `specs/041-parallel-work-package-agentic-test.md`
- `experiments/041/preregistration.md`
- `experiments/041/execution-telemetry.md`
- `experiments/041/control.md`
- `experiments/041/treatment-A.md`
- `experiments/041/treatment-B.md`
- `experiments/041/treatment.md`
- `experiments/041/comparison.md`
- `experiments/041/result.md`
- `experiments/041/acceptance-A.md`
- `experiments/041/acceptance-B.md`

Contextual evidence permitted:

- `specs/040-agentic-operating-model.md`
- `experiments/040/result.md`
- `experiments/040/comparison.md`
- current `README.md`
- current `ARCHITECTURE.md`
- current `ROADMAP.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`

Do not use live external state.

## Isolation

Do not modify:

- source code;
- tests;
- README;
- ARCHITECTURE;
- ROADMAP;
- frozen project models;
- Experiment 040 artifacts;
- Experiment 041 artifacts;
- Experiment 030 artifacts/state;
- Experiment 035 artifacts/state.

The only persistent project changes permitted are:

- this specification;
- the required Experiment 042 postmortem artifact.

## Evidence discipline

Every postmortem claim must distinguish:

- **MEASURED** — prospectively or deterministically recorded in 041;
- **DERIVED** — mechanically calculable from measured 041 evidence;
- **INFERRED** — interpretation supported by artifact comparison;
- **UNKNOWN** — not defensibly reconstructable.

Do not infer compute cost.

Do not infer agent hidden reasoning or token use.

Do not treat output byte count as direct compute cost or quality.

Do not treat internal role timestamps as authoritative when external wrapper boundaries exist.

## Decomposition model to audit

Experiment 041 assumed this workload could be decomposed as:

```text
                     OBJECTIVE
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
     PACKAGE A                PACKAGE B
 implemented software       operating/governance
             │                     │
             └──────────┬──────────┘
                        ▼
                   INTEGRATOR
                        ↓
                 accepted packet
```

The postmortem must ask whether Package A and B were merely **separable** or genuinely **economically independent**.

Use this distinction:

```text
SEPARABLE
= can be produced in different artifacts without shared mutation

ECONOMICALLY INDEPENDENT
= can be produced separately AND integrated with sufficiently low marginal cost that concurrency reduces the accepted-output critical path
```

Experiment 041 proved separability and operational independence. It did not prove economic independence.

## Required timing decomposition

Reconstruct the authoritative 041 elapsed path:

```text
package critical path
+
routing / dependency wait
+
integration
=
treatment accepted-output path
```

Use external wrapper telemetry as authoritative.

At minimum report:

```text
control_end_to_end
package_A
package_B
parallel_overlap
package_critical_path
routing_gap
integration_elapsed
post_package_overhead
final_treatment_elapsed
```

Also preserve the narrower internal timestamp mismatch as telemetry ambiguity rather than reconciling it away.

## Counterfactual timing analysis

Calculate only deterministic counterfactual bounds from measured components.

At minimum:

### CF1 — zero routing gap

```text
package critical path + integration
```

Question: would removing only routing latency have beaten control?

### CF2 — zero integration cost

```text
package critical path
```

Question: would perfect zero-cost integration have cleared the predeclared 20% threshold?

### CF3 — minimum integration required to beat control

Given measured package critical path and zero routing delay, derive:

```text
max integration time allowed to beat control
```

### CF4 — minimum integration required to clear 20% threshold

Derive the maximum total post-package overhead consistent with the 041 strong-positive threshold.

Do not treat these counterfactuals as achievable engineering forecasts. They are feasibility bounds.

## Semantic duplication audit

Compare control versus treatment artifacts for duplicated work categories.

At minimum inspect:

### Shared context reconstruction

Did both package agents independently reconstruct overlapping project architecture, terminology, repository boundaries, or evidence rules?

### Evidence retrieval duplication

Did both packages read overlapping repository documents or reconstruct overlapping facts?

### Boundary explanation duplication

Did both packages independently explain software-vs-manual, implemented-vs-unimplemented, governance, UNKNOWN discipline, or other cross-cutting distinctions?

### Final-form duplication

Did package artifacts already produce prose that then had to be summarized/reformatted rather than delivering compact contract outputs?

### Integrator reconciliation

Which integration actions were necessary because the two domains genuinely intersected, versus necessary only because the package outputs were not contract-normalized?

Classify each duplication as:

- NECESSARY SEMANTIC OVERLAP
- AVOIDABLE CONTRACT DUPLICATION
- INCIDENTAL FORMAT DUPLICATION
- UNKNOWN

## Integrator-work audit

The 041 Integrator performed no broad repository re-research. That establishes one important fact: integration cost did not come from secretly redoing package research.

Now determine what the Integrator actually had to do.

Classify integration work into:

1. **COPY / STRUCTURAL ASSEMBLY**
2. **NORMALIZATION / FORMAT ALIGNMENT**
3. **SEMANTIC RECONCILIATION**
4. **CONTRADICTION / AMBIGUITY RESOLUTION**
5. **CROSS-BOUNDARY SYNTHESIS**
6. **CITATION VERIFICATION**
7. **OTHER / UNKNOWN**

Estimate proportions only if artifact evidence supports a defensible qualitative classification. Do not fabricate per-category seconds.

## Contract-quality audit

Ask whether a different package contract could plausibly have reduced integration cost.

Examples of contract changes to consider only as hypotheses:

- rigid shared output schema;
- package outputs limited to facts/claims rather than final prose;
- explicit cross-boundary questions declared before launch;
- shared invariant glossary supplied once;
- package-specific exclusion lists;
- Integrator receives structured deltas rather than full essays;
- one package designated authority for cross-cutting concepts.

For each candidate contract change ask:

```text
Would this reduce integration work?
OR
Would it merely move equivalent work into package preparation/output formatting?
```

Do not count shifted work as saved work.

## Granularity / fixed-cost audit

Determine whether the workload was simply too small.

Use measured evidence to reason about:

- package elapsed of ~160–170 seconds;
- 82-second measured integration;
- 50-second routing gap;
- three treatment runs versus one control run;
- 2.30× machine-side output;
- equal accepted quality;
- no human intervention reduction.

Ask whether larger independent packages could theoretically amortize fixed integration/startup costs, while explicitly noting that this is not established by 041.

Do not extrapolate linearly.

## Delegation-policy extraction

042 should attempt to extract the smallest evidence-supported rule for future parallelization decisions.

Candidate form:

```text
PARALLELIZE ONLY IF:

1. sub-work is operationally separable;
2. cross-package semantic coupling is low;
3. outputs can be verified independently;
4. integration contract is narrow;
5. expected saved serial work materially exceeds fixed routing + integration cost;
6. human attention does not increase materially;
7. added compute/coordination cost is proportionate or at least measurable.
```

Do not adopt this verbatim unless supported by the postmortem.

The postmortem may instead conclude that evidence is insufficient for a general delegation rule.

## Relationship to Experiment 040

Use 040 only to distinguish mechanisms:

```text
040 — epistemic redundancy
independent disagreement caught an intermediate false PASS
result: promising but inconclusive

041 — parallel decomposition
real overlap occurred but accepted-output path worsened
result: treatment worse
```

Do not combine 040 and 041 into a synthetic multi-agent score.

A possible learned distinction is:

```text
ADD AN AGENT FOR:
- epistemic independence?
- genuine critical-path independence?

not merely:
- task size
- activity volume
```

Treat this as provisional unless the evidence supports it.

## Required failure classification

Assign one primary and any secondary causes from:

### F1 — INCIDENTAL ROUTING FRICTION

The treatment would likely have been competitive if orchestration delay were removed, with integration otherwise cheap enough.

### F2 — CONTRACT / INTERFACE FAILURE

Integration tax was materially driven by avoidable output/interface design rather than unavoidable semantics.

### F3 — STRUCTURAL SEMANTIC COUPLING

The package boundary required substantial synthesis because important concepts crossed the split; another agent did not remove that work.

### F4 — GRANULARITY / FIXED-COST MISMATCH

The packages were too small for fixed launch/routing/integration cost to amortize.

### F5 — TREATMENT EXECUTION DEFECT

A concrete avoidable execution mistake materially distorted the result.

### F6 — MIXED / INSUFFICIENT EVIDENCE

No dominant mechanism can be established.

The classification must follow evidence, not preference for another experiment.

## Decision rules for future parallel testing

### Another parallel-agent experiment is EARNED only if:

- the postmortem identifies a concrete failure mechanism;
- a materially different treatment can be specified without persistent orchestration infrastructure;
- the mechanism change is expected to affect accepted-output critical path, not merely cosmetic routing;
- the change does not simply shift equivalent work elsewhere;
- the next experiment can distinguish the revised hypothesis cheaply.

### Another parallel-agent experiment is NOT EARNED if:

- the main tax appears structurally semantic at this workload topology;
- only speculative orchestration optimization could rescue it;
- the proposed change merely reduces a small fraction of the measured deficit;
- the next workload is chosen only because it is larger or more favorable;
- compute/coordination uncertainty dominates interpretation.

## Required artifact

Create:

`experiments/042/parallel-decomposition-postmortem.md`

Required sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Authoritative 041 timing reconstruction
7. Internal/external timing ambiguity
8. CF1 zero-routing analysis
9. CF2 zero-integration analysis
10. CF3 break-even integration bound
11. CF4 strong-positive overhead bound
12. Semantic duplication audit
13. Evidence-retrieval duplication
14. Boundary-concept duplication
15. Final-form duplication
16. Integrator-work classification
17. Necessary versus avoidable integration
18. Contract-quality assessment
19. Granularity/fixed-cost assessment
20. Control-versus-treatment work amplification
21. Human-attention implication
22. Compute/cost implication
23. Relationship to 040
24. Primary failure classification F1–F6
25. Secondary failure classifications
26. Strongest evidence for another parallel test
27. Strongest evidence against another parallel test
28. Provisional delegation rule, if earned
29. What must not be optimized/built yet
30. Whether another parallel-agent experiment is earned: yes/no
31. If yes, exact revised hypothesis; if no, what evidence would reopen it
32. What the agentic operating-model hypothesis now says
33. Exactly one recommended next action

## Verdicts

### A — FAILURE MECHANISM IDENTIFIED; REVISED PARALLEL TEST EARNED

A concrete avoidable mechanism explains the 041 failure and a meaningfully different bounded treatment can test it.

### B — FAILURE MECHANISM PARTIALLY IDENTIFIED; NO RETEST YET

The postmortem narrows the cause but cannot justify another parallel trial without additional evidence or a materially different workload condition arising naturally.

### C — STRUCTURAL DECOMPOSITION TAX

Evidence indicates that this workload topology was operationally separable but not economically independent; integration/semantic coupling defeats parallel benefit. Preserve single-agent execution for similar work.

### D — INCIDENTAL EXECUTION FAILURE

A concrete execution defect invalidated 041 as a test of parallel economics. Only use if the defect materially explains the result rather than merely contributing modest overhead.

### E — INVALID / INSUFFICIENT POSTMORTEM

Repository evidence cannot support a defensible mechanism classification.

## Budget

Target active work: 20–35 minutes.

Hard ceiling: 50 active minutes.

Incremental external spend: €0.

Use prospective timing.

No external action.

No code changes.

No new multi-agent treatment.

## Stop rules

Stop when:

- authoritative 041 timing is reconstructed;
- counterfactual bounds are calculated;
- duplication and Integrator work are classified sufficiently to distinguish major hypotheses;
- a primary failure mechanism is assigned or evidence is declared insufficient;
- the next-agent-experiment decision is determined;
- further artifact archaeology is unlikely to change that decision.

Do not fill the time budget.

## Success condition

Success means answering:

> **Was Experiment 041 slow because our orchestration was clumsy, because our package contract was poor, because the work was semantically coupled, because the packages were too small, or because the evidence cannot distinguish these explanations—and what does that imply for future delegation?**

A conclusion that no further parallel-agent test is currently earned is a valid success.

## Completion report

Return exactly:

1. Verdict
2. Repository baseline
3. Active time / method
4. Spend
5. Isolation confirmation
6. Control elapsed
7. Package A elapsed
8. Package B elapsed
9. Parallel overlap
10. Package critical path
11. Routing gap
12. Integration elapsed
13. Treatment elapsed
14. CF1 zero-routing result
15. CF2 zero-integration result
16. Break-even integration bound
17. Strong-positive overhead bound
18. Semantic duplication finding
19. Evidence-retrieval duplication finding
20. Boundary-concept duplication finding
21. Final-form duplication finding
22. Integrator-work finding
23. Contract-quality finding
24. Granularity/fixed-cost finding
25. Work-amplification finding
26. Human-attention finding
27. Compute/cost finding
28. Primary failure classification
29. Secondary failure classifications
30. 040/041 combined interpretation
31. Provisional delegation rule
32. Another parallel test earned: yes/no
33. Exact reopening/retest condition
34. What must not be built
35. Artifact path
36. Commit SHA
37. Exactly one recommended next action
