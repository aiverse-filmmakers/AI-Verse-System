# Repair R0.2 - WSA-2026-012 Memory Lifecycle Parent Containment

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-012`  
**Severity:** BLOCKER  
**Owner:** `AI-Verse-Memory`  
**Original audited ref:** `406b14fb4398eb1b16dd5f30e50520e8c3540972`  
**Repair PR:** `AI-Verse-Memory#30`  
**Final repair PR head:** `acbe3e22d9b12c0fc1b0dcd95eeea393a57a69f2`  
**Merged repair ref:** `7a1ed5777fd11616375501d730fcbd488beff8b8`  
**Status:** **CLOSED**

## 1. Original failure

Memory protected canonical Memory writes from several direct symlink escapes, but component lifecycle paths were not uniformly protected.

The original audited lifecycle could:

- copy runtime files through a symlinked parent such as `target/scripts`;
- copy adapter files through symlinked parents under `.claude/skills` or `.agents/skills`;
- remove a normal-looking leaf directory with `shutil.rmtree` even when an ancestor redirected that leaf outside the selected target.

A concrete destructive trace was:

`target/scripts -> external directory -> target/scripts/ai-verse-memory appears as an ordinary external directory -> uninstall rmtree(runtime)`

Equivalent parent-chain risks existed for adapter directories.

The leaf-only `is_symlink()` checks did not prove the complete path remained physically contained by the selected target.

## 2. Repair contract

Closure required all of the following:

1. use one shared containment law for Memory lifecycle paths;
2. reject symlinked parent components;
3. reject Windows junction/reparse components;
4. prove existing path components resolve inside the selected target's canonical root;
5. validate the nearest existing parent before creating missing children;
6. never recursively delete runtime/adapters until the full path has passed containment;
7. preflight destructive uninstall targets before unregistering or deleting anything;
8. apply the protection to install, setup, update, reconcile and uninstall;
9. cover `scripts`, runtime directory, `.claude`, `.claude/skills`, adapter directory, `.agents`, `.agents/skills`, and adapter directory;
10. prove external sentinel data survives the rejected operations on Linux, macOS and Windows.

## 3. Implemented repair

At merged Memory ref `7a1ed5777fd11616375501d730fcbd488beff8b8`, `scripts/install_engine.py` defines one shared:

`assert_safe_lifecycle_path(target, candidate)`

The helper:

- normalizes the supplied target/candidate path;
- requires the selected target to exist and be a directory;
- refuses a selected target that is itself a symlink/junction/reparse point;
- establishes the selected target's canonical physical root;
- handles platform path aliases while preserving that physical root;
- walks each existing candidate component;
- rejects POSIX symlinks;
- rejects Windows reparse/junction components through `st_file_attributes & 0x0400`;
- checks resolved existing components remain descendants of the canonical selected target;
- resolves the nearest existing parent for a missing destination and requires it to remain inside the canonical target.

The shared helper is now used by target-root lifecycle operations including:

- runtime package copies;
- sibling runtime support-module copies;
- adapter installation;
- local extension registry directory/file access;
- legacy integration marker cleanup;
- standalone marker writes;
- standalone profile/scenario/runtime copies;
- update/reconcile paths;
- destructive uninstall targets.

`source_copy` validates before parent creation and revalidates before the copy/write.

## 4. Destructive uninstall containment

`scripts/component.py` now has a destructive preflight:

`_preflight_uninstall_paths(target, mode)`

Before native uninstall can unregister Memory or delete any adapter/runtime path, the preflight validates all destructive targets.

After preflight:

- each adapter directory is validated again before `shutil.rmtree`;
- the runtime directory is validated again before `shutil.rmtree`;
- standalone lifecycle file removals are individually validated;
- marker edits are routed through the shared target-root containment helper.

Therefore a bad runtime or adapter parent fails closed before the lifecycle mutates registration or removes any component path.

## 5. Permanent adversarial regressions

`tests/test_component_lifecycle.py` adds two lifecycle attack tests.

### Install/setup containment

`test_install_and_setup_reject_symlink_or_reparse_lifecycle_parents`

Attacks:

- `scripts`;
- `scripts/ai-verse-memory`;
- `.claude`;
- `.claude/skills`;
- `.claude/skills/ai-verse-memory`;
- `.agents`;
- `.agents/skills`;
- `.agents/skills/ai-verse-memory`.

The operation must raise and the external sentinel must survive. No external Memory runtime or skill file may be written.

### Uninstall containment

`test_uninstall_preflight_rejects_symlink_or_reparse_paths_without_external_deletion`

Attacks the same parent/leaf family after a successful install/setup.

The operation must raise, the external sentinel must survive, and the local extension registry bytes must remain unchanged. This proves destructive preflight occurs before unregister/removal.

### Windows-specific proof

The regression harness does not skip Windows directory-link coverage.

On Windows it explicitly creates directory junctions with:

`cmd /c mklink /J`

This exercises Windows reparse-point behavior rather than relying only on POSIX symlink semantics.

## 6. CI correction preserved as evidence

The first repair head exposed an over-strict portability issue in the new containment helper.

Initial workflow:

`35155623941`

Result:

- Ubuntu acceptance passed;
- macOS/Windows acceptance failed because platform-level aliases above the selected root were represented differently:
  - macOS `/var` versus `/private/var`;
  - Windows short 8.3 user path versus long user path.

