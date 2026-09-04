# Experiment 040 — Control-versus-Treatment Comparison

## Frozen design

- Frozen baseline: `12e1a21f71d169b4ff62fbb15ff51ae20a234999`
- Workload: repository-only reconstruction and audit of operational telemetry for Experiments 020, 021, 025, 026, 030, 031, 032, 033, 034, and 035
- Measurement freeze received: `2026-09-04T11:39:23Z`
- Control output: frozen and complete in `experiments/040/control.md`
- Treatment output: frozen and complete in `experiments/040/treatment.md`
- Isolation: preserved until both arm outputs and both blind packets froze
- External action: none
- Live Experiment 030/035 state: not inspected

## Arm identity reveal

The mapping was sealed before arm execution and revealed only after the human measurements were frozen:

| Blind packet | Arm |
|---|---|
| A | TREATMENT |
| B | CONTROL |

The acceptance packets remain byte-for-byte unchanged from their frozen published versions:

- Packet A SHA-256: `55698474befb1c1b4ec416a2f939d8db39114fcbfc7df678de42d38183161b62`
- Packet B SHA-256: `f1c251e047e1ffbbfa090abe453f02d38e199dbe127f9f64ba1dc97621059b5e`

## Frozen blind human measurements

| Measure | Control (B) | Treatment (A) |
|---|---:|---:|
| Accept / reject | Accept | Accept |
| Material corrections required | None | None |
| Additional evidence required | None | None |
| Clarity | High | High |
| Confidence | High | High |
| Human review minutes | 0.27 | 0.22 |
| Accepted material learning units | 1 | 1 |

The human read only the standardized acceptance packets during normal acceptance. No intermediate treatment artifact required human inspection, so no escalation minutes were added.

## Acceptance checklist

| SPEC-040 gate | Control | Treatment |
|---|---|---|
| 1. All ten experiments represented | PASS | PASS |
| 2. No live external state inspected | PASS | PASS |
| 3. Populated telemetry has quality classifications | PASS | PASS |
| 4. UNKNOWN not converted to zero | PASS | PASS |
| 5. Recorded and estimated time distinguished | PASS | PASS |
| 6. No false homogeneous funnel | PASS | PASS |
| 7. Delivery separated from exposure/effect/value | PASS | PASS |
| 8. Strongest supported conclusion bounded | PASS | PASS |
| 9. Strong unsupported conclusion explicit | PASS | PASS |
| 10. Contradictions/ambiguities surfaced | PASS | PASS |
| 11. Canonical project files unchanged | PASS | PASS |
| 12. Claims reconstructable from repository evidence | PASS | PASS |

Both outputs pass the common quality gate. Blind acceptance recorded no human-required correction or additional-evidence request for either packet.

## Primary HAL comparison

SPEC-040 defines `HAL = human active minutes / accepted material learning units`. Each accepted arm produced one unit.

| Arm | Calculation | HAL |
|---|---|---:|
| Control | `0.27 / 1` | 0.27 human minutes/unit |
| Treatment | `0.22 / 1` | 0.22 human minutes/unit |

Defensible descriptive calculations:

- Attention speedup: `0.27 / 0.22 = 1.23×`
- Treatment reduction: `0.05` minute, or `3.0` seconds
- Relative reduction: `0.05 / 0.27 = 18.5%`

The accounting includes the frozen packet-review measurements and all observed post-start human exception/clarification work. Both arms had zero such interventions and zero escalations. The initial standardized experiment request and unattended machine runtime were excluded as preregistered.

The treatment HAL is numerically lower. The absolute difference is only three seconds on one accepted unit, so it is not by itself a practically meaningful or generalizable human-attention advantage.

## Elapsed-time comparison

| Measure | Control | Treatment |
|---|---:|---:|
| Successful arm path | 117 seconds | 361 seconds from Producer start to recorded Synthesizer end |
| Role detail | One 117-second run | Producer 86 seconds; Reviewer 75 seconds; Adversary elapsed UNKNOWN; Synthesizer full role runtime UNKNOWN |
| Review concurrency | N/A | Reviewer and Adversary launched concurrently; overlap duration UNKNOWN |

For the frozen successful paths, `elapsed_speedup = 117 / 361 = 0.32×`; equivalently, treatment elapsed was `361 / 117 = 3.09×` control. The treatment did not reduce wall-clock time.

The treatment measurement includes file-mediated coordination gaps. The Synthesizer recorded only a seven-second late-captured interval and explicitly classified its full role runtime UNKNOWN, while the end-to-end Producer-start-to-Synthesizer-end boundary remains derivable. Initial failed launches produced no artifacts for either arm and are excluded from the successful-path figures; total elapsed including those attempts is UNKNOWN.

## Operational comparison

| Property | Control | Treatment | Finding |
|---|---|---|---|
| Human active minutes | 0.27 | 0.22 | Treatment lower by 0.05 minute; modest single-run difference |
| Human interventions after standardized start | 0 | 0 | Equal |
| Human escalations to intermediates | 0 | 0 | Treatment kept intermediate complexity machine-side |
| Successful production/review/synthesis agent runs | 1 | 4 | Treatment used Producer, Reviewer, Adversary, Synthesizer |
| Symmetric packet-formatting runs | 1 | 1 | Equal interface transformation |
| Initial artifactless launch retries | 1 | 1 | Equal; disclosed, not selected as evidence |
| Narrow retrieval retries in successful arm work | 2 | At least 3 | Producer recorded 2; Synthesizer recorded 1 |
| Clarification requests | 0 | 0 | Equal |
| Human-required factual/material corrections | 0 | 0 | Equal at blind acceptance |
| Machine review corrections before treatment freeze | N/A | Enumerated as 6, while telemetry summary says 5 | Treatment caught issues; internal count inconsistency preserved |
| Listed final contradictions/ambiguities | 7 | 9 | Descriptive only; not treated as a quality score |
| Listed unsupported conclusions | 8 | 13 | Treatment explicitly rejected more tempting inferences; counts are descriptive only |
| Repository drift/scope violations | 0 | 0 | Equal |
| External spend | €0 incremental | €0 incremental | No paid external service used |
| Compute/model cost | UNKNOWN | UNKNOWN | Cost multiplier not calculated |

