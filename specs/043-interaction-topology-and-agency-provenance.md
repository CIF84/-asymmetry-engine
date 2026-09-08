# Spec 043 — Interaction Topology and Agency Provenance

## Status

READY FOR EXECUTION

## Type

Bounded repository-only comparative analysis. No external interaction. No new opportunity discovery. No canonical model mutation.

## Baseline

Execute from synchronized `main` at or after:

`43c53a1f7879d08c101e6eaabf30b73cabfb6979`

Experiment 030 is closed.

Experiment 035 is closed with final verdict A — MATERIAL DECISION EFFECT OBSERVED.

## Why this experiment exists

Experiments 030 and 035 are the first matched-enough actor-facing interventions to support a useful comparative question.

Both involved:

- a fixed identifiable actor;
- a still-live decision;
- a bounded evidence-linked resolution;
- an explicitly authorized same-surface public intervention;
- no follow-up intervention during the observation window;
- a predefined observation window;
- a final read-only observation;
- explicit separation of delivery from downstream effect.

Their outcomes diverged materially:

- Experiment 030 established public surface delivery but could not establish actor exposure, comprehension, decision effect, or value.
- Experiment 035 established exposure, semantic engagement, actor-specific refinement, and a material decision effect under its governing specification.

A new validity question also emerged after 035:

> Public account response does not prove unaided human authorship.

Forums and collaborative platforms may contain human-authored, AI-assisted, delegated-agent, automated, or synthetic responses. The experiment therefore needs to distinguish response provenance, decision authority, semantic engagement, and downstream decision effect rather than assuming that an account response directly proves human cognition.

The purpose of 043 is to compare the two interaction topologies, identify what the evidence actually supports, introduce a bounded agency-provenance distinction, and determine what—if anything—has been earned for later alignment of the Opportunity Model or Operating Model.

## Primary questions

1. What structural properties were common to Experiments 030 and 035?
2. What structural properties differed materially?
3. Which differences plausibly explain why exposure/effect was observable in 035 but not 030?
4. Which differences plausibly explain why 035 produced useful actor refinement?
5. How should AI-assisted or agent-authored public responses affect interpretation of actor-facing experiments?
6. What minimum interaction topology is now supported for future actor-facing experiments?
7. What changes, if any, are earned for later canonical alignment?

## Non-goal

This experiment MUST NOT answer:

- whether GitHub is generally better than Reddit;
- whether technical actors are generally better than commercial actors;
- whether AI-generated responses are common on either platform;
- whether the 035 actor response was human-authored, AI-assisted, agent-authored, or synthetic;
- whether 035 produced downstream product/user/commercial value;
- whether 030's resolution had no value;
- whether any result generalizes beyond the bounded evidence.

No external research is authorized to estimate bot prevalence or authorship probabilities.

## Sources

Primary evidence:

- `experiments/030/interaction-record.md`
- `experiments/035/superset-actor-facing-resolution-test.md`
- governing Specs 030 and 035

Supporting context may be read only as needed from:

- Experiments 028, 029, 032, 033, 034
- current `README.md`
- current `ROADMAP.md`
- `docs/OPERATING_MODEL.md`
- `docs/OPPORTUNITY_MODEL_001_035.md`
- relevant checkpoints documenting accessible-surface and actor-first discovery

Do not use live external state. Persisted repository evidence is authoritative for 030/035.

## Isolation / prohibited actions

Do NOT:

- inspect Reddit, GitHub issue #43331, PR #41907, actor profiles, reactions, comments, or any live external state;
- contact or respond to either actor;
- modify Experiments 030 or 035;
- modify the frozen Opportunity Model;
- modify the Operating Model;
- modify README, ROADMAP, ARCHITECTURE, code, tests, or prior experiment records;
- create a bot detector, provenance service, account classifier, authorship model, or orchestration system;
- infer human authorship from writing style;
- infer AI authorship from writing style;
- search the web for bot prevalence or platform statistics;
- generalize platform superiority from n=2.

## Evidence classes

Every material conclusion must be classified as one of:

- **OBSERVED** — directly preserved in the experiment records.
- **DERIVED** — follows mechanically from observed facts.
- **INFERRED** — plausible interpretation of bounded evidence; not directly observed.
- **UNKNOWN** — cannot be established from preserved evidence.

Do not convert UNKNOWN to failure, zero, absence, human, AI, authentic, or synthetic.

## Comparison frame

Construct one explicit 030 × 035 matrix covering at minimum:

```text
actor identifiable
actor role relative to decision
live decision
public decision object
surface persistence
same-surface intervention
legitimate intervention path
platform-native notification / attention path
publicly observable exposure signal
publicly observable response channel
actor-held missing information
resolution falsifiability
invitation to challenge/correct
response attributable to fixed actor identity
human authorship provenance
AI assistance provenance
decision authority provenance
semantic engagement
public decision-state refinement
observable next-action change
downstream real-world action
economic effect
value capture
```

