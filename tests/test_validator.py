import json
from pathlib import Path

from dr.models import parse_plan
from dr.validator import validate_plan

SAMPLE = Path("dr/plans/sample-enterprise.json")


def load_sample():
    return parse_plan(json.loads(SAMPLE.read_text(encoding="utf-8")))


def test_sample_plan_passes_and_orders_dependencies():
    report = validate_plan(load_sample())
    assert report["status"] == "PASS"
    sequence = report["recovery_sequence"]
    assert sequence.index("identity-network") < sequence.index("data-platform")
    assert sequence.index("data-platform") < sequence.index("customer-api")


def test_missing_dependency_fails():
    raw = json.loads(SAMPLE.read_text(encoding="utf-8"))
    raw["workloads"][0]["dependencies"] = ["unknown-service"]
    report = validate_plan(parse_plan(raw))
    assert report["status"] == "FAIL"
    assert any("does not exist" in error for error in report["errors"])


def test_dependency_cycle_fails():
    raw = json.loads(SAMPLE.read_text(encoding="utf-8"))
    raw["workloads"][0]["dependencies"] = ["customer-api"]
    report = validate_plan(parse_plan(raw))
    assert report["status"] == "FAIL"
    assert any("cycle" in error.lower() for error in report["errors"])


def test_dependency_must_recover_first():
    raw = json.loads(SAMPLE.read_text(encoding="utf-8"))
    raw["workloads"][2]["recovery_order"] = 1
    report = validate_plan(parse_plan(raw))
    assert report["status"] == "FAIL"
    assert any("lower recovery_order" in error for error in report["errors"])


def test_same_region_is_rejected():
    raw = json.loads(SAMPLE.read_text(encoding="utf-8"))
    raw["recovery_region"] = raw["primary_region"]
    assert validate_plan(parse_plan(raw))["status"] == "FAIL"


def test_zero_rpo_produces_a_caution():
    raw = json.loads(SAMPLE.read_text(encoding="utf-8"))
    raw["workloads"][0]["rpo_minutes"] = 0
    report = validate_plan(parse_plan(raw))
    assert any("RPO 0" in warning for warning in report["warnings"])
