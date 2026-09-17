# Repair R0.4 - WSA-2026-029 Connections Destructive Purge Containment

**Repair date:** 2026-09-17  
**Finding:** `WSA-2026-029`  
**Severity:** BLOCKER  
**Owner:** `AI-Verse-Connections`  
**Original audited ref:** `baaac641558dbff1c2eabb0b5ec785a633f49a5b`  
**Live pre-repair ref:** `53b62bc636b9f1f367073c977050d12faf6509ec`  
**Repair PR:** `AI-Verse-Connections#2`  
**Final repair PR head:** `c4bb77f680298d91ce619db91a39d69daaaa76a8`  
**Merged repair ref:** `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`  
**Status:** **CLOSED**

## 1. Original failure

Connections accepted an arbitrary state home from the public service constructor or `AIVERSE_CONNECTIONS_HOME`.

The destructive lifecycle path was:

`configured home -> StateStore.purgeAll() -> fs.rm(this.home, { recursive: true, force: true })`

There was no durable Connections ownership marker, no canonical-realpath ownership binding, no broad-root refusal and no bounded known-child deletion.

A typo or unsafe lifecycle invocation could therefore recursively erase unrelated user data.

The live pre-repair ref `53b62bc636b9f1f367073c977050d12faf6509ec` had zero changed files from the audited product ref `baaac641558dbff1c2eabb0b5ec785a633f49a5b`, so the audited failure remained materially unchanged at repair start.

## 2. Repair contract

Closure required:

1. durable Connections ownership evidence;
2. ownership bound to the exact canonical state-root realpath;
3. rejection of filesystem roots, broad user/system roots and foreign homes;
4. rejection of missing, malformed, wrong or copied ownership markers;
5. rejection of an exact home that is a symlink/junction target;
6. no recursive deletion of an arbitrary configured root;
7. deletion limited to known Connections-owned children;
8. preservation of unexpected/unowned children;
9. a safe path for a fresh custom Connections home;
10. a narrow upgrade route for recognizable legacy Connections state;
11. permanent negative regressions for the original destructive class.

## 3. Implemented repair

At merged Connections ref `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`, `src/state-store.js` now defines persistent `ownership.json` evidence containing:

- ownership schema version;
- `componentId: ai-verse-connections`;
- exact `rootRealpath`;
- creation/update timestamps.

The state root is normalized and inspected before ownership is accepted. Destructive or owner-state operations reject broad roots including filesystem root, the user home, the user-home parent, temporary root and common system locations.

The exact selected Connections home may not itself be a symlink/junction target. The ownership marker must be a regular file, must identify Connections, and its recorded realpath must equal the current canonical realpath. Copying a valid marker to a second directory therefore does not transfer purge authority.

## 4. Install and legacy ownership

`install()` now calls `StateStore.claimHome()` before publishing lifecycle state.

A home may be claimed only when:

- it is newly created/empty; or
- it is a recognizable legacy Connections home containing only known legacy state entries and a valid legacy lifecycle state structure.

A non-empty unrelated directory fails closed and is not silently converted into a Connections-owned root.

Recognizable legacy state receives the new persistent exact-root ownership marker so existing legitimate installations can move forward without destructive migration.

## 5. Bounded purge

The original whole-root recursive erase has been removed.

`purgeAll()` now:

1. proves exact root ownership;
2. enumerates the root;
3. removes only known Connections-owned state:
   - `lifecycle.json`;
   - `registry.json`;
   - `credentials.enc.json`;
   - `receipts.ndjson`;
   - `.write.lock`;
   - known atomic temporary JSON files;
   - `ownership.json` last;
4. preserves every unknown/unowned child;
5. removes the root directory only when it is empty after bounded owner cleanup.

If a known owned child is itself a symlink, the link is unlinked rather than recursively followed.

A purge result reports whether the root was removed and which unknown entries were preserved.

## 6. Permanent regressions

Two permanent regression files were added:

- `test/connections-lifecycle-containment.integration.test.js`;
- `test/connections-purge-foreign.integration.test.js`.

They cover:

1. unrelated non-empty home cannot be claimed;
2. recognizable legacy home receives exact ownership evidence;
3. missing ownership marker fails closed;
4. wrong/foreign marker fails closed;
5. copied marker cannot authorize another root;
6. filesystem root/user home/user-home parent/temp root are refused;
7. safe owned custom purge succeeds;
8. unknown sentinel data is preserved by bounded purge;
9. exact Connections home symlink or Windows junction is refused;
10. direct destructive purge of a foreign non-empty home is refused.

The directory-link regression uses a POSIX directory symlink and requests a Windows `junction` when executed on Windows.

## 7. Exact repair-head validation

The final repaired PR head was:

`c4bb77f680298d91ce619db91a39d69daaaa76a8`

