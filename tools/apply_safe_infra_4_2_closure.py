from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one closure anchor, found {count}: {old[:80]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


ROADMAP = "docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md"
EVIDENCE = "docs/SAFE-INFRASTRUCTURE-SLICE-4.2-UPDATE-GATING.md"

# Canonical program counters/status.
replace_once(
    ROADMAP,
    "**Status:** IN PROGRESS - PHASE 4; SLICE 4.1 COMPLETE  \n",
    "**Status:** IN PROGRESS - PHASE 4; SLICE 4.2 COMPLETE  \n",
)
replace_once(ROADMAP, "**Completed:** 12  \n", "**Completed:** 13  \n")
replace_once(ROADMAP, "**Remaining:** 6  \n", "**Remaining:** 5  \n")
replace_once(ROADMAP, "**Overall progress:** 66.7%  \n", "**Overall progress:** 72.2%  \n")
replace_once(ROADMAP, "**Current phase progress:** 1/4  \n", "**Current phase progress:** 2/4  \n")
replace_once(ROADMAP, "**Slices until Phase 5:** 3  \n", "**Slices until Phase 5:** 2  \n")
replace_once(
    ROADMAP,
    "**Next:** Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements  \n",
    "**Next:** Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX  \n",
)
replace_once(
    ROADMAP,
    "**Next slice task list:** STOP - derive only when Slice 4.2 starts\n",
    "**Next slice task list:** STOP - derive only when Slice 4.3 starts\n",
)
replace_once(
    ROADMAP,
    "**Phase progress:** 1/4\n\n## Slice 4.1",
    "**Phase progress:** 2/4\n\n## Slice 4.1",
)

# Slice 4.2 canonical closure.
replace_once(
    ROADMAP,
    "## Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements\n\n**Status:** NOT STARTED  \n**Dependencies:** 4.1, 2.2  \n**Adaptive tasks:** derive from the current qualified Distribution update flow\n\nThe completed Core Update Program v1 updater is the base. Extend it; do not replace it.\n",
    "## Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements\n\n**Status:** COMPLETE  \n**Dependencies:** 4.1, 2.2  \n**Adaptive tasks:** 6/6 COMPLETE\n\nExtended the shipped Core Update Program v1 updater rather than replacing it. Distribution now reads exact target component release metadata before mutation, classifies structural compatibility as COMPATIBLE / OPTIONAL / REQUIRED / BLOCKED-REVIEW, preserves preview-only planning, and prevents incompatible target software from being falsely activated. No structural migration is executed by normal update.\n\n### Final adaptive task list\n\n- [x] **4.2-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.2, the infrastructure recipe contract, shipped updater/LKG flow and current owner descriptor state; inventory overlapping work before writes.\n- [x] **4.2-T2** Implement exact target component descriptor acquisition/validation plus deterministic read-only structural requirement classification, consuming only `ai-verse.infrastructure-upgrade/v1` owner metadata and failing closed on missing/ambiguous/unverifiable evidence.\n- [x] **4.2-T3** Extend Core `update_plan` with OPTIONAL / REQUIRED / BLOCKED-REVIEW activation truth while preserving no-op behavior, keeping preview read-only and exposing a concise member-facing recommendation without generation IDs, recipe IDs, repository paths or hashes.\n- [x] **4.2-T4** Extend mutating update staging/activation so OPTIONAL work is never silently applied, REQUIRED/BLOCKED structural state cannot be falsely activated, and a blocked apply stops before live software/receipt mutation or owner migration. Preserve the existing Slice 4.1 LKG and interruption model.\n- [x] **4.2-T5** Add focused positive and destructive-negative tests for no-infrastructure compatibility, OPTIONAL compatibility, REQUIRED activation block, BLOCKED/REVIEW ambiguity/unrecognized generation, stale/unverifiable evidence, read-only preview, plain-English output and interruption/source-receipt truth.\n- [x] **4.2-T6** Qualify the exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.2 and stop before Slice 4.3.\n",
)
replace_once(
    ROADMAP,
    "- member is never asked for release IDs, repository paths, migration recipe IDs or infrastructure generations.\n\n### NEXT\n\nSlice 4.3.\n",
    "- member is never asked for release IDs, repository paths, migration recipe IDs or infrastructure generations.\n\n### Exact evidence\n\n- detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-4.2-UPDATE-GATING.md`;\n- task-list / start record merged through System PR #200;\n- Distribution PR #31 qualified head: `51eb900ac2d692fce7f6e3ae705fdebca257c463`;\n- Distribution merged main: `9842451bca86f32e48763fbfe07243a613f15214`;\n- PR-head `Distribution CI` run `38320871651`: **SUCCESS**, six jobs;\n- exact merged-main `Distribution CI` run `38321170716`: **SUCCESS**, six jobs.\n\n### Validation discoveries\n\n- The admitted target OS snapshot has a historical stale top-level descriptor `revision` while publishing no `migration.infrastructure`. The gate therefore trusts the exact Git carrier snapshot to prove absence, but requires exact revision binding as soon as structural metadata is published. This preserves the already-qualified current Core update without weakening future recipe admission.\n- Existing preservation tests use `ReleaseSet.raw` for generated-file fixture metadata. Runtime structural descriptor probes are therefore limited to canonical catalog-shaped releases instead of treating any non-empty fixture metadata as an admitted runtime release.\n- Synthetic structural tests were corrected to use catalog-shaped release metadata so OPTIONAL / REQUIRED / BLOCKED-REVIEW assertions exercise the real runtime branch.\n\n### Acceptance criteria\n\n- `aiverse update` remains the one-action admitted software update: **PASS**;\n- `aiverse update --plan` remains read-only preview: **PASS**;\n- normal update does not perform OPTIONAL infrastructure rearrangement: **PASS**;\n- target software incompatible with current infrastructure is not falsely activated: **PASS**;\n- REQUIRED upgrade state is visible and actionable in plain English: **PASS**;\n- BLOCKED/REVIEW state cannot be misrepresented as safe automatic work: **PASS**;\n- update stages only when structural evidence permits it and activation truth remains explicit: **PASS**;\n- release/update transaction remains truthful after interruption, with known structural refusal occurring before LKG rotation or live mutation: **PASS**;\n- member-facing output does not require release IDs, repository paths, migration recipe IDs or infrastructure generations: **PASS**;\n- exact PR-head and exact merged-main six-platform Distribution CI are green: **PASS**.\n\n### Completion report\n\n```text\nCompleted: Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements\nTasks: 6/6\nOverall: 13/18 slices (72.2%)\nPhase: Phase 4 - Implement Distribution orchestration and simple member UX\nPhase progress: 2/4\nUntil Phase 5: 2 slices\nNext: Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX\nBlockers/drift/amendments: no Slice 4.2 blocker or protected-law amendment. Existing unrelated broad-gate issues remain separate.\n```\n\n### NEXT\n\n**STOP after Slice 4.2 under the current one-at-a-time execution request.**\n\nNext execution unit: Slice 4.3. Derive its adaptive task list only after fresh refs are fetched. No Safe Infrastructure Slice 4.3 implementation was started here.\n",
)

# Detailed evidence file status and task closure.
replace_once(EVIDENCE, "**Status:** IN PROGRESS  \n", "**Status:** COMPLETE  \n")
for task_id in ("4.2-T1", "4.2-T2", "4.2-T3", "4.2-T4", "4.2-T5", "4.2-T6"):
    replace_once(EVIDENCE, f"- [ ] **{task_id}**", f"- [x] **{task_id}**")

evidence_path = Path(EVIDENCE)
evidence_text = evidence_path.read_text(encoding="utf-8")
if "## Final implementation evidence" not in evidence_text:
    evidence_text += '''\n## Final implementation evidence\n\n- Distribution PR #31 qualified head: `51eb900ac2d692fce7f6e3ae705fdebca257c463`.\n- PR-head `Distribution CI` run `38320871651`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.\n- Distribution PR #31 merged as `9842451bca86f32e48763fbfe07243a613f15214`.\n- Exact merged-main `Distribution CI` run `38321170716`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.\n- Product diff at merge was limited to `core_update.py`, `infrastructure_gate.py`, `recovery_orchestrator.py`, `update_output.py`, and `test_infrastructure_update_gate.py`; all temporary patch/workflow helpers were removed before qualification.\n\n## Final behavior\n\n`aiverse update --plan` now includes structural activation truth without mutating the installation. Exact target component snapshots that publish no infrastructure contract remain compatible. When an owner does publish `ai-verse.infrastructure-upgrade/v1`, Distribution requires exact target binding and deterministic owner evidence, resolves only a unique admitted path, and fails closed on ambiguity, stale/unverifiable evidence, unknown generation or a detector that cannot prove read-only behavior.\n\nOPTIONAL structural work never runs inside normal update. REQUIRED work blocks activation but may be represented as evidence-backed staging-compatible state. BLOCKED/REVIEW refuses unsafe staging/activation. The installed mutating path rechecks activation before entering the update transaction, and the Slice 4.1 recovery wrapper rejects known REQUIRED/BLOCKED updates before LKG rotation. No owner migration logic or `aiverse upgrade` apply surface was invented in Slice 4.2.\n\n## Validation discoveries\n\n1. The currently admitted OS target commit `64f7325444d18f94c9d4755d32eb89f3468bda6b` contains a historical component descriptor whose top-level `revision` names an older commit while publishing no infrastructure block. Requiring that stale field even for absence would have broken an already-qualified update. The final rule trusts the exact Git snapshot to prove absence, but requires exact descriptor/recipe target binding once infrastructure metadata is present.\n2. Existing preservation tests use `ReleaseSet.raw` for generated-file fixture metadata. Treating any non-empty `raw` as a real catalog release caused fake revisions to be network-probed. The final gate recognizes canonical catalog-shaped runtime releases explicitly.\n3. After that correction, the new structural tests themselves had to be upgraded from `raw={"fixture": true}` to catalog-shaped synthetic releases so they continued to exercise the production branch.\n\nThese were caught before merge. They do not weaken the protected laws and required no protected-law amendment.\n\n## Acceptance results\n\n- shipped `aiverse update` semantics preserved: **PASS**;\n- `aiverse update --plan` preview remains read-only: **PASS**;\n- OPTIONAL rearrangement never silently applied by update: **PASS**;\n- REQUIRED incompatibility cannot be falsely activated: **PASS**;\n- BLOCKED/REVIEW ambiguity and unverifiable evidence fail closed: **PASS**;\n- evidence-backed staging/activation truth is explicit: **PASS**;\n- known structural refusal happens before LKG rotation/live mutation: **PASS**;\n- existing interruption/journal model remains authoritative after mutation admission: **PASS**;\n- default member output hides generations, recipe IDs, repository paths and hashes: **PASS**;\n- exact PR-head and exact merged-main six-job Distribution CI: **PASS**.\n\n## Closure\n\nSlice 4.2 is complete at **13/18 slices = 72.2%**. Phase 4 is **2/4 complete** with **2 slices until Phase 5**. The next Safe Infrastructure execution unit is **Slice 4.3**, and it has not been implemented by this slice.\n'''
    evidence_path.write_text(evidence_text, encoding="utf-8")
