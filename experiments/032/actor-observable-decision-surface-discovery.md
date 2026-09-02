# Spec 032 — Actor-Observable Decision Surface Discovery

Run date: 2026-09-02

Repository baseline: `bd50da8a2f6ac0499d04b1d94f9448336a4f23dd` on synchronized local `main`

Execution mode: research-only. No actor was contacted, no comment or reaction was posted, no private identity was resolved, no software was built, and no paid data was used.

Spec 030 isolation: maintained. Its artifact, actor, and actor-response state were not inspected, modified, contacted, or used as evidence.

## 1. Verdict

**B — TOPOLOGY IMPROVED, ONE BOUNDED UNCERTAINTY.**

Starting from self-identified actors materially improved intervention topology. Ten qualifying candidates were formed from 34 raw actor signals across seven surface families. None failed because the actor was merely inferred. Nine reached decisive kills; one, Apache Superset SIP-225, remains one bounded public uncertainty short of FORGE: whether the semantic-layer hierarchy interface and landing sequence are concrete enough to make the proposed chart-local configuration safely migratable.

The run does not claim market scale, willingness to pay, or product potential. It shows only that actor-first origins yield more testable exposure and effect paths than accessible surfaces alone.

## 2. Primary question tested

Can RADAR improve survivor yield by starting only from surfaces where a real decision-maker self-identifies, a consequential decision remains open, a bounded future resolution could legitimately reach that actor, and some decision effect could later be observed?

**Finding:** yes, narrowly. Actor-access and exposure topology improved relative to Spec 031, and one candidate retained only one bounded public uncertainty. Exact-resolution competition became the dominant downstream kill.

## 3. Surface families inspected

| Family | Raw signals | Why materially distinct | Qualifying candidates |
|---|---:|---|---:|
| GitHub issues and discussions | 8 | Repository-native maintainers/users expose issue state, labels, replies, and visible disposition changes | 2 |
| Standards/core-development discussion | 4 | Named proposal authors and core participants deliberate language policy on a governed Discourse surface | 1 |
| Product support communities | 6 | Named administrators/operators expose current configurations and can continue the same support thread | 3 |
| Technical vendor forums | 5 | Named operators expose production architecture and vendor-specific state | 1 |
| Reddit operator/founder threads | 5 | Founders state live allocation and leadership choices, with subreddit-specific controls | 2 |
| Stack Exchange Q&A | 4 | Named users ask bounded pre-action questions; answers/comments/acceptance are visible | 1 |
| Marketplace/founder-sale listings | 2 | Sellers are visible, but buyer state and post-sale effects are usually hidden | 0 |

GitHub and marketplace/listing surfaces are not Reddit or generic forums. Search was used only to locate native surfaces and was not counted as a family.

## 4. Raw actor signals inspected

Thirty-four raw signals were inspected. The list below preserves the actor signal and why it did or did not form a candidate.

