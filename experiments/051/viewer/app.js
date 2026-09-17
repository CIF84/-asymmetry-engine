(function () {
  "use strict";

  const fixture = window.OPPORTUNITY_FIXTURES;
  if (!fixture || !Array.isArray(fixture.opportunities)) {
    document.body.innerHTML = "<p>Experiment 051 fixture data could not be loaded.</p>";
    return;
  }

  const dimensions = ["resolution", "access", "adoption", "control", "regulatory", "economic"];
  const labels = {
    resolution: "Resolution",
    access: "Access",
    adoption: "Adoption",
    control: "Control",
    regulatory: "Regulatory",
    economic: "Economic"
  };

  const rows = document.getElementById("opportunity-rows");
  const empty = document.getElementById("empty-state");
  const lifecycleFilter = document.getElementById("lifecycle-filter");
  const search = document.getElementById("opportunity-search");
  const reset = document.getElementById("reset-controls");
  const detailSelect = document.getElementById("detail-select");
  const detail = document.getElementById("detail-content");

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function classToken(value) {
    return String(value || "unknown").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
  }

  function statePill(state) {
    return `<span class="state-pill state-${classToken(state)}">${escapeHtml(state)}</span>`;
  }

  function lifecyclePill(state, count) {
    const suffix = typeof count === "number" ? ` · ${count}` : "";
    return `<span class="badge lifecycle-${classToken(state)}">${escapeHtml(state)}${suffix}</span>`;
  }

  function evidencePill(value) {
    return `<span class="evidence-pill">${escapeHtml(value)}</span>`;
  }

  function repoHref(path) {
    if (path.startsWith("experiments/")) return `../../${path.slice("experiments/".length)}`;
    if (path.startsWith("docs/") || path.startsWith("specs/")) return `../../../${path}`;
    return `../../../${path}`;
  }

  function sourceLink(path, label) {
    return `<a href="${escapeHtml(repoHref(path))}">${escapeHtml(label || path)}</a>`;
  }

  function renderLegend() {
    document.getElementById("distance-legend").innerHTML = fixture.distanceVocabulary.map(statePill).join("");
    const counts = fixture.lifecycleVocabulary.map((state) => [state, fixture.opportunities.filter((item) => item.lifecycle.state === state).length]);
    document.getElementById("lifecycle-counts").innerHTML = counts.map(([state, count]) => lifecyclePill(state, count)).join("");
    document.getElementById("fixture-version").textContent = `Fixture ${fixture.schemaVersion}`;
  }

  function searchableText(item) {
    return [
      item.name,
      item.experimentRange,
      item.lifecycle.state,
      item.lifecycle.historicalDisposition,
      item.significance,
      item.dominantBlocker,
      item.nextDiscriminator,
      item.evidenceHorizon,
      ...dimensions.map((key) => item.dimensions[key].state),
      ...item.experiments.map((event) => `${event.id} ${event.disposition}`)
    ].join(" ").toLowerCase();
  }

  function visibleItems() {
    const lifecycle = lifecycleFilter.value;
    const query = search.value.trim().toLowerCase();
    return fixture.opportunities.filter((item) => {
      const lifecycleMatch = lifecycle === "ALL" || item.lifecycle.state === lifecycle;
      return lifecycleMatch && (!query || searchableText(item).includes(query));
    });
  }

  function renderRows() {
    const items = visibleItems();
    empty.hidden = items.length > 0;
    rows.innerHTML = items.map((item) => {
      const distanceCells = dimensions.map((key) => `<td data-label="${labels[key]}">${statePill(item.dimensions[key].state)}</td>`).join("");
      return `
        <tr>
          <td data-label="Opportunity">
            <button class="opportunity-link" type="button" data-opportunity-id="${escapeHtml(item.id)}">
              ${escapeHtml(item.name)}
              <small>${escapeHtml(item.experimentRange)}</small>
            </button>
          </td>
          <td data-label="Lifecycle">${lifecyclePill(item.lifecycle.state)}</td>
          ${distanceCells}
          <td data-label="Blocker / next observation" class="cell-copy">
            <strong>${escapeHtml(item.dominantBlocker)}</strong>
            ${escapeHtml(item.nextDiscriminator)}
          </td>
          <td data-label="Evidence horizon" class="horizon-copy">${escapeHtml(item.evidenceHorizon)}</td>
        </tr>`;
    }).join("");

    rows.querySelectorAll("[data-opportunity-id]").forEach((button) => {
      button.addEventListener("click", () => {
        detailSelect.value = button.dataset.opportunityId;
        renderDetail(button.dataset.opportunityId);
        document.getElementById("detail").scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  function renderRole(title, role) {
    return `
      <article class="fact-card">
        <h4>${escapeHtml(title)}</h4>
        <div>${evidencePill(role.evidenceClass)}</div>
        <p><strong>${escapeHtml(role.state)}</strong></p>
        <p>${escapeHtml(role.value)}</p>
      </article>`;
  }

  function renderDimension(key, value) {
    const feasibility = value.feasibility ? `<dt>Feasibility</dt><dd>${escapeHtml(value.feasibility)}</dd>` : "";
    const blocker = value.blocker ? `<dt>Blocker</dt><dd>${escapeHtml(value.blocker)}</dd>` : "";
    const next = value.nextObservation ? `<dt>Next observation</dt><dd>${escapeHtml(value.nextObservation)}</dd>` : "";
    return `
      <article class="dimension-card">
        <div class="dimension-heading">
          <h4>${escapeHtml(labels[key])}</h4>
          ${statePill(value.state)}
        </div>
        ${evidencePill(value.evidenceClass)}
        <p>${escapeHtml(value.evidence)}</p>
        <dl>${feasibility}${blocker}${next}</dl>
      </article>`;
  }

  function renderListCard(title, modifier, items) {
    const content = items.length ? items.map((item) => `<li>${escapeHtml(item)}</li>`).join("") : "<li>None recorded.</li>";
    return `<article class="knowledge-card knowledge-card--${modifier}"><h4>${escapeHtml(title)}</h4><ul>${content}</ul></article>`;
  }

  function renderDetail(id) {
    const item = fixture.opportunities.find((candidate) => candidate.id === id) || fixture.opportunities[0];
    const reactivation = item.reactivationCondition
      ? `<li>${escapeHtml(item.reactivationCondition)}</li>`
      : "<li>No reactivation condition is claimed; a materially different thesis would require a new experiment.</li>";
    detail.innerHTML = `
      <div class="detail-header">
        <article class="detail-title-card">
          <div>${evidencePill(item.lifecycle.evidenceClass)} <span class="evidence-pill">${escapeHtml(item.experimentRange)}</span></div>
          <h3>${escapeHtml(item.name)}</h3>
          <p><strong>Decision thesis:</strong> ${escapeHtml(item.thesis)}</p>
          <p><strong>Significance:</strong> ${escapeHtml(item.significance)}</p>
        </article>
        <article class="lifecycle-card" data-lifecycle="${escapeHtml(item.lifecycle.state)}">
          <h4>Derived lifecycle</h4>
          ${lifecyclePill(item.lifecycle.state)}
          <p>${escapeHtml(item.lifecycle.reason)}</p>
          <p class="historical-disposition"><strong>Preserved historical disposition</strong><br>${escapeHtml(item.lifecycle.historicalDisposition)}</p>
        </article>
      </div>

      <div class="role-grid">
        ${renderRole("Decision actor", item.actor)}
        ${renderRole("Beneficiary", item.beneficiary)}
        ${renderRole("Buyer / payer", item.buyerPayer)}
      </div>

      <div class="dimension-grid">
        ${dimensions.map((key) => renderDimension(key, item.dimensions[key])).join("")}
      </div>

      <div class="knowledge-grid">
        ${renderListCard("Known", "known", item.known)}
        ${renderListCard("Unknown", "unknown", item.unknowns)}
        ${renderListCard("Blocked", "blocked", [item.dominantBlocker])}
        ${renderListCard("Next observation", "next", [item.nextDiscriminator])}
        ${renderListCard("Reactivation condition", "next", []).replace("<li>None recorded.</li>", reactivation)}
        ${renderListCard("Explicitly unproven", "unknown", item.unprovenClaims)}
      </div>

      <article class="timeline-card">
        <h4>Immutable experiment history</h4>
        <div class="timeline">
          ${item.experiments.map((event) => `
            <div class="timeline-item">
              <span class="timeline-id">${escapeHtml(event.id)}</span>
              <strong>${escapeHtml(event.phase)}<br><span class="evidence-pill">${escapeHtml(event.disposition)}</span></strong>
              <p>${escapeHtml(event.effect)}</p>
              ${sourceLink(event.source, "Open evidence")}
            </div>`).join("")}
        </div>
      </article>

      <article class="provenance-card">
        <h4>Evidence provenance</h4>
        <p><strong>Horizon:</strong> ${escapeHtml(item.evidenceHorizon)}. These files support the current representation; they are not rewritten by this viewer.</p>
        <div class="source-list">${item.sources.map((path) => sourceLink(path)).join("")}</div>
      </article>`;
  }

  function initializeDetail() {
    detailSelect.innerHTML = fixture.opportunities.map((item) => `<option value="${escapeHtml(item.id)}">${escapeHtml(item.name)} · ${escapeHtml(item.experimentRange)}</option>`).join("");
    detailSelect.addEventListener("change", () => renderDetail(detailSelect.value));
    renderDetail(fixture.opportunities[0].id);
  }

  lifecycleFilter.addEventListener("change", renderRows);
  search.addEventListener("input", renderRows);
  reset.addEventListener("click", () => {
    lifecycleFilter.value = "ALL";
    search.value = "";
    renderRows();
  });

  renderLegend();
  initializeDetail();
  renderRows();
})();
