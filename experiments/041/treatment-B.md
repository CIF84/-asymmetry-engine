# Experiment 041 — Treatment Package B Frozen Artifact

## Package identity

- **Arm:** TREATMENT
- **Role:** PACKAGE-B AGENT
- **Scope:** Work Package B — Empirical Operating and Governance Truth
- **Baseline:** `6360064ea874e7350de2121e9cc569b9045fd1e0`
- **Repository state:** `HEAD` matched the requested baseline.
- **Mode:** Repository-only, read-only
- **UTC start captured:** `2026-09-04T12:00:11Z`
- **UTC end captured:** `2026-09-04T12:01:18Z`
- **Canonical files modified:** None
- **External interaction/spend:** None / €0
- **Live Experiment 030/035 state inspected:** No
- **Package A, control, or other treatment outputs inspected:** No
- **Compute/model cost:** UNKNOWN

## Evidence read

Read completely:

- `specs/041-parallel-work-package-agentic-test.md`, lines 1–611
- `experiments/041/preregistration.md`, lines 1–54

Read as relevant persisted evidence at the frozen baseline:

- `README.md`
- `ROADMAP.md`
- `docs/OPERATING_MODEL.md`
- `docs/OPPORTUNITY_MODEL_001_035.md`
- `docs/ECONOMIC_REASONING_MODEL.md`
- `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md`
- `docs/ARCHITECTURE_GAP_AUDIT_001_036.md`
- `docs/OPERATIONAL_CHECKPOINT_001_029.md`
- `docs/STRATEGIC_CHECKPOINT_001_029.md`
- `docs/LEARNING_CHECKPOINT_029.md`
- persisted results for Experiments 031, 032, 033, 034, 038, 039, and 040

The Package B contract and repository-only restriction are defined at `specs/041-parallel-work-package-agentic-test.md:140-156`. The preregistered package-independence gate is PASS at `experiments/041/preregistration.md:9-19`.

## Structured findings — eleven Package B questions

### 1. Current empirical operating loop

The current learned economic loop is:

```text
OBSERVE
→ RADAR
→ DISCRIMINATE
→ FORGE
→ INTERACT
→ MEASURE
→ LEARN
```

Operationally, that expands to: observe a signal; identify an actor and still-changeable decision; test consequence, recoverability, and intervention topology; search for an adequate exact resolution; choose the cheapest discriminator; construct and challenge a disposable resolution when earned; interact only with authorization; distinguish delivery, exposure, effect, value, and capture; then preserve what reality changed (`README.md:33-69`).

The human/repository execution loop is more procedural: question → reasoning/research → decision → bounded specification → authorization where required → execution → persisted result → independent review → continue/narrow/pivot/park/kill → checkpoint only when earned (`docs/OPERATING_MODEL.md:751-781`).

These are learned/manual operating practices, not a mandatory runtime pipeline. Candidates may skip stages or stop at a failed necessary condition (`docs/OPERATING_MODEL.md:232-268`; `docs/OPPORTUNITY_MODEL_001_035.md:264-309`).

**Confidence:** High.

### 2. Opportunity-discrimination policy

The operative economic object is an economically consequential decision under uncertainty for which information is recoverable, existing resolution is inadequate, a better resolution is feasible, the actor can legitimately be reached, and effect can be observed. Commercial opportunity additionally requires capture and repeatability (`docs/OPPORTUNITY_MODEL_001_035.md:35-73`).

Research order is governed by the cheapest decision-relevant observation capable of destroying a hypothesis while retaining credible survivors—not by a fixed stage order or additive score (`docs/OPPORTUNITY_MODEL_001_035.md:264-272`, `357-390`).

Strong current kill conditions are:

- no live identifiable decision;
- weak consequence;
- unrecoverable or uneconomic information;
- adequate exact resolver already exists;
- actor cannot legitimately be reached;
- effect is not observable;
- controls make the experiment illegitimate or uneconomic.

