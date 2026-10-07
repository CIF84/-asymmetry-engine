# Experiment 053 — Engine-State and Funnel Semantics Audit

## 1. Verdict

**B — PARTIAL SEMANTICS; DATA-CONTRACT REPAIR FIRST. [DERIVED]**

Existing evidence supports historical run summaries, named chain histories, and explicitly partial distributions. It does not support a complete deduplicated opportunity population, current lifecycle totals, or current attention load. The Engine-level question is useful, but an inventory/funnel UI would currently give these missing denominators unwarranted authority. Repair the manual evidence contract before a new Engine-state UI experiment; no software is earned.

## 2. Repository baseline

**[RECORDED]** Synchronized `main` / `origin/main`: `71c28d2568c95958d0ef9b3b3ba86f8069e928a2`, after a normal fast-forward containing SPEC-053 and its `READY_FOR_EXECUTION` activation. Experiment 052's published closure and publication-state update remain in ancestry. Execution moved STATUS to `IMPLEMENTING` under the operating protocol. Pre-existing untracked `.DS_Store` files are unrelated and preserved.

Contract: [SPEC-053](../../specs/053-engine-state-funnel-semantics-audit.md). This artifact and the mechanical STATUS transition are the only permitted changes.

## 3. Active time and timing method

**[RECORDED]** Prospective start: `2026-10-07T08:46:28Z`, immediately after synchronization and before evidence reconstruction. One continuous repository-only interval covers reading, semantic reconstruction, writing, and integrity/test freeze. The completed timing record below supplies the end and elapsed duration; Git commit timestamps are not used as active-time telemetry. No observation window or human approval wait occurred during the timed interval.

The run stops below the target if identity gaps, metric supportability, memory recoverability, and the implementation gate are decisive; it does not fill the 20–40 minute target artificially. Hard ceiling: 60 active minutes.

## 4. Spend

**[RECORDED]** Incremental external spend: **€0**. **[UNKNOWN]** Compute/model/credit cost is not exposed and is not represented as zero.

## 5. Isolation confirmation

**[RECORDED]** Repository-only audit. No live web research, source acquisition, RADAR, actor contact, regulatory freshness check, platform interaction, or publication occurred. No new opportunity was created. No UI, software, schema, database, counting logic, monitor, scheduler, policy, or protocol was implemented. Existing specifications, experiments, frozen 051/052 artifacts, living documents, source, tests, and schema are preserved.

## 6. Evidence horizon and reconstruction quality

**[DERIVED]** Economic/opportunity evidence horizon is through Experiment 052, with each chain retaining its own earlier last observation. The October 7 contract date does not refresh September actor or regulatory facts. Reconstruction is targeted, not a census.

Evidence priority: original result/final-observation records; checkpoints when early results are not present as standalone artifacts; cross-experiment audits; frozen representation fixtures as derived interpretations; specifications only for intent and boundaries. In this audit, **RECORDED** means explicitly preserved in the repository, not independently reverified in the external world. **DERIVED** marks a calculation or semantic interpretation from that record. **ESTIMATED** retains approximate source measurements. **UNKNOWN** means absent or insufficient support, never zero.

Primary source map:

| Source | Use and limit |
|---|---|
| [README](../../README.md), [Roadmap](../../ROADMAP.md), [Operating Model](../../docs/OPERATING_MODEL.md) | Current implemented boundary and non-linear research policy; no inventory denominator |
| [Opportunity Model 001–035](../../docs/OPPORTUNITY_MODEL_001_035.md) | Anatomy, gates, evidence ladder; historical document predates final 030/035 outcomes |
| [Economic Telemetry Baseline](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md) | Partial telemetry and run counts; explicitly censors 030/035 at initialization |
| [001–019 checkpoint](../../docs/LEARNING_CHECKPOINT_001_019.md), checkpoints [020](../../docs/LEARNING_CHECKPOINT_020.md), [021](../../docs/LEARNING_CHECKPOINT_021.md), [022](../../docs/LEARNING_CHECKPOINT_022.md), [023](../../docs/LEARNING_CHECKPOINT_023.md), [024](../../docs/LEARNING_CHECKPOINT_024.md), [027](../../docs/LEARNING_CHECKPOINT_027.md), [028](../../docs/LEARNING_CHECKPOINT_028.md) | Early chains and selected batch totals; not complete row-level inventory |
| [031](../031/radar-compounding-test.md), [032](../032/actor-observable-decision-surface-discovery.md), [046](../046/fresh-opportunity-discovery-aligned-interaction-policy.md) | Detailed candidate/disposition ledgers and run-level denominators |
| [030 final record](../030/interaction-record.md), [035 final record](../035/superset-actor-facing-resolution-test.md), [043 provenance audit](../043/interaction-topology-and-agency-provenance.md) | Delivery, exposure, authority, authorship, decision-state effect remain separate |
| [047](../047/realtime-migration-discriminator-feasibility-check.md), [048](../048/bounded-realtime-migration-evidence-request.md) | Same carried candidate, actor-held discriminator, repeated attempts, final delivery ambiguity |
| [050 economic audit](../050/economic-distance-to-value-audit.md) | Chain frontiers and economic evidence limits; experiment-intent counts are not opportunity counts |
| [051 fixtures](../051/opportunities.js), [052 control fixtures](../052/viewer/control-fixtures.js), [052 approved evidence](../052/human-acceptance-evidence.md), [052 debrief](../052/debrief.md) | Historical sample lifecycle/control semantics and operator need; synthetic scenarios excluded |
| [models.py](../../src/asymmetry_engine/models.py), [db.py](../../src/asymmetry_engine/db.py), [038](../038/revision-aware-observation-persistence.md), [Architecture](../../ARCHITECTURE.md) | Implemented source-item/capture identity and run accounting; no opportunity-state tables |

