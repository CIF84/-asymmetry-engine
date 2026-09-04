# Experiment 041 — Matched Control-versus-Treatment Comparison

## Frozen design and reveal

- Frozen baseline: `6360064ea874e7350de2121e9cc569b9045fd1e0`
- Workload: SPEC-041 Repository Reconstructability Packet
- Package-independence preregistration: PASS before execution
- Arm outputs and blind packets: frozen before human review
- Human measurements frozen before reveal: yes
- Reveal recorded: `2026-09-04T18:13:26Z`
- Packet A: **TREATMENT**
- Packet B: **CONTROL**
- Live Experiment 030/035 state: not inspected
- Canonical repository truth: unchanged

The sealed-map SHA-256 remained `a4c811fff4da5582ab282ecfa6813eb8c554839700f1c92f8a805736b4faf8ec` from preregistration through reveal.

## Immutable blind human measurements

| Measure | Control (Packet B) | Treatment (Packet A) |
|---|---:|---:|
| Accept/reject | Accept | Accept |
| Material corrections required | None | None |
| Additional evidence required | None | None |
| Clarity | High | High |
| Confidence | High | High |
| Human review minutes | 0.27 | 0.30 |
| Accepted material learning units | 1 | 1 |

No human inspected the treatment package intermediates during normal acceptance. No correction, clarification, disagreement-resolution, or exception time was added for either arm.

## Quality gate

| SPEC-041 gate | Control | Treatment |
|---|---|---|
| 1. Package A implemented truth materially correct | PASS | PASS |
| 2. Package B operating/governance truth materially correct | PASS | PASS |
| 3. Software separated from manual practice | PASS | PASS |
| 4. Learned policy separated from automation | PASS | PASS |
| 5. Historical design not presented as current truth | PASS | PASS |
| 6. Live 030/035 state not inspected | PASS | PASS |
| 7. Revision-aware semantics accurate | PASS | PASS |
| 8. Authorization boundary accurate | PASS | PASS |
| 9. Commercial/repeatability claims remain unproven | PASS | PASS |
| 10. Material ambiguities surfaced | PASS | PASS |
| 11. Claims reconstructable from repository evidence | PASS | PASS |
| 12. Canonical files unchanged | PASS | PASS |

Both packets were independently accepted with High clarity and High confidence. No material correction, extra evidence, integration error, or repository drift was identified. Both preserved explicit unsupported-claim boundaries and bounded reconstruction ambiguities. The treatment was more concise at the human interface; concision is not treated as an independent quality win.

## Prospectively captured elapsed timing

External wrapper timing is authoritative for successful-path boundaries because it includes model startup, retrieval, generation, and output freeze. Internal agent timestamps are preserved as diagnostic sub-intervals but are not substituted for wrapper elapsed.

### Control

- External start: `2026-09-04T11:59:54Z`
- External freeze: `2026-09-04T12:03:16Z`
- End-to-end elapsed: `202` seconds
- Accepted units: `1`
- Control AEL: `202 / 1 = 202` seconds per accepted unit

The control self-recorded a 93-second internal interval: Package A 34 seconds, Package B 26 seconds, reconciliation 7 seconds, and 26 seconds of internal transition/telemetry overhead. The external wrapper contains another 109 seconds outside that self-recorded boundary. Because control package intervals are internal while treatment package intervals are external wrappers, cross-arm package-level speed ratios are not semantically comparable.

### Treatment packages

| Package | Start | End | Wrapper elapsed |
|---|---|---|---:|
| A | `2026-09-04T11:59:53Z` | `2026-09-04T12:02:42Z` | 169 s |
| B | `2026-09-04T11:59:55Z` | `2026-09-04T12:02:34Z` | 159 s |

- Launch skew: `2` seconds
- Actual overlap: `159` seconds
- Package-phase union: `169` seconds
- Parallel overlap fraction: `159 / 169 = 94.1%`
- Theoretical package-only critical path: `max(169, 159) = 169` seconds
- Hypothetical sequential duration for the same two treatment package runs: `169 + 159 = 328` seconds
- Package-stage time avoided by concurrency: `328 - 169 = 159` seconds, descriptive only

Package-internal timestamps were 62 seconds for A and 67 seconds for B. They exclude wrapper work and are not used for AEL.

### Treatment integration and end-to-end path

- Slower package freeze: `2026-09-04T12:02:42Z`
- Integrator wrapper start: `2026-09-04T12:03:32Z`
- Routing/dependency wait: `50` seconds
- Integrator wrapper elapsed: `82` seconds
- Integration/routing overhead above package critical path: `50 + 82 = 132` seconds
- Treatment start: earliest package start, `2026-09-04T11:59:53Z`
- Treatment freeze: `2026-09-04T12:04:54Z`
- End-to-end elapsed: `301` seconds
- Accepted units: `1`
- Treatment AEL: `301 / 1 = 301` seconds per accepted unit

The Integrator artifact contains a narrower internal 24-second interval and an internally calculated 253-second path. Those values omit wrapper time. They are preserved as a telemetry-boundary ambiguity; the prospectively captured external wrapper yields the comparable 301-second accepted-output boundary.

