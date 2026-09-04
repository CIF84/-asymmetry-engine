# Experiment 042 — Parallel Decomposition Postmortem

## 1. Verdict

**C — STRUCTURAL DECOMPOSITION TAX**

- **[MEASURED]** Experiment 041 proved real concurrency and preserved accepted quality, but treatment required 301 seconds versus 202 seconds for control (`experiments/041/execution-telemetry.md:7-15,54-60`; `experiments/041/comparison.md:18-49`).
- **[DERIVED]** Removing all routing delay leaves 251 seconds. Removing all integration leaves 169 seconds, which is only 16.3% below control and still misses SPEC-041's predeclared 20% strong-positive threshold (`experiments/041/comparison.md:97-105`).
- **[INFERRED]** The work packages were operationally separable but not economically independent at this workload granularity. Fixed integration plus necessary cross-boundary synthesis defeated the parallel benefit.
- **[UNKNOWN]** The exact division of the 82-second Integrator wrapper among semantic reconciliation, normalization, and final generation cannot be recovered.

## 2. Repository baseline

- **[MEASURED]** Repository: `https://github.com/CIF84/-asymmetry-engine.git`
- **[MEASURED]** Synchronized baseline: `34f1b71309906426b8f402138c5e4238b19f3813`
- **[MEASURED]** SPEC-042 exists at that commit and Experiment 041's completed commit `b922ce0f23bfbb31dac3bc752014e8226442e7c7` is in its history.

## 3. Active time and timing method

- **[MEASURED]** Prospective active-work start: `2026-09-04T18:33:03Z`, captured before SPEC-042 analysis.
- **[MEASURED]** Active-work end: `2026-09-04T18:38:08Z`.
- **[DERIVED]** Active time: `305` seconds (`5.08` minutes), calculated from prospectively captured epoch timestamps.
- **[MEASURED]** Method: one continuous postmortem work interval; unattended external-agent execution did not occur; no parallel work packages were spawned.
- **[INFERRED]** This interval is adequate for the bounded audit because all stop conditions were met; further archaeology was unlikely to change the counterfactual bounds or failure classification.

## 4. Spend

- **[MEASURED]** Incremental external spend: `€0`.
- **[UNKNOWN]** Model/compute/credit cost was not exposed and is not inferred from runs, elapsed time, or bytes.

## 5. Isolation confirmation

- **[MEASURED]** Repository-only analysis; no external actor contact or live external research.
- **[MEASURED]** Experiment 030 and 035 live state was not inspected.
- **[MEASURED]** Experiment 041 artifacts were read but not modified.
- **[MEASURED]** Source, tests, canonical documents, prior experiments, and frozen models were not modified.
- **[MEASURED]** No new agentic treatment, parallel package execution, orchestration optimization, or infrastructure work occurred.

## 6. Authoritative 041 timing reconstruction

**[MEASURED]** External wrapper telemetry is authoritative (`experiments/041/execution-telemetry.md:3-15,17-60`).

| Component | Value | Quality |
|---|---:|---|
| Control end-to-end | 202 s | MEASURED |
| Package A | 169 s | MEASURED |
| Package B | 159 s | MEASURED |
| Parallel overlap | 159 s | DERIVED from measured wrapper intervals |
| Package critical path | 169 s | DERIVED as `max(169,159)` |
| Routing/dependency gap | 50 s | DERIVED from slower-package end to Integrator start |
| Integration elapsed | 82 s | MEASURED by external wrapper |
| Post-package overhead | 132 s | DERIVED as `50 + 82` |
| Treatment end-to-end | 301 s | DERIVED from earliest package start to Integrator freeze |

- **[DERIVED]** Treatment equation: `169 + 50 + 82 = 301` seconds.
- **[DERIVED]** Treatment was `99` seconds or `49.0%` slower than control; elapsed speedup was `202 / 301 = 0.67×` (`experiments/041/comparison.md:97-105`).

## 7. Internal/external timing ambiguity

