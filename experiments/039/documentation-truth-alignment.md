# Experiment 039 — Documentation Truth Alignment

**Baseline commit:** `7d58199d2f6b3c80b4015e27ed8bb51bd3949c37`  
**Verdict:** **A — DOCUMENTATION ALIGNED**  
**Prospective timer start:** `2026-09-03T03:02:07Z`  
**Prospective timer end:** `2026-09-03T03:10:10Z`  
**Active time:** `8 minutes 3 seconds` (483 seconds), derived from prospectively captured UTC epoch timestamps through final documentation review  
**Incremental spend:** `€0`

## 1. Scope and isolation

Reviewed and changed only:

- `README.md`;
- `ARCHITECTURE.md`;
- `ROADMAP.md`;
- this required result artifact.

Current code and accepted repository evidence through Experiment 038 were used as the truth hierarchy. No source code, tests, schema, adapters, specifications, frozen Opportunity Model, Economic Telemetry Baseline, or Experiment 030/035 artifact was modified. No live 030/035 state was inspected, no actor was contacted, and no opportunity research was performed.

## 2. Assessment before alignment

### README

The entry point still described the original generic signal → decision demand → asymmetry detection → registry → monitoring/scoring → commercial experiment pipeline as the current system. It presented aggressive discovery automation, automatic ranking, and cash-flowing assets too strongly relative to implemented and empirically validated capabilities. It did preserve important purpose: implementation is becoming less scarce, problem selection matters, software is not the default answer, public evidence can compound learning, and commercialization remains the objective.

### ARCHITECTURE

The document was predominantly an aspirational component inventory. It described unimplemented decision extraction, generic detection, registry, score snapshots, monitoring, experiment/outcome/asset persistence, scheduling, and CLI commands as the intended architecture. Its valid principles—modular monolith, SQLite, source independence, immutable evidence, provenance, deterministic computation, low complexity, and evidence pressure—remained useful. Its persistence section did not describe the accepted revision-aware semantics from Experiment 038.

### ROADMAP

The roadmap imposed a sequential build program with count thresholds, ranked-output milestones, generic registry/scoring/monitoring phases, and fixed day targets. That sequence no longer matched empirical development, which has selected work by dominant uncertainty, fatal gates, accessible decision surfaces, exact-resolution competition, controls, and small earned adaptations.

## 3. Stale assumptions found and resolution

| Stale assumption | Resolution |
|---|---|
| One fixed automated pipeline is the Engine | Replaced with an empirical operating loop explicitly distinguished from software and allowed to branch, skip, or stop |
| Generic registry is a required near-term system | Listed as unimplemented and unearned; retained only as historical context |
| Additive scoring is the primary selector | Replaced with fatal-gate-first policy and cheapest discriminating observation; no new score introduced |
| Automated extraction/clustering/ranking is required | Reframed as absent by design while semantic policy remains unstable |
| Discovery should be automated aggressively | Replaced with evidence-earned automation of validated repeated mechanics |
| Signal/count milestones demonstrate progress | Removed; progress is decision-changing evidence, including cheap justified rejection |
| Calendar phases govern development | Removed; future work is evidence-gated |
| Publication implies interaction success | Explicitly separated delivery, exposure, engagement, effect, value, and capture |
| Revenue assets are current capability | Preserved as long-term direction while revenue and repeatability remain unproven |
| Observation persistence stores one permanent first-seen row | Replaced with Experiment 038 logical-item/capture/latest-view semantics |

## 4. Current truths preserved

All three documents now preserve these accepted truths:

- the current project definition is economically consequential decisions under resolvable uncertainty, cheap decision-effect testing, and learning toward repeatable value;
- commercialization and value capture remain the objective but are not validated;
- the learned OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN loop is research practice, not runtime architecture;
- the opportunity anatomy contains necessary conditions that cannot safely be collapsed into an additive score;
- current software is a small collector/normalizer/SQLite/revision-aware persistence/CN75 reasoning/CLI/test substrate;
- exact-resolution comparison, research policy, decision compression, interaction, measurement, and most controls remain manual;
- consequential action requires separate explicit authorization;
- operational telemetry is manual and the historical baseline is partial;
- automation must be earned by repetition, mechanical reuse, improved economics, and small reversible scope;
- ATLAS → RADAR → FORGE → PORTFOLIO → FREEDOM remains a strategic economic direction rather than a deployment diagram.

## 5. Historical material removed or reframed

Large obsolete component catalogs, hypothetical schemas, commands, lifecycle states, fixed count targets, numbered build phases, and calendar promises were removed from current guidance. They were not copied into an archival appendix because Git already preserves the exact history.

Each document now contains a short historical note stating that the project began with a generic extraction/detection/registry/scoring pipeline and that Experiments 013–038 changed the governing model. Valid early principles were retained without preserving obsolete implementation detail.

## 6. Cross-document contradictions

### Discovered before editing

- README and ARCHITECTURE described a generic automated system that current code does not implement.
- ROADMAP treated that aspirational system as mandatory sequential work, while later operating documents select experiments by uncertainty.
- Scoring appeared as current architecture despite repeated fatal-gate evidence and no scoring code.
- Automation language implied stable discovery mechanics despite continued semantic/manual research-policy evolution.
- Commercial assets appeared closer to current capability than allowed evidence supports.
- None of the top-level documents clearly integrated revision-aware capture semantics from 038.

### Remaining after editing

No material contradiction remains across project definition, operating loop, current implementation, scoring, automation, manual judgment, authorization, validation status, or long-term objective. Minor differences are purposeful: README is the concise entry point, ARCHITECTURE is the implementation boundary, and ROADMAP is the evidence-gated decision policy.

## 7. Stale-term search

The edited files were searched case-insensitively for:

```text
Automate discovery aggressively
Asymmetry Registry
ScoreSnapshot
TOP 10
1,000 observations
100 plausible decision signals
20 evidence-backed candidate asymmetries
persistent asymmetry registry
Monitoring + Scoring
detect run
asymmetries list
```

Result: no matches. Related concepts such as generic registry and additive scoring remain only in explicit historical, unimplemented, superseded, or unearned language.

## 8. Adversarial review

1. The learned loop is not presented as rigid software; every document states that it may branch, skip, or stop.
2. Manual empirical practice is explicitly separated from implemented modules.
3. No response or value outcome is attributed to Experiments 030 or 035; publication initialization is limited to delivery.
4. Commercialization, value capture, portfolio, and FREEDOM remain present as unvalidated long-term objectives.
5. Additive scoring and aggressive automation are explicitly superseded.
6. No replacement infrastructure, phase name, ontology, service, or scoring model was invented.
7. A new contributor can distinguish current code, current operating practice, unproven hypotheses, and long-term direction from the three top-level documents.

## 9. Validation

Test command after documentation changes:

```text
.venv/bin/pytest -q
```

Result: **89 passed in 0.25 seconds**, with one sandbox-specific `PytestCacheWarning` because pytest could not update `.pytest_cache`; no test or tracked file was affected.

Repository diff/status check: passed. Only `README.md`, `ARCHITECTURE.md`, `ROADMAP.md`, and this required result artifact are changed. Source code, tests, specs, frozen documents, and live-experiment artifacts are unchanged. `git diff --check` passes.

## 10. Exactly one recommended next action

Use the aligned README, Architecture, and Roadmap as the present-tense documentation baseline during the next independent review, correcting future drift only when new accepted evidence changes current truth.
