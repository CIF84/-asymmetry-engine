from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .db import Repository
from .sources.comext import (
    CN75_CHILD_PRODUCT,
    CN75_PRODUCT,
    DATASET,
    FLOW,
    REPORTER,
    SOURCE_ID,
)

VALUE = "VALUE_IN_EUROS"
MASS = "QUANTITY_IN_100KG"
YEARS = ("2023", "2024")
SELECTED_PARTNERS = ("FR", "IT")


class ReasoningError(RuntimeError):
    pass


@dataclass(frozen=True)
class EconomicEntity:
    entity_type: str
    source_native_id: str
    label: str


@dataclass(frozen=True)
class Measurement:
    name: str
    value: float
    unit: str
    derivation: str
    observation_ids: tuple[str, ...]


@dataclass(frozen=True)
class EvidenceRelationship:
    subject: str
    predicate: str
    object: str
    basis: str
    observation_ids: tuple[str, ...]


@dataclass(frozen=True)
class DisequilibriumArgument:
    entities: tuple[EconomicEntity, ...]
    measurements: tuple[Measurement, ...]
    relationships: tuple[EvidenceRelationship, ...]
    detected: tuple[str, ...]
    unusual: tuple[str, ...]
    decomposition: tuple[str, ...]
    geography: tuple[str, ...]
    supported_interpretation: tuple[str, ...]
    not_supported: tuple[str, ...]
    alternative_explanations: tuple[str, ...]
    next_best_evidence: tuple[str, ...]

    def measurement(self, name: str) -> Measurement:
        return next(item for item in self.measurements if item.name == name)

    def render(self) -> str:
        sections = (
            ("DETECTED", self.detected),
            ("WHY IT IS UNUSUAL", self.unusual),
            ("DECOMPOSITION", self.decomposition),
            ("GEOGRAPHY", self.geography),
            ("SUPPORTED INTERPRETATION", self.supported_interpretation),
            ("NOT SUPPORTED", self.not_supported),
            ("ALTERNATIVE EXPLANATIONS", self.alternative_explanations),
            ("NEXT BEST EVIDENCE", self.next_best_evidence),
        )
        lines: list[str] = []
        for heading, items in sections:
            lines.append(heading)
            lines.extend(f"- {item}" for item in items)
            lines.append("")
        lines.append("RELATIONSHIPS")
        lines.extend(
            f"- {item.subject} {item.predicate} {item.object} "
            f"[{item.basis}; lineage: {', '.join(item.observation_ids)}]"
            for item in self.relationships
        )
        lines.append("")
        lines.append("LINEAGE")
        lines.extend(
            f"- {item.name} = {item.value:,.4f} {item.unit} -> {item.derivation} -> "
            f"{', '.join(item.observation_ids)}"
            for item in self.measurements
        )
        return "\n".join(lines)


def _growth(new: float, old: float, name: str) -> float:
    if old == 0:
        raise ReasoningError(f"Cannot calculate {name}: 2023 baseline is zero")
    return (new / old - 1) * 100


def _fmt_percent(value: float) -> str:
    return f"{value:+.2f}%"


def _load_observations(repository: Repository) -> list[dict[str, Any]]:
    rows = repository.connection.execute(
        """SELECT external_id, metadata_json FROM source_observations
           WHERE source_id=? ORDER BY external_id""",
        (SOURCE_ID,),
    ).fetchall()
    observations = []
    for row in rows:
        metadata = json.loads(row["metadata_json"])
        if (
            metadata.get("dataset") == DATASET
            and metadata.get("reporter_code") == REPORTER
            and metadata.get("flow_code") == FLOW
            and metadata.get("product_code") in {CN75_PRODUCT, CN75_CHILD_PRODUCT}
            and metadata.get("reference_period") in YEARS
            and metadata.get("measure_code") in {VALUE, MASS}
        ):
            observations.append({"external_id": row["external_id"], **metadata})
    return observations


