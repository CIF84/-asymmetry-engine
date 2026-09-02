# Spec 032 — Actor-Observable Decision Surface Discovery

## Status

RADAR discovery-policy experiment.

Research-only. Do not build software, contact actors, post publicly, run outreach, test pricing, accept payment, or modify Spec 030.

---

## Context

Spec 031 produced a valid high-information rejection set: 37 raw signals, 14 signal-native candidates, 3 bounded deep dives, 0 survivors, €0 spend, and early kills driven by learned RADAR policy.

The accepted interpretation is narrower than generic "RADAR compounding":

> **Accumulated learning is improving falsification and discrimination efficiency.**

However, Spec 031 exposed a more specific bottleneck.

RADAR can now generate many decision-shaped candidates and kill weak ones cheaply, but serious candidates often fail because:

- the actor is only an inferred actor type rather than an individually observable decision-maker;
- the surface is publicly accessible but the actor is not legitimately reachable there;
- a communication path exists but the economic/value effect cannot be observed;
- decisive state is private and cannot be elicited through a bounded interaction;
- the resolution could be delivered but no downstream decision signal is visible.

This means the phrase **accessible decision surface** is too broad to describe intervention experimentability.

A review page can be accessible while its reviewer is unreachable.
A calculator can be accessible while user behavior is invisible.
A procurement notice can be accessible while the supplier making the decision is unobservable.

The new research prior is therefore stricter:

```text
OBSERVABLE ACTOR
      ↕
LIVE DECISION
      ↕
LEGITIMATE INTERVENTION PATH
      ↕
OBSERVABLE EFFECT
```

All four must coexist before expensive opportunity research is justified.

---

## Primary question

> **Can RADAR improve survivor yield by starting only from public or legitimately accessible surfaces where a real decision-maker self-identifies, a consequential decision remains open, a bounded intervention could legitimately reach that actor, and some effect of the resolution could later be observed?**

This experiment tests whether **actor-observable decision topology** is a more productive candidate-generation origin than accessible-surface discovery alone.

It does not test whether any resulting candidate has market scale, willingness to pay, repeatability, or durable product potential.

---

## Core distinction

Do not conflate these properties:

```text
SURFACE ACCESS
≠ ACTOR ACCESS
≠ INTERVENTION PERMISSION
≠ ACTOR EXPOSURE
≠ EFFECT OBSERVABILITY
```

For this experiment:

- **surface access** means the signal can legitimately be observed;
- **actor access** means a specific actor is present and identifiable within the decision context;
- **intervention path** means a bounded future response/resolution could legitimately be delivered through that context or a tightly adjacent one;
- **actor exposure** means there is a plausible way to know or infer that the resolution reached the actor;
- **effect observability** means some response, reframing, next action, choice, challenge, or other decision-relevant behavior could plausibly be observed after exposure.

A candidate must not advance merely because the surface is public.

---

## Actor-observable topology

A qualifying discovery origin should provide evidence of most or all of:

1. **Specific actor** — a real individual, team, maintainer, buyer, seller, applicant, operator, or organization is visibly making the decision.
2. **Live decision** — the economically relevant choice remains changeable.
3. **Decision context** — enough state is exposed to understand what is being decided and why.
4. **Decision-relevant uncertainty** — missing information materially affects the choice.
5. **Economic consequence** — money, recurring cost, labor, margin, switching cost, risk, asset value, opportunity cost, or another meaningful economic outcome is at stake.
6. **Recoverable information** — enough decisive information is public, derivable, or can plausibly be elicited through a bounded actor interaction.
7. **Legitimate intervention path** — a future disposable resolution could be delivered without scraping private identities, evading platform controls, unsolicited private outreach, or bespoke relationship-building.
8. **Exposure observability** — the experiment could plausibly distinguish delivered/seen/engaged states better than pure guesswork.
9. **Effect observability** — a future experiment could plausibly observe a decision-relevant response or action.
10. **Residual resolution gap** — no adequate existing resolver already performs the bounded job at the relevant decision moment.

The first research objective is to find this topology, not to invent a product.

---

## Strong discovery origins

Prefer surfaces where actors voluntarily expose active decision state, such as:

- public Q&A threads with a concrete unresolved choice;
- GitHub issues/discussions where maintainers or users are deciding whether/how to act;
- public professional/community posts asking for decision help;
- marketplace listings/questions where the actual buyer or seller is identifiable and the decision remains open;
- public request/proposal/discussion systems where the decision owner participates visibly;
- product/community support surfaces where a user is considering switching, buying, upgrading, configuring, or abandoning before commitment;
- public founder/operator discussions exposing an unresolved allocation, pricing, build, buy, or operational decision;
- other surfaces discovered during research that satisfy the topology.

