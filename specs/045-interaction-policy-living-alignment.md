# Spec 045 — Interaction Policy Living Alignment

## Status

READY FOR EXECUTION

## Type

Bounded documentation alignment. No external research. No actor interaction. No software implementation. No historical-model rewrite.

## Baseline

Execute from synchronized `main` at or after:

`67725e6c590a4adfc3ef942b00bbf953c41dad6b`

Experiment 044 is closed and canonical at that baseline.

## Why this work is earned

Experiments 030, 035, 043, and 044 established that the current living operating documentation is materially incomplete around actor-facing interaction.

The evidence now supports a bounded update to present-tense operating policy, specifically:

- surface access, intervention permission, delivery/publication, and actor exposure are distinct states;
- exposure observability must be considered before an actor-facing experiment is executed;
- semantic engagement should not be silently equated with verified human cognition;
- message authorship, account/channel identity, decision authority, and accountability are distinct;
- authorship provenance can remain `UNKNOWN` without invalidating an authoritative decision-channel observation;
- stated intent, stated next action, public decision-state refinement, observed downstream action, economic effect, and value capture must remain distinct;
- synthetic-looking interaction can contaminate inference if semantic response is mistaken for real decision effect, but no bot/authorship-detection infrastructure is earned;
- `SAME / ADJACENT / SEPARATE` remains useful as a placement dimension but is insufficient by itself for experimentability;
- future actor-facing specs should preregister delivery/exposure evidence and silence handling;
- a non-rigid interaction evidence ledger is preferable to a mandatory linear pipeline.

Experiment 044 identified the smallest justified alignment package:

- `docs/OPERATING_MODEL.md` — Purpose and §§5, 6, 7, 9, 13, and 15 only;
- `README.md` — stale Experiments 030/035 status only;
- `ROADMAP.md` — stale open-window priority / next empirical gate only.

Everything else remains out of scope.

## Primary objective

Align current living documentation with the evidence earned by 030/035/043/044 while preserving:

- historical evidence horizons;
- manual/provisional status of the new interaction conventions;
- human authorization, consent, accountability, and governance;
- non-rigid experimentation;
- explicit UNKNOWN discipline;
- architectural restraint.

## Governing rule

```text
UPDATE LIVING TRUTH
WITHOUT
REWRITING HISTORY
OR
BUILDING THE IMPLICATION
```

## Allowed files

Modify only:

- `docs/OPERATING_MODEL.md`
- `README.md`
- `ROADMAP.md`
- required Experiment 045 result artifact

Create:

- `experiments/045/interaction-policy-living-alignment.md`

No other file may change.

## Explicitly prohibited files

Do NOT modify:

- `ARCHITECTURE.md`
- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- Experiments 030, 035, 043, or 044
- any earlier experiment
- source code
- tests
- database/schema files
- adapters
- any specification including this one

## Explicitly prohibited actions

Do NOT:

- inspect Reddit or live GitHub actor/surface state;
- contact any actor;
- perform new RADAR/FORGE/INTERACT research;
- search the web for bot prevalence or authorship-detection methods;
- infer human or AI authorship from prose style;
- create a bot detector, authorship classifier, identity service, provenance graph, interaction database, exposure tracker, notification monitor, or decision-state engine;
- create a rigid interaction pipeline;
- create a numeric interaction/topology score;
- infer GitHub superiority over Reddit;
- imply that Experiment 035 proved downstream implementation or economic value;
- reinterpret Experiment 030 silence as negative value evidence.

## Evidence horizon

Use as controlling evidence:

1. Experiment 030 final interaction record;
2. Experiment 035 final actor-facing result;
3. Experiment 043 interaction-topology / agency-provenance comparison;
4. Experiment 044 recursive alignment audit;
5. current living documentation at the baseline.

Do not broaden the evidence horizon unless a direct repository cross-reference is required to avoid contradiction.

## Alignment principle — non-rigid evidence ledger

Do not encode the following as a mandatory sequential lifecycle:

```text
DELIVERY
→ EXPOSURE
→ SEMANTIC PROCESSING
→ AGENCY / AUTHORITY
→ DECISION-STATE EFFECT
→ OBSERVED ACTION
→ ECONOMIC EFFECT
→ VALUE CAPTURE
```

Instead, document a **non-rigid evidence ledger** for actor-facing experiments.