## Reviewer contribution

The Reviewer independently reconstructed all ten rows, confirmed the core numerical table, and returned `FAIL — FIX REQUIRED`. It identified two acceptance-blocking categories:

1. the abbreviated Experiment 025 path was not reconstructable as an exact citation; and
2. “progressively later” overstated what heterogeneous experiment sequences support.

The final treatment used the full source path and replaced monotonic progression with a bounded, non-causal statement. This was material independent error detection, not ceremonial review.

## Adversary contribution

The Adversary also returned `FAIL pending correction` and contributed distinct challenges beyond the Reviewer’s core findings:

- “accumulated policy enabled” was unsupported causal attribution;
- describing bounded artifacts as produced “quickly” lacked a matched benchmark;
- experiment-local HIGH/LOW yield labels were not cross-experiment comparable; and
- the claimed pre-Experiment-036 independent draft order was unverifiable without a separately frozen pre-cross-check artifact.

It also reinforced the exact-citation issue and the right-censoring/cost discipline that survived attack. These challenges materially narrowed the final claim.

## Synthesizer contribution and preserved disagreement

The Synthesizer incorporated six enumerated changes: exact Experiment 025 path, removal of causal attribution, removal of monotonic-progression language, removal of unbenchmarked speed language, explicit local/non-comparable yield labels, and UNKNOWN classification for the unverified pre-cross-check ordering.

It preserved rather than averaged away the Experiment 031 funnel contradiction, right-censored 030/035 outcomes, human-attention gaps in historical evidence, non-comparable yield labels, UNKNOWN compute cost, and UNKNOWN pre-cross-check ordering.

The treatment telemetry summary says five material corrections while its change list enumerates six. That internal counting inconsistency is preserved here; no synthetic count replaces it.

## False PASS and material corrections

The Producer’s frozen candidate concluded `PASS as a Producer reconstruction`. Both independent checks then rejected it. This is one intermediate false PASS caught before the human-facing treatment output.

The review/adversary path produced at least five material correction categories and six enumerated edits. After synthesis, the blind human required no further correction or evidence. The control also required no human correction, but it had no independent pre-freeze review, so absence of observed correction is not proof that no latent issue existed.

## Coordination burden and duplicate work

Treatment created intentional duplicate reconstruction and checking across three pre-synthesis roles, four successful arm runs instead of one, at least one additional retrieval retry, file-mediated handoffs, and a substantially longer elapsed path. Reviewer and Adversary ran concurrently, but their elapsed overlap and compute cost were not exposed.

The duplicate work produced observable value by preventing the intermediate false PASS and narrowing claims without human intervention. It nevertheless increased machine-side work and coordination. No orchestration infrastructure was built, no manual human reconciliation was needed, and ordinary files were sufficient for all handoffs.

## Decision-compression observations

Token counts were unavailable. The following byte counts are descriptive proxies only and are not quality scores.

| Measure | Control | Treatment |
|---|---:|---:|
| Frozen arm working output bytes | 11,535 | 35,213 across Producer, Reviewer, Adversary, and Synthesizer |
| Final human-facing packet bytes | 9,731 | 10,662 |
| Working-output / packet byte ratio | 1.19:1 | 3.30:1 |

The numerator excludes the standardized packet itself to avoid counting the denominator twice. Treatment generated `3.05×` as many frozen working-output bytes as control, then compressed them into a human packet only 931 bytes (`9.6%`) larger. The human was not required to read the treatment intermediates.

This demonstrates the intended interface behavior—agents absorbed internal review complexity and exposed a compressed packet plus no exception—but not a robust human-attention advantage. The three-second review difference is too small and the single workload too narrow to separate operating-model benefit from timing noise.

## Cost comparison

Incremental external spend was €0 for both arms. Model/credit/compute cost was not exposed and remains UNKNOWN. Because treatment used more agent runs and generated more intermediate output, higher compute consumption is plausible, but its magnitude and proportionality cannot be established. No cost multiplier is calculated.

## Overall comparison

- Quality: preserved; both packets passed and were accepted with High clarity and High confidence.
- HAL: numerically improved from 0.27 to 0.22 minutes/unit, but only by three seconds.
- Elapsed time: worse for treatment; 361 versus 117 seconds on the successful frozen path.
- Error detection: better observed treatment process; independent review caught one intermediate false PASS and several unsupported formulations.
- Human burden: no intermediate escalation or manual reconciliation in either arm.
- Machine burden: materially higher for treatment; exact compute cost UNKNOWN.

## SPEC-040 verdict

**B — PROMISING BUT INCONCLUSIVE.**

The treatment preserved accepted quality and demonstrated useful independent error detection while keeping intermediate complexity away from the human. Its measured HAL was numerically lower, but the three-second absolute saving is not practically persuasive on one workload. Treatment wall-clock time and machine coordination were higher, and compute cost was unavailable. The evidence earns improved measurement/replication, not an agentic architecture or a general multi-agent operating claim.