## Elapsed comparison and practical threshold

- Elapsed speedup: `control / treatment = 202 / 301 = 0.67×`
- Treatment penalty: `301 - 202 = 99` seconds
- Relative treatment penalty: `99 / 202 = 49.0%`
- SPEC-041 strong-positive threshold: treatment normally at least 20% lower than control, or at most `161.6` seconds here
- Actual treatment: `301` seconds, `139.4` seconds above that threshold

Parallelism reduced the treatment package phase relative to the same package agents running sequentially, but it did not reduce the matched accepted-output critical path. Even eliminating the 50-second routing gap would leave `169 + 82 = 251` seconds, still 49 seconds slower than control. Even omitting integration entirely would produce a 169-second package phase, only 16.3% below control and short of the preregistered 20% threshold.

## HAL and human-attention guardrail

Each accepted packet equals one material learning unit.

- Control HAL: `0.27 / 1 = 0.27` human minutes per accepted unit
- Treatment HAL: `0.30 / 1 = 0.30` human minutes per accepted unit
- Attention ratio, control/treatment: `0.27 / 0.30 = 0.90×`
- Treatment difference: `0.03` minute = `1.8` seconds = `11.1%` more than control

Both arms recorded zero human interventions, clarifications, intermediate inspections, corrections, escalations, and manual integration. The 1.8-second difference is not a material human-attention regression, but it provides no HAL advantage.

## Integrator re-research assessment

The Integrator primarily reconciled the two frozen packages.

- Required inputs: frozen Package A, frozen Package B, SPEC-041, and preregistration
- Additional repository content reads: `0`
- Additional Git operation: one `HEAD` resolution, classified `CITATION VERIFICATION`
- Broad package re-research: no
- Package conflict requiring re-execution: no
- Manual human reconciliation: no

The Integrator did not hide broad reconstruction work inside the integration phase. Its 82-second wrapper elapsed is integration execution/formatting overhead, not a disguised second Package A/Package B research pass.

## Package-independence assessment

The preregistered five-part independence gate passed operationally:

1. Package A froze without Package B output.
2. Package B froze without Package A output.
3. Neither package mutated shared state.
4. Both produced reconstructable frozen artifacts.
5. The Integrator reconciled them without re-execution or broad re-research.

The two-second launch skew and 159-second overlap demonstrate real concurrency. Independence was sufficient to enable parallel work, but not sufficient to improve matched end-to-end economics.

## Machine-side work

| Measure | Control | Treatment |
|---|---:|---:|
| Successful arm agent runs | 1 | 3 |
| Symmetric blind packet-formatting runs | 1 | 1 |
| Retrieval retries in arm work | 2 | 2 total: Package A 0, Package B 1, Integrator 1 |
| Context restarts | 0 | 0 |
| Arm working-output bytes | 21,480 | 49,339 |
| Human-facing packet bytes | 16,921 | 9,451 |
| Incremental external spend | €0 | €0 |
| Compute/model/credit cost | UNKNOWN | UNKNOWN |

Treatment produced `49,339 / 21,480 = 2.30×` the frozen machine-side output. Its human packet was 7,470 bytes (`44.1%`) smaller, yet human review time was 1.8 seconds longer. Output size is descriptive and not treated as quality or cost. Compute cost remains UNKNOWN, so no cost multiplier is calculated.

The control also made one unsuccessful bare-`pytest` invocation because `pytest` was absent from its PATH; no retry followed. The repository integrity suite was later run outside both frozen arms using `.venv/bin/pytest`, so this arm-local limitation does not change the blind acceptance evidence.

## Quality comparison

- Acceptance: both accepted.
- Material corrections: none for either packet.
- Additional evidence: none for either packet.
- Clarity/confidence: High/High for both.
- Unsupported claims: both explicitly rejected conflation of software/manual practice, delivery/effect/value, UNKNOWN/zero, and evidence/commercial proof.
- Unresolved contradictions: both preserved bounded document-vocabulary, evidence-horizon, source-history, and runtime uncertainties; treatment additionally preserved wrapper/internal timing mismatch.
- Integration errors: none identified by the blind human or repository audit.
- Repository drift: none.

Accepted quality was preserved. It does not imply lower elapsed time, lower human attention, or lower compute cost.

## Coordination result

There was no package-independence failure, broad Integrator re-research, human routing intervention, or repository-integrity failure. The negative operating result arose from measurable coordination economics: a 50-second routing gap, an 82-second integration wrapper, slower per-package wrapper paths than the control's full 202-second result, and three arm agents instead of one.

## Overall SPEC-041 verdict

**D — PARALLEL TREATMENT WORSE.**

Both arms preserved accepted quality, but treatment successful-path elapsed was 49.0% worse, HAL was numerically worse, machine-side output and role count increased, and compute cost remained UNKNOWN. The real package overlap did not compensate for integration/routing overhead or slower package execution. Under the predeclared verdict definition, substantially worse elapsed time without a compensating accepted-quality or attention benefit requires Verdict D.
