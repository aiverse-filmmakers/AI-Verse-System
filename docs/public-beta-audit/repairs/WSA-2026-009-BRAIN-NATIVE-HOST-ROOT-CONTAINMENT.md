# Repair R1.1 - WSA-2026-009 Brain Native Host-Root Containment

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-009`  
**Severity:** HIGH  
**Owner:** `AI-Verse-Brain`  
**Original audited / live pre-repair ref:** `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`  
**Repair branch:** `repair/wsa-2026-009-native-root-containment`  
**Repair PR:** `AI-Verse-Brain#24`  
**Final tested PR head:** `f35a3f683f9014bbe3b508af341c09992ae2c1c3`  
**Merged repair ref:** `908f9a9a06c2b12204ada7f71cd761bae97b52ce`  
**Reviewed/merged product tree:** `66b650a63879898b936b7c8c550d10654caed366`  
**Status:** **CLOSED**

## 1. Original failure

Brain's native host discovery accepted `operator/` and `workspaces/` through ordinary directory checks. A directory symlink or Windows junction could therefore redirect one of those parents outside the selected AI-Verse root.

Later state containment was evaluated relative to those already-resolved redirected parents. Canonical state, initialization, runtime locks, installation markers and standalone-to-native adoption could consequently write outside the selected authority boundary while appearing locally valid.

The exact audited/live pre-repair ref remained `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4`, with zero open Brain repair PRs at repair start.

## 2. Repair contract

Closure required:

1. reject symlinked or junction/reparse native `operator` and `workspaces` parents;
2. physically confine operator and workspace Brain state to the selected host root;
3. reject a redirected individual workspace before deriving its Brain state;
4. physically confine native runtime paths and runtime locks;
5. physically confine initialization and installation-marker paths;
6. physically confine standalone-to-native adoption transaction, staging, retirement and destination paths;
7. revalidate physical targets immediately before mutation rather than trusting an earlier plan;
8. preserve safe first-install creation of missing descendants after the nearest existing parent is proven safe;
9. add permanent POSIX symlink and real Windows junction regressions with external sentinels;
10. leave WSA-2026-010 Goal concurrency and WSA-2026-011 release identity unchanged.

## 3. Shared physical-containment primitive

Merged Brain adds `engine/aiverse_brain/path_safety.py` as the shared native path guard.

`safe_host_path(...)`:

- canonicalizes the selected host root;
- requires the selected host root to be an existing directory;
- validates every supplied path component as one path segment;
- walks each existing component with `lstat`;
- rejects POSIX symbolic links;
- rejects Windows junction/reparse points through `st_file_attributes & 0x0400`;
- strictly resolves existing components and proves they remain beneath the selected canonical root;
- requires existing intermediate components to be directories;
- permits missing descendants only after the nearest existing parent has passed the physical containment check;
- can require a final directory or regular file when the caller needs stronger existence/type proof.

`validate_native_host_parents(...)` applies the same law to the native `operator` and `workspaces` roots.

## 4. Host discovery and scope confinement

`inspect_host(...)` now rejects a native-looking OS v2 layout when either `operator` or `workspaces` is redirected through a symlink/junction/reparse point. Such a layout becomes `INCOMPATIBLE_AI_VERSE` and is not permitted to fall back to standalone Brain state.

`native_path_contract(...)` and `StorageLayout` now derive native Brain paths through the shared guard:

- operator state: `operator/brain`;
- workspace state: `workspaces/<id>/brain` only after `workspaces/<id>` is proven to be the real in-root workspace directory;
- runtime: `runtime/ai-verse-brain/...`.

A redirected individual workspace therefore fails before Brain state is created or read through it.

## 5. Runtime and lock containment

ObjectStore runtime lock paths now use `StorageLayout.runtime_path(...)` rather than a raw runtime directory.

`RuntimeKeyLock` additionally revalidates the native runtime root immediately before lock mutation and re-derives `runtime/ai-verse-brain/locks/<namespace>` through the physical guard. A later replacement of `runtime`, `ai-verse-brain`, or `locks` with a symlink/junction cannot redirect lock creation outside the selected system.

## 6. Initialization and installation markers

Native initialization state and runtime paths, plus `operator/brain/installation.json`, are derived through the same guard.

`plan_init(...)` reports unsafe physical paths as blockers. `initialize(...)` then re-resolves the protected paths immediately before filesystem mutation so an earlier plan is not treated as continuing filesystem authority.

An existing native installation marker must be a regular, non-link file inside the contained native Brain state path.

## 7. Standalone-to-native adoption

Brain adoption now physically confines:

- the standalone `.ai-verse-brain` source;
- native `operator/brain` destination;
- `.aiverse/brain-adoption` controller directory;
- adoption transaction file;
- retirement snapshot;
- staging directory;
- native runtime destination.

The paths are revalidated between adoption phases. A redirected native destination or redirected adoption controller fails before the standalone source is retired, preserving the old canonical source and external sentinel data.

## 8. Permanent adversarial regressions

`tests/test_native_path_containment.py` adds ten WSA-009 cases:

1. redirected `operator` parent makes the native host incompatible and blocks initialization;
2. redirected `workspaces` parent makes the native host incompatible and blocks initialization;
3. redirected `workspaces/<id>` blocks workspace Brain state and path-contract derivation;
4. redirected `operator/brain` blocks initialization and installation-marker write;
5. redirected `runtime` blocks initialization;
6. redirected `runtime/ai-verse-brain` blocks initialization;
7. redirected nested runtime `locks` blocks runtime-key mutation;
8. linked native `installation.json` is rejected;
9. redirected adoption operator destination is refused before retiring standalone source;
10. redirected adoption transaction parent is refused before any external transaction write.

Directory attacks use a POSIX directory symlink on Linux/macOS and a real `cmd /c mklink /J` directory junction on Windows. Every applicable external-path attack uses sentinel data to prove the rejected operation did not mutate the external target.

The ordinary file-symlink marker regression is skipped on Windows only because creating ordinary file symlinks is not reliably permitted on hosted Windows runners. Windows still executes the corresponding parent/directory escape class with real junctions.

## 9. PR-head acceptance

Final tested Brain PR head:

`f35a3f683f9014bbe3b508af341c09992ae2c1c3`

PR-head workflows:

- CI run `35228628402`: **SUCCESS**;
  - package-smoke: SUCCESS;
  - Ubuntu Python 3.9: SUCCESS;
  - Ubuntu Python 3.12: SUCCESS;
  - macOS Python 3.9: SUCCESS;
  - macOS Python 3.12: SUCCESS;
  - Windows Python 3.9: SUCCESS;
  - Windows Python 3.12: SUCCESS;
- Skills Receipt Contract run `35228628604`: **SUCCESS**;
- OS Direction Ownership Contract run `35228628938`: **SUCCESS**.

Observed detailed legs:

- Windows Python 3.12 job `105226554049`: 237 tests completed successfully, with nine executable WSA-009 junction/path attacks passing and only the ordinary file-symlink test intentionally skipped;
- macOS Python 3.12 job `105226553976`: 237 / 237 tests passed, including all ten WSA-009 containment attacks.

## 10. Merge integrity

Brain PR #24 was squash-merged only after the reviewed exact head was green.

Merged Brain ref:

`908f9a9a06c2b12204ada7f71cd761bae97b52ce`

The final PR head and merged commit both have product tree:

`66b650a63879898b936b7c8c550d10654caed366`

Therefore the tested Brain tree is byte-for-byte the merged Brain tree.

Open Brain PRs after merge: **0**.

## 11. Merged-main recheck

Post-merge Brain `main` workflows on `908f9a9a06c2b12204ada7f71cd761bae97b52ce`:

- CI run `35228849333`: **SUCCESS**, all seven jobs including package smoke and all six Ubuntu/macOS/Windows Python matrix legs;
- Skills Receipt Contract run `35228849545`: **SUCCESS**;
- OS Direction Ownership Contract run `35228849499`: **SUCCESS**.

The supported cross-platform state therefore remains green on the actual merged product ref.

## 12. Finding-specific rechecks

### A1.3 standalone Brain recheck

The original failure mechanism was:

`selected root -> symlink/junction operator/workspaces parent -> already-resolved outside parent -> Brain state/runtime/install/adoption write outside selected root`

The repaired mechanism is:

`selected root -> walk every existing native Brain path component -> reject symlink/junction/reparse -> prove physical containment -> revalidate before mutation`

The WSA-009 escape mechanism no longer exists at the merged exact ref.

**A1.3 finding-specific result: PASS for WSA-2026-009 only.**

WSA-2026-010 and WSA-2026-011 remain OPEN.

### A3.2 existing-system adoption recheck

The Brain destination-scope branch of `C-A3.2-005` is resolved:

- redirected native parents fail host compatibility;
- redirected destination fails before standalone authority retirement;
- adoption transaction/staging paths are physically confined;
- external sentinels survive rejected attacks.

A3.2 remains PARTIAL overall because other migration/authority findings, including WSA-2026-013, WSA-2026-014 and WSA-2026-047, remain open.

### A4.1 adversarial path recheck

The Brain branch of owner-root contradiction `C-A4.1-003` is resolved for this finding. Operator, workspaces, individual workspace, state, runtime, runtime-lock, marker and adoption redirections fail closed under supported platform tests.

A4.1 remains FAILED overall because other security/path findings remain, including WSA-2026-033, WSA-2026-039, WSA-2026-050, WSA-2026-051 and other authority findings.

## 13. Finding transition

Canonical transition:

`WSA-2026-009: OPEN -> CLOSED`

Post-transition finding counts:

- historical findings: **63**;
- OPEN: **58**;
- CLOSED: **5**;
- remaining OPEN BLOCKERs: **0**.

R1 trusted-boundary phase progress after this closure:

**1 / 13 CLOSED = 7.69%**

Overall whole-system verdict remains **NO-GO**. The remaining repair waves and bounded final independent recheck are still mandatory.

## 14. Next repair

The dependency-safe next task is:

`R1.2 / WSA-2026-020 - AI-Verse-Data trusted scope provenance`

No implementation of WSA-2026-020 is included in this repair or closure packet.
