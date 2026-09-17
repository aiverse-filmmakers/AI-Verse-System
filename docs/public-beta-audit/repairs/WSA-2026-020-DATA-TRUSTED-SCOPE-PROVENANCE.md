# Repair R1.2 - WSA-2026-020 Data Trusted Scope Provenance

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-020`  
**Severity:** HIGH  
**Owner:** `AI-Verse-Data`  
**Audited/live pre-repair ref:** `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`  
**Repair branch:** `repair/wsa-2026-020-trusted-scope-provenance`  
**Repair PR:** `AI-Verse-Data#17`  
**Final tested PR head:** `8c30a5557f03cccfb5e96410b18732f9654ff531`  
**Merged repair ref:** `491e22084418f34b849c7d9e700a40973888dcf6`  
**Reviewed/merged product tree:** `a1c8b251f8820b7066f60135895fcb928227d44b`  
**Status:** **CLOSED**

## 1. Original failure

The public Data API exported `DataDatabaseScope` as a structurally compatible TypeScript interface. A caller could construct an ordinary object carrying the same visible fields and methods without obtaining the scope from `TrustedDataRoot` and the trusted scope constructors.

`openScopedDataDatabase(...)` trusted that object's caller-supplied `databasePath()` and `binding`. `createDataClient(...)` performed only a shallow workspace-ID shape check before reaching the same public open boundary.

A structurally forged scope could therefore provide an arbitrary database path and a chosen workspace binding while appearing type-compatible with a trusted scope.

## 2. Repair contract

Closure required:

1. trusted roots must carry runtime-verifiable provenance;
2. trusted database scopes must carry runtime-verifiable provenance that cannot be copied by reproducing their public shape;
3. the authoritative root, workspace identity, binding and database-path derivation must not come from mutable caller-visible values;
4. forged roots/scopes must fail before storage access;
5. the public client path must inherit the same fail-closed boundary;
6. post-construction mutation must not be able to redirect a legitimate scope;
7. safe native and standalone scopes must keep working;
8. permanent regressions must cover structural forgery, outside-path redirection, wrong/copy identity and tampering;
9. `WSA-2026-021` release/version identity must remain untouched.

## 3. Runtime provenance authority

The merged repair adds two module-private runtime provenance registries in `src/scope/trusted-root.ts`:

- a `WeakMap` that binds each genuine `TrustedDataRoot` object identity to its canonical root path;
- a `WeakMap` that binds each genuine Data scope object identity to its authoritative kind, workspace ID, trusted root, relative database path and storage binding.

These maps are not exported. Reproducing public fields, copying methods or satisfying the TypeScript interface does not reproduce authority.

A forged object that was not created by the trusted constructors now fails with `DataScopeError("SCOPE_UNTRUSTED", ...)`.

## 4. Authority is derived, not accepted from caller-visible fields

`openScopedDataDatabase(...)` now:

1. requires a scope identity present in the private provenance registry;
2. obtains the authoritative trusted root, workspace binding and relative database path from that private record;
3. resolves the database path again through the trusted root at open time;
4. passes the authoritative private binding to the storage driver.

It no longer trusts caller-provided `scope.databasePath()` or `scope.binding` as authority.

Because `createDataClient(...)` opens its scope through `openScopedDataDatabase(...)`, the public client also fails closed for an untrusted structurally forged scope before a database is opened or created.

## 5. Trusted-object immutability

`TrustedDataRoot` no longer stores canonical authority as a writable public field. Its `canonicalPath` getter reads the module-private provenance record.

Genuine trusted roots, genuine scopes, scope bindings and stored relative-path arrays are frozen after construction. A legitimate scope therefore cannot be redirected after trust by rewriting:

- the root canonical path;
- `workspaceId`;
- binding workspace identity;
- the visible `databasePath` method.

The actual open boundary still derives authority from the private registry rather than relying on freezing alone.

## 6. Permanent regressions

`test/trusted-scope-provenance.test.ts` adds five focused attack classes:

