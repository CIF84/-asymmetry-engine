# Experiment 041 — Frozen Execution Telemetry

**Baseline:** `6360064ea874e7350de2121e9cc569b9045fd1e0`  
**Capture method:** external UTC/epoch wrapper, preregistered before arm execution  
**Arm mapping:** sealed and intentionally omitted pending frozen human acceptance

## Control successful path

- Start UTC: `2026-09-04T11:59:54Z`
- End UTC: `2026-09-04T12:03:16Z`
- Elapsed: `202` seconds (DERIVED from recorded epochs)
- Exit code: `0`
- Final artifact frozen: yes

The control artifact contains its internal Package A, Package B, and reconciliation timing where captured. External wrapper telemetry is authoritative for the successful-path boundary.

## Treatment package phase

### Package A

- Start UTC: `2026-09-04T11:59:53Z`
- End UTC: `2026-09-04T12:02:42Z`
- Elapsed: `169` seconds
- Exit code: `0`
- Artifact frozen: yes

### Package B

- Start UTC: `2026-09-04T11:59:55Z`
- End UTC: `2026-09-04T12:02:34Z`
- Elapsed: `159` seconds
- Exit code: `0`
- Artifact frozen: yes

### Parallelism diagnostics

- Launch skew: `2` seconds
- Package-phase union: `169` seconds
- Theoretical package-only critical path: `max(169, 159) = 169` seconds
- Parallel overlap: `159` seconds
- Parallel overlap fraction: `159 / 169 = 94.1%` of the package-phase union

## Integrator

- Start UTC: `2026-09-04T12:03:32Z`
- End UTC: `2026-09-04T12:04:54Z`
- Elapsed: `82` seconds
- Exit code: `0`
- Final treatment artifact frozen: yes
- Direct repository content reads beyond required artifacts: `0`
- Git HEAD resolution: `1`, classified `CITATION VERIFICATION`
- Broad package re-research: no

## Treatment successful path

- Start: earliest package start, `2026-09-04T11:59:53Z`
- End: Integrator freeze, `2026-09-04T12:04:54Z`
- Elapsed: `301` seconds
- Package-to-Integrator routing gap after the slower package froze: `50` seconds
- Integration/routing overhead above package critical path: `301 - 169 = 132` seconds

## Other telemetry

- Human clarifications/interventions during arm execution: `0` observed for both arms
- Human inspection of intermediate treatment artifacts for acceptance: `0` at this stage
- Context restarts: `0` reported
- Incremental external spend: `€0`
- Compute/model/credit cost: `UNKNOWN`; the environment did not expose it
- Accepted units, AEL, HAL, final speedup verdict: pending blind human acceptance and arm reveal
