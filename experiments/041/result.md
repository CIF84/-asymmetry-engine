# Experiment 041 — Result

## Status

COMPLETE — **D: PARALLEL TREATMENT WORSE**

## Baseline and isolation

- Baseline: `6360064ea874e7350de2121e9cc569b9045fd1e0`
- Workload: SPEC-041 Repository Reconstructability Packet
- Package-independence gate: PASS before execution
- Control: one agent, Package A then Package B then reconciliation
- Treatment: concurrent Package-A Agent and Package-B Agent, followed by one Integrator
- Reviewer/Adversary roles: none
- Isolation: separate prompts, temporary outputs, and file-mediated handoff; preserved until both arm outputs froze
- Worktrees: not required because roles were read-only and wrote only isolated temporary output before persistence
- External interaction: none
- Live Experiment 030/035 state: not inspected
- Canonical project truth: unchanged

## Arm reveal after frozen human review

- Packet A = TREATMENT
- Packet B = CONTROL
- Reveal time: `2026-09-04T18:13:26Z`

The human measurements were frozen before reveal. Acceptance packets were not modified; their SHA-256 hashes remain:

- A: `1884237a9b46e2cddef5b9465f0639c0f15e2201b37e0d3ac51ffb7867c15aea`
- B: `148f2831fc36c26681d1e0384e946ef40c9df568b28b1d14399ea52ed86e3f02`

## Frozen acceptance evidence

| Arm | Accepted | Corrections | Extra evidence | Clarity | Confidence | Human minutes |
|---|---|---|---|---|---|---:|
| Control / B | Yes | None | None | High | High | 0.27 |
| Treatment / A | Yes | None | None | High | High | 0.30 |

Both arms produced one accepted material learning unit and passed the twelve-item quality gate.

## Prospective timing method

Each arm execution used an external UTC/epoch wrapper fixed before launch. AEL uses those wrapper boundaries because they include startup, retrieval, generation, and artifact freeze. Internal role timestamps remain diagnostic and are not substituted for semantically comparable end-to-end wrappers. UNKNOWN values remain UNKNOWN.

## AEL and elapsed result

- Control end-to-end: `202` seconds
- Treatment end-to-end: `301` seconds
- Control AEL: `202` seconds per accepted unit
- Treatment AEL: `301` seconds per accepted unit
- Elapsed speedup: `202 / 301 = 0.67×`
- Treatment penalty: `99` seconds, or `49.0%`

The predeclared strong-positive threshold required treatment to be approximately 20% lower than control, no more than 161.6 seconds. Treatment was 301 seconds and therefore failed the threshold decisively.

## Package overlap and integration

- Package A wrapper elapsed: `169` seconds
- Package B wrapper elapsed: `159` seconds
- Launch skew: `2` seconds
- Actual overlap: `159` seconds
- Overlap fraction: `94.1%`
- Package-only critical path: `169` seconds
- Same treatment package runs if sequential: `328` seconds
- Routing/dependency wait after slower package: `50` seconds
- Integrator wrapper elapsed: `82` seconds
- Integration/routing overhead above package critical path: `132` seconds

Concurrency shortened the treatment's own package phase relative to a hypothetical sequential execution of those same package agents. It did not shorten the matched accepted-output path. With the routing gap removed, treatment would still be 251 seconds; with integration omitted entirely, its 169-second package phase would improve on control by only 16.3%, below the preregistered 20% threshold.

The treatment artifact's internal 253-second calculation uses narrower role timestamps. The externally wrapped 301-second result is authoritative; the mismatch is retained as a telemetry-boundary ambiguity.

## HAL and human attention

- Control HAL: `0.27` human minutes per accepted unit
- Treatment HAL: `0.30` human minutes per accepted unit
- Treatment difference: `0.03` minute = `1.8` seconds = `11.1%` higher
- Human interventions/clarifications/escalations: `0` for both
- Intermediate treatment inspection: none
- Manual integration/rewrite: none

The HAL difference is not materially large, but treatment did not improve the human-attention guardrail.

## Integrator assessment

The Integrator primarily reconciled the frozen packages. It performed zero additional repository content reads and one Git HEAD check classified as CITATION VERIFICATION. It did not broadly re-research or reconstruct either package, suppress a package conflict, or require human coordination. Repository-mediated handoff was sufficient.

## Package-independence result

Package A and Package B were genuinely independent enough for concurrent execution: each froze without reading the other, neither mutated shared state, the launches were two seconds apart, and 159 seconds overlapped. The Integrator used their outputs directly. The independence hypothesis passed; the operating-economics hypothesis did not.

## Quality result

- Both outputs accepted with High clarity and High confidence.
- No material corrections or additional evidence requested.
- No integration error detected.
- Both separated implemented software, manual practice, learned-but-unimplemented policy, and unproven claims.
- Both preserved revision semantics, authorization boundaries, commercial uncertainty, and UNKNOWN discipline.
- No repository drift or canonical mutation occurred.

Accepted quality was preserved. Accepted quality is not evidence of lower elapsed time, lower human attention, or lower compute cost.

## Machine-side work and cost

- Successful arm runs: Control `1`; Treatment `3`
- Retrieval retries: Control `2`; Treatment `2` total
- Context restarts: `0` for both
- Working-output bytes: Control `21,480`; Treatment `49,339` (`2.30×`)
- Human packet bytes: Control `16,921`; Treatment `9,451`
- Incremental external spend: €0 for both
- Compute/model/credit cost: UNKNOWN for both
- Cost multiplier: not calculated

Treatment created more machine-side work and a smaller human packet, but that smaller packet did not reduce measured human review time.

## Strongest findings

- Strongest positive: the package split was genuinely independent, achieved 159 seconds of overlap, and integrated without broad re-research or human reconciliation.
- Strongest negative: despite preserved quality, treatment took 301 seconds versus 202 seconds, a 49.0% regression, and used three successful arm runs instead of one.
- Strongest unresolved uncertainty: which portion of the 132-second routing/integration overhead is structurally necessary versus avoidable under a different bounded integration contract; compute cost also remains UNKNOWN.

## Overall verdict

**D — PARALLEL TREATMENT WORSE.**

Parallel decomposition worked mechanically but failed the matched operating-economics test. Quality remained equal, HAL did not improve, end-to-end elapsed worsened substantially, and machine-side work increased. SPEC-041 therefore does not earn another parallel test without a new hypothesis explaining the integration/coordination failure.

## Exactly one recommended next action

Run one bounded repository-only postmortem that decomposes the measured 132-second routing/integration overhead into necessary reconciliation versus avoidable handoff cost before proposing any further parallel-agent experiment.
