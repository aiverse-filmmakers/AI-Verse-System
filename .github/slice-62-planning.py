from pathlib import Path

path = Path('docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')

# Reconcile the stale summary header left by the completed Slice 6.1 closure.
head, sep, rest = text.partition('\n---\n')
if not sep:
    raise SystemExit('roadmap header separator not found')
header_replacements = [
    ('**Completed:** 17  ', '**Completed:** 18'),
    ('**Remaining:** 3  ', '**Remaining:** 2'),
    ('**Overall progress:** 85.0%  ', '**Overall progress:** 90.0%'),
    ('**Current phase progress:** 0/3 slices complete  ', '**Current phase progress:** 1/3 slices complete'),
    ('**Slices until program completion:** 3  ', '**Slices until program completion:** 2'),
    ('**Current slice:** 6.1 - Cross-repo regression/evidence validation  ', '**Current slice:** 6.2 - End-to-end qualification'),
    ('**Next slice:** 6.2 - End-to-end qualification', '**Next slice:** 6.3 - Canonical closeout and handoff'),
]
for old, new in header_replacements:
    if head.count(old) != 1:
        raise SystemExit(f'expected one header token {old!r}, got {head.count(old)}')
    head = head.replace(old, new, 1)
text = head + sep + rest

old_slice = '''## Slice 6.2 - End-to-end qualification

**Status:** NOT STARTED  
**Dependencies:** 6.1

Prove Distribution-originated, component-originated, sibling-defect, stale-doc, breaking-contract and emergency paths end to end with exact refs, preservation, member isolation, provenance and reconstructability.
'''
new_slice = '''## Slice 6.2 - End-to-end qualification

**Status:** IN PROGRESS
**Dependencies:** 6.1
**Adaptive tasks:** 0/5 complete

Prove Distribution-originated, component-originated, sibling-defect, stale-doc, breaking-contract and emergency paths end to end with exact refs, preservation, member isolation, provenance and reconstructability.

### Bounded planning

Planning is bound to System `27ebfcfadb07260aa8854374bd03bd28d248f743` and Distribution `74a317497a54ec9e12c14ac705b7bbb251eddfe4`. This run inspected only the permanent execution/governance laws, accepted Slice 6.1 evidence, the current Core release, the existing candidate-admission -> preservation/composed-acceptance -> whole-product-qualification -> promotion/receipt chain, and the exact-ref repository-network/Safe Infrastructure validation surfaces. No 6.2 qualification, promotion, owner implementation, release/catalog mutation, Repository State/ledger refresh, member installation mutation or user-owned-state mutation was performed.

- **REUSE:** immutable candidate evidence/admission, Component Release Descriptor and owner-native acceptance, Registry/Repository State scoped evidence, lifecycle payload/preservation machinery, whole-product qualification, Core promotion planning/apply, durable release receipts/reconstruction, the current Repository Network Regression exact-checkout pattern, and Safe Infrastructure regression/convergence fixtures.
- **EXTEND:** compose those already-proven layers inside an isolated qualification workspace so one test path can traverse exact owner/System/Distribution evidence through qualification and receipt reconstruction without granting the harness new release, owner, Registry/State or member-state authority. Extend the existing exact-ref CI pattern rather than inventing a parallel acceptance service.
- **CREATE:** one deterministic end-to-end qualification harness/fixture layer in Distribution, plus only the minimal permanent CI wiring needed at final 6.2 closure. Fixture writes must be confined to temporary/isolated workspaces; live release catalogs and canonical owner/System state stay read-only.
- **RETIRE:** nothing. Existing owner-native CI, System Contract Validation, Distribution CI, Repository Network Regression, Safe Infrastructure gates and historical U35/U36 evidence remain authoritative in their existing scopes.
- **BLOCK/UNKNOWN:** no architecture blocker was found. A component-originated positive path requires a real exact owner-accepted forward revision; current observed owner heads are not acceptance merely because they are newer. Reuse exact future owner evidence if it already exists, otherwise create only a bounded temporary candidate/ref at the canonical owner and obtain native acceptance before Distribution adoption. Historical OS `setup-required` evidence is not reusable as PASS; the positive fixture must produce fresh exact composed acceptance or fail closed. No plan amendment is required.
- The live Core boundary remains unchanged at planning start: `current_release` is `core-first-run-rc1-2026-10-12`, the explicit candidate overlay is empty, `system_sync_debts` is empty, historical U36 evidence is untouched, and Slice 6.1 permanent network CI is the accepted cross-repository regression floor.

### Adaptive task list

- [ ] **6.2-T1** Build the isolated end-to-end qualification harness around the existing candidate-admission, preservation/composed-acceptance, whole-product-qualification, promotion and durable-receipt machinery, then prove a Distribution-originated forward Core candidate using unchanged exact owner-accepted component refs can traverse admission through isolated final admission and exact receipt reconstruction while member/user state and all live catalogs remain untouched.
- [ ] **6.2-T2** Prove the component-originated positive path with one real exact owner-accepted forward component revision: reuse existing exact acceptance if available or obtain bounded temporary owner-native candidate evidence at the canonical owner, freeze the required scoped System/Registry/State evidence in an isolated workspace, adopt exactly that ref in Distribution, and prove qualification, preservation/member isolation, isolated final admission and reconstructability without treating observed/latest refs as acceptance or mutating live release state.
- [ ] **6.2-T3** Extend the isolated harness with end-to-end sibling-defect, stale-doc and breaking-contract cases: a sibling defect must route back to the canonical owner and cannot be patched/adopted by Distribution without exact owner acceptance; stale System prose must produce evidence-first drift/reconciliation without regressing accepted implementation or fabricating release authority; a depended-on breaking contract must block composition/promotion unless an accepted compatibility/migration path exists. Prove exact provenance, no destructive member/user-state mutation and fail-closed/requalification behavior where required.
- [ ] **6.2-T4** Prove the emergency path end to end in isolation through the same owner validation, exact refs, compatibility/migration, preservation, member isolation and whole-product qualification gates; allow only explicit non-safety `SYSTEM-SYNC-DEBT`, bind the exact debt in durable receipt evidence, prove later normal promotion is blocked while debt is open, and prove reconciliation requires exact synchronized canonical State before normal promotion can resume. Perform no live promotion.
- [ ] **6.2-T5** Wire the accepted end-to-end harness into permanent exact-ref CI by extending the existing repository-network gate or adding only the minimal non-duplicative qualification gate, run clean Distribution and required System cross-validation, confirm live release/candidate/debt/member and canonical State/ledger remain unchanged, close Slice 6.2, advance only to the Slice 6.3 bounded discovery/planning start, and stop without beginning canonical closeout.

Slice 6.2 planning is complete. 6.2-T1 has not begun. No plan amendment was required.
'''
if text.count(old_slice) != 1:
    raise SystemExit(f'expected one untouched 6.2 block, got {text.count(old_slice)}')
