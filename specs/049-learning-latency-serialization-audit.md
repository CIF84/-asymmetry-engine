# Spec 049 — Learning Latency and Serialization Audit

## Status
READY FOR EXECUTION

## Type
Repository-only economic-operating audit. No external research, actor interaction, opportunity discovery, software implementation, or canonical-policy modification.

## Baseline
Execute from synchronized `main` at or after `63fb5b2754dde356dc7526c51ebd72b80a667830`. Experiment 048 is closed there as `DELIVERY UNKNOWN`.

## Primary question
Has serialized external waiting become a material bottleneck to Asymmetry Engine's economically relevant learning throughput?

## Core distinction
Do not conflate faster individual experiments with faster portfolio learning. Long elapsed experiments are only a throughput problem when external waiting creates idle critical-path serialization.

## Evidence horizon
Primary reconstruction: Experiments 030–048. Deepen 030–035, 040–042, and 046–048. Use 036–045 where needed to establish work completed during external waits.

At minimum inspect:
- `experiments/030/interaction-record.md`
- `experiments/031/radar-compounding-test.md`
- `experiments/032/actor-observable-decision-surface-discovery.md`
- `experiments/033/superset-semantic-hierarchy-dependency-check.md`
- `experiments/034/superset-disposable-sequencing-resolution.md`
- `experiments/035/superset-actor-facing-resolution-test.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- Experiments 036–045 as needed for overlap reconstruction
- `experiments/046/fresh-opportunity-discovery-aligned-interaction-policy.md`
- `experiments/047/realtime-migration-discriminator-feasibility-check.md`
- `experiments/048/bounded-realtime-migration-evidence-request.md`
- `docs/OPERATING_MODEL.md`
- `ROADMAP.md`

## Evidence discipline
Label material fields `RECORDED`, `DERIVED`, `ESTIMATED`, or `UNKNOWN`. Do not invent exact timestamps or false precision. Treat UNKNOWN compute cost as UNKNOWN.

## Timing concepts
- **Active work:** recorded or explicitly estimated execution work.
- **Calendar span:** supportable meaningful start to terminal evidence/closure.
- **External waiting:** next evidence depended primarily on actor/platform/moderation/observation/world process.
- **Internal waiting:** delay caused by AE workflow, authorization, handoff, environment, or tools.
- **Learning latency:** calendar time from admission of decision-relevant uncertainty to terminal decision-changing evidence/valid closure, only where both boundaries are supportable.
- **Active-work ratio:** active work / calendar span, descriptive only.
- **Serialization loss:** calendar delay caused by placing independent useful work behind a wait when that work could have proceeded without contamination. Waiting time alone is not serialization loss.

## Independence test
Two activities are plausibly independent only when overlap would not materially alter natural baseline, treatment exposure, relevant actor behavior, evidence interpretation, controls, authorization, scarce human attention, or shared candidate state.

## Required reconstruction
Use experiment-level and decision-chain views. Important chains include `032→033→034→035` and `046→047→048`.

For materially timing-relevant experiments/chains reconstruct where possible:
- question/uncertainty;
- start and terminal timestamps;
- calendar span;
- active work;
- external/internal waiting;
- human attention;
- spend;
- terminal evidence/economic evidence class;
- whether independent work could proceed while waiting;
- whether it actually did;
- evidence class.

## Required historical windows

### Window A — Experiment 030
Reconstruct publication, observation deadline, final observation, useful AE work during the wait, independence, and whether the Engine idled.

### Window B — Experiment 035
Do the same and explicitly determine whether 030 and 035 overlapped.

### Window C — Experiment 048
Reconstruct first and second authentication failures, authenticated third submission, moderation wait, final status-resolution check, useful AE work during those periods, and whether the branch blocked fresh economic work.

## Counterfactuals
Construct conservatively:
- **CF0 actual:** best-supported observed schedule.
- **CF1 conservative overlap:** move only clearly independent work that actually occurred historically into externally blocked windows where it could plausibly have happened earlier.
- **CF2 bounded portfolio policy:** assess allowing a small number of independent experiments to remain `ACTIVE / WAITING / READY` simultaneously under historical human-attention/control constraints. Qualitative is acceptable if timing evidence is insufficient.

Do not invent hypothetical experiments to inflate benefit.

## Falsification requirement
Actively test whether the concern is wrong. Specifically inspect whether 031–034 and other work already proceeded during 030/035 waits, whether 030 and 035 overlapped, whether perceived slowdown is partly narrative rather than operational, and whether 048 is exceptional rather than representative.

## Throughput assessment
Prefer where supportable:
- decision-changing evidence events per calendar day;
- high-information dispositions per calendar day;
- economic-learning events per human active minute;
- external-wait occupancy;
- idle-while-waiting time.

Do not create a synthetic score or optimize raw experiment count.

## Faster-evidence classification
Where useful classify historical discriminators as deterministic/publicly resolvable, immediate computation/tool, actor-held near-synchronous, asynchronous actor response, scheduled observation window, platform/moderation dependent, or market/event dependent. Faster evidence is not better if it loses discriminating power.

## Parallelism distinction
Preserve the distinction:

```text
parallel agents on one coherent artifact
→ semantic coupling/integration tax
→ 041/042 negative evidence

