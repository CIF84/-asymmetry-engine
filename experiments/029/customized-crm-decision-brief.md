# Customized CRM Stay / Upgrade / Migrate Decision Brief

- **Experimental manifest:** CRM-029-A
- **Fixed case:** the 12-person customized-Salesforce case posted to r/CRM on 13 August 2026
- **Decision horizon:** three years
- **Public sources checked:** 2 September 2026
**Currency:** USD; taxes excluded

## Evidence labels used throughout

- **KNOWN** — stated by the actor in the fixed public case or the actor's follow-up in that thread.
- **PUBLIC FACT** — current first-party vendor evidence, linked and dated below.
- **ESTIMATED** — a transparent scenario or bounded calculation, with drivers and sensitivity stated.
- **UNKNOWN / VERIFY** — a missing, decision-sensitive fact. It is not silently filled with a commenter claim.

## A. Decision snapshot

### The decision

The owner must decide whether to keep a deeply customized Salesforce Professional org and buy only the missing access, upgrade that org to Enterprise, or prove that HubSpot Enterprise can replace its operating logic before migrating. Commercial negotiation is part of both Salesforce paths, not a fourth technical architecture.

### Credible option set

1. **Professional + Web Services API, with renewal terms negotiated.** Preserve the existing org and buy the documented API-enablement add-on, but accept that API access alone does not raise the documented five-active-flows-per-flow-type limit or prove missing app/Visualforce capability.
2. **Salesforce Enterprise, with price and term negotiated.** Preserve the existing data model and gain documented API access plus much higher flow limits, subject to a written quote and edition-entitlement check.
3. **HubSpot Enterprise, but only after one representative workflow passes a parity test.** HubSpot documents custom objects, Salesforce custom-object sync, workflows, and imports, but those facts do not prove that this actor's relationships, automation, permissions, reports, or edge cases survive.

### What drives the decision now

The dominant variable is **workflow parity**, not headline seat price. The actor says the CRM is a heavily customized company-wide system of record, yet the public case does not reveal the object model or even one end-to-end critical workflow. That missing information controls both whether Professional plus API is sufficient and whether migration is safe.

The second driver is the **written three-year commercial envelope at 12 and 24 seats**. Public list prices make the recurring-cost stakes visible, but negotiated discounts, seat types, add-ons, implementation services, and renewal terms remain unknown.

### Dominated and premature directions

- **Stay unchanged is dominated on the available case facts.** It is cheapest, but the actor explicitly says the current five-flow cap, lack of native API access, unavailable Professional-edition apps, and lack of Visualforce pages block needed automation and integration. Doing nothing does not meet the stated direction of travel.
- **A full internal build is not decision-ready.** The actor raised it, so it is retained as a question, but there is no requirements inventory, engineering capacity, security/operations plan, or cost evidence. It is excluded from the serious option set rather than assigned invented economics.
- **Zoho One, Creatio, and Attio are names to screen later, not current serious options.** The actor named them but supplied no fit evidence, quote, or tested workflow. Expanding into three more platform investigations would enlarge rather than resolve this fixed decision.
- **An unnamed external workaround is not a separate option.** No specific product or bounded function is supplied. The narrow API add-on path is the only documented workaround that can be evaluated now.

### What cannot yet be concluded

No platform winner is defensible. Current evidence supports a reversible sequence: first make one critical workflow explicit; then test whether Professional plus API can execute it, whether Enterprise uniquely unlocks it, and whether HubSpot can reproduce it. Do not sign a multi-year upgrade or migration commitment before that discriminator and written commercial terms exist.

## B. Case facts

Only actor statements from the fixed r/CRM thread are treated as case facts.