Relevant states may include:

```text
SURFACE ACCESS
INTERVENTION PERMISSION
DELIVERY / PUBLICATION
ACTOR EXPOSURE
SEMANTIC ENGAGEMENT
ACCOUNT / CHANNEL IDENTITY
DECISION AUTHORITY / ACCOUNTABILITY
AUTHORSHIP PROVENANCE
DECISION-STATE REFINEMENT
STATED NEXT ACTION
OBSERVED DOWNSTREAM ACTION
ECONOMIC EFFECT
VALUE CAPTURE
```

Not every field is required for every experiment.

The specification should require only the states necessary to establish or falsify the experiment's actual hypothesis.

Later evidence may sometimes establish earlier states indirectly. Example: a substantive response can establish exposure even when no platform view receipt exists.

## Provenance conventions

### Authorship provenance

Where relevant, allow these provisional manual labels:

```text
HUMAN VERIFIED
AI-ASSISTED DISCLOSED
DELEGATED AGENT DISCLOSED
AUTOMATED DISCLOSED
UNKNOWN
```

Rules:

- never infer a label from writing style;
- `UNKNOWN` is neutral;
- authorship provenance is orthogonal to whether the responding channel has decision authority;
- do not imply these labels are a complete ontology.

### Decision-authority provenance

Where relevant, use the provisional manual scale:

```text
DIRECT
STRONG
INFERRED
UNKNOWN
```

Rules:

- classify authority relative to the specific decision object;
- do not equate proposal ownership with organizational authority, implementation authority, budget authority, or final approval authority;
- preserve human consent, accountability, and authorization where applicable;
- do not mechanize this scale.

## `docs/OPERATING_MODEL.md` required changes

### Purpose / evidence horizon

Update the stale statement that the document reflects lessons only through Specs 001–029 immediately before Spec 030.

The revised purpose should make clear that the living model now incorporates empirical interaction lessons through Experiment 044 while remaining directional and evidence-earned.

Do not rewrite the project purpose or broader FREEDOM objective.

### §5 — Economic experiment lifecycle

The current lifecycle ends with `ACCESSIBLE INTERVENTION → OBSERVED DECISION EFFECT` and can imply that interaction evidence is one simple transition.

Retain the economic lifecycle as a conceptual heuristic, but explicitly state that actor-facing interaction is evaluated through separable evidence states rather than assumed as one transition.

Add a compact non-rigid interaction evidence ledger using the fields above.

Make clear:

- the ledger is not a mandatory pipeline;
- experiments select only hypothesis-relevant states;
- same-surface access does not prove delivery or exposure;
- a substantive response may establish exposure and semantic engagement;
- decision-state refinement is not observed downstream action;
- observed action is not economic effect;
- economic effect is not value capture.

Do not make the section excessively long.

### §6 — Experiment contracts and proportional preregistration

Preserve the flexible, proportional contract philosophy.

Add a compact actor-facing preflight convention.

An actor-facing experiment should normally preregister at least:

```text
ACTOR / DECISION OWNER
DECISION OBJECT / TARGET CLAIM
INTERVENTION PATH
AUTHORIZATION
DELIVERY EVIDENCE
EXPOSURE EVIDENCE OR RESPONSE-AS-EXPOSURE LOGIC
SILENCE / NO-RESPONSE LOGIC
OBSERVATION WINDOW
INTERACTION LIMITS / STOP RULE
```

Conditionally, when required by the hypothesis, include:

```text
SEMANTIC-ENGAGEMENT EVIDENCE
DECISION-AUTHORITY PROVENANCE
AUTHORSHIP PROVENANCE
DECISION-STATE EFFECT
STATED NEXT ACTION
OBSERVED DOWNSTREAM ACTION
ECONOMIC EFFECT
VALUE CAPTURE
```

Do not create a universal rigid template or schema.

Add the rule that exposure observability must be considered **before publication**, because a successful post with no observable exposure path may be measurement-invalid for a behavioral hypothesis.

### §7 — Authorization is separate from execution

Preserve all existing authorization principles.

Add a bounded distinction:

```text
MESSAGE AUTHORSHIP
≠ ACCOUNT / CHANNEL IDENTITY
≠ DECISION AUTHORITY
≠ ACCOUNTABILITY
```

State that AI assistance or delegated-agent participation does not itself grant or remove authority.

