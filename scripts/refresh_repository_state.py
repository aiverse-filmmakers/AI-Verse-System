#!/usr/bin/env python3
"""AI-Verse Repository State refresh and projection entrypoint.

Slice 2.3 establishes this frozen path as the single Repository State projection
implementation. It validates existing Registry/State machine truth and renders the
human ledger deterministically. Live scoped/full evidence refresh is intentionally
added by Slice 3.1 to this same file rather than through a second state engine.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_repository_state import validate_state

DEFAULT_REGISTRY = Path("governance/repository-registry.json")
DEFAULT_STATE = Path("governance/repository-state.json")
DEFAULT_LEDGER = Path("docs/REPOSITORY-STATE-LEDGER.md")


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _short(value: str | None) -> str:
    return value[:12] if value else "-"


def _escape(value: Any) -> str:
    if value is None:
        return "-"
    return str(value).replace("|", "\\|").replace("\n", " ")


def _status_revision(block: dict[str, Any], key: str = "revision") -> str:
    status = block.get("status", "unknown")
    revision = block.get(key)
    return f"{status} `{_short(revision)}`" if revision else status


def render_ledger(registry: dict[str, Any], state: dict[str, Any]) -> str:
    registry_by_id = {item["repository_id"]: item for item in registry["repositories"]}
    state_by_id = {item["repository_id"]: item for item in state["repositories"]}

    lines: list[str] = [
        "# AI-Verse Repository State Ledger",
        "",
        "> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.",
        "",
        "Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.",
        "",
        "## Snapshot",
        "",
        f"- State schema: `{state['schema_version']}`",
        f"- Registry binding blob: `{state['registry_binding']['blob_sha']}`",
        f"- Refresh mode: `{state['refresh']['mode']}`",
        f"- Refresh scope: `{state['refresh']['scope']}`",
        f"- Refresh status: `{state['refresh']['status']}`",
        f"- Refresh evidence revision: `{state['refresh']['evidence_revision']}`",
        f"- Last full refresh: `{state['refresh']['last_full_refresh']['evidence_revision']}`" if state["refresh"]["last_full_refresh"] else "- Last full refresh: `none`",
        f"- Watchdog: `{state['watchdog']['status']}`",
        f"- Watchdog reason: {_escape(state['watchdog']['reason'])}",
        "",
        "## Repository state",
        "",
        "| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for registry_entry in registry["repositories"]:
        repo_id = registry_entry["repository_id"]
        item = state_by_id[repo_id]
        pin = item["distribution_pin"]
        descriptor = item["descriptor"]
        pin_text = _status_revision(pin)
        if pin.get("release_id"):
            pin_text += f" / {_escape(pin['release_id'])}"
        descriptor_text = _status_revision(descriptor)
        if descriptor.get("release_status"):
            descriptor_text += f" / {_escape(descriptor['release_status'])}"
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape(registry_entry["repository_full_name"]),
                    _escape(registry_entry["component_id"]),
                    f"`{_short(item['observed_head'])}`" if item["observed_head"] else "-",
                    _escape(_status_revision(item["owner_acceptance"])),
                    _escape(pin_text),
                    _escape(descriptor_text),
                    _escape(_status_revision(item["system_sync"], "checkpoint_revision")),
                    _escape(f"{item['freshness']['status']} / {item['freshness']['scope']}"),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Open drift",
            "",
            "| Severity | Scope | Drift | Repositories | Reason | Required action |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    open_drift = [item for item in state["drift"] if item["status"] == "open"]
    severity_order = {"BLOCKING": 0, "WARNING": 1, "INFO": 2}
    open_drift.sort(key=lambda item: (severity_order[item["severity"]], item["scope"], item["id"]))
    for drift in open_drift:
        names = [registry_by_id[repo_id]["component_id"] for repo_id in drift["repository_ids"]]
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape(drift["severity"]),
                    _escape(drift["scope"]),
                    _escape(drift["id"]),
                    _escape(", ".join(names)),
                    _escape(drift["reason"]),
                    _escape(drift["required_action"]),
                ]
            )
            + " |"
        )

    if not open_drift:
        lines.append("| INFO | global | none | - | No open drift recorded. | Continue normal evidence refresh. |")

    lines.extend(
        [
            "",
            "## Authority and freshness rules",
            "",
            "- This ledger is a projection only and is never machine authority.",
            "- Static repository identity, ownership and lifecycle facts come only from the Registry.",
            "- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.",
            "- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.",
            "- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.",
            "- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write-ledger", action="store_true", help="Write deterministic ledger projection")
    action.add_argument("--check-ledger", action="store_true", help="Fail if committed ledger differs from projection")
    args = parser.parse_args()

    try:
        registry = _load(args.registry)
        state = _load(args.state)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate_state(state, registry, registry_path=args.registry)
    if errors:
        print("INVALID REPOSITORY STATE", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    rendered = render_ledger(registry, state)

    if args.write_ledger:
        args.ledger.parent.mkdir(parents=True, exist_ok=True)
        args.ledger.write_text(rendered, encoding="utf-8")
        print(f"WROTE {args.ledger}")
        return 0

    if args.check_ledger:
        try:
            committed = args.ledger.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"LEDGER MISSING: {exc}", file=sys.stderr)
            return 1
        if committed != rendered:
            print("LEDGER OUT OF DATE: regenerate with --write-ledger", file=sys.stderr)
            return 1
        print(f"LEDGER CURRENT {args.ledger}")
        return 0

    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