These are interacting constraints, not dimensions whose failures can be offset by a high aggregate score (`docs/OPPORTUNITY_MODEL_001_035.md:315-351`; `ROADMAP.md:64-70`).

Signal volume, novelty, friction, public information, market size, automation potential, and software deliverability do not independently establish opportunity (`docs/OPPORTUNITY_MODEL_001_035.md:340-351`, `537-573`).

**Confidence:** High.

### 3. Exact-resolution role

Exact-resolution comparison asks whether the same actor’s actual decision is already adequately served. The comparison frame is:

```text
ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING
```

It is an early fatal discriminator because difficult-to-find or transformable information is not a residual opportunity when an adequate resolver already exists (`docs/OPPORTUNITY_MODEL_001_035.md:149-165`).

The discriminator is replicated from Experiment 020 onward. Its reusable procedure is documented, but decisive functional equivalence remains semantic and domain-specific. Markdown is currently cheaper than embeddings, competitor databases, or a generic comparator (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md:170-174`).

Thus the exact-resolution role is **empirically supported manual policy**, not implemented generic automation.

**Confidence:** High.

### 4. FORGE and decision-compression status

FORGE currently means converting bounded, unstructured uncertainty into explicit options, dominant discriminators, caveats, testable next questions, and a decision-ready resolution. It need not produce categorical certainty (`docs/OPPORTUNITY_MODEL_001_035.md:440-469`).

Experiments 025, 029, 033, and 034 provide repeated examples across tariffs, CRM, and software architecture. This supports a real reusable artifact pattern, but the reasoning remains highly semantic and cross-domain generality is not established (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md:200-204`).

Current classification:

- bounded decision compression: demonstrated;
- provisional reusable FORGE capability: supported;
- generic decision/recommendation engine: not earned;
- reliable actor value from compression: unproven.

The maturity map explicitly labels decision compression “Provisional reusable capability,” actor decision effect “Under active test,” and value creation a hypothesis (`docs/OPPORTUNITY_MODEL_001_035.md:600-619`).

**Confidence:** High.

### 5. Interaction, exposure, and effect distinctions

The evidence model requires distinct states:

```text
delivery
≠ exposure
≠ engagement/response
≠ comprehension
≠ decision effect
≠ downstream action
≠ value creation
≠ value capture
```

Surface access, actor access, intervention permission, and actor exposure are also separate (`docs/OPPORTUNITY_MODEL_001_035.md:183-216`).

A publication or comment can prove controlled delivery without proving that the actor saw it, understood it, changed a decision, received value, or would pay. Persisted 030/035 initialization evidence is intentionally right-censored; UNKNOWN exposure or effect must not be interpreted as failure or zero response (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:153-164`).

The roadmap accordingly requires bounded authorized interaction and explicit separation of delivery, exposure, engagement, decision effect, and downstream action (`ROADMAP.md:78-90`).

**Confidence:** High for the distinctions; direct effect outcomes remain UNKNOWN by design.

### 6. Specification / authorization / capability / access boundary

The governing invariant is:

```text
SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS
```

(`README.md:129-135`)

- **Specification:** the historical/preregistered contract describing what should happen; it does not itself grant permission (`docs/OPERATING_MODEL.md:272-310`).
- **Authorization:** permission for a consequential action to happen. Contact, publication, excess spend, contracts, payment, sensitive data, and other irreversible actions require explicit authority unless separately covered (`docs/OPERATING_MODEL.md:314-341`).
- **Capability:** an executor’s technical ability to perform an action. Capability does not imply permission.
- **Access:** whether the relevant surface or actor can actually and legitimately be reached; surface access does not establish actor access, permission, or exposure (`docs/OPPORTUNITY_MODEL_001_035.md:183-200`).

The current boundary is procedural and human-governed. No autonomous publication/contact executor, permission service, standing-authority model, or regulatory engine is established (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md:182-186`).

UNKNOWN must never silently become PASS (`docs/OPERATING_MODEL.md:345-374`).

**Confidence:** High.