parallel independent economic experiments
→ external waits may overlap
→ low integration dependency in principle
→ not yet prospectively tested
```

Use 042's economic-independence principle; do not reopen the agentic branch.

## Human/control constraints
Assess authorization burden, context switching, review burden, exception handling, platform/account risk, cognitive load, natural-baseline integrity, actor privacy, observation integrity, and treatment independence. Preserve UNKNOWN costs.

## Prospective portfolio gate
A manual portfolio experiment is earned only if:
1. external waiting materially contributes to calendar latency;
2. some waits could plausibly overlap independent useful work;
3. overlap would not obviously invalidate experiments;
4. human attention/cost/control burden appears bounded enough to test;
5. the question matters to AE's economic objective.

It is not earned if existing overlap is already sufficient, timing evidence is too weak, independence is unclear, or likely overhead dominates.

If earned, define only the smallest next question, e.g. whether 3–5 economically independent experiments can increase decision-changing evidence per calendar day without materially worsening human attention, spend, controls, or evidence quality.

## Software gate
`DO NOT BUILD` is the presumptive disposition. No scheduler, orchestration server, queue, event bus, experiment database, dashboard, multi-agent OS, automated authorization, autonomous outreach, or notification infrastructure is earned by 049. A positive result earns at most a manual prospective portfolio experiment.

## Adversarial checks
Before finalizing ask:
1. Are elapsed observation windows being mistaken for inactivity?
2. Did 031–034 already run while 030/035 waited?
3. Are we overweighting frustrating 048?
4. Would concurrency compete for human attention?
5. Would it change baselines/actor behavior?
6. Are timing records comparable enough?
7. Are we optimizing count rather than economic learning?
8. Could shorter experiments yield weaker evidence?
9. Are platform failures exceptional?
10. Is “portfolio” disguising premature orchestration?
11. Does the counterfactual move only genuinely movable work?
12. Would the prospective test change an operating decision?

## Explicit prohibitions
Do NOT inspect live external platforms, contact actors, reopen 048, run RADAR, create candidates, run multi-agent work, modify prior experiments/canonical documents/source/tests/schemas/specs, or implement scheduling/orchestration/monitoring. Do not assume all waits are avoidable or all experiments independent.

## Budget and stop conditions
Target active work: 15–30 minutes. Hard ceiling: 45 active minutes. External spend: €0. Use prospective timing from audit start through artifact/integrity freeze.

Stop early when the relevant timing windows are reconstructed to the highest available quality, the serialization concern is supported/weakened/unresolvable, the portfolio gate is decisive, and further archaeology is unlikely to change the result.

## Verdicts

### A — MATERIAL SERIALIZATION BOTTLENECK; PORTFOLIO TEST EARNED
External waiting materially contributes to calendar learning latency, meaningful independent work could overlap it, and a bounded manual portfolio experiment is justified. This does not imply historical work was fully serialized or software is earned.

### B — MIXED; LATENCY MATTERS BUT HISTORICAL OVERLAP IS MATERIAL
External latency matters, but substantial useful overlap already occurred or evidence cannot support a large serialization-loss claim. A portfolio test may still be earned only if the prospective question remains bounded and decision-relevant.

### C — SERIALIZATION CONCERN NOT SUPPORTED
Long spans exist but waits are already overlapped sufficiently or little decision-relevant idle time is attributable to serialization. No portfolio experiment earned.

### D — TIMING EVIDENCE INSUFFICIENT
Telemetry cannot distinguish external waiting, idle time, and actual serialization well enough to change operating policy.

### E — INVALID
Scope, isolation, timing, evidence, or repository-integrity requirements violated.

## Required artifact
Create only `experiments/049/learning-latency-serialization-audit.md`.

## Repository integrity
Verify only the 049 artifact changed, no prior/canonical/source/test/schema file changed, and no external interaction occurred. Run the existing test suite if available.

## Required completion report
Return exactly these 32 sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Evidence horizon and reconstruction quality
7. Timing-relevant experiment table
8. Decision-chain latency findings
9. Window A — Experiment 030 reconstruction
10. Window B — Experiment 035 reconstruction
11. 030/035 overlap finding
12. Window C — Experiment 048 reconstruction
13. Active-work versus calendar-time finding
14. External-wait finding
15. Internal-wait finding
16. Idle-while-waiting finding
17. Serialization-loss finding
18. CF0 — actual schedule
19. CF1 — conservative-overlap counterfactual
20. CF2 — bounded-portfolio counterfactual
21. Falsification result
22. Throughput-metric findings
23. Faster-evidence-class findings
24. Research-policy latency finding
25. Parallelism comparison with 040–042
26. Human-attention and coordination finding
27. Control/independence finding
28. Prospective portfolio-experiment gate
29. Software/automation disposition
30. What the audit establishes
31. What remains unproven
32. Exactly one recommended next action

Also append, after section 32 and without creating additional numbered sections:
- Artifact path
- Integrity/test result
- Commit SHA

Do not push.