- **[MEASURED]** Control reported an internal 93-second interval while its authoritative external wrapper measured 202 seconds. Its internal package/reconciliation intervals were 34/26/7 seconds plus 26 seconds of internal transition overhead; 109 wrapper seconds fall outside that self-recorded interval (`experiments/041/control.md:13-31`; `experiments/041/comparison.md:55-63`).
- **[MEASURED]** Package A and B internally reported 62 and 67 seconds, versus authoritative wrappers of 169 and 159 seconds (`experiments/041/treatment-A.md:5-20`; `experiments/041/treatment-B.md:3-17`; `experiments/041/comparison.md:65-80`).
- **[MEASURED]** The Integrator internally reported 24 seconds and a 253-second treatment path, versus the authoritative 82-second wrapper and 301-second path (`experiments/041/treatment.md:11-33`; `experiments/041/comparison.md:82-95`).
- **[INFERRED]** Internal boundaries excluded varying startup, retrieval, generation, or output-freeze work and are not semantically comparable across arms.
- **[UNKNOWN]** The 109 control-wrapper seconds and the role-level wrapper/internal deltas cannot be reliably allocated to individual activities.

## 8. CF1 zero-routing analysis

- **[DERIVED]** `package critical path + integration = 169 + 82 = 251` seconds.
- **[DERIVED]** CF1 remains `49` seconds (`24.3%`) slower than the 202-second control.
- **[INFERRED]** Eliminating incidental routing latency alone cannot rescue the treatment.

## 9. CF2 zero-integration analysis

- **[DERIVED]** Perfect zero-cost integration yields the 169-second package critical path.
- **[DERIVED]** CF2 is 33 seconds (`16.3%`) below control.
- **[DERIVED]** The 20%-lower strong-positive target was `0.8 × 202 = 161.6` seconds, so CF2 misses by `7.4` seconds.
- **[INFERRED]** Even an impossible zero-integration treatment would not earn SPEC-041's strongest positive verdict at the observed package durations.

## 10. CF3 break-even integration bound

Assuming zero routing delay:

- **[DERIVED]** `169 + integration = 202` gives a 33-second tie.
- **[DERIVED]** Integration must be strictly below 33 seconds to beat control; with whole-second measurements, at most 32 seconds.
- **[DERIVED]** The measured 82-second integration exceeds the tie bound by 49 seconds and would need a reduction greater than 59.8% to beat control.
- **[UNKNOWN]** Artifact evidence does not establish that such a reduction is achievable without shifting equivalent work into package preparation or output generation.

## 11. CF4 strong-positive overhead bound

- **[DERIVED]** Strong-positive total target: `161.6` seconds.
- **[DERIVED]** Maximum allowed post-package overhead: `161.6 - 169 = -7.4` seconds.
- **[DERIVED]** No nonnegative routing-plus-integration overhead can clear the 20% threshold with the observed package critical path.
- **[INFERRED]** A revised treatment limited to routing or Integrator optimization cannot satisfy the predeclared threshold; package execution would also have to change materially.

## 12. Semantic duplication audit

| Work category | Classification | Finding |
|---|---|---|
| Experiment/baseline/UNKNOWN discipline | NECESSARY SEMANTIC OVERLAP | Both packages needed the common contract and invariant boundary. |
| Implemented-versus-manual distinction | NECESSARY SEMANTIC OVERLAP | It is the final packet's central cross-boundary question, so both sides had to establish their side of it. |
| Generic-capability absences | NECESSARY SEMANTIC OVERLAP with some AVOIDABLE CONTRACT DUPLICATION | Package A listed absent software; Package B listed learned-but-unimplemented policy, forcing the Integrator to restate the boundary. |
| Historical/current-truth caveats | NECESSARY SEMANTIC OVERLAP | Code history capability and documentary evidence horizons intersect materially. |
| Repeated caveat and verdict prose | INCIDENTAL FORMAT DUPLICATION | Both packages were essay-like and the Integrator generated another final-form narrative. |

- **[INFERRED]** The split was semantically coupled at exactly the boundary the final answer had to explain, even though the packages could be produced independently.

## 13. Evidence-retrieval duplication