def build_cn75_argument(repository: Repository) -> DisequilibriumArgument:
    observations = _load_observations(repository)
    index = {
        (item["product_code"], item["partner_code"], item["measure_code"], item["reference_period"]): item
        for item in observations
    }

    def required(product: str, partner: str, measure: str, year: str) -> dict[str, Any]:
        item = index.get((product, partner, measure, year))
        if item is None or item.get("value") is None:
            raise ReasoningError(
                f"Missing required Comext evidence: product={product}, partner={partner}, "
                f"measure={measure}, year={year}"
            )
        return item

    parent = {(m, y): required(CN75_PRODUCT, "WORLD", m, y) for m in (VALUE, MASS) for y in YEARS}
    child = {(m, y): required(CN75_CHILD_PRODUCT, "WORLD", m, y) for m in (VALUE, MASS) for y in YEARS}
    partners = {
        (p, m, y): required(CN75_CHILD_PRODUCT, p, m, y)
        for p in SELECTED_PARTNERS
        for m in (VALUE, MASS)
        for y in YEARS
    }

    def lineage(*items: dict[str, Any]) -> tuple[str, ...]:
        return tuple(item["external_id"] for item in items)

    def value(item: dict[str, Any]) -> float:
        return float(item["value"])

    p23v, p24v = value(parent[(VALUE, "2023")]), value(parent[(VALUE, "2024")])
    p23m, p24m = value(parent[(MASS, "2023")]), value(parent[(MASS, "2024")])
    c23v, c24v = value(child[(VALUE, "2023")]), value(child[(VALUE, "2024")])
    c23m, c24m = value(child[(MASS, "2023")]), value(child[(MASS, "2024")])
    value_growth = _growth(p24v, p23v, "CN75 value growth")
    mass_growth = _growth(p24m, p23m, "CN75 mass growth")
    unit_change = _growth(p24v / p24m, p23v / p23m, "derived value-per-mass change")
    child_value_contribution = (c24v - c23v) / (p24v - p23v) * 100
    child_mass_contribution = (c24m - c23m) / (p24m - p23m) * 100

    partner_value_delta = sum(value(partners[(p, VALUE, "2024")]) - value(partners[(p, VALUE, "2023")]) for p in SELECTED_PARTNERS)
    partner_mass_delta = sum(value(partners[(p, MASS, "2024")]) - value(partners[(p, MASS, "2023")]) for p in SELECTED_PARTNERS)
    partner_value_contribution = partner_value_delta / (c24v - c23v) * 100
    partner_mass_contribution = partner_mass_delta / (c24m - c23m) * 100

    country_value_items = {
        (item["partner_code"], item["reference_period"]): item
        for item in observations
        if item["product_code"] == CN75_CHILD_PRODUCT
        and item["measure_code"] == VALUE
        and len(item["partner_code"]) == 2
        and not item["partner_code"].startswith("Q")
    }
    country_codes = sorted({code for code, _ in country_value_items})
    if not country_codes:
        raise ReasoningError("Missing country-level evidence for supplier concentration")

    def hhi(year: str) -> tuple[float, tuple[str, ...]]:
        items = [country_value_items[(code, year)] for code in country_codes if (code, year) in country_value_items]
        total = sum(value(item) for item in items)
        if total <= 0:
            raise ReasoningError(f"Cannot calculate {year} supplier concentration")
        return sum((value(item) / total) ** 2 for item in items), lineage(*items)

    hhi23, hhi23_lineage = hhi("2023")
    hhi24, hhi24_lineage = hhi("2024")
    selected_partner_value_items = tuple(
        partners[(partner, VALUE, year)] for partner in SELECTED_PARTNERS for year in YEARS
    )
    selected_partner_mass_items = tuple(
        partners[(partner, MASS, year)] for partner in SELECTED_PARTNERS for year in YEARS
    )

    measurements = (
        Measurement("CN75 2023 trade value", p23v, "EUR", "source-native cell", lineage(parent[(VALUE, "2023")])),
        Measurement("CN75 2024 trade value", p24v, "EUR", "source-native cell", lineage(parent[(VALUE, "2024")])),
        Measurement("CN75 value growth", value_growth, "percent", "(2024 value / 2023 value - 1) × 100", lineage(parent[(VALUE, "2023")], parent[(VALUE, "2024")])),
        Measurement("CN75 2023 net mass", p23m, "100 kg", "source-native cell", lineage(parent[(MASS, "2023")])),
        Measurement("CN75 2024 net mass", p24m, "100 kg", "source-native cell", lineage(parent[(MASS, "2024")])),
        Measurement("CN75 mass growth", mass_growth, "percent", "(2024 mass / 2023 mass - 1) × 100", lineage(parent[(MASS, "2023")], parent[(MASS, "2024")])),
        Measurement("CN75 derived value-per-mass change", unit_change, "percent", "change in EUR per 100 kg diagnostic", lineage(parent[(VALUE, "2023")], parent[(VALUE, "2024")], parent[(MASS, "2023")], parent[(MASS, "2024")])),
        Measurement("CN8 contribution to CN2 value change", child_value_contribution, "percent", "CN8 value delta / CN2 value delta × 100", lineage(child[(VALUE, "2023")], child[(VALUE, "2024")], parent[(VALUE, "2023")], parent[(VALUE, "2024")])),
        Measurement("CN8 contribution to CN2 mass change", child_mass_contribution, "percent", "CN8 mass delta / CN2 mass delta × 100", lineage(child[(MASS, "2023")], child[(MASS, "2024")], parent[(MASS, "2023")], parent[(MASS, "2024")])),
        Measurement("France and Italy contribution to CN8 value change", partner_value_contribution, "percent", "combined FR+IT value delta / CN8 value delta × 100", lineage(*selected_partner_value_items)),
        Measurement("France and Italy contribution to CN8 mass change", partner_mass_contribution, "percent", "combined FR+IT mass delta / CN8 mass delta × 100", lineage(*selected_partner_mass_items)),
        Measurement("CN8 supplier value HHI 2023", hhi23, "HHI (0–1)", "sum of squared value shares across reported two-letter country/territory partners", hhi23_lineage),
        Measurement("CN8 supplier value HHI 2024", hhi24, "HHI (0–1)", "sum of squared value shares across reported two-letter country/territory partners", hhi24_lineage),
        Measurement("CN8 supplier value HHI change", hhi24 - hhi23, "HHI points", "2024 HHI - 2023 HHI", tuple(dict.fromkeys((*hhi23_lineage, *hhi24_lineage)))),
    )

    relationships = (
        EvidenceRelationship("CN8 75022000", "PART_OF", "CN2 75", "source-native / structural", lineage(*child.values())),
        EvidenceRelationship("France (FR)", "SUPPLIES", "CN8 75022000 → Czechia (CZ)", "source-native / structural", lineage(*(partners[("FR", m, y)] for m in (VALUE, MASS) for y in YEARS))),
        EvidenceRelationship("Italy (IT)", "SUPPLIES", "CN8 75022000 → Czechia (CZ)", "source-native / structural", lineage(*(partners[("IT", m, y)] for m in (VALUE, MASS) for y in YEARS))),
    )
    survives = child_value_contribution > 50 and child_mass_contribution > 50
    concentration_direction = "increased" if hhi24 > hhi23 else "decreased"
    entities = (
        EconomicEntity("product", "CN2 75", parent[(VALUE, "2024")]["product_label"]),
        EconomicEntity("product", "CN8 75022000", child[(VALUE, "2024")]["product_label"]),
        EconomicEntity("reporter", "CZ", parent[(VALUE, "2024")]["reporter_label"]),
        EconomicEntity("partner", "FR", partners[("FR", VALUE, "2024")]["partner_label"]),
        EconomicEntity("partner", "IT", partners[("IT", VALUE, "2024")]["partner_label"]),
    )
    return DisequilibriumArgument(
        entities=entities,
        measurements=measurements,
        relationships=relationships,
        detected=(f"Czech CN75 import value changed {_fmt_percent(value_growth)} and net mass changed {_fmt_percent(mass_growth)} from 2023 to 2024.",),
        unusual=(f"Physical mass grew {mass_growth - value_growth:.2f} percentage points faster than trade value; the derived value per 100 kg diagnostic changed {_fmt_percent(unit_change)}.",),
        decomposition=(f"CN8 75022000 — {child[(VALUE, '2024')]['product_label']} — contributed {child_value_contribution:.2f}% of the CN75 value change and {child_mass_contribution:.2f}% of its mass change.", f"The parent anomaly {'survives' if survives else 'does not clearly survive'} this selected-child decomposition."),
        geography=(f"France and Italy together contributed {partner_value_contribution:.2f}% of the selected CN8 value change and {partner_mass_contribution:.2f}% of its mass change.", f"Supplier value HHI {concentration_direction} from {hhi23:.4f} to {hhi24:.4f} ({hhi24 - hhi23:+.4f})."),
        supported_interpretation=(f"Czech imports of nickel expanded materially in physical terms from 2023 to 2024. The increase was dominated by unwrought nickel alloys, especially supply from France and Italy, while derived value per unit mass declined and supplier concentration {concentration_direction}.",),
        not_supported=("The evidence does not establish that nickel market prices fell, Czech industrial demand increased, inventories were rebuilt, EV or battery demand caused the change, French or Italian production expanded, or that this is a commercial opportunity.",),
        alternative_explanations=("Unresolved explanations include product mix within CN8, contract timing, inventory movements, source-country rerouting, exchange-rate effects, revisions, confidentiality, and changes in domestic use or re-export.",),
        next_best_evidence=("Official nickel price or import-price indices, followed by Czech industrial production, inventory, and end-use evidence, would most reduce uncertainty.",),
    )
