# Spec 029 — Customized CRM Disposable Decision Resolution

## Status

FORGE experiment.

Produce one disposable decision resolution for the already-observed customized-Salesforce case from Spec 028.

This is not a market study, customer-validation experiment, CRM implementation project, or software build.

## Context

Spec 028 tested accessible-decision-surface discovery and produced one surviving candidate: a small business publicly exposing a live decision about whether to stay with Salesforce, negotiate, upgrade, migrate to another CRM, add external tooling, or build internally.

The candidate survived because:

- the actor self-identifies before commitment;
- material economic and operational consequences are visible;
- many relevant inputs are publicly supplied or user-controlled;
- authoritative platform facts are recoverable;
- generic TCO calculators and vendor migration funnels do not appear to resolve the bounded workflow-specific decision independently;
- discovery and potential intervention can occur on the same public surface.

The next uncertainty is whether the resolution itself can actually be produced defensibly.

## Objective

Answer one question:

> **Can FORGE transform the already-observed customized-Salesforce case into a defensible, evidence-linked stay / upgrade / negotiate / migrate decision brief using only the public case facts plus authoritative public evidence, while representing material uncertainty explicitly?**

The experiment must **produce the artifact**.

Do not substitute further opportunity research for resolution construction.

## Fixed experimental case

Use the same 12-person customized-Salesforce case identified and deepened in Spec 028 as the fixed case.

Retrieve the original public thread and reconstruct only facts actually supplied by the actor or clearly attributable follow-up context.

Do not invent missing business facts.

Do not silently import assumptions from commenters as actor facts.

If the original thread is no longer accessible or lacks enough recoverable detail to construct a bounded resolution, report that as an execution constraint rather than replacing the case with a more convenient one.

## Actor

Small-business owner/operator using a materially customized CRM and facing a still-changeable platform decision.

For this experiment, preserve the actor boundary of the observed case. Do not generalize to enterprise CRM transformation or generic CRM buyers.

## Decision to resolve

The artifact should help structure the bounded choice among plausible directions supported by the observed case, such as:

- stay on the current Salesforce configuration;
- stay and negotiate commercial terms;
- upgrade Salesforce edition/tier where relevant;
- migrate to a named candidate platform actually considered by the actor;
- use an external/add-on workaround if genuinely supported by the case;
- defer a migration until one or more decisive unknowns are verified.

Do not add options merely to make the matrix look comprehensive.

Do not recommend building internally unless the actor actually raised that option and enough evidence exists to evaluate it meaningfully.

## Core resolution hypothesis

The artifact does **not** need to prove:

> Which CRM is objectively best?

It should test whether FORGE can instead:

> **Turn an opaque platform decision into a smaller, explicit set of trade-offs and identify what must be verified before commitment.**

A successful resolution can reduce decision uncertainty without producing a categorical winner.

## Required evidence classes

Every material statement used in the decision must belong to one of four classes.

### 1. KNOWN — case facts

Facts explicitly supplied by the actor in the observed public case.

Examples may include, only where actually present:

- current platform and edition;
- seat count;
- expected growth;
- current spend;
- quoted or expected pricing;
- renewal timing;
- current custom objects;
- workflows/automations;
- integrations;
- required features;
- internal administration capacity;
- candidate platforms;
- reported pain points.

### 2. PUBLIC FACT — authoritative external evidence

Facts supported by first-party or otherwise authoritative sources, such as:

- vendor pricing;
- edition/tier capabilities;
- API/automation limits;
- custom-object support;
- integration documentation;
- migration/import/export documentation;
- contractual or product limitations where publicly documented.

Prefer first-party vendor documentation for platform capabilities and current pricing.

Record source and source-check date.

### 3. ESTIMATED — modeled quantity or bounded assumption

Examples:

- migration labor range;
- training effort;
- workflow rebuild effort;
- implementation duration range;
- internal administration burden;
- switching-cost range;
- multi-year cost where a component cannot be directly observed.

Every estimate must state:

- what drives it;
- the assumed range or scenario;
- why that range is reasonable;
- how sensitive the decision is to it.

Do not create fake precision.

### 4. UNKNOWN / VERIFY — decision-sensitive missing fact

Examples:

- exact negotiated renewal price;
- whether a specific workflow has feature parity;
- edge-case behavior of a custom object;
- actual integration migration complexity;
- exact implementation quote;
- data-quality issue;
- contractual constraint.

If a missing fact could reverse the preferred direction, make that explicit.

## Source hierarchy

Use evidence in this order where applicable:

1. original actor's public case statements;
2. official vendor pricing and product documentation;
3. official migration/integration/API documentation;
4. authoritative third-party evidence strictly where first-party material cannot answer the bounded question;
5. practitioner evidence only to calibrate estimates, never to masquerade as a universal fact.

Commercial CRM recommendation sites, affiliate comparison pages, SEO listicles, and vendor-generated competitor pages may help discover facts but should not control the conclusion where better evidence exists.

## Freshness requirement

CRM pricing and product capabilities change.

Before finalizing the artifact:

- check current authoritative sources;
- record the source-check date;
- distinguish current evidence from historical facts in the observed thread;
- do not assume the actor's historical quoted/current price still equals today's public price;
- state where negotiated pricing prevents a public exact comparison.

Freshness is part of the resolution, not metadata decoration.

## Option construction

Construct only the smallest defensible option set supported by the case.

For each option evaluate, where evidence permits:

- recurring platform economics;
- one-time switching/implementation burden;
- workflow fit;
- customization preservation/rebuild risk;
- integration risk;
- operational disruption;
- internal administration/training burden;
- reversibility / lock-in;
- major decision-sensitive unknowns.

Do not force every field into a numerical score.

## Economic horizon

Use a **three-year decision horizon** if the available facts make it meaningful.

The purpose is to expose recurring-versus-switching-cost trade-offs, not to manufacture a precise TCO forecast.

Where a component cannot be credibly quantified:

- use a bounded range if defensible;
- otherwise keep it qualitative and mark it UNKNOWN / VERIFY.

Do not assign arbitrary dollar values to unknown labor or risk merely to complete a total.

## Required artifact

Create a standalone Markdown artifact under:

`experiments/029/`

Preferred path:

`experiments/029/customized-crm-decision-brief.md`

It must be understandable by a reader who has not read Specs 028–029.

## Required artifact structure

### A. Decision snapshot

Open with a concise answer to:

- What decision is being made?
- What are the credible options?
- What currently appears to drive the decision?
- Is any option clearly dominated on available evidence?
- What cannot yet be concluded?

Do not bury the decision behind methodology.

### B. Case facts

List the relevant KNOWN facts from the actor.

Clearly distinguish them from external evidence and estimates.

### C. Option matrix

Use a compact decision table similar in spirit to:

```text
OPTION                 ECONOMICS     WORKFLOW RISK     SWITCHING BURDEN     REVERSIBILITY
Stay / negotiate       ...           ...               ...                  ...
Upgrade                 ...           ...               ...                  ...
Migrate candidate A     ...           ...               ...                  ...
Migrate candidate B     ...           ...               ...                  ...
```

Adapt fields to the evidence rather than mechanically preserving this exact layout.

### D. Three-year economics

Where defensible, show:

- known recurring costs;
- public list-price scenarios;
- known or estimated one-time migration/implementation costs;
- material internal-effort assumptions;
- ranges rather than false point estimates;
- which assumptions dominate the comparison.

If a complete three-year cost cannot be defensibly calculated, say so and show only the portions that can be supported.

### E. Workflow-fit and migration-risk analysis

For each serious option identify:

- essential workflows known from the case;
- documented support or limitation;
- what would need rebuilding;
- what remains unverified;
- which unknowns could reverse the decision.

### F. Decision-sensitive unknowns

Create a prioritized list of only the unknowns that materially affect the choice.

For each state:

- why it matters;
- which options it discriminates between;
- how it could be verified cheaply.

### G. Next validation action per option

Give **exactly one primary next validation action per serious option**.

Examples might include obtaining a written renewal quote, testing one workflow in a sandbox, exporting a representative object, confirming API capability, or obtaining a bounded migration quote.

Use the action that reduces the most important uncertainty for that option.

### H. Evidence and freshness

Provide authoritative references, source-check date, and any important evidence limitations.

### I. Boundaries

State explicitly that the artifact:

- is not a CRM implementation plan;
- is not a migration guarantee;
- does not inspect the actor's private CRM instance;
- cannot verify undocumented custom behavior;
- does not know negotiated prices unless supplied;
- represents estimates and uncertainty explicitly;
- is a bounded decision aid, not a universal CRM ranking.

## Recommendation rule

Do **not** force a winner.

A preferred direction may be stated only if the available evidence materially dominates alternatives after uncertainty is represented.

Otherwise conclude with a conditional decision structure such as:

```text
IF X is true → option A strengthens
IF Y is true → option B strengthens
IF Z cannot be verified → do not commit yet
```

The experiment succeeds if it makes the decision materially more legible, even if the correct output is "verify these two facts before choosing."

## Decision-space-reduction test

After producing the artifact, explicitly ask:

> **Did this resolution reduce the decision space, or merely organize information?**