1. a structurally compatible scope whose `databasePath()` targets an unrelated outside directory is rejected before that database is created;
2. `createDataClient(...)` rejects the same untrusted forged scope before outside storage is touched;
3. copying every visible field from a genuine scope plus a bound genuine `databasePath` method does not copy provenance and is rejected;
4. a genuine root/scope/binding cannot be rewritten after construction, and the real database still opens only at the original derived path while the outside sentinel path remains untouched;
5. a forged object cast as `TrustedDataRoot` is rejected by the trusted scope constructor.

These tests cover both non-derived path authority and wrong/copy workspace authority rather than only malformed input syntax.

## 7. PR-head acceptance

Exact tested PR head:

`8c30a5557f03cccfb5e96410b18732f9654ff531`

PR-head workflows:

- CI run `35259285539`: **SUCCESS**;
  - Ubuntu Node 22: SUCCESS;
  - Ubuntu Node 24: SUCCESS;
  - macOS Node 22: SUCCESS;
  - macOS Node 24: SUCCESS;
  - Windows Node 22: SUCCESS;
  - Windows Node 24: SUCCESS;
  - each leg completed build/test, package smoke, CLI smoke and install smoke;
- Release Smoke run `35259285534`: **SUCCESS**;
- Five-Component Release Acceptance run `35259285592`: **SUCCESS**, all three install-order jobs passed.

The composed acceptance includes Data initialization, structured-record seeding, late component discovery, disable/re-enable, detach/reattach without canonical-state loss and final component doctors.

## 8. Merge integrity

Data PR #17 was squash-merged only after the exact head above completed all required PR workflows.

Merged Data ref:

`491e22084418f34b849c7d9e700a40973888dcf6`

Final PR head and merged ref both have product tree:

`a1c8b251f8820b7066f60135895fcb928227d44b`

The tested product tree is therefore byte-for-byte the merged product tree.

Open Data PRs after merge: **0**.

## 9. Merged-main recheck

Push CI run `35259564907` on merged Data `main` completed **SUCCESS** across all six Ubuntu/macOS/Windows Node 22/24 jobs. Every job again completed build/test, package smoke, CLI smoke and install smoke.

The merged supported-platform state therefore reproduces the tested PR state.

## 10. Finding-specific rechecks

### A1.6 Data standalone recheck

Original failure mechanism:

`caller-created structural object -> accepted as DataDatabaseScope -> caller databasePath()/binding trusted -> arbitrary or wrong-scope storage open`

Repaired mechanism:

`scope object identity -> private provenance lookup -> trusted root + authoritative binding + derived relative path -> trusted-root resolution at open -> storage open`

Unregistered scopes and forged roots fail closed before storage access.

**A1.6 result: PASS for WSA-2026-020 only.**

`WSA-2026-021` remains OPEN.

### A2.4 identity/scope-isolation branch

The Data public-scope provenance branch is resolved for this finding: a caller can no longer claim workspace authority merely by constructing the expected object shape or supplying a matching visible binding.

A2.4 is not globally reclassified here; unrelated identity/authentication findings remain open.

### A3.10 multi-root/system-isolation branch

The WSA-020 contribution to cross-root isolation is resolved: scopes with equal visible workspace identifiers cannot be fabricated to redirect one trusted Data client into an arbitrary second root. Genuine scopes remain tied by object provenance to their originating trusted root.

A3.10 remains incomplete overall because `WSA-2026-049` and other lifecycle/isolation findings remain OPEN.

### A4.1 adversarial scope/path branch

The structurally forged Data path-authority attack now fails before filesystem/database access, including copied-visible-field and post-construction-tampering variants.

A4.1 remains failed/incomplete overall because other security/path findings remain OPEN.

## 11. Finding transition

Canonical transition:

`WSA-2026-020: OPEN -> CLOSED`

Post-transition counts:

- historical findings: **63**;
- OPEN: **57**;
- CLOSED: **6**;
- OPEN BLOCKERs: **0**.

R1 progress becomes:

**2 / 13 CLOSED = 15.38%**

Overall whole-system verdict remains **NO-GO**. Remaining repair waves and the bounded final independent recheck remain mandatory.

## 12. Next repair

The dependency-safe next task is:

`R1.3 / WSA-2026-022 - AI-Verse-Multiple-Bots operator/domain authority binding`

No implementation of WSA-2026-022 is included in this repair or closure packet.