**[RECORDED]** A filesystem search including ignored files, excluding `.git` and `.venv`, found no `.db`/`.sqlite*` file in this checkout. No database was opened or initialized: the Repository constructor can create/migrate tables. Schema/source inspection establishes capability only; absence of a local database says nothing about all historical runs or other checkouts.

## 7. Signal identity finding

**[RECORDED]** Implemented logical source identity is `(source_id, external_id)`; capture identity adds positive `capture_sequence`, local `observation_id`, and `pipeline_run_id`. Unchanged payload recapture is suppressed; materially changed payload appends a revision; latest readers select the highest sequence. Capture count, unique logical item count, fetched count, and changed-item count are different units.

**[DERIVED]** This identifies source records, not cross-source economic signals or decisions. The same event may appear in different sources; one source item may reveal multiple hypotheses; several items may concern one decision. A raw RADAR signal is a manually screened entry, not necessarily a persisted SourceObservation. Signal-level cross-source equivalence and the link from manual research to stored observations are **UNKNOWN**.

## 8. Candidate identity finding

**[RECORDED]** Candidates have run-local labels such as `031:C03`, `032:C03`, and `046:C10`; their numeric suffixes are not globally meaningful. Experiment 032 has ten qualifying candidates labeled C02–C11, not eleven candidates. Formation thresholds change: familiar hypotheses in 021, signal-native hypotheses in 022, and actor-observable candidates in 032 are not one uniform admission rule.

**[DERIVED]** Candidate identity should preserve a hypothesis attempt and its parent signals/run, with an explicit same-referent relation if rediscovered. Recurrence is allowed; discovery count is not unique-opportunity count. There is no durable global candidate identity or repeat-discovery ledger today. The ledger below retains existing local labels without minting production IDs.

## 9. Opportunity identity finding

**[DERIVED]** The stable conceptual referent needs an actor or explicitly scoped actor class, a decision instance/horizon, a bounded thesis/residual job, and a relation to its broader opportunity family. Evidence, blockers, experiments, and reactivation may change while that referent persists. A materially different actor/decision or changed residual job may be a new instance or thesis even within the same family; a URL or market category alone cannot settle equivalence.

**[RECORDED]** The six 051 fixture IDs name historical chains consistently, but they are experimental representation identifiers, not a canonical inventory registry. Cocoa and Canadian rows describe actor-class propositions; CRM, Superset, and realtime trace particular actor decisions. Counting these indiscriminately as six equivalent commercial opportunities would hide a family/instance mismatch.

**[DERIVED]** Stable chain reconstruction is possible for selected records. Stable global opportunity identity, admission boundaries, merge/split rules, and deduplication across all discoveries are not yet supportable. This audit creates no canonical opportunity identities.

## 10. Experiment-versus-opportunity finding

**[RECORDED]** Canadian 023–027, CRM 028–030, Superset 032–035, and realtime 046–048 each carry one identifiable branch through multiple experiments. Experiment 032 also examines ten candidates. Experiment 048 contains three authorized execution attempts and a later status check on the same fixed referent.

**[DERIVED]** Experiments are evidence jobs; attempts are execution events; signals are inputs; benchmark cases are tests. None are opportunity identities. The 20 tariff benchmark cases in 024, 12 lines in the 025 brief, ten EV configurations in 019, or 49 experiment-intent rows assessed in 050 must not become opportunity counts. 051/052 represent earlier chains rather than adding new economic opportunities.

## 11. Evidence/progression-state finding

**[DERIVED]** Use an evidence frontier/ledger, not one obligatory stage. Retain observed signal, formed hypothesis, gates tested/survived/untested, bounded gap, constructibility, decision-ready resolution, delivery, exposure, semantic engagement, authority, authorship provenance, decision-state effect, downstream action, economic effect, exchange/WTP, transaction, repeatability, and capture independently. A later observation may support an earlier fact retrospectively; it does not fill other missing states.

**[RECORDED]** Canadian 025, CRM 029, and Superset 034 reached decision-ready resolution. Superset 035 reached one material public decision-state refinement under the fixed proposal-author account; 043 preserves authorship provenance as UNKNOWN. CRM delivered publicly but exposure/effect remained UNKNOWN. Realtime never obtained the bounded matrix and delivery remained UNKNOWN. 050 records no established economic effect, WTP, transaction, repeatability, or value capture. These are documented frontiers, not proof that no private effect ever occurred.

## 12. Lifecycle-state finding

**[DERIVED]** ACTIVE / DORMANT / REVIEW / TERMINAL remains coherent if it describes disposition of a specified thesis at a stated horizon, independently of how much evidence it accumulated. ACTIVE needs an evidenced pursued/live thesis within its horizon and grants no execution authority; DORMANT needs a contingent obstacle and conditional reopening; REVIEW preserves unresolved classification or stale state; TERMINAL applies to the tested thesis/job, not every possible opportunity in that sector.

**[DERIVED from RECORDED fixtures]** In the curated six-row 051 sample: ACTIVE **0**, DORMANT **4**, REVIEW **1**, TERMINAL **1**. This is a sample snapshot, not current Engine inventory. Four dormant fixture rows do not establish that AE currently has four dormant decision instances; the CRM row's future reactivation explicitly requires a new live case. No transition timestamps or authoritative latest lifecycle record exist for the whole population.

## 13. Operational/control-state finding

**[RECORDED]** 052's historical entries show three DORMANT controls, two NO ACTION controls, and one BLOCKED / NO ACTION AVAILABLE control. Its four synthetic scenarios exercise decision, authorization, progression, and waiting. The two synthetic attention cards are not two actual pending Engine decisions.