| ID | KNOWN case fact | Decision relevance |
|---|---|---|
| K1 | The business has used Salesforce since 2019, starting with one license. | Establishes accumulated configuration and switching exposure. |
| K2 | It now has 12 people and the whole company uses Salesforce. | Establishes current scope; role-specific license needs remain unknown. |
| K3 | Salesforce is heavily customized, is not a stock sales pipeline, and is the system of record for a specific operating model. | Makes data-model and behavior conversion central. |
| K4 | The business needs more automation, cross-platform integration, and less friction to keep scaling. | Staying unchanged fails the stated need. |
| K5 | The actor reports Professional Edition is capped at five active flows. | Current automation ceiling. |
| K6 | The actor reports no native API access and a quoted $25/user/month API add-on. | Defines a potentially narrow stay-path remedy. |
| K7 | The actor reports current per-license cost of roughly $50–75 and total current spend of roughly $8,000–$10,000/year. | Historical/current case economics; not assumed to be today's public list price. |
| K8 | The actor reports Enterprise at $165–$175/user/month and describes it as the route to API access and far more flow capacity. | Historical quote/belief; current official list and capability evidence are checked separately. |
| K9 | The actor says third-party subscriptions include dialer, call recording/transcription, accounting sync, LLM integration, and forms; Formstack quoted $4,800/year. | Shows total stack cost, but quantities and must-have status are unknown. |
| K10 | The actor says workflows are deeply dependent on Salesforce and expects migration to involve trade-offs and pain. | Raises workflow rebuild and disruption risk. |
| K11 | HubSpot is the principal named comparison; the actor also asks about Zoho One, Creatio, Attio, and others. | Bounds the migration option used here to HubSpot; other names lack enough evidence. |
| K12 | The actor says a $70,000–$100,000 annual CRM cost is unaffordable at 12–24 people. | Establishes an affordability boundary, but not the components behind that all-in range. |
| K13 | In a follow-up, the actor identifies four blockers: five-flow cap, $25/license/month APIs, some third-party apps unavailable on Professional, and no Visualforce pages. | Defines the feature questions a stay/upgrade quote must answer. |
| K14 | The actor asks when an in-house build stops being a bad idea. | Permits retaining build as an unresolved question, not recommending it. |

The thread does **not** supply renewal date, contract end date, object/field/relationship inventory, active workflow definitions, record volume, integration topology, permission model, report inventory, administrator capacity, acceptable downtime, implementation quotes, or role-by-role seat needs.

## C. Option matrix

| Serious option | Recurring economics | Workflow fit | Switching / implementation burden | Reversibility and lock-in | Main decision-sensitive unknown |
|---|---|---|---|---|---|
| **1. Professional + Web Services API; negotiate renewal** | Lowest supportable Salesforce scenario: actor's current $8k–$10k/year plus documented $25/user/month API product. Exact renewal price unknown. | Preserves all current configuration; enables documented API access. Still subject to five active flows per flow type. App eligibility and Visualforce need remain unverified. | Low relative to migration, but any externalized automation still has design, monitoring, and vendor burden. | Most reversible near-term path; may deepen dependence on workarounds. Contract term unknown. | Can the next required automations fit within five active flows per type or be moved safely outside Salesforce without breaking required apps/pages? |
| **2. Salesforce Enterprise; negotiate price/term** | Current public list is $175/user/month billed annually. Actor's actual quote, discount, add-ons, term, and renewal cap unknown. | Preserves the current org; API is included and documented flow limit rises to 2,000 active flows per type. This does not itself prove every required app, Visualforce behavior, or Agentforce value. | Lower behavior-conversion risk than migration, but upgrade testing and administration remain. | Easy technically relative to migration; commercial reversibility may be low under the multi-year agreement the actor reports being offered. | What exact needed capability beyond API and flow count requires Enterprise, and what is its written three-year price at 12 and 24 seats? |
| **3. HubSpot Enterprise after workflow parity test** | Current Sales Hub Enterprise starts at $150/full Sales seat/month plus $3,500 required onboarding. Actual mix of full, core, and view-only seats and other Hubs/add-ons is unknown. | HubSpot documents Enterprise custom objects, workflows, imports, and Salesforce custom-object sync. Lookup-field mappings on Salesforce custom objects cannot be mapped directly and association behavior has constraints. Private workflow parity is unproven. | Highest immediate burden: data plus operating behavior, automation, integrations, reports, permissions, training, rehearsal, and cutover. No defensible dollar estimate is possible from public facts alone. | Migration is reversible only with retained export, cutover, and rollback provisions; rebuilding creates new platform-specific dependence. | Can one representative critical custom-object workflow, including its integration and exceptions, run end-to-end without a material regression? |

### Conditional decision structure

- **IF** the critical workflow can run on Professional with the Web Services API add-on and the remaining edition gaps are nonessential, **then Option 1 strengthens** because it preserves the customized system with the lowest visible recurring platform cost.
- **IF** the workflow requires the higher documented flow allocation or another verified Enterprise-only capability, and a written three-year quote stays below the actor's affordability boundary, **then Option 2 strengthens**.
- **IF** HubSpot reproduces the critical custom-object workflow and integration without material loss, and a bounded migration quote plus recurring subscription beats the accepted Salesforce envelope over three years, **then Option 3 strengthens**.
- **IF** none of those facts is verified, **do not commit yet**. A discount cannot cure missing functionality, and a lower license price cannot cure workflow failure.

