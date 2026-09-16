# Spec 049 — Learning Latency and Serialization Audit

## Status

READY FOR EXECUTION

## Type

Repository-only economic-operating audit. No external research, no actor interaction, no new opportunity discovery, no software implementation, and no canonical-policy modification.

## Baseline

Execute from synchronized `main` at or after:

`63fb5b2754dde356dc7526c51ebd72b80a667830`

Experiment 048 is closed at that baseline as `DELIVERY UNKNOWN`.

## Why this experiment exists

Asymmetry Engine exists to discover monetizable opportunities, experimentally learn which resolution mechanisms create value, test whether that value can be captured repeatably, and eventually compound validated mechanisms into low-maintenance assets.

Recent experiments demonstrate that internal research and discrimination can be fast while external experiment latency can consume days.

Examples include:

- Experiment 030: one public interaction followed by a 72-hour observation window, ending measurement-limited because exposure was not established;
- Experiment 035: one public interaction followed by a 72-hour observation window, producing a material public decision-state refinement;
- Experiments 046–048: fresh RADAR and discriminator work completed in minutes, followed by multiple days of authentication, moderation, and platform-state uncertainty, ultimately ending with delivery unknown.

The project may therefore have shifted bottlenecks.

Historically the Engine optimized strongly for:

```text
research cost ↓
false positives ↓
failed construction ↓
human attention ↓
unsupported claims ↓
```

Those remain important.

But the economic objective also depends on:

```text
CALENDAR TIME TO ECONOMICALLY RELEVANT EVIDENCE
```

A multi-day external wait is not necessarily a problem if other independent experiments continue during the wait. It becomes a serious throughput problem when the Engine implicitly serializes around asynchronous external uncertainty.

This specification tests whether that concern is supported by repository evidence before changing research policy or building orchestration.

## Primary question

Has serialized external waiting become a material bottleneck to Asymmetry Engine's economically relevant learning throughput?

## Secondary questions

1. How much experiment calendar time is active work versus external waiting?
2. Which waiting periods actually blocked other economically useful work, and which merely coexisted with parallel internal work?
3. How much historical calendar time could plausibly have been compressed by overlapping independent experiment waits?
4. Would concurrency have required materially more human attention, spend, coordination, or control complexity?
5. Are recent experiments already partially parallel in practice, making the perceived serialization problem smaller than it appears?
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

## Candidate metric vocabulary

This audit may use the following concepts, but must not pretend unavailable telemetry is precise.

### Active work time

Prospectively recorded human/model/executor work time where available.

If historical time is estimated, preserve the original evidence class.

### Calendar experiment span

Time from the experiment's meaningful start to its terminal decision-relevant evidence or valid closure.

Do not invent start/end timestamps when the repository does not support them.

### External waiting time

Elapsed period during which the next relevant evidence depended primarily on an external actor, platform, moderation state, scheduled observation window, market event, or other world process rather than active AE work.

### Internal waiting time

Elapsed period caused by AE's own workflow, scheduling, authorization, handoff, environment, or tool availability.

Keep this separate from external waiting where evidence permits.

### Learning latency (LL)

For a bounded experiment or chain:

```text
LL = calendar time from admission of the decision-relevant uncertainty
     to terminal decision-changing evidence or valid closure
```

Use only when both boundaries are supportable.

### Active-work ratio (AWR)

Where both values are supportable:

```text
AWR = active work time / calendar experiment span
```

This is descriptive, not a quality score.

### Serialization loss

The calendar delay attributable to sequencing independent work behind a waiting experiment when that work could plausibly have proceeded without contaminating the waiting experiment.

This is the central construct.

Do not calculate serialization loss merely as `waiting time`.

### Experiment independence

Two work packages are plausibly independent when running one during the other's waiting period would not materially alter:

- natural baseline;
- treatment exposure;
- actor behavior relevant to the other experiment;
- evidence interpretation;
- control state;
- authorization requirements;
- shared scarce human attention beyond the declared budget;
- shared candidate state in a way that changes the hypothesis.

Do not assume independence because experiments have different numbers.

## Evidence horizon

Primary reconstruction horizon:

- Experiments 030–048.

Use deeper detail for:

- 030;
- 031–035;
- 036–045 where relevant to whether useful internal work occurred while external windows were open;
- 046–048.

Earlier experiments may be inspected only if needed to establish a comparison or missing operating pattern.

Do not perform broad historical archaeology when recent evidence is sufficient.

## Required repository sources

At minimum inspect:

- `experiments/030/interaction-record.md`
- `experiments/031/radar-compounding-test.md`
- `experiments/032/actor-observable-decision-surface-discovery.md`
- `experiments/033/superset-semantic-hierarchy-dependency-check.md`
- `experiments/034/superset-disposable-sequencing-resolution.md`
- `experiments/035/superset-actor-facing-resolution-test.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- Experiments 036–045 as needed to reconstruct work completed while 030/035 were waiting
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
- run fresh RADAR;
- create new candidates;
- run a new multi-agent experiment;
- modify any existing experiment;
- modify README, ROADMAP, OPERATING_MODEL, ARCHITECTURE, frozen models, or checkpoints;
- implement a scheduler;
- implement orchestration;
- implement task queues;
- implement monitoring;
- create dashboards;
- create an experiment database;
- infer missing historical timestamps as exact values;
- treat UNKNOWN compute cost as zero;
- treat every waiting period as avoidable serialization;
- assume all historical experiments could safely have run concurrently;
- optimize experiment count as a proxy for economic learning.

## Evidence discipline

For each material field classify as:

- `RECORDED`
- `DERIVED`
- `ESTIMATED`
- `UNKNOWN`

Where a numeric counterfactual depends on assumptions, state the assumptions explicitly and use ranges when appropriate.

Do not reconstruct false precision.

## Unit of analysis

Use both:

### Experiment-level view

Useful for active time, elapsed time, waiting, and terminal evidence.

### Decision-chain view

Some economically meaningful questions span multiple experiments.

Examples:

```text
032 → 033 → 034 → 035
```

and

```text
046 → 047 → 048
```

Measure chain-level latency separately from experiment-level latency where supported.

Do not double-count chain time when aggregating.

## Required reconstruction table

For each material experiment or chain, reconstruct where possible:

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
| Could useful independent work proceed while waiting? | YES / PARTIAL / NO / UNKNOWN |
| Did useful independent work actually proceed? | YES / PARTIAL / NO / UNKNOWN |
| Evidence class | quality of reconstruction |

Do not force every experiment into the table if it has no meaningful timing relevance.

## Historical concurrency reconstruction

Reconstruct the actual timeline around the clearest asynchronous windows.

At minimum analyze:

### Window A — Experiment 030

Determine:

- publication time;
- observation deadline;
- final observation time;
- what AE work occurred between publication and final observation;
- whether that work was independent of 030;
- whether the Engine actually idled or already overlapped work.

### Window B — Experiment 035

Determine the same.

Pay special attention to whether 030 and 035 themselves overlapped.

### Window C — Experiment 048

Determine:

- initial execution attempt;
- second attempt;
- authenticated third submission;
- moderation waiting;
- final status-resolution check;
- useful AE work, if any, completed during those periods;
- whether the branch itself blocked fresh RADAR or other economically relevant work.

## Serialization counterfactual

Construct a conservative counterfactual, not an optimized fantasy schedule.

Question:

> If external waiting had been treated as non-blocking by default, what independent work already demonstrated by the historical record could plausibly have been moved into those waiting periods?

Use only work that actually occurred historically or a clearly bounded equivalent.

Do not invent hypothetical experiments to inflate the benefit.

Produce at least:

### CF0 — Actual observed schedule

Best-supported historical sequence.

### CF1 — Conservative overlap

Move only clearly independent internal/repository work into externally blocked windows.

### CF2 — Bounded portfolio policy

Estimate the calendar effect of allowing a small number of independent experiments to remain simultaneously ACTIVE / WAITING / READY, subject to the historical human-attention and authorization constraints.

CF2 may remain qualitative if timing evidence is insufficient.

## Important challenge: was the Engine actually serialized?

The audit must actively try to falsify the user's concern.

Search for evidence that:

- substantial work continued while 030 or 035 waited;
- Specs 031–034 were already examples of productive overlap;
- documentation, architecture, agentic, or RADAR work continued during external waits;
- the perceived slowdown comes mainly from following one conversational narrative rather than actual project inactivity;
- 048 is an exceptional platform failure rather than representative experiment latency.

If evidence shows the Engine already overlaps waiting periods effectively, say so.

Do not manufacture a bottleneck because the hypothesis is attractive.

## Throughput metrics

Do not use raw experiment count as the primary metric.

Evaluate candidate portfolio metrics such as:

### Decision-changing evidence events per calendar day

Count only terminal evidence that materially changes a candidate, policy, resolution, or economic belief.

### High-information dispositions per calendar day

Useful for RADAR-heavy periods.

### Economic-learning events per human active minute

Where human attention is available.

### External-wait occupancy

How many independent experiments are waiting on external evidence at once.

### Idle-while-waiting time

Calendar periods where external waiting was active and no other decision-relevant AE work occurred, where reconstructable.

Do not formalize a synthetic composite score.

## Experiment-selection latency question

Audit whether the current research-policy question:

> Given the current belief state, what is the cheapest next observation capable of materially changing what we should do?

needs a future additional consideration for **calendar latency / blocking behavior**.

Do not edit the Operating Model.

Possible conclusion might be that candidate experiments should consider:

- information value;
- active cost;
- human attention;
- external latency;
- whether latency blocks other work;
- independence from currently waiting experiments.

But promote nothing automatically.

## Faster-experiment design analysis

Without launching new work, classify historical discriminators by expected response speed:

- deterministic/publicly resolvable;
- immediate tool/computation;
- actor-held synchronous or near-synchronous;
- asynchronous actor response;
- scheduled observation window;
- platform/moderation dependent;
- market/event dependent.

Assess whether equivalent information could sometimes have been obtained from a faster evidence class.

Do not claim faster is better when it reduces discriminating power.

## Parallelism distinction

Explicitly compare this hypothesis with Experiments 040–042.

Preserve:

```text
PARALLEL AGENTS ON ONE COHERENT ARTIFACT
→ semantic coupling + integration tax
→ failed once in 041/042
```

versus:

```text
PARALLEL INDEPENDENT ECONOMIC EXPERIMENTS
→ external waits may overlap
→ little/no semantic integration dependency
→ not yet prospectively tested
```

Determine whether 042's economic-independence principle supports a portfolio experiment or warns against it.

Do not reopen the multi-agent branch.

## Human-attention constraint

The long-term goal is not maximum simultaneous activity.

The desired state is closer to:

```text
many independent external uncertainties progressing
while
human attention remains bounded
```

Audit whether historical evidence suggests concurrency would have increased:

- authorization burden;
- context switching;
- review burden;
- exception handling;
- platform/account risk;
- cognitive load.

If these costs are UNKNOWN, preserve them.

## Control constraint

Parallel experiments must not weaken:

- authorization boundaries;
- platform compliance;
- natural baselines;
- independence of treatments;
- actor privacy;
- observation-window integrity;
- epistemic challenge.

A portfolio policy may allow multiple waiting experiments without granting standing authorization for new consequential actions.

## Prospective portfolio experiment gate

At completion determine whether evidence earns a next experiment testing a small independent portfolio.

### Earned only if

1. external waiting is a material component of calendar latency;
2. at least some waiting periods plausibly could have overlapped independent useful work;
3. overlap would not obviously invalidate experiments;
4. human attention/cost/control burden appears bounded enough to test;
5. the hypothesis is decision-relevant to AE's economic objective.

### Not earned if

- the Engine already overlapped work sufficiently;
- waiting is not materially blocking learning;
- historical timing evidence is too weak;
- candidate independence cannot be established;
- human/control overhead likely dominates;
- the perceived slowdown is mainly narrative rather than operational.

## If a portfolio experiment is earned

Do not design it fully in Spec 049.

Define only the smallest next question, for example:

> Can a bounded portfolio of 3–5 economically independent experiments increase decision-changing evidence per calendar day without materially worsening human attention, spend, controls, or evidence quality?

Leave exact design to a later specification.

## Software / automation gate

Explicitly classify whether any implementation is earned.

Presumptive disposition:

`DO NOT BUILD`.

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

A positive latency result earns at most a **manual prospective portfolio experiment**.

Software is considered only after repeated portfolio experiments demonstrate stable mechanical coordination pain and favorable economics.

## Adversarial checks

Before finalizing ask:

1. Are we mistaking elapsed observation windows for project inactivity?
2. Did 031–034 already run while 030/035 were waiting?
3. Are we selectively focusing on 048 because it was frustrating?
4. Would concurrent experiments have competed for the same human attention?
5. Would concurrency have changed natural baselines or actor behavior?
6. Are timing records comparable enough for quantitative claims?
7. Are we optimizing experiment count instead of economic learning?
8. Could shorter experiments systematically produce weaker evidence?
9. Are platform failures representative or exceptional?
10. Are we using “portfolio” as an excuse to revive premature orchestration?
11. Does the counterfactual use only work that could genuinely have been moved earlier?
12. Would the proposed next experiment change a real operating decision?

Correct unsupported conclusions before completion.

## Budget

Target active work: 15–30 minutes.

Hard ceiling: 45 active minutes.

External spend: €0.

Use prospective active-work