- **[MEASURED]** Package A's primary evidence was code, tests, `pyproject.toml`, and `ARCHITECTURE.md`; Package B's was README, ROADMAP, operating/economic documents, checkpoints, and experiment results (`experiments/041/treatment-A.md:23-48`; `experiments/041/treatment-B.md:19-40`).
- **[MEASURED]** The only explicit shared required files in their evidence lists were SPEC-041 and preregistration.
- **[INFERRED]** Evidence-retrieval duplication was low and predominantly necessary contract context, not the primary failure mechanism.
- **[UNKNOWN]** Hidden token-level retrieval overlap is unavailable and is not inferred.

## 14. Boundary-concept duplication

- **[MEASURED]** Package A explained implemented modules, explicit generic-capability absences, revision/history limits, and architecture discrepancies (`experiments/041/treatment-A.md:182-240`).
- **[MEASURED]** Package B explained conceptual layers, manual policy, evidence horizons, authorization, UNKNOWN, and learned-but-unimplemented automation (`experiments/041/treatment-B.md:248-300`).
- **[MEASURED]** The Integrator then explicitly reconciled implemented software, manual practice, learned policy, and unproven claims (`experiments/041/treatment.md:86-95`).
- **[INFERRED]** This is necessary cross-boundary synthesis, not evidence that either package violated independence. It is also a structural tax of this particular split.

## 15. Final-form duplication

- **[MEASURED]** Package A was 20,230 bytes, Package B 17,675 bytes, and the Integrator output 11,434 bytes. Treatment working output totaled 49,339 bytes versus 21,480 bytes for control (`experiments/041/comparison.md:143-156`).
- **[DERIVED]** Treatment produced `2.30×` the machine-side bytes of control.
- **[MEASURED]** The two packages were full prose artifacts with findings, caveats, confidence, and diagnostics; the Integrator produced another complete prose packet.
- **[INFERRED]** Normalizing and recompressing final-form essays created avoidable contract and incidental format duplication.
- **[UNKNOWN]** Bytes do not reveal compute cost, reasoning effort, quality, or exact seconds spent on reformatting.

## 16. Integrator-work classification

| Class | Qualitative finding | Evidence quality |
|---|---|---|
| COPY / STRUCTURAL ASSEMBLY | Present and necessary to form the required final sections | INFERRED |
| NORMALIZATION / FORMAT ALIGNMENT | Material because package schemas and prose organization differed | INFERRED |
| SEMANTIC RECONCILIATION | Material at software/manual and implemented/learned boundaries | INFERRED |
| CONTRADICTION / AMBIGUITY RESOLUTION | Bounded; it retained document-horizon, history-API, migration, runtime, and timing ambiguities | MEASURED/INFERRED |
| CROSS-BOUNDARY SYNTHESIS | Necessary and central to the final workload | INFERRED |
| CITATION VERIFICATION | One Git HEAD resolution; no repository content reads | MEASURED |
| OTHER / UNKNOWN | Per-category seconds and hidden reasoning remain UNKNOWN | UNKNOWN |

- **[MEASURED]** The Integrator performed zero additional repository content reads and no broad package re-research (`experiments/041/execution-telemetry.md:43-52`; `experiments/041/comparison.md:118-129`).
- **[INFERRED]** The 82 seconds were integration/normalization/generation work, not disguised re-execution of the two packages.

## 17. Necessary versus avoidable integration

Necessary:

- **[INFERRED]** reconcile the narrow CN75 reasoner with the non-implemented generic FORGE concept;
- **[INFERRED]** distinguish revision-aware evidence storage from a complete empirical operating system;
- **[INFERRED]** state what is software, manual practice, learned policy, and still unproven;
- **[INFERRED]** preserve bounded discrepancies and UNKNOWNs spanning both domains.

Potentially avoidable:

- **[INFERRED]** duplicate final verdict/confidence/caveat prose;
- **[INFERRED]** normalize two different package structures into the mandated final form;
- **[INFERRED]** repeat common glossary and non-inference language.

- **[UNKNOWN]** No artifact-local timing separates necessary from avoidable integration seconds, so no savings estimate is assigned.

## 18. Contract-quality assessment

