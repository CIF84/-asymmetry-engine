# Experiment 047 — Realtime Migration Discriminator Feasibility Check

Run date: 2026-09-11

Repository baseline: `efe585fa227590e8a27c20cca02ba63a28ddcf58` on synchronized local `main`

Execution mode: bounded repository-plus-public-evidence feasibility check; no actor contact, benchmark, publication, FORGE work, or implementation

## 1. Verdict

**B — ACTOR-HELD BOUNDED DISCRIMINATOR.**

Constructibility class: **P2 — ACTOR-HELD BUT BOUNDED**. The public record contains a credible paired aggregate claim and a controlled-comparison attestation, but it does not contain the per-intent paired outcomes, denominator, acceptance rubric/threshold, target reasoning setting, or complete tool-outcome breakdown needed to distinguish a bounded adaptation problem from a broader model/roadmap dependency. The actor states that the qualification already ran and that its methodology, corpus, and detailed failures exist, so the missing decision-sensitive evidence is plausibly pre-existing and can be requested as one anonymized aggregate matrix without requesting confidential material.

## 2. Repository baseline

- Repository root: `/Users/romanchristov/Documents/GitHub/-asymmetry-engine`
- Origin: `https://github.com/CIF84/-asymmetry-engine.git`
- Branch: `main`
- Synchronized baseline: `efe585fa227590e8a27c20cca02ba63a28ddcf58`
- Spec 047 was present and read completely.
- The working tree was clean before execution.

## 3. Active time and timing method

Prospective run-level timing began at `2026-09-11T19:07:03Z` and froze at `2026-09-11T19:11:48Z`: **4 minutes 45 seconds**. The clock covers Experiment 046 reconstruction, the single native-thread freshness check, directly relevant official-document checks, schema classification, synthesis, artifact construction, tests, and integrity verification. The OpenAI Docs skill's required initial official-page lookup preceded candidate analysis and the timer; no duration is inferred for it. No per-field timing precision is claimed. The run stopped once P2 was decisive, below the 10–20 minute target rather than filling time, and remained inside the 30-active-minute hard ceiling.

## 4. Spend

Incremental external spend: **€0**. No new model calls or benchmarks were run for the discriminator, and no private or paid data was used.

## 5. Isolation / no-contact confirmation

- Inspected only the canonical Experiment 046 artifact, the native C10 thread, directly relevant official OpenAI documentation, and the forum guidelines linked from the native surface.
- Did not inspect the actor profile or unrelated activity.
- Did not contact, reply to, react to, vote on, message, tag, follow, or otherwise interact with the actor.
- Did not ask for the matrix or publish anything.
- Did not run a benchmark or infer private values from generic documentation.
- Did not inspect competitors or unrelated forum research.
- Did not expose or request prompts, tool schemas, logs, transcripts, customer data, secrets, or proprietary implementation details.
- Did not begin FORGE or produce migration advice.

## 6. Candidate decision state

**LIVE.** `RECORDED`: on 9 September 2026 the production-owner account described a current qualification failure and a migration problem under a stated January 2027 horizon. `RECORDED`: the bounded 11 September freshness check found the thread still public with the same decision statement, no public paired matrix, and no closing or successful-migration update. `RECORDED`: official documentation still lists `gpt-realtime-2025-08-28` as deprecated. `UNKNOWN`: the exact final shutdown date is not independently established by the official pages inspected; it remains an actor-stated conditional. No evidence showed the decision had moved or closed.

