# Spec 020 — EV Compatibility Commercial Evidence Gate

## Status

Research-only commercial/distribution gate. No product implementation by default.

## Context

Specs 017–019 progressively reduced uncertainty around one opportunity family:

```text
behavioral evidence
→ hidden configuration variable
→ credible derived information asymmetry
→ authoritative evidence feasibility
```

Spec 019 tested 10 representative UK EV × charger × tariff configurations and resolved 9 of 10 reproducibly from authoritative public evidence.

The candidate resolution is now approximately:

> Tell me whether this EV + charger + tariff setup will actually work before I buy or switch — show the material conditions, identify what controls charging, and show authoritative evidence for the answer.

Spec 019 also found meaningful maintenance complexity. Every compatible result carried material conditions; source guidance can be fragmented, undated, or contradictory; broad coverage could require significant monitoring and expert exception handling.

That does **not** justify another technical/data study yet.

The largest uncertainty has moved from technical resolvability to commercial relevance:

```text
OBSERVATION                         supported
REPEATED FRICTION                  supported
CREDIBLE ASYMMETRY                 supported
PLAUSIBLE RESOLUTION               supported
TECHNICAL RESOLVABILITY            strongly supported for narrow scope
DATA FEASIBILITY                   sufficient for narrow experiment; broad scale unresolved
COMMERCIAL PROPOSITION             unknown
VISITOR                            unknown
INTENT                             unknown
PRICED INTENT                      unknown
TRANSACTION                        unknown
```

This spec therefore asks whether enough observable, decision-proximate demand exists to justify the smallest behavioral experiment.

## Objective

Determine whether people currently making UK EV / charger / smart-tariff decisions expose a sufficiently specific and reachable intent surface for a **configuration-aware, evidence-backed compatibility answer**.

The central question is:

> Can we cheaply observe enough people who need configuration-level compatibility information at the point of decision to justify testing an actual decision artifact?

Do not validate broad EV interest.

Do not validate generic charger comparison, tariff comparison, EV ownership, or smart-charging education.

## Candidate proposition

The candidate should remain narrow:

```text
INPUT
vehicle
+ charger / planned charger
+ smart EV tariff / planned tariff
+ relevant household context

OUTPUT
compatible
/ compatible with material conditions
/ incompatible
/ unresolved

PLUS
controlling component
+ material caveats
+ authoritative provenance
+ source date
```

Example decision jobs include:

- Can I use this tariff with my existing EV and charger?
- Which charger should I buy if I want this tariff?
- Will this charger actually control the tariff, or will the vehicle?
- Does my vehicle generation qualify?
- Will solar / battery / multiple-EV context materially change the answer?
- Can I switch tariff without replacing hardware?

## Dominant uncertainty

The current uncertainty is **not** whether EV charging is popular.

It is whether configuration-specific compatibility uncertainty is:

- frequent enough;
- economically consequential enough;
- visible at a reachable decision point;
- insufficiently answered by suppliers/comparison sites;
- and observable cheaply enough to support a behaviorally meaningful experiment.

## Research design

Perform one bounded **commercial evidence / measurement-channel audit**.

Inspect three classes of evidence:

### A. Search intent

Look for UK search behavior expressing configuration or compatibility uncertainty around combinations of:

- EV + tariff;
- charger + tariff;
- vehicle + charger;
- compatibility / supported / works with;
- smart charging;
- tariff eligibility;
- charger choice conditional on tariff;
- switching tariff with existing hardware;
- multiple EV / solar / battery only where clearly decision-relevant.

Distinguish:

1. **CONFIGURATION-SPECIFIC DECISION INTENT**
2. **COMPATIBILITY / ELIGIBILITY INTENT BUT AMBIGUOUS**
3. **GENERIC EV / CHARGING / TARIFF INTEREST — EXCLUDE**

Do not let large generic EV search terms rescue a weak configuration-specific result.

Use free/public evidence first.

DataForSEO may be used only if:

- existing credentials/access remain available;
- expected information value justifies the request;
- incremental spend remains within this spec's budget;
- the request is tightly bounded;
- no new production integration is required.

DataForSEO remains a **Level 1 research instrument**.

### B. Decision questions

Inspect public questions/discussions only to determine whether users actually formulate configuration-level decisions.

Examples of useful evidence:

```text
Will Intelligent Octopus Go work with my [car] and [charger]?
Can I use OVO Charge Anytime with [vehicle]?
Do I need to replace my charger to use [tariff]?
Should the tariff connect to my car or charger?
Will this setup work with solar / two EVs?
```

Questions/forums are evidence of demand/friction here, not compatibility truth.

Record whether questions are:

- pre-purchase / pre-switch;
- setup/onboarding;
- post-failure troubleshooting.

Pre-decision evidence is substantially more valuable for this proposition.

### C. Existing resolution / competition

Inspect how users are currently expected to answer the decision.

Include:

- energy-supplier eligibility tools;
- charger manufacturers;
- EV charger comparison sites;
- tariff comparison tools;
- installers;
- other exact compatibility products discovered during the bounded search.

Ask whether an existing tool already accepts enough of the configuration to answer the complete decision with material conditions and provenance.

Do not treat fragmented supplier documentation as equivalent to a configuration-level answer.

## Required commercial reconstruction

From the evidence, reconstruct the strongest plausible commercial proposition.

Document:

### Actor

Who has the problem?

### Trigger

What event creates the decision?

Examples:

- buying an EV;
- buying/replacing a home charger;
- switching energy tariff;
- adding solar/battery;
- adding a second EV;
- discovering current setup is ineligible.

### Decision

What exactly must the actor decide?

### Economic consequence

What can go wrong financially or operationally if the compatibility answer is wrong or absent?

### Existing workaround

What does the actor do today?

### Residual gap

Why is that workaround insufficient?

### Candidate resolution

What is the smallest useful answer?

### Possible value capture

Identify plausible mechanisms without assuming any is validated, for example:

- charger referral/affiliate;
- energy-tariff referral;
- installer lead;
- paid detailed compatibility report;
- sponsored placement with disclosure;
- other mechanism directly supported by the evidence.

Do not enroll in programs or contact partners.

## Measurement-channel analysis

For each plausible acquisition surface, state the full observation chain.

For search, for example:

```text
real decision need
→ query expressed
→ reachable search inventory
→ impression
→ click
→ qualified configuration
→ answer viewed
→ recommended action available
→ action clicked
```

For forums/community traffic:

```text
real decision need
→ question/discussion appears
→ user sees relevant answer/tool
→ qualified visit
→ configuration completed
→ recommendation viewed
→ action clicked
```

Do not confuse upstream audience size with observable qualified behavior.

## Experiment power

If a plausible channel exists, estimate whether a small experiment could obtain enough **qualified independent observations** to teach us something.

The unit of evidence is not generic site traffic.

A qualified observation should represent someone with a real or plausibly imminent configuration decision.

Estimate:

- likely reachable volume;
- cost per qualified observation where estimable;
- expected qualification loss;
- time to accumulate observations;
- whether €60 and/or a small organic/manual distribution effort could plausibly produce a meaningful sample;
- what negative evidence would actually mean given the experiment's power.

Preserve:

> Absence of observed demand is evidence only to the extent that the experiment had sufficient power to observe demand.

## Commercial evidence gate

Use evidence, not enthusiasm.

### PASS TO BEHAVIORAL ARTIFACT

Proceed only if broadly all are true:

- repeated configuration-level decision behavior is observable;
- at least one acquisition surface reaches users before or during the economic decision;
- the existing solution remains materially fragmented or incomplete;
- the proposition can be expressed clearly without requiring EV expertise from the user;
- a small experiment could plausibly generate enough qualified observations to learn from behavior;
- the likely value-capture path is at least plausible;
- narrow evidence coverage from Spec 019 is sufficient for the experiment without first solving broad maintenance scalability.

### AMBIGUOUS

Return AMBIGUOUS if the decision exists but:

- reachable volume is unclear;
- observed behavior is mostly post-failure;
- competition may already resolve the exact decision;
- qualification loss makes a small experiment weak;
- or one tightly bounded commercial/distribution discriminator remains.

### FAIL

Return FAIL if broadly any are true:

- configuration-specific demand is too rare or inaccessible;
- observable behavior is mostly generic EV interest;
- users already receive an adequate exact answer at the point of decision;
- reaching qualified users requires disproportionate spend or partnerships;
- the smallest plausible experiment would be too underpowered to interpret;
- value capture is implausible even if the information is useful.