**[DERIVED]** Control is a dated task/authority requirement, not lifecycle or value. Superset can be lifecycle REVIEW with NO ACTION within its closed contract; realtime can be DORMANT and operationally BLOCKED. Current real attention load across opportunities is UNKNOWN. STATUS establishes the active repository work packet, not a complete opportunity-task queue; neither “one active experiment” nor “zero historical attention cards” supplies an Engine-wide attention count.

## 14. Terminal-versus-contingent disposition finding

**[DERIVED]** Historical KILL/PARK labels are dispositions of a bounded experiment/hypothesis, not universal permanent economic death. Preserve the original verdict, its gate/reason, and a separately sourced semantic interpretation.

| Evidence | Audit interpretation [DERIVED] | Reopening boundary |
|---|---|---|
| EV 020: BecSpec adequately resolves the same job | Terminal tested residual-resolution thesis | Materially different unresolved job/thesis or independently changed adequate-resolution evidence; no feature-expansion rescue |
| Canadian 027: correct resolution, inaccessible independent actor surface | Contingent access/distribution dormancy | Legitimate reachable still-live importer context under new scope |
| Cocoa 014: valid exposure not executable | Contingent execution/access blocker | Valid authenticated exposure; invalid test is not demand failure |
| CRM 030: public delivery, exposure UNKNOWN | Closed measurement-limited instance; family-level dormant interpretation | New live case with designed exposure/effect path; no reopening old actor interaction |
| 032 C08/C09: platform prohibits AI comments; sensitive/private state | Contingent control plus recoverability constraints | Separately authorized legitimate path and sufficient evidence; no bypass assumed |
| 032 C05: production HA advice requires benchmarks/qualified review | Contingent feasibility/control blocker | Bounded requirements, workload/failure tests, qualified review |
| 046 C03: closed consultation | Terminal historical submission window | A new window is a new decision instance, not revival of the expired deadline |
| 031 C04 / 046 C12: insufficient consequence/context | Review/unresolved for the broad economic possibility | New decisive evidence; do not treat missing support as proven absence of value |

No historical verdict is rewritten. Reactivation is neither automatic authorization nor automatic identity creation.

## 15. Opportunity Memory recoverability

**PARTIAL overall [DERIVED]**, with strong selected chain histories and weaker early/raw-stage coverage. Recoverability is graded against the requested fields, not against record length.

| Memory field | Selected chains / detailed later ledgers | Broader history / limitation |
|---|---|---|
| Referent/name and thesis | STRONG in six chains and named 031/032/046 attempts | PARTIAL for early category summaries and anonymous actor classes |
| Original signal / source | STRONG for CRM, Superset, realtime and many later candidate links | PARTIAL: 031 raw signals summarized by family; early results often only consolidated |
| Historical disposition / reason / evidence | STRONG for final chains and detailed kill tables | PARTIAL for batch totals, evolving gate labels, and discarded pre-formation context |
| Blocker and contingent nature | STRONG in selected chain audits; DERIVED for many kills | PARTIAL: KILL does not preserve a universal terminal/dormant distinction |
| Reactivation condition | Explicit in Canadian 027 and 051 dormant fixture interpretations; reconstructable for some later kills | PARTIAL elsewhere; broad new-signal suggestions do not establish a still-live decision |
| Last horizon / history | STRONG for final 030/035/048 and linked chains | PARTIAL for early rows; state transitions/dwell times usually absent |
| Stable identity across future rediscovery | PARTIAL: human reconciliation possible | No canonical family/instance or merge/split ledger |

**[UNKNOWN]** Whether unpreserved raw observations or conversation-only results can be recovered from some other source. No transcript archaeology or reconstruction of missing evidence is attempted. These limits favor preserving sidelined evidence cheaply, without a database.

## 16. High-confidence opportunity inventory

**[DERIVED]** The following are high-confidence reconstructable historical chain referents. They are not a complete admitted-opportunity population, not uniformly individual actor instances, and not current external states. Names and fixture IDs already exist in 051; this table does not introduce IDs.

| Existing referent | Signal / thesis / chain | Furthest recorded frontier | Historical disposition and last horizon | Blocker / reactivation |
|---|---|---|---|---|
| `cocoa-paid-pilot` | Czech CN18 import evidence → producer purchasing/repricing paid brief; 013→014 | Commercial proposition and paid-pilot instrument; valid exposure absent | 014 D INVALID; consolidated 001–019 checkpoint, 2026-09-02; fixture DORMANT is DERIVED | Authenticated producer exposure; unchanged bounded proposition only after valid access |
| `ev-smart-charging` | Review-derived UK configuration uncertainty; 018→019→020, fixture labels 019→020 | Public configuration feasibility; exact adequate substitute | 020 C FAIL/PARKED; 2026-09-02 checkpoint; fixture TERMINAL is DERIVED | Residual job already served; a genuinely changed thesis must be distinguished |
| `canadian-counter-tariff` | Fresh operational tariff change; known-HS importer decision; 023→027 | Gap benchmarked; decision-ready brief 025 | 027 C PARK; 2026-09-02 checkpoints; fixture DORMANT is DERIVED | Legitimate repeatable pre-decision importer surface; freshness must be re-established |
| `customized-crm` | Named owner's customized Salesforce stay/upgrade/migrate decision; 028→030 | Decision-ready brief; public delivery | 030 D measurement-limited; final observation 2026-09-05; fixture DORMANT is family-level DERIVED interpretation | Exposure unobservable; new live case, not retry of closed interaction |
| `superset-hierarchy` | SIP-225 author sequencing decision; 032 C03→033→034→035 | Decision-ready resolution and material authoritative public refinement | 035 A / REFINEMENT; final observation 2026-09-06; fixture REVIEW is DERIVED | Downstream/economic frontier unproven; no active task follows automatically |
| `realtime-migration` | Fixed production-owner paired qualification/migration uncertainty; 046 C10→047→048 | P2 actor-held bounded discriminator; request submitted, delivery UNKNOWN | Final status check 2026-09-16; fixture DORMANT is DERIVED | Missing matrix and inaccessible/private surface; legitimate observable still-live path plus new authorization |