### 7. Prospective telemetry policy

Telemetry should remain lightweight and artifact-local. Required prospective fields include:

- experiment/phase;
- uncertainty before and after;
- actual or explicitly estimated active minutes and timing method;
- incremental spend and currency;
- human-attention events, minutes, and role;
- control escalations and disposition;
- meaningful input and candidate-flow counts;
- bounded external interactions;
- verdict and validity;
- evidence yield;
- policy/model change.

UNKNOWN must be recorded as UNKNOWN; N/A requires a reason. Counts must identify their units, and interaction telemetry must preserve causal-stage distinctions (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:166-188`).

The policy does not authorize a dashboard, database, synthetic efficiency score, retrospective token-price reconstruction, ROI, conversion rate, or commercial-compounding claim (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:190-208`; `ROADMAP.md:49-51`).

For Experiment 041 specifically, wrappers capture UTC intervals; retries, failures, restarts, interventions, and output size are recorded where exposed, while unavailable telemetry remains UNKNOWN (`experiments/041/preregistration.md:36-45`).

**Confidence:** High.

### 8. Evidence-earned automation rule

The rule is:

> Automation should multiply validated asymmetries and repeated mechanical work, not compensate for weak opportunities or unresolved assumptions.

(`README.md:149-153`; `ROADMAP.md:123-127`)

Implementation requires all of the following:

1. a repeated observed problem;
2. a mechanically reusable operation;
3. likely improvement to future experiment economics;
4. a small reversible implementation;
5. post-implementation measurement.

Otherwise the disposition is document, keep manual, defer, or wait (`docs/OPERATING_MODEL.md:617-663`).

Human governance, consequential authorization, next-uncertainty selection, preregistration, and independent challenge remain protected. Orchestration engines, autonomous schedulers/outreach, generic policy/scoring/decision engines, telemetry dashboards, and permission services are explicitly unearned (`docs/OPERATING_MODEL.md:667-710`).

**Confidence:** High.

### 9. Current evidence boundary: supported versus unproven

**Supported or directionally supported:**

- useful fatal-gate/rejection policy;
- actor/live-decision/consequence/recoverability/exact-resolution reasoning;
- legitimate-access requirement;
- bounded decision compression and cheap disposable resolutions;
- controlled publication/delivery;
- qualitative migration of the binding uncertainty toward downstream actor effect;
- repeated near-zero incremental external spend;
- repository-centered specifications, results, checkpoints, and human authorization;
- revision-aware observation persistence.

The strongest defensible compounding claim is qualitative: accumulated research policy produces clearer cheap discriminators and moves surviving uncertainty downstream, usually at zero incremental external spend (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:102-121`; `README.md:155-159`).

**Still unproven or UNKNOWN:**

- repeatable actor effect;
- reliable actor value from decision compression;
- willingness to pay;
- revenue or transactions;
- value capture;
- repeatability across actors/domains;
- scalable economics;
- economic compounding;
- quantitatively improving speed/productivity;
- general false-negative cost of aggressive rejection;
- generality of every gate;
- autonomous operation.

The opportunity model classifies value creation as a hypothesis and capture, repeatability, scalable economics, and FREEDOM compatibility as untested (`docs/OPPORTUNITY_MODEL_001_035.md:579-621`). Historical evidence has no defensible ROI, revenue, transaction, repeatability, or causal-value proof (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:123-129`).

Experiment 040 additionally supports role-separated quality protection in one workload but not general agentic economics: elapsed time was worse, the human-time difference immaterial, and compute cost UNKNOWN (`experiments/040/result.md:119-146`).

**Confidence:** High for the stated boundary; commercial outcomes remain UNKNOWN.

### 10. Material discrepancies among README, ROADMAP, and operating/checkpoint artifacts

No material present-tense contradiction remains between the post-039 README and ROADMAP. Experiment 039 explicitly aligned them and reports no remaining material contradiction across project definition, loop, scoring, automation, authorization, validation status, and long-term objective (`experiments/039/documentation-truth-alignment.md:71-84`).

