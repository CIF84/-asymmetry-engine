## ADVERSARY — Frozen Challenge

**Baseline:** `12e1a21f71d169b4ff62fbb15ff51ae20a234999` verified.  
**Start UTC:** UNKNOWN — not prospectively captured; not reconstructed.  
**End UTC:** `2026-09-03T23:47:49Z`  
**Cost:** UNKNOWN.  
**Scope:** Read-only. No control/Reviewer output or live Experiment 030/035 state inspected.

### Attacks attempted

False compression; contradictory counts; right-censoring; time/cost/yield comparability; denominator mismatch; unsupported causal claims; human-control conflation; exact-citation integrity; possible dependence on the later telemetry baseline.

### Findings by severity

**HIGH — Unsupported causal efficiency claim**

The final claim that “accumulated policy enabled” cheap discriminators and moved uncertainty later implies attribution not established by matched evidence. The repository supports a qualitative sequence, but not that accumulated policy caused it. Experiment 031 itself says there is no matched historical baseline and speed improvement cannot be quantified (`experiments/031/radar-compounding-test.md:411-418`). Experiment 032 likewise rejects a speed comparison because the runs were unmatched and lacked per-candidate timing (`experiments/032/actor-observable-decision-surface-discovery.md:276-287`).

**HIGH — Post-draft independence is unverifiable**

The Producer’s strongest conclusion closely tracks the later baseline’s formulation at `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:115-121`. The Producer says that document was consulted only post-draft, but no timestamped/hash-preserved pre-cross-check draft is supplied. This does not prove leakage, but hidden reliance cannot be falsified from the frozen artifact. The claimed post-draft ordering must therefore remain UNKNOWN.

**MEDIUM — “HIGH” yield is presented too uniformly**

Experiments 020, 031, and 032 contain recorded HIGH-yield labels (`docs/LEARNING_CHECKPOINT_020.md:158-164`; `experiments/031/radar-compounding-test.md:420-440`; `experiments/032/actor-observable-decision-surface-discovery.md:295-319`). These are locally recorded judgments, not a standardized comparable yield measure. Cross-experiment comparisons using the shared word “HIGH” would be false compression. The table should explicitly state this.

**MEDIUM — “Produced quickly” lacks a valid benchmark**

The claim that Experiments 025 and 034 produced resolutions “quickly” relies on approximate durations for heterogeneous workloads: approximately 30 minutes (`docs/LEARNING_CHECKPOINT_025.md:7-15`) and approximately 27 minutes (`experiments/034/superset-disposable-sequencing-resolution.md:277-285`). Without a matched baseline or defined threshold, only the durations—not “quickly”—are supported.

**MEDIUM — Exact citation requirement is not fully met**

The Experiment 025 citation uses the non-path `experiments/025/...brief.md`. This is not an exact, reconstructable citation. Several claims also cite broad ranges rather than the narrow lines establishing each value.

**LOW — Experiment 031 contradiction correctly surfaced but not resolved**

The record says 13 of 14 candidates were killed before deepening while also recording three deepened candidates (`experiments/031/radar-compounding-test.md:20`; `:424-438`). The Producer properly refuses to synthesize an exclusive shallow/deep funnel. Only formed/deepened/killed aggregate counts survive.

**LOW — Right-censoring and cost discipline survive attack**

Experiment 030 remains pending with exposure and effect UNKNOWN (`experiments/030/interaction-record.md:95-121,155-171`). Experiment 035 likewise ends at initialization with exposure/effect UNKNOWN (`experiments/035/superset-actor-facing-resolution-test.md:156-195`). The Producer does not convert either into failure or value evidence. It also correctly keeps compute/model cost UNKNOWN.

### False-PASS risks

- Treating qualitative bottleneck ordering as demonstrated causal policy improvement.
- Treating locally assigned HIGH-yield labels as comparable units.
- Treating approximate minutes as evidence of relative speed.
- Accepting an unverifiable “post-draft cross-check” declaration without a frozen pre-cross-check artifact.
- Passing checklist item 12 despite the abbreviated Experiment 025 path.

### Required corrections

1. Replace “accumulated policy enabled” with a non-causal formulation: the selected records document a qualitative sequence of changing bottlenecks.
2. Replace “produced quickly” with the recorded approximate durations and state that no comparative speed claim follows.
3. State explicitly that yield labels are experiment-local and not cross-experiment comparable.
4. Replace the abbreviated Experiment 025 citation with the exact path and supporting lines.
5. Mark the claimed pre-baseline independent draft ordering as unverifiable/UNKNOWN unless a prospectively frozen draft or hash exists.

### Surviving claims

- Recorded external spend is `$0.09` for Experiment 020 and `€0` for 021, 025, 026, and 030–035.
- The selected records show several bounded, low-external-spend discriminators.
- Experiment 031’s aggregate counts survive, but its shallow/deep funnel does not.
- Experiment 026 is acquisition/authorization-boundary evidence, not negative value evidence.
- Experiments 030 and 035 prove publication/delivery only; exposure, effect, and value remain UNKNOWN.
- Human-attention efficiency, ROI, time trends, homogeneous conversion rates, and commercial value are unsupported.

## Recommendation

**FAIL pending correction.** The numerical reconstruction is largely sound, but the frozen candidate fails strict acceptance because its strongest conclusion is causally overcompressed, “quickly” is unbenchmarked, one citation is not exact, and independent pre-cross-check reconstruction is not auditable.