**[RECORDED]** Additional named historical hypotheses exist beyond these six. The candidate-memory ledger in section 17 reconstructs all **36 run-local candidate entries [DERIVED: 14 + 10 + 12]** in the selected 031/032/046 ledgers, including two entries already linked to the above chains. This expands evidence coverage without counting every hypothesis as an admitted opportunity or asserting a 40-opportunity deduplicated population.

## 17. Ambiguous/partial inventory

**[DERIVED]** Every row below preserves an existing hypothesis attempt. Actor-level instance identity, admission as a material opportunity, and current lifecycle are not inferred merely from naming. T = terminal *tested job/window*; C = contingent blocker; R = unresolved/review; H = historical bounded hold. These are this audit's interpretations, not rewritten source verdicts. For mixed kills, the conditions are retained rather than reduced to one dominant inventory state.

### Detailed later candidate memory

| Existing run-local referent | Original disposition [RECORDED] | Audit interpretation and memory worth retaining [DERIVED] |
|---|---|---|
| 031 C01 GrantScout coverage expansion | KILL / no handoff | C/R: actor-controlled repeat workflow evidence absent; actual usage could change the discriminator |
| 031 C02 Swan Token Plan | KILL | T for another option memo already supplied; a different empirical provider-cost question remains distinct |
| 031 C03 Brandfolder renewal/migration | KILL | C: legitimate reviewer access and private workflow/quote inputs missing |
| 031 C04 Smartcore GridSearchCV | KILL | R: material consequence/user demand insufficiently demonstrated |
| 031 C05 UK DTE supplier watch | KILL | R/C: non-specific notice; later concrete project would define a new instance |
| 031 C06 UAS Industry Day | KILL | T for attend/defer option memo answered by notice; expired event is not dormant forever |
| 031 C07 federal grant eligibility | KILL | T for generic eligibility/search job already served; no specific applicant instance |
| 031 C08 Singapore EDG readiness | KILL | T for public criteria; C for a separate private proposal-readiness question |
| 031 C09 Australian energy-plan switch | KILL | T for usage-input comparison job served by official tool |
| 031 C10 equipment lease/buy | KILL | T for bounded calculator comparison; actor instance/inputs absent |
| 031 C11 vintage ARP 2600 purchase | KILL | C: physical inspection/authenticity and hidden buyer; listing is not the buyer decision |
| 031 C12 Copilot billing response | KILL | T for official mechanics; C for private team usage/access |
| 031 C13 Australian surcharge transition | KILL | T for rules/margin calculation already served; preserve historical regulatory sensitivity, not current law |
| 031 C14 baggage-inclusive airfare | KILL | T for total-cost calculator job; platform-private outcomes limit an AE experiment |
| 032 C02 PEP 842 privacy policy | KILL | T for generic option memo; separate downstream-use evidence question is not the same thesis |
| 032 C03 Superset SIP-225 | ONE BOUNDED UNCERTAINTY | H then carried to 033–035; same chain, not another opportunity |
| 032 C04 Kestra Jackson 3 | KILL | T for additional research memo; next job is an already-defined compatibility spike |
| 032 C05 Proxmox HA storage | KILL | C: requirements, benchmarks, failure domains, staffing and qualified review |
| 032 C06 Rovo OAuth | KILL | T for endpoint/discovery explanation already resolved |
| 032 C07 Jira–GitHub connection | KILL | T for documentation job; product regression/support repair is a different intervention |
| 032 C08 CPG first warehouse hire | KILL / BLOCK | C: platform rule plus role facts; legitimate future evidence path required |
| 032 C09 founder CEO succession | KILL / BLOCK | C/R: private board/leadership evidence and platform rules; no assumed feasible future access |
| 032 C10 Bitbucket recovery | KILL | C: private support authority/retention and outcome visibility; recovery viability UNKNOWN |
| 032 C11 Adelaide pre-dawn travel | KILL | T for transport-choice memo already answered; date-specific new travel is a new instance |
| 046 C01 skills documentation-impact gate | KILL ACTOR/AUTHORITY | C/R: acceptance authority unresolved; visible proposer is insufficient |
| 046 C02 WHATWG partial inclusion | KILL RECOVERABILITY | C/R: multi-implementer compatibility/security evidence exceeds bounded recoverability |
| 046 C03 Drone Strategy consultation | KILL DECISION CLOSED | T for expired consultation window; future window must be identified separately |
| 046 C04 MiCA consultation | KILL UNCERTAINTY | R: no bounded participant-specific decision, not a qualified opportunity |
| 046 C05 PMIS procurement | KILL ACTOR/AUTHORITY | R: missing supplier/fit/bid instance; buyer notice is not supplier identity |
| 046 C06 DMS procurement pipeline | KILL ACTOR/AUTHORITY | R: no observed supplier-owned present decision |
| 046 C07 Azure GPv1→GPv2 | KILL DECISION CLOSED | T for disclosed migration choice already resolved |
| 046 C08 Jira automation allowance | KILL EXACT RESOLUTION | T for transition question already answered |
| 046 C09 Jira data residency | KILL ACTOR/AUTHORITY | C/R: authority, private requirements, compliance evidence absent |
| 046 C10 realtime migration | HOLD ONE BOUNDED DISCRIMINATOR | H then 047 P2/048 delivery UNKNOWN; same chain |
| 046 C11 PAX ERP no-AI positioning | KILL DECISION CLOSED | T for old binary; product evidence showed decision moved on |
| 046 C12 SaaS first customers | KILL UNCERTAINTY | R: product, ICP, channel-attempt baseline absent |