The list is illustrative, not exhaustive.

---

## Weak or disallowed discovery origins

Do not count as qualifying candidates:

- anonymous traffic or aggregate search demand with no actor;
- generic market categories;
- review pages where the reviewer cannot legitimately be engaged in the live decision context;
- completed post-purchase complaints with no remaining decision;
- calculators where users and downstream actions are invisible;
- procurement notices where no decision-making supplier/actor is exposed;
- eligibility portals where applicant state is private and no actor is visible;
- news stories describing a class of affected actors;
- inferred personas constructed from market data;
- actors whose only reachable route is unsolicited private outreach;
- cases where intervention requires obtaining private contact details outside the observed surface;
- cases where a reply can be posted but no actor-specific exposure or response could plausibly be distinguished;
- previously killed Spec 031 candidates unless a genuinely new signal independently changes the topology.

---

## Signal-before-hypothesis rule

Preserve this order for every counted candidate:

```text
RAW ACTOR SIGNAL
→ SPECIFIC ACTOR
→ LIVE DECISION
→ EXPOSED STATE
→ UNCERTAINTY
→ ECONOMIC CONSEQUENCE
→ RECOVERABLE INFORMATION
→ POSSIBLE RESOLUTION
→ INTERVENTION PATH
→ OBSERVABLE EFFECT
```

Do not begin with a business idea, market, or known pain point and search backward for a person who appears to fit it.

If the hypothesis existed before the actor signal, do not count it.

---

## Candidate-generation target

Generate **8–12 qualifying actor-observable candidate hypotheses**.

This target is intentionally lower than Spec 031 because actor topology is stricter.

Do not weaken the actor requirement to hit the quota.

If fewer than 8 qualifying candidates can be found within the time budget, stop and report that as evidence about candidate scarcity.

Record non-qualifying signals separately when they reveal why apparently attractive surfaces fail the topology.

---

## Surface diversity

Inspect at least **4 materially different surface families**.

At least **2 families must not be Reddit or generic forums**.

Do not use generic web search as a surface family. Search may locate primary actor surfaces, but the candidate must originate in the underlying actor-visible surface.

Avoid allowing one unusually productive platform to dominate the entire candidate set before at least four families have been tested.

---

## Actor test

Before forming a candidate ask:

> **Who exactly is making the decision, and what evidence shows that this actor is still deciding?**

Classify actor observability:

- **DIRECT** — a specific actor explicitly states the live decision;
- **STRONG** — a specific actor exposes behavior/state from which the live decision is strongly evidenced;
- **INFERRED** — only an actor type or hypothetical decision-maker can be inferred.

INFERRED candidates do not qualify for the required candidate set.

---

## Intervention-path test

Before deepening ask:

> **If we produced a disposable resolution, where exactly could it be placed so this specific actor could legitimately encounter it?**

Classify:

- **SAME** — resolution can be delivered within the original actor-visible decision surface;
- **ADJACENT** — actor has explicitly provided or invited a tightly adjacent legitimate route;
- **SEPARATE** — intervention requires a materially different channel, private identity resolution, cold outreach, gatekeeper access, or bespoke relationship-building.

SEPARATE normally kills the candidate for this experiment.

Do not interpret public identity as permission for private contact.

---

## Exposure-observability test

Ask:

> **After delivery, what evidence could distinguish actor exposure from mere technical publication?**

Possible evidence may include:

- direct reply;
- reaction;
- actor follow-up;
- actor-requested clarification;
- thread continuation;
- acknowledged receipt;
- visible issue/discussion state change;
- actor-supplied additional facts;
- another platform-native exposure indicator that is legitimate and sufficiently informative.

A public comment permalink proves delivery, not exposure.

If exposure cannot plausibly be distinguished, classify **EXPOSURE WEAK**.

---

## Effect-observability test

Ask:

> **If the resolution helps, what actor behavior could we observe that is closer to decision value than attention?**

Strong examples:

- option set changes;
- shortlist changes;
- actor reframes the decision;
- a decisive unknown becomes explicit;
- actor supplies new evidence needed to decide;
- next action changes;
- actor performs a recommended test;
- actor abandons a weak option;
- actor challenges a premise in a way that improves the resolution;
- actor reports that the resolution changed the decision.

Weak examples:

- views;
- likes from unknown people;
- generic thanks;
- page traffic;
- impressions;
- clicks with no relation to decision state.

Classify effect observability:

- **HIGH** — decision-relevant response/action is plausibly visible;
- **MEDIUM** — actor engagement is visible but decision effect would require one bounded follow-up or actor report;
- **LOW** — only attention/publication metrics are likely visible.

LOW normally kills the candidate.

---

## Recoverability test

