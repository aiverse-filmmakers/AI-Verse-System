# Safe Infrastructure Slice 4.2 - Update staging and activation gating

**Status:** IN PROGRESS  
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

- [ ] **4.2-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.2, the infrastructure recipe contract, shipped updater/LKG flow and current owner descriptor state; inventory overlapping work before writes.
- [ ] **4.2-T2** Implement exact target component descriptor acquisition/validation plus deterministic read-only structural requirement classification, consuming only `ai-verse.infrastructure-upgrade/v1` owner metadata and failing closed on missing/ambiguous/unverifiable evidence.
- [ ] **4.2-T3** Extend Core `update_plan` with OPTIONAL / REQUIRED / BLOCKED-REVIEW activation truth while preserving no-op behavior, keeping preview read-only and exposing a concise member-facing recommendation without generation IDs, recipe IDs, repository paths or hashes.
- [ ] **4.2-T4** Extend mutating update staging/activation so OPTIONAL work is never silently applied, REQUIRED/BLOCKED structural state cannot be falsely activated, and a blocked apply stops before live software/receipt mutation or owner migration. Preserve the existing Slice 4.1 LKG and interruption model.
- [ ] **4.2-T5** Add focused positive and destructive-negative tests for no-infrastructure compatibility, OPTIONAL compatibility, REQUIRED activation block, BLOCKED/REVIEW ambiguity/unrecognized generation, stale/unverifiable evidence, read-only preview, plain-English output and interruption/source-receipt truth.
- [ ] **4.2-T6** Qualify the exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.2 and stop before Slice 4.3.

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
