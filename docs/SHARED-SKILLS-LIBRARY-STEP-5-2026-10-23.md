# Shared Skills Library — step 5 qualification

Status: ACTIVE. No new Core release is admitted yet.

## Source delivery

- Skills source PR #23 merged after 20 exact-head native checks passed.
- Brain source PR #33 merged after nine exact-head native checks passed.
- Owner descriptor PRs Skills #24 and Brain #34 are awaiting their native gates.
- OS source PR #100 and Distribution source PR #75 are in qualification.

## Observed local evidence

- Skills full suite: 175 tests passed.
- Brain full suite: 263 tests passed using the source package and admitted interpreter on PATH.
- Distribution full suite: 544 tests passed, 11 skips.
- OS placement, promotion, resolver, member library and bindings passed.
- Actual Distribution/OS/Brain/Skills runtime fixture: nine groups passed.

## Qualification repairs

- Retained Python 3.9 support by pinning its Ubuntu runner to 22.04; the new Ubuntu default had no matching Python build.
- Corrected Memory fixture ordering: install provides runtime; setup registers generated adapters, which are asserted afterward.
- Exact new owner revisions are routed through native JSON lifecycle adapters.
- Three-platform new shared Skills composition coverage added to OS.

Remaining: finish source checks/acceptance, freeze exact candidate inputs, real fresh/populated install/update qualification on all supported platforms, promote through Core, then step 6 member update and manual skills move.

## Privacy hardening and v2 qualification

All three owner source changes and their initial descriptors merged. V1 authenticated candidate admission passed and a disposable macOS fresh Core installation passed exact pins, allfive owners, cross-workspace import, settings, retry, source preservation, uninstall/reinstall and no-op lifecycle checks.

Before rollout, OS private settings were found missing from template ignore rules. PR102 corrects this with13 actual Git path checks on allthree platforms; all32 source checks passed. PR103 accepts OS0.3.7 at5845fcfed123910e854ff764cb895c826a0b3291. V1 is not promoted; its immutable evidence remains historical. V2 must bind the corrected source and repeat platform qualification.

Populated V1 updates completed through owner health. Acceptance false positives on generated timestamps and equivalent registry JSON formatting were corrected: immutable package/member bytes stay protected, complete registry values (including unknown fields and disabled flags) must match, policy/authority/root changes remain refused, and setup receipts must name exact generations. Twelve focused guards pass. New fixtures retain a pre-existing personal method, old reference, same-name collision and unknown registration fields. These are acceptance improvements, not relaxations of the actual updater.
