# Safe Infrastructure Slice 4.1 - Last-Known-Good and Restore Evidence

Status: IN PROGRESS

## Slice-start refs

- System: `aiverse-filmmakers/AI-Verse-System@ad260107669b5525523c98f1dd8302c4675c8939`
- Distribution: `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`
- OS: `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- Skills: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

The canonical Safe Infrastructure roadmap was reconciled before this slice began and now truthfully records Phase 3 complete at 11/18 slices (61.1%), with Phase 4 / Slice 4.1 next. Temporary Slice 3.4 roadmap-closure helper/workflow/trigger files were removed before this task list was recorded.

## Verified shipped substrate

### REUSE

- Distribution private state home (`~/.aiverse/distribution` or `AIVERSE_DISTRIBUTION_HOME`).
- `StateStore.lifecycle_transaction()` cross-platform kernel lock and receipt-generation CAS boundary.
- `StateStore._atomic_json()` temp+fsync+atomic replace semantics.
- Existing Core update journal and owner-native interrupted-update recovery.
- Existing exact release receipt / released catalog bindings.
- Existing member-state fingerprint and semantic SQLite preservation helpers.
- Existing Core status/doctor/final-health verification.

### EXTEND

- Core mutating update path: require a verified LKG candidate before first admitted mutation.
- Distribution CLI: add `aiverse restore` preview and explicit `aiverse restore --apply`.
- Distribution preservation/recovery helpers where existing semantics can be reused without becoming a second canonical owner store.

### CREATE

- One Distribution-owned manifest-backed whole-install LKG store using immutable generation material plus an atomic current pointer.
- Recovery coverage manifest with CAPTURE / RECONSTRUCT / REBUILD / EXTERNAL-EXCLUDED classes.
- Transaction-safe restore engine and focused destructive-negative tests.

### DO NOT CREATE

- no second lifecycle lock/transaction system;
- no second canonical live state store;
- no generic backup service;
- no owner-domain migration inference;
- no silent secret copying;
- no multi-snapshot history product;
- no Workspace relocation semantics;
- no change to `aiverse update --plan`, `aiverse doctor`, `aiverse upgrade`, or existing owner-native update-journal meaning.

## Frozen Slice 4.1 semantics

1. Exactly one retained usable whole-install LKG is the product promise. Temporary candidate/restore transaction material does not count as another retained LKG.
2. Candidate material is staged and fully verified before the retained `current` pointer moves.
3. The prior valid LKG remains untouched until successor promotion succeeds.
4. If the current install is unhealthy, ambiguous, source-dirty where exact reconstruction is required, or cannot be represented truthfully, a mutating update must stop before mutation and preserve the old LKG.
5. Recovery material lives under Distribution private state and is never a live provider/canonical owner state source.
6. Large Workspace `assets/` and `outputs/` remain user-owned CAPTURE data unless an explicit owner contract proves otherwise. Size alone never excludes them.
7. Known derived/disposable material is REBUILD and is not copied merely for completeness.
8. External side effects and credential/security state that cannot be safely rewound are EXTERNAL-EXCLUDED and must be reported plainly.
9. Exact software/release state may be RECONSTRUCT only from evidence that the exact admitted revision remains recoverable; otherwise LKG qualification fails safely.
10. `aiverse restore` is read-only preview. `aiverse restore --apply` is the only whole-install restore mutation surface.
11. Restore keeps its target LKG intact throughout apply. A temporary transaction checkpoint may protect the pre-restore current state, but it never replaces the retained LKG.
12. Restore failure must either roll back through the temporary transaction checkpoint or stop `recovery-required` with the retained LKG still usable; it must not guess.

## Adaptive task list

- [ ] **4.1-T1** Reconcile the corrected Phase 3 closure, refresh System/Distribution/OS/Skills refs, and inventory shipped Distribution transaction, update-journal, preservation, exact-release and CLI surfaces.
- [ ] **4.1-T2** Define and implement the Distribution-owned LKG manifest/store: immutable staged generation, content verification, atomic current pointer, previous-LKG preservation until promotion, and bounded retention of exactly one successful generation.
- [ ] **4.1-T3** Implement evidence-backed recovery coverage classification and capture: canonical/user state CAPTURE (including large Workspace assets/outputs), exact software/release RECONSTRUCT evidence, owner-declared derived REBUILD exclusions, explicit security/external exclusions, and no blind secret copying.
- [ ] **4.1-T4** Integrate LKG qualification/rotation into the mutating Core `aiverse update` path before first mutation, reusing the existing lifecycle transaction and refusing mutation if a safe successor LKG cannot be qualified. Expose the reusable guard needed by future `upgrade --apply` without implementing Slice 4.2 orchestration.
- [ ] **4.1-T5** Implement `aiverse restore` preview and `aiverse restore --apply`: plain-English coverage/exclusion/replacement-risk preview, exact target validation, temporary restore checkpoint, covered local-state restore/reconstruction, owner/system verification, retained-target preservation, and truthful external-effect reporting.
- [ ] **4.1-T6** Add focused positive and destructive-negative tests for first LKG creation, rotation, failed candidate preservation, unhealthy/ambiguous refusal, exactly-one retention, large user assets, security exclusions, read-only preview, successful apply, restore failure recovery, and unchanged update-plan/doctor semantics.
- [ ] **4.1-T7** Run exact-head Distribution CI, record evidence, update the canonical roadmap to 12/18 (66.7%) with Phase 4 at 1/3, and stop before Slice 4.2.

## Acceptance gate

Slice 4.1 remains IN PROGRESS until every roadmap acceptance criterion is backed by shipped code/tests and exact-head CI evidence. No acceptance criterion may be closed from contract text alone.
