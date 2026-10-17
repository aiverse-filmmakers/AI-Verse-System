from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

BASE_SYSTEM = "ec6d09817edfc343a0f8d61006d4e3a3bd8329f6"
DIST_HEAD = "5f2ce4bfe9902c3944ec2d467d7766516dede077"
DIST_CI = "39051973345"
DIST_CANDIDATES_BLOB = "c1352da686207d404536a34464b7a03438c5d81a"
DIST_PROMOTIONS_BLOB = "8646ead86a03c31ce369f510fea2e0ac8cb227c5"
CURRENT_RELEASE = "core-first-run-rc1-2026-10-12"
STATE_PATH = Path("governance/repository-state.json")
ROADMAP_PATH = Path("docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md")


def fail(message: str) -> None:
    raise SystemExit(message)


def once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        fail(f"{label}: expected 1 match, found {count}")
    return text.replace(old, new, 1)


def verify_main_anchor() -> None:
    subprocess.run(["git", "fetch", "origin", "main"], check=True)
    observed = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
    if observed != BASE_SYSTEM:
        fail(f"canonical System main moved: expected {BASE_SYSTEM}, got {observed}")


def prepare() -> None:
    verify_main_anchor()
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    matches = [item for item in state.get("drift", []) if item.get("id") == "compact-release-receipt-not-yet-implemented"]
    if len(matches) != 1:
        fail(f"receipt drift: expected exactly one record, found {len(matches)}")
    drift = matches[0]
    if drift.get("status") != "open" or drift.get("severity") != "INFO" or drift.get("scope") != "Core":
        fail("receipt drift is not in the expected open INFO/Core state")
    if drift.get("repository_ids") != [1350081263]:
        fail("receipt drift repository scope changed")

    drift["status"] = "resolved"
    drift["reason"] = (
        "Future Core final admission now constructs and validates the compact immutable release receipt, "
        "publishes it before promotion/channel mutation, binds exact reconstruction evidence without duplicate authority, "
        "and is protected by permanent destructive-negative reconstruction regressions."
    )
    drift["evidence_refs"] = [
        f"aiverse-filmmakers/ai-verse-distribution@{DIST_HEAD}:src/aiverse_distribution/core_promotion.py",
        f"aiverse-filmmakers/ai-verse-distribution@{DIST_HEAD}:src/aiverse_distribution/release_receipt.py",
        f"aiverse-filmmakers/ai-verse-distribution@{DIST_HEAD}:tests/test_release_receipt_admission.py",
        f"aiverse-filmmakers/ai-verse-distribution@{DIST_HEAD}:tests/test_release_receipt_reconstruction_regressions.py",
    ]
    drift["required_action"] = (
        "No corrective action remains for this drift. Keep every future Core final admission receipt-gated, immutable, "
        "non-cyclic, reconstruction-bound and separate from member lifecycle/user-state recovery authority."
    )
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def finalize() -> None:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    refresh = state.get("refresh", {})
    if refresh.get("mode") != "scoped-refresh" or refresh.get("scope") != "Core" or refresh.get("status") != "complete":
        fail(f"closing State refresh is not complete Core scoped refresh: {refresh}")
    if refresh.get("evidence_revision") != BASE_SYSTEM:
        fail("closing State refresh is not bound to the expected canonical System evidence revision")

    repos = {item.get("repository_id"): item for item in state.get("repositories", []) if isinstance(item, dict)}
    distribution = repos.get(1350081263)
    if not isinstance(distribution, dict) or distribution.get("access") != "verified" or distribution.get("observed_head") != DIST_HEAD:
        fail("closing State did not observe the exact validated Distribution head")

    core_repo_ids = [1361862361, 1362233598, 1361910454, 1362243580, 1364457521]
    for repo_id in core_repo_ids:
        entry = repos.get(repo_id)
        pin = entry.get("distribution_pin") if isinstance(entry, dict) else None
        if not isinstance(pin, dict) or pin.get("status") != "pinned" or pin.get("release_id") != CURRENT_RELEASE:
            fail(f"Core repository {repo_id} no longer pins {CURRENT_RELEASE}")

    receipt_drift = [item for item in state.get("drift", []) if item.get("id") == "compact-release-receipt-not-yet-implemented"]
    if len(receipt_drift) != 1 or receipt_drift[0].get("status") != "resolved":
        fail("compact receipt drift was not resolved")
    if [item for item in state.get("drift", []) if item.get("status") == "open"]:
        fail("unexpected open canonical drift remains after Slice 5.4 closure")

    workflow_run = os.environ.get("SYSTEM_CLOSURE_RUN_ID", "unknown")
    text = ROADMAP_PATH.read_text(encoding="utf-8")

    replacements = [
        ("**Completed:** 16  ", "**Completed:** 17  ", "header completed"),
        ("**Remaining:** 4  ", "**Remaining:** 3  ", "header remaining"),
        ("**Overall progress:** 80.0%  ", "**Overall progress:** 85.0%  ", "header progress"),
        ("**Current execution phase:** Phase 5 - Enforce safe composition and delivery in Distribution  ", "**Current execution phase:** Phase 6 - Prove the network and close  ", "header phase"),
        ("**Current phase progress:** 3/4 slices complete  ", "**Current phase progress:** 0/3 slices complete  ", "header phase progress"),
        ("**Slices until next phase:** 1  ", "**Slices until program completion:** 3  ", "header remaining phases"),
        ("**Current slice:** 5.4 - Durable release receipts  ", "**Current slice:** 6.1 - Cross-repo regression/evidence validation  ", "header current slice"),
        ("**Current slice status:** IN PROGRESS  ", "**Current slice status:** NOT STARTED  ", "header current status"),
        ("**Next slice:** 6.1 - Cross-repo regression/evidence validation", "**Next slice:** 6.2 - End-to-end qualification", "header next slice"),
    ]
    for old, new, label in replacements:
        text = once(text, old, new, label)

    phase5 = "# Phase 5 - Enforce safe composition and delivery in Distribution\n\n**Phase size:** 4 slices"
    phase5_done = phase5 + "  \n**Status:** COMPLETE, 4/4"
    text = once(text, phase5, phase5_done, "Phase 5 closure")

    start = text.index("## Slice 5.4 - Durable release receipts")
    end = text.index("\n# Phase 6 - Prove the network and close", start)
    section = text[start:end]
    section = once(section, "**Status:** IN PROGRESS", "**Status:** COMPLETE", "Slice 5.4 status")
    section = once(section, "**Adaptive tasks:** 3/4 complete", "**Adaptive tasks:** 4/4 complete", "Slice 5.4 count")

    t4 = "- [ ] **5.4-T4** Run clean Distribution and required System cross-validation for the adopted durable-receipt path, confirm final release/debt/drift state, resolve `compact-release-receipt-not-yet-implemented` only if exact evidence proves the future-admission requirement is enforced, publish required closing Core State/ledger, close Slice 5.4 and Phase 5, advance to Slice 6.1, and stop without beginning Phase 6 execution."
    t4_done = t4.replace("- [ ]", "- [x]", 1)
    section = once(section, t4, t4_done, "T4 checkbox")

    evidence = t4_done + f'''\n\n### T4 closure evidence\n\n- Fresh marker-free Distribution validation used exact head `{DIST_HEAD}`, whose tree is identical to accepted T3 merge `f407302df93fee18ae407d59cf0409227436ddfe`. Distribution CI `{DIST_CI}` passed all six Linux/macOS/Windows Python 3.11/3.12 jobs. No product/runtime/release/catalog bytes changed during the validation trigger.\n- Exact final live catalogs remain unchanged: candidate overlay is empty (blob `{DIST_CANDIDATES_BLOB}`), `current_release` remains `{CURRENT_RELEASE}`, and `system_sync_debts` remains empty (promotion catalog blob `{DIST_PROMOTIONS_BLOB}`). No live promotion and no retroactive receipt instance occurred.\n- Exact implementation evidence proves the future-admission requirement: `core_promotion.py` constructs and validates the v1 receipt, immutably publishes it before release/promotion/channel writes, refuses overwrite, and the final release-set carries the non-cyclic receipt reference. `release_receipt.py`, admission regressions and permanent reconstruction regressions bind the exact release/evidence/owner/Registry/State/lock/compatibility/preservation/promotion/debt facts while excluding member/user-state authority.\n- The canonical `compact-release-receipt-not-yet-implemented` `INFO/Core` drift is resolved, with exact evidence refs at Distribution `{DIST_HEAD}`. The closing Registry-derived Core scoped refresh is complete and records Distribution `{DIST_HEAD}` while preserving the five current Core component pins at `{CURRENT_RELEASE}`. The generated ledger is regenerated from that State and has no open drift.\n- System closure workflow run `{workflow_run}` validated Registry, closing State, deterministic ledger and the complete System contract test suite before publishing. Historical U36 evidence remains untouched; member lifecycle/user-owned state remains untouched. No plan amendment was required.\n'''
    section = once(section, t4_done, evidence, "T4 evidence insertion")

    old_summary = "Slice 5.4 planning and 5.4-T1 through 5.4-T3 are complete. 5.4-T4 has not begun. Future Core final admission is durable-receipt-gated, cross-platform deterministic and protected by permanent exact-reconstruction/destructive-negative regressions; no live release was promoted and canonical State/ledger remain intentionally unchanged until closure. No plan amendment was required."
    new_summary = "Slice 5.4 is COMPLETE, 4/4. Future Core final admission is durable-receipt-gated, immutable, non-cyclic, cross-platform deterministic and protected by permanent exact-reconstruction/destructive-negative regressions. The compact-receipt drift is resolved in closing Core State/ledger; live release/candidate/debt state is unchanged and no live promotion occurred. Phase 5 is COMPLETE, 4/4. Phase 6 has not begun. No plan amendment was required."
    section = once(section, old_summary, new_summary, "Slice 5.4 closure summary")
    text = text[:start] + section + text[end:]

    pointer_start = text.index("# Current execution pointer")
    new_pointer = f'''# Current execution pointer\n\n**Completed:** 17/20  \n**Overall:** 85.0%  \n**Phase:** Phase 6 - Prove the network and close  \n**Phase progress:** 0/3  \n**Until program completion:** 3 slices  \n**Current slice:** Slice 6.1 - Cross-repo regression/evidence validation (`NOT STARTED`; slice-start planning has not begun)\n**Next:** Slice 6.1 start - perform only bounded discovery/planning for the cross-repo regression/evidence-validation slice, classify `REUSE | EXTEND | CREATE | RETIRE | BLOCK/UNKNOWN`, record the smallest evidence-backed adaptive task list and first execution task, then stop without implementing or pre-validating that task\n**Blockers/drift/amendments:** Slice 5.4 and Phase 5 are complete. Fresh clean Distribution CI `{DIST_CI}` passed on marker-free head `{DIST_HEAD}` with the exact accepted T3 tree. Final live Core release remains `{CURRENT_RELEASE}`, candidate overlay remains empty, and `system_sync_debts` remains empty. Closing Core State/ledger resolve `compact-release-receipt-not-yet-implemented` only after exact receipt-gated final-admission and reconstruction-regression evidence; no open canonical drift remains in the closing scoped Core snapshot. No live promotion, historical U36 rewrite, member lifecycle mutation or user-owned-state mutation occurred. No plan amendment required. Slice 6.1 planning has not begun.\n'''
    text = text[:pointer_start] + new_pointer
    ROADMAP_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "finalize"}:
        fail("usage: slice-54-t4-close.py prepare|finalize")
    if sys.argv[1] == "prepare":
        prepare()
    else:
        finalize()
