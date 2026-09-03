# Economic Telemetry Baseline — Experiments 001–035

**Experiment:** 036  
**Phase:** ATLAS / operational measurement  
**Baseline repository state:** `66c8b2356c9b4a96061513421325cda5fdc455f3`  
**Verdict:** **B — PARTIAL BASELINE**

## 1. Purpose and scope

This document asks what the repository can defensibly establish about whether the Asymmetry Engine is becoming cheaper or faster at producing discriminating economic evidence. It reconstructs operational telemetry through Experiment 035, treats Experiments 031–035 most deeply, samples economically informative predecessors, and avoids disproportionate archaeology where the record is weak.

The result is a partial baseline. Recent work supports a useful resource-and-funnel reconstruction and a qualitative bottleneck-migration claim. It does not support a comparable historical time series or a claim that delivered resolutions have created economic value.

This run used repository evidence only. It did not inspect the current response, reaction, profile, or state-change evidence for Experiments 030 or 035; did not contact any actor; and did not modify `docs/OPPORTUNITY_MODEL_001_035.md`.

## 2. Reconstruction method

Evidence priority was:

1. persisted experiment/result artifacts;
2. experiment-specific learning checkpoints;
3. cross-experiment operational and learning checkpoints;
4. specifications only for experimental intent, never as proof of actual resource use or outcome.

Tier 1 reconstructs Experiments 031–035 field by field. Tier 2 samples Experiments 013–030 where explicit operational facts were cheap to recover, with emphasis on 014, 020, and 024–030. Tier 3 uses the aggregate 001–019 checkpoint because no reliable experiment-level operational series exists for 001–012. Extraction stopped once further archival work was unlikely to change the verdict.

Counts were retained in their original experimental context. A RADAR candidate count is not treated as comparable to a FORGE resolution, an INTERACT publication, or an ATLAS audit.

## 3. Evidence-quality rules

- **RECORDED:** explicitly preserved as a definite fact in an experiment or result artifact.
- **DERIVED:** mechanically calculated from recorded facts; the source inputs remain visible.
- **ESTIMATED:** historically described as approximate, including values stated as “approximately,” “roughly,” or “under.”
- **UNKNOWN:** not defensibly reconstructable from the preserved record.
- **N/A:** the dimension genuinely does not apply to that experiment type; it is not a substitute for missing data.

UNKNOWN is not zero. A target budget is not actual time. Commit timestamps are not active-time telemetry. Current prices are not used to reconstruct historical tool cost. No synthetic score, conversion rate, ROI, or statistical inference is calculated across heterogeneous experiments.

## 4. Historical telemetry coverage map

| Tier | Experiments | Coverage | Defensible use |
|---|---:|---|---|
| 1 | 031–035 | Strongest preserved coverage. Time and spend are present throughout, although 033–035 time is approximate; RADAR funnel counts exist for 031–032; interaction initialization telemetry exists for 035. | Reconstruct the recent funnel, resource use, policy changes, and bottleneck movement. |
| 2 | 013–030 | Uneven. Explicit resource facts exist for 020, 021, 025, 026, and 030; useful outcome/funnel facts exist for 024 and 027–029, but several lack time, spend, human-attention, control, or yield fields. | Establish selected precedents and show why a historical trend is not comparable. |
| 3 | 001–012 | Experiment-level operational telemetry is insufficient. The 001–019 checkpoint provides qualitative learning yield, not a comparable resource series. | Establish the absence of a quantitative baseline and the point at which prospective logging was first requested. |

Coverage is therefore adequate for a **recent operational baseline**, not for a longitudinal efficiency curve from Experiment 001.

## 5. Experiment-level telemetry table

Quality labels apply to each populated field. When a field is absent it is shown as UNKNOWN rather than inferred.

