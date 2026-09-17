# Repair R0.3 - WSA-2026-016 Skills Controller Containment

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-016`  
**Severity:** BLOCKER  
**Owner:** `AI-Verse-Skills`  
**Original audited ref:** `8c321c03421a2e0e470280cc40e588a27c1a510d`  
**Repair PR:** `AI-Verse-Skills#15`  
**Final repair PR head:** `62b49d6420a6034fd08c47c2070ec473f128a392`  
**Merged repair ref:** `3541d2a7af1b20ca12736ed7454d119295d8e193`  
**Status:** **CLOSED**

## 1. Original failure

Skills already physically confined provider package paths, but lifecycle controller state under `root/.aiverse` did not have an equivalent independent physical-containment boundary.

That meant lifecycle state, generation storage and destructive retention could derive from a controller path redirected outside the selected Skills root through a symlink or Windows junction/reparse point.

The critical class was not merely a lexical `..` traversal. A path such as a redirected `.aiverse` or `.aiverse/generations` could remain lexically inside the selected root while physically referring to external storage.

## 2. Repair contract

Closure required all of the following:

1. one shared controller-path safety primitive;
2. controller paths physically confined to the selected Skills root;
3. POSIX symlink rejection;
4. Windows junction/reparse rejection;
5. existing controller descendants proven to resolve under the selected canonical root;
6. missing descendants allowed only when their nearest existing parent is safe;
7. generation paths and active state derived through the same primitive;
8. learning/setup/integration controller state derived through the same law;
9. destructive generation purge unable to recursively remove redirected external data;
10. platform regressions on Ubuntu, macOS and Windows, including real Windows junctions.

This repair was intentionally bounded to WSA-2026-016. It does not close WSA-2026-017, WSA-2026-018 or WSA-2026-019.

## 3. Implemented repair

At merged Skills ref `3541d2a7af1b20ca12736ed7454d119295d8e193`, `installer/generation_lifecycle.py` defines one low-level controller primitive:

`controller_path(root, *parts)`

The primitive:

- derives controller-owned state from the selected root;
- rejects invalid path components;
- rejects a selected root that is itself a symlink/junction/reparse point;
- rejects POSIX symlinks in the existing controller chain;
- rejects Windows junction/reparse components using `st_file_attributes`;
- resolves existing components and proves they remain descendants of the selected canonical root;
- validates the nearest existing parent before allowing creation of a missing controller descendant.

The following core lifecycle paths now derive through that primitive:

- `.aiverse` metadata root;
- `.aiverse/generations`;
- active generation pointer;
- individual immutable generation paths;
- generation commit destination;
- generation activation state.

## 4. Compatibility-layer integration

The repair follows the repository's existing `apply_*` composition pattern instead of introducing a parallel lifecycle architecture.

`installer/controller_containment.py` binds the controller containment rule into supported lifecycle surfaces, including:

- legacy controller manifest access;
- setup state;
- integration state;
- learning state;
- learning staging;
- destructive generation retention/purge.

`installer/aiverse_skills.py` applies this compatibility layer as part of the established public Skills composition.

This keeps the fix architecture-preserving and avoids opportunistic changes to unrelated lock, retention-lease or release-identity behavior.

## 5. Destructive purge containment

The public generation purge path now obtains the generation root through the confined controller primitive and validates each generation entry through the same generation-path boundary before recursive removal.

A redirected `.aiverse` or `.aiverse/generations` therefore fails closed before `shutil.rmtree` can operate on external data.

External-sentinel regressions prove the rejected purge does not delete the redirected external content.

## 6. Permanent adversarial regressions

`tests/test_generation_lifecycle.py` now includes permanent containment attacks covering:

- redirected `.aiverse` controller root;
- redirected `.aiverse/generations`;
- commit-stage attempts through redirected controller state;
- status reads through redirected controller state;
- destructive public purge through redirected generation storage;
- learning state through redirected controller storage.

The tests require external sentinel data to survive rejected operations.

On Windows, the test helper creates real directory junctions with:

`cmd /c mklink /J`

The Windows path is therefore exercising reparse/junction behavior rather than skipping the attack class.

## 7. CI correction preserved as evidence

An early repair head exposed a portability issue in the existing interruption regression on macOS.

The failing comparison used two lexical spellings of the same physical path:

- `/var/...`;
- `/private/var/...`.

The new containment attacks themselves passed. The interruption test failed because its mocked pointer swap compared lexical paths and therefore did not trigger on macOS.

That head was not merged.

The regression was corrected to compare resolved physical paths. This preserved the interruption test while avoiding a false platform-specific mismatch.

Final corrected PR head:

`62b49d6420a6034fd08c47c2070ec473f128a392`

## 8. Final PR-head acceptance

All four relevant workflow families passed on the final reviewed PR head.

### Validate AI-Verse Skills

Run `35192350269`: **SUCCESS**

### Lifecycle Controller Containment

Run `35192350296`: **SUCCESS**

Matrix result: **6 / 6 jobs green**

- Ubuntu Python 3.9;
- Ubuntu Python 3.12;
- macOS Python 3.9;
- macOS Python 3.12;
- Windows Python 3.9;
- Windows Python 3.12.

