# Experiment 040 — Result

## Status

COMPLETE — **B: PROMISING BUT INCONCLUSIVE**

## Baseline and workload

- Baseline commit: `12e1a21f71d169b4ff62fbb15ff51ae20a234999`
- Workload: matched repository-evidence reconstruction for Experiments 020, 021, 025, 026, 030, 031, 032, 033, 034, and 035
- Canonical project truth: read-only and unchanged
- External interaction: none
- Live Experiment 030/035 state: not inspected

## Measurement method

Role timestamps were prospectively captured where practicable. Control elapsed is derived from its recorded start/end. Treatment end-to-end successful-path elapsed is derived from Producer start to recorded Synthesizer end; individual Adversary elapsed, full Synthesizer role runtime, dependency waits, and parallel-overlap duration remain UNKNOWN.

Human active time followed `experiments/040/preregistration.md`: the initial standardized request and unattended model runtime were excluded; packet review, clarification, correction, reconciliation, and exception inspection were included. The human reviewed only the two standardized blind packets and froze self-timed measurements before identity reveal. No treatment intermediate required human inspection and no escalation time was added.

Incremental external spend was observed as €0. The environment exposed no compute/model/credit price, so compute cost and cost multiplier remain UNKNOWN.

## Isolation and roles

The simplest existing mechanism was used: ephemeral read-only Codex executions, separate temporary output directories, and persisted file handoffs. No worktree was required because all roles were read-only and wrote only to isolated temporary output targets before freeze.

- Control: one agent performed the entire reconstruction without independent review.
- Treatment Producer: produced the frozen first candidate.
- Treatment Reviewer: independently checked evidence, classifications, completeness, and inference.
- Treatment Adversary: independently attempted to falsify the strongest conclusions.
- Treatment Synthesizer: read persisted role artifacts, resolved supported challenges from repository evidence, and preserved unresolved disagreement.
- Reviewer and Adversary were launched concurrently and could not read each other.
- Neither arm could read the other before both froze.

The sealed reveal after frozen human measurement is:

- Packet A = TREATMENT
- Packet B = CONTROL

## Files created

- `experiments/040/preregistration.md`
- `experiments/040/control.md`
- `experiments/040/producer.md`
- `experiments/040/reviewer.md`
- `experiments/040/adversary.md`
- `experiments/040/treatment.md` (the Synthesizer’s final output)
- `experiments/040/acceptance-A.md`
- `experiments/040/acceptance-B.md`
- `experiments/040/comparison.md`
- `experiments/040/result.md`

No separate `synthesizer.md` is needed because `treatment.md` is the frozen Synthesizer artifact.

## Frozen human acceptance evidence

| Packet / arm | Accepted | Material corrections | Additional evidence | Clarity | Confidence | Human review minutes |
|---|---|---|---|---|---|---:|
| A / Treatment | Yes | None | None | High | High | 0.22 |
| B / Control | Yes | None | None | High | High | 0.27 |

The frozen acceptance packets were not modified. Their SHA-256 values are:

- A: `55698474befb1c1b4ec416a2f939d8db39114fcbfc7df678de42d38183161b62`
- B: `f1c251e047e1ffbbfa090abe453f02d38e199dbe127f9f64ba1dc97621059b5e`

## Primary metric

Both arms passed the twelve-item quality gate and produced one accepted material learning unit.

- Control HAL: `0.27 / 1 = 0.27` human minutes per accepted unit
- Treatment HAL: `0.22 / 1 = 0.22` human minutes per accepted unit
- Attention speedup: `0.27 / 0.22 = 1.23×`
- Absolute difference: `0.05` minute = `3.0` seconds
- Relative difference: `18.5%` lower treatment review time

Treatment HAL is numerically lower, but the absolute saving is not practically meaningful evidence from one workload. The result does not establish a general human-attention advantage.

## Secondary metrics