| Experiment | Phase / entering uncertainty | Active time | Spend | Flow / interaction | Human / controls | Evidence yield | Dominant uncertainty after / policy change |
|---|---|---|---|---|---|---|---|
| 001–012 | Foundational observation, reasoning, architecture; experiment-level questions vary | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Major model changes are documented only in aggregate (RECORDED); operational efficiency is UNKNOWN. |
| 013–019 | Commercial pressure tests and recovery/experimentability work | UNKNOWN | UNKNOWN | 014 attempted a paid-pilot path but did not obtain valid market exposure (RECORDED) | UNKNOWN | “High evidence yield despite high activity” for 001–019 aggregate (RECORDED), not experiment-level | Exposure-channel validity and earlier exact-resolution search became important (RECORDED). |
| 020 | RADAR / whether EV compatibility lacked an adequate exact resolution | ~50–60 min (ESTIMATED) | $0.09 (RECORDED) | ~20 searches and ~15 major source inspections (ESTIMATED); no outreach (RECORDED) | UNKNOWN | High/useful falsification in checkpoint narrative; no explicit LOW/MEDIUM/HIGH field, therefore UNKNOWN | Candidate parked; exact-resolution search moved earlier (RECORDED). |
| 021 | RADAR / whether the revised policy could reject a fresh set cheaply | ~20 min (ESTIMATED) | €0 (RECORDED) | 11 formed, 2 deepened, 11 killed, 0 advanced (RECORDED); 9 shallow kills (DERIVED from recorded counts) | UNKNOWN | UNKNOWN | Evaluation strengthened; candidate-generation quality became bottleneck (RECORDED). |
| 024 | RADAR / whether a material live counter-tariff resolution gap existed | UNKNOWN | UNKNOWN | 20 benchmark cases (RECORDED); one candidate advanced to FORGE (RECORDED) | UNKNOWN | UNKNOWN | Material functional gap demonstrated; first empirical RADAR→FORGE handoff (RECORDED). |
| 025 | FORGE / whether the bounded gap could become a decision-ready resolution | ~30 min (ESTIMATED) | €0 (RECORDED) | 12-line brief; all 12 passed validation (RECORDED); external interaction N/A | UNKNOWN | UNKNOWN | Decision-ready resolution produced; actor exposure became next gate (RECORDED). |
| 026 | INTERACT acquisition / whether a qualifying actor interaction could be obtained | <10 min (ESTIMATED) | €0 (RECORDED) | No qualifying interaction obtained; no outreach sent (RECORDED) | Authorization boundary caused a valid stop (RECORDED); intervention count UNKNOWN | No explicit label; no behavioral evidence (RECORDED) | Distribution feasibility separated from value failure (RECORDED). |
| 027 | RADAR / whether the tariff resolution had an accessible decision surface | UNKNOWN | UNKNOWN | One carried opportunity parked; no actor interaction (RECORDED) | UNKNOWN | UNKNOWN | Intervention experimentability became an explicit selection gate (RECORDED). |
| 028 | RADAR / whether actor-first surface discovery could yield a bounded candidate | UNKNOWN | UNKNOWN | 4 surface families, 10 formed, 3 deepened, 7 shallow-killed, 1 advanced (RECORDED) | No outreach/posting (RECORDED); intervention/control counts UNKNOWN | UNKNOWN | Same-surface CRM candidate advanced; actor-first topology adopted (RECORDED). |
| 029 | FORGE / whether the CRM case could become a decision-ready aid | UNKNOWN | UNKNOWN | One carried candidate; one decision-ready artifact (RECORDED); interaction N/A | UNKNOWN | UNKNOWN | Decision space reduced; real actor interaction became next gate (RECORDED). |
| 030 | INTERACT / whether a compact CRM resolution affects a live decision | ~20 min preparation + <1 min posting (ESTIMATED) | €0 (RECORDED) | 1 public reply; delivery verified at initialization (RECORDED) | One human-verification/sign-in handoff (RECORDED); exact intervention count UNKNOWN | LOW at initialization (RECORDED) | Publication feasible; exposure and effect remain UNKNOWN in the frozen initialization record (RECORDED). |
| 031 | RADAR / whether learned policy could cheaply generate and discriminate fresh signal-native hypotheses | 9 min (RECORDED) | €0 (RECORDED) | 7 families, 37 raw signals, 14 formed, 3 deepened, 14 killed, 0 advanced (RECORDED) | 0 human interventions; 0 external-action escalations; 7 conditional/review/block classifications (RECORDED) | HIGH (RECORDED) | No survivor; exact resolution, recoverability, and actor/effect observability reordered as gates (RECORDED). |
| 032 | RADAR / whether actor-observable origins improve intervention/effect topology | 26 min (RECORDED) | €0 (RECORDED) | 7 families, 34 raw signals, 10 formed, 3 deepened, 9 killed, 1 bounded survivor (RECORDED) | 0 human interventions; 2 BLOCK + 2 REVIEW controls; no interaction (RECORDED) | HIGH (RECORDED) | Actor-access kills fell to zero; exact-resolution/dependency uncertainty became bottleneck (RECORDED). |
| 033 | RADAR discriminator / which Superset hierarchy dependency direction was supported | ~16 min (ESTIMATED) | €0 (RECORDED) | One carried candidate; S2 favored; advanced to disposable resolution (RECORDED) | UNKNOWN | UNKNOWN | Direction concrete; migration/source sequencing boundary unresolved (RECORDED). |
| 034 | FORGE / whether that boundary could become a decision-ready resolution | ~27 min (ESTIMATED) | €0 (RECORDED) | One carried candidate; decision-ready PASS; advanced to controlled interaction (RECORDED) | UNKNOWN | UNKNOWN | Actor decision effect and actual implementation seam cost remained unproven (RECORDED). |
| 035 | INTERACT / whether the resolution could enter the live public decision under controls | ~18 min (ESTIMATED) | €0 (RECORDED) | 1 authorized comment, 0 follow-ups, delivery verified (RECORDED) | 1 authorization event; 0 control escalations (RECORDED) | LOW at initialization (RECORDED) | Publication succeeded; exposure, comprehension, decision effect, and downstream value remain UNKNOWN/UNTESTED in the frozen initialization record (RECORDED). |

