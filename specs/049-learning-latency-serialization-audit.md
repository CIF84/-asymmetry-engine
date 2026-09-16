# Spec 049 — Learning Latency and Serialization Audit

## Status

READY FOR EXECUTION

## Type

Repository-only economic-operating audit. No external research, actor interaction, new opportunity discovery, software implementation, or canonical-policy modification.

## Baseline

Execute from synchronized `main` at or after:

`63fb5b2754dde356dc7526c51ebd72b80a667830`

Experiment 048 is closed at that baseline as `DELIVERY UNKNOWN`.

## Why this experiment exists

Asymmetry Engine exists to discover monetizable opportunities, experimentally learn which resolution mechanisms create value, test whether that value can be captured repeatably, and eventually compound validated mechanisms into low-maintenance assets.

Recent work suggests that internal research can complete in minutes while external observation, actor response, moderation, or platform state can consume days. The project may therefore have shifted bottlenecks from active research cost toward calendar latency.

That concern is not yet established. Experiments 031–034 were conducted while Experiments 030/035 were active, so the project may already have overlapped waiting with productive work more than the conversational narrative suggests.

This audit must determine whether external waiting actually created **idle critical-path serialization** rather than merely long experiment spans.

## Primary question

Has serialized external waiting become a material bottleneck to Asymmetry Engine's economically relevant learning throughput?

## Secondary questions

1. How much relevant calendar time is active work versus external or internal waiting?
2. Which waiting periods actually blocked economically useful work?
3. Which independent work already occurred during those waits?
4. How much historical calendar time could conservatively have been compressed through overlap?
5. Would concurrency have materially increased human attention, spend, coordination, or control burden?
6. Is the dominant problem experiment duration, portfolio scheduling, observation-window design, surface choice, or something else?
7. Does evidence justify a bounded prospective portfolio-throughput experiment?
8. Does evidence justify software/orchestration? Presumptive answer: no.

## Core distinction

Do not conflate:

```text
FASTER INDIVIDUAL EXPERIMENTS
```

with:

```text
FASTER PORTFOLIO LEARNING
```

An experiment can validly require several days while the Engine continues productive work elsewhere.

The concern is **idle critical-path serialization**, not elapsed time by itself.

## Evidence horizon

Primary reconstruction horizon: Experiments 030–048.

Use deeper detail for:

- 030;
- 031–035;
- 036–045 where relevant to work completed while external windows were open;
- 040–042 only for parallelism economics;
- 046–048.

Earlier experiments may be inspected only if needed to establish a comparison or missing operating pattern.

## Required repository sources

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

Use commit history/timestamps only where needed and where repository evidence makes them meaningful.

## Explicit prohibitions

Do NOT:

- inspect any live external platform;
- contact any actor;
- reopen Experiment 048;
- run fresh RADAR or create candidates;
- run a new multi-agent experiment;
- modify any existing experiment;
- modify README, ROADMAP, OPERATING_MODEL, ARCHITECTURE, frozen models, or checkpoints;
- modify source code, tests, schemas, or prior specs;
- implement a scheduler, orchestration, task queues, monitoring, dashboards, or experiment databases;
- infer missing historical timestamps as exact values;
- treat UNKNOWN compute cost as zero;
- treat every waiting period as avoidable serialization;
- assume all historical experiments could safely have run concurrently;
- optimize experiment count as a proxy for economic learning.

## Evidence discipline

For every material field classify as:

- `RECORDED`
- `DERIVED`
- `ESTIMATED`
- `UNKNOWN`

Where a numeric counterfactual depends on assumptions, state them explicitly and use ranges where appropriate. Do not reconstruct false precision.

## Timing concepts

### Active work time

Prospectively recorded human/model/executor work time where available. Preserve historical estimates as estimates.

### Calendar experiment span

Time from a supportable meaningful start to terminal decision-relevant evidence or valid closure.

### External waiting time

Elapsed period where next relevant evidence depended primarily on an external actor, platform, moderation state, scheduled observation window, market event, or other world process.

### Internal waiting time

Elapsed period caused by AE workflow, scheduling, authorization, handoff, environment, or tool availability.

### Learning latency (LL)

Where both boundaries are supportable:

```text
LL = calendar time from admission of decision-relevant uncertainty
     to terminal decision-changing evidence or valid closure
```

### Active-work ratio (AWR)

Where valid:

```text
AWR = active work time / calendar experiment span
```

Descriptive only; not a quality score.

### Serialization loss

Calendar delay attributable to sequencing independent useful work behind a waiting experiment when that work could plausibly have proceeded without contaminating either experiment.

Do not calculate serialization loss as waiting time alone.

## Experiment independence

Two work packages are plausibly independent when running one during the other's waiting period would not materially alter:

- natural baseline;
- treatment exposure;
- relevant actor behavior;
- evidence interpretation;
- control state;
- authorization requirements;
- shared scarce human attention beyond the declared budget;
- shared candidate state in a way that changes the hypothesis.

Do not assume independence because experiments have different numbers.

## Unit of analysis

Use both experiment-level and decision-chain views.

Important chains include:

```text
032 → 033 → 034 → 035
```

and

```text
046 → 047 → 048
```

Measure chain latency separately where supported. Do not double-count chain time in aggregate claims.

## Required reconstruction table

For each materially timing-relevant experiment or chain, reconstruct where possible:

| Field | Meaning |
|---|---|
| Experiment / chain | ID(s) |
| Question / uncertainty | Short description |
| Start timestamp | RECORDED / ESTIMATED / UNKNOWN |
| Terminal timestamp | RECORDED / ESTIMATED / UNKNOWN |
| Calendar span | Derived where valid |
| Active work | Recorded/estimated |
| External waiting | Recorded/derived/unknown |
| Internal waiting | Recorded/derived/unknown |
| Human attention | Where recorded |
| Spend | Where recorded |
| Terminal evidence | What changed the decision |
| Economic evidence class | rejection / resolution / actor effect / value / capture / etc. |
| Could independent work proceed while waiting? | YES / PARTIAL / NO / UNKNOWN |
| Did independent work actually proceed? | YES / PARTIAL / NO / UNKNOWN |
| Evidence class | Reconstruction quality |

Do not force irrelevant experiments into the table.

## Historical concurrency reconstruction

### Window A — Experiment 030

Determine:

- publication time;
- observation deadline;
- final observation time;
- useful AE work occurring during the wait;
- whether that work was independent;
- whether the Engine actually idled.

### Window B — Experiment 035

Determine the same and explicitly establish whether 030 and 035 overlapped.

### Window C — Experiment 048

Determine:

- initial execution attempt;
- second attempt;
- authenticated third submission;
- moderation waiting;
- final status-resolution check;
- useful AE work, if any, during those periods;
- whether the branch genuinely blocked fresh economic work.

## Serialization counterfactual

Construct a conservative counterfactual rather than an optimized fantasy schedule.

Question:

> If external waiting had been treated as non-blocking by default, what independent work already demonstrated by the historical record could plausibly have been moved into those waiting periods?

Use only work that actually occurred historically or a clearly bounded equivalent.

Produce:

### CF0 — Actual observed schedule

Best-supported historical sequence.

### CF1 — Conservative overlap

Move only clearly independent internal/repository work into externally blocked periods where it plausibly could have happened earlier.

### CF2 — Bounded portfolio policy

Assess the likely calendar effect of allowing a small number of independent experiments to remain simultaneously `ACTIVE / WAITING / READY`, subject to historical human-attention and authorization constraints.

CF2 may remain qualitative if timing evidence is insufficient.

## Falsification requirement

Actively try to falsify the serialization concern.

Search for evidence that:

- substantial work continued while 030 or 035 waited;
- Specs/Experiments 031–034 already demonstrate productive overlap;
- documentation, architecture, agentic, RADAR, or other decision-relevant work continued during external waits;
- perceived slowdown comes partly from following one conversational narrative rather than actual project inactivity;
- 048 is an exceptional platform failure rather than representative experiment latency.

If the Engine already overlaps waits effectively, say so.

## Throughput metrics

Do not use raw experiment count as the primary metric.

Evaluate where supportable:

- decision-changing evidence events per calendar day;
- high-information dispositions per calendar day;
- economic-learning events per human active minute;
- external-wait occupancy;
- idle-while-waiting time.

Do not formalize a synthetic composite score.

## Research-policy latency question

Audit whether the current question:

> Given the current belief state, what is the cheapest next observation capable of materially changing what we should do?

may need a future additional consideration for calendar latency and blocking behavior.

Possible future considerations include:

- information value;
- active cost;
- human attention;
- external latency;
- whether latency blocks other work;
- independence from currently waiting experiments.

Do not modify policy in Spec 049.

## Faster-experiment analysis

Without launching new work, classify historical discriminators where possible as:

- deterministic/publicly resolvable;
- immediate tool/computation;
- actor-held synchronous or near-synchronous;
- asynchronous actor response;
- scheduled observation window;
- platform/moderation dependent;
- market/event dependent.

Assess whether equivalent information could sometimes have come from a faster evidence class. Do not claim faster is better when discriminating power falls.

## Parallelism distinction

Explicitly compare:

```text
PARALLEL AGENTS ON ONE COHERENT ARTIFACT
→ semantic coupling + integration tax
→ 041/042 negative evidence
```

with:

```text
PARALLEL INDEPENDENT ECONOMIC EXPERIMENTS
→ external waits may overlap
→ little/no semantic integration dependency
→ not yet prospectively tested
```