This was not merged.

The helper was corrected to canonicalize the selected target consistently while still walking/rejecting redirected components inside the selected target.

Final repair head:

`acbe3e22d9b12c0fc1b0dcd95eeea393a57a69f2`

## 7. Final exact-head CI

Workflow run:

`35155708095`

Final result:

**SUCCESS - 12 / 12 jobs green**

Successful jobs:

- public-beta acceptance: Ubuntu;
- public-beta acceptance: macOS;
- public-beta acceptance: Windows;
- unit tests: Ubuntu Python 3.9;
- unit tests: Ubuntu Python 3.12;
- unit tests: macOS Python 3.9;
- unit tests: macOS Python 3.12;
- unit tests: Windows Python 3.9;
- unit tests: Windows Python 3.12;
- installer smoke: Ubuntu;
- installer smoke: Windows;
- OS update integration: Ubuntu.

Windows public-beta acceptance job `104994513236` explicitly executed both new lifecycle containment tests successfully and reported:

- `Ran 17 tests`;
- `OK`.

Because the Windows test helper creates real directory junctions, this is direct hosted evidence for the reparse-point attack class in the finding.

## 8. Merge integrity

Memory PR #30 merged as:

`7a1ed5777fd11616375501d730fcbd488beff8b8`

Comparison from final tested PR head:

`acbe3e22d9b12c0fc1b0dcd95eeea393a57a69f2`

to merged main reports:

- one merge commit ahead;
- **zero changed files**.

Immediately after merge:

- Memory main = `7a1ed5777fd11616375501d730fcbd488beff8b8`;
- open Memory PRs = 0.

Therefore the product files re-audited on merged main are the same product files that passed the final PR-head workflow.

## 9. A1.4 standalone Memory recheck

Original WSA-012 lifecycle condition:

`lexical child path + leaf-only symlink check -> copy/rmtree through redirected parent`

Repaired condition:

`candidate lifecycle path -> shared physical target containment -> reject symlink/junction/reparse component -> resolve existing chain inside canonical target -> destructive preflight -> bounded lifecycle effect`

Merged-main inspection confirms the helper is active in the shared installer boundary and destructive uninstall preflight.

The original parent-redirection attack is permanently exercised across the required runtime/adapter parent levels.

**WSA-2026-012 closure criteria are satisfied.**

This finding-specific recheck does not close or weaken:

- `WSA-2026-013` Memory lifecycle/write authority;
- `WSA-2026-014` Memory migration authority handoff atomicity;
- `WSA-2026-015` Memory release/bootstrap identity.

## 10. A3.10 lifecycle/recovery recheck

A3.10 contradiction `C-A3.10-001` grouped four destructive lifecycle BLOCKERs:

- WSA-006 Gateway;
- WSA-012 Memory;
- WSA-016 Skills;
- WSA-029 Connections.

After R0.1 and R0.2:

- Gateway WSA-006: CLOSED;
- Memory WSA-012: CLOSED;
- Skills WSA-016: OPEN;
- Connections WSA-029: OPEN.

The Memory branch of the destructive lifecycle contradiction is therefore resolved.

A3.10 remains **PARTIAL** because the remaining Skills and Connections blockers plus other lifecycle/recovery findings remain open.

## 11. A4.1 adversarial security/path recheck

A4.1 contradiction `C-A4.1-003` includes WSA-012 in the owner-root/path-confinement failure family.

For Memory lifecycle paths, the previously proven attack class is now closed:

- symlinked `scripts`: rejected;
- symlinked runtime directory: rejected;
- symlinked `.claude` chain: rejected;
- symlinked `.agents` chain: rejected;
- Windows junction/reparse equivalents: rejected;
- install/setup external write: rejected;
- uninstall external recursive deletion: rejected;
- external sentinel preservation: proven;
- lifecycle registration preservation on rejected uninstall: proven.

A4.1 overall remains **FAILED** because other path/security/authority findings remain open.

## 12. Finding transition

Canonical state transition:

`OPEN -> CLOSED`

Closure basis:

- repaired merged exact SHA exists;
- one shared lifecycle containment law covers the original mechanism;
- destructive operations preflight before mutation;
- permanent regressions cover all parent/leaf levels required by the finding;
- actual Windows junction tests pass;
- Ubuntu/macOS/Windows public-beta acceptance passes;
- complete supported Python matrix passes;
- installer and OS-update compatibility evidence passes;
- merged-main inspection and zero-file-difference merge comparison confirm the tested repair is the merged repair;
- A1.4, A3.10 and A4.1 finding-specific rechecks no longer reproduce WSA-012.

Post-transition counts:

- total historical findings: **63**;
- OPEN: **61**;
- CLOSED: **2**;
- historical BLOCKER findings: **4**;
- remaining OPEN BLOCKERs: **2**.

Remaining OPEN BLOCKERs:

- `WSA-2026-016` Skills lifecycle-controller containment;
- `WSA-2026-029` Connections destructive purge containment.

Overall whole-system verdict remains:

**NO-GO**

## 13. Next repair

The dependency-safe next repair is:

`R0.3 / WSA-2026-016 - AI-Verse-Skills lifecycle-controller containment`

No implementation of WSA-016 is included in this closure packet.