Sources are the candidate and kill/disposition sections of linked 031, 032, and 046 artifacts in section 6. Per-row last horizons are their run dates: 031/032 **2026-09-02**, 046 **2026-09-11**; carried Superset/realtime rows use the later chain horizons in section 16. Reopening conditions above are audit interpretations unless an explicit source next-discriminator is identified; they do not establish that blockers changed.

### Earlier partial referents and non-admitted records

| Preserved referent | Evidence available | Identity / missingness [DERIVED] |
|---|---|---|
| Czech CN75 nickel commercial translation | 013 case scope and 001–019 checkpoint: economically interesting, commercially distant | Broad branch recoverable; actor/decision instance and complete outcome row not preserved here |
| CN28 chemicals / supplier substitution | 013 scope and checkpoint: strong asymmetry, poor operator fit, trust/regulatory burden | Potentially contingent; precise decision, controlling rule, and actual reactivation condition UNKNOWN |
| CN85 solar/battery comparison | 013 scope and checkpoint: appeared crowded | Tested domain recoverable; residual job and exact terminal threshold insufficient for unique instance |
| Czech exact-appliance repair / second quote / replace | SPEC-016 intent plus checkpoint: exact repair-vs-replace intent weak, adjacent repair economics measurable | Thesis narrowing/split ambiguity; do not combine adjacent demand or count twice by guess |
| Old-stock environmental-claim triage | 022 checkpoint: strongest fresh regulatory-transition candidate, same-job commercial products found | Terminal proposed residual job at that horizon; not proof regulation itself blocked it |
| Contradictory bank/merchant payment-dispute state | 022 checkpoint: inaccessible multi-institution decisive facts | Contingent recoverability candidate; actor/event identity and full row ledger incomplete |
| Other 021/022/023/028 hypotheses | Checkpoints preserve batch totals and selected learning | Omitted row-level identities/links not reconstructed from specification expectations |
| Raw records excluded before formation | 032 R01 Flowise archived/read-only; R07 closed OpenDisplay; 046 IETF agenda and Confluence advisory | Observations, not opportunities; keep reasons without inflating candidate/admission counts |

Specifications clarify intended referents, never prove execution. No broad CN category is promoted into a new opportunity in this audit.

## 18. Known historical missingness

**[DERIVED]** Missingness includes incomplete early row ledgers; raw signals retained only as family examples; inconsistent formation/admission definitions; no cross-run dedup map; no explicit family-versus-instance contract; compound kill reasons without normalized terminal/contingent tags; sparse reactivation conditions; incomplete evidence horizons and transition times; no current opportunity task/authority ledger; no observation-to-candidate link; and no complete externally refreshed population.

**[RECORDED]** 031 says thirteen candidates were killed before deepening while recording three deepened among fourteen formed. These cannot establish a consistent shallow/deep partition. Its aggregate formed/killed/deepened counts are retained separately; no eleven-or-thirteen shallow-kill value is repaired by inference. Its headline exact-resolution count is six, although other compound kill rows mention existing guidance; retain that recorded definition rather than silently recoding a larger total.

**[DERIVED]** Older telemetry/model documents intentionally stop 030/035 at initialization; final records and 043 establish the later horizon. Similarly, 048's initial attempt verdicts do not supersede its final delivery ambiguity. A latest *document* is not necessarily the latest evidence for every referent.

## 19. Funnel-versus-state-model finding

**[DERIVED]** The strongest model is a combination: a branching search/experiment history, independent lifecycle disposition, and an evidence frontier with orthogonal control requirements. A portfolio state view is a possible presentation of those semantics, not proof that revenue assets or autonomous portfolio operation exist.

A linear funnel may depict a single preregistered run with compatible units, such as 032 raw→formed→discriminated, but its survivor must not then be counted again as several new opportunities in 033–035. Branches can stop, be censored, split, or revisit evidence. TERMINAL/DORMANT is independent of achieved resolution or actor-effect evidence. Categorical frontier labels must not become an ordered numerical distance or additive score.

## 20. System-count supportability matrix

Classification abbreviations: **C = CURRENTLY DISPLAYABLE**, **H = DISPLAYABLE WITH EXPLICIT PARTIAL/HISTORICAL LABEL**, **N = NOT CURRENTLY SUPPORTABLE**. The display value must include its unit/population/horizon; H never authorizes presenting a complete current Engine number.

