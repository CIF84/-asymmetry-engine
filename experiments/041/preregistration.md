# Experiment 041 — Preregistration

**Frozen baseline:** `6360064ea874e7350de2121e9cc569b9045fd1e0`  
**Matched workload:** Repository Reconstructability Packet defined by SPEC-041  
**Canonical truth:** read-only  
**External interaction/spend:** prohibited / €0  
**Compute/model cost:** UNKNOWN unless exposed

## Package-independence gate

Result: **PASS** before arm execution.

1. Package A can be answered independently from current code, tests, and documentation cross-checks; it does not require Package B output.
2. Package B can be answered independently from persisted documentation, specifications, and experiments; it does not require Package A output.
3. Both packages are repository-read-only and mutate no shared state.
4. Each package has a complete bounded contract and can freeze a reconstructable artifact independently.
5. Integration requires only comparison of the software/operating boundary, citation resolution, and explicit ambiguity reconciliation. It does not require either package to be re-executed from scratch.

The packages are semantically related at the final boundary but operationally independent. This is genuine decomposition, not Reviewer/Adversary redundancy.

## Arm contracts and isolation

- Control: exactly one agent performs Package A, then Package B, then reconciliation and freezes one output. No delegation.
- Treatment: exactly one Package-A Agent and one Package-B Agent launch as concurrently as the environment permits. Each freezes an isolated artifact and cannot read the other. Exactly one Integrator then reads the two frozen artifacts plus only bounded repository evidence required for explicit conflict, citation, or cross-boundary reconciliation.
- No Reviewer or Adversary role is permitted.
- Control and treatment use the same repository baseline and workload contract.
- Neither arm may read the other arm's prompts, outputs, or conclusions before both final arm outputs freeze.
- Arm outputs are temporary and isolated until freeze; repository files mediate only permitted persistent experiment records.

## Blind acceptance

The packet mapping was randomly selected and sealed before arm execution in an isolated temporary file. Seal SHA-256: `a4c811fff4da5582ab282ecfa6813eb8c554839700f1c92f8a805736b4faf8ec`.

After both arms freeze, structurally equivalent packets labeled only A and B will be created without process telemetry, topology, or arm identity. The mapping will remain sealed until the human freezes accept/reject, corrections, evidence requests, clarity, confidence, and review minutes for both packets. Frozen arms cannot rewrite after comparison.

## Prospective telemetry method

- Each model execution is wrapped by an external UTC start/end/epoch capture; elapsed seconds are derived from those timestamps.
- Control records its overall wrapper interval and is instructed to capture Package A, Package B, and reconciliation boundaries internally where practicable.
- Treatment package wrappers launch concurrently; overlap is derived from their external start/end intervals.
- Integrator uses a separately timed wrapper after both package artifacts freeze.
- Integrator must enumerate every direct repository read and classify its reason as CONFLICT RESOLUTION, CITATION VERIFICATION, CROSS-BOUNDARY RECONCILIATION, or OTHER with explanation.
- Retries, failures, context restarts, clarifications, human interventions, and output bytes are recorded where exposed. UNKNOWN remains UNKNOWN.
- Initial standardized launch and unattended runtime are excluded from HAL. Blind packet review, clarification, exception inspection, correction, and manual reconciliation are included.
- Model/credit cost remains UNKNOWN unless the execution environment exposes it. Incremental external spend is recorded separately.

## Acceptance and metrics

Both arms will be judged against the same twelve-item SPEC-041 gate. One accepted packet equals one accepted material learning unit.

- `AEL = successful-path wall-clock elapsed seconds / accepted material learning units`
- `HAL = human active minutes / accepted material learning units`

No speedup, overlap, integration, HAL, or cost ratio will be calculated unless its inputs and denominators are defensible.
