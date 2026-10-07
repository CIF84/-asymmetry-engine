(function () {
  "use strict";
  const engine = window.ENGINE_FIXTURES, knowledge = window.OPPORTUNITY_FIXTURES, control = window.CONTROL_PLANE_FIXTURES;
  if (!engine || !knowledge || !control || !window.CONTRACT_EVIDENCE) { document.body.innerHTML = "<p>Saved records could not load. Counts are unavailable.</p>"; return; }
  const copy = window.OPERATOR_COPY;
  const rows = engine.rows;
  const byId = id => rows.find(r => r.id === id);
  const opportunity = id => knowledge.opportunities.find(o => o.id === id);
  const dimensions = ["resolution", "access", "adoption", "control", "regulatory", "economic"];
  const labels = {resolution:"Resolution",access:"Access",adoption:"Adoption",control:"Control",regulatory:"Regulatory",economic:"Economic"};
  const states = ["ACTIVE", "DORMANT", "REVIEW", "TERMINAL"];
  const esc = s => String(s ?? "").replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;").replaceAll("'","&#039;");
  const token = s => String(s).toLowerCase().replace(/[^a-z0-9]+/g,"-");
  const link = (path,label) => `<a href="../../../${esc(path)}" target="_blank" rel="noopener">${esc(label || path)}</a>`;
  const sourceLinks = paths => `<div class="sources">${[...new Set(paths)].map(p => link(p)).join("")}</div>`;
  const stateText = s => copy.states[s] || s;
  const pill = s => `<span class="pill state-${token(s)}" title="${esc(s)}">${esc(stateText(s))}</span>`;
  const precision = (title,body) => `<details class="precision"><summary>${esc(title)}</summary>${body}</details>`;
  const originalControl = item => precision("Original instruction and exact status",`<p><b>${esc(item.operationalState)}</b></p><dl>${[["Why",item.why],["Original instruction · historical or demonstration only",item.requestedAction],["If no action",item.ifNoAction],["Conditional movement",item.movement]].map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}</dl>`);
  const technicalList = (title,items) => precision(title,`<ul>${items.map(v=>`<li>${esc(v)}</li>`).join("")}</ul>`);
  const inspect = (id,label) => `<button class="inspect-button" type="button" data-record="${esc(id)}">${esc(label || "See what we learned →")}</button>`;
  const defaultSources = [engine.historicalSource, engine.fixtureSource, "experiments/054/review.md"];
  function frontierCounts(index) { return ["S","R","N","U"].map(s => rows.filter(r => r.frontier[index] === s).length); }
  function renderEngine() {
    document.getElementById("cohort-horizon").textContent = "Last recorded checks: Cocoa / EV / Canadian tariff: 2026-09-02; CRM: 2026-09-05; Superset: 2026-09-06; realtime: 2026-09-16. These are different dates, not today's status.";
    document.getElementById("frontier-method").innerHTML = `<p>Evidence frontier: independent assertions about six historical chain records. Denominator = 6 in every row. Rows overlap; there is no mandatory order and no conversion rate.</p><dl>${engine.frontierLabels.map((label,i)=>`<dt>${esc(copy.frontiers[i])}</dt><dd>${esc(label)}</dd>`).join("")}</dl><p>${Object.entries(engine.statuses).map(([key,value])=>`${esc(copy.frontierStatus[key])}: ${esc(value)}`).join(" · ")}</p>`;
    document.getElementById("dimension-method").innerHTML = `<dl>${dimensions.map(k=>`<dt>${esc(copy.dimensions[k])}</dt><dd>${esc(labels[k])}</dd>`).join("")}</dl><p>These are independent categorical interpretations, not a score or a prediction. Near (NEAR), Partway (MEDIUM), Far (FAR), Blocked (BLOCKED), Not known (UNKNOWN). UNKNOWN ≠ FAR; BLOCKED ≠ TERMINAL.</p><p>Active (ACTIVE): active at the recorded date. Paused until conditions change (DORMANT): conditional reopening only. Needs reassessment (REVIEW): the record needs review. Ended for this tested idea (TERMINAL): historical thesis ended, not every future opportunity in that area.</p>`;
    // These are display counts from manually authored fixtures, not automated admission/identity inference.
    document.querySelector('[data-audit="governed"]').innerHTML = `${engine.prospective.length} <span>records so far ↗</span>`;
    for (const [key,number] of [["families",rows.length],["instances",rows.filter(r=>r.instance).length],["unresolved",rows.filter(r=>!r.instance).length]]) document.querySelector(`[data-audit="${key}"] b`).textContent = number;
    document.getElementById("frontier").innerHTML = engine.frontierLabels.map((name,i) => {
      const counts = frontierCounts(i);
      const description = `${copy.frontiers[i]}: ${counts[0]} with supporting evidence, ${counts[1]} with the premise refuted, ${counts[2]} not reached in the test, ${counts[3]} not known; out of ${rows.length} past records. Explain this number.`;
      return `<button class="frontier-row" type="button" data-audit="front:${i}" aria-label="${esc(description)}" title="${esc(description)}"><span class="frontier-name">${esc(copy.frontiers[i])}</span><span class="frontier-bar" aria-hidden="true">${counts.map((n,j)=>`<span class="bar-${["S","R","N","U"][j]}" style="width:${n/rows.length*100}%"></span>`).join("")}</span><span class="frontier-count">${counts[0]}/${rows.length} ↗</span></button>`;
    }).join("");
    document.getElementById("lifecycle").innerHTML = ["family","instance"].map(unit => {
      const population = unit === "family" ? rows : rows.filter(r=>r.instance);
      return `<p class="distribution-label">${unit === "family" ? "6 opportunity ideas" : "3 specific decisions identified"}</p><div class="distribution">${states.map(state=>`<button type="button" data-audit="life:${unit}:${state}"><b>${population.filter(r => (unit === "family" ? opportunity(r.id).lifecycle.state : r.instanceState) === state).length}</b>${esc(stateText(state))} ↗</button>`).join("")}</div>`;
    }).join("");
    document.getElementById("blockers").innerHTML = `<div class="distribution">${["CONTINGENT","STRUCTURAL AT HORIZON","UNRESOLVED"].map(cat=>`<button type="button" data-audit="block:${cat}"><b>${rows.filter(r=>r.blocker===cat).length}</b>${esc(stateText(cat))} ↗</button>`).join("")}</div>`;
    document.getElementById("runs").innerHTML = engine.runs.map(r=>`<button type="button" data-audit="run:${r.id}">Experiment ${r.id}<br><strong>${r.candidates} candidates in this search ↗</strong></button>`).join("");
  }
  function descriptor(key) {
    const base = {population:"054 historical bounded cohort · six chain records", horizon:engine.horizon, derivation:"DERIVED from manually authored 054 assertions; no external refresh or global identity inference.", missingness:"Historical admissions UNKNOWN for all six; current external state unassessed. This cohort is partial, not the complete Engine.", sources:defaultSources, members:rows};
    if (key === "governed") return {...base,title:"Prospective governed population", result:`${engine.prospective.length} captured records`, unit:"Records captured prospectively under the 054 contract", population:"Governed prospective fixture population only; historical/synthetic/run records excluded", horizon:`Repository snapshot at 055 baseline, ${engine.capturedAt}`, derivation:engine.prospectiveBasis, missingness:"Zero represented governed records is not zero opportunities, zero demand, or zero discovery. Prospective use is untested.", sources:["STATUS.md","specs/055-engine-control-plane-v2.md","experiments/054/review.md"],members:[], empty:"No governed prospective records are represented. Historical evidence remains available separately."};
    if (key === "families") return {...base,title:"Represented historical family hypotheses",result:"6 family hypotheses",unit:"Bounded local family thesis labels; denominator six validation chain rows",derivation:"One bounded thesis per selected chain. Copied 051 referents retain 054 family/instance interpretations; no global market uniqueness claim."};
    if (key === "instances") return {...base,title:"Supported historical decision instances",result:"3 supported / 3 not established",unit:"Attributed owner + decision object + event/horizon; denominator six chain rows",members:rows.filter(r=>r.instance),missingness:"Cocoa, EV and Canadian actor/event identity is not established. Their class, sample configurations and demo manifest cannot supply decision instances."};
    if (key === "unresolved") return {...base,title:"Family-only records with unresolved instance identity",result:"3 unresolved family-only records",unit:"Chain records lacking a supported particular owner/event; denominator six",members:rows.filter(r=>!r.instance),missingness:"UNKNOWN/UNRESOLVED is neither zero real decisions nor three newly established instances. No merge/split or admission is inferred."};
    if (key === "attention") return {...base,title:"Actual current opportunity-attention load",result:"UNKNOWN",unit:"Current real opportunity tasks needing human judgment/permission; denominator UNKNOWN",population:"Complete current Engine attention population is not established",derivation:"054 contract rows have NO CURRENT EVIDENCE; 052 supplies only historical closed controls and synthetic exercises. STATUS is a separate project-operation pointer.",missingness:"No live/current attention inventory. Six scoped historical records cannot establish a whole-Engine load; synthetic attention requests excluded.",sources:[engine.fixtureSource,"experiments/052/debrief.md","STATUS.md"],memberNote:"Scoped historical records are listed to expose missing current evidence, not as current attention tasks."};
    if (key === "reactivation") return {...base,title:"Dormant family records with explicit reopening conditions",result:"4 / 4 dormant family records",unit:"Dormant family hypotheses with conditional reopening evidence; denominator four dormant families",members:rows.filter(r=>opportunity(r.id).lifecycle.state==="DORMANT"),missingness:"No blocker is claimed cleared. CRM requires a new live case; realtime continuity is conditional. No authorization is supplied.",memberNote:"Each condition is conditional and historically/semantically sourced."};
    if (key.startsWith("front:")) {
      const i=Number(key.split(":")[1]), counts=frontierCounts(i);
      return {...base,title:`Evidence assertion · ${engine.frontierLabels[i]}`,result:`${counts[0]} supported / ${counts[1]} premise refuted / ${counts[2]} not reached / ${counts[3]} UNKNOWN`,unit:"Historical chain records; denominator six; assertions overlap between rows",derivation:"Each chain's independent frontier cell is transcribed from 054 §25 and the six-case fixture. Counts within this assertion sum to six, not across assertions.",missingness:"UNKNOWN is absent/insufficient/unobserved evidence, not a negative outcome. Not reached records execution history, not absence of private effects. No conversion rate.",frontIndex:i};
    }
    if (key.startsWith("life:")) {
      const [,unit,state]=key.split(":"),population=unit==="family"?rows:rows.filter(r=>r.instance),members=population.filter(r=>(unit==="family"?opportunity(r.id).lifecycle.state:r.instanceState)===state);
      return {...base,title:`Historical ${unit} lifecycle · ${state}`,result:`${members.length} / ${population.length}`,unit:`${unit==="family"?"Family hypotheses":"Supported decision instances"}; denominator ${population.length}`,members,derivation:"DERIVED lifecycle assignments at each row's own historical horizon. CRM family DORMANT and instance REVIEW are separate scoped interpretations; old verdicts retained.",missingness:"No common-date current lifecycle, transition timestamps or dwell times. Three family-only rows excluded from instance distributions.",empty:`No ${state} ${unit} assignments in this scoped historical snapshot. This does not establish a current Engine zero.`};
    }
    if (key.startsWith("block:")) {
      const cat=key.slice(6),members=rows.filter(r=>r.blocker===cat);
      return {...base,title:`Primary historical blocker · ${cat}`,result:`${members.length} / 6 chain records`,unit:"Primary blocker interpretation per chain record; denominator six",members,derivation:"DERIVED: cocoa/Canadian/CRM/realtime contingent; EV structural for tested thesis at historical horizon; Superset unresolved downstream/economic frontier.",missingness:"Primary dispositions are not mutually exclusive individual causes. Realtime has both missing actor-held evidence and access ambiguity. No cleared blocker is inferred."};
    }
    if (key.startsWith("run:")) {
      const run=engine.runs.find(r=>r.id===key.slice(4));
      return {...base,title:`Experiment ${run.id} historical run telemetry`,result:`${run.candidates} run-local candidates`,unit:"Formed candidate attempts within one run; not unique opportunities",population:`Historical Experiment ${run.id} candidate ledger; separate from 054 cohort`,horizon:run.horizon,derivation:"Reported row/count arithmetic audited by 053. Candidate labels are run-local and formation gates vary across runs.",missingness:"Global candidate identity/admission/deduplication UNKNOWN. Do not combine these values into a unique-opportunity total or conversion rate.",members:[],sources:[run.source,"experiments/053/engine-state-funnel-semantics-audit.md#20-system-count-supportability-matrix"],empty:"Included units are that run's candidate ledger, accessible in the source artifact; they are not additional cohort families."};
    }
    throw new Error(`Unknown aggregate ${key}`);
  }
  function auditCopy(key,d) {
    const general={title:d.title,unit:"Each of the six selected past records describes one opportunity idea.",note:"The records ended at different dates. They do not establish today's full picture of AE. Whether they qualified for historical tracking is not known (UNKNOWN)."};
    const fixed={
      governed:["Records under the new recording rules","Only records made under the new rules count here; past work and demonstrations are excluded.","No new-rule records are represented. This does not mean no real opportunities, demand or discoveries. Using the new rules on new work remains untested."],
      families:["Six ideas from past work","One idea per selected chain of experiments; six chains in this sample.","An idea is not a particular person's decision. These local labels make no claim that each is unique across the market."],
      instances:["Which specific decisions are identified?","Three of the six records identify a decision's owner, subject and timing.","Cocoa, EV and Canadian tariff identify types of people or demonstrations, not supported particular decisions. These three are excluded from this list."],
      unresolved:["Which ideas lack an identified decision?","Three of the six records lack a supported particular decision owner and event.","Their decision identity is not known (UNKNOWN / UNRESOLVED). This is not evidence that no real decision exists."],
      attention:["What needs your attention today?","Today's real opportunity tasks are not counted: the total is unknown.","The saved records have no current evidence. Old instructions and made-up examples cannot establish today's tasks. Project work is shown separately."],
      reactivation:["What would let paused ideas resume?","Four of the four paused ideas have conditions for another test.","No condition is known to be met. CRM requires a new live case; realtime must still concern the same decision. No new action is authorized."]
    };
    if(fixed[key])return {title:fixed[key][0],unit:fixed[key][1],note:fixed[key][2]};
    if(key.startsWith("front:"))return {...general,title:copy.frontiers[Number(key.split(":")[1])],unit:"Six past records, one question. The same record can support other rows too.",note:"Not known (UNKNOWN) means evidence is absent, insufficient or unobserved; it is not a negative outcome. Not reached describes what the test did, not private effects. There is no conversion rate."};
    if(key.startsWith("life:")){const [,unit,state]=key.split(":");return {...general,title:`${unit==="family"?"Opportunity ideas":"Identified decisions"}: ${stateText(state)}`,unit:unit==="family"?"Out of six past opportunity ideas.":"Out of three identified decisions. The other three records lack a supported decision identity.",note:"Status is interpreted at each record's own date, not today. CRM's idea is paused but its particular decision needs reassessment; those are different scopes. Old verdicts remain intact."};}
    if(key.startsWith("block:"))return {...general,title:stateText(key.slice(6)),unit:"Main reason progress stopped, out of six past records.",note:"This groups the main reason per record, not every cause. A record can have several causes. No barrier is known to have cleared."};
    if(key.startsWith("run:"))return {...general,title:`Earlier search: Experiment ${key.slice(4)}`,unit:"Candidates within this one historical search, excluded from the six-record sample.",note:"Search rules differ. Candidate identities across searches are not established. Do not add these counts as unique opportunities or conversion rates."};
    return general;
  }
  function showAudit(key) {
    const d=descriptor(key),a=auditCopy(key,d),panel=document.getElementById("aggregate-audit");
    const result=d.result.replaceAll("family hypotheses","opportunity ideas").replaceAll("unresolved family-only records","ideas without an identified decision").replaceAll("dormant family records","paused ideas").replaceAll("run-local candidates","candidates in this search").replaceAll("captured records","records so far").replaceAll("premise refuted","with the premise refuted").replaceAll("supported","with supporting evidence").replaceAll("not established","not established").replaceAll("UNKNOWN","not known (UNKNOWN)");
    document.getElementById("audit-title").textContent=a.title;
    document.getElementById("audit-content").innerHTML=`<p class="audit-result"><strong>${esc(result)}</strong></p><p>${esc(a.unit)}</p><p>${esc(a.note)}</p><p><b>Dates covered:</b> ${esc(d.horizon===engine.horizon?document.getElementById("cohort-horizon").textContent:d.horizon)}</p><h3>Records behind this number</h3>${d.members.length?`<div class="member-list">${d.members.map(r=>`<button type="button" data-record="${r.id}">${esc(r.short)}${d.frontIndex!==undefined?` · ${esc(copy.frontierStatus[r.frontier[d.frontIndex]])}`:""}<small>${esc(r.horizon)}</small><small>${esc(copy.records[r.id].decision)} →</small></button>`).join("")}</div>`:`<p class="audit-empty">${esc(key==="governed"?"There are no records under the new rules yet; the separate past-work sample is still available.":key.startsWith("run:")?"The candidates are listed in that search’s original record below. They are not additional ideas in the six-record sample.":"No records match this past status in the selected sample. This does not establish today’s status.")}</p>`}
      ${precision("Exact counting terms, method and unknowns",`<dl class="audit-facts">${[["Result",d.result],["Unit / denominator",d.unit],["Population",d.population],["Evidence horizon",d.horizon],["Derivation",d.derivation],["Missingness",d.missingness]].map(([name,value])=>`<div><dt>${esc(name)}</dt><dd>${esc(value)}</dd></div>`).join("")}</dl>${d.memberNote?`<p>${esc(d.memberNote)}</p>`:""}`)}<h3>Original records and sources</h3>${sourceLinks(d.sources)}`;
    panel.hidden=false;panel.focus({preventScroll:true});panel.scrollIntoView({block:"start"});
  }
  const groupDefs=[{id:"attention",title:"A choice or permission is needed"},{id:"safe",title:"Completed; no action in the old test"},{id:"waiting",title:"Waiting for outside evidence"},{id:"blocked",title:"Blocked; no useful action allowed"},{id:"dormant",title:"Paused until conditions change"}];
  function controlCard(item,synthetic) {
    const o=synthetic?null:opportunity(item.id),r=synthetic?null:byId(item.id),text=synthetic?copy.synthetic[item.id]:copy.records[item.id];
    return `<article class="control-card"><span class="badge ${synthetic?"synthetic":""}">${synthetic?"MADE-UP EXAMPLE · NOT A REAL TASK":"PAST INSTRUCTION · NOT A TASK TODAY"}</span>${pill(item.operationalState)}<h4>${esc(o?o.name:text.name)}</h4>${r?`<p class="group-caption">${esc(r.horizon)} · today's status: not known (NO CURRENT EVIDENCE)</p>`:""}<p>${esc(text.why)}</p>${synthetic?`<dl><dt>Example request</dt><dd>${esc(text.action)}</dd><dt>If no action</dt><dd>${esc(text.inaction)}</dd><dt>What could change this</dt><dd>${esc(text.movement)}</dd></dl>`:`<p><b>Before another test:</b> ${esc(text.condition)}</p>`}${originalControl(item)}${inspect(item.id,"See instructions and evidence →")}</article>`;
  }
  function renderControls(items,synthetic) {
    return groupDefs.map(group=>{
      const selected=items.filter(i=>i.group===group.id);
      if(!selected.length)return "";
      return `<section class="control-group"><div><h3>${esc(group.title)}</h3><p class="group-caption">${selected.length} ${synthetic?"made-up examples; excluded from all counts":"past records; not tasks today"}</p></div><div class="control-cards">${selected.map(i=>controlCard(i,synthetic)).join("")}</div></section>`;
    }).join("");
  }
  function renderPossibility() {
    document.getElementById("opportunity-overview").innerHTML=rows.map(r=>{
      const o=opportunity(r.id);
      return `<article class="possibility-row"><div><h3>${esc(o.name)}</h3><span class="badge">${esc(o.experimentRange)}</span>${pill(o.lifecycle.state)}<p>${r.instance?"A specific past decision is identified":"A specific decision is not identified (UNRESOLVED)"}</p><p>${esc(r.horizon)}</p></div><div class="dimension-mini">${dimensions.map(k=>`<div><span>${esc(copy.dimensions[k])}</span><b>${pill(o.dimensions[k].state)}</b></div>`).join("")}</div>${inspect(r.id)}</article>`;
    }).join("");
  }
  function prose(text) {
    // Only display copied Markdown. Escape first; source links resolve against the original 054 fixture location.
    let out=esc(text);
    out=out.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(_,label,dest)=>{
      const href=new URL(dest.replaceAll("&amp;","&"),new URL("../../054/manual-cohort-fixture.md",window.location.href));
      if(!["file:","http:","https:"].includes(href.protocol))return label;
      return `<a href="${esc(href.href)}" target="_blank" rel="noopener">${label}</a>`;
    });
    return out.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>").replace(/`([^`]+)`/g,"<code>$1</code>");
  }
  const list=(title,items)=>`<article><h4>${esc(title)}</h4><ul>${items.map(v=>`<li>${esc(v)}</li>`).join("")}</ul></article>`;
  function renderDetail(id) {
    const target=document.getElementById("detail-content");
    const synthetic=control.synthetic.find(x=>x.id===id);
    if(synthetic){
      const text=copy.synthetic[id];
      target.innerHTML=`<div class="synthetic-detail"><span class="badge synthetic">MADE-UP EXAMPLE · NOT AN ACTUAL TASK</span><h3>${esc(text.name)}</h3>${pill(synthetic.operationalState)}<p>This demonstrates the interface only. No actual opportunity, task, running analysis, waiting period or external action is created or authorized.</p><p><b>Why:</b> ${esc(text.why)}</p><p><b>Example request:</b> ${esc(text.action)}</p><p><b>If no action:</b> ${esc(text.inaction)}</p><p><b>What could change this:</b> ${esc(text.movement)}</p>${originalControl(synthetic)}${sourceLinks(["experiments/052/viewer/control-fixtures.js"])}</div>`;
      return;
    }
    const r=byId(id),o=opportunity(id),c=control.historical.find(x=>x.id===id),contract=window.CONTRACT_EVIDENCE.find(x=>x.id===id),text=copy.records[id];
    target.innerHTML=`<div class="detail-banner"><span class="badge">SELECTED PAST WORK · INCOMPLETE PICTURE</span><h3>${esc(o.name)}</h3><p>${esc(text.idea)}</p><p><b>Last recorded check:</b> ${esc(r.horizon)}</p>${precision("Original hypothesis and historical verdict",`<p>${esc(o.thesis)}</p><p>${esc(o.lifecycle.historicalDisposition)}</p>`)}</div>
      <div class="fact-grid"><article><h4>What idea and decision does this represent?</h4>${pill(o.lifecycle.state)}<p>Status of the idea, interpreted from past evidence.</p><p>${esc(text.decision)}</p><strong>${r.instance?`Specific decision: ${esc(stateText(r.instanceState))}` : "Specific decision: not established"}</strong><p>Whether this qualified for historical tracking: not known (UNKNOWN).<br>Today's status: not known (UNKNOWN).</p>${precision("Exact identity and status terms",`<p>${esc(r.instanceLabel)}</p><p>Family ${esc(o.lifecycle.state)} · DERIVED; instance ${esc(r.instanceState || "NOT ESTABLISHED")} · historical admission UNKNOWN; current external lifecycle UNKNOWN.</p>`)}</article><article><h4>What did the old test allow?</h4>${pill(c.operationalState)}<p>${esc(text.why)}</p><strong>Today's tasks: not known (NO CURRENT EVIDENCE)</strong>${originalControl(c)}</article><article><h4>What would allow progress?</h4>${pill(r.blocker)}<p>${esc(text.condition)}</p><p>${esc(text.route)}</p><strong>No barrier is known to have cleared. No new permission is given.</strong>${precision("Exact blocker and reopening terms",`<p>${esc(r.blocker)}</p><p>${esc(r.reactivation)}</p><p>${esc(r.route)}</p>`)}</article></div>
      <h3>Who decides, benefits or might pay?</h3><p>A decision maker or beneficiary is not automatically a paying customer. No AE buyer or payer has been established in these records.</p><div class="fact-grid">${[["Person making the decision",o.actor],["Who would benefit",o.beneficiary],["Who would pay AE",o.buyerPayer]].map(([name,v],i)=>`<article><h4>${name}</h4><p>${esc(text.roles[i])}</p>${precision("Exact role and evidence classification",`<strong>${esc(v.state)} · ${esc(v.evidenceClass)}</strong><p>${esc(v.value)}</p>`)}</article>`).join("")}</div>
      <h3>Six separate questions about this idea</h3><p class="chart-note">Not known does not mean far from success. Blocked does not mean ended. These labels are categories, not scores or rankings.</p><div class="dimensions">${dimensions.map((k,i)=>{const d=o.dimensions[k];return `<article class="dimension"><div class="dimension-header"><h4>${esc(copy.dimensions[k])}</h4>${pill(d.state)}</div><p>${esc(text.dimensions[i])}</p>${precision(`Exact ${labels[k]} evidence and possible next check`,`<p><b>${esc(d.state)} · ${esc(d.evidenceClass)}</b>${d.feasibility?` · feasibility ${esc(d.feasibility)}`:""}</p><p>${esc(d.evidence)}</p><dl>${d.blocker?`<dt>Blocker</dt><dd>${esc(d.blocker)}</dd>`:""}${d.nextObservation?`<dt>Next observation · not authorized action</dt><dd>${esc(d.nextObservation)}</dd>`:""}</dl>`)}</article>`;}).join("")}</div>
      <div class="knowledge-grid">${list("What we know",text.known)}${list("What we do not know",text.unknowns)}${list("Main barrier and possible next check",[text.barrier,text.next])}${list("What the evidence does not prove",text.unproven)}</div>${technicalList("Original statements of knowns, unknowns, barriers and unproven claims",[...o.known,...o.unknowns,o.dominantBlocker,o.nextDiscriminator,...o.unprovenClaims])}
      <article class="trajectory"><h3>What changed as we tested?</h3><p class="chart-note">These experiments tested the same idea over time; they are not additional opportunities. The original results stay intact.</p>${o.experiments.map((e,i)=>`<div class="timeline-event"><span class="event-id">EXPERIMENT ${esc(e.id)}</span><p>${esc(text.history[i])}</p>${precision("Original phase, verdict and effect",`<p><strong>${esc(e.phase)} · ${esc(e.disposition)}</strong></p><p>${esc(e.effect)}</p>`)}${link(e.source,"Read the original evidence ↗")}</div>`).join("")}</article>
      <h3>What does this record support?</h3><table class="evidence-frontier-table"><thead><tr><th>Question</th><th>What the evidence says</th></tr></thead><tbody>${engine.frontierLabels.map((name,i)=>`<tr><td>${esc(copy.frontiers[i])}</td><td title="${esc(engine.statuses[r.frontier[i]])}">${esc(copy.frontierStatus[r.frontier[i]])}</td></tr>`).join("")}</tbody></table><p class="chart-note">Not known does not disprove private effects. Submitting the realtime request did not verify delivery. Superset's stated next action did not prove implementation.</p>
      <details class="contract-source"><summary>Original identity and evidence record · Experiment 054</summary><p>Copied verbatim from the approved record. Its old permissions and unknowns apply only to that experiment and its dates.</p>${contract.text.split("\n\n").map(p=>`<p>${prose(p)}</p>`).join("")}</details>
      <h3>Where did this come from, and what is missing?</h3><p class="chart-note">Historical tracking eligibility and AE's buyer or payer are not known (UNKNOWN). Today's external state has not been checked.</p>${precision("Exact memory and accounting terms",`<p>Memory ${esc(r.memory)} · historical admission UNKNOWN · AE buyer/payer UNKNOWN · current state unassessed. V0 categorical interpretation and 054 accounting are separately cited.</p>`)}${sourceLinks([...o.sources,engine.fixtureSource,engine.historicalSource,"experiments/052/viewer/control-fixtures.js","experiments/054/review.md"])}`;
  }
  function selectRecord(id,scroll=true) {
    const select=document.getElementById("detail-select");select.value=id;renderDetail(id);
    if(scroll){document.getElementById("evidence").scrollIntoView({block:"start"});select.focus({preventScroll:true});}
  }
  document.getElementById("detail-select").innerHTML=`<optgroup label="Ideas from past work">${rows.map(r=>`<option value="${r.id}">${esc(opportunity(r.id).name)}</option>`).join("")}</optgroup><optgroup label="Made-up examples · excluded from counts">${control.synthetic.map(x=>`<option value="${x.id}">${esc(copy.synthetic[x.id].name)}</option>`).join("")}</optgroup>`;
  document.getElementById("detail-select").addEventListener("change",e=>renderDetail(e.target.value));
  document.addEventListener("click",e=>{const audit=e.target.closest("[data-audit]");if(audit)showAudit(audit.dataset.audit);const record=e.target.closest("[data-record]");if(record)selectRecord(record.dataset.record);});
  document.getElementById("close-audit").addEventListener("click",()=>{document.getElementById("aggregate-audit").hidden=true;document.getElementById("engine-title").scrollIntoView({block:"start"});document.querySelector('[data-audit="governed"]').focus({preventScroll:true});});
  const navLinks=[...document.querySelectorAll(".layer-nav a")];
  navLinks[0].setAttribute("aria-current","location");
  if(window.IntersectionObserver){
    const observer=new IntersectionObserver(entries=>{
      for(const entry of entries)if(entry.isIntersecting){navLinks.forEach(a=>{if(a.getAttribute("href")==="#"+entry.target.id)a.setAttribute("aria-current","location");else a.removeAttribute("aria-current");});}
    },{rootMargin:"-70px 0px -65% 0px",threshold:0});
    for(const id of ["engine","control","possibility","evidence"])observer.observe(document.getElementById(id));
  }
  renderEngine();document.getElementById("historical-controls").innerHTML=renderControls(control.historical,false);document.getElementById("synthetic-controls").innerHTML=renderControls(control.synthetic,true);renderPossibility();selectRecord(rows[0].id,false);
})();
