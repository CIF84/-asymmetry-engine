# Learning Checkpoint — Spec 024

**Checkpoint date:** 2 September 2026  
**Scope:** Spec 024  
**Milestone:** First empirically demonstrated RADAR → FORGE handoff

## Outcome

Spec 024 returned **P2 — MATERIAL FUNCTIONAL GAP DEMONSTRATED**.

A 20-case adversarial benchmark established an official Canadian truth baseline and tested live public counter-tariff resolvers against it. Accurate components exist, but no tested resolver consistently joined the bounded known-HS decision inputs into a complete, reliable decision output.

RADAR ends for this candidate.

The next phase is FORGE.

```text
OBSERVE
  ↓
REASON
  ↓
DISCOVER
  ↓
REJECT / ADVANCE
  ↓
LIVE COMPETITOR BENCHMARK
  ↓
MATERIAL RESOLUTION GAP DEMONSTRATED
  ↓
────────────────────────────
        RADAR → FORGE
────────────────────────────
  ↓
RESOLVE
  ↓
INTERACT
  ↓
MEASURE
```

## 1. What 024 proved

The candidate is no longer supported merely by fragmented search results or competitor marketing claims.

Spec 024 established:

- a current authoritative schedule baseline;
- 20 defensible cases spanning rates, origin, date, exposed/non-exposed controls, adjacent classifications, and remission relevance;
- live execution against multiple public resolvers;
- concrete systematic input/completeness gaps;
- at least one material live core error;
- a bounded residual resolution job.

The strongest evidence was a removed-seafood control where one live resolver returned a 25% counter-tariff and CAD 5,500 incremental cost despite the item being absent from the current authoritative schedule.

```text
OFFICIAL TRUTH
no current exposure
→ $0

LIVE RESOLVER
stale inclusion
→ 25%
→ $5,500

DIFFERENCE
→ economically consequential wrong decision
```

This is operational evidence that freshness, provenance, and joined decision logic matter economically.

## 2. The residual gap is narrow

The opportunity is not "tariff information" and not "customs classification."

The demonstrated unresolved function is:

```text
KNOWN CANADIAN HS TARIFF ITEM
+
ORIGIN
+
CUSTOMS VALUE
+
ENTRY / IN-TRANSIT DATE
+
CURRENT COUNTER-TARIFF SCHEDULE
+
EXCEPTION / REMISSION FACTS
        ↓
CASE-SPECIFIC EXPOSURE
+
RATE
+
INCREMENTAL COST
+
MATERIAL CAVEATS
+
AUTHORITATIVE EVIDENCE
+
NEXT ACTION
```

The known-HS boundary remains essential.

FORGE must not silently expand into customs classification.

## 3. Composition is the value hypothesis

Spec 024 showed that market components are individually available:

- current tariff-line membership;
- arithmetic;
- origin guidance;
- explanatory context;
- some batch/code lookup;
- generic remission guidance.

But no tested public resolver composed all required elements reliably into the bounded decision.

This reinforces a recurring Engine thesis:

> **Public evidence can exist while decision information remains unresolved because the economically useful answer requires trustworthy composition.**

The value hypothesis is therefore not privileged access to secret data.

It is reliable transformation of fragmented evidence into a decision-ready answer.

## 4. Provenance and freshness are part of the resolution

024 observed simultaneous public surfaces presenting materially different schedule counts and at least one stale exposure result.

Therefore provenance cannot be treated as decorative citation.

For this class of resolution:

```text
ANSWER
+
WHY
+
AUTHORITATIVE SOURCE
+
SOURCE CHECK DATE
+
UNCERTAINTY / CAVEAT
```

is part of the functional product.

This may generalize to other derived-information asymmetries, but should not yet become a generic architecture abstraction.

## 5. Input compatibility is resolution quality

A resolver may contain correct data yet still fail the decision job because it cannot accept the actor's available input representation.

Examples from 024 included:

- known eight-digit tariff item not directly accepted;
- curated product categories instead of known code;
- mandatory ten-digit input where the authoritative measure is expressed differently;
- no origin input;
- no entry-date input;
- no customs-value input.

Therefore:

> **Correct information behind an incompatible interface may still leave the actor's decision unresolved.**

## 6. Core truth and decision completeness remain distinct

The benchmark validated the separation introduced before 024.

### Core truth

- exposure;
- rate;
- effective-date treatment;
- incremental cost.

### Decision completeness

- classification caveat;
- origin caveat;
- remission relevance;
- authoritative provenance;
- usable next action.

FORGE should preserve this distinction.

A beautiful report with incorrect core truth is worthless.

A correct calculation without uncertainty/provenance/action may still fail to resolve the decision.

## 7. RADAR evidence ladder at handoff

Current state:

```text
OBSERVATION                         ✓
REPEATED FRICTION                   ✓
CREDIBLE ASYMMETRY                 ✓
RECOVERABLE INFORMATION            ✓
ECONOMIC CONSEQUENCE               ✓
EXACT RESOLUTION GAP               ✓
LIVE COMPETITOR BENCHMARK          ✓
PLAUSIBLE RESOLUTION               ✓

─────────────────────────────────────
RADAR → FORGE
─────────────────────────────────────

RESOLUTION PRODUCED                 ← NEXT
RESOLUTION CORRECT
RESOLUTION UNDERSTANDABLE
DECISION IMPROVED
BEHAVIOR CHANGED
VALUE CREATED
VALUE CAPTURED
TRANSACTION
REPEAT
```

Payment is intentionally downstream.

Do not collapse resolution quality, behavior change, value creation, and value capture into one experiment.

## 8. FORGE changes the Engine's relationship with reality

Until this point the Engine has primarily learned to observe, reason, discover, and reject.

FORGE introduces creation of an intervention:

```text
OPPORTUNITY HYPOTHESIS
        ↓
DISPOSABLE RESOLUTION
        ↓
CAN THE ANSWER BE PRODUCED?
        ↓
IS IT TRUSTWORTHY?
        ↓
IS IT DECISION-READY?
        ↓
EXPOSE TO REALITY
        ↓
OBSERVE BEHAVIOR
```

The first FORGE task should therefore manufacture the resolution itself rather than perform another market study.

## 9. Do not introduce acquisition dependency too early

Codex recommended immediately producing the brief for one real importer-supplied manifest.

That would combine two uncertainties:

1. can FORGE produce a trustworthy decision-ready resolution?
2. can we acquire a real importer and observe behavior?

It would also reintroduce the low-throughput B2B acquisition weakness observed in the cocoa experiment.

The cleaner sequence is:

```text
SPEC 025
produce and validate disposable resolution

THEN
expose resolution to real decision-maker(s)
and observe behavior
```

025 must not become research about whether the artifact could be built. It must actually produce the artifact.

## 10. First FORGE artifact

The initial artifact should be intentionally disposable.

Acceptable implementation forms include Markdown, HTML, or another simple human-readable report format.

It should resemble:

```text
CANADIAN COUNTER-TARIFF ORDER EXPOSURE BRIEF

HS ITEM       EXPOSURE       RATE       COST
0409...       YES            50%        $5,000
3004...       NO             0%         $0
4407...       REVIEW         25%        $10,000

TOTAL IDENTIFIED EXPOSURE
$XX,XXX

NEXT ACTION
✓ proceed / price with identified exposure
⚠ confirm origin
⚠ investigate remission
⚠ escalate classification if supplied code is uncertain

WHY
authoritative Government of Canada evidence
source checked <date>

NOT PROVIDED
customs classification
legal determination
remission eligibility guarantee
```

The exact presentation may evolve during construction if evidence shows a clearer decision format.

## 11. Disposable before durable

025 should optimize:

- speed;
- correctness;
- provenance;
- clarity;
- observability;
- reversibility;
- cheapness.

It should not optimize:

- scale;
- maintainability;
- UI polish;
- automation;
- generalized architecture;
- account systems;
- database design;
- ingestion pipelines;
- monetization infrastructure.

The artifact may be manually assembled.

That is a feature of the experiment, not a defect.

## 12. What 025 must answer

> **Can FORGE transform the demonstrated asymmetry into a trustworthy, decision-ready resolution using the evidence already available?**

This decomposes into:

```text
CAN PRODUCE ANSWER?
        ↓
CORE TRUTH CORRECT?
        ↓
UNCERTAINTY REPRESENTED?
        ↓
PROVENANCE INSPECTABLE?
        ↓
NEXT ACTION CLEAR?
        ↓
DECISION-READY ARTIFACT?
```

If yes, the next uncertainty becomes interaction with a real decision-maker.

If no, FORGE should identify the specific resolution failure rather than retreat automatically into broad RADAR research.

## 13. Supported vs unproven

**Supported:** a material live functional gap exists in the bounded public resolver market tested on 2 September 2026.

**Supported:** the gap can produce economically material wrong answers or require manual composition across tools.

**Supported:** authoritative evidence exists for the bounded transformation.

**Not yet proven:** FORGE can produce the complete answer reliably in a compact artifact.

**Not yet proven:** an importer understands or trusts the artifact.

**Not yet proven:** receiving the artifact changes a decision.

**Not yet proven:** changed decisions create measurable economic value.

**Not yet proven:** any actor will pay or otherwise permit value capture.

These uncertainties should be tested sequentially where practical.

## 14. Next empirical question

> **Can FORGE produce a trustworthy, decision-ready Canadian counter-tariff exposure brief from already-classified inputs without building durable software?**

This motivates Spec 025 — Canadian Counter-Tariff Disposable Resolution.
