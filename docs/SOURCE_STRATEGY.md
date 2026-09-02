# Source Strategy

## Purpose

This document records the current evidence-driven source acquisition strategy.

The Engine should not add connectors because a dataset is interesting. A source earns implementation when it contributes **novel, commercially relevant evidence that changes interpretation or corrects known errors**.

## Source Value

Use this as a decision heuristic rather than a precise formula:

```text
SOURCE VALUE ≈
Novel Information
× Commercial Relevance
× Breadth
× Reliability
× Combinability
× Reuse Freedom
────────────────────────────
Cash Cost
+ Engineering Cost
+ Maintenance
+ Vendor Dependency
+ Licensing Friction
```

The strongest sources are not necessarily individually powerful. The information advantage may live in the joins.

## Evidence Roles

### Discovery

Question: **What is changing, painful, unusual, or newly possible?**

Examples:

- Stack Exchange — articulated decision friction
- EUR-Lex / Cellar — regulatory and legal change
- OpenAlex — research topology and knowledge convergence
- EPO / patents — technology change
- Wikimedia / trends — attention velocity

### Structural

Question: **What are the underlying economics?**

Examples:

- Eurostat SBS — market structure and denominator
- Comext — physical trade flow, geography, concentration, quantities, values, implied unit values
- Prodcom — domestic production
- EPREL — product attributes, efficiency, repairability, warranty and spare-parts structure
- TED — institutional demand and budget
- marketplaces — price, availability and transaction supply where access permits

### Validation

Question: **Is there enough commercial intent, unresolved demand, or monetizable solution gap?**

Examples:

- Brave Search — solution and information supply
- DataForSEO — paid search-demand economics
- affiliate networks — monetization availability
- marketplaces — transaction proximity

Paid validation should normally occur after cheaper discovery and structural evidence have narrowed the candidate set.

## Empirical Connector Tests

### Comext — EARNED

Historical testing showed that physical-flow evidence can correct a patent false positive and can reveal import dependence and supply-chain structure that knowledge signals cannot.

Unique contribution:

```text
trade value
trade quantity
origin / destination
partner concentration
implied unit value
physical-flow velocity
import dependence
```

Important limitation: not relevant to all domains, especially pure software and many services.

### OpenAlex — EARNED

The original hypothesis was research velocity. The stronger discovered contribution is:

```text
semantic decomposition
fine-grained topics
knowledge topology
cross-domain convergence
research velocity
citation structure
```

It helps distinguish technology, capability, application and market concepts hidden inside broad patent categories.

Historical backtesting must explicitly distinguish data-time leakage from model-time leakage because modern topic classification may be applied retrospectively to older works.

### Brave Search — EARNED CONCEPTUALLY

Manual competition pressure tests showed that search can kill attractive-looking opportunities by revealing existing solution saturation.

Primary role:

```text
solution supply
information availability
specialist vs generic competition
freshness
geographic coverage
commercialization evidence
```

Treat result retention and third-party content rights carefully. The durable asset should be derived economic intelligence, not a stored copy of the search corpus.

### EUR-Lex / Cellar — EARNED CONCEPTUALLY

EUR-Lex adds a structurally orthogonal signal: **causal policy change**.

Policy can modify rights, obligations, access, deadlines, liability, incentives and technical market structure before ordinary demand signals appear.

Historical examples:

- GDPR was adopted in 2016 and applied from 25 May 2018, creating a known compliance deadline.
- PSD2 was adopted in 2015, required transposition by 13 January 2018, created legal rights for payment-initiation and account-information services, and required secure account-access interfaces through subsequent technical rules.

Policy evidence must retain lifecycle state. Proposal, adoption, entry into force, application and transposition are economically different.

Access/reuse position is strong:

- EUR-Lex permits reuse of legal documents for commercial and non-commercial purposes unless otherwise specified.
- EUR-Lex metadata is CC0.
- Cellar metadata is CC0 and exposes REST, SPARQL and notification mechanisms.
- EUR-Lex webservice is free after registration; Cellar can support direct and bulk retrieval.

Primary role:

```text
regulatory shock
obligation creation
market-design change
deadline / effective date
actor exposure
legal-state transitions
```

Policy alone does not prove demand. It should be joined with affected actors, required actions, solution supply and commitment.

### EPREL — EARNED DOMAIN-SPECIFICALLY

Excellent substrate for consumer durable-goods economics, with standardized product-level attributes. Generic TCO / repair-versus-replace opportunities are already increasingly occupied, so value likely lies in narrower exact-model decision synthesis or joins with price and household economics.

### DataForSEO — DEFER

Its strongest unique contribution is commercial search economics: volume, CPC and advertiser competition.

Current preferred role:

```text
open intelligence
    ↓
candidate asymmetry
    ↓
structural analysis
    ↓
paid demand validation only where information value justifies cost
```

Do not activate merely because an adapter exists.

## Current Preferred Stack

```text
CHEAP BROAD DISCOVERY
EUR-Lex + OpenAlex + Stack Exchange + EPO + public attention signals
        ↓
CANDIDATE DISEQUILIBRIA
        ↓
STRUCTURAL JOIN
Comext + Prodcom + Eurostat + EPREL + TED + legitimate marketplaces
        ↓
ECONOMIC CONSEQUENCE / ASYMMETRY
        ↓
COMPETITION + SOLUTION INTELLIGENCE
Brave + GitHub + app ecosystems + marketplaces
        ↓
SURVIVING OPPORTUNITY
        ↓
SELECTIVE PAID VALIDATION
DataForSEO + specialist datasets
        ↓
EXPERIMENT
```

## Acquisition Policy

Do not constrain by number of connectors.

Constrain by:

```text
time
cash
maintenance burden
licensing friction
marginal information gain
```

After each source or evidence investment, ask:

1. What new economic states became visible?
2. Which previous false positive or false negative can this source correct?
3. Did it change an opportunity interpretation rather than merely confirm it?
4. Which remaining blind spot now dominates uncertainty?
5. Is another data source more valuable than running a commercial experiment?

## Information Acquisition as Capital Allocation

A future agentic Engine may decide whether to purchase evidence.

The decision rule should eventually resemble:

```text
expected value of information > cost of acquisition
```

Example:

```text
Opportunity A
structural confidence: high
asymmetry confidence: high
commercial demand: unknown

Paid search evidence can resolve the dominant uncertainty.
Cost: €X
Expected decision value: > €X

→ acquire evidence
```

This should leave an audit trail explaining why the information was purchased and how the result changed the opportunity interpretation.

## Next Implementation Priority

The next connector should be **Comext physical-flow evidence**, because it has passed an incremental historical test and contributes a signal family not represented by the current codebase.

OpenAlex and EUR-Lex should follow only after the Comext slice is inspected against real data and the next uncertainty is reassessed.

Do not build the economic knowledge graph yet. The current research model should guide future slices, but implementation remains small and empirical.
