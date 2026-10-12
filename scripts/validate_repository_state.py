#!/usr/bin/env python3
"""Validate AI-Verse Repository State v1 against the canonical Registry.

Repository State is dynamic observation/evidence only. Static ownership and identity
facts remain in the Repository Registry. This validator is fail-closed and does not
perform network access or infer missing acceptance evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

STATE_VERSION = "ai-verse.repository-state/v1"
REGISTRY_VERSION = "ai-verse.repository-registry/v1"
STATE_ID = "ai-verse.repository-network"
SHA40 = re.compile(r"^[0-9a-f]{40}$")

TOP_LEVEL_KEYS = {
    "schema_version",
    "state_id",
    "registry_binding",
    "refresh",
    "watchdog",
    "repositories",
    "drift",
    "semantics",
}
REGISTRY_BINDING_KEYS = {"path", "schema_version", "blob_sha"}
REFRESH_KEYS = {
    "mode",
    "scope",
    "status",
    "repository_ids",
    "evidence_revision",
    "last_scoped_refresh",
    "last_full_refresh",
}
REFRESH_RECORD_KEYS = {"scope", "status", "evidence_revision", "observed_at"}
WATCHDOG_KEYS = {"status", "heartbeat_revision", "last_successful_full_scan", "reason"}
REPOSITORY_KEYS = {
    "repository_id",
    "access",
    "observed_head",
    "owner_acceptance",
    "distribution_pin",
    "descriptor",
    "system_sync",
    "freshness",
}
EVIDENCE_STATE_KEYS = {"status", "revision", "evidence_refs"}
DISTRIBUTION_PIN_KEYS = {"status", "revision", "release_id", "evidence_refs"}
DESCRIPTOR_KEYS = {"status", "revision", "release_status", "blob_sha", "evidence_refs"}
SYSTEM_SYNC_KEYS = {"status", "checkpoint_revision", "evidence_refs"}
FRESHNESS_KEYS = {"scope", "status", "evidence_revision"}
DRIFT_KEYS = {
    "id",
    "marker",
    "status",
    "severity",
    "scope",
    "repository_ids",
    "reason",
    "evidence_refs",
    "required_action",
}
SEMANTICS_KEYS = {
    "dynamic_state_only",
    "registry_static_truth_authority",
    "human_ledger_authority",
    "human_ledger_path",
    "dates_informational_only",
    "unknown_evidence_fails_closed",
}

SCOPES = {"component", "Core", "Agent", "Full", "global"}
REFRESH_MODES = {"manual-bootstrap", "scoped-refresh", "full-refresh"}
REFRESH_STATUSES = {"complete", "partial", "failed"}
ACCESS_STATUSES = {"verified", "unverified", "unavailable", "failed"}
EVIDENCE_STATUSES = {"accepted", "unverified", "unavailable", "failed", "not-applicable"}
PIN_STATUSES = {"pinned", "unpinned", "unverified", "unavailable", "failed", "not-applicable"}
DESCRIPTOR_STATUSES = {"observed", "missing", "unavailable", "failed", "not-applicable"}
SYNC_STATUSES = {"synchronized", "unverified", "debt", "unavailable", "failed", "not-applicable"}
FRESHNESS_STATUSES = {"fresh", "stale", "unknown", "failed"}
WATCHDOG_STATUSES = {"WATCHDOG-CURRENT", "WATCHDOG-STALE", "WATCHDOG-FAILED"}
DRIFT_SEVERITIES = {"INFO", "WARNING", "BLOCKING"}
DRIFT_STATUSES = {"open", "resolved"}

STATIC_REGISTRY_FIELDS_FORBIDDEN_IN_STATE = {
    "repository_full_name",
    "component_id",
    "canonical_responsibility",
    "lifecycle",
    "rollout_wave",
    "release_profiles",
    "distribution_ships",
    "component_release_descriptor_path",
    "owner_acceptance_kind",
    "system_refs",
    "surface_classification",
    "direct_compatibility_dependencies",
}


def _object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def _exact_keys(obj: dict[str, Any], expected: set[str], path: str, errors: list[str]) -> None:
    missing = expected - set(obj)
    unknown = set(obj) - expected
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"{path}: unknown keys: {', '.join(sorted(unknown))}")


def _sha_or_none(value: Any, path: str, errors: list[str]) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not SHA40.fullmatch(value):
        errors.append(f"{path}: expected lowercase 40-character Git SHA or null")
        return None
    return value


def _sha(value: Any, path: str, errors: list[str]) -> str | None:
    if not isinstance(value, str) or not SHA40.fullmatch(value):
        errors.append(f"{path}: expected lowercase 40-character Git SHA")
        return None
    return value


def _positive_int_list(value: Any, path: str, errors: list[str], *, allow_empty: bool = False) -> list[int]:
    if not isinstance(value, list):
        errors.append(f"{path}: expected array")
        return []
    if not allow_empty and not value:
        errors.append(f"{path}: expected non-empty array")
    if any(type(item) is not int or item <= 0 for item in value):
        errors.append(f"{path}: expected positive integer repository IDs")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{path}: duplicate repository IDs are not allowed")
    return value


def _evidence_refs(value: Any, path: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{path}: expected array")
        return []
    if any(not isinstance(item, str) or not item for item in value):
        errors.append(f"{path}: expected non-empty evidence reference strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{path}: duplicate evidence references are not allowed")
    return value


def _git_blob_sha(path: Path) -> str:
    content = path.read_bytes()
    payload = b"blob " + str(len(content)).encode("ascii") + b"\0" + content
    return hashlib.sha1(payload).hexdigest()


def _validate_refresh_record(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    record = _object(value, path, errors)
    if not record:
        return {}
    _exact_keys(record, REFRESH_RECORD_KEYS, path, errors)
    if record.get("scope") not in SCOPES:
        errors.append(f"{path}.scope: invalid scope")
    if record.get("status") not in REFRESH_STATUSES:
        errors.append(f"{path}.status: invalid refresh status")
    _sha(record.get("evidence_revision"), f"{path}.evidence_revision", errors)
    observed_at = record.get("observed_at")
    if observed_at is not None and not isinstance(observed_at, str):
        errors.append(f"{path}.observed_at: expected date-time string or null")
    return record


def _validate_evidence_state(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    item = _object(value, path, errors)
    if not item:
        return {}
    _exact_keys(item, EVIDENCE_STATE_KEYS, path, errors)
    status = item.get("status")
    if status not in EVIDENCE_STATUSES:
        errors.append(f"{path}.status: invalid evidence status")
    revision = _sha_or_none(item.get("revision"), f"{path}.revision", errors)
    refs = _evidence_refs(item.get("evidence_refs"), f"{path}.evidence_refs", errors)
    if status == "accepted" and (revision is None or not refs):
        errors.append(f"{path}: accepted evidence requires exact revision and evidence refs")
    if status in {"unavailable", "failed", "not-applicable"} and revision is not None:
        errors.append(f"{path}: {status} evidence must not claim a revision")
    if status == "not-applicable" and refs:
        errors.append(f"{path}: not-applicable evidence must not carry refs")
    return item


def _validate_distribution_pin(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    item = _object(value, path, errors)
    if not item:
        return {}
    _exact_keys(item, DISTRIBUTION_PIN_KEYS, path, errors)
    status = item.get("status")
    if status not in PIN_STATUSES:
        errors.append(f"{path}.status: invalid pin status")
    revision = _sha_or_none(item.get("revision"), f"{path}.revision", errors)
    release_id = item.get("release_id")
    if release_id is not None and (not isinstance(release_id, str) or not release_id):
        errors.append(f"{path}.release_id: expected non-empty string or null")
    refs = _evidence_refs(item.get("evidence_refs"), f"{path}.evidence_refs", errors)
    if status == "pinned" and (revision is None or not isinstance(release_id, str) or not release_id or not refs):
        errors.append(f"{path}: pinned state requires exact revision, release_id and evidence refs")
    if status in {"unpinned", "unavailable", "failed", "not-applicable"} and revision is not None:
        errors.append(f"{path}: {status} pin must not claim a revision")
    if status == "not-applicable" and (release_id is not None or refs):
        errors.append(f"{path}: not-applicable pin must not carry release/evidence")
    return item


def _validate_descriptor(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    item = _object(value, path, errors)
    if not item:
        return {}
    _exact_keys(item, DESCRIPTOR_KEYS, path, errors)
    status = item.get("status")
    if status not in DESCRIPTOR_STATUSES:
        errors.append(f"{path}.status: invalid descriptor status")
    revision = _sha_or_none(item.get("revision"), f"{path}.revision", errors)
    blob_sha = _sha_or_none(item.get("blob_sha"), f"{path}.blob_sha", errors)
    release_status = item.get("release_status")
    if release_status is not None and (not isinstance(release_status, str) or not release_status):
        errors.append(f"{path}.release_status: expected non-empty string or null")
    refs = _evidence_refs(item.get("evidence_refs"), f"{path}.evidence_refs", errors)
    if status == "observed" and (revision is None or blob_sha is None or not release_status or not refs):
        errors.append(f"{path}: observed descriptor requires revision, release status, blob SHA and evidence refs")
    if status in {"missing", "unavailable", "failed", "not-applicable"}:
        if revision is not None or blob_sha is not None or release_status is not None:
            errors.append(f"{path}: {status} descriptor must not claim observed descriptor fields")
    if status == "not-applicable" and refs:
        errors.append(f"{path}: not-applicable descriptor must not carry refs")
    return item


def _validate_system_sync(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    item = _object(value, path, errors)
    if not item:
        return {}
    _exact_keys(item, SYSTEM_SYNC_KEYS, path, errors)
    status = item.get("status")
    if status not in SYNC_STATUSES:
        errors.append(f"{path}.status: invalid system-sync status")
    checkpoint = _sha_or_none(item.get("checkpoint_revision"), f"{path}.checkpoint_revision", errors)
    refs = _evidence_refs(item.get("evidence_refs"), f"{path}.evidence_refs", errors)
    if status == "synchronized" and (checkpoint is None or not refs):
        errors.append(f"{path}: synchronized state requires checkpoint revision and evidence refs")
    if status in {"unavailable", "failed", "not-applicable"} and checkpoint is not None:
        errors.append(f"{path}: {status} system-sync state must not claim a checkpoint")
    if status == "not-applicable" and refs:
        errors.append(f"{path}: not-applicable system-sync state must not carry refs")
    return item


def validate_state(state: Any, registry: Any, *, registry_path: Path | None = None) -> list[str]:
    errors: list[str] = []
    root = _object(state, "$", errors)
    reg = _object(registry, "registry", errors)
    if not root or not reg:
        return errors

    _exact_keys(root, TOP_LEVEL_KEYS, "$", errors)
    if root.get("schema_version") != STATE_VERSION:
        errors.append(f"$.schema_version: expected {STATE_VERSION!r}")
    if root.get("state_id") != STATE_ID:
        errors.append(f"$.state_id: expected {STATE_ID!r}")
    if reg.get("schema_version") != REGISTRY_VERSION:
        errors.append(f"registry.schema_version: expected {REGISTRY_VERSION!r}")

    registry_entries = reg.get("repositories")
    if not isinstance(registry_entries, list) or not registry_entries:
        errors.append("registry.repositories: expected non-empty array")
        return errors
    registry_by_id: dict[int, dict[str, Any]] = {}
    for index, entry in enumerate(registry_entries):
        if not isinstance(entry, dict):
            errors.append(f"registry.repositories[{index}]: expected object")
            continue
        repo_id = entry.get("repository_id")
        if type(repo_id) is not int or repo_id <= 0:
            errors.append(f"registry.repositories[{index}].repository_id: invalid")
            continue
        registry_by_id[repo_id] = entry

    binding = _object(root.get("registry_binding"), "$.registry_binding", errors)
    if binding:
        _exact_keys(binding, REGISTRY_BINDING_KEYS, "$.registry_binding", errors)
        if binding.get("path") != "governance/repository-registry.json":
            errors.append("$.registry_binding.path: must point to canonical Registry")
        if binding.get("schema_version") != REGISTRY_VERSION:
            errors.append("$.registry_binding.schema_version: registry version mismatch")
        bound_blob = _sha(binding.get("blob_sha"), "$.registry_binding.blob_sha", errors)
        if registry_path is not None and bound_blob is not None:
            actual_blob = _git_blob_sha(registry_path)
            if bound_blob != actual_blob:
                errors.append("$.registry_binding.blob_sha: does not match Registry content")

    refresh = _object(root.get("refresh"), "$.refresh", errors)
    refresh_ids: list[int] = []
    refresh_revision = None
    if refresh:
        _exact_keys(refresh, REFRESH_KEYS, "$.refresh", errors)
        if refresh.get("mode") not in REFRESH_MODES:
            errors.append("$.refresh.mode: invalid mode")
        scope = refresh.get("scope")
        if scope not in SCOPES:
            errors.append("$.refresh.scope: invalid scope")
        if refresh.get("status") not in REFRESH_STATUSES:
            errors.append("$.refresh.status: invalid status")
        refresh_ids = _positive_int_list(refresh.get("repository_ids"), "$.refresh.repository_ids", errors)
        unknown = set(refresh_ids) - set(registry_by_id)
        if unknown:
            errors.append(f"$.refresh.repository_ids: unregistered IDs: {', '.join(map(str, sorted(unknown)))}")
        refresh_revision = _sha(refresh.get("evidence_revision"), "$.refresh.evidence_revision", errors)
        last_scoped = _validate_refresh_record(refresh.get("last_scoped_refresh"), "$.refresh.last_scoped_refresh", errors)
        if last_scoped:
            if last_scoped.get("scope") != scope:
                errors.append("$.refresh.last_scoped_refresh.scope: must equal current refresh scope")
            if last_scoped.get("evidence_revision") != refresh.get("evidence_revision"):
                errors.append("$.refresh.last_scoped_refresh.evidence_revision: must equal current refresh evidence revision")
        last_full = refresh.get("last_full_refresh")
        if last_full is not None:
            full = _validate_refresh_record(last_full, "$.refresh.last_full_refresh", errors)
            if full and full.get("scope") not in {"Full", "global"}:
                errors.append("$.refresh.last_full_refresh.scope: must be Full or global")
        if refresh.get("mode") == "full-refresh" and last_full is None:
            errors.append("$.refresh: full-refresh requires last_full_refresh")

        if refresh.get("status") == "complete" and scope in {"Core", "Agent", "Full"}:
            expected = {
                repo_id
                for repo_id, entry in registry_by_id.items()
                if entry.get("surface_classification") in {"governance", "release-orchestrator"}
                or scope in (entry.get("release_profiles") or [])
            }
            if set(refresh_ids) != expected:
                errors.append(f"$.refresh.repository_ids: complete {scope} refresh must contain exactly registered control-plane plus {scope} participants")

    watchdog = _object(root.get("watchdog"), "$.watchdog", errors)
    watchdog_status = None
    if watchdog:
        _exact_keys(watchdog, WATCHDOG_KEYS, "$.watchdog", errors)
        watchdog_status = watchdog.get("status")
        if watchdog_status not in WATCHDOG_STATUSES:
            errors.append("$.watchdog.status: invalid watchdog status")
        heartbeat = _sha_or_none(watchdog.get("heartbeat_revision"), "$.watchdog.heartbeat_revision", errors)
        successful = watchdog.get("last_successful_full_scan")
        full_scan = None
        if successful is not None:
            full_scan = _validate_refresh_record(successful, "$.watchdog.last_successful_full_scan", errors)
            if full_scan and full_scan.get("scope") not in {"Full", "global"}:
                errors.append("$.watchdog.last_successful_full_scan.scope: must be Full or global")
            if full_scan and full_scan.get("status") != "complete":
                errors.append("$.watchdog.last_successful_full_scan.status: must be complete")
        if watchdog_status == "WATCHDOG-CURRENT" and (heartbeat is None or full_scan is None):
            errors.append("$.watchdog: WATCHDOG-CURRENT requires heartbeat and successful full scan")
        reason = watchdog.get("reason")
        if not isinstance(reason, str) or not reason:
            errors.append("$.watchdog.reason: expected non-empty reason")

    repositories = root.get("repositories")
    if not isinstance(repositories, list) or not repositories:
        errors.append("$.repositories: expected non-empty array")
        repositories = []
    seen_ids: set[int] = set()
    for index, value in enumerate(repositories):
        path = f"$.repositories[{index}]"
        item = _object(value, path, errors)
        if not item:
            continue
        forbidden = set(item) & STATIC_REGISTRY_FIELDS_FORBIDDEN_IN_STATE
        if forbidden:
            errors.append(f"{path}: static Registry fields are forbidden in State: {', '.join(sorted(forbidden))}")
        _exact_keys(item, REPOSITORY_KEYS, path, errors)
        repo_id = item.get("repository_id")
        if type(repo_id) is not int or repo_id <= 0:
            errors.append(f"{path}.repository_id: expected positive integer")
            continue
        if repo_id in seen_ids:
            errors.append(f"{path}.repository_id: duplicate State repository ID")
        seen_ids.add(repo_id)
        registry_entry = registry_by_id.get(repo_id)
        if registry_entry is None:
            errors.append(f"{path}.repository_id: unregistered repository")
            continue

        access = item.get("access")
        if access not in ACCESS_STATUSES:
            errors.append(f"{path}.access: invalid access status")
        observed = _sha_or_none(item.get("observed_head"), f"{path}.observed_head", errors)
        if access == "verified" and observed is None:
            errors.append(f"{path}: verified access requires observed_head")
        if access in {"unavailable", "failed"} and observed is not None:
            errors.append(f"{path}: {access} access must not claim observed_head")

        acceptance = _validate_evidence_state(item.get("owner_acceptance"), f"{path}.owner_acceptance", errors)
        pin = _validate_distribution_pin(item.get("distribution_pin"), f"{path}.distribution_pin", errors)
        descriptor = _validate_descriptor(item.get("descriptor"), f"{path}.descriptor", errors)
        _validate_system_sync(item.get("system_sync"), f"{path}.system_sync", errors)

        freshness = _object(item.get("freshness"), f"{path}.freshness", errors)
        if freshness:
            _exact_keys(freshness, FRESHNESS_KEYS, f"{path}.freshness", errors)
            if freshness.get("scope") not in SCOPES:
                errors.append(f"{path}.freshness.scope: invalid scope")
            freshness_status = freshness.get("status")
            if freshness_status not in FRESHNESS_STATUSES:
                errors.append(f"{path}.freshness.status: invalid status")
            freshness_revision = _sha(freshness.get("evidence_revision"), f"{path}.freshness.evidence_revision", errors)
            if freshness_status == "fresh" and access != "verified":
                errors.append(f"{path}: freshness cannot be fresh without verified access")
            if repo_id in refresh_ids and refresh and refresh.get("status") == "complete":
                if freshness_status != "fresh":
                    errors.append(f"{path}: repository in complete current refresh must be fresh")
                if refresh_revision is not None and freshness_revision != refresh_revision:
                    errors.append(f"{path}.freshness.evidence_revision: must equal current refresh evidence revision")

        shipped = registry_entry.get("distribution_ships") is True
        runtime = registry_entry.get("surface_classification") == "runtime-component"
        if shipped and pin.get("status") == "not-applicable":
            errors.append(f"{path}.distribution_pin: Distribution-shipped repository cannot be not-applicable")
        if not shipped and pin.get("status") != "not-applicable":
            errors.append(f"{path}.distribution_pin: non-shipped repository must be not-applicable")
        if runtime and descriptor.get("status") == "not-applicable":
            errors.append(f"{path}.descriptor: runtime component descriptor cannot be not-applicable")
        if not runtime and descriptor.get("status") != "not-applicable":
            errors.append(f"{path}.descriptor: control-plane repository descriptor must be not-applicable")
        if runtime and acceptance.get("status") == "not-applicable":
            errors.append(f"{path}.owner_acceptance: runtime component acceptance cannot be not-applicable")

    registered_ids = set(registry_by_id)
    if seen_ids != registered_ids:
        missing = registered_ids - seen_ids
        extra = seen_ids - registered_ids
        if missing:
            errors.append(f"$.repositories: missing registered repository IDs: {', '.join(map(str, sorted(missing)))}")
        if extra:
            errors.append(f"$.repositories: contains unregistered repository IDs: {', '.join(map(str, sorted(extra)))}")

    drift = root.get("drift")
    if not isinstance(drift, list):
        errors.append("$.drift: expected array")
        drift = []
    seen_drift_ids: set[str] = set()
    for index, value in enumerate(drift):
        path = f"$.drift[{index}]"
        item = _object(value, path, errors)
        if not item:
            continue
        _exact_keys(item, DRIFT_KEYS, path, errors)
        drift_id = item.get("id")
        if not isinstance(drift_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,119}", drift_id):
            errors.append(f"{path}.id: invalid drift id")
        elif drift_id in seen_drift_ids:
            errors.append(f"{path}.id: duplicate drift id")
        else:
            seen_drift_ids.add(drift_id)
        if item.get("marker") != "CANONICAL-DRIFT-DETECTED":
            errors.append(f"{path}.marker: expected CANONICAL-DRIFT-DETECTED")
        if item.get("status") not in DRIFT_STATUSES:
            errors.append(f"{path}.status: invalid drift status")
        if item.get("severity") not in DRIFT_SEVERITIES:
            errors.append(f"{path}.severity: invalid drift severity")
        if item.get("scope") not in SCOPES:
            errors.append(f"{path}.scope: invalid drift scope")
        ids = _positive_int_list(item.get("repository_ids"), f"{path}.repository_ids", errors)
        unknown = set(ids) - registered_ids
        if unknown:
            errors.append(f"{path}.repository_ids: unregistered IDs: {', '.join(map(str, sorted(unknown)))}")
        for text_key in ("reason", "required_action"):
            if not isinstance(item.get(text_key), str) or not item.get(text_key):
                errors.append(f"{path}.{text_key}: expected non-empty string")
        _evidence_refs(item.get("evidence_refs"), f"{path}.evidence_refs", errors)

    if watchdog_status in {"WATCHDOG-STALE", "WATCHDOG-FAILED"}:
        watchdog_drift = [
            item
            for item in drift
            if isinstance(item, dict)
            and item.get("status") == "open"
            and item.get("scope") == "global"
            and item.get("severity") in {"WARNING", "BLOCKING"}
            and isinstance(item.get("id"), str)
            and item.get("id").startswith("repository-watchdog-")
        ]
        if not watchdog_drift:
            errors.append("$.watchdog: stale/failed watchdog requires open global WARNING/BLOCKING drift")

    semantics = _object(root.get("semantics"), "$.semantics", errors)
    if semantics:
        _exact_keys(semantics, SEMANTICS_KEYS, "$.semantics", errors)
        expected = {
            "dynamic_state_only": True,
            "registry_static_truth_authority": "governance/repository-registry.json",
            "human_ledger_authority": False,
            "human_ledger_path": "docs/REPOSITORY-STATE-LEDGER.md",
            "dates_informational_only": True,
            "unknown_evidence_fails_closed": True,
        }
        for key, value in expected.items():
            if semantics.get(key) != value:
                errors.append(f"$.semantics.{key}: expected {value!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "state",
        nargs="?",
        type=Path,
        default=Path("governance/repository-state.json"),
        help="Repository State JSON (default: governance/repository-state.json)",
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("governance/repository-registry.json"),
        help="Canonical Registry JSON (default: governance/repository-registry.json)",
    )
    args = parser.parse_args()

    try:
        state = json.loads(args.state.read_text(encoding="utf-8"))
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate_state(state, registry, registry_path=args.registry)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VALID {state['state_id']} repositories={len(state['repositories'])} drift={len(state['drift'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
