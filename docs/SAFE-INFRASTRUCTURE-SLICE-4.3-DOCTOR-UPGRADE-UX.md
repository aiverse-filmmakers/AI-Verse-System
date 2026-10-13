# Safe Infrastructure Slice 4.3 - Doctor and upgrade-plan aggregation UX

**Status:** COMPLETE  
**Canonical slice:** `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`, Slice 4.3  
**Recorded before product implementation:** yes

## Starting refs

- `aiverse-filmmakers/AI-Verse-System@0580241ed284d5f5e80b8afbc0b706fb075db4b1`
- `aiverse-filmmakers/ai-verse-distribution@9842451bca86f32e48763fbfe07243a613f15214`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

## Evidence classification

- **REUSE/EXTEND:** shipped `Orchestrator.doctor()` owner fan-out and composed OS doctor evidence.
- **REUSE/EXTEND:** Slice 4.2 `InfrastructureUpdateGate` exact-target owner infrastructure metadata validation and deterministic OPTIONAL / REQUIRED / BLOCKED-REVIEW classification.
- **CREATE:** one read-only structural `aiverse upgrade` preview surface over the locked admitted release.
- **CREATE:** concise traffic-light member formatter for doctor/upgrade while preserving full JSON evidence.
- **DEFER:** all structural apply, LKG rotation for upgrade, owner migration invocation, resume and post-apply verification remain Slice 4.4.
- **NO OWNER CHANGE EXPECTED:** current admitted Core owner descriptors publish no live `migration.infrastructure`; future behavior is qualified through exact admitted synthetic fixtures without inventing owner migrations.

## Adaptive task list

- [x] **4.3-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.3, Slice 2.3 doctor/member-UX invariants, Slice 4.2 structural gate, shipped doctor fan-out and current owner descriptor state; inventory overlapping work before writes.
- [x] **4.3-T2** Extend whole-install doctor results with deterministic aggregate health/member-summary data while preserving isolated owner evidence, continuing safe independent checks after one owner failure, and keeping doctor strictly read-only.
- [x] **4.3-T3** Implement read-only `upgrade` planning over the locked admitted release by reusing exact owner infrastructure metadata/detectors and producing OPTIONAL / REQUIRED / BLOCKED-REVIEW counts without applying any owner operation.
- [x] **4.3-T4** Add concise plain-English traffic-light formatting for `aiverse doctor` and `aiverse upgrade`; keep full technical evidence in `--json`; default output must not expose release IDs, repository/filesystem paths, Git hashes, infrastructure generations, recipe IDs or component-owner jargon.
- [x] **4.3-T5** Add focused positive/destructive-negative tests for healthy whole-system aggregation, injected isolated owner failure, continued unrelated safe checks, doctor/upgrade read-only proof, OPTIONAL/REQUIRED/BLOCKED clarity, no-live-infrastructure compatibility, JSON evidence retention, and default-output jargon/path/hash leakage.
- [x] **4.3-T6** Qualify exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.3 and stop before Slice 4.4.

## Current findings

The shipped Distribution doctor already satisfies the core fan-out architecture: it calls each selected owner independently, records per-owner results, makes any owner failure force aggregate failure, continues subsequent safe checks, and adds OS composed-system evidence separately. The current generic CLI formatter was the main member-UX gap because it printed release IDs, root paths and component IDs by default.

The shipped CLI had no `upgrade` command. Slice 4.3 adds only the read-only preview. The exact admitted Core release currently has no published owner infrastructure recipe block, so its truthful current preview reports no structural improvement. Future OPTIONAL / REQUIRED / BLOCKED-REVIEW behavior is proven with admitted synthetic fixtures and exact owner metadata rather than invented migration logic.

## Protected boundaries

- `aiverse doctor` remains one read-only member command.
- `aiverse upgrade` is preview-only in Slice 4.3.
- Component-specific doctor remains an internal/expert surface, never required for the member workflow.
- Distribution aggregates owner evidence; it does not reproduce owner health or migration semantics.
- No `upgrade --apply`, migration execution, reference repair or LKG rotation is introduced here.
- No protected-law amendment was required.

## Final implementation evidence