Exact repaired lifecycle validation performed independently of unavailable hosted runners established:

- `StateStore` syntax check: PASS;
- destructive lifecycle adversarial harness: **10 / 10 PASS**;
- actual lifecycle `install -> setup -> uninstall({purge:true})`: PASS;
- safe custom owned purge removed the empty owner root;
- foreign/broad/missing-marker/wrong-marker/copied-marker/link cases failed closed;
- unknown external/user sentinel state survived the bounded purge cases.

This validation exercised the exact destructive boundary repaired by WSA-029.

## 8. Hosted-CI evidence limitation retained as WSA-2026-003

Connections already has a six-job hosted matrix for Ubuntu/macOS/Windows on Node 20/22, but the private-repository Actions infrastructure is still unable to allocate runners.

PR workflow run:

`35219295977`

All six jobs were labeled failed by GitHub, but every job had:

- `steps: []`;
- `runner_id: 0`;
- no runner name;
- no checkout, Node setup or test execution.

This is not a product-test failure.

An unchanged-main run before merge, `35218943165`, showed the same six empty no-runner jobs, proving the condition is inherited infrastructure behavior rather than a repair regression.

Post-merge main run `35219652570` again produced the same six empty no-runner jobs at merged SHA `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`.

Therefore:

- WSA-2026-029 closure does **not** claim hosted Windows/macOS/Linux test execution;
- WSA-2026-003 remains **OPEN** and retains responsibility for hosted-CI evidence availability;
- the no-runner jobs are not reclassified as failed product tests.

## 9. Merge integrity

Connections PR #2 merged as:

`a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`

Comparison from final reviewed PR head `c4bb77f680298d91ce619db91a39d69daaaa76a8` to merged main reports:

- one merge commit ahead;
- **zero changed files**.

Immediately after merge:

- Connections main contains the reviewed product bytes;
- open Connections PRs = 0.

## 10. A1.10 finding-specific recheck

Original destructive path:

`arbitrary configured home -> purgeAll -> recursive force-remove entire home`

Repaired path:

`configured home -> broad/root/link guard -> canonical realpath -> exact Connections ownership proof -> bounded known-owned-child deletion -> preserve unknown children`

The original arbitrary-home recursive purge mechanism no longer exists at the repaired exact ref.

**WSA-2026-029 closure requirements are satisfied.**

This recheck does not close or weaken:

- WSA-2026-030 installation/system binding;
- WSA-2026-031 MCP credential-origin binding;
- WSA-2026-032 final-edge lifecycle/budget authority;
- WSA-2026-033 normalized path authorization;
- WSA-2026-051 DNS/private-network containment;
- WSA-2026-054 through WSA-2026-057 or WSA-2026-059.

## 11. A3.10 lifecycle/recovery recheck

Contradiction `C-A3.10-001` grouped four destructive lifecycle containment BLOCKERs:

- WSA-006 Gateway: CLOSED;
- WSA-012 Memory: CLOSED;
- WSA-016 Skills: CLOSED;
- WSA-029 Connections: CLOSED by this repair.

Therefore the destructive lifecycle containment branch of A3.10 is now fully resolved.

A3.10 overall remains **PARTIAL** because other lifecycle/recovery/concurrency findings and the two-system acceptance finding WSA-049 remain open.

## 12. A4.1 adversarial security/path recheck

For the Connections destructive-purge class:

- filesystem/broad paths: rejected;
- foreign non-empty roots: rejected;
- missing ownership marker: rejected;
- wrong/foreign marker: rejected;
- copied marker: rejected by realpath binding;
- exact home symlink/junction: rejected;
- safe custom owned root: supported;
- unknown/unowned data inside an owned root: preserved;
- arbitrary whole-root recursive deletion: removed.

The WSA-029 branch of owner-root contradiction `C-A4.1-003` is resolved.

A4.1 overall remains **FAILED** because other path, authority, authentication and network findings remain open, including WSA-009, WSA-033, WSA-039, WSA-050 and WSA-051.

## 13. Finding transition and R0 exit

Canonical transition:

`WSA-2026-029: OPEN -> CLOSED`

Post-transition finding counts:

- historical findings: **63**;
- OPEN: **59**;
- CLOSED: **4**;
- historical BLOCKER findings: **4**;
- remaining OPEN BLOCKER findings: **0**.

Phase R0 destructive-containment BLOCKER repair is therefore:

**4 / 4 CLOSED = 100% COMPLETE**

Overall whole-system verdict remains **NO-GO**. Later repair waves and the bounded final independent recheck are still mandatory.

## 14. Next repair

The dependency-safe next task is:

`R1.1 / WSA-2026-009 - AI-Verse-Brain physical host-root containment`

No implementation of WSA-009 is included in this repair or closure packet.
