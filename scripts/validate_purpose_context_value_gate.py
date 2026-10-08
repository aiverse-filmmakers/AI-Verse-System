#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED_OUTCOMES = {"VALUE PROVEN", "PARTIALLY PROVEN", "NOT PROVEN"}
REQUIRED_EVIDENCE = {
    "gateway_task_1_head",
    "gateway_task_2_head",
    "gateway_task_3_head",
    "gateway_accepted_head",
    "os_accepted_head",
    "gateway_ci",
    "context_ladder",
    "permanent_bot_boundary",
    "automation_boundary",
    "temporary_worker_boundary",
}
REQUIRED_PROOFS = {
    "strategic_decision_basis_positive_all_frozen_scenarios",
    "next_action_improvement",
    "prioritization_improvement",
    "blocker_awareness_improvement",
    "explainability_improvement",
    "cross_session_projection_stability",
    "trivial_task_zero_purpose_reads",
    "purpose_envelope_within_16384_bytes",
    "relevant_owner_reads_bounded_to_one",
    "purpose_unavailable_preserves_ordinary_execution",
    "context_noise_unrelated_scope_refs_zero",
    "workspace_isolation_regression",
    "authority_regression",
    "provider_cost_measured",
    "production_model_output_measured",
}


def validate(payload):
    errors = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if payload.get("slice") != "7.3":
        errors.append("slice must be 7.3")

    outcome = payload.get("outcome")
    if outcome not in ALLOWED_OUTCOMES:
        errors.append("outcome must be exactly VALUE PROVEN, PARTIALLY PROVEN, or NOT PROVEN")

    allowed = payload.get("phase_8_allowed")
    if not isinstance(allowed, bool):
        errors.append("phase_8_allowed must be boolean")
    elif allowed != (outcome == "VALUE PROVEN"):
        errors.append("phase_8_allowed must be true only when outcome is VALUE PROVEN")

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict):
        errors.append("evidence must be an object")
    else:
        missing = sorted(REQUIRED_EVIDENCE - set(evidence))
        if missing:
            errors.append(f"evidence missing: {', '.join(missing)}")
        for key in REQUIRED_EVIDENCE & set(evidence):
            value = evidence[key]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"evidence.{key} must be a non-empty string")

    proofs = payload.get("proofs")
    if not isinstance(proofs, dict):
        errors.append("proofs must be an object")
    else:
        missing = sorted(REQUIRED_PROOFS - set(proofs))
        if missing:
            errors.append(f"proofs missing: {', '.join(missing)}")
        for key in REQUIRED_PROOFS & set(proofs):
            if not isinstance(proofs[key], bool):
                errors.append(f"proofs.{key} must be boolean")

        if outcome == "VALUE PROVEN":
            must_be_true = {
                "strategic_decision_basis_positive_all_frozen_scenarios",
                "next_action_improvement",
                "prioritization_improvement",
                "blocker_awareness_improvement",
                "explainability_improvement",
                "cross_session_projection_stability",
                "trivial_task_zero_purpose_reads",
                "purpose_envelope_within_16384_bytes",
                "relevant_owner_reads_bounded_to_one",
                "purpose_unavailable_preserves_ordinary_execution",
                "context_noise_unrelated_scope_refs_zero",
            }
            for key in sorted(must_be_true):
                if proofs.get(key) is not True:
                    errors.append(f"VALUE PROVEN requires proofs.{key}=true")
            for key in ("workspace_isolation_regression", "authority_regression"):
                if proofs.get(key) is not False:
                    errors.append(f"VALUE PROVEN requires proofs.{key}=false")

    caveats = payload.get("measurement_caveats")
    if not isinstance(caveats, list) or not caveats or not all(isinstance(item, str) and item.strip() for item in caveats):
        errors.append("measurement_caveats must be a non-empty list of strings")

    decision_basis = payload.get("decision_basis")
    if not isinstance(decision_basis, str) or not decision_basis.strip():
        errors.append("decision_basis must be a non-empty string")

    return errors


def main(argv):
    if len(argv) != 2:
        print("usage: validate_purpose_context_value_gate.py <gate.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    payload = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(payload)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"purpose-context value gate valid: {payload['outcome']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
