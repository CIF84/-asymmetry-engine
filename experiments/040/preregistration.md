# Experiment 040 — Preregistration and Measurement Contract

**Frozen baseline:** `12e1a21f71d169b4ff62fbb15ff51ae20a234999`  
**Workload:** independent reconstruction of operational telemetry for Experiments 020, 021, 025, 026, 030, 031, 032, 033, 034, and 035  
**External spend ceiling:** €0  
**Canonical truth:** read-only  
**External interaction:** prohibited

## Arm isolation

- Control and treatment receive the same frozen SPEC-040 workload and baseline.
- Each arm independently reconstructs primary experiment/checkpoint evidence before consulting Experiment 036 as a post-reconstruction cross-check.
- Arm working artifacts remain in separate temporary directories until both final outputs freeze.
- Neither arm may read the other arm's files, conclusions, prompts, or messages before freeze.
- No frozen output may be rewritten after cross-arm comparison begins.
- Only permitted Experiment 040 artifacts will be copied into the repository.

## Treatment roles

The treatment uses Producer → independently concurrent Reviewer and Adversary → Synthesizer. Producer output freezes before review. Reviewer and Adversary read the same frozen Producer artifact but not each other's work. Synthesizer reads only persisted treatment role artifacts and repository evidence needed to resolve disagreements. Material unresolved disagreement must remain visible or escalate.

The workload is decomposable because the fixed table can be produced once and independently checked for factual/evidentiary failure; all work is read-only; persisted files make handoffs verifiable; and concurrent review tests a real review critical path. No persistent orchestration mechanism will be created.

## Prospective telemetry

Each arm/role records UTC start and end timestamps from `date -u`, retries, tool failures, clarification requests, and output bytes. Wall-clock elapsed is derived from timestamps. Agent/model cost is `UNKNOWN` unless exposed by the environment. No commit time is used as execution time.

Human active attention excludes unattended agent runtime and the initial standardized experiment request. It includes any additional delegation/clarification burden, exception handling, substantive acceptance review, correction, or reconciliation. Normal packet review will be prospectively self-timed by the human and reported in minutes. If an exception requires inspection of treatment intermediates, that time will be added to treatment human active minutes and the reason recorded as an escalation.

## Normal human acceptance interface

For HAL measurement, the normal human review surface for each arm is only that arm's standardized final acceptance packet.

Treatment Producer, Reviewer, Adversary, and Synthesizer artifacts are machine-to-machine evidence and audit material. The human is not required to read them during normal acceptance. If unresolved disagreement, suspected error, missing evidence, or another exception requires the human to inspect an intermediate treatment artifact, the inspection time is treatment human active time and its reason is an escalation.

This measures the intended hypothesis: agents absorb internal complexity; humans inspect compressed output and exceptions.

## Blind-ish human comparison

After both arms freeze, two structurally equivalent final acceptance packets will be labeled only `A` and `B`. Arm identity will not be disclosed until the human freezes, for each packet:

- accept / reject;
- material corrections required;
- additional evidence required;
- clarity assessment;
- confidence assessment;
- human review minutes.

The arm-label mapping is sealed in the isolated temporary workspace before arm execution and will be disclosed in the final comparison only after measurements freeze. Neither arm may revise its frozen output after seeing the other arm.

## Acceptance gate

Both packets are judged against the same twelve-item SPEC-040 checklist: all ten experiments; isolation; quality labels; UNKNOWN discipline; recorded/estimated time distinction; no false homogeneous funnel; delivery/effect/value separation; bounded supported and unsupported conclusions; surfaced contradictions; no canonical change; and reconstructable sources.

One accepted packet equals one accepted material learning unit. For an accepted arm, HAL equals its human active review/escalation minutes. If rejected, accepted units are zero and HAL is reported as not meaningfully finite. Attention, elapsed time, cost, quality, and compression remain separate; unavailable ratios remain UNKNOWN.