Windows Python 3.9 job `105107547111` explicitly ran all 10 immutable lifecycle/controller tests, including the new junction, redirected-controller and purge-sentinel attacks, and reported:

- `Ran 10 tests`;
- `OK`.

### Runtime Readiness

Run `35192350294`: **SUCCESS**

All six Ubuntu/macOS/Windows x Python 3.9/3.12 jobs passed.

### Full E2E Install

Run `35192350298`: **SUCCESS**

The real journey passed:

- registry/generation validation;
- full pinned upstream install;
- capability-provider validation;
- setup and integrity doctor;
- immutable generation pin/copy;
- immutable update;
- pointer-only rollback;
- uninstall while preserving pinned generation;
- recovery.

## 9. Merge integrity

Skills PR #15 merged as:

`3541d2a7af1b20ca12736ed7454d119295d8e193`

Final reviewed PR head:

`62b49d6420a6034fd08c47c2070ec473f128a392`

Both the PR head and merged commit resolve to the same product tree:

`3e5f72ed405aec0cc015afb52a98505178cf0c3f`

Immediately after merge, the Skills repository had zero open pull requests.

This establishes that the merged product tree is the product tree that passed the final PR-head gates.

## 10. Post-merge main recheck

The merged main SHA `3541d2a7af1b20ca12736ed7454d119295d8e193` triggered and passed the full relevant main workflow set:

- Lifecycle Controller Containment run `35201821336`: **SUCCESS**;
- Runtime Readiness run `35201821346`: **SUCCESS**;
- Full E2E Install run `35201821359`: **SUCCESS**;
- Validate AI-Verse Skills run `35201821414`: **SUCCESS**.

Therefore closure does not rely only on PR-head evidence. The repaired merged main was independently exercised after merge.

## 11. A1.5 standalone Skills recheck

Original WSA-016 condition:

`selected Skills root -> unvalidated root/.aiverse controller -> lifecycle/generation/retention path may resolve outside selected root`

Repaired condition:

`selected Skills root -> controller_path physical containment -> reject symlink/junction/reparse indirection -> all supported controller/generation/state paths derive through that boundary -> destructive purge validates before recursive removal`

The original mechanism is no longer present at the repaired exact ref.

**WSA-2026-016 closure criteria are satisfied.**

This finding-specific recheck does not close or weaken:

- `WSA-2026-017` lifecycle-lock stale-holder liveness;
- `WSA-2026-018` active-generation retention/in-use protection;
- `WSA-2026-019` release/bootstrap identity.

## 12. A3.10 lifecycle/recovery recheck

A3.10 contradiction `C-A3.10-001` grouped four destructive lifecycle BLOCKERs:

- WSA-006 Gateway;
- WSA-012 Memory;
- WSA-016 Skills;
- WSA-029 Connections.

After R0.1 through R0.3:

- Gateway WSA-006: CLOSED;
- Memory WSA-012: CLOSED;
- Skills WSA-016: CLOSED;
- Connections WSA-029: OPEN.

The Skills branch of the destructive lifecycle contradiction is therefore resolved.

A3.10 remains **PARTIAL** because Connections WSA-029 and other lifecycle/recovery findings remain open, including the two-system acceptance gap WSA-049.

## 13. A4.1 adversarial security/path recheck

A4.1 contradiction `C-A4.1-003` includes WSA-016 in the owner-root confinement family.

For Skills controller state, the previously proven attack class is now closed:

- redirected `.aiverse`: rejected;
- redirected generation store: rejected;
- redirected learning state: rejected;
- commit through redirected controller: rejected;
- status through redirected controller: rejected;
- destructive purge through redirected generation store: rejected;
- external sentinel preservation: proven;
- Windows junction/reparse equivalents: proven by hosted Windows jobs.

A4.1 overall remains **FAILED** because other path/security findings remain open, including WSA-009, WSA-029, WSA-033 and WSA-039.

## 14. Finding transition

Canonical state transition:

`OPEN -> CLOSED`

Closure basis:

- one shared controller-path containment primitive now exists;
- all relevant lifecycle controller/generation/state paths are routed through it;
- unsafe symlink/junction/reparse indirection fails closed;
- destructive purge validates confinement before recursive deletion;
- permanent external-sentinel regressions cover the original failure family;
- Ubuntu/macOS/Windows x Python 3.9/3.12 containment matrix passes;
- Runtime Readiness passes across the same supported matrix;
- repository validation passes;
- full install/update/rollback/uninstall/recovery E2E passes;
- the tested PR tree is exactly the merged product tree;
- all four relevant post-merge main workflows pass;
- A1.5, A3.10 and A4.1 finding-specific rechecks no longer reproduce WSA-016.

Post-transition counts:

- total historical findings: **63**;
- OPEN: **60**;
- CLOSED: **3**;
- historical BLOCKER findings: **4**;
- remaining OPEN BLOCKERs: **1**.

Remaining OPEN BLOCKER:

- `WSA-2026-029` Connections destructive purge containment.

Overall whole-system verdict remains:

**NO-GO**

## 15. Next repair

The dependency-safe next repair is:

`R0.4 / WSA-2026-029 - AI-Verse-Connections destructive purge containment`

No implementation of WSA-2026-029 is included in this closure packet.
