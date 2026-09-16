# Repair R0.1 - WSA-2026-006 Gateway Destructive Purge Containment

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-006`  
**Severity:** BLOCKER  
**Owner:** `AI-Verse-Gateway`  
**Original audited ref:** `46c15ee58b028dd7fb8b310327ea705ef618805e`  
**Repair PR:** `AI-Verse-Gateway#32`  
**Repair PR head:** `94a1416724f076f06783385c4df07cf18bdbd788`  
**Merged repair ref:** `5347a0b7e3f3f302f4570e9bc37d515192753610`  
**Status:** **CLOSED**

## 1. Original failure

The audited Gateway accepted an arbitrary `--home PATH` and destructive `uninstall --purge` recursively removed that resolved path with:

`rm(home, { recursive: true, force: true })`

The operation did not require a valid Gateway ownership marker, did not bind ownership to a canonical real path, and did not protect unrelated entries inside the selected directory.

This was a proven data-loss path and therefore a dogfood BLOCKER.

## 2. Repair contract

Closure required all of the following:

1. destructive purge must require durable Gateway ownership evidence;
2. ownership must be bound to the exact canonical filesystem root;
3. filesystem roots and broad user-home targets must fail closed;
4. symlink/junction/reparse targets must not authorize destructive purge;
5. missing, malformed, foreign or copied ownership evidence must fail closed;
6. an unrelated non-empty directory must not become Gateway-owned merely because it is supplied through `--home`;
7. purge must delete known Gateway-owned state/files instead of blindly recursively deleting the entire selected root;
8. unknown/unowned entries must survive purge;
9. normal uninstall must preserve Gateway-owned canonical state and enough ownership identity for safe reinstall;
10. negative regressions must execute on Linux, macOS and Windows.

## 3. Implemented repair

At merged Gateway ref `5347a0b7e3f3f302f4570e9bc37d515192753610`:

- `paths(home)` includes persistent `ownership.json`;
- installation writes an ownership marker containing:
  - schema version;
  - `component_id: ai-verse-gateway`;
  - the canonical `root_realpath`;
  - creation/update timestamps;
- ownership markers are accepted only as regular files and only when the component ID/schema/root binding match;
- filesystem roots and the user home directory are rejected;
- the exact Gateway home cannot be a symlink/junction/reparse target;
- existing directories are canonicalized with `realpath` before ownership is bound;
- unrelated non-empty directories without Gateway ownership evidence are refused;
- legacy Gateway homes may gain the persistent marker only when their contents are exclusively the known legacy Gateway entries;
- destructive purge requires the valid persistent ownership marker;
- destructive purge removes only:
  - Gateway `state/`;
  - `config.json`;
  - `host.json`;
  - `goal-owner.json`;
  - `install.json`;
  - `ownership.json`;
- the root directory itself is removed only when empty;
- unexpected files/directories are preserved;
- normal uninstall preserves `state/` and `ownership.json`, allowing a subsequent install to safely reuse retained Gateway state.

Parent path aliases are neutralized by resolving the selected Gateway directory to its canonical physical real path before ownership is recorded or destructive paths are derived. The exact Gateway home itself is additionally rejected if it is a symlink/junction/reparse target.

## 4. Permanent regression coverage

New test file:

`test/lifecycle-containment.test.mjs`

The repair adds regressions proving:

1. install refuses to claim an unrelated non-empty directory;
2. purge fails closed without persistent ownership evidence;
3. purge rejects a foreign or malformed ownership marker;
4. a copied ownership marker cannot authorize a different root;
5. purge refuses the filesystem root and user home;
6. purge rejects an exact home symlink/junction;
7. safe custom-home purge removes Gateway-owned state but preserves an unknown sentinel file;
8. normal uninstall preserves ownership/state and reinstall remains safe.

The test was added to both the normal Gateway test suite and Gateway lifecycle acceptance.

## 5. Exact-head CI and composition evidence

PR-head ref:

`94a1416724f076f06783385c4df07cf18bdbd788`

### Main CI

Run `35152574719`: **SUCCESS**

All six jobs passed:

- Ubuntu, Node 20;
- Ubuntu, Node 22;
- macOS, Node 20;
- macOS, Node 22;
- Windows, Node 20;
- Windows, Node 22.

Ubuntu Node 22 job `104984235806` explicitly reported:

