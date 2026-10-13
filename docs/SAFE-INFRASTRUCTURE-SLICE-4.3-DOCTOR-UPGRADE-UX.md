# Safe Infrastructure Slice 4.3 - Doctor and upgrade-plan aggregation UX

**Status:** IN PROGRESS  
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

- [ ] **4.3-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.3, Slice 2.3 doctor/member-UX invariants, Slice 4.2 structural gate, shipped doctor fan-out and current owner descriptor state; inventory overlapping work before writes.
- [ ] **4.3-T2** Extend whole-install doctor results with deterministic aggregate health/member-summary data while preserving isolated owner evidence, continuing safe independent checks after one owner failure, and keeping doctor strictly read-only.
- [ ] **4.3-T3** Implement read-only `upgrade` planning over the locked admitted release by reusing exact owner infrastructure metadata/detectors and producing OPTIONAL / REQUIRED / BLOCKED-REVIEW counts without applying any owner operation.
- [ ] **4.3-T4** Add concise plain-English traffic-light formatting for `aiverse doctor` and `aiverse upgrade`; keep full technical evidence in `--json`; default output must not expose release IDs, repository/filesystem paths, Git hashes, infrastructure generations, recipe IDs or component-owner jargon.
- [ ] **4.3-T5** Add focused positive/destructive-negative tests for healthy whole-system aggregation, injected isolated owner failure, continued unrelated safe checks, doctor/upgrade read-only proof, OPTIONAL/REQUIRED/BLOCKED clarity, no-live-infrastructure compatibility, JSON evidence retention, and default-output jargon/path/hash leakage.
- [ ] **4.3-T6** Qualify exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.3 and stop before Slice 4.4.

## Current findings

The shipped Distribution doctor already satisfies the core fan-out architecture: it calls each selected owner independently, records per-owner results, makes any owner failure force aggregate failure, continues subsequent safe checks, and adds OS composed-system evidence separately. The current generic CLI formatter is the main member-UX gap because it prints release IDs, root paths and component IDs by default.

The shipped CLI has no `upgrade` command yet. Slice 4.3 therefore adds only the read-only preview. The exact admitted Core release currently has no published owner infrastructure recipe block, so its truthful current preview is expected to report no structural improvement. Future OPTIONAL / REQUIRED / BLOCKED-REVIEW behavior must be proven with admitted synthetic fixtures and exact owner metadata, not invented migration logic.

## Protected boundaries

- `aiverse doctor` remains one read-only member command.
- `aiverse upgrade` is preview-only in Slice 4.3.
- Component-specific doctor remains an internal/expert surface, never required for the member workflow.
- Distribution aggregates owner evidence; it does not reproduce owner health or migration semantics.
- No `upgrade --apply`, migration execution, reference repair or LKG rotation is introduced here.
- No protected-law amendment is currently indicated.
