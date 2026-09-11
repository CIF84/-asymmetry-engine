# Spec 047 — Realtime Migration Discriminator Feasibility Check

## Status

READY FOR EXECUTION

## Type

Bounded repository-plus-public-evidence discriminator-feasibility check for the single HOLD candidate from Experiment 046.

No actor contact. No publication. No outreach. No implementation. No FORGE construction. No canonical-policy modification.

## Baseline

Execute from synchronized `main` at or after:

`7dec70fa07ed5ac30ecb4531ffc75e2be7aba7db`

Experiment 046 is canonical at that baseline.

## Candidate under test

Experiment 046 candidate C10:

**Production `gpt-realtime-2.1` migration decision** exposed through the OpenAI Developer Community.

The actor is a production-system owner deciding how to qualify or sequence migration from a deprecated realtime model snapshot under a stated migration horizon.

Experiment 046 classified C10 as:

`HOLD — ONE BOUNDED DISCRIMINATOR`

because public evidence did not establish the paired workload-specific distribution needed to distinguish:

- model/capability behavior change;
- prompt adaptation;
- tool-schema/tool-contract adaptation;
- reasoning-setting/configuration effects;
- broader vendor capability/roadmap dependency.

The proposed discriminator was one anonymized paired matrix from the actor's already-existing fixed qualification corpus.

## Why this experiment exists

Experiment 046 correctly stopped before assuming that the missing paired matrix could be obtained or reconstructed.

The next uncertainty is therefore not yet the migration decision itself.

It is:

> **Is the discriminator publicly constructible from existing evidence, or is the decisive comparison genuinely actor-held?**

This distinction determines whether the next valid step is:

- bounded public research;
- an authorized actor-facing experiment;
- candidate rejection;
- or termination because an exact resolution or closed decision already exists.

Spec 047 must answer that question without contacting the actor or beginning FORGE.

## Primary question

Can the minimum paired discriminator required for C10 be constructed from already-public evidence with sufficient fidelity to change the migration decision?

## Secondary questions

1. What exact evidence cells are already public?
2. Which required cells remain missing?
3. Are the missing cells actually decision-sensitive?
4. Can any missing cells be recovered from current official/public sources without actor input?
5. Does an adequate exact resolution now exist?
6. Has the decision materially moved or closed since Experiment 046?
7. If actor-held evidence remains necessary, is the request narrow enough to justify a separately authorized INTERACT experiment?
8. Would unknown authorship or public-channel provenance weaken the intended claim?

## Scope boundary

This experiment may inspect only:

- the canonical Experiment 046 artifact;
- the current public OpenAI Developer Community thread that generated C10;
- current official OpenAI documentation directly relevant to the named realtime models, migration, reasoning settings, function/tool calling, prompting/configuration, deprecation, and any explicitly referenced migration guidance;
- public links explicitly referenced by the actor or official documentation when required to interpret the discriminator;
- narrowly necessary public evidence showing whether the actor's decision has materially moved or closed.

Do not broaden into general benchmarking, model-comparison research, competitor research, unrelated forum threads, social profiles, or market research.

## Explicit prohibitions

Do NOT:

- reply to or contact the actor;
- react, vote, like, tag, follow, message, or otherwise interact;
- ask for the matrix;
- post anywhere;
- run new production or synthetic model benchmarks;
- use private or connected actor data;
- solicit confidential prompts, schemas, logs, customer data, latency traces, or production examples;
- infer human/AI authorship from prose style;
- infer vendor roadmap commitments not explicitly public;
- infer undocumented model guarantees;
- construct fake matrix cells from generic documentation;
- treat absence of public evidence as proof that the actor lacks it;
- begin FORGE;
- create migration advice beyond the feasibility question;
- implement software;
- modify canonical docs, policies, prior experiments, source, tests, or schemas.

## Prospective timing

Start a prospective active-work timer before analysis.

Target active work: 10–20 minutes.

Hard ceiling: 30 active minutes.

Incremental external spend: €0.

Stop early when one disposition is decisive.

## Step 1 — Reconstruct the minimum discriminator contract

From Experiment 046 and the actor's public statements, define the minimum evidence package required to distinguish the competing explanations.

Do not expand the discriminator simply because more data would be interesting.

The default candidate contract is:

```text
same fixed actor corpus
same prompts/instructions
same tool schemas/contracts
same relevant session/configuration conditions where known
legacy model result
2.1 model result
per-intent pass/fail
required-tool-call success/failure
wrong-tool / no-tool outcome where relevant
reasoning setting where relevant
latency only if already captured and decision-sensitive
pre-existing acceptance threshold
```