| Operator question | Class | Defensible value/example and evidence quality | Required display limit |
|---|---|---|---|
| Signals observed in defined horizon | H; N for all-Engine unique total | 031: 37; 032: 34; 046: 14 raw screened entries [RECORDED] | Separate run horizons/definitions; not unique cross-source signals or SQLite captures |
| Candidates generated | H | 031: 14; 032: 10; 046: 12 [RECORDED]; 36 selected run-local entries [DERIVED] | Candidate attempts, not admitted/deduplicated opportunities |
| Survived fatal gates | H; N for consistent population survival | 032: zero full survivors plus one bounded uncertainty; 046: zero full survivors plus one HOLD; 028: one advanced [RECORDED] | Hold, full survivor and admission are distinct; untested gates retained |
| Became material opportunities | N for system total | Selected branches have consequence/gap evidence [RECORDED], but no uniform admission event | Do not reinterpret all qualifying candidates as material opportunities |
| ACTIVE / DORMANT / REVIEW / TERMINAL | H; N for current totals | Six fixture rows: 0 / 4 / 1 / 1 [DERIVED] | Curated historical chain sample with row horizons and family/instance caveat |
| Decision-ready resolution | H | Three named economic-decision chains: Canadian 025, CRM 029, Superset 034 [DERIVED from RECORDED records] | Audited chain set only; benchmark cases and internal UI milestones excluded |
| Actor/decision effect | H | One established material public decision-state refinement, Superset 035 [RECORDED] | Actor authority scoped; authorship/downstream/economic effect UNKNOWN; not generic success |
| Economic effect | H; N for actual/current total | Zero *documented qualifying economic-effect events identified in the audited chain set* [DERIVED]; outcomes UNKNOWN | “Not established”, never zero real-world value or no effect |
| Exchange/WTP | H; N for actual/current total | One specified paid-pilot intent, cocoa 014 [RECORDED]; zero valid WTP results identified [DERIVED] | Invalid exposure; intent and exchange evidence separate |
| Transaction | H; N for actual/current total | No established transaction in reviewed history through 052 [RECORDED in 050; later 051/052 representation only] | Outcome/capability UNKNOWN; no conversion denominator |
| Repeatability/value capture | H; N for actual/current total | No established commercial repeatability or captured value in reviewed history [RECORDED/DERIVED] | Repeated internal resolutions/UI acceptance are not repeated exchange |
| Currently need human attention | N for opportunity population | 052 attention cards are synthetic [RECORDED]; current system-wide count UNKNOWN | STATUS gives one work pointer, not all opportunity actions |
| Dominant blocker classes | H | Selected run-specific reason/control counts (section 21) [RECORDED] | Selection bias, overlaps, and historical horizon visible |
| Where evidence accumulates/terminates | H | Chain map in section 16 [DERIVED] | Historical branch endpoints and censor reasons, no forced conversion waterfall |

**[DERIVED]** No economic inventory metric above qualifies as a complete current Engine truth. A current repository operational pointer and structured identity *capability* are displayable facts, but not substitutes for these missing metrics.

### Historical run denominators

| Run / source | Formed hypotheses/candidates [RECORDED] | Other preserved flow [RECORDED unless marked] |
|---|---:|---|
| 021 checkpoint | 11 | 2 deepened, 11 killed, 0 advanced; raw signal count UNKNOWN |
| 022 checkpoint | 9 | 3 signal families, no survivor; complete raw denominator UNKNOWN |
| 023 checkpoint | 8 | 6 cheaply rejected, 2 deeper, 1 bounded uncertainty; not 2 full survivors |
| 028 checkpoint | 10 | 7 shallow killed, 3 deepened, 1 advanced; no row-complete inventory here |
| 031 result | 14 | 37 raw, 3 deepened, 14 killed, 0 survivors; shallow partition inconsistent |
| 032 result | 10 | 34 raw, 3 deepened, 9 killed, 0 full survivors + 1 bounded uncertainty |
| 046 result | 12 | 14 raw, 3 deepened, 11 killed, 0 full survivors + 1 HOLD |

**[DERIVED]** 37 + 34 + 14 = 85 reported raw-screening entries across the three detailed runs; 14 + 10 + 12 = 36 formed entries; 14 + 9 + 11 = 34 killed entries. These are arithmetic sums of heterogeneous run-local records, not a deduplicated cumulative Engine funnel. They cannot supply a 34/36 terminal-opportunity rate or a two-opportunity survival population. Repeat discovery must be reconciled before any unique total.

### Counting rules

**[DERIVED]** Count source records by logical key, captures by revision key, hypothesis attempts by run-local identity, and opportunities only by an explicitly reconciled decision/thesis referent. A single opportunity may have several independent established evidence states; cumulative “ever reached” counts may overlap and cannot be added into a population. A mutually exclusive distribution requires a defined state assignment rule and an explicit UNKNOWN/unclassified bin. Lifecycle and evidence frontier remain separate axes.

Reactivation adds history without creating a new identity automatically; a new actor/decision or changed thesis must be adjudicated. It must not erase historical kills or alter frozen run counts. Curated fixtures may be counted only as fixtures/sample chain rows, never as the complete Engine. Display the population definition, observation interval, source horizon, source/reconstruction quality, inclusion/exclusion and dedup rules, missingness, and row-level audit links beside every number.

## 21. Blocker/disposition distribution finding

**[RECORDED]** 031 headline: six exact-resolution kills under its explicit definition; fourteen total kills with compound conditions. 032: five exact-resolution kills, two BLOCK and two REVIEW REQUIRED control classifications. 046 disposition table: four ACTOR/AUTHORITY kills (C01/C05/C06/C09), three DECISION CLOSED kills (C03/C07/C11), two UNCERTAINTY kills (C04/C12), one RECOVERABILITY kill (C02), one EXACT RESOLUTION kill (C08), and one HOLD (C10). **[DERIVED]** The 046 distribution sums to twelve local candidates.

**[DERIVED]** These support historical gate/disposition summaries; they do not share a stable cross-run taxonomy. Control flags can overlap dominant reasons. The six-chain sample highlights access/exposure/missing actor-held evidence after resolution competition, but its curation favors surviving/deepened branches. “Most AE opportunities are blocked” and a complete dominant-blocker pie chart are not supportable. Structural failures and contingent blockers must be retained separately, including multiple blockers and UNKNOWN classification.

## 22. Dormant/reactivation finding

**[RECORDED]** Canadian 027 expressly permits revisit only after a legitimate low-friction importer-access channel or materially changed distribution fact. 051 preserves cocoa access, CRM new-case exposure, and realtime legitimate still-live surface/matrix conditions. **[DERIVED]** These make selected dormant evidence worth preserving without asserting that an old decision is still live.