- **[MEASURED]** The package contract successfully enforced scope, read-only isolation, independent freezing, and reconstructable evidence.
- **[INFERRED]** It was weak as an integration interface: both packages returned broad narrative artifacts rather than a shared rigid claims/deltas schema, explicit cross-boundary questions, or compact evidence records.
- **[INFERRED]** A rigid shared schema, glossary, or package-specific exclusions could reduce normalization and repeated prose.
- **[UNKNOWN]** Such changes may merely shift equivalent work into contract preparation or package formatting. 041 did not measure the shifted-work counterfactual.
- **[DERIVED]** Contract-only routing/integration improvements cannot clear the 20% threshold unless package critical-path time also falls by at least 7.4 seconds.

## 19. Granularity/fixed-cost assessment

- **[MEASURED]** Package wrappers were only 159–169 seconds, while integration was 82 seconds and routing 50 seconds.
- **[DERIVED]** Integration equaled 48.5% of the package critical path; routing equaled 29.6%; combined overhead equaled 78.1%.
- **[INFERRED]** The workload was too small at this decomposition/interface boundary to amortize fixed startup, routing, synthesis, and output-freeze costs.
- **[UNKNOWN]** Larger independent packages might amortize fixed cost, but 041 does not support linear extrapolation or choosing a larger favorable workload as a rescue.

## 20. Control-versus-treatment work amplification

- **[MEASURED]** Successful arm runs: control 1, treatment 3.
- **[MEASURED]** Retrieval retries: 2 for each arm; context restarts: 0 for each.
- **[MEASURED]** Working output: 21,480 bytes control versus 49,339 treatment (`2.30×`).
- **[MEASURED]** Human packet: 16,921 bytes control versus 9,451 treatment.
- **[INFERRED]** Treatment amplified machine-side production while compressing the final interface, but that compression did not improve accepted-output elapsed or human review time.

## 21. Human-attention implication

- **[MEASURED]** Both outputs were accepted with High clarity/confidence and no correction or additional evidence request.
- **[MEASURED]** Control HAL was 0.27 minutes; treatment HAL 0.30 minutes; no intermediate human inspection or intervention occurred (`experiments/041/comparison.md:18-49,107-116`).
- **[DERIVED]** Treatment used 1.8 seconds (`11.1%`) more human review time.
- **[INFERRED]** The difference is too small to establish material harm, but there is no human-attention compensation for the elapsed regression.

## 22. Compute/cost implication

- **[MEASURED]** Incremental external spend was €0 for both arms.
- **[UNKNOWN]** Compute/model/credit cost and cost multiplier are unavailable.
- **[INFERRED]** Three runs and 2.30× output are possible cost drivers, not cost measurements.
- **[INFERRED]** Cost uncertainty weakens any case for another treatment; it does not convert UNKNOWN into evidence of high or low cost.

## 23. Relationship to Experiment 040

- **[MEASURED]** Experiment 040's epistemic-redundancy treatment caught an intermediate false PASS but was slower and produced only an immaterial three-second HAL difference (`experiments/040/result.md:105-146`).
- **[MEASURED]** Experiment 041 isolated parallel decomposition, achieved real overlap, preserved quality, but worsened elapsed by 49.0% (`experiments/041/result.md:45-90,116-126`).
- **[INFERRED]** Epistemic independence may justify an extra agent for bounded error detection; mere task separability does not justify an extra agent for critical-path speed.
- **[INFERRED]** No synthetic multi-agent score combines these different mechanisms.

## 24. Primary failure classification F1–F6

**[INFERRED] F4 — GRANULARITY / FIXED-COST MISMATCH**

- **[DERIVED]** The 132-second fixed routing/integration tax was 78.1% of the 169-second package critical path.
- **[DERIVED]** Even perfect zero-cost integration could not clear the 20% threshold at the observed package durations.
- **[INFERRED]** The packages were too small for this fixed coordination and synthesis boundary to amortize.

## 25. Secondary failure classifications

1. **F3 — STRUCTURAL SEMANTIC COUPLING. [INFERRED]** The final question required reconciliation across software/manual, implemented/learned, history/current, and evidence/governance boundaries. This work remained after independent package production.
2. **F2 — CONTRACT / INTERFACE FAILURE. [INFERRED]** Full-form heterogeneous prose required normalization and recompression; a narrower claims/deltas interface might reduce some work, but savings are unmeasured and may be shifted.
3. **F1 — INCIDENTAL ROUTING FRICTION. [MEASURED/DERIVED]** The 50-second routing gap was real, but eliminating it still leaves treatment 24.3% slower than control.