Material reconstruction ambiguities remain:

1. **Different abstraction levels.** README presents `OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN`, while the older Operating Model’s economic-plane shorthand omits an explicit DISCRIMINATE label. Its detailed lifecycle and research policy nevertheless contain the discrimination operation (`README.md:33-69`; `docs/OPERATING_MODEL.md:195-268`).

2. **Temporal scope.** `docs/OPERATING_MODEL.md` is explicitly based on evidence through Spec 029 and predates 030 (`docs/OPERATING_MODEL.md:3-9`). `docs/OPPORTUNITY_MODEL_001_035.md` and the telemetry baseline are frozen through 035, while README/ROADMAP were aligned through Experiment 038/039. A reader must treat checkpoints as dated evidence, not automatically the newest canonical wording.

3. **Historical audit statements.** The pre-alignment architecture audit records broader/stale README and roadmap automation language (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md:227-243`). Experiment 039 later resolved that top-level documentary drift (`experiments/039/documentation-truth-alignment.md:21-48`). Reading the audit without chronology could recreate a contradiction that no longer exists at this baseline.

4. **Conceptual names versus implementation.** ATLAS, RADAR, FORGE, PORTFOLIO, and FREEDOM name an economic direction, not deployed modules or a guaranteed sequence (`README.md:161-169`). The learned loop is research practice, not runtime architecture (`experiments/039/documentation-truth-alignment.md:50-63`).

5. **Distributed current truth.** Current policy is reconstructable, but remains spread across top-level summaries, dated checkpoints, frozen models, experiment results, and Git history (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md:212-216`).

**Confidence:** High.

### 11. Confidence and unknowns

**Overall confidence:** High for current documented operating/governance policy; Medium for claims of empirical generality.

Primary UNKNOWNs:

- exposure, response, and effect beyond persisted 030/035 initialization evidence;
- whether decision compression reliably creates actor value;
- willingness to pay, transaction, capture, repeatability, and revenue;
- quantitative time-efficiency or productivity trend;
- full historical human-attention and compute cost;
- false-negative cost of the rejection policy;
- universal versus domain-contingent gates;
- stable mechanics sufficient to automate exact-resolution comparison, research scheduling, FORGE, telemetry, or interaction tracking.

Historical telemetry is sparse, heterogeneous, and often estimated; elapsed and active time are not interchangeable, candidate units vary, and compute/tool usage was not consistently recorded (`docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:153-164`).

## What a new operator must not infer

A new operator must not infer that:

- the learned operating loop is implemented software;
- named framework layers are deployed modules;
- every candidate must follow a rigid pipeline;
- a signal, friction, novelty, or public information constitutes demand or opportunity;
- additive scoring can compensate for a fatal constraint;
- publication or delivery proves exposure, response, effect, or value;
- access implies authorization;
- a specification grants permission;
- technical capability grants authority;
- decision compression has proven actor or commercial value;
- one successful resolution establishes repeatability or market size;
- zero incremental external spend proves declining total cost;
- UNKNOWN exposure is negative response;
- current evidence establishes revenue, willingness to pay, scalable economics, compounding, autonomous operation, or general multi-agent superiority.

## Retries, failures, and interventions

- **Retrieval retry:** 1. Attempting to read `experiments/041/preregistration.md` from the frozen commit failed because the permitted Experiment 041 directory is untracked; it was then read directly from the working tree.
- **Environment warnings:** Repeated macOS `xcrun` temporary-cache warnings occurred because the read-only environment could not create files under `/tmp`. Repository reads still completed.
- **Context restarts:** 0 observed.
- **Human clarifications/interventions:** 0.
- **External actions:** 0.
- **Canonical mutations:** 0.
- **Compute/model cost:** UNKNOWN.
- **Incremental external spend:** €0.

**Artifact status:** FROZEN PACKAGE-B OUTPUT. No recommendations and no Package A findings included.