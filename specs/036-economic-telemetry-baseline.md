# Spec 036 — Economic Telemetry Baseline

## Status

ATLAS / operational measurement experiment.

This is **not** a new opportunity-discovery run. It must not inspect the live response state of Experiments 030 or 035, contact actors, generate fresh opportunity candidates, or modify the frozen Opportunity Model.

---

## Context

Experiments 031–035 suggest that the Engine may be improving in a way that candidate count alone cannot measure.

The observed sequence is approximately:

```text
031
broad discovery → cheap rejection set
actor/effect experimentability weak
      ↓
032
actor + intervention + effect topology selected deliberately
bottleneck moves to residual resolution gap
      ↓
033
bounded discriminator resolves dependency uncertainty
      ↓
034
disposable decision-ready resolution produced
      ↓
035
resolution enters a real decision surface
```

The Engine has repeatedly claimed that a useful compounding criterion is not simply more opportunities, but cheaper/faster production of discriminating economic evidence.

However, historical telemetry was not collected consistently enough to assume that claim can already be measured quantitatively.

This experiment therefore asks whether a defensible baseline can be reconstructed without manufacturing precision.

---

## Primary question

> **Can the repository's historical evidence through Experiment 035 support a defensible baseline for whether the Engine is becoming cheaper or faster at producing discriminating economic evidence?**

---

## Secondary questions

1. Which historical experiments contain reliable active-time, monetary-spend, candidate-flow, interaction, and evidence-yield telemetry?
2. Which fields are missing, inconsistent, estimated, or incomparable?
3. Can any directional compounding claim be supported from the available evidence?
4. What is the minimum telemetry future experiments should record prospectively?
5. What should explicitly **not** be measured or scored yet?

---

## Scope

Use repository evidence from Experiments / Specs / checkpoints 001–035 as needed.

Prioritize actual result artifacts and checkpoint documents over recollection.

The most telemetry-rich recent sequence 031–035 should receive the deepest treatment. Earlier experiments should be reconstructed only to the level supported by preserved evidence.

Do not spend disproportionate time recovering weak historical detail.

---

## Isolation requirements

Experiments 030 and 035 are currently in live observation windows.

Do not inspect:

- current Reddit response/reaction state for 030;
- current GitHub response/reaction/state changes attributable to 035 beyond the already frozen publication initialization artifact;
- any actor profile or adjacent activity intended to infer exposure.

The existing persisted 030/035 artifacts may be read only for telemetry already frozen before this run.

Do not update their measurement states.

---

## Evidence discipline

Every reconstructed telemetry field must be classified as one of:

- **RECORDED** — explicitly preserved in an experiment/result artifact;
- **DERIVED** — mechanically calculable from recorded facts;
- **ESTIMATED** — explicitly described historically as approximate;
- **UNKNOWN** — not defensibly reconstructable.

Never convert UNKNOWN into zero.

Never convert a target time budget into actual time.

Never infer active time from commit timestamps or wall-clock elapsed time unless an artifact explicitly defines that method.

Never invent tool/compute cost from current pricing.

---

## Core telemetry dimensions

For each experiment where evidence exists, attempt to reconstruct:

| Dimension | Meaning |
|---|---|
| Experiment | ID |
| Phase | OBSERVE / RADAR / FORGE / INTERACT / CONTROL / ATLAS / other |
| Primary uncertainty | Main question entering the experiment |
| Active time | Actual recorded/estimated active minutes |
| Monetary spend | Incremental external spend |
| Raw signals | If applicable |
| Candidates formed | If applicable |
| Candidates deepened | If applicable |
| Candidates killed | If applicable |
| Candidates advanced | If applicable |
| External interactions | Count if applicable |
| Human interventions | If recorded |
| Control escalations | If recorded |
| Evidence yield | Existing LOW/MEDIUM/HIGH classification if explicitly recorded |
| Dominant uncertainty after | What became the next bottleneck |
| Policy/model change | Whether the result changed research policy or opportunity model |
| Evidence quality | RECORDED / DERIVED / ESTIMATED / UNKNOWN by field |

Do not force non-applicable experiments into RADAR candidate metrics.

---

## Reconstruction tiers

Use three tiers to prevent archival archaeology from dominating the experiment.

### Tier 1 — recent telemetry-rich sequence

Experiments **031–035**.

Reconstruct as fully as the repository permits.

### Tier 2 — economically informative predecessors

Experiments **013–030**, especially 014, 020, 024–030.

Recover only telemetry that is explicit or cheaply obtainable from existing artifacts/checkpoints.

### Tier 3 — foundational source/architecture experiments

Experiments **001–012**.

Summarize only where reliable operational telemetry already exists. Otherwise mark historical telemetry insufficient.

The purpose is a baseline, not perfect bookkeeping reconstruction.

---

## Compounding hypotheses to test

Evaluate the following separately.

### C1 — Time efficiency

Later experiments may require less active time to reach a discriminating stop/advance decision.

Do not claim support unless comparable actual-time evidence exists.

### C2 — Monetary efficiency

The Engine may increasingly reach useful evidence at near-zero incremental external spend.

Distinguish genuine cost reduction from simply selecting experiments that do not require paid data.

### C3 — Falsification efficiency

Learned gates may kill weak candidates earlier and with less unnecessary deepening.

Look for preserved candidate-flow and terminal-gate evidence.

### C4 — Bottleneck migration

Research-policy learning may move dominant failure modes later in the opportunity lifecycle.

This can be supported qualitatively even when precise time telemetry is incomplete, but the evidence chain must be explicit.

### C5 — Resolution efficiency