Do not rescue a FAIL by expanding geography, broadening into generic EV comparison, or building first.

## Required verdict

Choose exactly one:

- **A — PASS: build the smallest behavioral compatibility artifact**
- **B — AMBIGUOUS: one tightly bounded commercial discriminator remains**
- **C — FAIL: commercial observability does not justify an artifact**
- **D — BLOCKED: required evidence source unavailable**

## Required completion report

Return:

1. evidence sources and incremental cost;
2. search-intent findings with generic demand separated from configuration-specific demand;
3. public decision-question findings, classified pre-decision / onboarding / post-failure;
4. existing-resolution and exact-competition findings;
5. reconstructed actor / trigger / decision / consequence / workaround / residual gap;
6. strongest candidate proposition in one sentence;
7. plausible value-capture mechanisms ranked by evidence, not preference;
8. acquisition surfaces;
9. measurement chain for each serious surface;
10. experiment-power analysis;
11. what a smallest behavioral experiment would need to observe;
12. verdict A/B/C/D;
13. exact evidence most strongly supporting the verdict;
14. exactly one recommended next action;
15. architecture implications separated into:
    - evidence strong enough to preserve;
    - hypotheses too early to institutionalize;
16. **research economics report** as specified below.

## Research economics report

Beginning with this spec, explicitly treat AI/Codex research effort as an economic input to the Engine.

The purpose is not to optimize token usage prematurely. It is to detect when the Engine begins spending increasing inference/time for diminishing uncertainty reduction.

Report, to the extent observable without inventing precision:

### Effort

- elapsed research time;
- approximate number of searches / pages / major source inspections;
- paid data/API spend;
- whether the task was primarily web research, code execution, implementation, or mixed;
- any visible Codex usage constraint encountered during execution.

### Uncertainty reduction

State:

- dominant uncertainty entering the spec;
- dominant uncertainty leaving the spec;
- what important hypothesis moved materially up/down;
- whether the result changed the next decision.

### Evidence yield

Classify the run qualitatively:

- **HIGH YIELD** — substantial uncertainty reduction / decision change for modest effort;
- **MEDIUM YIELD** — useful evidence but meaningful uncertainty remains;
- **LOW YIELD** — substantial effort produced little decision-relevant information.

Do not infer hidden token counts, monetary model cost, or unavailable system metrics.

The Engine should eventually be able to reason about:

```text
information gained
÷
research time + paid data + inference/compute burden
```

but this spec does **not** authorize a generic research-efficiency score.

Preserve the principle:

> Compute and research effort are economic inputs. If increasingly expensive inference produces only tiny increments of evidence, that is itself an operating-cost signal.

## Next-action discipline

If **A — PASS**, specify the smallest behavioral artifact and its evidence gate, but do not implement it in this spec.

If **B — AMBIGUOUS**, permit exactly one bounded discriminator.

If **C — FAIL**, park or kill this EV opportunity family. Do not search for a replacement EV opportunity in the same spec.

If **D — BLOCKED**, identify the unavailable evidence and stop.

## Budget

- Cash: **€5 maximum** for research data; preferably €0.
- Research/operator time: **4 hours maximum**.
- No advertising spend in this spec.
- No product implementation.

## Non-goals

Do not:

- build a compatibility checker;
- build a landing page;
- implement software;
- create scrapers/connectors;
- create an EV database or graph;
- run the Spec 019 30-day maintenance replay;
- validate broad EV demand;
- expand beyond the UK;
- buy ads;
- contact users, suppliers, manufacturers, installers, or affiliate programs;
- create payment infrastructure;
- solve hundreds of configurations;
- rewrite architecture documents;
- treat generic EV search volume as proposition demand;
- infer demand from technical feasibility;
- optimize Codex usage at the expense of evidence quality.

## Governing principles

> Do not validate the scalability of an unvalidated product.

> Behavioral evidence discovers the question. Authoritative evidence should answer it.

> Provenance is part of the resolution when value comes from derived information.

> Negative experimental evidence is meaningful only relative to the experiment's power to observe behavior.

> Prefer opportunities whose commercial hypotheses can be falsified cheaply, quickly, and at sufficient sample size.

> Compute and research effort are economic inputs; track when their marginal evidence yield begins to deteriorate.
