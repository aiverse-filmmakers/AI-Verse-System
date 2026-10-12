#!/usr/bin/env python3
"""Run the AI-Verse repository drift watchdog using the canonical refresh engine.

This file is orchestration only. Repository discovery, exact-ref observation,
Distribution pin discovery and ledger projection remain owned by
refresh_repository_state.py. The watchdog adds heartbeat transitions around a
Registry-derived global refresh and never writes sibling repositories.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import refresh_repository_state as state_refresh

DEFAULT_REGISTRY = Path("governance/repository-registry.json")
DEFAULT_STATE = Path("governance/repository-state.json")
DEFAULT_LEDGER = Path("docs/REPOSITORY-STATE-LEDGER.md")
SYSTEM_COMPONENT_ID = "ai-verse-system"
WATCHDOG_DRIFT_PREFIX = "repository-watchdog-"


def _parse_time(value: str) -> datetime:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        raise ValueError("watchdog observed time must include a timezone")
    return parsed.astimezone(timezone.utc)


def _format_time(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _system_repository_id(registry: dict[str, Any]) -> int:
    for item in registry["repositories"]:
        if item.get("component_id") == SYSTEM_COMPONENT_ID:
            return item["repository_id"]
    raise ValueError("Registry has no ai-verse-system entry")


def collect_watchdog_failures(state: dict[str, Any]) -> list[dict[str, Any]]:
    """Return deterministic evidence failures from one full refresh result."""

    failures: list[dict[str, Any]] = []
    for item in state["repositories"]:
        repo_id = item["repository_id"]
        access = item.get("access")
        if access in {"unavailable", "failed"}:
            failures.append({"repository_id": repo_id, "surface": "repository", "kind": access})

        descriptor = item.get("descriptor") or {}
        descriptor_status = descriptor.get("status")
        if descriptor_status in {"missing", "unavailable", "failed"}:
            kind = "failed" if descriptor_status == "missing" else descriptor_status
            failures.append({"repository_id": repo_id, "surface": "descriptor", "kind": kind})

        pin = item.get("distribution_pin") or {}
        pin_status = pin.get("status")
        if pin_status in {"unavailable", "failed"}:
            failures.append({"repository_id": repo_id, "surface": "distribution-pin", "kind": pin_status})

    return sorted(failures, key=lambda item: (item["repository_id"], item["surface"], item["kind"]))


def _last_full_attempt_time(state: dict[str, Any]) -> datetime | None:
    record = (state.get("refresh") or {}).get("last_full_refresh")
    if not isinstance(record, dict):
        return None
    observed_at = record.get("observed_at")
    if not isinstance(observed_at, str) or not observed_at:
        return None
    try:
        return _parse_time(observed_at)
    except ValueError:
        return None


def missed_expected_scans(prior_state: dict[str, Any], observed_at: str) -> int:
    """Infer fully missed daily windows since the prior recorded full attempt.

    Exact Git refs remain lineage authority. Time is used only for the frozen
    operational heartbeat schedule. One normal daily interval is allowed;
    additional whole 24-hour intervals count as missed expected scans.
    """

    previous = _last_full_attempt_time(prior_state)
    if previous is None:
        return 0
    current = _parse_time(observed_at)
    if current <= previous:
        return 0
    whole_days = int((current - previous).total_seconds() // 86400)
    return max(0, whole_days - 1)


def _watchdog_evidence_ref(revision: str) -> str:
    return f"aiverse-filmmakers/AI-Verse-System@{revision}:scripts/run_repository_watchdog.py"


def _set_watchdog_drift(
    state: dict[str, Any],
    registry: dict[str, Any],
    *,
    watchdog_status: str,
    reason: str,
    evidence_revision: str,
) -> None:
    target_id = None
    if watchdog_status == "WATCHDOG-FAILED":
        target_id = "repository-watchdog-failed"
    elif watchdog_status == "WATCHDOG-STALE":
        target_id = "repository-watchdog-stale"

    for item in state["drift"]:
        if isinstance(item, dict) and str(item.get("id", "")).startswith(WATCHDOG_DRIFT_PREFIX):
            item["status"] = "resolved"

    if target_id is None:
        return

    target = next((item for item in state["drift"] if item.get("id") == target_id), None)
    if target is None:
        target = {
            "id": target_id,
            "marker": "CANONICAL-DRIFT-DETECTED",
            "status": "open",
            "severity": "WARNING",
            "scope": "global",
            "repository_ids": [_system_repository_id(registry)],
            "reason": reason,
            "evidence_refs": [_watchdog_evidence_ref(evidence_revision)],
            "required_action": "Run the same Registry-derived global watchdog refresh successfully. Do not auto-rewrite sibling repositories or treat silence as CLEAN.",
        }
        state["drift"].append(target)
    else:
        target.update(
            status="open",
            severity="WARNING",
            scope="global",
            repository_ids=[_system_repository_id(registry)],
            reason=reason,
            evidence_refs=[_watchdog_evidence_ref(evidence_revision)],
            required_action="Run the same Registry-derived global watchdog refresh successfully. Do not auto-rewrite sibling repositories or treat silence as CLEAN.",
        )


def apply_watchdog_transition(
    registry: dict[str, Any],
    prior_state: dict[str, Any],
    refreshed_state: dict[str, Any],
    *,
    observed_at: str,
) -> tuple[dict[str, Any], bool, list[dict[str, Any]]]:
    """Apply watchdog heartbeat semantics to one canonical global refresh."""

    _parse_time(observed_at)
    if refreshed_state["refresh"].get("scope") != "global":
        raise ValueError("watchdog transition requires a global refresh")

    result = copy.deepcopy(refreshed_state)
    record = result["refresh"]["last_scoped_refresh"]
    record["observed_at"] = observed_at
    result["refresh"]["last_full_refresh"] = copy.deepcopy(record)

    failures = collect_watchdog_failures(result)
    successful = result["refresh"].get("status") == "complete" and not failures
    evidence_revision = result["refresh"]["evidence_revision"]
    prior_watchdog = prior_state["watchdog"]

    if successful:
        result["watchdog"] = {
            "status": "WATCHDOG-CURRENT",
            "heartbeat_revision": evidence_revision,
            "last_successful_full_scan": copy.deepcopy(result["refresh"]["last_full_refresh"]),
            "reason": f"Successful Registry-derived global heartbeat at {observed_at}; all registered repositories were scanned with no access/fetch failure.",
        }
        _set_watchdog_drift(
            result,
            registry,
            watchdog_status="WATCHDOG-CURRENT",
            reason=result["watchdog"]["reason"],
            evidence_revision=evidence_revision,
        )
        return result, True, failures

    missed = missed_expected_scans(prior_state, observed_at)
    previous_status = prior_watchdog.get("status")
    stale = previous_status in {"WATCHDOG-STALE", "WATCHDOG-FAILED"} or missed >= 1
    status = "WATCHDOG-STALE" if stale else "WATCHDOG-FAILED"
    detail = ", ".join(
        f"{item['repository_id']}:{item['surface']}:{item['kind']}" for item in failures
    ) or f"refresh-status:{result['refresh'].get('status')}"
    reason = (
        f"Global watchdog attempt at {observed_at} did not produce a successful full heartbeat; "
        f"missed_expected_scans={missed}; failures={detail}."
    )
    result["watchdog"] = {
        "status": status,
        "heartbeat_revision": prior_watchdog.get("heartbeat_revision"),
        "last_successful_full_scan": copy.deepcopy(prior_watchdog.get("last_successful_full_scan")),
        "reason": reason,
    }
    _set_watchdog_drift(
        result,
        registry,
        watchdog_status=status,
        reason=reason,
        evidence_revision=evidence_revision,
    )
    return result, False, failures


def watchdog_is_current(state: dict[str, Any], *, now: str | None = None) -> tuple[bool, str]:
    """Evaluate persisted heartbeat freshness without changing State.

    A CURRENT heartbeat older than two expected daily windows is operationally
    stale even if no scheduled runner was available to write the transition.
    """

    watchdog = state.get("watchdog") or {}
    if watchdog.get("status") != "WATCHDOG-CURRENT":
        return False, f"watchdog status is {watchdog.get('status')}"
    success = watchdog.get("last_successful_full_scan")
    if not isinstance(success, dict) or not success.get("observed_at"):
        return False, "CURRENT watchdog has no timestamped successful full scan"
    heartbeat = watchdog.get("heartbeat_revision")
    if heartbeat != success.get("evidence_revision"):
        return False, "heartbeat revision does not match successful full scan"
    if now is not None:
        current = _parse_time(now)
        observed = _parse_time(success["observed_at"])
        if current < observed:
            return False, "watchdog check time precedes heartbeat"
        if (current - observed).total_seconds() >= 172800:
            return False, "successful full heartbeat is at least two expected daily windows old"
    return True, "watchdog heartbeat is current"


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--api-base", default=state_refresh.DEFAULT_API_BASE)
    parser.add_argument("--evidence-revision", help="Exact System revision; defaults to local Git HEAD")
    parser.add_argument("--observed-at", help="UTC/offset timestamp for this scheduled/manual attempt")
    parser.add_argument("--write", action="store_true", help="Write canonical State and generated ledger locally")
    parser.add_argument("--check-current", action="store_true", help="Check persisted watchdog status/freshness without network refresh")
    parser.add_argument("--now", help="Timestamp used by --check-current age evaluation")
    args = parser.parse_args()

    try:
        registry = _load(args.registry)
        state = _load(args.state)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"WATCHDOG INVALID INPUT: {exc}", file=sys.stderr)
        return 2

    if args.check_current:
        try:
            current, reason = watchdog_is_current(state, now=args.now)
        except ValueError as exc:
            print(f"WATCHDOG INVALID TIME: {exc}", file=sys.stderr)
            return 2
        print(f"WATCHDOG {'CURRENT' if current else 'NOT-CURRENT'}: {reason}")
        return 0 if current else 1

    observed_at = args.observed_at or _format_time(datetime.now(timezone.utc))
    try:
        observed_at = _format_time(_parse_time(observed_at))
        evidence_revision = args.evidence_revision or state_refresh._local_head()
        client = state_refresh.GitHubClient(api_base=args.api_base, token=os.environ.get("GITHUB_TOKEN"))
        refreshed = state_refresh.refresh_state(
            registry,
            state,
            client=client,
            scope="global",
            evidence_revision=evidence_revision,
            registry_blob_sha=state_refresh._git_blob_sha(args.registry),
        )
        result, successful, failures = apply_watchdog_transition(
            registry,
            state,
            refreshed,
            observed_at=observed_at,
        )
    except (ValueError, state_refresh.EvidenceFailed, state_refresh.EvidenceUnavailable) as exc:
        print(f"WATCHDOG REFRESH FAILED: {exc}", file=sys.stderr)
        return 1

    errors = state_refresh.validate_state(result, registry, registry_path=args.registry)
    if errors:
        print("WATCHDOG PRODUCED INVALID STATE", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    ledger = state_refresh.render_ledger(registry, result)
    if args.write:
        args.state.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        args.ledger.write_text(ledger, encoding="utf-8")

    print(
        f"WATCHDOG {result['watchdog']['status']} scope=global repos={len(result['refresh']['repository_ids'])} "
        f"evidence={result['refresh']['evidence_revision']} failures={len(failures)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