Two preservation caveats matter. First, Experiment 031's narrative says thirteen candidates were killed before deepening, while its table records three deepened among fourteen formed; the explicit funnel counts above are retained, but the inconsistency prevents a more precise shallow-kill metric. Second, no current-response evidence for 030 or 035 was consulted; their rows end at persisted initialization.

## 6. Focused 031–035 funnel and resource reconstruction

```text
031 RADAR
37 raw → 14 formed → 3 deepened → 0 advanced
9 recorded min | €0 | HIGH yield
        ↓ policy: privilege actor/effect observability
032 RADAR
34 raw → 10 formed → 3 deepened → 1 bounded survivor
26 recorded min | €0 | HIGH yield
        ↓ bottleneck: exact dependency/residual resolution
033 RADAR discriminator
1 carried → S2 favored → 1 advanced
~16 estimated min | €0 | yield UNKNOWN
        ↓ bottleneck: minimal sequencing/migration boundary
034 FORGE
1 carried → decision-ready PASS → 1 interaction-ready
~27 estimated min | €0 | yield UNKNOWN
        ↓ bottleneck: actor exposure/effect
035 INTERACT initialization
1 authorized publication → delivery verified → effect UNKNOWN
~18 estimated min | €0 | LOW initialization yield
```

The mixed-quality time sum for 031–035 is approximately 96 minutes (DERIVED from 9 + 26 recorded minutes and ~16 + ~27 + ~18 estimated minutes). It is descriptive only: these experiments perform different jobs, three inputs are approximate, and the sum is not an efficiency metric.

The central observable change is funnel topology, not raw volume. Experiment 032 formed fewer candidates than 031 and took longer, but produced one candidate whose actor, intervention, and effect topology survived with one bounded uncertainty. Experiments 033–035 then moved that single candidate through discrimination, disposable resolution, and verified delivery. Delivery is the end of the supported chain; actor effect is not yet evidence.

## 7. Compounding hypothesis assessment C1–C8