Determine whether 042's economic-independence principle supports a portfolio test or warns against it. Do not reopen the multi-agent branch.

## Human-attention constraint

The desired state is not maximum simultaneous activity. It is:

```text
multiple independent external uncertainties progressing
while
human attention remains bounded
```

Audit whether concurrency would plausibly increase:

- authorization burden;
- context switching;
- review burden;
- exception handling;
- platform/account risk;
- cognitive load.

Preserve UNKNOWN costs.

## Control constraint

Parallel experiments must not weaken:

- authorization boundaries;
- platform compliance;
- natural baselines;
- treatment independence;
- actor privacy;
- observation-window integrity;
- epistemic challenge.

A portfolio policy may allow multiple waiting experiments without granting standing authorization for consequential actions.

## Prospective portfolio experiment gate

A next experiment testing a small independent portfolio is earned only if:

1. external waiting is a material component of calendar latency;
2. at least some waits plausibly could overlap independent useful work;
3. overlap would not obviously invalidate experiments;
4. human attention/cost/control burden appears bounded enough to test;
5. the hypothesis is decision-relevant to AE's economic objective.

It is not earned if:

- the Engine already overlaps waits sufficiently;
- waiting is not materially blocking learning;
- timing evidence is too weak;
- candidate independence cannot be established;
- human/control overhead likely dominates;
- perceived slowdown is mainly narrative rather than operational.

If earned, define only the smallest next question, e.g.:

> Can a bounded portfolio of 3–5 economically independent experiments increase decision-changing evidence per calendar day without materially worsening human attention, spend, controls, or evidence quality?

Do not design that experiment fully here.

## Software / automation gate

Explicitly classify whether implementation is earned.

Presumptive disposition: `DO NOT BUILD`.

Do not build:

- scheduler;
- orchestration server;
- queue;
- event bus;
- experiment database;
- dashboard;
- multi-agent operating system;
- automated authorization system;
- autonomous outreach;
- notification infrastructure.

A positive result earns at most a manual prospective portfolio experiment. Software is considered only after repeated portfolio experiments expose stable mechanical coordination pain and favorable economics.

## Adversarial checks

Before finalizing ask:

1. Are we mistaking elapsed observation windows for project inactivity?
2. Did 031–034 already run while 030/035 were waiting?
3. Are we selectively focusing on 048 because it was frustrating?
4. Would concurrent experiments compete for the same human attention?
5. Would concurrency change natural baselines or actor behavior?
6. Are timing records comparable enough for quantitative claims?
7. Are we optimizing experiment count instead of economic learning?
8. Could shorter experiments systematically produce weaker evidence?
9. Are platform failures representative or exceptional?
10. Are we using “portfolio” as an excuse to revive premature orchestration?
11. Does the counterfactual use only work that could genuinely have moved earlier?
12. Would the proposed next experiment change a real operating decision?

Correct unsupported conclusions before completion.

## Budget and stop conditions

Target active work: 15–30 minutes.

Hard ceiling: 45 active minutes.

External spend: €0.

Use prospective active-work timing from the start of the audit through artifact/integrity freeze.

Stop early when:

- the relevant timing windows are reconstructed to the highest evidence quality available;
- the serialization concern is either supported, materially weakened, or remains unresolvable;
- the portfolio-experiment gate has a decisive result;
- further archaeology is unlikely to change that result.

Do not fill the budget artificially.

## Verdicts

### A — MATERIAL SERIALIZATION BOTTLENECK; PORTFOLIO TEST EARNED

Evidence shows external waiting materially contributes to calendar learning latency, meaningful independent work could plausibly overlap those waits, and a bounded manual portfolio experiment is justified.

This verdict does not imply that historical work was fully serialized or that software is earned.

### B — MIXED; LATENCY MATTERS BUT HISTORICAL OVERLAP IS MATERIAL

External latency is meaningful, but the project already overlaps substantial useful work or historical evidence cannot support a large serialization-loss claim. A portfolio test may be earned only if the prospective question remains decision-relevant and bounded.

### C — SERIALIZATION CONCERN NOT SUPPORTED

Long experiment spans exist, but the Engine already overlaps waits sufficiently or little decision-relevant idle time is attributable to serialization. No portfolio experiment is earned.

### D — TIMING EVIDENCE INSUFFICIENT

Repository telemetry cannot distinguish external waiting, idle time, and actual serialization well enough to change operating policy.

### E — INVALID

Scope, isolation, timing, evidence, or repository-integrity requirements were violated.

## Required artifact

Create only:

`experiments/049/learning-latency-serialization-audit.md`

Do not modify any other file.

## Repository integrity

Before completion verify:

- only the Experiment 049 artifact changed;
- no prior experiment changed;
- no canonical document changed;
- no source/test/schema file changed;
- no external interaction occurred.

Run the existing test suite as an integrity check if available.

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
14