Native evidence: [production migration thread](https://community.openai.com/t/follow-up-gpt-realtime-2-1-shows-a-critical-shift-from-tool-driven-to-reasoning-driven-behavior-in-our-production-ai-agent/1396083).

## 7. Minimum discriminator schema

The smallest defensible matrix is one row per anonymized intent class already present in the fixed qualification corpus:

| Column | Classification | Purpose |
|---|---|---|
| anonymized intent-class ID | REQUIRED | exposes whether failure is localized without revealing business content |
| paired case count | REQUIRED | supplies the denominator and confirms comparable coverage |
| legacy model identifier | REQUIRED | fixes the comparator |
| target model identifier | REQUIRED | fixes the candidate replacement |
| constant-control attestation/version tokens | REQUIRED | confirms the same corpus, prompt/instruction version, tool-contract version, and relevant session configuration without disclosing contents |
| legacy pass count | REQUIRED | paired baseline outcome |
| target pass count | REQUIRED | paired replacement outcome |
| success rubric | REQUIRED | makes pass/fail interpretable |
| pre-existing acceptance threshold | REQUIRED | determines whether the migration path is viable |
| expected tool required? | REQUIRED | separates tool-required from non-tool cases |
| target correct-tool / wrong-tool / no-tool / other-failure counts | REQUIRED | distinguishes the reported tool-selection failure class |
| target reasoning effort | REQUIRED | tests the explicitly plausible configuration explanation |
| paired tool-choice mode | REQUIRED | distinguishes autonomous, required, or forced-tool behavior |
| attempt/retry policy | REQUIRED | makes the stated three-attempt example and aggregate comparable |
| session/audio condition identifier | CONDITIONAL | required only if input capture, VAD, language, or modality can explain the row |
| language/audio-consistency result | CONDITIONAL | required only for a migration acceptance criterion covering the reported French audio/text inconsistency |
| latency | CONDITIONAL | required only if latency is part of the pre-existing acceptance threshold |
| short sanitized failure-class note | CONDITIONAL | needed only when the categorical tool outcome does not explain the failed row |
| aggregate success rate | OPTIONAL | derivable from required counts |
| sanitized example utterance | OPTIONAL | illustrative, not necessary to discriminate |
| raw prompts, schemas, logs, transcripts, customer data, secrets | REMOVE | confidential scope expansion; unnecessary for the first discriminator |
| generic benchmark or competitor result | REMOVE | non-equivalent substitution |
| full application architecture | REMOVE | unnecessary and potentially proprietary |

## 8. Required fields

Required fields are: anonymous intent class; paired denominator; exact legacy and target model identifiers; a non-content constant-control attestation/version token set; paired pass counts; the success rubric; the pre-existing acceptance threshold; whether each class requires a tool; target correct/wrong/no-tool/other counts; target reasoning effort; paired tool-choice mode; and the qualification attempt/retry policy.

These are necessary to determine whether the public 100% versus approximately 25% aggregate reflects a broad capability mismatch, a concentrated tool-selection/configuration failure, or an evaluation-contract difference. Raw implementation contents are not required.

## 9. Conditional fields

- Session/audio condition identifier, if capture, VAD, language, or modality can affect a row.
- Language/audio-consistency outcome, only if it belongs to the actual migration acceptance gate.
- Latency, only if the actor's pre-existing threshold treats it as decision-sensitive.
- One short sanitized failure-class note, only when categorical tool outcomes do not explain a failed class.

## 10. Removed / optional fields

Aggregate rates and a sanitized example are optional because the required counts produce the rate and the matrix, not an anecdote, performs the decision job. Raw prompts, tool schemas, logs, transcripts, customer data, secrets, proprietary implementation details, the full corpus, generic benchmarks, competitor comparisons, and a full architecture description are removed. Requesting them would add confidentiality risk without improving the first discriminator.

## 11. Public evidence inventory

| Field | Availability | Evidence status |
|---|---|---|
| same fixed corpus | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: actor says the same test corpus was used |
| same prompts/instructions | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: same instructions; exact text properly absent |
| same tools/application/architecture | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: same tools and application; exact contracts absent |
| same voice/language configuration | PUBLIC — ACTOR-SUPPLIED | `RECORDED` attestation |
| exact model pair | PUBLIC — ACTOR-SUPPLIED and PUBLIC — OFFICIAL | `RECORDED` |
| aggregate legacy result | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: 100% reported |
| aggregate target result | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: approximately 25% reported |
| one example intent/result | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: legacy success, target failure after three attempts |
| qualitative target failure modes | PUBLIC — ACTOR-SUPPLIED | `RECORDED`: no-tool, misinterpretation, refusal/inability, language/preamble issues |
| paired denominator by intent class | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` |
| paired per-intent pass counts | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` |
| success rubric | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` beyond “successfully executed” |
| pre-existing acceptance threshold | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` |
| complete correct/wrong/no-tool breakdown | ACTOR-HELD / NOT PUBLIC | `UNKNOWN`; only qualitative summary public |
| target reasoning effort | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` |
| paired tool-choice mode | ACTOR-HELD / NOT PUBLIC | `UNKNOWN` |
| attempt/retry policy | ACTOR-HELD / NOT PUBLIC | `UNKNOWN`; one example reports three attempts |
| official target capabilities | PUBLIC — OFFICIAL | `RECORDED`: reasoning setting and function calling supported |
| official workload equivalence | UNKNOWN | no guarantee found |

## 12. Actor-supplied public evidence

`RECORDED`: the actor reports a full qualification using the same application, architecture, instructions, tools, voice configuration, language, and corpus, with only the model changed. It reports 100% legacy success versus approximately 25% target success, one repeated failure example, typical legacy latency, and several qualitative target failure modes. It also says the methodology, corpus, and detailed failure cases are available to provide to the Realtime engineering team.

This is evidence of the actor's reported production qualification state. It is not an independently verified benchmark and does not reveal the missing matrix cells.

## 13. Official public evidence

`RECORDED`: official [`gpt-realtime-2.1` model documentation](https://developers.openai.com/api/docs/models/gpt-realtime-2.1) describes a reasoning model with configurable reasoning effort and supported function calling. `RECORDED`: official [`gpt-realtime` documentation](https://developers.openai.com/api/docs/models/gpt-realtime) lists the `gpt-realtime-2025-08-28` snapshot as deprecated. `RECORDED`: the Realtime API reference exposes reasoning configuration and tool-choice controls, including a specific/required tool mode. `RECORDED`: official [Realtime prompting guidance](https://developers.openai.com/api/docs/guides/voice-prompting) says prompt precision, reasoning effort, preamble behavior, and tool policy are configurable and should be evaluated.

These facts show plausible discriminator variables. They do not establish performance on WebPlanning-AI, a deterministic/non-reasoning equivalence guarantee, an extension, a roadmap commitment, or a workload-specific migration solution.

## 14. Missing decision-sensitive fields

The public record lacks: the paired denominator and per-intent outcomes; the pass rubric and threshold; target reasoning effort; paired tool-choice mode; attempt/retry policy; target failure counts by correct/wrong/no-tool/other; and session condition where relevant. These fields are decision-sensitive because the aggregate alone cannot show whether failures are broad, localized, configuration-dependent, or below/above the actor's actual migration gate.

No missing value was inferred. Absence from public evidence does not imply the actor lacks it.

## 15. Decision-state freshness result

**LIVE.** The one bounded read-only check on 11 September 2026 found no actor update reporting migration, abandonment, a chosen workaround, or closure. The post remains a current request for a viable path, and the official model page continues to mark the legacy snapshot deprecated. The January 2027 date remains actor-supplied rather than independently verified by the official evidence inspected.

## 16. Exact-resolution recheck

No adequate exact resolution was found. Official documentation identifies configuration levers and general prompting practices, but it does not resolve the reported fixed workload, populate the paired matrix, establish functional equivalence, promise a non-reasoning mode, extend the deprecated snapshot, or state a product roadmap. The actor's aggregate and example demonstrate a reported problem but do not localize it enough to choose a migration path. P4 is not earned.

## 17. Public constructibility classification P1–P6

**P2 — ACTOR-HELD BUT BOUNDED.**

P1 fails because multiple decision-sensitive cells are not public. P3 fails because the actor says the full qualification already ran and offers methodology/corpus/failure evidence; the minimum public request can be answered with aggregate anonymized counts rather than new broad testing or confidential content. P4 fails because no exact resolver exists. P5 fails because the decision remains live. P6 fails because the permitted evidence is sufficient to make a decisive constructibility classification.

## 18. Why public evidence is or is not sufficient

Public evidence is sufficient to establish that a controlled paired qualification is reported, that the target exposes relevant configuration levers, and that the missing evidence is bounded. It is insufficient to construct the discriminator because a 100% versus approximately 25% aggregate plus one example cannot locate failure across intent classes, reveal the pass contract, or distinguish reasoning/tool-choice/retry settings. Substituting official generic claims or another workload would be non-equivalent and was not done.

## 19. Actor-held evidence assessment

`DERIVED`: the missing evidence is plausibly actor-held because the actor reports a completed full qualification and offers its methodology, corpus, and detailed failures. `UNKNOWN`: whether the actor has already summarized those results in the exact requested shape. The bounded request asks only for a redacted aggregation of existing results; it does not ask for a new benchmark, corpus contents, raw prompts, schemas, logs, transcripts, or customer data.

## 20. If P2: minimal future evidence request

Target: the same production-owner account in the same native thread.

Preregistered request content:

> Could you share one anonymized aggregate table from the qualification already run, with one row per intent class: paired case count, legacy and 2.1 pass counts, whether a tool was required, the 2.1 correct-tool / wrong-tool / no-tool / other-failure counts, the 2.1 reasoning-effort and tool-choice modes, the retry policy, and the pre-existing pass threshold? A simple confirmation that prompt, tool-contract, corpus, and relevant session versions were held constant is enough—please do not share prompts, schemas, logs, transcripts, customer data, or proprietary examples.

Why each field is requested is recorded in Sections 7–9. Interaction limit: at most one public top-level contribution and no follow-up unless a later specification separately authorizes it. Observation window: seven calendar days from verified delivery, ending with at most one read-only final check. No interaction is authorized or executed here.

## 21. If P2: interaction evidence ledger

| State | Required evidence / observability |
|---|---|
| surface access | `OBSERVABLE`: native public thread remains accessible |
| intervention permission | `UNKNOWN` now; requires explicit user authorization and a later governing spec |
| delivery | `OBSERVABLE`: published permalink and public rendering |
| exposure | `INDIRECTLY OBSERVABLE` only through a substantive response from the target account; silence leaves UNKNOWN |
| semantic engagement | response supplies/refuses/refines requested fields in a way dependent on the request |
| account/channel identity | `OBSERVABLE`: same public production-owner account |
| decision authority/accountability | direct for its own migration state; not OpenAI product/roadmap authority |
| authorship provenance | `UNKNOWN` unless explicitly disclosed otherwise |
| decision-state refinement | matrix localizes bounded adaptation, broad mismatch, or remaining ambiguity |
| stated next action | qualifying only if the account states a concrete migration/test path |
| observed downstream action | outside immediate hypothesis; actor-report dependent unless independently public |

Economic effect and value capture are not required for the immediate discriminator-acquisition hypothesis and remain outside the next experiment. Silence cannot be treated as value failure: delivery may be verified while exposure and response remain UNKNOWN.

## 22. If P2: authorship / agency-provenance handling

Authorship provenance is **UNKNOWN**. No inference is made from prose style. A semantically dependent response from the same production-owner account may establish authoritative-channel engagement and reported decision-state refinement, but it cannot establish verified human reading, comprehension, or cognitive change. The account has authority over its disclosed migration decision, not OpenAI's roadmap or model guarantees.

## 23. If P2: synthetic-evidence-contamination check

A third-party response cannot satisfy the actor-held discriminator. A response under the target account must contain the missing workload-state fields or explicitly refine their availability; a generic semantic-looking reply is insufficient. An automated or AI-assisted response could still express accountable public channel state, but with authorship UNKNOWN it cannot prove human cognition. Even an adequate matrix would establish reported qualification evidence, not independently verified model behavior, completed migration, downstream operational effect, economic effect, or value capture.

## 24. If P2: control-feasibility classification

**CONDITIONAL.** The [OpenAI Developer Community guidelines](https://community.openai.com/guidelines) permit relevant technical discussion but state that the forum is public/community-run, staff response is not guaranteed, and sensitive information must not be shared. A future test therefore requires a separate explicit user authorization and governing spec, one bounded public interaction maximum, no private message or follow-up, no confidential-data request, no implication of OpenAI authority, no model/roadmap promise, no promotion, and the seven-day/one-check observation boundary. These controls are feasible but were not exercised.

## 25. Comparison with Experiment 046 HOLD

Experiment 047 **confirmed genuinely actor-held evidence** and narrowed the HOLD. Experiment 046 correctly identified a paired fixed-corpus discriminator. Experiment 047 removed raw corpus, prompts, schemas, logs, broad latency collection, generic benchmarks, and architecture detail; identified the exact missing decision-sensitive cells; established that relevant public documentation is not an exact substitute; and classified the remaining package P2. It did not reduce the HOLD to public research, find a resolver, or show the candidate closed.

## 26. What the experiment establishes

- The discriminator cannot be populated publicly without invention or non-equivalent substitution.
- The actor publicly reports that a paired qualification and underlying evidence already exist.
- The missing evidence can be compressed into one anonymized aggregate matrix with bounded fields.
- Current official documentation exposes plausible configuration variables but does not resolve this workload.
- The decision remains live on the permitted freshness evidence.
- One separately specified and authorized actor-facing evidence request is justified; FORGE is not.

## 27. What remains unproven

- The missing matrix values, denominator, rubric, threshold, settings, and failure distribution.
- Whether the actor can or will produce the bounded aggregation without new work.
- Whether any response would be delivered, exposed, semantically processed, or decision-changing.
- Natural-person authorship or verified human cognition.
- Whether the failure localizes to prompting/configuration/tool contracts or reflects broader capability mismatch.
- Any extension, deterministic replacement, early-access channel, or vendor roadmap commitment.
- Successful migration, downstream operational action, economic effect, or value capture.

## 28. Exactly one recommended next action

Specify—but do not execute without separate explicit authorization—one bounded public INTERACT experiment that requests only the anonymized aggregate matrix preregistered in Section 20 and applies the ledger and controls in Sections 21–24.

Artifact path: `experiments/047/realtime-migration-discriminator-feasibility-check.md`

Test/integrity result: **PASS — 89 tests passed in 0.76 seconds; only the Experiment 047 artifact changed before staging; no prior experiment, canonical document, source, test, schema, or specification changed; no actor interaction or external publication occurred.**

Commit SHA: recorded after the verified local commit.