The matrix should distinguish `YES`, `NO`, `PARTIAL`, and `UNKNOWN` only where those states are supported.

## Critical distinction: account identity versus human authorship

Adopt this conceptual separation for the analysis:

```text
MESSAGE ORIGIN
Who generated the words?

DECISION AUTHORITY
Who is entitled to speak or act for the decision?

SEMANTIC ENGAGEMENT
Did the response engage the actual proposition?

DECISION-STATE EFFECT
Did the observable decision state materially change?
```

Do not collapse these into one construct.

### Authorship provenance classes

For public response evidence, classify authorship provenance only as:

- `HUMAN VERIFIED`
- `HUMAN + AI DISCLOSED`
- `DELEGATED AGENT DISCLOSED`
- `AUTOMATED / BOT DISCLOSED`
- `UNKNOWN`

If the experiment record contains no explicit disclosure or other direct provenance evidence, use `UNKNOWN`.

Do not infer from prose style, latency, sophistication, grammar, account age, or subjective “AI-like” characteristics.

### Authority classes

Classify decision authority separately as:

- `DIRECT` — fixed identity is explicitly the proposal/decision owner or author in the preserved record.
- `STRONG` — fixed identity has a documented role materially responsible for the decision.
- `INFERRED`
- `UNKNOWN`

Do not infer that an authenticated account proves unaided human authorship.

## Reinterpretation of 035

Test whether 035's final conclusions remain valid under authorship uncertainty.

At minimum distinguish:

### Claim A

> A human decision-maker personally read, understood, and cognitively changed their mind because of the intervention.

Assess whether this is supported.

### Claim B

> The intervention entered the fixed actor's public decision channel, elicited a semantically relevant response under an authoritative actor identity, supplied previously missing implementation state, and refined the observable decision object.

Assess whether this is supported.

Do not preserve Claim A merely because Claim B is strong.

If needed, recommend a more durable wording for M2/M3/M4/M5/M6 that does not assume unaided human cognition.

## Synthetic evidence contamination

Explicitly test the following failure mode:

```text
AE-generated intervention
        ↓
public platform
        ↓
AI/agent-generated response
        ↓
semantic-looking exchange
        ↓
false inference of real economic actor effect
```

Ask:

1. What evidence in 035 prevents or fails to prevent this contamination?
2. Does actor authority reduce the risk even when authorship is UNKNOWN?
3. What additional downstream evidence would be needed to establish that an economically consequential decision system—not merely a conversational system—was affected?

Do not claim the failure mode occurred. Assess only validity exposure.

## Decision-system concept

Evaluate this possible replacement for human-centric interaction logic:

```text
DELIVERY
  ↓
EXPOSURE
  ↓
SEMANTIC PROCESSING
  ↓
AGENCY / AUTHORITY
  ↓
DECISION-STATE EFFECT
  ↓
OBSERVED ACTION
  ↓
ECONOMIC EFFECT
  ↓
VALUE CAPTURE
```

Treat `AUTHORSHIP PROVENANCE` as a parallel evidence field rather than necessarily a stage in the causal chain.

The analysis must determine whether this is:

- earned now;
- partially earned / provisional;
- useful but premature;
- unsupported.

Do not promote it automatically.

## Interaction-topology analysis

Do not reduce the 030/035 difference to platform brand.

Consider bounded structural hypotheses such as:

- public decision object versus discussion thread;
- fixed decision owner versus general advice-seeking actor;
- platform-native attention/notification mechanics;
- durable review/discussion workflow;
- response expectations/norms;
- actor-held private implementation facts needed to resolve the question;
- ability of the actor to falsify or refine the resolution;
- observable public decision-state changes;
- private versus public downstream action;
- surface ability to distinguish delivery from exposure;
- whether the intervention itself naturally invited a correction that improved the resolution.

For each hypothesized explanatory factor, label it:

- SUPPORTED DIFFERENCE
- PLAUSIBLE CONTRIBUTOR
- NOT DISCRIMINATED
- CONTRADICTED

Do not pretend n=2 supports causal attribution where it does not.

## Same-surface topology refinement

Assess whether the existing SAME / ADJACENT / SEPARATE interaction-topology concept is sufficient.

Specifically test whether `SAME` should remain useful but be supplemented by distinct fields for:

```text
surface access
actor access
intervention permission
delivery observability
exposure observability
semantic response observability
decision-state observability
downstream action observability
```

Do not replace the existing topology merely for elegance. Require evidence that the additional distinction prevents a failure seen in 030 or clarifies the positive result in 035.

