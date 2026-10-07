/* Presentation only. Original fixtures remain byte-identical to frozen V2.
 * These summaries do not supply new evidence, identity, status or authority.
 */
window.OPERATOR_COPY = {
  frontiers: ["A problem was noticed", "Worth investigating", "Existing answers leave a gap", "An answer is ready to use", "Delivery was verified", "The person saw it", "Their decision was refined", "They acted on it", "An economic outcome changed", "Willingness to pay or exchange", "A transaction happened", "The result can be repeated", "AE gained value from it"],
  frontierStatus: {S:"Evidence supports it",R:"Evidence refutes the premise",N:"Test did not reach it",U:"Not known (UNKNOWN)"},
  states: {ACTIVE:"Active",DORMANT:"Paused until conditions change",REVIEW:"Needs reassessment",TERMINAL:"Ended for this tested idea",UNKNOWN:"Not known",BLOCKED:"Blocked",NEAR:"Near",MEDIUM:"Partway",FAR:"Far","CONTINGENT":"Depends on changed conditions","STRUCTURAL AT HORIZON":"The tested premise failed","UNRESOLVED":"Still unresolved","NO ACTION":"No action in the old test","BLOCKED / NO ACTION AVAILABLE":"Blocked; no useful action allowed","NEEDS DECISION":"A choice is needed","NEEDS AUTHORIZATION":"Permission is needed","PROGRESSING":"Work is in progress","WAITING":"Waiting until a set time"},
  dimensions: {resolution:"Is there a useful answer?",access:"Can we reach the person?",adoption:"Will they use it?",control:"Can we run a valid test?",regulatory:"Are the relevant obligations clear?",economic:"Can AE earn value?"},
  records: {
    "cocoa-paid-pilot": {
      idea:"A weekly brief might help small Czech chocolate producers decide when to buy cocoa and change prices.",
      decision:"We identified a type of producer, but no particular producer's decision was established.",
      why:"The paid-pilot idea remained plausible, but we could not reach suitable producers through a legitimate authenticated route.",
      condition:"A legitimate authenticated route to suitable producers must become available. Identify the actual producer and decision before counting a specific decision.",
      route:"Keep the idea if the underlying proposition is unchanged. A particular producer and decision must be evidenced first.",
      dimensions:["A brief and a four-week paid pilot were designed. No producer validated the answer.","Suitable producers could be found publicly, but valid delivery to them could not be carried out.","No suitable producer received the brief. Actual use and repeat use are not known.","The test stopped because valid authentication and delivery were unavailable; no response was invented.","Legal, tax, advisory and commercial obligations for the recurring paid brief were not established.","An audience, offer, price and payment criterion were specified. Willingness to pay, payment and repeatable earnings were not observed."],
      history:["Cocoa was selected as the most plausible idea for a cheap commercial test.","Prospects were found, but valid outreach did not happen. The test was invalid; it did not show a lack of demand."]
    },
    "ev-smart-charging": {
      idea:"Could AE give UK EV buyers a better answer about whether their vehicle, charger, tariff and household setup would work together?",
      decision:"We tested example configurations, not decisions attributed to particular EV owners.",
      why:"An existing service, BecSpec, already provided substantially the answer this idea proposed.",
      condition:"No condition for resuming the old idea was established. A material change in the existing answer or the decision would require a dated reassessment; the old failure verdict stays intact.",
      route:"A new decision needs its own supported owner and timing. Example configurations do not count as those decisions.",
      dimensions:["The answer could be assembled, but an adequate equivalent answer already existed.","Reaching an EV owner was not tested before the idea ended.","Use of AE's answer was not tested before the idea ended.","No test with an actual decision maker was warranted after the equivalent answer was found.","No obligations specific to this opportunity were established.","The decision can be costly, but AE's distinct advantage, buyer, payment path and earnings were not established."],
      history:["9 of 10 example configurations were resolved from authoritative evidence; maintenance work was also exposed.","BecSpec already supplied the tested answer. The premise that existing answers were inadequate failed."]
    },
    "canadian-counter-tariff": {
      idea:"Could a short, reliable tariff brief help a Canadian importer decide before committing to a shipment or changing prices?",
      decision:"The demonstration shipment was not an identified importer's real decision.",
      why:"The answer held up in testing, but we could not reliably reach suitable importers before their decisions.",
      condition:"Find a legitimate, repeatable way to reach an importer before the decision. Check that the rules, shipment facts and timing are still current.",
      route:"A different importer or regulatory time window means a new specific decision. Demonstration shipment lines remain tests of evidence.",
      dimensions:["A correct 12-line brief passed the evidence, arithmetic and clarity checks. An importer's understanding and response were not tested.","The searched routes did not combine a suitable importer, timely access and repeatable delivery.","No suitable importer received the answer; trust, use and repeat use are not known.","No outreach was sent. Permission and a legitimate, repeatable route remained barriers.","Official rules supported the brief, but origin, remission and exceptions still needed checks for the actual shipment.","Tariff costs mattered and the answer was cheap to produce. Effects, a payer, payment and repeatable earnings were not observed."],
      history:["The work identified a specific kind of tariff uncertainty and a possible gap in existing answers.","Across 20 test cases, no tested service consistently supplied the full answer needed.","A correct 12-line brief was built and checked.","The work stopped at the permission and access boundary; no outreach was sent.","No sufficiently feasible independent route to suitable importers was found."]
    },
    "customized-crm": {
      idea:"Help someone decide whether to stay with, upgrade or replace a customized Salesforce setup, using public evidence and explicit private unknowns.",
      decision:"u/Maleficent-Ad1562's stay, upgrade or migrate decision for customized Salesforce is identified in the historical record.",
      why:"The reply was published, but we could not tell whether the person saw it or changed anything. That interaction is closed.",
      condition:"A new live CRM case must allow us to observe whether the person sees the answer and what it changes. Do not reopen the closed interaction.",
      route:"A future case is a new specific decision. The old person's private outcome remains unknown.",
      dimensions:["A defensible brief offered three options, with checks and private unknowns made explicit.","Publication and a stable link were verified. Whether the person saw it is not known.","No later action, changed shortlist, confidence, workflow test, quote request or migration was observed.","One authorized public reply was made. No follow-up was permitted; the interaction is closed.","No assessment of the private system's legal, privacy, migration or sector obligations was performed.","The CRM choice involved material cost. AE's effect, payer, willingness to pay, payment and repeatable earnings were not established."],
      history:["A person described an important CRM decision that could still change, with useful public evidence.","The brief reduced the choice to three credible options and checks that could affect the choice.","Public delivery was verified. Whether the person saw, understood or acted on it remained unknown."]
    },
    "superset-hierarchy": {
      idea:"Help decide whether to ship chart-level hierarchy now, with a narrow boundary for later changes, rather than wait for an unspecified wider contract.",
      decision:"tomerkl65's sequencing decision for SIP-225 / #43331 is identified in the historical record.",
      why:"The person's response refined the decision, but later implementation and economic outcomes were not observed. The test is closed.",
      condition:"No condition for resuming a paused idea was established. Later implementation and economic consequences remain unobserved.",
      route:"Later evidence must concern the same owner, decision and time window. Saying what comes next is not proof it happened.",
      dimensions:["The answer was ready to use. The person endorsed its direction, supplied implementation facts and refined what the output should provide.","The same public issue contained the decision, answer and a directly related response from the responsible person.","The person stated an intention to ship and refined the contract. Formal adoption, code changes, merge, release and user effects were not observed.","One authorized comment and one final read-only check produced interpretable response evidence. There was no follow-up.","No legal, licensing or compliance analysis specific to this opportunity was performed.","A material change in the person's decision was observed. Implementation, economic benefit, a payer, payment and earnings were not established."],
      history:["A live Superset sequencing decision was selected where a response could be observed in the same issue.","No near-term wider hierarchy contract or reliable delivery path was found; shipping now with a narrow boundary was favored.","The sequencing answer and a limit on further work were prepared.","The person endorsed the direction, supplied implementation facts and refined the answer's contract."]
    },
    "realtime-migration": {
      idea:"A small comparison of paired results might show whether a production migration needs local setup changes or depends on broader model capabilities.",
      decision:"WebPlanning_SIM-Ltd's production qualification and migration decision is identified in the historical record.",
      why:"The request was submitted, but later access could not establish whether it was publicly delivered. No useful further action was authorized.",
      condition:"A legitimate route with observable delivery must return. The same decision must still be live, the paired results still missing, and fresh authorization must be given.",
      route:"It is the same decision only if owner, subject and timing remain supported. Otherwise its identity is unresolved or it is a new event.",
      dimensions:["The public totals were insufficient. The needed comparison was held by the person making the decision.","The submitted request entered moderation. A later check could not find a public page or verify delivery.","No suitable response, migration action or later production outcome was observed.","Two authentication failures preceded one authorized submission. Moderation remained unknown; the test closed without delivery verification.","No compliance assessment of the private production system was performed. Confidential material was excluded.","Reliability and migration labor matter economically. The answer, its effect, a payer, payment and AE earnings remain unestablished."],
      history:["The migration case was found. More evidence was needed before building an answer.","The smallest defensible comparison was defined. The person held the data; constructing it from public evidence would require invention.","Two failed attempts, one moderated submission and one ambiguous check were preserved. No conclusion about the person's behavior followed."]
    }
  },
  synthetic: {
    "synthetic-decision":{name:"Demonstration · choose what to learn next",why:"Two valid ways to test remain. The saved evidence cannot choose between their different learning goals.",action:"Choose which question matters next, or defer both.",inaction:"The made-up test stays paused. Nothing external happens and no evidence is lost.",movement:"A recorded human choice of which question to test."},
    "synthetic-authorization":{name:"Demonstration · allow or reject an interaction",why:"A made-up interaction has passed design review, but acting externally still requires explicit human permission.",action:"Allow exactly the proposed action, reject it, or leave it unexecuted.",inaction:"Nothing is posted and no permitted interaction is used.",movement:"Explicit permission, followed by fresh checks before acting."},
    "synthetic-progress":{name:"Demonstration · local analysis in progress",why:"A made-up local analysis is within the approved scope and has no unresolved exception.",action:"None, unless an exception or missing permission is raised.",inaction:"The made-up analysis continues until its agreed stopping point.",movement:"Completion, an exception, or a request for human judgment."},
    "synthetic-wait":{name:"Demonstration · wait until the agreed check",why:"A made-up interaction has an observation deadline that has not passed.",action:"Wait until the deadline. Do not check repeatedly, follow up or interpret silence.",inaction:"The waiting period stays undisturbed; the final check occurs only at the authorized time.",movement:"The agreed deadline, or relevant evidence already visible through an authorized check."}
  }
};
// Full primary-detail translation; exact original statements remain expandable.
Object.assign(window.OPERATOR_COPY.records["cocoa-paid-pilot"], {
  known:["Cocoa was the strongest idea in Experiment 013's selected commercial tests.","Experiment 014 specified a paid manual pilot, separating replies from intent to pay.","The attempted test did not validly reach suitable producers."],
  unknowns:["Would a suitable producer pay?","Would the brief change purchasing or pricing?","Payment, repeatability, costs per customer and AE's earnings.","Legal and operating obligations for this exact offer."],
  unproven:["That no observed commitments means no demand.","That the intended producer is an observed paying customer.","That a recurring cocoa brief is commercially viable or can scale."],
  barrier:"A legitimate authenticated way to reach enough suitable producers for a valid test.",
  next:"Only after valid access exists, test the already-defined paid pilot. Do not change the offer opportunistically.",
  roles:["An independent Czech chocolate or confectionery producer buying cocoa commercially.","The producer deciding about purchasing, inventory, margins and prices.","The producer was the intended customer, but valid exposure and willingness to pay were not observed."]
});
Object.assign(window.OPERATOR_COPY.records["ev-smart-charging"], {
  known:["Compatibility uncertainty is real and can often be resolved.","Experiment 019 resolved 9 of 10 example configurations using authoritative evidence.","BecSpec already supplied substantially the answer this idea proposed."],
  unknowns:["A buyer, payer and payment exchange were never tested.","This result makes no claim about every future EV decision."],
  unproven:["That the underlying problem is fake.","That every EV opportunity has ended.","That adding features would create a meaningful advantage."],
  barrier:"No gap in the available answer was demonstrated: BecSpec already supplied substantially the proposed answer.",
  next:"No next test for the old idea. A materially different decision, or a distinct delivery or earnings advantage, would be a new hypothesis.",
  roles:["A UK EV owner or buyer comparing a vehicle, charger, tariff and household setup before buying or switching.","The consumer avoiding an incompatible charging and tariff setup.","No payer for an AE answer was established before the equivalent existing service ended this line of work."]
});
Object.assign(window.OPERATOR_COPY.records["canadian-counter-tariff"], {
  known:["The tested public services left a material gap in the answer needed.","A correct, ready-to-use brief was produced cheaply.","The search found no acceptable independent way to reach the relevant decision maker."],
  unknowns:["Would a real importer understand, trust or use the brief?","Would an importer or intermediary pay?","Economic benefit, payment, repeatability and AE's earnings."],
  unproven:["That the answer lacks value.","That affected importers can be reached at acceptable cost.","That an importer affected by the cost would pay AE."],
  barrier:"No route combined a live importer decision, legitimate access and a repeatable rate of valid tests.",
  next:"Whether a legitimate, practical route to an importer becomes available while the decision can still change.",
  roles:["A Canadian small or medium importer or buyer facing the historical September 8 tariff decision.","The importing business affected by tariff costs and compliance uncertainty.","The importer faces costs, but no AE payer, purchasing authority, budget or payment mechanism was observed."]
});
Object.assign(window.OPERATOR_COPY.records["customized-crm"], {
  known:["The person described a detailed CRM choice that could still change, with a material affordability limit.","A one-off brief reduced the choice to three options linked to evidence.","The reply was publicly available, but no response from that person was observed during the agreed window."],
  unknowns:["Whether the person saw, understood or trusted it, changed their framing, shortlist or confidence, or took a next action.","Whether alternatives matched private workflows and what the actual commercial terms were.","Economic benefit, a payer for AE, willingness to pay, payment, repeatability and AE's earnings."],
  unproven:["That public posting reached the person.","That silence proves a lack of attention, understanding, trust or value.","That a buyer of CRM software would pay AE."],
  barrier:"Posting publicly did not let us observe whether the person saw the answer or what it changed.",
  next:"A different future case needs an authorized route that lets us observe whether the person sees the answer and its effect before an interaction is carried out.",
  roles:["The small-business owner operating the customized Salesforce setup.","The 12-person business whose workflows, costs and migration risk depend on the choice.","The person buys CRM products, but no evidence establishes that they would pay AE for a decision aid."]
});
Object.assign(window.OPERATOR_COPY.records["superset-hierarchy"], {
  known:["At the last recorded check, no concrete near-term wider hierarchy contract required waiting.","The person directly discussed the proposed boundary for finding data and supplied missing implementation facts.","Their response materially refined the decision and stated what they intended to do next."],
  unknowns:["Formal agreement, code adoption, merge, release and effects on users.","Project status after the recorded check on 2026-09-06.","A payer, economic benefit, willingness to pay, payment, repeatability and AE's earnings."],
  unproven:["That the response was written solely by a human.","That the proposal was formally adopted or implemented.","That an open-source decision participant would pay AE.","Economic value or AE earning value."],
  barrier:"Beyond the 2026-09-06 check, implementation status and a path from benefit to payment are not established by saved evidence.",
  next:"Only if separately authorized and still relevant, check whether the proposed boundary for finding data and ordered levels entered the implementation or a formal decision.",
  roles:["tomerkl65, author of the SIP-225 proposal and a participant in the project decision.","Superset participants and users affected by delivery timing and later migration or rework.","No AE buyer, payer, purchasing authority, budget or payment mechanism was identified."]
});
Object.assign(window.OPERATOR_COPY.records["realtime-migration"], {
  known:["The person reported totals comparing results on the same test material, with the migration decision unresolved.","The missing evidence can be a small anonymized comparison of paired results that the person plausibly already holds.","The public request was submitted once. Public approval and delivery were never verified."],
  unknowns:["Public delivery, whether the person saw or meaningfully engaged with the request, and any response.","Paired results for each task type and the evaluation and setup fields.","Migration action, economic benefit, a payer, willingness to pay, payment and AE's earnings.","Who or what authored the available material."],
  unproven:["That the request was approved, rejected, removed or seen.","That aggregate results prove a model-wide capability limit or a dependency on future plans.","That the person controls OpenAI's product plans.","That silence or an inaccessible page proves a behavioral or value failure."],
  barrier:"The needed paired comparison was not obtained, and public delivery or the moderation result cannot be established.",
  next:"Only after legitimate access returns and a new specification and permission are earned, obtain the already-defined anonymized paired results. Do not request new tests or confidential material.",
  roles:["WebPlanning_SIM-Ltd, with authority only over its own production qualification and migration decision.","Its operating business and production-agent users or customers; private identities are not established.","A business payer is plausible, but purchasing authority, budget, offer and a way to pay AE were not evidenced."]
});