Classify decisive information:

- **HIGH** — public, authoritative, derivable, or already actor-supplied;
- **MEDIUM** — mostly recoverable, with one bounded actor-supplied variable/test needed;
- **LOW** — decisive state depends on inaccessible private records, confidential systems, physical inspection, professional judgment, or post-decision evidence.

MEDIUM is acceptable when the actor-visible surface permits the missing variable to be requested legitimately and cheaply.

LOW normally kills.

This is an important difference from Spec 031: private state is not automatically fatal if the actor can naturally provide the bounded missing fact within the same decision interaction.

---

## Exact-resolution competition

Only after the candidate passes actor/intervention/effect topology and cheap consequence/recoverability gates, search for functional existing resolution using:

```text
ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING
```

Kill when an adequate accessible resolver already performs the bounded job at the relevant decision moment.

Do not confuse existing information with existing decision resolution.

Do not deepen merely because existing tools are imperfect; identify the specific residual gap.

---

## Economic-consequence test

The decision must plausibly affect meaningful economic value, including:

- money spent/lost;
- recurring cost;
- labor or implementation effort;
- switching/migration cost;
- margin;
- asset value;
- contractual lock-in;
- failure/rework risk;
- opportunity cost;
- material time-to-decision;
- other defensible economic consequence.

Do not require a precise monetary estimate at discovery stage.

Do require enough evidence that the consequence is more than curiosity or convenience.

---

## Deepening limit

Deepen at most **3 candidates**.

A candidate deserves deepening only if it has already survived:

```text
SPECIFIC ACTOR
→ LIVE DECISION
→ ECONOMIC CONSEQUENCE
→ LEGITIMATE INTERVENTION PATH
→ PLAUSIBLE EXPOSURE OBSERVABILITY
→ MEDIUM/HIGH EFFECT OBSERVABILITY
→ MEDIUM/HIGH RECOVERABILITY
→ INITIAL EXACT-RESOLUTION CHECK
```

For each deepened candidate identify:

- strongest evidence for the opportunity;
- strongest evidence against it;
- exact existing resolution;
- decisive remaining uncertainty;
- cheapest stop observation;
- cheapest progression observation;
- plausible disposable resolution;
- exact future intervention location;
- exposure evidence that could be observed;
- decision-effect evidence that could be observed;
- relevant controls;
- whether a real interaction experiment is justified.

Do not interact with the actor in Spec 032.

---

## Control feasibility

For serious candidates perform a lightweight manual check of relevant controls:

- platform rules and norms;
- public versus private communication;
- actor invitation/context;
- privacy and identity handling;
- source/data legitimacy;
- professional/regulatory sensitivity;
- commercial-activity implications;
- authorization required for any future consequential external action;
- resource/time/spend exposure.

Classify future interaction feasibility:

- **PASS**;
- **CONDITIONAL**;
- **REVIEW REQUIRED**;
- **BLOCK**.

Spec 032 itself authorizes no interaction.

---

## Survivor definition

A survivor must have concrete evidence for all of:

```text
REAL OBSERVABLE ACTOR
× LIVE ECONOMIC DECISION
× MEANINGFUL UNCERTAINTY
× RECOVERABLE DECISIVE INFORMATION
× INADEQUATE EXISTING RESOLUTION
× CONSTRUCTIBLE BOUNDED RESOLUTION
× LEGITIMATE ACTOR INTERVENTION PATH
× PLAUSIBLE EXPOSURE OBSERVABILITY
× PLAUSIBLE DECISION-EFFECT OBSERVABILITY
× ACCEPTABLE CONTROL FEASIBILITY
```

This is a conjunctive gate, not a numeric score.

One fatal zero can dominate the opportunity.

---

## At most one survivor

Recommend at most **one** candidate for a future FORGE resolution/intervention sequence.

If multiple candidates survive, choose the one whose next economic uncertainty can be reduced most cheaply and decisively.

Do not advance a candidate merely because it resembles the CRM case.

---

## Comparison with Spec 031

At completion, explicitly compare the candidate topology with Spec 031.

Ask:

1. Did starting from observable actors reduce the number of actor-access kills?
2. Did it improve exposure observability?
3. Did it improve decision-effect observability?
4. Did it reduce candidate volume materially?
5. Did stricter topology improve survivor quality?
6. Which new bottleneck became dominant?

Do not make speed claims unless telemetry supports them.

---

## Operational telemetry

Record:

| Metric | Value |
|---|---|
| Active research time | |
| Paid spend | |
| Surface families inspected | |
| Raw actor signals inspected | |
| DIRECT actor signals | |
| STRONG actor signals | |
| INFERRED/non-qualifying signals | |
| Qualifying candidates generated | |
| Candidates killed | |
| Candidates deepened | |
| Survivors | |
| Actor-access kills | |
| Exposure-observability kills | |
| Effect-observability kills | |
| Recoverability kills | |
| Exact-resolution kills | |
| Control kills/escalations | |
| Human interventions required | |
| Evidence yield | LOW / MEDIUM / HIGH |

Where practical, record approximate active minutes by surface family or deepened candidate. Do not build telemetry infrastructure.

---

## Time and cost envelope

Target active research time: **60 minutes**.

Hard active-time ceiling: **90 minutes**.

Preferred incremental spend: **€0**.

Maximum incremental paid research spend: **€2**, only for one bounded observation with clearly superior expected information value.

Stop early when every candidate has a decisive disposition.

Do not use remaining time to rescue killed candidates.

---

## Verdicts

### A — ACTOR-OBSERVABLE FORGE CANDIDATE

At least one candidate survives the full actor-observable topology with concrete evidence of a real live actor, consequential uncertainty, recoverability, residual resolution gap, legitimate intervention path, exposure observability, decision-effect observability, and acceptable controls.

Recommend exactly one next FORGE experiment.

### B — TOPOLOGY IMPROVED, ONE BOUNDED UNCERTAINTY

No candidate yet justifies FORGE, but one candidate survives all except one bounded uncertainty and the actor-observable prior materially improves experimentability relative to Spec 031.

Recommend exactly one cheap discriminator.

### C — NO SURVIVOR, ACTOR-OBSERVABLE PRIOR INFORMATIVE

No candidate survives, but the run provides useful evidence about where actor-observable topology succeeds or fails and identifies the next dominant bottleneck.

Recommend one research-policy adjustment, not a forced candidate.

### D — ACTOR-OBSERVABLE DISCOVERY FAILURE

The run could not obtain enough qualifying actor signals to test the hypothesis, or execution violated the design enough that the result cannot be interpreted.

State precisely why.

---

## Required artifact

Create:

`experiments/032/actor-observable-decision-surface-discovery.md`

Preserve enough evidence and source references to reconstruct:

- raw actor signals;
- actor classification;
- candidate formation;
- kill decisions;
- deepened cases;
- exact-resolution findings;
- intervention/exposure/effect topology;
- controls;
- telemetry;
- comparison with Spec 031;
- verdict.

Do not modify historical experiment artifacts.

---

## Required completion report

Return exactly these sections:

1. Verdict
2. Primary question tested
3. Surface families inspected
4. Raw actor signals inspected
5. DIRECT / STRONG / INFERRED actor classification
6. Qualifying actor-observable candidates
7. Non-qualifying signal patterns
8. Candidate kill table
9. Deepened candidates
10. Economic-consequence findings
11. Recoverability findings
12. Exact-resolution findings
13. Intervention-path findings
14. Exposure-observability findings
15. Effect-observability findings
16. Control-feasibility findings
17. Strongest candidate, if any
18. Cheapest discriminator / FORGE handoff, if any
19. Comparison with Spec 031
20. Dominant bottleneck after this run
21. Operational telemetry
22. What RADAR learned
23. What remains unproven
24. Architecture/research-policy implications
25. Exactly one recommended next action

---

## Non-goals

Do not:

- inspect or update Spec 030 actor-response evidence;
- contact any actor;
- post publicly;
- send private messages;
- use cold email;
- resolve private identities from public handles;
- scrape contact information;
- build software;
- build a candidate database;
- build a scoring engine;
- build a surface ontology;
- build a regulatory rules engine;
- create an autonomous research scheduler;
- run ads;
- create landing pages;
- test pricing or willingness to pay;
- accept payments;
- perform TAM/SAM/SOM analysis;
- broaden a weak candidate into adjacent intent;
- force the candidate quota;
- force a survivor;
- preferentially search CRM/SaaS because Spec 028 succeeded there;
- reopen Spec 031 candidates without materially new actor evidence.

---

## Governing principles

> **A public surface is not the same thing as an accessible actor.**

> **Communication accessibility is not intervention experimentability.**

> **Intervention experimentability requires both actor access and effect observability.**

> **Delivery is not exposure. Exposure is not comprehension. Comprehension is not decision effect.**

> **Prefer decisions where reality can answer whether the resolution helped.**

> **Private state is acceptable only when the missing variable can be bounded and legitimately elicited from the actor.**

> **Behavioral evidence discovers the question. Authoritative evidence should answer it.**

> **Exact existing resolution can kill an otherwise elegant opportunity.**

> **The cheapest decisive observation should precede deeper research.**

> **Disposable before durable.**

> **Do not optimize RADAR for generating candidates. Optimize it for generating economically testable candidates.**
