#!/usr/bin/env python3
"""Validate AI-Verse Safe Infrastructure Qualification v1 evidence."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "ai-verse.safe-infrastructure-qualification/v1"
IDENTITY_CONTRACT = "ai-verse.durable-identity-reference/v1"
UPGRADE_CONTRACT = "ai-verse.infrastructure-upgrade/v1"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
HEX40_ANYWHERE = re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE)

FORBIDDEN_DEFAULT_SUMMARY_PATTERNS = [
    re.compile(r"\bworkspaces/", re.IGNORECASE),
    re.compile(r"\.git(?:/|\b)", re.IGNORECASE),
    re.compile(r"\brelease[_ -]?set[_ -]?id\b", re.IGNORECASE),
    re.compile(r"\bcomponent[_ -]?id\b", re.IGNORECASE),
    re.compile(r"\binfrastructure generation\b", re.IGNORECASE),
    re.compile(r"\bmigration recipe\b", re.IGNORECASE),
    re.compile(r"\brecipe id\b", re.IGNORECASE),
    re.compile(r"\bowner id\b", re.IGNORECASE),
]

TOP_KEYS = {"schema_version", "target", "identity_contract", "upgrade_contract", "sections", "overall"}
TARGET_KEYS = {"release_set_id", "component_revisions"}
SECTION_KEYS = {"convergence", "restore", "doctor", "member_ux"}
CONVERGENCE_KEYS = {
    "status",
    "same_exact_target",
    "target_contract_equivalent",
    "user_state_preserved",
    "identity_reference_verified",
    "ambiguity_avoided",
    "evidence",
}
RESTORE_KEYS = {
    "status",
    "covered_state_exact",
    "software_exact",
    "owner_rebuild_verified",
    "exclusions_truthful",
    "retained_target_survived",
    "identity_reference_verified",
    "evidence",
}
DOCTOR_KEYS = {
    "status",
    "command",
    "aggregate_ok",
    "read_only",
    "required_owner_checks",
    "owner_results",
    "composed_system_checked",
    "failure_injection",
    "evidence",
}
UX_KEYS = {
    "status",
    "default_summary",
    "plain_english",
    "small_screen",
    "read_only_preview_language",
    "internal_jargon_required",
    "technical_evidence_available",
    "evidence",
}
EVIDENCE_KEYS = {"kind", "owner", "ref", "result"}
OWNER_RESULT_KEYS = {"owner", "status"}
FAILURE_KEYS = {"injected_owner", "aggregate_ok", "unrelated_checks_continued"}


def _object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def _exact_keys(obj: dict[str, Any], expected: set[str], path: str, errors: list[str], *, optional: set[str] | None = None) -> None:
    optional = optional or set()
    missing = expected - set(obj)
    unknown = set(obj) - expected - optional
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"{path}: unknown keys: {', '.join(sorted(unknown))}")


def _bool(obj: dict[str, Any], key: str, path: str, errors: list[str]) -> bool | None:
    value = obj.get(key)
    if not isinstance(value, bool):
        errors.append(f"{path}.{key}: expected boolean")
        return None
    return value


def _status(obj: dict[str, Any], path: str, errors: list[str]) -> str | None:
    value = obj.get("status")
    if value not in {"PASS", "FAIL"}:
        errors.append(f"{path}.status: expected PASS or FAIL")
        return None
    return value


def _evidence(value: Any, path: str, errors: list[str], *, require_pass: bool) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{path}: expected non-empty evidence array")
        return
    for index, item in enumerate(value):
        item_path = f"{path}[{index}]"
        obj = _object(item, item_path, errors)
        if not obj:
            continue
        _exact_keys(obj, EVIDENCE_KEYS - {"owner"}, item_path, errors, optional={"owner"})
        for key in ("kind", "ref"):
            if not isinstance(obj.get(key), str) or not obj.get(key):
                errors.append(f"{item_path}.{key}: expected non-empty string")
        if "owner" in obj and (not isinstance(obj.get("owner"), str) or not obj.get("owner")):
            errors.append(f"{item_path}.owner: expected non-empty string when present")
        if obj.get("result") not in {"PASS", "FAIL"}:
            errors.append(f"{item_path}.result: expected PASS or FAIL")
        if require_pass and obj.get("result") != "PASS":
            errors.append(f"{item_path}.result: PASS section cannot rely on failed evidence")


def _all_true(obj: dict[str, Any], keys: tuple[str, ...], path: str, errors: list[str]) -> None:
    for key in keys:
        if obj.get(key) is not True:
            errors.append(f"{path}.{key}: must be true when section status is PASS")


def validate_qualification(data: Any) -> list[str]:
    errors: list[str] = []
    root = _object(data, "$", errors)
    if not root:
        return errors
    _exact_keys(root, TOP_KEYS, "$", errors)

    if root.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"$.schema_version: expected {SCHEMA_VERSION!r}")
    if root.get("identity_contract") != IDENTITY_CONTRACT:
        errors.append(f"$.identity_contract: expected {IDENTITY_CONTRACT!r}")
    if root.get("upgrade_contract") != UPGRADE_CONTRACT:
        errors.append(f"$.upgrade_contract: expected {UPGRADE_CONTRACT!r}")
    if root.get("overall") not in {"PASS", "FAIL"}:
        errors.append("$.overall: expected PASS or FAIL")

    target = _object(root.get("target"), "$.target", errors)
    if target:
        _exact_keys(target, TARGET_KEYS, "$.target", errors)
        release_set_id = target.get("release_set_id")
        if not isinstance(release_set_id, str) or not release_set_id:
            errors.append("$.target.release_set_id: expected non-empty string")
        revisions = target.get("component_revisions")
        if not isinstance(revisions, dict) or not revisions:
            errors.append("$.target.component_revisions: expected non-empty object")
        else:
            for component, revision in revisions.items():
                if not isinstance(component, str) or not component:
                    errors.append("$.target.component_revisions: component keys must be non-empty strings")
                if not isinstance(revision, str) or not SHA40.fullmatch(revision):
                    errors.append(f"$.target.component_revisions.{component}: expected exact lowercase 40-character Git SHA")

    sections = _object(root.get("sections"), "$.sections", errors)
    section_statuses: dict[str, str | None] = {}
    if sections:
        _exact_keys(sections, SECTION_KEYS, "$.sections", errors)

        convergence = _object(sections.get("convergence"), "$.sections.convergence", errors)
        if convergence:
            _exact_keys(convergence, CONVERGENCE_KEYS, "$.sections.convergence", errors)
            status = _status(convergence, "$.sections.convergence", errors)
            section_statuses["convergence"] = status
            for key in (
                "same_exact_target",
                "target_contract_equivalent",
                "user_state_preserved",
                "identity_reference_verified",
                "ambiguity_avoided",
            ):
                _bool(convergence, key, "$.sections.convergence", errors)
            if status == "PASS":
                _all_true(
                    convergence,
                    (
                        "same_exact_target",
                        "target_contract_equivalent",
                        "user_state_preserved",
                        "identity_reference_verified",
                        "ambiguity_avoided",
                    ),
                    "$.sections.convergence",
                    errors,
                )
            _evidence(convergence.get("evidence"), "$.sections.convergence.evidence", errors, require_pass=status == "PASS")

        restore = _object(sections.get("restore"), "$.sections.restore", errors)
        if restore:
            _exact_keys(restore, RESTORE_KEYS, "$.sections.restore", errors)
            status = _status(restore, "$.sections.restore", errors)
            section_statuses["restore"] = status
            for key in (
                "covered_state_exact",
                "software_exact",
                "owner_rebuild_verified",
                "exclusions_truthful",
                "retained_target_survived",
                "identity_reference_verified",
            ):
                _bool(restore, key, "$.sections.restore", errors)
            if status == "PASS":
                _all_true(
                    restore,
                    (
                        "covered_state_exact",
                        "software_exact",
                        "owner_rebuild_verified",
                        "exclusions_truthful",
                        "retained_target_survived",
                        "identity_reference_verified",
                    ),
                    "$.sections.restore",
                    errors,
                )
            _evidence(restore.get("evidence"), "$.sections.restore.evidence", errors, require_pass=status == "PASS")

        doctor = _object(sections.get("doctor"), "$.sections.doctor", errors)
        if doctor:
            _exact_keys(doctor, DOCTOR_KEYS, "$.sections.doctor", errors)
            status = _status(doctor, "$.sections.doctor", errors)
            section_statuses["doctor"] = status
            if doctor.get("command") != "aiverse doctor":
                errors.append("$.sections.doctor.command: expected 'aiverse doctor'")
            aggregate_ok = _bool(doctor, "aggregate_ok", "$.sections.doctor", errors)
            read_only = _bool(doctor, "read_only", "$.sections.doctor", errors)
            if read_only is False:
                errors.append("$.sections.doctor.read_only: doctor must remain read-only")
            _bool(doctor, "composed_system_checked", "$.sections.doctor", errors)

            required = doctor.get("required_owner_checks")
            required_owners: list[str] = []
            if not isinstance(required, list) or not required or any(not isinstance(x, str) or not x for x in required):
                errors.append("$.sections.doctor.required_owner_checks: expected non-empty array of owner strings")
            elif len(required) != len(set(required)):
                errors.append("$.sections.doctor.required_owner_checks: duplicates are not allowed")
            else:
                required_owners = list(required)

            owner_results = doctor.get("owner_results")
            seen: dict[str, str] = {}
            if not isinstance(owner_results, list) or not owner_results:
                errors.append("$.sections.doctor.owner_results: expected non-empty array")
            else:
                for index, item in enumerate(owner_results):
                    item_path = f"$.sections.doctor.owner_results[{index}]"
                    obj = _object(item, item_path, errors)
                    if not obj:
                        continue
                    _exact_keys(obj, OWNER_RESULT_KEYS, item_path, errors)
                    owner = obj.get("owner")
                    item_status = obj.get("status")
                    if not isinstance(owner, str) or not owner:
                        errors.append(f"{item_path}.owner: expected non-empty string")
                        continue
                    if owner in seen:
                        errors.append(f"$.sections.doctor.owner_results: duplicate owner result for {owner}")
                    if item_status not in {"PASS", "FAIL", "NOT_APPLICABLE"}:
                        errors.append(f"{item_path}.status: invalid owner result")
                    seen[owner] = item_status
            for owner in required_owners:
                if owner not in seen:
                    errors.append(f"$.sections.doctor.owner_results: missing required owner result for {owner}")
            if status == "PASS":
                if aggregate_ok is not True:
                    errors.append("$.sections.doctor.aggregate_ok: PASS doctor qualification requires aggregate_ok=true")
                for owner in required_owners:
                    if seen.get(owner) != "PASS":
                        errors.append(f"$.sections.doctor.owner_results: required owner {owner} must PASS")

            failure = _object(doctor.get("failure_injection"), "$.sections.doctor.failure_injection", errors)
            if failure:
                _exact_keys(failure, FAILURE_KEYS, "$.sections.doctor.failure_injection", errors)
                injected = failure.get("injected_owner")
                if not isinstance(injected, str) or not injected:
                    errors.append("$.sections.doctor.failure_injection.injected_owner: expected non-empty string")
                elif required_owners and injected not in required_owners:
                    errors.append("$.sections.doctor.failure_injection.injected_owner: must name a required owner")
                if failure.get("aggregate_ok") is not False:
                    errors.append("$.sections.doctor.failure_injection.aggregate_ok: injected required-owner failure must make aggregate_ok=false")
                if failure.get("unrelated_checks_continued") is not True:
                    errors.append("$.sections.doctor.failure_injection.unrelated_checks_continued: unrelated safe checks must continue")
            _evidence(doctor.get("evidence"), "$.sections.doctor.evidence", errors, require_pass=status == "PASS")

        ux = _object(sections.get("member_ux"), "$.sections.member_ux", errors)
        if ux:
            _exact_keys(ux, UX_KEYS, "$.sections.member_ux", errors)
            status = _status(ux, "$.sections.member_ux", errors)
            section_statuses["member_ux"] = status
            for key in (
                "plain_english",
                "small_screen",
                "read_only_preview_language",
                "internal_jargon_required",
                "technical_evidence_available",
            ):
                _bool(ux, key, "$.sections.member_ux", errors)
            if status == "PASS":
                _all_true(
                    ux,
                    ("plain_english", "small_screen", "read_only_preview_language", "technical_evidence_available"),
                    "$.sections.member_ux",
                    errors,
                )
                if ux.get("internal_jargon_required") is not False:
                    errors.append("$.sections.member_ux.internal_jargon_required: must be false when section status is PASS")
            summary = ux.get("default_summary")
            if not isinstance(summary, str) or not summary.strip():
                errors.append("$.sections.member_ux.default_summary: expected non-empty string")
            else:
                nonempty_lines = [line for line in summary.splitlines() if line.strip()]
                if len(summary) > 900:
                    errors.append("$.sections.member_ux.default_summary: exceeds 900 characters")
                if len(nonempty_lines) > 12:
                    errors.append("$.sections.member_ux.default_summary: exceeds 12 non-empty lines")
                if HEX40_ANYWHERE.search(summary):
                    errors.append("$.sections.member_ux.default_summary: default output must not expose Git SHA values")
                for pattern in FORBIDDEN_DEFAULT_SUMMARY_PATTERNS:
                    if pattern.search(summary):
                        errors.append("$.sections.member_ux.default_summary: default output contains internal architecture jargon")
                        break
            _evidence(ux.get("evidence"), "$.sections.member_ux.evidence", errors, require_pass=status == "PASS")

    if root.get("overall") == "PASS":
        missing = SECTION_KEYS - set(section_statuses)
        if missing:
            errors.append("$.overall: cannot PASS with missing sections")
        for name in SECTION_KEYS:
            if section_statuses.get(name) != "PASS":
                errors.append(f"$.overall: cannot PASS when {name} is not PASS")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("qualification", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.qualification.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    errors = validate_qualification(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID {data['target']['release_set_id']} {data['overall']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