- **[INFERRED]** F5 is not assigned because no concrete treatment defect explains the result.
- **[DERIVED/UNKNOWN]** F6 is not primary because deterministic bounds establish F4, although per-category integration seconds remain UNKNOWN.

## 26. Strongest evidence for another parallel test

- **[MEASURED]** The package split achieved 159 seconds of actual overlap, two-second launch skew, independent frozen artifacts, zero cross-package reads, and integration without broad re-research (`experiments/041/execution-telemetry.md:17-52`).
- **[INFERRED]** This proves the mechanism can execute cleanly when packages are separable.
- **[INFERRED]** It does not meet SPEC-042's threshold for recommending another test because no concrete revised treatment has a feasible strong-positive timing budget.

## 27. Strongest evidence against another parallel test

- **[DERIVED]** CF4 permits negative 7.4 seconds of post-package overhead, so no routing/integration-only change can meet the predeclared threshold.
- **[MEASURED]** Accepted quality was equal, HAL did not improve, treatment used three runs and 2.30× output, and compute cost remained UNKNOWN (`experiments/041/comparison.md:143-181`).
- **[INFERRED]** Choosing a larger or more favorable workload without a naturally arising economic-independence condition would optimize the desired conclusion rather than test a revised mechanism.

## 28. Provisional delegation rule, if earned

**[INFERRED]** A narrow rule is earned for similar repository synthesis:

> Do not parallelize merely separable narrative work. Parallelize only when packages are independently verifiable, cross-boundary semantics are low, the output interface is compact, and a prospectively bounded `max(package elapsed) + routing + integration` is materially below the comparable single-agent path without increasing HAL or relying on UNKNOWN cost.

- **[DERIVED]** For a strong-positive replication using the 041 discriminator, the bound must satisfy `max(package elapsed) + routing + integration ≤ 0.8 × control elapsed` with all terms nonnegative and semantically comparable.

## 29. What must not be optimized/built yet

- **[INFERRED]** Do not build or optimize an orchestration server, scheduler, router, task graph, message broker, agent API, shared memory, persistent identity, dashboard, or autonomous delegation policy.
- **[INFERRED]** Do not optimize the measured 50-second routing gap as if it were the decisive cause; CF1 disproves that.
- **[INFERRED]** Do not convert a structured-output hypothesis into canonical infrastructure before evidence shows that shifted work and compute economics improve.

## 30. Whether another parallel-agent experiment is earned: no

**[DERIVED/INFERRED] No.**

- **[DERIVED]** The observed package critical path already exceeds the strong-positive target before any nonnegative integration cost.
- **[INFERRED]** Contract improvements are plausible but not quantified, and they may shift work rather than save it.
- **[UNKNOWN]** Compute economics remain unavailable.

## 31. What evidence would reopen parallel testing

**[INFERRED]** Reopen only when a naturally arising workload—not selected because it is larger or favorable—has independently verifiable package outputs and a preregistered compact interface, and pre-existing/pilot evidence supports the feasibility inequality:

`max(package_A, package_B) + routing + integration ≤ 0.8 × comparable_single_agent_elapsed`

- **[INFERRED]** All terms must use comparable external boundaries; routing and integration must be nonnegative and include shifted contract-preparation/formatting work; treatment HAL must not materially worsen; compute cost must be measurable or bounded enough to judge proportionality. Until then, the reopening condition is not met.

## 32. What the agentic operating-model hypothesis now says

- **[INFERRED]** Agent count should follow the kind of independence, not task size or apparent separability.
- **[INFERRED]** Experiment 040 provides bounded evidence that epistemically independent challenge can protect quality.
- **[INFERRED]** Experiments 041–042 show that operationally separate narrative packages can still be economically coupled by fixed integration and cross-boundary semantics.
- **[INFERRED]** For similar repository reconstruction/synthesis, single-agent execution remains the supported default.

## 33. Exactly one recommended next action

Preserve single-agent execution for similar cross-boundary repository reconstruction and synthesis workloads.