| Metric | Control | Treatment |
|---|---:|---:|
| Accepted units | 1 | 1 |
| Human active minutes | 0.27 | 0.22 |
| Human interventions after standardized start | 0 | 0 |
| Intermediate-review escalations | 0 | 0 |
| Successful arm role runs | 1 | 4 |
| Successful-path elapsed | 117 s | 361 s |
| Elapsed speedup, control/treatment | — | 0.32× |
| Retrieval retries recorded in successful work | 2 | at least 3 |
| Initial artifactless launch retries | 1 | 1 |
| Human-required corrections | 0 | 0 |
| Frozen working-output bytes | 11,535 | 35,213 |
| Human-facing packet bytes | 9,731 | 10,662 |
| Byte compression proxy | 1.19:1 | 3.30:1 |
| Incremental external spend | €0 | €0 |
| Compute/model cost | UNKNOWN | UNKNOWN |
| Repository drift/scope violations | 0 | 0 |

Elapsed treatment/control multiplier was `3.09×`. Total elapsed including the initial artifactless launches is UNKNOWN. Token compression and compute-cost ratios are not calculated because the required inputs were not exposed.

## Quality and correction result

Both blind packets were accepted with High clarity and High confidence, no material human correction, and no request for more evidence.

Treatment review nevertheless added observable quality protection. The Producer initially returned PASS, while both Reviewer and Adversary returned FAIL pending correction. The final synthesis:

- repaired the exact Experiment 025 citation;
- removed unsupported causal attribution;
- removed monotonic-progression language;
- removed unbenchmarked speed language;
- made experiment-local yield labels explicitly non-comparable; and
- classified the claimed pre-cross-check draft ordering as UNKNOWN.

This is one intermediate false PASS caught before human exposure. The final treatment telemetry says five material synthesis corrections while its enumerated list contains six; the inconsistency remains disclosed rather than normalized.

The Reviewer supplied material source and boundedness checks. The Adversary added distinct causal, benchmark, comparability, and auditability challenges. The Synthesizer incorporated the supported challenges and retained the unresolved Experiment 031 funnel contradiction, right-censoring, UNKNOWN compute cost, and UNKNOWN pre-cross-check ordering.

## Decision compression and coordination

Treatment generated 35,213 bytes of frozen role output and presented a 10,662-byte packet, a descriptive 3.30:1 byte proxy. Control generated 11,535 bytes and presented 9,731 bytes, a 1.19:1 proxy. The treatment packet was 931 bytes (9.6%) larger, but the human did not inspect any of its intermediates.

Repository-mediated handoff was sufficient: no persistent orchestration infrastructure, human reconciliation, or intermediate escalation was required. Treatment also created intentional duplicate work, more role executions, more machine-side coordination, and a 3.09× longer successful elapsed path. Compute cost remains UNKNOWN.

## Strongest results

- Strongest positive: independent Reviewer and Adversary checks caught an intermediate false PASS and materially narrowed unsupported claims without adding human review or reconciliation work.
- Strongest negative: treatment required four successful arm roles and 361 seconds versus one role and 117 seconds, while the measured human-time saving was only three seconds.
- Strongest unresolved uncertainty: whether the tiny HAL difference and quality-protection benefit repeat on another workload at a compute and coordination cost proportionate to the attention saved.

## Interpretation

Accepted output quality, lower human attention, lower elapsed time, and lower compute cost are separate claims:

- accepted quality was preserved;
- human attention was numerically lower but not convincingly lower in practical terms;
- elapsed time was worse;
- compute cost is UNKNOWN and plausibly higher given the additional runs, but was not measured.

The treatment therefore does not earn agentification, orchestration infrastructure, or a general acceleration claim.

## Overall verdict

**B — PROMISING BUT INCONCLUSIVE.**

Quality was preserved, independent review contributed real value, and machine-side complexity stayed behind the acceptance interface. The HAL advantage was too small, the workload too singular, elapsed time worse, and compute cost too uncertain for Verdict A.

## Exactly one recommended next action

Run one second bounded matched experiment on a different repository-only workload with two genuinely parallel work packages, using the same blind packet-only human review and complete prospective elapsed/retry/compute telemetry where exposed.