## D. Three-year economics

### Supported recurring-price scenarios

These are exposure bands, not TCO totals. They exclude tax, existing and future third-party apps, implementation, training, internal administration, migration, downtime, and negotiated terms.

| Option / scenario | Evidence class and calculation | Three-year visible amount | What drives the range | Decision sensitivity |
|---|---|---:|---|---|
| Stay unchanged, 12 seats throughout | **ESTIMATED:** KNOWN current total spend $8k–$10k/year × 3. | **$24,000–$30,000** | Actor's reported spend; assumes no seat or price change. | Not choice-worthy despite low cost because it leaves stated blockers unresolved. |
| Stay unchanged, 24-seat equivalent throughout | **ESTIMATED:** double the actor's current 12-person total, then × 3. | **$48,000–$60,000** | Assumes cost scales linearly and all 24 people need equivalent access. | Illustrative ceiling only; role mix and growth timing can materially lower it. |
| Professional + API, 12 seats throughout | **ESTIMATED:** current $8k–$10k/year + PUBLIC FACT API add-on $25 × 12 × 12 months; then × 3. | **$34,800–$40,800** | Current contract price plus all-user Web Services API licenses. | Strong if it solves the workflow gap; weak if the flow/app/page limits remain binding. |
| Professional + API, 24-seat equivalent throughout | **ESTIMATED:** doubled current base $16k–$20k/year + $25 × 24 × 12; then × 3. | **$69,600–$81,600** | Linear seat scaling and all-user API assumption. | Highly sensitive to seat roles, growth timing, and actual renewal quote. |
| Salesforce Enterprise, 12 seats throughout | **ESTIMATED public-list scenario:** PUBLIC FACT $175 × 12 × 36 months. | **$75,600** | Current list price; assumes 12 paid Enterprise users for all three years. | A negotiated quote could lower it; add-ons/services could raise it. |
| Salesforce Enterprise, 24 seats throughout | **ESTIMATED public-list scenario:** $175 × 24 × 36 months. | **$151,200** | All 24 users at list for all three years. | Growth timing and discount dominate. This is not an actor quote. |
| HubSpot Sales Hub Enterprise, 12 full Sales seats | **ESTIMATED public-list scenario:** PUBLIC FACT $150 × 12 × 36 + $3,500 onboarding. | **$68,300** | All 12 require full Sales Enterprise seats; one onboarding fee. | Seat-type mix can lower it; extra Hubs, credits, apps, or services can raise it. |
| HubSpot Sales Hub Enterprise, 24 full Sales seats | **ESTIMATED public-list scenario:** $150 × 24 × 36 + $3,500. | **$133,100** | All 24 require full Sales Enterprise seats for all three years. | Highly sensitive to role mix and growth timing; migration cost is still excluded. |

### What the numbers do and do not show

At 12 static seats, current public list inputs put the visible three-year HubSpot Enterprise subscription plus onboarding **$7,300 below** Salesforce Enterprise list ($68,300 versus $75,600). At 24 static seats the visible difference is **$18,100** ($133,100 versus $151,200). These arithmetic gaps are not savings claims: a migration whose cash cost and disruption exceed the gap loses on this narrow horizon, while a mixed HubSpot seat model or negotiated Salesforce price can move the threshold materially.

The Professional + API scenario is visibly cheaper than either Enterprise list scenario, but it only wins if it actually resolves the blocked workflow. At 12 static seats, its visible three-year gap below Salesforce Enterprise is roughly **$34,800–$40,800**. That gap is the maximum visible room for workarounds and remaining add-ons before the narrow recurring-price advantage disappears; it is not a budget recommendation.

No complete three-year TCO is defensible. The decisive missing quantities are the actual seat ramp and role mix, written Salesforce terms, exact HubSpot package, current third-party stack, workflow rebuild scope, implementation quote, internal effort, and disruption. Commenter anecdotes are not used to fill those holes.

### Estimate discipline

- **Drivers:** seat count, seat type, growth timing, negotiated price, add-ons, object/workflow complexity, integrations, reports, permissions, data quality, and acceptable cutover risk.
- **Why these ranges/scenarios are reasonable:** each arithmetic scenario uses either the actor's stated current spend or a current first-party list price and only the actor's stated 12–24-person boundary. No labor rate or migration duration is invented.
- **Sensitivity:** workflow failure overrides a price advantage; negotiated terms can erase the public-list gap; a migration cost above the visible list-price gap can reverse the three-year economic comparison.