Evidence of reduction can include:

- eliminating a dominated option;
- narrowing the plausible option set;
- identifying a decisive threshold;
- converting broad uncertainty into one or two verifiable questions;
- revealing that the current decision framing is wrong;
- identifying a reversible next step that avoids premature commitment.

If the artifact merely summarizes CRM facts without changing the structure of the decision, it is not yet a strong resolution.

## Internal validation

Validate the artifact before finalizing.

### V1 — Case fidelity

- Every KNOWN fact traces to the actor's public case.
- Commenter claims are not silently attributed to the actor.
- Missing facts are not invented.

### V2 — Public-fact fidelity

- Material vendor claims trace to current authoritative evidence.
- Pricing/capability evidence is dated.
- Historical and current facts are not conflated.

### V3 — Estimate discipline

- Estimates are visibly labeled.
- Ranges have stated drivers.
- No fake precision.
- Decision sensitivity is stated.

### V4 — Unknown discipline

- Material unknowns are visible.
- Unknowns capable of reversing the decision are highlighted.
- The artifact does not hide uncertainty behind a recommendation.

### V5 — Decision usefulness

- The opening is decision-first.
- Options are bounded.
- Trade-offs are legible.
- Each serious option has exactly one next validation action.
- The artifact reduces the decision space rather than merely summarizing information.

Log and correct material failures before assigning the final verdict.

## Verdicts

### A — DECISION-READY RESOLUTION PRODUCED

The artifact is case-faithful, evidence-linked, explicit about estimates and unknowns, decision-first, and materially reduces the decision space.

Next uncertainty becomes whether a real actor understands/trusts it and whether it changes a decision or next action.

### B — RESOLUTION PRODUCED, ONE MATERIAL WEAKNESS

The artifact is useful but exactly one bounded weakness prevents a confident A verdict.

Recommend exactly one repair or discriminator.

### C — RESOLUTION NOT RELIABLY PRODUCIBLE

The public case plus authoritative evidence cannot support a defensible bounded decision resolution.

Identify the precise failure: insufficient case inputs, unrecoverable workflow state, unstable evidence, unbounded implementation uncertainty, or another concrete reason.

Do not retreat into broad CRM market research.

### D — EXPERIMENT INVALID

The artifact was not actually produced/tested, the original case became unavailable, or another execution failure prevented the experiment from answering its question.

## Time and cost envelope

Target active execution time: **60–90 minutes**.

A bounded overrun is allowed only to validate/correct a material evidence issue in the produced artifact.

Preferred spend: **€0**.

Maximum research spend: **€2**, only if clearly justified by information value.

## Research/execution economics

Record:

- active time;
- original case facts extracted;
- authoritative sources inspected;
- serious options evaluated;
- quantitative calculations performed;
- estimates introduced;
- material unknowns retained;
- corrections made during validation;
- files created;
- paid spend;
- entering uncertainty;
- leaving uncertainty;
- hidden complexity discovered;
- evidence yield HIGH / MEDIUM / LOW.

## Required completion report

Return exactly these sections:

1. Verdict
2. Artifact created
3. Fixed case reconstructed
4. Decision being resolved
5. Known case facts
6. Public facts used
7. Estimates introduced
8. Unknown / verify facts retained
9. Option set
10. Three-year economics
11. Workflow-fit analysis
12. Decision-sensitive unknowns
13. Next validation action per option
14. Decision-space reduction
15. Case-fidelity validation
16. Evidence/freshness validation
17. Estimate/uncertainty validation
18. Artifact weaknesses
19. What FORGE learned
20. What remains unproven
21. Research/execution economics
22. Architecture/framework implications
23. Exactly one recommended next action

## Non-goals

Do not:

- contact or reply to the original actor;
- post publicly;
- acquire another participant;
- search for a more convenient CRM case;
- conduct CRM market sizing;
- conduct broad CRM category research;
- research pricing or monetization for this product idea;
- test willingness to pay;
- run ads;
- build a landing page;
- build software;
- build a CRM recommendation engine;
- create a vendor database;
- automate pricing ingestion;
- scrape vendor documentation at scale;
- create generic migration architecture;
- perform implementation or migration work;
- access private CRM data;
- force a categorical CRM recommendation;
- expand the problem to rescue the experiment.

## Governing principles

> **FORGE makes something capable of interacting with reality.**

> **Disposable before durable.**

> **Resolve one decision before building a system.**

> **Known facts, public facts, estimates, and unknowns are different evidence classes.**

> **Uncertainty represented is more useful than false precision.**

> **A decision aid can create value by reducing the decision space without choosing for the actor.**

> **Do not expand the problem to rescue the experiment.**
