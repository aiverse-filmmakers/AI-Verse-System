# Safe Infrastructure Slice 4.2 - Update staging and activation gating

**Status:** COMPLETE  
**Canonical slice:** `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`, Slice 4.2  
**Recorded before product implementation:** yes

## Starting refs

- `aiverse-filmmakers/AI-Verse-System@d7043c1a6541374e97acf192eee8a39158006741`
- `aiverse-filmmakers/ai-verse-distribution@2fec4675287be748ae222efa61330bdaee37b0bc`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

System advanced after the Slice 4.1 closure through unrelated repository-network Registry work. Slice 4.2 starts from the refreshed System head above and must not overwrite that work.

## Evidence classification

- **REUSE:** completed Core Update Program v1 `aiverse update` and `aiverse update --plan` flow.
- **REUSE:** Slice 4.1 lifecycle lock, update journal/recovery behavior and reusable LKG guard.
- **EXTEND:** update planning with structural requirement awareness from exact target component release descriptors.
- **EXTEND:** activation gating so incompatible target software cannot be committed as active.
- **CREATE:** the smallest Distribution-owned read-only structural requirement planner needed by update gating. It consumes owner metadata/operations and does not become a second migration registry.
- **DEFER:** structural `aiverse upgrade` aggregation/apply remains Slice 4.3/4.4.
- **NO OWNER CHANGE EXPECTED:** the current admitted Core release does not publish `migration.infrastructure`; Phase 3 deliberately deferred descriptor publication until a future exact admitted owner revision.

## Adaptive task list

- [x] **4.2-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.2, the infrastructure recipe contract, shipped updater/LKG flow and current owner descriptor state; inventory overlapping work before writes.
- [x] **4.2-T2** Implement exact target component descriptor acquisition/validation plus deterministic read-only structural requirement classification, consuming only `ai-verse.infrastructure-upgrade/v1` owner metadata and failing closed on missing/ambiguous/unverifiable evidence.
- [x] **4.2-T3** Extend Core `update_plan` with OPTIONAL / REQUIRED / BLOCKED-REVIEW activation truth while preserving no-op behavior, keeping preview read-only and exposing a concise member-facing recommendation without generation IDs, recipe IDs, repository paths or hashes.
- [x] **4.2-T4** Extend mutating update staging/activation so OPTIONAL work is never silently applied, REQUIRED/BLOCKED structural state cannot be falsely activated, and a blocked apply stops before live software/receipt mutation or owner migration. Preserve the existing Slice 4.1 LKG and interruption model.
- [x] **4.2-T5** Add focused positive and destructive-negative tests for no-infrastructure compatibility, OPTIONAL compatibility, REQUIRED activation block, BLOCKED/REVIEW ambiguity/unrecognized generation, stale/unverifiable evidence, read-only preview, plain-English output and interruption/source-receipt truth.
- [x] **4.2-T6** Qualify the exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.2 and stop before Slice 4.3.

## Current owner/descriptors finding

The current admitted Core target `core-first-run-rc1-2026-10-12` pins OS revision `64f7325444d18f94c9d4755d32eb89f3468bda6b`. Its accepted `release/component-release.json` does not publish `migration.infrastructure`. This is expected and truthful because that accepted revision predates the later Phase 3 structural detector/promotion work.

Therefore Slice 4.2 must prove future structural gating through admitted synthetic fixtures and fail-closed contract tests without inventing a live migration or changing current owner semantics.

## Protected boundaries

- Plain `aiverse update` remains the one-action admitted software update.
- `aiverse update --plan` remains preview only.
- Normal update never performs OPTIONAL structural rearrangement.
- Distribution may orchestrate owner evidence but may not invent owner migration logic.
- No structural apply command is introduced in this slice.
- No protected-law amendment is currently indicated.

## Final implementation evidence

- Distribution PR #31 qualified head: `51eb900ac2d692fce7f6e3ae705fdebca257c463`.
- PR-head `Distribution CI` run `38320871651`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.
- Distribution PR #31 merged as `9842451bca86f32e48763fbfe07243a613f15214`.
- Exact merged-main `Distribution CI` run `38321170716`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.
- Product diff at merge was limited to `core_update.py`, `infrastructure_gate.py`, `recovery_orchestrator.py`, `update_output.py`, and `test_infrastructure_update_gate.py`; all temporary patch/workflow helpers were removed before qualification.

## Final behavior

`aiverse update --plan` now includes structural activation truth without mutating the installation. Exact target component snapshots that publish no infrastructure contract remain compatible. When an owner does publish `ai-verse.infrastructure-upgrade/v1`, Distribution requires exact target binding and deterministic owner evidence, resolves only a unique admitted path, and fails closed on ambiguity, stale/unverifiable evidence, unknown generation or a detector that cannot prove read-only behavior.

OPTIONAL structural work never runs inside normal update. REQUIRED work blocks activation but may be represented as evidence-backed staging-compatible state. BLOCKED/REVIEW refuses unsafe staging/activation. The installed mutating path rechecks activation before entering the update transaction, and the Slice 4.1 recovery wrapper rejects known REQUIRED/BLOCKED updates before LKG rotation. No owner migration logic or `aiverse upgrade` apply surface was invented in Slice 4.2.

## Validation discoveries

1. The currently admitted OS target commit `64f7325444d18f94c9d4755d32eb89f3468bda6b` contains a historical component descriptor whose top-level `revision` names an older commit while publishing no infrastructure block. Requiring that stale field even for absence would have broken an already-qualified update. The final rule trusts the exact Git snapshot to prove absence, but requires exact descriptor/recipe target binding once infrastructure metadata is present.
2. Existing preservation tests use `ReleaseSet.raw` for generated-file fixture metadata. Treating any non-empty `raw` as a real catalog release caused fake revisions to be network-probed. The final gate recognizes canonical catalog-shaped runtime releases explicitly.
3. After that correction, the new structural tests themselves had to be upgraded from `raw={"fixture": true}` to catalog-shaped synthetic releases so they continued to exercise the production branch.

These were caught before merge. They do not weaken the protected laws and required no protected-law amendment.

## Acceptance results

- shipped `aiverse update` semantics preserved: **PASS**;
- `aiverse update --plan` preview remains read-only: **PASS**;
- OPTIONAL rearrangement never silently applied by update: **PASS**;
- REQUIRED incompatibility cannot be falsely activated: **PASS**;
- BLOCKED/REVIEW ambiguity and unverifiable evidence fail closed: **PASS**;
- evidence-backed staging/activation truth is explicit: **PASS**;
- known structural refusal happens before LKG rotation/live mutation: **PASS**;
- existing interruption/journal model remains authoritative after mutation admission: **PASS**;
- default member output hides generations, recipe IDs, repository paths and hashes: **PASS**;
- exact PR-head and exact merged-main six-job Distribution CI: **PASS**.

## Closure

Slice 4.2 is complete at **13/18 slices = 72.2%**. Phase 4 is **2/4 complete** with **2 slices until Phase 5**. The next Safe Infrastructure execution unit is **Slice 4.3**, and it has not been implemented by this slice.