| Hypothesis | Assessment | Repository-grounded reason |
|---|---|---|
| **C1 — Time efficiency** | **Not supported** | Comparable actual-time evidence does not exist across phases or history. The two recorded Tier 1 RADAR runs are 9 and 26 minutes, so later is not simply faster; their scopes and outputs differ. Approximate FORGE/INTERACT times cannot establish a trend. |
| **C2 — Monetary efficiency** | **Directionally supported, narrowly** | 020 used $0.09; 021, 025, 026, and 030–035 report zero incremental spend. This demonstrates repeated near-zero-spend learning, but not cost reduction: experiment selection changed and most earlier spend is UNKNOWN. |
| **C3 — Falsification efficiency** | **Directionally supported** | 020 falsified a plausible opportunity before construction; 021 killed 11 in ~20 minutes; 031 killed 14 in 9 recorded minutes; 032 preserved selective deepening while improving actor/effect topology. There is no matched per-candidate baseline, so the magnitude is unmeasured. |
| **C4 — Bottleneck migration** | **Supported qualitatively** | The explicit chain moves from exact-resolution competition, to distribution/access, to actor/effect-aware candidate topology, to dependency sequencing, to resolution boundary, and finally to actor effect after verified delivery. |
| **C5 — Resolution efficiency** | **Directionally supported from one bounded chain** | 033 and 034 used ~43 minutes combined (DERIVED from ESTIMATED inputs) and €0 to move one public dependency uncertainty into a decision-ready disposable resolution. One case does not establish a trend or market value. |
| **C6 — Interaction efficiency** | **Operationally partial; effect unproven** | 035 used ~18 minutes, €0, one authorization event, one comment, and no follow-up to achieve verified delivery. 030 also preserved a low-cost verified publication. Neither initialization record proves exposure, comprehension, decision effect, or value. |
| **C7 — Human-attention efficiency** | **Insufficient** | 031–032 record zero human interventions, and 035 records one authorization event; 030 records a verification/sign-in handoff. The field is absent or semantically inconsistent elsewhere, and minutes of human attention are not preserved. |
| **C8 — Economic compounding** | **Not supported** | The chain has produced discriminating epistemic evidence and verified delivery, but no preserved proof yet of value creation, willingness to pay, transaction, repeatability, or recurring cash flow. |

## 8. Strongest supported compounding claim

The strongest defensible claim is:

> Accumulated research policy is producing a clearer sequence of cheap, controlled discriminators that rejects weak candidates and moves the surviving uncertainty later—from resolution competition and access toward bounded resolution and observable actor effect—usually at zero incremental external spend.

This is a qualitative operating-policy claim. It is supported by the 020→021 falsification precedent, the 026→028 actor-surface correction, and the 031→035 bottleneck chain. It is not a claim that total time is declining or economic value is compounding.

## 9. Strongest unsupported or overclaimed claim

The strongest unsupported claim would be:

> The Engine is becoming quantitatively faster and more economically productive, and its delivered interventions create repeatable commercial value.

Historical active time is sparse and incomparable; human attention and control effort are inconsistently defined; evidence-yield labels are missing in many runs; and the preserved chain ends at verified delivery. There is no defensible ROI, revenue, willingness-to-pay, transaction, repeatability, or causal value evidence through the allowed baseline.

## 10. Bottleneck-migration analysis

The repository supports the following explicit migration:

```text
013–020: plausible opportunity can still have an adequate exact resolution
    ↓
021–025: early competition checks improve; a real gap reaches cheap resolution
    ↓
026–027: actor acquisition / accessible decision surface becomes binding
    ↓
028–032: actor-first discovery improves topology; exact residual gap binds again
    ↓
033: public dependency direction resolved; minimal sequencing boundary remains
    ↓
034: decision-ready boundary resolved; actor effect becomes binding
    ↓
035 initialization: controlled delivery verified; exposure/effect/value remain unknown
```

This supports learning because earlier failure modes informed later gates, and the next uncertainty became more downstream and behaviorally relevant. It does not guarantee monotonic progress: exact-resolution competition reappeared after actor-first selection, and a later bottleneck is not automatically more valuable. The useful signal is that the project identified and tested the currently binding uncertainty without prematurely building software or conflating access failure with value failure.