| ID | Native surface and signal | Actor evidence | Formation result |
|---|---|---|---|
| R01 | [Flowise discussion #6678](https://github.com/FlowiseAI/Flowise/discussions/6678): operator comparing incremental updates with scheduled re-indexing for a real service business | DIRECT, but native status check found the repository archived/read-only before candidate formation | non-qualifying |
| R02 | [Superset SIP-225](https://github.com/apache/superset/issues/43331): author asks ship chart-local hierarchy now or wait for semantic-layer source | DIRECT; proposal author, open pre-discussion | C03 |
| R03 | [Kestra #14597](https://github.com/kestra-io/kestra/issues/14597): maintainer must decide Jackson 3 migration scope | DIRECT; assigned author, open issue | C04 |
| R04 | chatlas file-search/provider-RAG scope issue | DIRECT; maintainer scope decision, but consequence below threshold | non-qualifying |
| R05 | OpenAI Codex no-progress watchdog issue | DIRECT user impact, but asks maintainers for a product fix rather than exposing the reporter's open decision | non-qualifying |
| R06 | Cherry Studio legacy migration bug | DIRECT user failure, but exact fix shape is already supplied; no residual decision | non-qualifying |
| R07 | OpenDisplay wire-protocol research issue | DIRECT, but native status check showed closed/decided | non-qualifying |
| R08 | .NET async validation API proposal | STRONG actor state, but API already approved | non-qualifying |
| R09 | [PEP 842 postmortem](https://discuss.python.org/t/pep-842-postmortem-how-do-we-protect-the-standard-library/108575): proposal author asks what to do after withdrawal | DIRECT; named author and live options | C02 |
| R10 | PEP 829 startup-configuration discussion | DIRECT participants, but decision had advanced into an existing formal PEP process | non-qualifying |
| R11 | PEP 661 typing-spec discussion | DIRECT participants, but the observed question had already converged | non-qualifying |
| R12 | CPython issue-cleanup discussion | DIRECT organizer, but the open state is volunteer coordination rather than a bounded economic decision | non-qualifying |
| R13 | [Atlassian Rovo MCP support thread](https://community.atlassian.com/forums/Rovo-questions/Error-making-tool-calls-to-Rovo-MCP-Server/qaq-p/3274841): enterprise client cannot complete OAuth refresh | DIRECT operator with logs and continuing clarifications | C06 |
| R14 | [Jira–GitHub connection thread](https://community.atlassian.com/forums/Jira-questions/Issue-connecting-Jira-with-GitHub/qaq-p/3281966): admin cannot use documented non-owner approval path | DIRECT administrator, current blocked integration | C07 |
| R15 | [Bitbucket recovery thread](https://community.atlassian.com/forums/Bitbucket-questions/Urgent-request-to-recover-legacy-Bitbucket-Issues-data-after/qaq-p/3281248): workspace admin seeks recovery after tracker sunset | DIRECT administrator, current unrecovered business data | C10 |
| R16 | Jira CSV update question | DIRECT administrator, but bounded implementation question lacked material economic consequence evidence | non-qualifying |
| R17 | Atlassian Premium metadata opt-out question | DIRECT admin, but an Atlassian team answer resolved the observed choice | non-qualifying |
| R18 | Atlassian build-vs-buy webinar post | INFERRED organizations rather than a specific deciding actor | non-qualifying |
| R19 | [Proxmox HA storage thread](https://forum.proxmox.com/threads/proxmox-%E2%86%92-zfs-%E2%86%92-virtio-scsi-%E2%86%92-nfs-a-viable-ha-storage-architecture-for-100-vms.185872/): startup designing 60 TB/100-VM storage to avoid a €200k–€400k SAN | DIRECT operator, explicit pre-purchase decision | C05 |
| R20 | Proxmox ZFS-on-SAN thread | DIRECT operator, but official support boundary and replies already answer the setup question | non-qualifying |
| R21 | Proxmox Veeam backup failure thread | DIRECT production operators, but observed state is incident diagnosis rather than a bounded open choice | non-qualifying |
| R22 | Proxmox no-subscription production question | DIRECT small-business owner, but existing thread and official subscription distinction already resolve the choice | non-qualifying |
| R23 | Ubiquiti controller migration thread | DIRECT operator, but author later states the selected migration path | non-qualifying |
| R24 | [First-hire thread](https://www.reddit.com/r/Entrepreneur/comments/1vg667u/need_first_hire_suggestions/): food CPG founder entering a warehouse cannot find the needed first hire | DIRECT founder, live staffing decision | C08 |
| R25 | [Founder succession thread](https://www.reddit.com/r/Entrepreneur/comments/1v0an68/when_to_let_go_as_a_founder/): eight-year CEO considers installing a more experienced CEO | DIRECT founder, live leadership decision | C09 |
| R26 | Entrepreneur returning to employment thread | DIRECT operator, but the decision context is broad and effect is mostly private | non-qualifying |
| R27 | sysadmin Wi-Fi redesign vendor thread | DIRECT operator, but the observed four-month-old thread had extensive answers and no evidence the choice remained open | non-qualifying |
| R28 | sysadmin $520k server quote thread | DIRECT operator, but edits show approval, price negotiation, and order completion | non-qualifying |
| R29 | [Adelaide pre-dawn transport question](https://travel.stackexchange.com/questions/204057/ease-of-getting-taxi-rideshare-at-330am-on-a-sunday-in-adelaide): traveler cannot miss a 6:00 flight and weighs taxi, rental, or airport hotel | DIRECT traveler and explicit option set | C11 |
| R30 | Long-name airfare booking question | DIRECT traveler, but no meaningful economic consequence beyond ordinary booking friction was evidenced | non-qualifying |
| R31 | Lufthansa companion-ticket chargeback question | DIRECT traveler, but financial/legal facts and post-bank effect were not sufficiently exposed | non-qualifying |
| R32 | Damaged-passport replacement question | DIRECT traveler, but authoritative carrier/government resolution and existing answers dominated | non-qualifying |
| R33 | Indie Hackers/Flippa AI-journal asset-sale positioning question | DIRECT seller, but January listing status did not establish that the sale decision remained open | non-qualifying |
| R34 | Reverb vintage instrument listing | STRONG seller sale state, but buyer is inferred and no unresolved seller uncertainty is exposed | non-qualifying |

No Spec 031 candidate was reopened. Similar categories were counted only when a new, independently observed actor signal established a different topology.

## 5. DIRECT / STRONG / INFERRED actor classification

| Classification | Count | Interpretation |
|---|---:|---|
| DIRECT | 28 | A specific actor explicitly stated state, choice, request, or next test |
| STRONG | 2 | Specific actor behavior/status strongly evidenced a decision, without an explicit live question |
| INFERRED/non-qualifying | 4 | Actor type, buyer, organization, or decision ownership could only be inferred |

DIRECT does not itself mean qualifying. Eighteen DIRECT signals were rejected for closed status, weak consequence, completed decisions, exact resolution, or weak effect topology.

## 6. Qualifying actor-observable candidates

| ID | Actor and live decision | Consequence | Path | Exposure | Effect | Recoverability |
|---|---|---|---|---|---|---|
| C02 | PEP 842 author/core participants: stdlib privacy mechanism after withdrawal | downstream breakage and core-maintainer burden | SAME | HIGH | HIGH via option/proposal change | MEDIUM/HIGH |
| C03 | Superset SIP author/community: ship chart-local hierarchy or wait for semantic layer | implementation/rework labor and compatibility | SAME | HIGH | HIGH via SIP/PR disposition | HIGH |
| C04 | Kestra maintainer: Jackson 3 migration scope | core/plugin compatibility and maintainer labor | SAME | HIGH | HIGH via issue/implementation disposition | HIGH |
| C05 | Proxmox startup operator: commodity HA architecture vs enterprise storage | €200k–€400k avoided spend, outage/data-loss risk | SAME | HIGH | MEDIUM via stated architecture/test | MEDIUM |
| C06 | Rovo enterprise operator: OAuth endpoint/discovery and telemetry path | blocked integration and engineering labor | SAME | HIGH | HIGH via reported reconnect/result | HIGH |
| C07 | Jira administrator: restore non-owner GitHub approval workflow | blocked integration and admin/owner labor | SAME | HIGH | MEDIUM via reported connection | HIGH |
| C08 | Food CPG founder: role/channel/process for first warehouse hire | payroll, founder time, warehouse scaling | SAME technically | HIGH | MEDIUM via shortlist/hire-plan report | MEDIUM |
| C09 | Startup founder/CEO: retain role, redesign it, or recruit successor | company execution, leadership cost, opportunity cost | SAME technically | HIGH | MEDIUM via reframing/next step | LOW |
| C10 | Bitbucket workspace admin: recover business issue data after sunset | lost project history and development continuity | ADJACENT to private support | MEDIUM | LOW/MEDIUM; actual recovery private | LOW/MEDIUM |
| C11 | Traveler: taxi booking, rental, or airport hotel for unmissable flight | missed-flight/rebooking and hotel/rental cost | SAME | HIGH | MEDIUM via accepted choice/report | HIGH |

These were signal-native hypotheses. No business concept was selected before the actor signal.

## 7. Non-qualifying signal patterns

- Completed decisions with explicit outcome edits, such as the $520k server purchase.
- Support incidents that ask for a fix but do not expose an actor choice.
- Approved, closed, or already-selected proposals and migrations.
- Public listings where buyer identity and buyer uncertainty remain hidden.
- Generic build-vs-buy or founder advice content describing actor classes.
- Technical questions whose consequence was curiosity or ordinary convenience.
- Threads with extensive exact answers and no evidence the decision remained open.
- Cases where downstream behavior occurs only inside a private support, bank, employer, or booking workflow.

## 8. Candidate kill table

| ID | Terminal disposition | Dominant reason |
|---|---|---|
| C02 | KILL | The withdrawn PEP, competing PEPs 843/844, and the live postmortem already enumerate the functional choices; the residual need is empirical downstream-use evidence, not another option memo. |
| C03 | ONE BOUNDED UNCERTAINTY | All topology gates pass, but the issue does not link a concrete semantic-layer hierarchy contract or landing sequence needed to validate migration safety. |
| C04 | KILL | The issue already states the exact compatibility questions and coexistence option; the next decisive observation is a repository/plugin compatibility spike, not an additional research resolution. |
| C05 | KILL | 100-VM/60-TB production architecture requires bounded RPO/RTO, failure-domain, staffing, and benchmark evidence plus qualified review; public advice alone is not an acceptable control surface. |
| C06 | KILL | The thread and official OAuth 2.1/discovery guidance already resolve endpoint versus authorization-server behavior and the support escalation payload. |
| C07 | KILL | Atlassian's official guide and exact non-owner KB already specify owner-link/request flows; this appears to be a product regression requiring support, not a missing decision resolution. |
| C08 | KILL / BLOCK | r/Entrepreneur explicitly treats AI/GPT-generated comments as spam; the technically SAME path is not legitimate for this experimenter. |
| C09 | KILL / BLOCK | Decisive board, performance, financing, and leadership evidence is private/professionally sensitive, and the subreddit prohibits AI-generated comments. |
| C10 | KILL | A public reply can be exposed, but recovery authority and recovery success exist only in Atlassian's private support systems; decision effect cannot be observed reliably. |
| C11 | KILL | The same page already gives a bounded recommendation to pre-book a named taxi service, so the residual resolution gap is absent. |

Candidates killed: 9. Full survivors: 0. Candidates with exactly one bounded uncertainty: 1.

## 9. Deepened candidates

Exactly three candidates were deepened.

### D1 / C02 — Python standard-library private API policy

- **Strongest evidence for:** the named PEP author explicitly asks what to do after withdrawal, the topic is open, and choices affect downstream breakage and long-term core maintenance.
- **Strongest evidence against:** [PEP 842](https://peps.python.org/pep-0842/), [PEP 843](https://peps.python.org/pep-0843/), [PEP 844](https://peps.python.org/pep-0844/), and the postmortem already contain the option analysis. Participants identify the true missing evidence: why users reached for private APIs.
- **Exact existing resolution:** current PEPs and thread cover export syntax, decorators, policy-only change, typeshed/autocomplete, `__dir__`, and transition aliases.
- **Decisive remaining uncertainty:** distribution of accidental use versus deliberate use because no adequate public API exists.
- **Cheapest stop observation:** read the live thread through its convergence on empirical-use reasons and narrower mechanisms.
- **Cheapest progression observation:** a cited sample of downstream breakages classifying why each private name was used.
- **Plausible disposable resolution:** a small evidence table, not another architecture proposal.
- **Future intervention location:** SAME Discourse topic.
- **Exposure evidence:** author/core participant reply, reaction, or request for examples.
- **Decision-effect evidence:** option set changes, an evidence request is adopted, or a subsequent proposal narrows.
- **Controls:** CONDITIONAL; public-source evidence only, comply with core-development norms, and obtain explicit authorization before posting.
- **Interaction justified:** not yet; the contemplated generic memo is duplicate resolution.

### D2 / C03 — Apache Superset SIP-225 sequencing

- **Strongest evidence for:** the author exposes an open binary sequencing decision, a reference implementation, additive schema, feature flag, migration intent, and a repository-native pre-discussion state. Official Superset docs confirm current Drill By/Drill to Detail do not provide the proposed fixed, in-place hierarchy.
- **Strongest evidence against:** the proposal says semantic-layer hierarchy primitives are "now landing" without linking a hierarchy contract or delivery sequence. SIP-182 remains a broad phased semantic-layer proposal, not proof that chart hierarchy metadata is imminent.
- **Exact existing resolution:** [current exploration documentation](https://superset.apache.org/docs/using-superset/exploring-data/) covers ad-hoc Drill By and Drill to Detail; it does not perform author-configured in-place hierarchical drill-down.
- **Decisive remaining uncertainty:** whether a concrete semantic-layer hierarchy interface will land soon enough, and with a compatible shape, to make chart-local configuration short-lived rework.
- **Cheapest stop observation:** no public hierarchy interface/linked implementation exists, or maintainers say the dependency is not planned for the target horizon.
- **Cheapest progression observation:** identify the exact hierarchy field/interface and linked issue/PR plus expected landing sequence; compare it with `drilldown_hierarchy: string[]`.
- **Plausible disposable resolution:** a one-page compatibility/sequencing note with three outcomes: ship unchanged, add a migration adapter, or wait.
- **Future intervention location:** SAME SIP-225 GitHub issue, after explicit authorization.
- **Exposure evidence:** proposal-author or committer reply/reaction, requested clarification, or issue project/status change.
- **Decision-effect evidence:** SIP text changes, chart-local schema changes, reference PR sequence changes, or an explicit ship/wait disposition.
- **Controls:** CONDITIONAL. Superset invites SIP discussion before major work; contribution must be original, evidence-based, non-promotional, and authorized. No code or PR should precede agreement.
- **Interaction justified:** only after the bounded public dependency check is completed.

### D3 / C05 — Proxmox startup HA storage architecture

- **Strongest evidence for:** a named startup operator exposes a pre-purchase design for 60 TB+, about 100 VMs, 25 GbE, high IOPS, 24/7 operation, commodity NVMe, and an explicit desire to avoid a €200k–€400k enterprise SAN.
- **Strongest evidence against:** the proposal does not bound RPO, RTO, tolerated data loss, failure domains, rebuild behavior, staffing, or tested small-file/burst performance. Those variables dominate the architectural choice.
- **Exact existing resolution:** the [Proxmox storage documentation](https://pve.proxmox.com/pve-docs-7/pvesm.1.html) distinguishes local ZFS from shared NFS and distributed storage; the native thread already narrows feasible options to Ceph, asynchronous ZFS replication, or LINSTOR/DRBD.
- **Decisive remaining uncertainty:** measured workload/failure requirements and whether the team can operate the selected distributed system safely.
- **Cheapest stop observation:** inability to state acceptable RPO/RTO and reproduce representative small-file plus burst load on a disposable three-node test.
- **Cheapest progression observation:** a failure-injection benchmark across one bounded Ceph or LINSTOR/DRBD design, including recovery time, acknowledged-write loss, and tail latency.
- **Plausible disposable resolution:** a requirements-to-test matrix, not a production architecture recommendation.
- **Future intervention location:** SAME Proxmox thread, only after authorization and qualified review.
- **Exposure evidence:** actor reply, supplied RPO/RTO values, or posted benchmark plan/result.
- **Decision-effect evidence:** removal of the nested NFS-VM design, selection of a test candidate, or changed hardware purchase sequence.
- **Controls:** REVIEW REQUIRED because incomplete advice could create production outage or data-loss risk; do not prescribe deployment or solicit private infrastructure data.
- **Interaction justified:** no; the control and validation burden exceeds a disposable public reply.

## 10. Economic-consequence findings

Actor-first surfaces exposed consequence more cleanly than category-first discovery:

- C03/C04 concerned implementation, compatibility, and rework labor across mature open-source systems.
- C05 exposed an explicit €200k–€400k avoided-enterprise-storage anchor plus outage/data-loss risk.
- C08/C09 exposed payroll, founder time, leadership, and organizational opportunity cost.
- C06/C07/C10 exposed blocked enterprise integration or lost business data.
- C11 exposed missed-flight, rebooking, hotel, rental, and taxi cost.

Economic consequence still did not imply a safe or unresolved opportunity.

## 11. Recoverability findings

| Level | Candidates | Finding |
|---|---|---|
| HIGH | C03, C04, C06, C07, C11 | Public docs/repository state plus bounded actor-reported result could resolve the decision |
| MEDIUM | C02, C05, C08 | Most state is public, but one bounded sample, RPO/RTO/workload variable, or role constraint is required |
| LOW/MEDIUM | C10 | Public policy can be found, but backend retention/recovery authority is private |
| LOW | C09 | Board dynamics, performance evidence, financing, and candidate alternatives are private and professionally sensitive |

Private state was accepted only where it could naturally be bounded and supplied on the same surface. C09 failed that test.

## 12. Exact-resolution findings

Exact functional resolution killed five candidates after actor topology passed:

- C02 already has a proposal family and active option analysis; the missing input is empirical evidence.
- C04 already specifies the compatibility matrix and coexistence path; the next step is implementation testing.
- C06's thread plus official Atlassian OAuth discovery guidance resolves the configuration distinction.
- C07 has an [official connection guide](https://support.atlassian.com/jira-cloud-administration/docs/integrate-with-github/) and an [exact non-owner KB](https://support.atlassian.com/jira/kb/integrating-github-cloud-with-jira-cloud-when-jira-admin-is-not-a-github-organization-owner/).
- C11 already received the bounded taxi-prebooking answer at the relevant decision moment.

C03 retained a residual gap: current Superset tools are functionally different, while the future semantic hierarchy dependency is not concrete enough to settle sequencing.

## 13. Intervention-path findings

Nine qualifying candidates originated with a SAME path and one was ADJACENT.

- GitHub/Discourse proposal surfaces offered the clearest legitimate future path because discussion and visible disposition are native to the decision process.
- Product support threads offered legitimate factual help, but exact official resolution or private support authority often dominated.
- Reddit technically offered SAME comments, but explicit community rules made the path illegitimate for AI-generated participation.
- C10's public community post led only to a private support process, weakening both intervention and measurement.
- The non-qualifying Flowise signal demonstrated that discovery-time accessibility must be verified before candidate formation and rechecked before any future interaction.

## 14. Exposure-observability findings

Exposure was HIGH or plausibly distinguishable for nine qualifying candidates through actor reply, reaction, clarification, accepted answer, or issue state change. It was MEDIUM for C10 because a public reply could be seen but recovery would move private.

No permalink, view count, or publication event was treated as actor exposure.

## 15. Effect-observability findings

Decision-effect observability was materially better than in Spec 031:

- HIGH for C02, C03, C04, and C06 because proposal, issue, test, or configuration state could visibly change.
- MEDIUM for C05, C07, C08, C09, and C11 because the actor could report a changed architecture, connection, shortlist, role frame, or transport choice.
- LOW/MEDIUM for C10 because successful recovery occurs in private support infrastructure.

Generic thanks, votes, traffic, and anonymous reactions were not counted as decision effects.

## 16. Control-feasibility findings

| Group | Future classification | Controls |
|---|---|---|
| C02 | CONDITIONAL | Authorized, evidence-based public contribution; core-development norms; no mass outreach to downstream users |
| C03 | CONDITIONAL | Authorization required; SIP discussion only; original evidence; no uninvited code/PR |
| C04 | CONDITIONAL | Authorization and repository norms; no implementation under this research experiment |
| C05 | REVIEW REQUIRED | Production HA/data-loss stakes, vendor context, qualified technical review, no prescriptive deployment advice from incomplete facts |
| C06–C07 | CONDITIONAL | Atlassian permits AI for polishing but requires the core contribution to be human-written, accurate, and helpful; no private logs or identifiers |
| C08–C09 | BLOCK | r/Entrepreneur explicitly prohibits AI/GPT-generated comments; no DM or alternate channel |
| C10 | REVIEW REQUIRED | Private support/data retention, account ownership, and business data; no attempt to access tickets or identify staff |
| C11 | CONDITIONAL | General factual answer only, platform rules, authoritative/local evidence, no booking or purchase |

Spec 032 authorized none of these future interactions. No external action occurred.

## 17. Strongest candidate, if any

**C03 — Apache Superset SIP-225.**

It has a real proposal author, an open repository-governed decision, explicit economic/rework consequence, high public recoverability, a constructible bounded resolution, a SAME intervention path, observable exposure, observable proposal/implementation effects, and conditionally acceptable controls. It remains one bounded uncertainty short of FORGE because the supposedly landing semantic-layer hierarchy contract and schedule are not linked or verifiable from the proposal.

## 18. Cheapest discriminator / FORGE handoff, if any

No FORGE handoff is yet justified.

The cheapest discriminator is a public dependency check for C03: locate the exact Superset semantic-layer hierarchy interface and linked implementation/landing sequence, then compare its shape with SIP-225's chart-local `drilldown_hierarchy: string[]`. If no concrete dependency exists in the relevant horizon, ship-now compatibility analysis becomes possible; if an incompatible contract is imminent, wait or require an adapter.

This discriminator is research-only and requires no actor interaction.

## 19. Comparison with Spec 031

| Question | Spec 032 finding |
|---|---|
| Did actor-access kills decrease? | Yes. Zero qualifying candidates used an inferred actor; no candidate was killed merely because only an actor type existed. |
| Did exposure observability improve? | Yes. Nine of ten had a plausible actor-specific exposure indicator; Spec 031 often had publication-only surfaces. |
| Did effect observability improve? | Yes. Most candidates exposed a visible reply, issue/proposal change, reported test, or stated next action, although economic outcomes often still required actor report. |
| Did volume decline? | Yes: 10 qualifying candidates from 34 raw actor signals versus 14 from 37 raw signals in Spec 031. The stricter origin rejected more DIRECT-but-closed signals before formation. |
| Did survivor quality improve? | Yes, narrowly. Spec 031 had no survivor; Spec 032 produced one candidate with exactly one bounded public uncertainty. |
| What new bottleneck dominated? | Exact existing resolution or an already-defined next engineering test, not actor access. |

No speed claim is made because the runs were not matched and per-candidate timing was not instrumented.

## 20. Dominant bottleneck after this run

**Residual resolution gap after exact-job checking.**

Actor-first discovery moved the bottleneck downstream. Five of ten candidates reached an actor-visible, consequential, legitimate surface but were killed because authoritative documentation, the same thread, an existing proposal, or an already-defined implementation test performed the bounded job. The next policy should preserve actor topology while moving exact-resolution checks immediately after cheap consequence/recoverability confirmation.

## 21. Operational telemetry

| Metric | Value |
|---|---|
| Active research time | 26 minutes |
| Paid spend | €0 |
| Surface families inspected | 7 |
| Raw actor signals inspected | 34 |
| DIRECT actor signals | 28 |
| STRONG actor signals | 2 |
| INFERRED/non-qualifying signals | 4 inferred; 24 total signals did not form qualifying candidates |
| Qualifying candidates generated | 10 |
| Candidates killed | 9 |
| Candidates deepened | 3 |
| Survivors | 0 full; 1 with one bounded uncertainty |
| Actor-access kills | 0 |
| Exposure-observability kills | 0 among qualifying candidates; 1 raw signal rejected after native surface closure |
| Effect-observability kills | 1 dominant, 2 contributing |
| Recoverability kills | 1 dominant, 2 contributing |
| Exact-resolution kills | 5 |
| Control kills/escalations | 2 BLOCK; 2 REVIEW REQUIRED; no escalation or interaction performed |
| Human interventions required | 0 |
| Evidence yield | HIGH |

Approximate active allocation: GitHub/proposal surfaces 8 minutes; product/vendor support 6 minutes; Reddit/Stack Exchange/marketplace screening 4 minutes; exact-resolution/control checks and synthesis 8 minutes.

The 60-minute target was not filled artificially. Every candidate had a decisive disposition or the single bounded discriminator, so the run stopped early and remained well below the 90-minute hard ceiling.

## 22. What RADAR learned

- Actor-first origin is effective at eliminating actor-type and unreachable-review candidates before formation.
- Native status must be checked before candidate formation and rechecked later: an apparently high-quality SAME surface can become read-only between publication and research.
- SAME communication plus visible replies materially improves exposure measurement, but does not guarantee economic-effect visibility.
- Platform rules can convert a technically available comment box into a blocked intervention path.
- Exact-resolution checking remains essential even after excellent actor topology; it became the dominant kill.
- Proposal systems are especially productive because actor, decision state, exposure, and effect are co-located.
- The highest-quality residual uncertainty is often a linked dependency/status fact rather than a market question.

## 23. What remains unproven

- Whether C03's semantic-layer hierarchy dependency is concrete and near-term.
- Whether resolving that dependency would produce an authorized future intervention or a decision change.
- Whether actor-first discovery improves survivor yield across matched repeated runs rather than this single comparison.
- Whether reported issue/proposal changes correlate with meaningful economic value outside the public surface.
- Whether non-forum actor-visible surfaces can supply qualifying candidates consistently.
- Whether platform-native exposure indicators can distinguish comprehension from mere engagement.
- Whether any future candidate supports willingness-to-pay, repeatability, or durable product potential; none was tested here.

## 24. Architecture/research-policy implications

- Start from actor-visible topology, but verify native surface status immediately before candidate formation and again before any future intervention.
- Keep actor class, intervention path, exposure evidence, and decision-effect evidence as separate fields.
- Move exact functional-resolution checking earlier once actor, consequence, and recoverability pass.
- Treat platform content rules as part of topology, not a late compliance check.
- Prefer governed proposal/issue surfaces where decision changes are natively visible.
- Record whether the remaining discriminator is public research, actor-supplied data, implementation testing, or professional judgment.
- Do not automate discovery or build a surface ontology from one topology experiment.

## 25. Exactly one recommended next action

Perform the bounded public dependency check for Superset SIP-225 by identifying the exact semantic-layer hierarchy interface and linked landing sequence, then record whether its shape makes the chart-local `drilldown_hierarchy` proposal safely migratable; do not contact any actor or begin FORGE until that single uncertainty is resolved.