## E. Workflow-fit and migration-risk analysis

The case identifies categories of need, not executable workflow specifications. “Essential” below therefore means essential to validate, not proven must-have behavior.

| Validation surface | Professional + API | Salesforce Enterprise | HubSpot Enterprise | Could reverse the choice? |
|---|---|---|---|---|
| Custom-object system of record | Existing model is preserved. Exact object/relationship limits are not inventoried. | Existing model is preserved, reducing behavior-conversion risk. | Custom objects are documented, but must be recreated; Salesforce custom-object lookup fields cannot be mapped directly and associations have stated constraints. | **Yes.** A critical relationship or lifecycle that cannot be reproduced can stop migration. |
| Automation | Existing flows remain; official limit is five active flows per flow type. External API automation may help but introduces another runtime and operating owner. | Official limit is 2,000 active flows per type; existing flow behavior still needs regression testing after any changes. | Workflows are documented and custom objects can participate, subject to subscription and relationship requirements. Existing Salesforce automations must be documented and rebuilt. | **Yes.** If the needed automation cannot fit Professional or cannot be reproduced in HubSpot, that path fails. |
| Integrations / third-party apps | Web Services API can be purchased; some partner apps may use vendor-provided API tokens. Actor says certain needed apps are unavailable, but does not name them. | API access is included by default. Required app availability remains unverified. | Native Salesforce import/sync is documented; complex/custom migration may require APIs or third-party integrators. Each named accounting, calling, forms, and AI dependency still needs an exact compatibility check. | **Yes.** One nonreplaceable operational integration can determine the platform. |
| Pages / user interface | Actor reports no Visualforce pages; whether a page is actually required is unknown. | Capability and migration impact must be confirmed against the actor's current edition and page requirement; no conclusion is inferred here. | Any Salesforce-specific UI must be redesigned, not copied. No public case detail supports a parity claim. | **Potentially.** Only if the missing page supports a critical scenario. |
| Reports, permissions, history, attachments | Preserved, subject to any workaround's access model. | Preserved, but edition/permission changes require testing. | HubSpot's migration guidance explicitly calls for report inventory/rebuild; public documentation does not prove parity for the actor's reporting, sharing, audit, or attachment needs. | **Yes.** Compliance, permission, or historical-data requirements could block migration. |
| Training and disruption | Lowest likely change burden, but external automation adds support burden. | Moderate change relative to current behavior; implementation scope unknown. | Highest likely change burden because behavior, not only rows, changes. No dollar or duration estimate is defensible without an inventory. | **Yes.** Low tolerance for downtime or no internal owner can favor staying. |

### What must be rebuilt under migration

At minimum, a migration would have to inventory and either reproduce, redesign, or retire the custom objects and associations, flows and triggers, integration behaviors, reports, permissions, forms/pages, historical records and activities, and user operating scenarios. HubSpot's own migration page separates records, integrations, automation, and reports and says complex/custom data can require APIs or third-party integrators. That is evidence of work categories, not evidence of this case's cost or duration.

## F. Prioritized decision-sensitive unknowns

| Priority | UNKNOWN / VERIFY | Why it matters / options discriminated | Cheapest credible verification |
|---:|---|---|---|
| 1 | The single highest-value workflow's objects, relationships, trigger, side effects, integration, exception paths, owner, and expected output. | Discriminates all three options. Without it, “five flows,” “API,” and “custom objects” cannot be translated into fit. It can reverse every direction. | Actor writes one acceptance scenario and an anonymized representative record set. |
| 2 | A written Salesforce entitlement and commercial quote at 12 and 24 seats for Professional + Web Services API and Enterprise, including term, renewal cap, app access, flow allocation, and required page capability. | Discriminates Options 1 and 2 and sets the price migration must beat. Negotiated pricing is not public. | Ask the account executive for one side-by-side written quote with the listed fields. |
| 3 | HubSpot parity for the priority workflow, especially custom-object associations/lookup semantics and the critical integration. | Discriminates Option 3. A failed relationship or exception path can block migration regardless of list price. | Run one anonymized end-to-end proof in a trial/sandbox or vendor-led technical session; record pass/fail against the scenario. |
| 4 | Role-by-role access needs at 12 and 24 people. | Changes both vendors' seat economics and may reverse the public-list comparison. | Map each role to required actions and obtain the corresponding seat type in both written quotes. |
| 5 | Migration inventory and bounded implementation/cutover quote. | Determines whether HubSpot's recurring-price difference survives one-time switching cost and whether disruption is acceptable. | After workflow parity passes, give one vendor/partner the inventory and request a phased fixed-scope quote with assumptions. |
| 6 | Existing third-party annual spend and which dependencies are mandatory, replaceable, or bundled in each option. | Actor's all-in affordability concern includes more than CRM seats; omitting it can reverse the comparison. | Export the last 12 months of CRM-adjacent contracts into a one-page cost/owner/renewal list. |
| 7 | Contract and renewal timing, termination terms, data-export rights, and rollback window. | Controls leverage, lock-in, and the practical ability to test or migrate. | Read the order form and master terms; extract four dates/clauses. |