**[UNKNOWN]** How many opportunities actually reopened, time spent dormant, blocker removal frequency, or economic yield of reactivation. No monitored changes or reactivation automation exist. Before any future action, recheck decision horizon, blocker, exact resolution, and authority under a separate contract; this audit performs none of those external checks.

## 23. Regulatory-reactivation finding

**[RECORDED]** Chemicals in the 001–019 checkpoint carried trust/regulatory burden; 031 C07/C08/C13 have eligibility/privacy/regulatory control sensitivity; 032 C08/C09 have historical platform-rule blocks; 046 C09 concerns data-residency compliance and actor authority. Canadian 027's limiting gate is actor access, not proof that customs regulation prohibited the proposed resolution. Old-stock 022 and surcharge 031 were rejected for adequate existing resolution, not solely for a regulatory prohibition.

**[DERIVED]** Preserve the exact blocker class, jurisdiction/platform, relied-on evidence date, actor/decision scope, and a conditional reopening observation where supported. Qualified review or an authorized legitimate path can be conceptually contingent. A change in law is not automatically a removed access/trust/resolution constraint and cannot itself authorize action. For early chemicals, the controlling rule and a concrete reactivation condition remain UNKNOWN.

**[UNKNOWN]** No reviewed chain demonstrates a regulatory/control blocker subsequently removed and a commercially successful reopened opportunity. The preservation hypothesis has case support for optionality and learning, not empirical reactivation effectiveness. No current law or platform rule was checked or inferred from historical text.

## 24. Efficiency-metric finding

**[DERIVED]** Useful descriptions are run-local input/disposition counts, horizon-labeled partial state/frontier distributions, cited blocker types, recorded active time and spend, and a traceable movement of the binding uncertainty. Throughput requires deduplicated opportunity admissions/transitions and defined intervals; time-in-state requires timestamped state events; current attention load requires current tasks/authority; inventory size and reactivation frequency require completeness. Those prerequisites are absent or partial, so the respective system metrics remain UNKNOWN.

031's nine recorded minutes, 032's twenty-six, and 046's prospectively reported nine minutes twelve seconds describe different runs. They do not prove a monotonic efficiency curve. Commit time and document order do not supply dwell time. Do not compute generic conversion, one funnel percentage, success rate across heterogeneous experiments, composite efficiency, opportunity score, economic ROI, or failure rate from unexposed actors.

## 25. Discrimination-learning potential

**[DERIVED]** Retained dispositions could support future learning about which exact-resolution gates invalidate a bounded thesis, which access/control gates preserve a contingent one, and whether later evidence changes a particular classification. The record also shows policy changes followed by different observed bottlenecks (020→021 and 031→032), not causal gate-accuracy estimates.

Required future evidence includes same-referent revisits, stable gate definitions, predeclared cheap discriminators, last horizon, reviewer correction, blocker-change observations, and valid outcomes. Keep non-revisited cases censored. **[UNKNOWN]** False-positive/false-negative rates, gates that “mostly” reopen, discrimination improvement over time, and the value of dormant inventory. A high kill rate alone may reflect selection bias or obvious candidates rather than accuracy.

## 26. Four-level information-architecture assessment

**SUPPORTED WITH REFINEMENT AS A SEMANTIC HYPOTHESIS [DERIVED]**:

- ENGINE: aggregate only defined, reconstructable populations/frontiers and show missingness prominently.
- CONTROL: dated human task, waiting dependency, permission and stop-state requirements.
- POSSIBILITY SPACE: referent, lifecycle, independent six-dimensional distance and its uncertainty.
- EVIDENCE: source, provenance, observation horizon, experiments and trajectory.

These are information responsibilities with linked audit paths, not production modules or a mandatory screen order. ENGINE must not transform incomplete possibility/control records into apparently live totals. The layers can share referents while retaining distinct counting units. 052's visually similar-box defect remains a human observation, not a layout change in 053.

## 27. Engine-layer semantic contract

**PROPOSED AUDIT OUTPUT ONLY [DERIVED]**. Every later aggregate needs:

1. Named unit and population boundary: source items, hypothesis attempts, scoped decision instances, or opportunity families; never implicit mixtures.
2. Explicit inclusion/admission rule, completeness status, and horizon/window; distinguish repository-known history from current external reality.
3. Human-auditable referent reconciliation and parent signal/candidate/experiment links, including same-as, new-instance, split/merge uncertainty and synthetic exclusions.
4. Independent evidence frontier, lifecycle disposition, and dated control state/authority, with UNKNOWN, untested, censor and no-action meanings preserved.
5. State-transition observation times when recorded, separate from ingestion/run/artifact times; corrections preserve prior evidence and source verdicts.
6. Each aggregate's RECORDED/DERIVED/ESTIMATED/UNKNOWN class, source links, missingness, overlap and dedup rules; reveal what numerator and denominator actually mean.
7. Distinguish “zero documented qualifying events in this audited population” from “zero real effects”, and incomplete inventory from empty inventory.
8. Link aggregate → included/excluded row → reason/state → immutable evidence/trajectory. A reactivation suggestion is not a task, priority or authorization.

This defines semantic requirements without implementing a schema, counting logic, or architecture.

## 28. Data-contract gaps

**[DERIVED]** The minimum manual repair is: define family versus decision-instance counting; explicit candidate-to-opportunity admission; cross-experiment same-referent links; dedup and unresolved identity treatment; an authoritative dated state/evidence/authority entry; terminal versus contingent reason and reactivation condition; coverage/missingness statement; and separate transition/observation times. Link to existing source items where applicable without requiring all manual RADAR signals to originate in SQLite.