## 11. Data-quality limitations

- Actual active minutes are rare. Most preserved durations are explicitly approximate, and elapsed time is not interchangeable with active effort.
- Phase and task scope vary substantially; a broad RADAR scan, one dependency discriminator, a FORGE artifact, and a publication are not comparable units.
- Monetary spend is better preserved recently, but zero-spend selection is not proof of falling cost. Historical spend remains largely UNKNOWN.
- Candidate terminology changes across experiments. Raw signals, hypotheses, benchmark cases, carried candidates, resolution outputs, and interactions must not share one denominator.
- Evidence-yield LOW/MEDIUM/HIGH is explicit for 030–032 and 035 but absent in many other artifacts.
- Human intervention, human authorization, browser handoff, independent challenge, and control escalation are not recorded with a stable schema.
- Tool and compute use is not consistently recorded; retrospective token or current-price estimates are prohibited.
- Experiment 031 contains a shallow-kill narrative/count ambiguity, so only its unambiguous aggregate counts are used.
- Experiment 030 and 035 evidence is intentionally right-censored at initialization. UNKNOWN effect cannot be interpreted as zero response or failure.
- One successful sequential case cannot establish statistical significance, general conversion, or commercial repeatability.

## 12. Minimum prospective telemetry standard

Every future experiment should add one compact Markdown block to its result artifact:

```text
Experiment ID / phase
Primary uncertainty before
Active minutes: actual or ESTIMATED, with timing method
Incremental external spend: amount + currency
Human attention: event count + minutes where observable + role
Control escalations: count + disposition
Inputs: count and unit, only where meaningful
Candidate flow: formed / deepened / killed / advanced, only for candidate experiments
External interactions: count by bounded action type
Terminal decision / verdict / execution validity
Primary uncertainty after
Evidence yield: LOW / MEDIUM / HIGH + one-sentence basis
Policy/model change: yes/no + one sentence
```

Each required resource field must be completed even when its value is `UNKNOWN`; `N/A` requires a reason. Actual minutes should come from a simple start/stop active-work log, excluding approval waits and observation windows, while any reconstruction remains labeled ESTIMATED. Counts must name their unit. Interaction artifacts must keep delivery, exposure, engagement, decision effect, and value separate.

The fields earn their burden because each closes an observed gap: time and spend provide the denominator; uncertainty, verdict, and yield define the evidence output; flow counts show falsification; human/control fields expose scarce governance cost; interaction counts preserve causal stage; and policy change records whether learning altered future operation.

## 13. Metrics explicitly deferred

The baseline does not calculate or authorize:

- a single Engine efficiency or productivity score;
- ROI, hourly economic value, expected revenue, or opportunity-success probability;
- conversion rates across heterogeneous phases or experiments;
- statistical significance from the small non-comparable sample;
- retrospective compute, token, or tool costs not recorded at execution;
- productivity inferred from commits or elapsed calendar time;
- an assumed monetary value for rejection, learning, delivery, or human attention;
- commercial compounding from publication or delivery alone;
- a response-rate metric that treats UNKNOWN exposure as failure.

These remain deferred until consistent prospective denominators exist and the evidence chain reaches actor effect and economic value often enough to justify comparison.

## 14. Whether implementation or automation is earned

**No.** A telemetry database, dashboard, synthetic scoring system, or automated instrumentation layer is not earned. The sample is small, the schema has not yet been used consistently, and several terms still need operational stabilization. A compact Markdown block in each experiment artifact is sufficient, auditable, cheap, and easy to revise. Implementation should be reconsidered only after repeated prospective use reveals a stable schema and a real retrieval or aggregation burden.

## 15. Exactly one recommended next action

Apply the minimum prospective telemetry block above to the next authorized experiment at initialization and completion, recording actual active minutes with a simple active-work timer; use that first fully prospective record as the start of the comparable baseline rather than attempting further retrospective reconstruction.