The first three unknowns dominate. The remaining four improve the economics only after a workflow is concrete enough to test.

## G. Exactly one primary next validation action per serious option

| Serious option | One primary next action | What a useful result contains |
|---|---|---|
| **1. Professional + API; negotiate renewal** | **Obtain a written Professional-renewal quote that names the Web Services API product and confirms, for 12 and 24 seats, its price plus the exact flow, required-app, and page entitlements.** | A dated orderable configuration, not an oral “API add-on” assurance. |
| **2. Salesforce Enterprise; negotiate price/term** | **Obtain a written three-year Enterprise quote at 12 and 24 seats with discount, required products, commitment, renewal cap, and termination terms.** | A comparable cash schedule and lock-in boundary. |
| **3. HubSpot Enterprise migration** | **Execute one anonymized end-to-end parity test of the actor's highest-value custom-object workflow, including its critical integration and exception path.** | A documented pass/fail against expected state changes and output, not a canned demo. |

## H. Evidence and freshness

### Actor evidence

| ID | Source | Used for | Source state | Checked |
|---|---|---|---|---|
| A1 | [Original r/CRM case — “Small business outgrowing Salesforce Professional”](https://www.reddit.com/r/CRM/comments/1vmybl6/small_business_outgrowing_salesforce_professional/) | K1–K14, including the actor's follow-up blocker list | Public thread dated 13–16 Aug 2026 | 2 Sep 2026 |

No commenter claim is used as a case fact, migration estimate, negotiation fact, or recommendation.

### Current first-party evidence

| ID | Authoritative source | PUBLIC FACT supported | Source state / date | Checked |
|---|---|---|---|---|
| S1 | [Salesforce Sales Cloud pricing](https://www.salesforce.com/sales/cloud/) | Enterprise public list price is $175/user/month, billed annually; Pro Suite public list is $100/user/month. | Current page | 2 Sep 2026 |
| S2 | [Salesforce editions with API access](https://help.salesforce.com/s/articleView?id=000005140&language=en_US&type=1) | Enterprise includes API access; Professional does not include it by default but can buy the Web Services API product; Additional API Calls does not enable API access. | Published 7 Jul 2026 | 2 Sep 2026 |
| S3 | [Salesforce add-on pricing PDF](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/pricing/all-add-ons.pdf) | Web Services API is $25/user/month, billed annually, for Pro Suite/Professional and included in Enterprise/Unlimited. | Current 2026 PDF | 2 Sep 2026 |
| S4 | [Salesforce General Flow Limits](https://help.salesforce.com/s/articleView?id=platform.flow_considerations_limit.htm&language=en_US) | Professional: five active and five total flows per flow type; Enterprise: 2,000 active and 4,000 total per type. | Current Help page | 2 Sep 2026 |
| H1 | [HubSpot Sales Hub pricing](https://www.hubspot.com/pricing/sales?tier=enterprise) | Sales Hub Enterprise starts at $150/seat/month; required Enterprise onboarding is $3,500. | Current page; promotional prices also displayed, not used | 2 Sep 2026 |
| H2 | [HubSpot Product & Services Catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog) | Sales Hub is seat-priced with no minimum for new customers; full Enterprise functionality requires Sales Enterprise seats; view-only access is distinct. | Current catalog | 2 Sep 2026 |
| H3 | [HubSpot custom-object documentation](https://knowledge.hubspot.com/object-settings/create-custom-objects) | Enterprise subscriptions can create custom objects and use them with workflows/reports; object/property limits apply. | Updated 12 Jun 2026 | 2 Sep 2026 |
| H4 | [HubSpot Salesforce custom-object sync](https://knowledge.hubspot.com/salesforce/set-up-and-use-salesforce-custom-object-sync) | Enterprise can sync Salesforce custom objects; objects must first exist in HubSpot; lookup-field mapping and association constraints apply. | Updated 11 May 2026 | 2 Sep 2026 |
| H5 | [HubSpot Salesforce import documentation](https://knowledge.hubspot.com/salesforce/import-salesforce-records) | Standard and custom Salesforce records can be imported; sync behavior has requirements and limitations. | Updated 12 May 2026 | 2 Sep 2026 |
| H6 | [HubSpot's Salesforce migration process](https://www.hubspot.com/switch-from-salesforce) | Migration work categories include records, integrations, automation, and reports; complex/custom data may need APIs or third parties. | Current vendor page | 2 Sep 2026 |

### Evidence limitations

- The actor's prices and quote are historical case facts; they are not substituted for current list prices.
- Public list prices do not reveal the actor's negotiated price, package, taxes, discounts, or renewal terms.
- Vendor documentation establishes available capabilities and stated limits, not parity for a private customized org.
- HubSpot's migration page is vendor-authored process evidence, not an independent assurance of effort, duration, “no loss,” or success. Its promotional claims are not used in the conclusion.
- Salesforce public documentation confirms API and flow facts but does not answer the actor's unnamed third-party-app or unspecified Visualforce requirement.
- No affiliate comparison page, SEO listicle, generic TCO calculator, or commenter anecdote controls this brief.

## I. Boundaries

This artifact:

- is a disposable decision aid for one fixed public case, not a universal CRM ranking;
- is not a CRM implementation plan or migration guarantee;
- does not inspect or access the actor's private Salesforce instance;
- cannot verify undocumented custom behavior, workflow importance, data quality, permissions, or edge cases;
- does not know negotiated prices, contract terms, or implementation quotes unless the actor supplies them;
- does not treat public list-price arithmetic as complete TCO;
- represents modeled scenarios as **ESTIMATED** and missing facts as **UNKNOWN / VERIFY**;
- does not recommend or assess Agentforce, an internal build, or unnamed tools without case-specific evidence;
- does not contact the actor, reply to the thread, or perform migration work.

## Decision-space-reduction result

**This resolution reduced the decision space; it did not merely organize information.**

It made four reductions:

1. eliminated “stay unchanged” because it cannot satisfy the actor's stated automation/integration need;
2. removed internal build, unnamed external tooling, and three untested vendor names from the immediate serious option set without claiming they are universally bad;
3. showed that negotiation is a commercial layer on two Salesforce configurations, not an independent workflow solution;
4. converted the broad “which CRM?” question into three option-specific tests dominated by one shared discriminator: an executable critical-workflow definition, followed by written Salesforce terms and a HubSpot parity result.

The artifact does not choose a winner. It identifies a reversible next sequence and prevents a seat-price comparison from masquerading as a migration decision.

## Internal validation log

| Check | Result | Material issue found and correction |
|---|---|---|
| **V1 — Case fidelity** | PASS | The draft risked treating the actor's “unlimited flows” wording as a vendor fact. Corrected to the documented 2,000 active flows per flow type. Commenter migration and negotiation anecdotes were excluded. |
| **V2 — Public-fact fidelity** | PASS | The actor's $165–$175 Enterprise quote was separated from today's $175 public list. The API-enablement product was corrected to **Web Services API**; Salesforce explicitly says Additional API Calls does not enable Professional API access. |
| **V3 — Estimate discipline** | PASS | No migration labor, duration, or arbitrary internal rate was invented. Every monetary scenario states its inputs, exclusions, drivers, and reversal sensitivity. |
| **V4 — Unknown discipline** | PASS | Workflow definition, entitlements, negotiated terms, seat mix, migration scope, stack cost, and contract timing remain visible. The first three are flagged as capable of reversing the choice. |
| **V5 — Decision usefulness** | PASS | The brief opens with the decision, bounds three serious options, eliminates premature paths, gives exactly one primary action per serious option, and states conditional decision rules. |

## Final experimental verdict

**A — DECISION-READY RESOLUTION PRODUCED.**

The public case and current first-party evidence were sufficient to produce a case-faithful, evidence-linked brief that exposes rather than hides material uncertainty and materially narrows the decision. “Decision-ready” here means ready to direct the next evidence-gathering action; it does not mean ready to sign a CRM contract.
