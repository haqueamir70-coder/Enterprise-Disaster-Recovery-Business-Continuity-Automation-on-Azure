"""Rule-based checks for synthetic BCDR plans; not a live Azure health probe."""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import asdict

from .models import RecoveryPlan

ALLOWED_TIERS = {"tier-0", "tier-1", "tier-2", "tier-3"}
ALLOWED_EXERCISES = {
    "tabletop",
    "test-failover",
    "planned-failover",
    "unplanned-failover",
    "failback",
}


def validate_plan(plan: RecoveryPlan) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    names = [workload.name for workload in plan.workloads]
    if len(names) != len(set(names)):
        errors.append("Workload names must be unique.")
    if plan.primary_region.strip().lower() == plan.recovery_region.strip().lower():
        errors.append("Primary and recovery regions must be different.")
    if plan.exercise_type not in ALLOWED_EXERCISES:
        errors.append(f"Unsupported exercise_type '{plan.exercise_type}'.")

    by_name = {workload.name: workload for workload in plan.workloads}
    for workload in plan.workloads:
        if workload.tier not in ALLOWED_TIERS:
            errors.append(f"{workload.name}: invalid tier '{workload.tier}'.")
        if workload.rto_minutes <= 0 or workload.rpo_minutes < 0:
            errors.append(f"{workload.name}: RTO must be positive and RPO cannot be negative.")
        if workload.recovery_order < 1:
            errors.append(f"{workload.name}: recovery_order must be >= 1.")
        if not workload.recovery_method.strip():
            errors.append(f"{workload.name}: recovery_method cannot be empty.")
        for dependency in workload.dependencies:
            if dependency not in by_name:
                errors.append(f"{workload.name}: dependency '{dependency}' does not exist.")
            elif dependency == workload.name:
                errors.append(f"{workload.name}: workload cannot depend on itself.")

    # Topological cycle check: edges point from prerequisite to dependent.
    indegree = {name: 0 for name in names}
    dependents: dict[str, list[str]] = defaultdict(list)
    for workload in plan.workloads:
        for dependency in workload.dependencies:
            if dependency in by_name and dependency != workload.name:
                indegree[workload.name] += 1
                dependents[dependency].append(workload.name)
    queue = deque(name for name, degree in indegree.items() if degree == 0)
    visited: list[str] = []
    while queue:
        current = queue.popleft()
        visited.append(current)
        for child in dependents[current]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if len(visited) != len(names):
        errors.append("Dependency cycle detected; recovery order cannot be calculated.")

    for workload in plan.workloads:
        for dependency in workload.dependencies:
            if (
                dependency in by_name
                and by_name[dependency].recovery_order >= workload.recovery_order
            ):
                errors.append(
                    f"{workload.name}: dependency '{dependency}' must have a lower recovery_order."
                )

    if plan.exercise_type == "test-failover":
        warnings.append(
            "Confirm the target is an isolated test network and cleanup is approved "
            "before execution."
        )
    if plan.exercise_type in {"planned-failover", "unplanned-failover", "failback"}:
        warnings.append(
            "This validator does not execute failover. Require change approval, "
            "operator authorization and service-specific checks."
        )
    for workload in plan.workloads:
        if workload.rpo_minutes == 0:
            warnings.append(
                f"{workload.name}: RPO 0 is a demanding target; verify service guarantees "
                "and synchronous replication semantics."
            )

    ordered = sorted(plan.workloads, key=lambda workload: (workload.recovery_order, workload.name))
    return {
        "plan_name": plan.plan_name,
        "exercise_type": plan.exercise_type,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "recovery_sequence": [workload.name for workload in ordered],
        "workload_count": len(plan.workloads),
        "workloads": [asdict(workload) for workload in ordered],
        "scope_note": (
            "Synthetic model validation only; no Azure API, replication, backup or recovery test "
            "was performed."
        ),
    }
