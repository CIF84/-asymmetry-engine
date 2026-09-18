/*
 * Experiment 052 manually authored control-state fixtures.
 *
 * Historical entries point to the frozen Experiment 051 opportunity fixtures.
 * They describe only repository-known state at the stated evidence horizon.
 * Synthetic entries exist solely to exercise control-plane states that the
 * historical fixtures cannot honestly supply. No state is calculated.
 */
window.CONTROL_PLANE_FIXTURES = {
  schemaVersion: "052-v1",
  evidenceBoundary: "Repository history through Experiment 051; no live-world freshness.",
  orderingRule: "Grouped by present control requirement, then stable fixture order; never ranked by value or urgency.",
  historical: [
    {
      id: "cocoa-paid-pilot",
      operationalState: "DORMANT",
      group: "dormant",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "The paid-pilot proposition survived translation, but no legitimate authenticated route to qualifying producers was available.",
      requestedAction: "None now. Reactivate only if a legitimate authenticated actor surface becomes available under a separately authorized experiment.",
      ifNoAction: "The opportunity remains dormant. Demand, value, and willingness to pay remain unknown; no negative demand inference follows.",
      movement: "Verified legitimate delivery to qualifying producers using the already-bounded proposition."
    },
    {
      id: "ev-smart-charging",
      operationalState: "NO ACTION",
      group: "safe",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "The historical residual-resolution thesis terminated after a functionally equivalent resolver was found.",
      requestedAction: "None for this thesis. A materially different unresolved decision would require a new hypothesis.",
      ifNoAction: "No current work is lost. NO ACTION describes the control state, not the opportunity's historical significance.",
      movement: "Only a materially different thesis with a distinct unresolved decision."
    },
    {
      id: "canadian-counter-tariff",
      operationalState: "DORMANT",
      group: "dormant",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "The resolution survived, but relevant importer decisions were not reachable through a legitimate repeatable surface.",
      requestedAction: "None now. Reactivate only when a legitimate low-friction surface can reach a qualifying importer decision.",
      ifNoAction: "The opportunity remains dormant; usefulness, adoption, economic effect, and value capture remain unproven.",
      movement: "A legitimate decision-proximate access surface with observable delivery."
    },
    {
      id: "customized-crm",
      operationalState: "DORMANT",
      group: "dormant",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "The bounded interaction was published, but actor exposure and all behavioral outcomes remained unknown when the experiment closed.",
      requestedAction: "Do not reopen the closed actor interaction. A future test requires a distinct live case with observable exposure.",
      ifNoAction: "The historical result remains delivery-unknown rather than becoming evidence of no value.",
      movement: "A new, independently authorized case with exposure observability designed before interaction."
    },
    {
      id: "superset-hierarchy",
      operationalState: "NO ACTION",
      group: "safe",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "The historical actor-facing test produced bounded decision-state refinement and is closed at its evidence horizon.",
      requestedAction: "None within this historical chain. Do not infer current live-world state or economic effect.",
      ifNoAction: "The established decision-state effect is preserved; downstream implementation and value capture remain unknown.",
      movement: "A separately specified economic or downstream-action hypothesis, if later supported."
    },
    {
      id: "realtime-migration",
      operationalState: "BLOCKED / NO ACTION AVAILABLE",
      group: "blocked",
      attentionType: "NO USEFUL CURRENT HUMAN ACTION",
      why: "The exact submitted treatment could not be located after moderation and public delivery remained unknown when Experiment 048 closed.",
      requestedAction: "None. Do not retry, poll, or infer actor behavior from inaccessible delivery state.",
      ifNoAction: "The candidate remains unresolved at delivery. Exposure, semantic engagement, actor effect, and economic effect remain unknown.",
      movement: "A new specification may be considered only if a legitimate, observable, non-duplicative decision surface exists."
    }
  ],
  synthetic: [
    {
      id: "synthetic-decision",
      name: "Synthetic · choose the next bounded discriminator",
      opportunityState: "ACTIVE",
      operationalState: "NEEDS DECISION",
      group: "attention",
      attentionType: "DECISION",
      why: "Two evidence-valid discriminators remain and repository evidence cannot choose between their different learning goals.",
      requestedAction: "Choose which learning question matters next, or explicitly defer both.",
      ifNoAction: "The hypothetical experiment remains paused; no external action occurs and no evidence is lost.",
      movement: "A recorded human choice of discriminator.",
      scenarioBoundary: "Interface exercise only. This is not an actual AE opportunity or pending decision."
    },
    {
      id: "synthetic-authorization",
      name: "Synthetic · authorize or reject a bounded interaction",
      opportunityState: "ACTIVE",
      operationalState: "NEEDS AUTHORIZATION",
      group: "attention",
      attentionType: "AUTHORIZATION",
      why: "A hypothetical same-surface interaction has passed design review, but consequential external action requires explicit human authority.",
      requestedAction: "Authorize exactly the bounded action, reject it, or leave it unexecuted.",
      ifNoAction: "Nothing is posted and no interaction allowance is consumed.",
      movement: "An explicit authorization decision followed by fresh pre-action controls.",
      scenarioBoundary: "Interface exercise only. No real interaction is prepared or authorized."
    },
    {
      id: "synthetic-progress",
      name: "Synthetic · bounded repository analysis in progress",
      opportunityState: "REVIEW",
      operationalState: "PROGRESSING",
      group: "safe",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "A hypothetical repository-only analysis is within approved scope and has no unresolved exception.",
      requestedAction: "None unless an exception or missing authority is surfaced.",
      ifNoAction: "The hypothetical analysis continues to its bounded freeze point.",
      movement: "Completion, exception, or a request for consequential judgment.",
      scenarioBoundary: "Interface exercise only. No background process or agent is running."
    },
    {
      id: "synthetic-wait",
      name: "Synthetic · predeclared external observation window",
      opportunityState: "ACTIVE",
      operationalState: "WAITING",
      group: "waiting",
      attentionType: "NO CURRENT HUMAN ACTION",
      why: "A hypothetical interaction has a fixed observation deadline that has not elapsed.",
      requestedAction: "Wait until the deadline; do not poll, follow up, or reinterpret silence.",
      ifNoAction: "The observation window remains uncontaminated and the final check occurs only at its authorized time.",
      movement: "The predeclared deadline or qualifying evidence already visible through an authorized observation.",
      scenarioBoundary: "Interface exercise only. No actual observation window is open."
    }
  ]
};