## Minimum future actor-facing experiment topology

Derive the smallest future preflight standard supported by 030 × 035.

Candidate requirements may include, but are not limited to:

- identifiable decision-bearing actor or authoritative decision channel;
- still-changeable consequential decision;
- legitimate intervention permission/path;
- credible exposure mechanism;
- observable exposure OR a response mechanism that itself establishes exposure;
- semantically discriminating response/effect channel;
- clear distinction between authorship provenance and authority;
- observable decision-state or downstream action where effect is the target;
- predefined handling of silence when exposure is unverified.

Do not require every future experiment to prove human authorship unless the experiment's hypothesis specifically concerns human cognition.

## Human-versus-decision-system interpretation

Answer explicitly:

> Does AE fundamentally need to influence humans, or does it need to influence economically consequential decision systems?

The answer must remain bounded to what 030/035 justify.

A permissible conclusion might distinguish:

- human cognition experiments;
- actor/organizational decision-state experiments;
- machine/delegated-agent decision experiments;
- economic-outcome experiments.

Do not erase human authority, accountability, consent, or authorization controls merely because agents may participate.

## Canonical alignment gate

At the end, classify each possible project update as:

- **EARNED NOW**
- **EARNED AS PROVISIONAL POLICY**
- **NOT YET EARNED**

Evaluate at minimum:

- Opportunity Model: exposure observability as a first-class experimentability condition;
- Opportunity Model: agency/authority provenance distinction;
- Operating Model: revised interaction evidence chain;
- Operating Model: authorship provenance field;
- experiment templates: explicit exposure / agency / decision-state evidence fields;
- architecture/software: any implementation;

No canonical file may be modified in 043. The result only recommends later alignment.

## Adversarial checks

Before finalizing, ask:

1. Are we treating 035's authoritative account response as proof of human authorship?
2. Are we treating UNKNOWN authorship as evidence of AI authorship?
3. Are we treating 030 silence as value failure?
4. Are we claiming GitHub beats Reddit from one case each?
5. Are we using platform notification mechanics without preserved evidence?
6. Are we confusing semantic response with downstream economic action?
7. Are we preserving the fact that 035 materially improved the resolution even if authorship is UNKNOWN?
8. Are we accidentally making human cognition irrelevant when the experiment specifically targets human judgment?
9. Are we proposing software to solve an ontology problem before the ontology stabilizes?

Correct any failure.

## Required result artifact

Create:

`experiments/043/interaction-topology-and-agency-provenance.md`

## Verdicts

### A — TOPOLOGY / PROVENANCE REFINEMENT EARNED

030 × 035 support one or more concrete, bounded changes to future interaction policy, and authorship uncertainty can be handled without invalidating the strongest supported 035 result.

### B — PARTIAL REFINEMENT ONLY

Some distinction is useful, but the evidence is insufficient to change future preflight policy materially.

### C — NO NEW POLICY EARNED

030 and 035 are too heterogeneous or provenance uncertainty is too severe for useful comparative refinement.

### D — 035 MATERIAL EFFECT INVALIDATED

Agency/authorship uncertainty destroys the evidence required for Spec 035's material-effect verdict.

### E — INVALID ANALYSIS

Scope, evidence, isolation, or attribution rules were violated.

## Budget

Target active work: 15–30 minutes.

Hard ceiling: 45 active minutes.

Spend: €0 external.

Use prospective active-work timing. Stop early if the comparison reaches a decisive bounded conclusion.

## Required completion report

Return exactly these 32 sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. 030 final state
7. 035 final state
8. Common structural properties
9. Material structural differences
10. 030 × 035 comparison matrix
11. Exposure-observability finding
12. Response/effect-observability finding
13. Actor-held-information finding
14. Challenge/refinement finding
15. Platform-brand inference check
16. 035 authorship provenance
17. 035 decision-authority classification
18. Claim A human-cognition assessment
19. Claim B authoritative-decision-channel assessment
20. Synthetic-evidence-contamination assessment
21. Whether 035 verdict survives provenance uncertainty
22. Revised interaction evidence chain assessment
23. SAME/ADJACENT/SEPARATE topology assessment
24. Minimum future actor-facing preflight standard
25. Human-versus-decision-system conclusion
26. Opportunity Model alignment candidates
27. Operating Model alignment candidates
28. Experiment-template alignment candidates
29. Architecture/software implication
30. What remains unproven
31. Artifact path and commit SHA
32. Exactly one recommended next action

## Success criterion

The result should let a future operator distinguish:

```text
public response
≠ authoritative actor response
≠ verified human authorship
≠ semantic engagement
≠ decision-state effect
≠ downstream action
≠ economic effect
```

while preserving any real learning that survives those distinctions.