A complete historical backfill is not required to start a truthful prospective cohort. Do not invent historical identities, dates, regulation, missing rows, or admission events. The next contract should test these requirements on existing records plus an explicitly limited cohort before any durable architecture is proposed. Repair here means a bounded Markdown evidence agreement, not hooks, templates, database, identity service, or workflow software.

## 29. Later UI experiment gate

**DEFER / DATA-CONTRACT REPAIR FIRST [DERIVED]**.

| SPEC-053 implementation condition | Assessment |
|---|---|
| Useful subset of system semantics supportable | PASS for historical run/chain summaries; partial for overall Engine inventory |
| Population/horizon limits explicit | PASS in this audit; admission/dedup denominator remains incomplete |
| No implication of false completeness | CONDITIONAL: a historical run-report view is truthful; a current Engine inventory/distribution view cannot yet be supported |
| Evidence/lifecycle/control remain distinct | PASS conceptually; no full dated state-assignment record |
| Real operator question from 052 answered | Need established; overall performance, inventory and attention demand still require the missing contract |

A historical report display could be accurate with the labels above, but it would not resolve the dominant whole-Engine inventory/state question. Verdict B is selected over A because the key identities/admission/current-state denominators need repair before that UI test. It is selected over C because the operator need is real and semantics are useful, and over D because the distinctions and repair path are reconstructable. Scope/integrity/timing checks exclude E if they pass.

## 30. Software/non-build disposition

**DO NOT BUILD [DERIVED]**. No Engine funnel/dashboard, opportunity database or identity service, migration, event store, monitor, reactivation automation, scheduler, scoring, ranking, classifier, or autonomous portfolio system is earned. Do not modify the accepted 051/052 viewers to conceal population gaps.

## 31. Protocol-alignment candidate

**RECOVERY ≠ EXECUTION [RECORDED contract observation; DERIVED alignment candidate].** Requests to inspect, reconcile, recover, or report the next permitted operation authorize only that bounded recovery work, not execution of the recovered operation. Record this as a candidate for a separately reviewed protocol update. No AGENTS or protocol edit is made in 053.

## 32. What the audit establishes

**[DERIVED]** AE can reconstruct useful partial historical evidence and selected chain referents; generic experimental KILL is not a lifecycle state; observation, candidate, opportunity, experiment and attempt counts are distinct; current global funnel/attention metrics would overstate identity/coverage/freshness; Opportunity Memory is PARTIAL but worth preserving. The decisive prerequisite is a small manual data-contract repair rather than Engine-state software.

## 33. What remains unproven

**[UNKNOWN]** Full opportunity population, cross-run uniqueness, complete current lifecycle/control assignment, source-to-opportunity lineage, inventory completeness, actual current actor/regulatory state, dormant reopening frequency or yield, stage dwell time, comparable throughput/efficiency, empirical gate accuracy, production architecture, population-scale UI benefit, economic effect, WTP, transaction, repeatability, and value capture. Historical absence of recorded outcomes is not observed failure.

## 34. Exactly one recommended next action

Prepare one bounded, repository-only manual opportunity identity/evidence-contract repair packet that defines decision-instance versus family units, admission/dedup rules, dated independent evidence/lifecycle/control states, horizon/missingness and reactivation records, and validates them on an explicitly limited existing-evidence cohort before any Engine-state UI implementation.

This is a recommendation for the next specification/review, not authorization to execute repair, begin Experiment 054, change living truth, or publish 053.

## Completion timing, telemetry and integrity

- **[RECORDED]** Evidence/artifact/test freeze: `2026-10-07T08:55:54Z`.
- **[DERIVED]** Active continuous interval: **9 minutes 26 seconds (566 seconds)** from the prospective start. Final mechanical recording and Git commit follow this freeze; no observation window or approval wait is included.
- **[RECORDED]** Existing suite: **89 passed**, `.venv/bin/pytest -q`.
- **[RECORDED]** All 34 required report sections present; all local evidence links resolve; the section 17 detailed ledger retains exactly 36 existing run-local candidate entries.
- **[RECORDED]** Integrity: protected tracked files unchanged against `71c28d2`; original 052 approved closure retained in ancestry; changed-file scope limited to this artifact and STATUS; `git diff --check` / staged whitespace check passes before commit.
- **[RECORDED]** Human interventions: 0; consequential external actions and control escalations: 0. No new approval judgment was required. Incremental external spend: €0; compute cost UNKNOWN.
- **[DERIVED]** Evidence yield: HIGH for the bounded audit question, because reconstructable historical evidence is separated from unsupported current counts and the non-build gate is decisive. This is not a quantitative productivity score.
- **[DERIVED]** Dominant uncertainty after: whether a small manual identity/admission/horizon/state contract can support a faithful prospective cohort without inventing old evidence. No policy/model alignment is applied.
- **[RECORDED]** Stop condition: identity distinctions, supportability matrix, PARTIAL memory verdict, and repair-first gate are decisive. Further archaeology would not supply a missing current inventory/admission/task contract; the run stops below the target without exceeding the hard ceiling.

**Artifact path:** `experiments/053/engine-state-funnel-semantics-audit.md`.

**Integrity/test result:** PASS — protected history unchanged, only permitted files changed, whitespace clean, 89 tests passed.

**Commit SHA:** supplied in the completion report after the immutable local execution commit; discoverable as the commit introducing this artifact. No amend or push.

**Operational endpoint:** `IMPLEMENTATION_FROZEN`; audit complete locally, awaiting independent review under a fresh bounded handoff. No review-branch publication, closure, repair execution, or later experiment is performed.
