(function () {
  "use strict";

  const knowledge = window.OPPORTUNITY_FIXTURES;
  const control = window.CONTROL_PLANE_FIXTURES;
  if (!knowledge || !control) {
    document.body.innerHTML = "<p>Experiment 052 fixture data could not be loaded.</p>";
    return;
  }

  const dimensions = ["resolution", "access", "adoption", "control", "regulatory", "economic"];
  const labels = {
    resolution: "Resolution", access: "Access", adoption: "Adoption",
    control: "Control", regulatory: "Regulatory", economic: "Economic"
  };
  const groupDefinitions = [
    { id: "attention", title: "Needs attention", description: "Human judgment or explicit authority is required now." },
    { id: "safe", title: "Progressing / safe without intervention", description: "No current human action is requested; this says nothing about value or rank." },
    { id: "waiting", title: "Waiting on external state", description: "Time or outside evidence—not human action—is the present dependency." },
    { id: "blocked", title: "Blocked / no useful action available", description: "Progress cannot continue, and current human intervention would not resolve the constraint." },
    { id: "dormant", title: "Dormant / reactivation", description: "Contingently inactive historical opportunities with explicit reactivation conditions." }
  ];

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;").replaceAll("'", "&#039;");
  }

  function token(value) {
    return String(value || "unknown").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
  }

  function sourceHref(path) {
    if (path.startsWith("experiments/")) return `../../${path.slice("experiments/".length)}`;
    return `../../../${path}`;
  }

  function sourceLink(path, label) {
    return `<a href="${escapeHtml(sourceHref(path))}">${escapeHtml(label || path)}</a>`;
  }

  const historicalItems = control.historical.map((state) => {
    const opportunity = knowledge.opportunities.find((item) => item.id === state.id);
    if (!opportunity) throw new Error(`Missing frozen V0 opportunity: ${state.id}`);
    return { kind: "historical", ...state, name: opportunity.name, opportunityState: opportunity.lifecycle.state, opportunity };
  });
  const syntheticItems = control.synthetic.map((item) => ({ kind: "synthetic", ...item }));
  const allItems = [...historicalItems, ...syntheticItems];

  function badge(label, kind) {
    return `<span class="badge ${escapeHtml(kind || "")}">${escapeHtml(label)}</span>`;
  }

  function renderCard(item) {
    const sourceBadge = item.kind === "synthetic" ? badge("Synthetic scenario", "synthetic") : badge("Historical evidence", "historical");
    const range = item.opportunity ? `<span class="experiment-range">${escapeHtml(item.opportunity.experimentRange)}</span>` : "";
    return `<article class="control-card ${item.kind}">
      <div class="badge-row">${sourceBadge}${badge(item.operationalState, "operational")}</div>
      <div><h4>${escapeHtml(item.name)}</h4>${range}</div>
      <dl>
        <dt>Why</dt><dd>${escapeHtml(item.why)}</dd>
        <dt>Human action</dt><dd>${escapeHtml(item.requestedAction)}</dd>
        <dt>If no action</dt><dd>${escapeHtml(item.ifNoAction)}</dd>
      </dl>
      <button class="drill-button" type="button" data-detail-id="${escapeHtml(item.id)}">Trace classification →</button>
    </article>`;
  }

  function renderGroups() {
    const container = document.getElementById("control-groups");
    container.innerHTML = groupDefinitions.map((group) => {
      const items = allItems.filter((item) => item.group === group.id);
      return `<section class="control-group group-${group.id}" aria-labelledby="group-${group.id}">
        <div class="group-heading">
          <span class="count">${items.length}</span>
          <div><h3 id="group-${group.id}">${escapeHtml(group.title)}</h3><p>${escapeHtml(group.description)}</p></div>
        </div>
        <div class="card-grid">${items.map(renderCard).join("")}</div>
      </section>`;
    }).join("");

    const attentionCount = allItems.filter((item) => item.group === "attention").length;
    document.getElementById("summary-note").textContent = `${attentionCount} item${attentionCount === 1 ? "" : "s"} ask for human attention in this test fixture. Both are unmistakably synthetic; no historical opportunity is presented as requiring action now.`;

    container.querySelectorAll("[data-detail-id]").forEach((button) => {
      button.addEventListener("click", () => {
        document.getElementById("detail-select").value = `${allItems.find((item) => item.id === button.dataset.detailId).kind}:${button.dataset.detailId}`;
        renderDetail(button.dataset.detailId);
        document.getElementById("detail").scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  function statePill(state) {
    return `<span class="state-pill state-${token(state)}">${escapeHtml(state)}</span>`;
  }

  function renderDimension(key, value) {
    return `<article class="dimension-card">
      <div class="dimension-heading"><h4>${labels[key]}</h4>${statePill(value.state)}</div>
      <p><strong>${escapeHtml(value.evidenceClass)}</strong></p>
      <p>${escapeHtml(value.evidence)}</p>
      ${value.blocker ? `<dl><dt>Blocker</dt><dd>${escapeHtml(value.blocker)}</dd></dl>` : ""}
      ${value.nextObservation ? `<dl><dt>Next observation</dt><dd>${escapeHtml(value.nextObservation)}</dd></dl>` : ""}
    </article>`;
  }

  function listCard(title, items) {
    return `<article class="knowledge-card"><h4>${escapeHtml(title)}</h4><ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("") || "<li>None recorded.</li>"}</ul></article>`;
  }

  function renderControlHeader(item) {
    return `<div class="detail-state-grid">
      <article class="fact-card fact-card--accent"><h4>1 · Current opportunity state</h4>${statePill(item.opportunityState)}<p>${item.opportunity ? escapeHtml(item.opportunity.lifecycle.reason) : "Synthetic state used only to test the control interface."}</p></article>
      <article class="fact-card fact-card--accent"><h4>2 · Current control state</h4>${badge(item.operationalState, "operational")}<p>${escapeHtml(item.why)}</p></article>
      <article class="fact-card fact-card--accent"><h4>3 · What could move it</h4><p>${escapeHtml(item.movement)}</p><p><strong>Requested human action:</strong> ${escapeHtml(item.requestedAction)}</p><p><strong>If no action:</strong> ${escapeHtml(item.ifNoAction)}</p></article>
    </div>`;
  }

  function renderHistoricalDetail(item) {
    const o = item.opportunity;
    const reactivation = o.reactivationCondition || "No reactivation is claimed; a materially different thesis would require a new experiment.";
    return `${renderControlHeader(item)}
      <div class="role-grid">
        ${[["Decision actor", o.actor], ["Beneficiary", o.beneficiary], ["Buyer / payer", o.buyerPayer]].map(([title, role]) => `<article class="fact-card"><h4>${title}</h4><p><strong>${escapeHtml(role.state)} · ${escapeHtml(role.evidenceClass)}</strong></p><p>${escapeHtml(role.value)}</p></article>`).join("")}
      </div>
      <h3>4 · Six-dimensional evidence vector</h3>
      <p><strong>UNKNOWN ≠ FAR. BLOCKED ≠ TERMINAL.</strong> These categorical states are not magnitudes or scores.</p>
      <div class="dimension-grid">${dimensions.map((key) => renderDimension(key, o.dimensions[key])).join("")}</div>
      <div class="knowledge-grid">
        ${listCard("Known", o.known)}${listCard("Unknown", o.unknowns)}
        ${listCard("Dominant blocker", [o.dominantBlocker])}${listCard("Next discriminator", [o.nextDiscriminator])}
        ${listCard("Reactivation condition", [reactivation])}${listCard("Explicitly unproven", o.unprovenClaims)}
      </div>
      <article class="timeline-card"><h4>5 · Evidence / immutable trajectory</h4><div class="timeline">${o.experiments.map((event) => `<div class="timeline-item"><span class="timeline-id">Experiment ${escapeHtml(event.id)}</span><p><strong>${escapeHtml(event.phase)} · ${escapeHtml(event.disposition)}</strong></p><p>${escapeHtml(event.effect)}</p>${sourceLink(event.source, "Open evidence")}</div>`).join("")}</div></article>
      <article class="provenance-card"><h4>6 · Evidence provenance</h4><p><strong>Horizon:</strong> ${escapeHtml(o.evidenceHorizon)}</p><div class="source-list">${o.sources.map((path) => sourceLink(path)).join("")}</div></article>`;
  }

  function renderSyntheticDetail(item) {
    return `<div class="synthetic-warning">SYNTHETIC CONTROL SCENARIO — interface exercise only. This is not historical AE evidence, a live task, an authorization request, or a running process.</div>
      ${renderControlHeader(item)}
      <div class="knowledge-grid">
        ${listCard("Scenario boundary", [item.scenarioBoundary])}
        ${listCard("Historical claims", ["None. No six-dimensional opportunity evidence is asserted for this scenario."])}
        ${listCard("Control distinction under test", [item.attentionType, item.operationalState])}
        ${listCard("Explicitly unproven", ["That this scenario exists in AE now.", "That a human would accept this classification.", "That any external or autonomous action is authorized."])}
      </div>`;
  }

  function renderDetail(id) {
    const item = allItems.find((candidate) => candidate.id === id) || allItems[0];
    document.getElementById("detail-content").innerHTML = item.kind === "historical" ? renderHistoricalDetail(item) : renderSyntheticDetail(item);
  }

  function initializeDetail() {
    const select = document.getElementById("detail-select");
    select.innerHTML = `<optgroup label="Historical evidence">${historicalItems.map((item) => `<option value="historical:${escapeHtml(item.id)}">${escapeHtml(item.name)}</option>`).join("")}</optgroup><optgroup label="Synthetic control scenarios">${syntheticItems.map((item) => `<option value="synthetic:${escapeHtml(item.id)}">${escapeHtml(item.name)}</option>`).join("")}</optgroup>`;
    select.addEventListener("change", () => renderDetail(select.value.split(":")[1]));
    renderDetail(historicalItems[0].id);
  }

  document.getElementById("fixture-version").textContent = `${control.schemaVersion} · manual states · €0 external spend`;
  renderGroups();
  initializeDetail();
})();
