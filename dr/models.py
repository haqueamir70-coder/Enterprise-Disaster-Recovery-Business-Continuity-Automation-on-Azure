"""Typed data structures for synthetic recovery plans."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Workload:
    name: str
    tier: str
    rto_minutes: int
    rpo_minutes: int
    dependencies: tuple[str, ...]
    recovery_order: int
    recovery_method: str


@dataclass(frozen=True)
class RecoveryPlan:
    plan_name: str
    primary_region: str
    recovery_region: str
    exercise_type: str
    workloads: tuple[Workload, ...]


def parse_plan(raw: dict[str, Any]) -> RecoveryPlan:
    """Parse a JSON object, rejecting missing or incorrectly typed core fields."""
    required = ("plan_name", "primary_region", "recovery_region", "exercise_type", "workloads")
    missing = [key for key in required if key not in raw]
    if missing:
        raise ValueError(f"Missing plan fields: {', '.join(missing)}")
    if not isinstance(raw["workloads"], list) or not raw["workloads"]:
        raise ValueError("workloads must be a non-empty list")

    workloads: list[Workload] = []
    required_workload_fields = (
        "name", "tier", "rto_minutes", "rpo_minutes", "dependencies",
        "recovery_order", "recovery_method",
    )
    for index, item in enumerate(raw["workloads"]):
        if not isinstance(item, dict):
            raise ValueError(f"workloads[{index}] must be an object")
        for key in required_workload_fields:
            if key not in item:
                raise ValueError(f"workloads[{index}] is missing '{key}'")
        if not isinstance(item["dependencies"], list) or not all(
            isinstance(value, str) for value in item["dependencies"]
        ):
            raise ValueError(f"workloads[{index}].dependencies must be a list of strings")
        try:
            rto = int(item["rto_minutes"])
            rpo = int(item["rpo_minutes"])
            order = int(item["recovery_order"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"workloads[{index}] RTO/RPO/order must be integers") from exc
        workloads.append(
            Workload(
                name=str(item["name"]),
                tier=str(item["tier"]),
                rto_minutes=rto,
                rpo_minutes=rpo,
                dependencies=tuple(item["dependencies"]),
                recovery_order=order,
                recovery_method=str(item["recovery_method"]),
            )
        )
    return RecoveryPlan(
        plan_name=str(raw["plan_name"]),
        primary_region=str(raw["primary_region"]),
        recovery_region=str(raw["recovery_region"]),
        exercise_type=str(raw["exercise_type"]),
        workloads=tuple(workloads),
    )
