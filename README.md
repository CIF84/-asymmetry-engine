# Asymmetry Engine

Asymmetry Engine is an experimental system for discovering economically consequential decisions under resolvable uncertainty, cheaply testing whether better information improves those decisions, and learning which resolution mechanisms can create and eventually capture repeatable value.

Commercialization remains the long-term objective. Revenue, willingness to pay, repeatability, scalable economics, and autonomous operation are not yet validated capabilities.

## Why it exists

AI continues to reduce the cost of implementation, research, analysis, and content production. Valuable problem selection remains scarce: which live decisions matter, what information is missing, whether that information can be recovered, whether an adequate answer already exists, whether the affected actor can legitimately be reached, and whether a better resolution changes anything.

The project therefore does not begin with “what software should we build?” It asks:

> What is the cheapest credible observation or resolution that can change an economically meaningful decision?

Software is one possible implementation of a proven resolution mechanism, not the default output.

## Current learned opportunity anatomy

A promising opportunity currently requires the interaction of:

```text
ECONOMICALLY CONSEQUENTIAL UNCERTAINTY
× RECOVERABLE INFORMATION
× INADEQUATE EXISTING RESOLUTION
× RESOLUTION FEASIBILITY
× ACCESSIBLE DECISION SURFACE
× OBSERVABLE EFFECT
× PLAUSIBLE VALUE CAPTURE
```

These are not additive score dimensions. One fatal constraint can dominate the others. A vivid signal is not automatically demand; friction is not automatically an opportunity; novelty is not automatically a residual gap; delivery is not automatically exposure or value.

## Current empirical operating loop

```text
OBSERVE
  ↓
RADAR
  ↓
DISCRIMINATE
  ↓
FORGE
  ↓
INTERACT
  ↓
MEASURE
  ↓
LEARN
  ↺
```

This is a research and operating loop, not a software pipeline. A real run may skip stages, return to an earlier question, or stop as soon as a necessary condition fails.

In practice the work often looks like:

```text
observe a signal
→ identify actor and still-changeable decision
→ test economic consequence, recoverability, and intervention topology
→ search for an adequate exact resolution
→ choose the cheapest discriminator
→ produce a disposable resolution when earned
→ challenge it adversarially
→ interact only with explicit authorization
→ separate delivery, exposure, effect, value, and capture
→ preserve what reality changed
```

RADAR transforms heterogeneous evidence into falsifiable opportunity hypotheses. FORGE compresses bounded uncertainty into options, discriminators, and testable next questions. Both currently depend heavily on semantic judgment.

## Current software

The implemented code is intentionally smaller than the conceptual Engine. It currently provides:

- bounded adapters for legitimate public or licensed source APIs;
- source-specific normalization into stable logical observations;
- SQLite source, pipeline-run, and observation persistence;
- revision-aware append-only captures for materially changed source items;
- deterministic current/latest observation retrieval;
- source metadata, timestamps, URLs, caveats, and provenance primitives;
- one domain-specific Czech CN75 economic reasoning slice with explicit lineage and unsupported claims;
- a small CLI and deterministic test suite.

Observation persistence distinguishes:

```text
logical item = (source_id, external_id)

unchanged recapture → duplicate, no redundant capture
changed recapture   → append next capture_sequence
current reader      → highest capture_sequence
```

This is bounded revision-aware persistence, not generic event sourcing or a complete provenance platform. Source-registry history remains deferred.

## What remains manual or unimplemented

There is no generic software implementation for:

- opportunity detection or generic RADAR;
- opportunity scoring or automatic ranking;
- monitoring;
- experiment or outcome databases;
- exact-resolution semantic comparison;
- research-policy selection;
- FORGE as a generic decision engine;
- actor interaction or effect measurement;
- authorization or regulatory policy enforcement;
- revenue-asset or portfolio management.

These absences are deliberate. Repository-centered specifications, result artifacts, checkpoints, and human review are currently cheaper and more reliable than prematurely encoding a still-changing operating policy.

## How empirical development works

Development follows evidence pressure rather than a fixed component roadmap:

```text
observed problem
→ bounded specification
→ explicit authorization where consequential
→ smallest valid execution
→ result artifact
→ independent challenge
→ checkpoint or formalization only when repeated evidence earns it
```

Specifications preregister questions, evidence, controls, budgets, stop conditions, and verdicts. Results record what happened. Checkpoints state what accumulated evidence currently means. Git preserves the history between them.

Consequential external action obeys:

```text
SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS
```

The current control model is procedural and human-governed. It is not a permission service or autonomous action layer.

## Design principles

- Observe before inventing.
- Fail cheaply and distinguish invalid measurement from negative value evidence.
- Search for adequate exact resolutions before expensive deepening.
- Preserve source identity, provenance, freshness, caveats, and unsupported claims.
- Prefer official APIs, open data, and legitimate access; public visibility does not imply unrestricted reuse.
- Keep source adapters independent from persistence.
- Use deterministic computation where it is simpler and more reliable than semantic inference.
- Prefer disposable resolution work before durable product work.
- Treat public signals as inputs to proprietary learning, not as permission to copy or contact.
- Avoid dependence on one platform where a validated workflow can reasonably be diversified.
- Automate repeated mechanical work only after evidence shows that doing so improves experiment economics.

The governing automation rule is:

> Automation should multiply validated asymmetries and repeated mechanical work, not compensate for weak opportunities or unresolved assumptions.

## Current evidence boundary

The project has demonstrated useful rejection policy, bounded decision compression, low-cost resolution construction, controlled publication, and revision-aware source persistence. It has only a partial operational telemetry baseline. It has not established repeatable actor effect, willingness to pay, revenue, or economic compounding.

Experiments 030 and 035 remain independent observation windows. Their publication initialization does not establish response or value.

## Long-term direction

The broader direction remains:

```text
ATLAS → RADAR → FORGE → PORTFOLIO → FREEDOM
```

This names an economic ambition, not implemented modules or a guaranteed sequence. Success would mean repeatedly producing useful economic evidence, resolving important decisions, validating value creation and capture, and eventually operating a diversified portfolio of low-maintenance assets with progressively less mechanical human effort.

## Historical design note

The project began with a generic signal → extraction → detection → registry → scoring → monitoring pipeline and count-based build milestones. Experiments 013–038 weakened that fixed-pipeline assumption and moved the operating model toward hard discriminators, accessible decision surfaces, exact-resolution checks, disposable resolutions, explicit controls, and evidence-earned automation. Git preserves the original documents; this README describes present truth.