Challenge every field:

- REQUIRED — needed to discriminate the decision;
- CONDITIONAL — needed only for certain failure classes;
- OPTIONAL — useful but not decision-sensitive;
- REMOVE — scope creep.

The result should be the smallest defensible matrix schema.

## Step 2 — Public evidence inventory

For each required/conditional field, classify availability as:

- `PUBLIC — ACTOR-SUPPLIED`
- `PUBLIC — OFFICIAL`
- `PUBLIC — OTHER AUTHORITATIVE`
- `ACTOR-HELD / NOT PUBLIC`
- `UNKNOWN`

Record exact supporting source or the absence of one.

Do not infer private values.

## Step 3 — Decision-state freshness check

Perform one bounded read-only freshness check of the native public thread and directly relevant official documentation.

Determine whether the migration decision is still:

- `LIVE`
- `MOVED BUT STILL CHANGEABLE`
- `CLOSED`
- `UNKNOWN`

A moved decision may include:

- actor reports successful migration;
- actor reports abandoning migration;
- actor adopts a specific workaround;
- official deprecation/migration state changes materially;
- a new exact resolution appears.

Do not inspect actor profiles or unrelated activity.

## Step 4 — Exact-resolution recheck

Check whether a new or previously missed adequate exact resolution now performs the actor's job.

An exact resolution must resolve the workload-specific decision, not merely describe model capabilities.

Possible exact resolution classes:

- official migration procedure addressing the reported failure mode;
- official compatibility/behavior guidance that removes the ambiguity;
- actor's own public paired results sufficient to choose a path;
- a public, authoritative decision artifact matching the same workload and acceptance criteria closely enough to substitute legitimately.

Generic docs, release notes, model cards, or unrelated anecdotes are not exact resolutions merely because they are relevant.

## Step 5 — Public constructibility test

Attempt to answer:

> Can the minimum discriminator be populated from public evidence without inventing, approximating, or substituting non-equivalent data?

Classify:

### P1 — PUBLICLY CONSTRUCTIBLE

All decision-sensitive fields required for the discriminator are public and sufficiently comparable.

This earns a separate bounded discriminator-analysis experiment. It does not itself authorize FORGE.

### P2 — ACTOR-HELD BUT BOUNDED

At least one decision-sensitive field is not public, but the missing evidence is narrow, already plausibly exists, can be requested without confidential detail, and a response could materially discriminate the decision.

This may earn a separately specified and authorized INTERACT experiment.

### P3 — ACTOR-HELD / BURDENSOME OR AMBIGUOUS

The required evidence would demand substantial new testing, confidential details, broad logs/prompts/schemas, or multiple ambiguous follow-ups.

Kill on recoverability/experiment economics unless a later independent signal changes the boundary.

### P4 — EXACT RESOLUTION FOUND

Current public evidence already performs the exact decision job.

Kill as duplicate resolution.

### P5 — DECISION MOVED / CLOSED

The original decision is no longer live in the relevant sense.

Kill as closed/moved.

### P6 — INVALID / INSUFFICIENT

The experiment cannot reliably establish one of the above due to scope, access, evidence, or execution failure.

## Step 6 — Interaction feasibility if and only if P2

If classification is P2, do not contact the actor.

Instead preregister the smallest future actor-facing discriminator request.

It must ask only for evidence necessary to classify the migration problem.

Prefer a request that can be answered with an anonymized aggregate matrix rather than raw prompts, schemas, logs, transcripts, customer data, or proprietary implementation details.

The request should normally avoid asking the actor to perform new broad work if the evidence already exists.

Record:

- target authoritative account/channel;
- decision object;
- exact evidence package requested;
- why each requested field is decision-sensitive;
- what must remain private/unrequested;
- delivery evidence;
- exposure evidence;
- semantic-response evidence;
- decision-state effect evidence;
- authorship provenance handling;
- silence logic;
- interaction limit;
- observation window;
- control classification.

No interaction is authorized by Spec 047.

## Interaction evidence ledger

If P2, use the aligned non-rigid ledger and include only hypothesis-relevant states.

At minimum assess:

```text
surface access
intervention permission
delivery
exposure
semantic engagement
account/channel identity
decision authority/accountability
authorship provenance
decision-state refinement
stated next action
observed downstream action
```

Economic effect and value capture may remain outside the next experiment if the immediate hypothesis is only discriminator acquisition and decision refinement.

## Authorship / agency provenance