Once a candidate survives RADAR, the Engine may reduce a bounded uncertainty into a defensible disposable resolution cheaply.

Use 033–034 as the primary evidence pair.

### C6 — Interaction efficiency

The Engine may be improving at getting a resolution into a legitimate, observable real decision context.

035 publication proves delivery, not effect. Do not inspect or infer its live response state.

### C7 — Human-attention efficiency

The Engine may be reducing mechanical human involvement while preserving governance/authorization.

Support only from explicitly recorded intervention/authorization telemetry.

### C8 — Economic compounding

The Engine may be improving at producing **economic evidence**, not merely epistemic rejection.

This is the strongest claim and should receive the highest burden of proof.

A chain ending at delivery into a decision surface is not yet proof of value creation, WTP, transaction, or repeatability.

---

## Unit-of-progress model

Do not create a synthetic numeric score.

Use this conceptual transformation only:

```text
SCARCE RESOURCES
(time + money + compute/tools + human attention)
        ↓
ASYMMETRY ENGINE
        ↓
DISCRIMINATING ECONOMIC EVIDENCE
```

The eventual optimization objective may resemble:

> economic evidence gain per unit of scarce resource

but this experiment must determine whether the numerator and denominator are currently measurable before attempting a metric.

---

## Required comparisons

At minimum, compare:

### 031 → 032

Did the actor/effect-observability policy change alter candidate quality or merely reduce candidate count?

### 032 → 033

Did the bottleneck move from intervention topology to residual-resolution uncertainty?

### 033 → 034

How much recorded resource was required to move from bounded uncertainty to decision-ready resolution?

### 034 → 035 initialization

How much recorded resource was required to move from resolution to verified real-world delivery under controls?

### Earlier history → 031–035

Can any defensible directional comparison be made, or is historical telemetry too inconsistent?

---

## Required artifact

Create:

`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`

The document must contain:

1. purpose and scope;
2. reconstruction method;
3. evidence-quality rules;
4. historical telemetry coverage map;
5. experiment-level telemetry table;
6. focused 031–035 funnel/resource reconstruction;
7. compounding hypothesis assessment C1–C8;
8. strongest supported compounding claim;
9. strongest unsupported/overclaimed claim;
10. bottleneck-migration analysis;
11. data-quality limitations;
12. minimum prospective telemetry standard;
13. metrics explicitly deferred;
14. whether implementation/automation is earned;
15. exactly one recommended next action.

---

## Minimum prospective telemetry standard

The experiment should propose the smallest future logging standard justified by observed gaps.

Consider whether every future experiment should preserve at least:

```text
experiment ID
phase
primary uncertainty before
actual active minutes
incremental external spend
human attention/interventions
control escalations
input count where meaningful
candidate count where meaningful
terminal decision / verdict
primary uncertainty after
evidence yield
external interaction count
policy/model change yes/no + description
```

Do not automatically adopt this list. Challenge each field for usefulness and collection burden.

Prefer Markdown recording over a database or telemetry system unless repeated evidence clearly earns implementation.

---

## Metrics explicitly prohibited in this experiment

Do not manufacture:

- a single Engine efficiency score;
- ROI percentage;
- hourly economic value;
- probability of opportunity success;
- expected revenue;
- opportunity conversion rate across incomparable experiments;
- statistical significance from the small heterogeneous sample;
- retrospective compute/token costs not explicitly recorded;
- productivity claims based on commit frequency;
- commercial compounding claims from interaction delivery alone.

---

## Verdicts

### A — DEFENSIBLE BASELINE

Historical evidence supports a useful baseline with clear data-quality boundaries and at least one meaningful directional compounding conclusion.

### B — PARTIAL BASELINE

Recent experiments support useful telemetry, but historical inconsistency prevents broader compounding conclusions.

### C — TELEMETRY INSUFFICIENT

The evidence is too incomplete/incomparable for a meaningful baseline; the useful result is a prospective logging standard.

### D — INVALID

The run violates isolation, manufactures unsupported precision, or otherwise cannot be interpreted.

---

## Stop rules

Stop when:

- Tier 1 is reconstructed;
- enough Tier 2/Tier 3 evidence has been sampled to determine historical coverage quality;
- additional archival work is unlikely to change the baseline verdict;
- minimum prospective telemetry can be specified;
- no new economic conclusion would be changed by more historical extraction.

Do not fill a time budget artificially.

---

## Resource budget

Target active time: **30–45 minutes**.

Hard ceiling: **60 minutes**.

Incremental spend: **€0**.

No external interaction.

No software implementation.

---

## Success condition

Success does not require proving compounding.

Success means producing a defensible answer to:

> **What can we actually measure about the Engine's economic learning efficiency today, what can we only say directionally, and what must we start recording prospectively before stronger claims become legitimate?**

---

## Required completion report

Return exactly:

1. Verdict
2. Repository baseline
3. Scope inspected
4. Isolation confirmation
5. Reconstruction method
6. Historical telemetry coverage
7. Tier 1 telemetry summary
8. Tier 2 telemetry summary
9. Tier 3 telemetry summary
10. 031→032 comparison
11. 032→033 comparison
12. 033→034 comparison
13. 034→035 initialization comparison
14. C1 time efficiency
15. C2 monetary efficiency
16. C3 falsification efficiency
17. C4 bottleneck migration
18. C5 resolution efficiency
19. C6 interaction efficiency
20. C7 human-attention efficiency
21. C8 economic compounding
22. Strongest supported claim
23. Strongest unsupported claim
24. Minimum prospective telemetry standard
25. Metrics deferred
26. Implementation earned: yes/no
27. Artifact path
28. Active time / spend
29. Commit SHA
30. Exactly one recommended next action