Consequential authorization continues to depend on the authority and consequence of the action, not merely whether text was generated by a human or AI.

Do not create new legal claims.

### §9 — Evidence control

Extend the important evidence questions for actor-facing interactions.

Add questions such as:

- What establishes that the intervention was delivered?
- What establishes exposure?
- Does a response establish exposure even if platform view evidence is absent?
- Is the response semantically relevant to the target claim?
- What authority does the responding account/channel have over this decision object?
- What is known about message authorship, and what remains UNKNOWN?
- Is the observed evidence a decision-state refinement, merely stated intent, actual downstream action, economic effect, or value capture?

Add the core distinction that public or semantic-looking response must not automatically be converted into human cognition or economic effect.

Do not replace the existing `KNOWN / PUBLIC FACT / ESTIMATED / UNKNOWN` evidence classes.

### §13 — Execution QA versus epistemic QA

Preserve the current distinction.

Add actor-facing epistemic QA questions including:

- Was exposure observable or only delivery?
- Could silence represent unseen delivery?
- Does the response demonstrate semantic engagement with the actual proposition?
- Are authority and authorship being conflated?
- Could synthetic or delegated interaction create semantic evidence without proving the downstream effect being claimed?
- Is stated next action being mistaken for observed action?
- Is decision-state refinement being mistaken for economic value?

Describe synthetic-evidence contamination proportionally: it is a validity question when the claimed effect requires evidence beyond semantic exchange. Do not imply bots are presumed present.

### §15 — Operational telemetry

Preserve lightweight prospective telemetry.

Add that actor-facing experiments should record the hypothesis-relevant interaction evidence states where meaningful, such as:

- delivery;
- exposure;
- semantic engagement;
- authority provenance;
- authorship provenance;
- decision-state refinement;
- stated next action;
- observed downstream action;
- economic effect;
- value capture.

Missing or unavailable states remain `UNKNOWN`.

Do not require every state for every experiment and do not create synthetic scores.

## `README.md` required change

Change only the stale Current Evidence Boundary paragraph stating:

> Experiments 030 and 035 remain independent observation windows...

Replace it with a concise current-state statement reflecting that:

- 030 closed measurement-limited at exposure;
- 035 produced one bounded material decision-state refinement under an authoritative actor identity;
- 043 established the need to separate exposure, semantic engagement, authority, authorship provenance, decision-state effect, downstream action, and economic effect;
- this remains n=2 and does not establish repeatable actor effect, platform superiority, downstream implementation, or economic value.

Keep this to one short paragraph. Do not turn README into an interaction handbook.

Do not change any other README section unless a tiny wording adjustment is strictly necessary to avoid direct contradiction with the new paragraph.

## `ROADMAP.md` required changes

### Current operating priorities

Replace the stale priority `Preserve open empirical boundaries` referring to 030/035 as open windows.

The replacement should state the present priority after closure, approximately:

- preserve the interaction evidence distinctions learned from 030/035/043;
- require observable exposure/effect paths appropriate to future actor-facing hypotheses;
- continue treating decision-state refinement as distinct from downstream action and economic value.

Keep it concise.

### Next empirical gate

Replace the stale gate beginning `After already-authorized observation windows close:`.

The new gate should reflect the current unresolved economic question without inventing the next experiment.

A suitable evidence-gated formulation is:

```text
when a future candidate reaches INTERACT:
1. define which interaction evidence states are required by the hypothesis;
2. confirm exposure/effect observability before publication;
3. execute only through a legitimate authorized path;
4. classify the resulting evidence without collapsing decision-state refinement into downstream action or value;
5. choose the next experiment from the dominant remaining uncertainty.
```

Do not commit the roadmap to a specific domain, platform, actor, or next experiment.

Leave the rest of ROADMAP materially unchanged.

## ARCHITECTURE treatment

Do not modify `ARCHITECTURE.md`.

Experiment 044 found it already accurately describes interaction as manual/unimplemented and no software change is earned.

## Frozen historical models

Do not modify:

- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`

Their historical horizons are informative.

The living Operating Model supersedes interaction-policy assumptions where later evidence differs.

Do not insert retrospective annotations into the frozen files.

## Software / infrastructure gate

Explicitly preserve that manual fields do NOT earn software.

No implementation is justified for:

- bot detection;
- authorship inference;
- authority inference;
- identity verification;
- exposure tracking;
- interaction persistence;
- notification monitoring;
- provenance graphs;
- decision-state engines;
- generic experiment platforms.

## Cross-document consistency requirements

After editing, verify README, ROADMAP, and OPERATING_MODEL materially agree that:

- 030 and 035 are closed;
- 030 did not establish exposure or value failure;
- 035 established bounded decision-state refinement, not downstream action/economic value;
- exposure observability matters before behavioral publication;
- semantic engagement is not automatically verified human cognition;
- authority and authorship are distinct;
- authorship can remain UNKNOWN;
- interaction evidence is a non-rigid ledger, not a mandatory pipeline;
- software is not earned.

Do not duplicate the full Operating Model ledger in README or ROADMAP.

## Adversarial review

Before finalizing, ask:

1. Did we accidentally turn the evidence ledger into a rigid lifecycle?
2. Did we make every field mandatory regardless of hypothesis?
3. Did we imply the 035 response was verified human-only?
4. Did we weaken authority, consent, or accountability because AI may participate?
5. Did we treat UNKNOWN authorship as suspicious?
6. Did we overgeneralize from n=2?
7. Did we imply GitHub is superior to Reddit?
8. Did we convert decision-state refinement into downstream action or economic value?
9. Did we rewrite historical evidence rather than living policy?
10. Did we create or imply software infrastructure not earned by evidence?
11. Are README and ROADMAP still concise entry-point documents rather than duplicated operating manuals?

Correct any failure before completion.

## Validation

Run the existing test suite as a repository-integrity check.

Also verify:

- only the three allowed living docs plus the Experiment 045 result artifact changed;
- no frozen/historical files changed;
- no source/test changes occurred;
- no stale wording remains that says 030/035 are open observation windows;
- no new wording claims verified human authorship for 035;
- no new wording claims downstream implementation/economic value from 035.

## Required result artifact

Create:

`experiments/045/interaction-policy-living-alignment.md`

Record:

- baseline;
- prospective active time;
- spend;
- isolation;
- exact files changed;
- each Operating Model section changed and why;
- README stale-state correction;
- ROADMAP stale-state/gate correction;
- how non-rigid ledger semantics were preserved;
- provenance conventions introduced;
- what remains provisional;
- what remained deliberately untouched;
- cross-document consistency result;
- stale-term search result;
- test result;
- repository-integrity result;
- overall verdict;
- exactly one recommended next action.

## Verdicts

### A — LIVING INTERACTION POLICY ALIGNED

All evidence-earned interaction distinctions are represented proportionately in living documentation without historical rewrite, rigid ontology, or software expansion.

### B — MATERIAL IMPROVEMENT, RESIDUAL DRIFT

Most alignment succeeded, but a specific meaningful inconsistency remains and is explicitly identified.

### C — OVER-ALIGNMENT / EXCESS FORMALIZATION

The changes are materially more rigid, broad, or complex than the evidence earns.

### D — INCOMPLETE ALIGNMENT

Required living-document drift remains unresolved.

### E — INVALID

Scope, evidence, isolation, or integrity constraints were violated.

## Budget

Target active work: 15–25 minutes.

Hard ceiling: 40 active minutes.

Incremental external spend: €0.

Use prospective active-work timing and stop early when validation passes.

## Required completion report

Return exactly these 24 sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Files changed
7. Operating Model purpose/horizon change
8. Operating Model §5 change
9. Operating Model §6 change
10. Operating Model §7 change
11. Operating Model §9 change
12. Operating Model §13 change
13. Operating Model §15 change
14. README change
15. ROADMAP current-priority change
16. ROADMAP next-gate change
17. Non-rigid ledger validation
18. Provenance/authority validation
19. Historical/frozen-artifact validation
20. Software/non-build validation
21. Cross-document consistency result
22. Test and repository-integrity result
23. Artifact path and commit SHA
24. Exactly one recommended next action

## Success criterion

A technically literate new operator should now be able to read the living documentation and correctly infer that actor-facing evidence is multidimensional and hypothesis-dependent:

```text
publication is not exposure
semantic response is not necessarily verified human cognition
authorship is not authority
decision-state refinement is not observed action
observed action is not economic effect
economic effect is not value capture
```

while also understanding that these distinctions are **manual evidence discipline**, not implemented interaction infrastructure.