Do not infer natural-person authorship.

Use only:

- `HUMAN VERIFIED`
- `AI-ASSISTED DISCLOSED`
- `DELEGATED AGENT DISCLOSED`
- `AUTOMATED DISCLOSED`
- `UNKNOWN`

Unknown authorship does not invalidate an authoritative-channel response when the intended claim concerns the production owner's public decision state rather than verified human cognition.

It does limit any claim about human understanding or cognitive change.

## Synthetic-evidence contamination check

If P2, ask:

- Would a semantically plausible response be attributable to the same production-owner decision channel?
- Could a third-party or automated response satisfy the surface signal without informing the actor's actual migration decision?
- What evidence would show the response actually contains actor-held workload state?
- What later evidence would still be required before claiming observed downstream migration or economic effect?

Do not perform bot detection.

## Control feasibility

If P2, classify the hypothetical future interaction as:

- `PASS`
- `CONDITIONAL`
- `REVIEW REQUIRED`
- `BLOCK`

Consider:

- OpenAI Developer Community rules and norms;
- public-only interaction;
- no confidential-data solicitation;
- no implication of OpenAI/vendor authority;
- no request for customer data or secrets;
- no promise of model behavior or roadmap;
- explicit user authorization required before posting;
- one bounded public interaction maximum unless a later spec says otherwise.

## Decision logic after P2

Even if P2 is earned, do not assume the candidate will reach FORGE.

A future response may produce:

```text
matrix localizes bounded adaptation problem
→ possible FORGE resolution experiment

matrix shows broad capability mismatch / roadmap dependency
→ likely KILL — RECOVERABILITY / RESOLUTION VALUE

matrix remains ambiguous
→ likely KILL or one newly bounded discriminator only if justified

no exposure / no response
→ measurement-limited result according to preregistered silence logic
```

## Comparison with Experiment 046

At completion state whether 047:

- reduced the HOLD to public research;
- confirmed genuinely actor-held evidence;
- showed the candidate was more burdensome than 046 suggested;
- found an exact resolver;
- found the decision moved/closed;
- or failed to discriminate.

Do not claim policy speed improvement.

## Evidence discipline

Classify important findings as:

- `RECORDED`
- `DERIVED`
- `INFERRED`
- `UNKNOWN`

Keep documentation facts separate from actor workload facts.

Generic model capability is not workload performance.

Actor report is evidence of reported production state, not independently verified model behavior.

## Success criteria

Spec 047 succeeds if it converts the HOLD into one decisive next-state classification without contact or construction.

A successful outcome can be P1, P2, P3, P4, or P5.

## Verdicts

### A — PUBLIC DISCRIMINATOR AVAILABLE

Classification P1. A bounded public discriminator analysis is now justified.

### B — ACTOR-HELD BOUNDED DISCRIMINATOR

Classification P2. One separately authorized actor-facing evidence request is justified.

### C — CANDIDATE KILLED

Classification P3, P4, or P5. The branch should stop unless new independent evidence emerges.

### D — INCONCLUSIVE

Classification P6 or equivalent unresolved state; no interaction or FORGE is earned.

### E — INVALID

Scope, external-action, timing, evidence, or repository-integrity requirements were violated.

## Required artifact

Create:

`experiments/047/realtime-migration-discriminator-feasibility-check.md`

Do not modify any other file.

## Repository integrity

Before completion verify:

- only the Experiment 047 artifact changed;
- no prior experiment changed;
- no canonical doc changed;
- no source, test, schema, or specification changed;
- no actor interaction occurred;
- no external publication occurred.

Run the existing test suite if available.

## Required completion report

Return exactly these 28 sections:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation / no-contact confirmation
6. Candidate decision state
7. Minimum discriminator schema
8. Required fields
9. Conditional fields
10. Removed / optional fields
11. Public evidence inventory
12. Actor-supplied public evidence
13. Official public evidence
14. Missing decision-sensitive fields
15. Decision-state freshness result
16. Exact-resolution recheck
17. Public constructibility classification P1–P6
18. Why public evidence is or is not sufficient
19. Actor-held evidence assessment
20. If P2: minimal future evidence request
21. If P2: interaction evidence ledger
22. If P2: authorship / agency-provenance handling
23. If P2: synthetic-evidence-contamination check
24. If P2: control-feasibility classification
25. Comparison with Experiment 046 HOLD
26. What the experiment establishes
27. What remains unproven
28. Exactly one recommended next action

Also return:

- artifact path;
- test/integrity result;
- commit SHA.