- Slice 4.3 start/task record: System PR #202, merged as `b35e0ea4cefa7c770d2b786f52291f45cdb054a7` after Contract Validation `38373315133` succeeded on Python 3.11 and 3.13.
- Distribution PR #32 qualified head: `5ee2cfea8155907a279e6a33fe64505712151cab`.
- PR-head `Distribution CI` run `38374443919`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.
- Distribution PR #32 merged main: `15e03219185f484cbbc4c5887d967ddc5630d1a6`.
- Exact merged-main `Distribution CI` run `38375126907`: **SUCCESS** on Ubuntu/macOS/Windows with Python 3.11/3.12.
- Product diff was limited to the installed entrypoint, the new read-only experience orchestrator/formatter, and focused 4.3 tests. No temporary workflow/helper machinery was added to Distribution.

## Final behavior

The installed whole-system `aiverse doctor` now uses a separate read-only `doctor_overview()` layer instead of replacing the internal lifecycle `doctor()`. This preserves the existing update/LKG/restore final-health contract while giving members one concise whole-system view. The underlying owner fan-out still records isolated results, continues safe independent checks after one owner failure, and cannot turn an owner failure into aggregate PASS.

`aiverse upgrade` now exists as a read-only structural preview over the exact locked admitted release. It reuses Slice 4.2 owner infrastructure evidence and returns OPTIONAL / REQUIRED / BLOCKED-REVIEW truth without applying owner operations, repairing references, rotating LKG or mutating the receipt. A pending lifecycle owner effect is reported as review-blocked rather than ignored.

Default doctor/upgrade output is intentionally small and plain-English. It reports health, safe improvements, required changes, review/blocked counts, risk, whether anything changed and the recommended next action. Full technical owner/component evidence remains available through `--json`. Existing `doctor --component ...` routing remains available as an expert compatibility surface, but the member does not need it.

## Validation discoveries

1. The new test harness initially used a mocked catalog without supplying a transition contract. Because the orchestrator correctly validates real Core transitions during construction, those synthetic tests failed before 4.3 behavior ran. The fixtures were corrected to inject a mock transition contract; production validation was not weakened.
2. A first pending-lifecycle test manually inserted `_pending_lifecycle` into the receipt. `StateStore.write()` correctly strips that derived view because authoritative pending effects live in `pending-lifecycle.json`. The test was corrected to use the real `lifecycle_transaction()` + `begin_effect()` contract.
3. Review identified that routing every `doctor` invocation through the new member formatter would silently remove the existing expert `doctor --component ...` surface. Final routing sends only whole-system doctor through the new overview while preserving the component-scoped expert path.

All three issues were caught before merge. None required a protected-law amendment.

## Acceptance results

- one `aiverse doctor` command checks the whole supported installation from the member perspective: **PASS**;
- owner checks execute internally with isolated evidence/results: **PASS**;
- one owner failure is surfaced and cannot become false aggregate PASS: **PASS**;
- unrelated safe owner checks remain represented after another owner failure: **PASS**;
- member does not need component-specific doctor commands: **PASS**;
- existing component-scoped expert doctor remains compatible: **PASS**;
- default summary is concise and plain English: **PASS**;
- full technical evidence remains available and machine-readable through `--json`: **PASS**;
- doctor and upgrade preview are read-only: **PASS**;
- OPTIONAL / REQUIRED / BLOCKED-REVIEW cases are explicit: **PASS**;
- pending lifecycle recovery blocks structural planning without mutation: **PASS**;
- default output does not expose release IDs, repository/filesystem paths, Git hashes, infrastructure generations or recipe IDs: **PASS**;
- internal lifecycle doctor semantics used by update/LKG/restore remain unchanged: **PASS**;
- exact PR-head and exact merged-main six-job Distribution CI are green: **PASS**.

## Closure

Slice 4.3 is complete at **14/18 slices = 77.8%**. Phase 4 is **3/4 complete** with **1 slice until Phase 5**. The next Safe Infrastructure execution unit is **Slice 4.4 - Implement `upgrade --apply` orchestration, resume and verification**. No Slice 4.4 implementation was started by this slice.
