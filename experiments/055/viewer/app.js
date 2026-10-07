(function () {
  "use strict";
  const engine = window.ENGINE_FIXTURES, knowledge = window.OPPORTUNITY_FIXTURES, control = window.CONTROL_PLANE_FIXTURES;
  if (!engine || !knowledge || !control || !window.CONTRACT_EVIDENCE) { document.body.innerHTML = "<p>Static fixture data could not load. Counts are unavailable.</p>"; return; }
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
  const pill = s => `<span class="pill state-${token(s)}">${esc(s)}</span>`;
  const inspect = (id,label) => `<button class="inspect-button" type="button" data-record="${esc(id)}">${esc(label || "Inspect evidence →")}</button>`;
  const defaultSources = [engine.historicalSource, engine.fixtureSource, "experiments/054/review.md"];
  function frontierCounts(index) { return ["S","R","N","U"].map(s => rows.filter(r => r.frontier[index] === s).length); }
  function renderEngine() {
    document.getElementById("cohort-horizon").textContent = engine.horizon;
    // These are display counts from manually authored fixtures, not automated admission/identity inference.
    document.querySelector('[data-audit="governed"]').innerHTML = `${engine.prospective.length} <span>captured records ↗</span>`;
    for (const [key,number] of [["families",rows.length],["instances",rows.filter(r=>r.instance).length],["unresolved",rows.filter(r=>!r.instance).length]]) document.querySelector(`[data-audit="${key}"] b`).textContent = number;
    document.getElementById("frontier").innerHTML = engine.frontierLabels.map((name,i) => {
      const counts = frontierCounts(i);
      const description = `${name}: ${counts[0]} supported, ${counts[1]} refuted, ${counts[2]} not reached, ${counts[3]} unknown; denominator ${rows.length} historical chain records. Audit this assertion.`;
      return `<button class="frontier-row" type="button" data-audit="front:${i}" aria-label="${esc(description)}" title="${esc(description)}"><span class="frontier-name">${esc(name)}</span><span class="frontier-bar" aria-hidden="true">${counts.map((n,j)=>`<span class="bar-${["S","R","N","U"][j]}" style="width:${n/rows.length*100}%"></span>`).join("")}</span><span class="frontier-count">${counts[0]}/${rows.length} ↗</span></button>`;
    }).join("");
    document.getElementById("lifecycle").innerHTML = ["family","instance"].map(unit => {
      const population = unit === "family" ? rows : rows.filter(r=>r.instance);
      return `<p class="distribution-label">${unit === "family" ? "6 family hypotheses" : "3 supported decision instances"}</p><div class="distribution">${states.map(state=>`<button type="button" data-audit="life:${unit}:${state}"><b>${population.filter(r => (unit === "family" ? opportunity(r.id).lifecycle.state : r.instanceState) === state).length}</b>${state} ↗</button>`).join("")}</div>`;
    }).join("");
    document.getElementById("blockers").innerHTML = `<div class="distribution">${["CONTINGENT","STRUCTURAL AT HORIZON","UNRESOLVED"].map(cat=>`<button type="button" data-audit="block:${cat}"><b>${rows.filter(r=>r.blocker===cat).length}</b>${cat} ↗</button>`).join("")}</div>`;
    document.getElementById("runs").innerHTML = engine.runs.map(r=>`<button type="button" data-audit="run:${r.id}">Experiment ${r.id}<br><strong>${r.candidates} run-local candidates ↗</strong></button>`).join("");
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
  function showAudit(key) {
    const d=descriptor(key),panel=document.getElementById("aggregate-audit");
    document.getElementById("audit-title").textContent=d.title;
    document.getElementById("audit-content").innerHTML=`<dl class="audit-facts">${[["Result",d.result],["Unit / denominator",d.unit],["Population",d.population],["Evidence horizon",d.horizon],["Derivation",d.derivation],["Missingness",d.missingness]].map(([name,value])=>`<div><dt>${esc(name)}</dt><dd>${esc(value)}</dd></div>`).join("")}</dl><h3>Included records / underlying evidence</h3>${d.memberNote?`<p>${esc(d.memberNote)}</p>`:""}${d.members.length?`<div class="member-list">${d.members.map(r=>`<button type="button" data-record="${r.id}">${esc(r.short)}${d.frontIndex!==undefined?` · ${esc(engine.statuses[r.frontier[d.frontIndex]])}`:""}<small>${esc(r.horizon)}</small><small>${esc(d.frontIndex===undefined?r.instanceLabel:opportunity(r.id).name)} →</small></button>`).join("")}</div>`:`<p class="audit-empty">${esc(d.empty || "No included records for this scoped assertion.")}</p>`}<h3>Derivation / source artifacts</h3>${sourceLinks(d.sources)}`;
    panel.hidden=false;panel.focus({preventScroll:true});panel.scrollIntoView({block:"start"});
  }
  const groupDefs=[{id:"attention",title:"Needs judgment / authorization"},{id:"safe",title:"Completed / no action within old contract"},{id:"waiting",title:"Waiting on outside evidence"},{id:"blocked",title:"Blocked / no authorized useful action"},{id:"dormant",title:"Dormant / conditional reopening"}];
  function controlCard(item,synthetic) {
    const o=synthetic?null:opportunity(item.id),r=synthetic?null:byId(item.id);
    return `<article class="control-card"><span class="badge ${synthetic?"synthetic":""}">${synthetic?"SYNTHETIC · UI ONLY":"HISTORICAL CONTROL"}</span><span class="badge">${esc(item.operationalState)}</span><h4>${esc(o?o.name:item.name)}</h4>${r?`<p class="group-caption">${esc(r.horizon)} · current control: NO CURRENT EVIDENCE</p>`:""}<dl>${[["Why",item.why],[synthetic?"Hypothetical requested action":"Original V1 instruction · not a current task",item.requestedAction],[synthetic?"If no action in this scenario":"Original V1 inaction interpretation · historical",item.ifNoAction],["What could move it · conditional",r?r.reactivation:item.movement]].map(([k,v])=>`<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}</dl>${inspect(item.id,"Trace control / evidence →")}</article>`;
  }
  function renderControls(items,synthetic) {
    return groupDefs.map(group=>{
      const selected=items.filter(i=>i.group===group.id);
      if(!selected.length)return "";
      return `<section class="control-group"><div><h3>${esc(group.title)}</h3><p class="group-caption">${selected.length} ${synthetic?"synthetic exercises; excluded from Engine":"historical fixture records; not live tasks"}</p></div><div class="control-cards">${selected.map(i=>controlCard(i,synthetic)).join("")}</div></section>`;
    }).join("");
  }
  function renderPossibility() {
    document.getElementById("opportunity-overview").innerHTML=rows.map(r=>{
      const o=opportunity(r.id);
      return `<article class="possibility-row"><div><h3>${esc(o.name)}</h3><span class="badge">${esc(o.experimentRange)}</span>${pill(o.lifecycle.state)}<p>${r.instance?"Supported historical instance":"Family-only · instance UNRESOLVED"}</p><p>${esc(r.horizon)}</p></div><div class="dimension-mini">${dimensions.map(k=>`<div><span>${labels[k]}</span><b>${pill(o.dimensions[k].state)}</b></div>`).join("")}</div>${inspect(r.id)}</article>`;
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
      target.innerHTML=`<div class="synthetic-detail"><span class="badge synthetic">SYNTHETIC · NOT AN ACTUAL TASK</span><h3>${esc(synthetic.name)}</h3>${pill(synthetic.operationalState)}<p>${esc(synthetic.scenarioBoundary)}</p><p><b>Why:</b> ${esc(synthetic.why)}</p><p><b>Hypothetical action:</b> ${esc(synthetic.requestedAction)}</p><p><b>If no action:</b> ${esc(synthetic.ifNoAction)}</p><p><b>Movement:</b> ${esc(synthetic.movement)}</p><p>No historical opportunity, evidence frontier, current attention request or execution authority is asserted.</p>${sourceLinks(["experiments/052/viewer/control-fixtures.js"])}</div>`;
      return;
    }
    const r=byId(id),o=opportunity(id),c=control.historical.find(x=>x.id===id),contract=window.CONTRACT_EVIDENCE.find(x=>x.id===id);
    target.innerHTML=`<div class="detail-banner"><span class="badge">HISTORICAL / PARTIAL</span><h3>${esc(o.name)}</h3><p>${esc(o.thesis)}</p><p><b>Evidence horizon:</b> ${esc(r.horizon)}</p><p><b>Original disposition:</b> ${esc(o.lifecycle.historicalDisposition)}</p></div>
      <div class="fact-grid"><article><h4>Family / instance identity</h4>${pill(o.lifecycle.state)}<p>DERIVED family lifecycle</p><p>${esc(r.instanceLabel)}</p><strong>${r.instance?`Instance ${r.instanceState} · DERIVED` : "Instance NOT ESTABLISHED"}</strong><p>Historical admission: UNKNOWN<br>Current external lifecycle: UNKNOWN</p></article><article><h4>Historical control / current missingness</h4>${pill(c.operationalState)}<p>${esc(c.why)}</p><strong>Current control: NO CURRENT EVIDENCE</strong><p>Original V1 instruction, not a live task: ${esc(c.requestedAction)}</p></article><article><h4>Blocker / conditional movement</h4>${pill(r.blocker)}<p>${esc(r.reactivation)}</p><p>${esc(r.route)}</p><strong>No cleared blocker or new authority claimed.</strong></article></div>
      <h3>Roles and economic boundary</h3><div class="fact-grid">${[["Decision actor",o.actor],["Beneficiary",o.beneficiary],["Buyer / payer for AE",o.buyerPayer]].map(([name,v])=>`<article><h4>${name}</h4><strong>${esc(v.state)} · ${esc(v.evidenceClass)}</strong><p>${esc(v.value)}</p></article>`).join("")}</div>
      <h3>Six independent dimensions · preserved V0 evidence</h3><p class="chart-note">UNKNOWN ≠ FAR; BLOCKED ≠ TERMINAL. Categories are not numeric distances, ranking or a composite.</p><div class="dimensions">${dimensions.map(k=>{const d=o.dimensions[k];return `<article class="dimension"><div class="dimension-header"><h4>${labels[k]}</h4>${pill(d.state)}</div><p><b>${esc(d.evidenceClass)}</b>${d.feasibility?` · feasibility ${esc(d.feasibility)}`:""}</p><p>${esc(d.evidence)}</p><dl>${d.blocker?`<dt>Blocker</dt><dd>${esc(d.blocker)}</dd>`:""}${d.nextObservation?`<dt>Next observation · not authorized action</dt><dd>${esc(d.nextObservation)}</dd>`:""}</dl></article>`;}).join("")}</div>
      <div class="knowledge-grid">${list("Known",o.known)}${list("Unknown",o.unknowns)}${list("Dominant blocker / next discriminator",[o.dominantBlocker,o.nextDiscriminator])}${list("Explicitly unproven",o.unprovenClaims)}</div>
      <article class="trajectory"><h3>Evidence trajectory · original history retained</h3><p class="chart-note">Experiments are evidence jobs, not new opportunity identities. Historical verdicts remain intact.</p>${o.experiments.map(e=>`<div class="timeline-event"><span class="event-id">EXPERIMENT ${esc(e.id)}</span><p><strong>${esc(e.phase)} · ${esc(e.disposition)}</strong></p><p>${esc(e.effect)}</p>${link(e.source,"Open original evidence ↗")}</div>`).join("")}</article>
      <h3>Independent frontier · this historical record</h3><table class="evidence-frontier-table"><thead><tr><th>Assertion</th><th>Evidence status</th></tr></thead><tbody>${engine.frontierLabels.map((name,i)=>`<tr><td>${esc(name)}</td><td>${esc(engine.statuses[r.frontier[i]])}</td></tr>`).join("")}</tbody></table><p class="chart-note">No private effect is disproved by an UNKNOWN cell. Realtime submission ≠ verified delivery; Superset stated action ≠ implementation.</p>
      <details class="contract-source"><summary>054 manual identity/evidence contract · verbatim historical record</summary><p>Copied from the approved 054 fixture. Its historical permissions and UNKNOWN states remain scoped to that experiment and evidence horizon.</p>${contract.text.split("\n\n").map(p=>`<p>${prose(p)}</p>`).join("")}</details>
      <h3>Source provenance / missingness</h3><p class="chart-note">Memory ${esc(r.memory)} · historical admission UNKNOWN · AE buyer/payer UNKNOWN · current state unassessed. V0 categorical interpretation and 054 accounting are separately cited.</p>${sourceLinks([...o.sources,engine.fixtureSource,engine.historicalSource,"experiments/052/viewer/control-fixtures.js","experiments/054/review.md"])}`;
  }
  function selectRecord(id,scroll=true) {
    const select=document.getElementById("detail-select");select.value=id;renderDetail(id);
    if(scroll){document.getElementById("evidence").scrollIntoView({block:"start"});select.focus({preventScroll:true});}
  }
  document.getElementById("detail-select").innerHTML=`<optgroup label="Historical families">${rows.map(r=>`<option value="${r.id}">${esc(opportunity(r.id).name)}</option>`).join("")}</optgroup><optgroup label="Synthetic control exercises · excluded">${control.synthetic.map(x=>`<option value="${x.id}">${esc(x.name)}</option>`).join("")}</optgroup>`;
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