text = text.replace(old_slice, new_slice, 1)

change_log_marker = '# Program Change Log\n\n'
if text.count(change_log_marker) != 1:
    raise SystemExit('Program Change Log marker not unique')
change_log_entry = '''## 2026-10-17 - Slice 6.2 bounded planning started

- Bound planning to System `27ebfcfadb07260aa8854374bd03bd28d248f743` and Distribution `74a317497a54ec9e12c14ac705b7bbb251eddfe4`; no end-to-end qualification or product/release/State/member mutation was performed.
- Reused the completed candidate-admission, preservation, whole-product qualification, promotion/debt and durable-receipt layers plus the permanent exact-ref Repository Network Regression and Safe Infrastructure fixtures rather than introducing a second release or acceptance authority.
- Identified the only positive-path evidence caveat: a component-originated forward revision must be genuinely owner-accepted at an exact ref; observed/latest owner heads cannot substitute for native acceptance. Historical `setup-required` output also cannot be relabeled PASS.
- Derived five adaptive tasks: Distribution-originated positive qualification, component-originated positive qualification, sibling/stale-doc/breaking-contract cross-boundary cases, emergency debt/reconciliation, then permanent CI and clean closure. 6.2-T1 is the only next task. No plan amendment.

'''
text = text.replace(change_log_marker, change_log_marker + change_log_entry, 1)

pointer = text.index('# Current execution pointer')
pointer_text = '''# Current execution pointer

**Completed:** 18/20
**Overall:** 90.0%
**Phase:** Phase 6 - Prove the network and close
**Phase progress:** 1/3
**Until program completion:** 2 slices
**Current slice:** Slice 6.2 - End-to-end qualification (`IN PROGRESS`, 0/5 tasks complete)
**Next:** 6.2-T1 - build the isolated end-to-end qualification harness around the existing candidate-admission, preservation/composed-acceptance, whole-product-qualification, promotion and durable-receipt machinery, then prove a Distribution-originated forward Core candidate using unchanged exact owner-accepted component refs can traverse admission through isolated final admission and exact receipt reconstruction while member/user state and all live catalogs remain untouched
**Blockers/drift/amendments:** Slice 6.2 planning is complete at System `27ebfcfadb07260aa8854374bd03bd28d248f743` and Distribution `74a317497a54ec9e12c14ac705b7bbb251eddfe4`. Live Core release remains `core-first-run-rc1-2026-10-12`, candidate overlay and `system_sync_debts` remain empty, historical U36 and canonical System State/ledger are unchanged. No architecture blocker or plan amendment. For later 6.2-T2, a component-originated positive path must use real exact owner-native acceptance rather than a newer observed head; fresh exact composed acceptance is required and historical `setup-required` evidence is not PASS. 6.2-T1 has not begun.
'''
text = text[:pointer] + pointer_text

path.write_text(text, encoding='utf-8')
