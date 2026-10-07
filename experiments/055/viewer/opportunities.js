/*
 * Experiment 051 historical opportunity fixtures.
 *
 * This file is intentionally plain JavaScript so the static viewer works from a
 * file:// URL without a server. The objects are repository-grounded snapshots,
 * not live-world claims. Order is chronological by first experiment, never rank.
 */
window.OPPORTUNITY_FIXTURES = {
  schemaVersion: "051-v0",
  generatedFromRepositoryAt: "2026-09-17",
  orderingRule: "Chronological by first experiment; no automatic ranking.",
  distanceVocabulary: ["NEAR", "MEDIUM", "FAR", "BLOCKED", "UNKNOWN"],
  lifecycleVocabulary: ["ACTIVE", "DORMANT", "TERMINAL", "REVIEW"],
  evidenceClasses: ["RECORDED", "DERIVED", "ESTIMATED", "UNKNOWN"],
  caveats: [
    "The viewer renders repository-known state at each stated evidence horizon, not current external reality.",
    "Distance states are independent categorical descriptions, not scores, ranks, or a composite.",
    "UNKNOWN is not FAR. BLOCKED is not TERMINAL. A historical KILL/PARK is preserved separately from lifecycle.",
    "Decision actor, beneficiary, buyer/payer, actor effect, economic effect, and value capture remain distinct."
  ],
  opportunities: [
    {
      id: "cocoa-paid-pilot",
      name: "Czech cocoa purchasing and repricing aid",
      experimentRange: "013→014",
      evidenceHorizon: "Through Experiment 014; consolidated in the 001–019 checkpoint dated 2026-09-02",
      lifecycle: {
        state: "DORMANT",
        evidenceClass: "DERIVED",
        reason: "The proposition survived commercial translation, but valid authenticated exposure to qualifying producers was not executable. The test was invalid, not negative.",
        historicalDisposition: "Experiment 013 advanced cocoa as the most plausible cheap commercial test; Experiment 014 ended D — INVALID."
      },
      significance: "A direct paid-pilot hypothesis tied cocoa-input movements to purchasing and finished-product repricing decisions for small Czech producers.",
      thesis: "A lightweight weekly evidence-backed brief may reduce cocoa purchasing and repricing uncertainty for independent Czech chocolate or confectionery producers.",
      actor: {
        state: "KNOWN",
        value: "Independent Czech chocolate/confectionery producer purchasing cocoa inputs commercially.",
        evidenceClass: "RECORDED"
      },
      beneficiary: {
        state: "KNOWN",
        value: "The producer making purchasing, inventory, margin, and repricing decisions.",
        evidenceClass: "DERIVED"
      },
      buyerPayer: {
        state: "SUPPORTED HYPOTHESIS",
        value: "The same producer was the intended paid-pilot customer, but no qualifying prospect reached valid market exposure and no WTP was observed.",
        evidenceClass: "RECORDED"
      },
      dominantBlocker: "Legitimate authenticated access to a sufficiently powered set of qualifying producers.",
      nextDiscriminator: "Only after legitimate access exists, execute the already-bounded paid-pilot exposure test without changing the proposition opportunistically.",
      reactivationCondition: "A legitimate authenticated outreach or native decision surface that can expose the unchanged proposition to qualifying producers with observable delivery.",
      dimensions: {
        resolution: {
          state: "MEDIUM",
          evidenceClass: "DERIVED",
          evidence: "Experiment 013 supported a plausible decision aid and Experiment 014 specified a concrete four-week paid pilot and sample contents; no actor validated the resolution.",
          nextObservation: "A qualifying actor's response to the unchanged sample and offer.",
          blocker: "Resolution usefulness never reached valid actor exposure."
        },
        access: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          evidence: "Public prospects could be identified, but legitimate authenticated outreach could not be executed in the available setup.",
          nextObservation: "Verified delivery through a legitimate authenticated channel.",
          blocker: "No valid exposure channel."
        },
        adoption: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "No qualifying producer received the treatment, so workflow fit, repeat use, and purchasing/repricing adoption were not observed.",
          nextObservation: "Observed use of the brief in an actual purchasing or repricing decision.",
          blocker: null
        },
        control: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          feasibility: "BLOCKED",
          evidence: "The experiment stopped rather than fabricate authentication, delivery, responses, or a participant.",
          nextObservation: "A separately authorized execution with verified authenticated capability.",
          blocker: "Execution capability and valid exposure were absent."
        },
        regulatory: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "The historical chain did not establish the legal, tax, advisory, or commercial obligations of a paid recurring brief.",
          nextObservation: "Only if the commercial test becomes executable, bound the obligations relevant to that exact offer.",
          blocker: null
        },
        economic: {
          state: "MEDIUM",
          evidenceClass: "DERIVED",
          evidence: "A direct audience, explicit paid-pilot offer, price, and transaction criterion were specified, but valid exposure, WTP, payment, repeatability, and value capture remain unobserved.",
          nextObservation: "Behavioral commitment to the bounded paid pilot; actual payment remains the transaction threshold.",
          blocker: "Access failure prevents interpreting demand."
        }
      },
      known: [
        "The candidate survived Experiment 013 as the strongest of that bounded commercial translation set.",
        "Experiment 014 specified an explicit paid manual pilot and distinguished replies from payment intent.",
        "The attempted experiment did not obtain valid market exposure."
      ],
      unknowns: [
        "Whether any qualifying producer would pay.",
        "Whether the brief would change purchasing or repricing behavior.",
        "Transaction, repeatability, unit economics, and value capture.",
        "Offer-specific regulatory and operating obligations."
      ],
      unprovenClaims: [
        "That zero observed commitments indicate no demand.",
        "That the intended producer is an observed buyer/payer.",
        "That a recurring cocoa brief is commercially viable or scalable."
      ],
      experiments: [
        {
          id: "013",
          phase: "Commercial translation",
          disposition: "ADVANCED COCOA",
          effect: "Selected cocoa as the most plausible candidate for a cheap commercial test.",
          source: "specs/013-commercial-translation-pressure-test.md"
        },
        {
          id: "014",
          phase: "Paid-pilot / WTP intent",
          disposition: "D — INVALID",
          effect: "Public prospects were identifiable, but valid authenticated outreach/exposure was not obtained; no demand conclusion followed.",
          source: "specs/014-cocoa-paid-pilot.md"
        }
      ],
      sources: [
        "docs/LEARNING_CHECKPOINT_001_019.md",
        "docs/STRATEGIC_CHECKPOINT_001_029.md",
        "docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    },
    {
      id: "ev-smart-charging",
      name: "UK EV smart-charging compatibility",
      experimentRange: "019→020",
      evidenceHorizon: "Through Experiment 020; checkpoint dated 2026-09-02",
      lifecycle: {
        state: "TERMINAL",
        evidenceClass: "DERIVED",
        reason: "The configuration-level problem is real and recoverable, but BecSpec already performs substantially the same bounded UK resolution. The residual-resolution thesis was falsified under the historical evidence.",
        historicalDisposition: "Experiment 020: C — FAIL; opportunity family PARKED."
      },
      significance: "Pre-purchase charging and tariff compatibility can materially affect EV charging cost and usability, but the tested market already had an adequate bounded resolver.",
      thesis: "AE could resolve configuration-specific UK EV smart-charging compatibility from fragmented authoritative evidence better than the market.",
      actor: {
        state: "KNOWN",
        value: "UK EV owner or buyer evaluating vehicle, charger, tariff, and household configuration before purchase or switching.",
        evidenceClass: "DERIVED"
      },
      beneficiary: {
        state: "KNOWN",
        value: "The consumer avoiding an incompatible charging/tariff configuration.",
        evidenceClass: "DERIVED"
      },
      buyerPayer: {
        state: "UNKNOWN",
        value: "No buyer/payer for an AE resolution was established before exact competition terminated the chain.",
        evidenceClass: "UNKNOWN"
      },
      dominantBlocker: "No demonstrated residual resolution gap: BecSpec already supplies substantially the contemplated answer.",
      nextDiscriminator: "None for this historical thesis. A materially different unresolved decision or differentiated distribution/value-capture advantage would constitute a new hypothesis, not continuation by feature expansion.",
      reactivationCondition: null,
      dimensions: {
        resolution: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          evidence: "Experiment 019 showed recoverability, but Experiment 020 found an adequate functionally equivalent resolver.",
          nextObservation: null,
          blocker: "Residual resolution gap falsified."
        },
        access: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "The chain stopped at exact-resolution competition before a bounded access experiment became decision-relevant.",
          nextObservation: null,
          blocker: null
        },
        adoption: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "AE-specific adoption was not tested because the artifact hypothesis terminated first.",
          nextObservation: null,
          blocker: null
        },
        control: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "No actor-facing control test was warranted after the exact-resolution kill.",
          nextObservation: null,
          blocker: null
        },
        regulatory: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "No opportunity-specific regulatory path was established before termination.",
          nextObservation: null,
          blocker: null
        },
        economic: {
          state: "FAR",
          evidenceClass: "DERIVED",
          evidence: "The underlying decision is economically consequential, but no differentiated resolution, buyer/payer, exchange path, WTP, or value capture was established.",
          nextObservation: null,
          blocker: "Adequate exact competition prevents advancement of this thesis."
        }
      },
      known: [
        "Configuration-specific compatibility uncertainty is real and often recoverable.",
        "Experiment 019 resolved 9 of 10 representative configurations from authoritative evidence.",
        "BecSpec already performed substantially the same bounded decision-resolution function."
      ],
      unknowns: [
        "Buyer/payer and economic exchange were never tested.",
        "No claim is made about every possible future EV decision problem."
      ],
      unprovenClaims: [
        "That the problem itself is fake.",
        "That all EV-related opportunities are terminal.",
        "That adding features would create differentiated value."
      ],
      experiments: [
        {
          id: "019",
          phase: "Evidence feasibility",
          disposition: "TECHNICALLY RECOVERABLE",
          effect: "Resolved 9 of 10 representative configurations and exposed maintenance burden.",
          source: "specs/019-ev-configuration-evidence-feasibility.md"
        },
        {
          id: "020",
          phase: "Exact-resolution competition",
          disposition: "C — FAIL / PARKED",
          effect: "BecSpec falsified the inadequate-existing-resolution premise for the tested function.",
          source: "docs/LEARNING_CHECKPOINT_020.md"
        }
      ],
      sources: [
        "docs/LEARNING_CHECKPOINT_001_019.md",
        "docs/LEARNING_CHECKPOINT_020.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    },
    {
      id: "canadian-counter-tariff",
      name: "Canadian counter-tariff exposure brief",
      experimentRange: "023→027",
      evidenceHorizon: "Through Experiment 027; checkpoints dated 2026-09-02",
      lifecycle: {
        state: "DORMANT",
        evidenceClass: "DERIVED",
        reason: "The asymmetry and resolution survived, but relevant importer decisions were not reachable through a legitimate low-friction repeatable surface.",
        historicalDisposition: "Experiment 027: C — DISTRIBUTION NOT FEASIBLE ENOUGH / PARK."
      },
      significance: "A wrong tariff treatment can change landed cost, purchasing, and repricing decisions for Canadian SME importers.",
      thesis: "Given an already-classified tariff item and bounded shipment facts, AE can provide a trustworthy, decision-ready exposure brief before commitment or repricing.",
      actor: {
        state: "KNOWN CLASS",
        value: "Canadian SME importer or buyer facing a live September 8 counter-tariff decision.",
        evidenceClass: "RECORDED"
      },
      beneficiary: {
        state: "KNOWN CLASS",
        value: "The importing organization exposed to tariff cost and compliance uncertainty.",
        evidenceClass: "DERIVED"
      },
      buyerPayer: {
        state: "UNKNOWN",
        value: "The importer is economically affected, but no AE buyer/payer, budget, procurement authority, or exchange mechanism was observed.",
        evidenceClass: "UNKNOWN"
      },
      dominantBlocker: "No accessible decision surface combining live importer intent, legitimate reach, and repeatable experimental throughput.",
      nextDiscriminator: "Whether a legitimate low-friction importer-access channel becomes available while the tariff decision is still live.",
      reactivationCondition: "A new legitimate importer-access channel or materially changed distribution fact that permits pre-decision exposure and observable effect.",
      dimensions: {
        resolution: {
          state: "NEAR",
          evidenceClass: "RECORDED",
          evidence: "Experiment 025 produced a correct decision-ready 12-line brief; all lines passed truth, provenance, boundary, arithmetic, and clarity checks.",
          nextObservation: "Actor comprehension and decision effect, once a valid surface exists.",
          blocker: null
        },
        access: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          evidence: "Broker/freight, association, search, community, government, and authenticated customs paths failed to combine relevant actor presence, timing, reachability, and throughput.",
          nextObservation: "A surface that legitimately exposes a qualifying importer before the decision closes.",
          blocker: "Gatekeeper permission, institutional trust, authenticated workflows, and sparse public intent."
        },
        adoption: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "No qualifying actor received the resolution, so workflow use, trust, action, and repeat behavior are unobserved.",
          nextObservation: "Use of the brief in a live commit/reprice decision.",
          blocker: null
        },
        control: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          feasibility: "BLOCKED",
          evidence: "Experiment 026 stopped at the authorization/acquisition boundary and sent no outreach; Experiment 027 found no sufficiently feasible independent path.",
          nextObservation: "A separately authorized bounded interaction only after channel feasibility changes.",
          blocker: "No legitimate, repeatable independent intervention path."
        },
        regulatory: {
          state: "MEDIUM",
          evidenceClass: "RECORDED",
          feasibility: "REVIEW REQUIRED",
          evidence: "The resolution used current authoritative tariff schedules but preserved material origin, remission, and exception uncertainty requiring case-specific verification.",
          nextObservation: "Verify the bounded shipment's origin/remission facts against authoritative rules or a qualified broker where required.",
          blocker: "Case-specific customs facts can remain material."
        },
        economic: {
          state: "FAR",
          evidenceClass: "DERIVED",
          evidence: "Economic consequence is concrete and resolution cost was low, but no actor effect, buyer/payer, exchange path, WTP, transaction, repeatability, or capture was observed.",
          nextObservation: "First establish valid actor access and resolution effect; a payment test before that would be uninterpretable.",
          blocker: "Access precedes a legitimate exchange discriminator."
        }
      },
      known: [
        "A material exact functional gap existed in tested public resolvers.",
        "A correct disposable decision-ready resolution was constructed cheaply.",
        "The bounded distribution search found no acceptable independent decision surface."
      ],
      unknowns: [
        "Whether a genuine importer would understand, trust, or act on the brief.",
        "Whether an importer or intermediary would pay for it.",
        "Economic effect, transaction, repeatability, and value capture."
      ],
      unprovenClaims: [
        "That the resolution lacks value.",
        "That affected importers are reachable at acceptable cost.",
        "That the economically affected importer is an AE buyer/payer."
      ],
      experiments: [
        { id: "023", phase: "Opportunity discovery", disposition: "ONE BOUNDED UNCERTAINTY", effect: "Identified a concrete actor, decision, consequence, and potential resolution gap.", source: "docs/LEARNING_CHECKPOINT_023.md" },
        { id: "024", phase: "Functional benchmark", disposition: "GAP DEMONSTRATED", effect: "A 20-case benchmark showed no tested resolver consistently produced the complete bounded decision output.", source: "docs/LEARNING_CHECKPOINT_024.md" },
        { id: "025", phase: "Disposable resolution", disposition: "A — DECISION-READY", effect: "Constructed and validated the 12-line exposure brief.", source: "experiments/025/canadian-counter-tariff-exposure-brief.md" },
        { id: "026", phase: "Actor interaction acquisition", disposition: "D — INVALID / NOT OBTAINED", effect: "No qualifying participant; no outreach or behavioral inference.", source: "docs/LEARNING_CHECKPOINT_026.md" },
        { id: "027", phase: "Distribution feasibility", disposition: "C — PARK", effect: "No low-friction repeatable accessible decision surface was found.", source: "docs/LEARNING_CHECKPOINT_027.md" }
      ],
      sources: [
        "experiments/025/canadian-counter-tariff-exposure-brief.md",
        "docs/LEARNING_CHECKPOINT_023.md",
        "docs/LEARNING_CHECKPOINT_024.md",
        "docs/LEARNING_CHECKPOINT_025.md",
        "docs/LEARNING_CHECKPOINT_026.md",
        "docs/LEARNING_CHECKPOINT_027.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    },
    {
      id: "customized-crm",
      name: "Customized CRM stay / upgrade / migrate decision",
      experimentRange: "028→030",
      evidenceHorizon: "Through final Experiment 030 observation on 2026-09-05",
      lifecycle: {
        state: "DORMANT",
        evidenceClass: "DERIVED",
        reason: "The historical actor decision received a public resolution, but actor exposure and effect remained unknowable; the fixed experiment is closed and cannot be treated as currently live.",
        historicalDisposition: "Experiment 030: D — measurement-limited interaction; surface publication confirmed, actor exposure UNKNOWN."
      },
      significance: "The actor reported unaffordable CRM growth economics, migration risk, and a customized system-of-record dependency for a 12-person business.",
      thesis: "A bounded workflow-parity and written-quote discriminator can compress a broad CRM choice into defensible stay, upgrade, or migrate branches.",
      actor: {
        state: "KNOWN",
        value: "The small-business owner operating the customized Salesforce environment.",
        evidenceClass: "RECORDED"
      },
      beneficiary: {
        state: "KNOWN",
        value: "The 12-person business whose workflows, costs, and migration risk depend on the decision.",
        evidenceClass: "RECORDED"
      },
      buyerPayer: {
        state: "UNKNOWN FOR AE",
        value: "The actor buys CRM products, but no evidence identifies them as buyer/payer for an AE decision aid.",
        evidenceClass: "DERIVED"
      },
      dominantBlocker: "No observable actor-exposure/effect path; delivery to the public surface did not establish that the actor saw the resolution.",
      nextDiscriminator: "For a future distinct case, require an authorized surface with observable exposure/effect before executing a bounded decision intervention.",
      reactivationCondition: "A new live CRM decision with a legitimate same-surface path that can establish exposure and effect; do not reopen the closed actor interaction.",
      dimensions: {
        resolution: {
          state: "NEAR",
          evidenceClass: "RECORDED",
          evidence: "Experiment 029 produced a defensible public-evidence decision brief with three credible branches and explicit private unknowns.",
          nextObservation: "Actor correction, acceptance, or use of the workflow-parity and quote tests in a distinct valid case.",
          blocker: null
        },
        access: {
          state: "MEDIUM",
          evidenceClass: "RECORDED",
          evidence: "Same-surface publication and a stable permalink were verified, but actor exposure was not observable.",
          nextObservation: "Qualifying actor-dependent response or another logically sufficient exposure signal in a future case.",
          blocker: "Surface access and delivery did not provide actor-exposure observability."
        },
        adoption: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "No post-intervention actor action, shortlist change, confidence change, workflow test, quote request, or migration decision was observable.",
          nextObservation: "An actor-stated next action or observed downstream decision behavior in a future valid case.",
          blocker: null
        },
        control: {
          state: "MEDIUM",
          evidenceClass: "RECORDED",
          feasibility: "BOUNDED",
          evidence: "Exactly one authorized public reply was executed within controls; no follow-up or broader contact occurred. The historical interaction is closed.",
          nextObservation: "A separately specified and authorized future case; no reopening of Experiment 030.",
          blocker: "The fixed surface lacked exposure observability."
        },
        regulatory: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "No legal, privacy, data-migration, or sector-specific regulatory assessment was performed for the actor's private implementation.",
          nextObservation: "Bound only the requirements material to a future selected branch and private data context.",
          blocker: null
        },
        economic: {
          state: "FAR",
          evidenceClass: "DERIVED",
          evidence: "The underlying CRM decision has material cost, but actor effect, buyer/payer for AE, economic effect, WTP, transaction, repeatability, and capture remain unestablished.",
          nextObservation: "First obtain valid actor-effect evidence in a distinct case; only then determine whether an exchange hypothesis is legitimate.",
          blocker: "Decision delivery did not cross the actor-effect boundary."
        }
      },
      known: [
        "The public actor exposed a detailed, still-changeable CRM decision and material affordability boundary.",
        "A disposable resolution reduced the option space to three evidence-linked branches.",
        "The reply was publicly available, but no fixed-actor response was observed during the bounded window."
      ],
      unknowns: [
        "Actor exposure, comprehension, trust, framing change, shortlist change, confidence change, and next action.",
        "Private workflow parity and actual commercial terms.",
        "Economic effect, AE buyer/payer, WTP, transaction, repeatability, and value capture."
      ],
      unprovenClaims: [
        "That public publication reached the actor.",
        "That silence indicates attention, comprehension, trust, or value failure.",
        "That the CRM buyer is an AE buyer/payer."
      ],
      experiments: [
        { id: "028", phase: "Actor-first discovery", disposition: "ADVANCED", effect: "Found a same-surface live decision with material consequence and recoverable public evidence.", source: "docs/LEARNING_CHECKPOINT_028.md" },
        { id: "029", phase: "Disposable resolution", disposition: "DECISION-READY", effect: "Compressed the choice into three credible branches and decision-sensitive checks.", source: "experiments/029/customized-crm-decision-brief.md" },
        { id: "030", phase: "Same-surface interaction", disposition: "D — MEASUREMENT-LIMITED", effect: "Verified public delivery; actor exposure, M1–M6, and material decision effect remained UNKNOWN.", source: "experiments/030/interaction-record.md" }
      ],
      sources: [
        "docs/LEARNING_CHECKPOINT_028.md",
        "docs/LEARNING_CHECKPOINT_029.md",
        "experiments/029/customized-crm-decision-brief.md",
        "experiments/030/interaction-record.md",
        "experiments/043/interaction-topology-and-agency-provenance.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    },
    {
      id: "superset-hierarchy",
      name: "Superset hierarchy sequencing decision",
      experimentRange: "032→035",
      evidenceHorizon: "Through final Experiment 035 observation on 2026-09-06",
      lifecycle: {
        state: "REVIEW",
        evidenceClass: "DERIVED",
        reason: "The bounded decision effect is established, but repository evidence does not establish current project state after the observation horizon or a commercial opportunity topology.",
        historicalDisposition: "Experiment 035: A — MATERIAL DECISION EFFECT OBSERVED; outcome class REFINEMENT."
      },
      significance: "The sequencing decision affected implementation/rework risk for an open-source hierarchical drill-down proposal and its reference implementation.",
      thesis: "Ship chart-local hierarchy now with a narrow source-resolution boundary if cheap, rather than waiting for an unspecified semantic hierarchy contract.",
      actor: {
        state: "KNOWN / AUTHORITATIVE FOR OWN PROPOSAL",
        value: "SIP-225 proposal author and project decision participant `tomerkl65`.",
        evidenceClass: "RECORDED"
      },
      beneficiary: {
        state: "KNOWN CLASS",
        value: "Superset project participants and users affected by delivery timing and future migration/rework.",
        evidenceClass: "DERIVED"
      },
      buyerPayer: {
        state: "UNKNOWN",
        value: "No buyer, payer, procurement authority, budget, or exchange mechanism for an AE resolution was identified.",
        evidenceClass: "UNKNOWN"
      },
      dominantBlocker: "No current repository-grounded downstream implementation state or economic topology beyond the 2026-09-06 evidence horizon.",
      nextDiscriminator: "If separately authorized and still decision-relevant, observe whether the explicit source/resolve seam and ordered-level abstraction entered the implementation or formal disposition.",
      reactivationCondition: null,
      dimensions: {
        resolution: {
          state: "NEAR",
          evidenceClass: "RECORDED",
          evidence: "Experiment 034 produced an S2 decision-ready resolution; Experiment 035's fixed actor endorsed the direction, supplied implementation facts, and refined the output contract.",
          nextObservation: "Repository-grounded downstream adoption of the refined seam, if a later experiment is separately justified.",
          blocker: null
        },
        access: {
          state: "NEAR",
          evidenceClass: "RECORDED",
          evidence: "The same public issue carried the decision, intervention, and an authoritative actor response explicitly tied to the resolution.",
          nextObservation: null,
          blocker: null
        },
        adoption: {
          state: "MEDIUM",
          evidenceClass: "DERIVED",
          evidence: "The actor stated ship-now intent and a concrete contract refinement, but formal SIP adoption, code change, merge, shipping, and end-user effect were not observed.",
          nextObservation: "A formal issue/PR/code disposition attributable to the decision state.",
          blocker: "Stated next action is not observed downstream implementation."
        },
        control: {
          state: "NEAR",
          evidenceClass: "RECORDED",
          feasibility: "BOUNDED",
          evidence: "One authorized public comment and one final read-only check produced interpretable response evidence without follow-up.",
          nextObservation: null,
          blocker: null
        },
        regulatory: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "The historical decision concerned open-source architecture; no opportunity-specific legal/licensing/compliance analysis was performed.",
          nextObservation: "Only if a future economic hypothesis makes a specific obligation decision-relevant.",
          blocker: null
        },
        economic: {
          state: "FAR",
          evidenceClass: "RECORDED",
          evidence: "A material actor decision-state effect exists, but downstream implementation, end-user effect, economic effect, buyer/payer, WTP, transaction, repeatability, and value capture remain unestablished.",
          nextObservation: "First distinguish downstream implementation/end-user effect from a separate commercial opportunity; do not infer a payer from project authority.",
          blocker: "No buyer/payer or exchange topology."
        }
      },
      known: [
        "No concrete near-term semantic hierarchy contract required waiting at the evidence horizon.",
        "The actor explicitly engaged the intervention's source/resolve seam and supplied missing implementation state.",
        "The actor's response materially refined the decision framing and stated next action."
      ],
      unknowns: [
        "Formal consensus, code adoption, merge/shipping, and end-user effect.",
        "Current project state beyond the 2026-09-06 repository evidence horizon.",
        "Buyer/payer, economic effect, WTP, transaction, repeatability, and value capture."
      ],
      unprovenClaims: [
        "Verified human-only authorship of the response.",
        "Formal implementation or project adoption.",
        "That an open-source decision participant is an AE buyer/payer.",
        "Economic value or value capture."
      ],
      experiments: [
        { id: "032", phase: "Actor-observable discovery", disposition: "B — ONE BOUNDED UNCERTAINTY", effect: "Selected the live Superset sequencing decision with strong same-surface effect observability.", source: "experiments/032/actor-observable-decision-surface-discovery.md" },
        { id: "033", phase: "Dependency discriminator", disposition: "B — DIRECTION CONCRETE", effect: "Found no current hierarchy contract or reliable landing path; favored ship-now with a boundary.", source: "experiments/033/superset-semantic-hierarchy-dependency-check.md" },
        { id: "034", phase: "Disposable resolution", disposition: "A — DECISION-READY", effect: "Constructed the S2 sequencing resolution and bounded stop rule.", source: "experiments/034/superset-disposable-sequencing-resolution.md" },
        { id: "035", phase: "Actor-facing interaction", disposition: "A — MATERIAL DECISION EFFECT", effect: "Actor endorsed the direction, supplied implementation state, and refined the source/resolve contract.", source: "experiments/035/superset-actor-facing-resolution-test.md" }
      ],
      sources: [
        "experiments/032/actor-observable-decision-surface-discovery.md",
        "experiments/033/superset-semantic-hierarchy-dependency-check.md",
        "experiments/034/superset-disposable-sequencing-resolution.md",
        "experiments/035/superset-actor-facing-resolution-test.md",
        "experiments/043/interaction-topology-and-agency-provenance.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    },
    {
      id: "realtime-migration",
      name: "Production gpt-realtime-2.1 migration",
      experimentRange: "046→048",
      evidenceHorizon: "Through Experiment 048 status resolution on 2026-09-16",
      lifecycle: {
        state: "DORMANT",
        evidenceClass: "DERIVED",
        reason: "The candidate retained one actor-held bounded discriminator, but public delivery of the evidence request could not be established and the fixed surface became inaccessible or private.",
        historicalDisposition: "Experiment 047: P2 actor-held bounded discriminator; Experiment 048 closed DELIVERY UNKNOWN."
      },
      significance: "The actor reported a production migration with reliability, tool-use, and migration-labor consequences before a stated shutdown date.",
      thesis: "A small anonymized paired outcome matrix could distinguish bounded configuration/contract adaptation from a broader capability or roadmap dependency.",
      actor: {
        state: "KNOWN ACCOUNT / DIRECT AUTHORITY FOR OWN MIGRATION",
        value: "`WebPlanning_SIM-Ltd`, authoritative only for its own production qualification and migration decision.",
        evidenceClass: "RECORDED"
      },
      beneficiary: {
        state: "KNOWN CLASS",
        value: "The actor's operating organization and its production-agent users/customers, without claims about private identities.",
        evidenceClass: "DERIVED"
      },
      buyerPayer: {
        state: "UNKNOWN",
        value: "An organizational payer is plausible but no procurement authority, budget, offer, or AE exchange path was evidenced.",
        evidenceClass: "UNKNOWN"
      },
      dominantBlocker: "The actor-held paired discriminator was not obtained; the submitted request's public delivery/moderation outcome is unknowable.",
      nextDiscriminator: "Only if a new specification and authorization are earned after legitimate surface access returns, obtain the already-defined anonymized paired aggregate evidence without requesting new tests or confidential material.",
      reactivationCondition: "A legitimate observable thread/surface plus fresh authorization, with the original decision still live and the bounded matrix still missing.",
      dimensions: {
        resolution: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          evidence: "The public aggregate claim is insufficient to distinguish localized bounded adaptation from broad capability dependency; the required matrix is actor-held.",
          nextObservation: "Existing per-intent paired counts, rubric/threshold, target reasoning setting, tool-choice mode, retry policy, and bounded outcome breakdown.",
          blocker: "Missing actor-held discriminator."
        },
        access: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          evidence: "The third attempt was submitted under CIF84 but entered moderation; a later single check returned page-not-found/private and could not establish public delivery.",
          nextObservation: "No further check is authorized. Reactivation requires a new legitimate observable path and separate authorization.",
          blocker: "Delivery status and fixed-surface availability cannot be established."
        },
        adoption: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          evidence: "No qualifying actor response, migration action, or downstream production outcome was observable.",
          nextObservation: "A stated migration disposition or observed downstream action after a valid resolution, if ever separately tested.",
          blocker: null
        },
        control: {
          state: "BLOCKED",
          evidenceClass: "RECORDED",
          feasibility: "BLOCKED",
          evidence: "Two authentication failures preceded one authorized submission; the moderation outcome remained unknowable and the experiment closed without delivery verification.",
          nextObservation: "A future attempt would require restored legitimate capability, fresh controls, a new specification if the treatment changes, and fresh authorization.",
          blocker: "Platform delivery/observability failure."
        },
        regulatory: {
          state: "UNKNOWN",
          evidenceClass: "UNKNOWN",
          feasibility: "UNKNOWN",
          evidence: "No regulatory/compliance assessment of the actor's private production system was performed; confidential materials were explicitly excluded.",
          nextObservation: "Only candidate-specific obligations made relevant by a later valid resolution may be assessed.",
          blocker: null
        },
        economic: {
          state: "FAR",
          evidenceClass: "DERIVED",
          evidence: "Production reliability and migration labor are economically consequential, but resolution, actor effect, buyer/payer, economic effect, WTP, transaction, repeatability, and value capture remain unestablished.",
          nextObservation: "The paired discriminator must first make a resolution possible; payment intent cannot substitute for it.",
          blocker: "Pre-resolution evidence gap and delivery ambiguity."
        }
      },
      known: [
        "The actor publicly reported a same-corpus aggregate comparison and unresolved migration decision.",
        "The missing evidence can be expressed as a narrow anonymized aggregate matrix plausibly already held by the actor.",
        "The public request was submitted once, but public approval/delivery was never verified."
      ],
      unknowns: [
        "Public delivery, exposure, semantic engagement, and actor response.",
        "The paired per-intent outcomes and evaluation/configuration fields.",
        "Migration action, economic effect, buyer/payer, WTP, transaction, and value capture.",
        "Authorship provenance."
      ],
      unprovenClaims: [
        "That the treatment was approved, rejected, removed, or seen.",
        "That the aggregate proves a model-wide capability or roadmap dependency.",
        "That the actor has OpenAI roadmap authority.",
        "That silence or inaccessible state indicates behavioral or value failure."
      ],
      experiments: [
        { id: "046", phase: "Fresh discovery", disposition: "HOLD — ONE BOUNDED DISCRIMINATOR", effect: "Found the production migration case; no FORGE handoff earned.", source: "experiments/046/fresh-opportunity-discovery-aligned-interaction-policy.md" },
        { id: "047", phase: "Discriminator feasibility", disposition: "P2 — ACTOR-HELD BUT BOUNDED", effect: "Defined the smallest defensible matrix and established that public construction would require invention.", source: "experiments/047/realtime-migration-discriminator-feasibility-check.md" },
        { id: "048", phase: "Bounded evidence request", disposition: "CLOSED — DELIVERY UNKNOWN", effect: "Preserved two failed attempts, one moderated submission, and one ambiguous status check without behavioral inference.", source: "experiments/048/bounded-realtime-migration-evidence-request.md" }
      ],
      sources: [
        "experiments/046/fresh-opportunity-discovery-aligned-interaction-policy.md",
        "experiments/047/realtime-migration-discriminator-feasibility-check.md",
        "experiments/048/bounded-realtime-migration-evidence-request.md",
        "experiments/050/economic-distance-to-value-audit.md"
      ]
    }
  ]
};
