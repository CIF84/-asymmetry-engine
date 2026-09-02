from datetime import datetime, timezone

import pytest

from asymmetry_engine.cli import main
from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.reasoning import ReasoningError, build_cn75_argument
from asymmetry_engine.sources.comext import DATASET, normalize_cell, comext_source

NOW = datetime(2026, 9, 4, 12, tzinfo=timezone.utc)


def observation(product, product_label, partner, partner_label, measure, year, value):
    unit_label = "VALUE_IN_EUROS" if measure == "VALUE_IN_EUROS" else "QUANTITY_IN_100KG"
    cell = {
        "dimensions": {
            "freq": "A",
            "reporter": "CZ",
            "partner": partner,
            "product": product,
            "flow": "1",
            "indicators": measure,
            "time": year,
        },
        "labels": {
            "freq": "Annual",
            "reporter": "Czechia",
            "partner": partner_label,
            "product": product_label,
            "flow": "IMPORT",
            "indicators": unit_label,
            "time": year,
        },
        "value": value,
        "status": None,
    }
    return normalize_cell(cell, NOW, "https://example.invalid/comext")


def evidence():
    result = []
    parent = {("VALUE_IN_EUROS", "2023"): 100, ("VALUE_IN_EUROS", "2024"): 126.74,
              ("QUANTITY_IN_100KG", "2023"): 100, ("QUANTITY_IN_100KG", "2024"): 147.6}
    child = {("VALUE_IN_EUROS", "2023"): 50, ("VALUE_IN_EUROS", "2024"): 75,
             ("QUANTITY_IN_100KG", "2023"): 40, ("QUANTITY_IN_100KG", "2024"): 85}
    for (measure, year), value in parent.items():
        result.append(observation("75", "NICKEL AND ARTICLES THEREOF", "WORLD", "World", measure, year, value))
    for (measure, year), value in child.items():
        result.append(observation("75022000", "UNWROUGHT NICKEL ALLOYS", "WORLD", "World", measure, year, value))
    partner_values = {
        "FR": {("VALUE_IN_EUROS", "2023"): 20, ("VALUE_IN_EUROS", "2024"): 40,
               ("QUANTITY_IN_100KG", "2023"): 15, ("QUANTITY_IN_100KG", "2024"): 40},
        "IT": {("VALUE_IN_EUROS", "2023"): 10, ("VALUE_IN_EUROS", "2024"): 20,
               ("QUANTITY_IN_100KG", "2023"): 10, ("QUANTITY_IN_100KG", "2024"): 25},
        "DE": {("VALUE_IN_EUROS", "2023"): 20, ("VALUE_IN_EUROS", "2024"): 15,
               ("QUANTITY_IN_100KG", "2023"): 15, ("QUANTITY_IN_100KG", "2024"): 20},
    }
    labels = {"FR": "France", "IT": "Italy", "DE": "Germany"}
    for partner, values in partner_values.items():
        for (measure, year), value in values.items():
            result.append(observation("75022000", "UNWROUGHT NICKEL ALLOYS", partner, labels[partner], measure, year, value))
    return result


def populated_repository(path):
    class Collector:
        source = comext_source()

        def collect(self):
            return evidence()

    repository = Repository(path)
    result = run_collection(Collector(), repository, lambda: NOW)
    assert result.inserted_count == len(evidence())
    return repository


def test_extracts_persisted_cn75_evidence_and_calculates_growth(tmp_path):
    repository = populated_repository(tmp_path / "reason.db")
    argument = build_cn75_argument(repository)
    assert argument.measurement("CN75 value growth").value == pytest.approx(26.74)
    assert argument.measurement("CN75 mass growth").value == pytest.approx(47.6)
    assert argument.measurement("CN75 derived value-per-mass change").value == pytest.approx(-14.13, abs=.01)
    repository.close()


def test_value_mass_and_partner_contributions_are_explicit(tmp_path):
    repository = populated_repository(tmp_path / "reason.db")
    argument = build_cn75_argument(repository)
    assert argument.measurement("CN8 contribution to CN2 value change").value == pytest.approx(25 / 26.74 * 100)
    assert argument.measurement("CN8 contribution to CN2 mass change").value == pytest.approx(45 / 47.6 * 100)
    assert argument.measurement("France and Italy contribution to CN8 value change").value == pytest.approx(120)
    assert argument.measurement("France and Italy contribution to CN8 mass change").value == pytest.approx(40 / 45 * 100)
    repository.close()


def test_supplier_concentration_uses_country_value_shares(tmp_path):
    repository = populated_repository(tmp_path / "reason.db")
    argument = build_cn75_argument(repository)
    assert argument.measurement("CN8 supplier value HHI 2023").value == pytest.approx(.36)
    assert argument.measurement("CN8 supplier value HHI 2024").value == pytest.approx((40 / 75) ** 2 + (20 / 75) ** 2 + (15 / 75) ** 2)
    assert argument.measurement("CN8 supplier value HHI change").value > 0
    repository.close()


def test_structural_relationships_and_exact_lineage_are_retained(tmp_path):
    repository = populated_repository(tmp_path / "reason.db")
    argument = build_cn75_argument(repository)
    parent = next(item for item in argument.relationships if item.predicate == "PART_OF")
    assert (parent.subject, parent.object, parent.basis) == ("CN8 75022000", "CN2 75", "source-native / structural")
    france = next(item for item in argument.relationships if item.subject == "France (FR)")
    assert france.predicate == "SUPPLIES"
    assert all(item.startswith(f"comext:{DATASET}:CZ:1:FR:75022000:") for item in france.observation_ids)
    growth = argument.measurement("CN75 value growth")
    assert growth.observation_ids == (
        f"comext:{DATASET}:CZ:1:WORLD:75:VALUE_IN_EUROS:EUR:2023",
        f"comext:{DATASET}:CZ:1:WORLD:75:VALUE_IN_EUROS:EUR:2024",
    )
    repository.close()


def test_supported_interpretation_does_not_claim_market_price(tmp_path):
    repository = populated_repository(tmp_path / "reason.db")
    argument = build_cn75_argument(repository)
    supported = " ".join(argument.supported_interpretation).lower()
    assert "price" not in supported
    assert "derived value per unit mass" in supported
    assert "nickel market prices fell" in " ".join(argument.not_supported).lower()
    repository.close()


def test_missing_required_evidence_fails_clearly(tmp_path):
    repository = Repository(tmp_path / "empty.db")
    with pytest.raises(ReasoningError, match="Missing required Comext evidence"):
        build_cn75_argument(repository)
    repository.close()


def test_cli_output_is_deterministic_for_fixed_evidence(tmp_path, capsys):
    path = tmp_path / "reason.db"
    populated_repository(path).close()
    assert main(["reason-cn75", "--database", str(path)]) == 0
    first = capsys.readouterr().out
    assert main(["reason-cn75", "--database", str(path)]) == 0
    second = capsys.readouterr().out
    assert first == second
    assert "DETECTED\n" in first
    assert "LINEAGE\n" in first