- tests: **104**;
- pass: **104**;
- fail: **0**.

Its log includes the new containment regressions, including unrelated-directory refusal, missing ownership rejection, copied-marker rejection, root/home rejection, symlink/junction rejection, bounded purge and safe reinstall.

### Composed Gateway workflows

All PR-head composed workflows also passed:

- Context Ladder Integrated Acceptance, run `35152574653`: SUCCESS;
- Invisible Intelligence Automation Recommendation Boundary, run `35152574693`: SUCCESS;
- Invisible Intelligence Temporary Worker Composition, run `35152574804`: SUCCESS;
- Invisible Intelligence Permanent Bot Composition, run `35152574938`: SUCCESS.

## 6. Merge integrity

Gateway PR #32 merged as:

`5347a0b7e3f3f302f4570e9bc37d515192753610`

A comparison of PR head `94a1416724f076f06783385c4df07cf18bdbd788` to merged main `5347a0b7e3f3f302f4570e9bc37d515192753610` reports no changed files.

Therefore the exact product bytes exercised by the successful PR workflows are the bytes now present on Gateway main.

Immediately after merge:

- Gateway main = `5347a0b7e3f3f302f4570e9bc37d515192753610`;
- open Gateway PRs = 0.

No post-merge workflow was available at the moment of recheck, so closure relies on the successful exact PR-head matrix plus the proven zero-file-difference merge identity.

## 7. A1.2 standalone Gateway recheck

The executable WSA-006 trace from the original audit no longer exists:

Old:

`--home -> path.resolve -> rm(home, recursive)`

Repaired:

`--home -> canonical directory + broad-root guard -> persistent exact-root ownership verification -> bounded known-owner deletion`

The original WSA-006 closure requirements are now enforced in executable code and permanently covered by regression tests.

This recheck does **not** close or weaken:

- `WSA-2026-007` Gateway lifecycle/live-service truth;
- `WSA-2026-008` Gateway concurrency/idempotency/control-state races.

Standalone result for this finding only:

**WSA-2026-006 closure criteria satisfied.**

## 8. A3.10 lifecycle/recovery recheck

A3.10 contradiction `C-A3.10-001` grouped four destructive lifecycle BLOCKERs:

- WSA-006 Gateway;
- WSA-012 Memory;
- WSA-016 Skills;
- WSA-029 Connections.

The Gateway part is now resolved:

- normal uninstall still preserves canonical Gateway state;
- reinstall remains safe;
- explicit purge is ownership-bound and bounded;
- unknown directory contents are preserved;
- the repaired behavior passed Linux/macOS/Windows CI.

A3.10 as a whole remains **PARTIAL** because the Memory, Skills and Connections destructive blockers remain open, and its separate two-system acceptance finding remains open.

## 9. A4.1 adversarial security/path recheck

A4.1 contradiction `C-A4.1-003` included WSA-006 in the owner-root confinement failure set.

For Gateway destructive purge, the previously proven attack class is now closed at the repaired ref:

- arbitrary unrelated root: rejected;
- filesystem root: rejected;
- user home: rejected;
- exact symlink/junction home: rejected;
- missing owner evidence: rejected;
- wrong owner evidence: rejected;
- copied owner evidence bound to another real root: rejected;
- unknown content inside an owned root: preserved instead of recursively deleted.

A4.1 overall remains **FAILED** because the other inherited security/path/auth findings remain open. This closure changes only the WSA-006 Gateway branch of that contradiction family.

## 10. Finding transition

Canonical state transition:

`OPEN -> CLOSED`

Reason:

- repaired exact SHA exists;
- the original destructive failure path is removed;
- permanent negative regressions cover the original mechanism;
- complete Linux/macOS/Windows owner CI passed;
- relevant composed Gateway workflows passed;
- A1.2, A3.10 and A4.1 finding-specific rechecks no longer reproduce the WSA-006 condition.

Post-transition audit counts:

- total historical findings: **63**;
- OPEN: **62**;
- CLOSED: **1**;
- historical BLOCKER findings: **4**;
- remaining OPEN BLOCKERs: **3**.

The overall whole-system verdict remains:

**NO-GO**

## 11. Next repair

The dependency-safe next repair is:

`R0.2 / WSA-2026-012 - AI-Verse-Memory lifecycle parent-symlink containment`

No work on WSA-012 is included in this closure packet.
