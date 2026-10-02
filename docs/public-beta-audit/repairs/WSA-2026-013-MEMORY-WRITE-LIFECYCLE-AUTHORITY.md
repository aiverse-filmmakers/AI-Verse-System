# WSA-2026-013 Closure - Memory Write Authority vs Lifecycle

**Finding:** `WSA-2026-013`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Memory`  
**Repair wave:** R2.2  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Native Memory canonical mutation did not consume current component lifecycle authority.

The shared writable-authority hook enforced retired standalone authority, but native mode returned without checking whether Memory was currently:

- supported by the local extension registry;
- installed;
- attached;
- enabled;
- setup-complete;
- blocked in migration-required state.

Because already-loaded Memory code could still reach canonical mutation APIs directly, native writes could occur before setup, after disable, after detach, after uninstall, or while an unresolved legacy authority handoff required migration.

Canonical contradiction: `C-A1.4-002`.

Required closure evidence:

- native canonical writes consume authoritative local extension/setup state;
- normal writes require supported + installed + attached + enabled + setup-complete;
- migration-required allows only explicitly admitted migration/recovery writes;
- lifecycle bootstrap uses a narrow explicit exception rather than a global native bypass;
- canonical atomics, session digests, promotion and metadata mutation fail before setup and after disable/detach/uninstall.

## 2. Baseline and repair identity

**Pre-repair Memory ref:** `7a1ed5777fd11616375501d730fcbd488beff8b8`  
**Open Memory PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-013-native-write-lifecycle-authority`  
**Repair PR:** `AI-Verse-Memory#31`  
**Final tested PR head:** `d998cb2612b42d11727d39429fb45b3b11999062`  
**Merged Memory ref:** `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904`  
**Tested/merged product tree:** `4444ff070fd55c604a80c072081068bb265ccde6`

The exact tested PR head and merged `main` commit have the same product tree.

Open Memory PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Native lifecycle authority is consumed at the canonical mutation gate

The existing shared writable-authority hook is now authoritative in native mode instead of returning early.

For native canonical writes it reads current owner lifecycle evidence from:

1. `.aiverse/extensions/registry.json`;
2. the Memory component receipt at `operator/memory/.ai-verse-memory-state/component.json`;
3. current Memory migration/authority-handoff evidence.

Normal native canonical mutation now requires:

- the `ai-verse-memory` registry entry exists;
- registry `supported === true`;
- registry `installed === true`;
- current registry membership proves attachment;
- registry `enabled === true`;
- component receipt `installed === true`;
- component receipt `enabled === true`;
- component receipt `setup_completed === true`;
- no unresolved migration-required condition.

Missing, malformed or contradictory lifecycle evidence fails closed.

### 3.2 Loaded source is not write authority

Lifecycle state is read at mutation admission time.

The presence of an imported/loaded Memory module or preserved canonical data does not grant write authority.

Permanent regressions prove the same already-loaded Memory object is denied:

- after package install but before setup;
- after disable;
- after detach;
- after uninstall;
- after reinstall but before setup.

Normal uninstall still preserves canonical Memory data as designed, but preserved data is read-only until lifecycle authority is re-established.

### 3.3 Registry flags are authoritative

The repair proves registry state is not advisory metadata.

With an otherwise valid setup:

- `supported=false` blocks canonical mutation;
- `installed=false` blocks canonical mutation;
- restoring both to the admitted state restores write admission.

Enabled state is also required at both registry and component-receipt layers.

### 3.4 Migration-required is a real write fence

Native migration-required state now blocks ordinary canonical mutation.

The migration-required computation checks:

- the native authority handoff;
- any reviewed legacy migration plan whose handoff is incomplete;
- any legacy `.ai-verse-memory` canonical route that has not been retired under the matching handoff.

Ordinary writes fail while that authority conflict exists.

### 3.5 Migration uses a narrow explicit intent

The repair does not restore a broad native-mode bypass for migration.

Only explicit migration/recovery entry points call the same authority guard with:

`intent="migration"`

That intent still requires the base native lifecycle state to be supported, installed, attached, enabled and setup-complete.

It bypasses only the migration-required prohibition necessary to perform the migration/handoff itself.

This is deliberately narrow and does not close or redesign `WSA-2026-014` migration atomicity.

### 3.6 Standalone retirement semantics are preserved

Standalone mode keeps the existing retired-authority contract.

A retired standalone store remains preserved as historical evidence and rejects canonical writes after authority has moved to the adopted OS root.

### 3.7 Canonical mutation surfaces inherit the shared gate

The existing mutation architecture routes canonical mutation through the shared writable-authority boundary.

The closure regressions directly cover:

- atomic Memory writes;
- session-digest writes;
- metadata mutation;
- session-digest promotion.

Existing supersession/forget/correction paths continue to use the same canonical mutation gate.

### 3.8 Same-process serialization preserves the existing durable lock contract

Admitting realistic lifecycle-ready fixtures exposed a Windows Python 3.12 contention stall in an existing same-process concurrent-writer regression.

The final repair preserves the established serialization law by adding a per-path in-process mutex in front of the existing durable mutation file lock.

This does not replace or weaken the cross-process lock.

The durable file lock remains responsible for:

- cross-process exclusion;
- stale-owner detection;
- dead-owner recovery;
- transaction recovery;
- durable mutation serialization.

Reentrant same-thread behavior remains supported through the existing thread-local lock count.

The cross-platform concurrent-writer regression is green on the final head.

## 4. Permanent regressions

Dedicated WSA-2026-013 coverage was added to `tests/test_component_lifecycle.py`.

It proves:

1. package install without setup cannot write a canonical atom;
2. package install without setup cannot write a session digest;
3. setup establishes valid write authority;
4. disable blocks atomics;
5. disable blocks session digests;
6. disable blocks metadata mutation;
7. disable blocks promotion;
8. detach blocks all four mutation surfaces with the already-loaded Memory module;
9. uninstall blocks all four mutation surfaces with the already-loaded Memory module;
10. reinstall without setup remains write-blocked;
11. preserved canonical data remains discoverable after uninstall/reinstall;
12. registry `supported=false` blocks canonical writes;
13. registry `installed=false` blocks canonical writes;
14. restored admitted registry state restores writes;
15. migration-required blocks ordinary canonical writes;
16. explicit migration planning remains admitted through the narrow migration intent.

Installer smoke now also proves:

- native package install alone rejects `remember`;
- standard component setup is then performed;
- the same canonical write succeeds after setup.

Existing native unit/benchmark fixtures were changed only to establish the lifecycle state that a real admitted native writer now requires.

## 5. Validation evidence

### Final PR-head acceptance

Final PR-head workflow:

`37037225207`

On exact final head `d998cb2612b42d11727d39429fb45b3b11999062`:

- unit tests, Ubuntu Python 3.9: **PASS**
- unit tests, Ubuntu Python 3.12: **PASS**
- unit tests, macOS Python 3.9: **PASS**
- unit tests, macOS Python 3.12: **PASS**
- unit tests, Windows Python 3.9: **PASS**
- unit tests, Windows Python 3.12: **PASS**
- public-beta acceptance, Ubuntu: **PASS**
- public-beta acceptance, macOS: **PASS**
- public-beta acceptance, Windows: **PASS**
- installer smoke, Ubuntu: **PASS**
- installer smoke, Windows: **PASS**
- OS-update integration: **PASS**

Representative unit suite:

- tests run: **127**
- passed: **126**
- failed: **0**
- skipped: **1**

Both dedicated WSA-2026-013 tests passed.

The existing concurrent-writer regression passed on Ubuntu and Windows Python 3.12 on the accepted head.

Representative Windows public-beta lifecycle suite:

- tests run: **19**
- failed: **0**
- skipped: **1**

### Intermediate-run notes

The first repair head exposed expected integration assumptions rather than an authority-gate defect:

- installer smoke attempted a canonical write after package install but before setup;
- synthetic native unit/benchmark fixtures performed canonical writes without lifecycle admission;
- two lock-recovery tests assumed the component-state directory did not already exist.

Those fixtures/smokes were corrected to model the real lifecycle contract.

A later Windows Python 3.12 run exposed a same-process file-lock polling stall after realistic component state was present. The final head adds an in-process serialization mutex while retaining the durable cross-process lock.

None of the failed intermediate heads is the accepted repair head.

### Post-merge acceptance

Post-merge workflow:

`37037623090`

On merged Memory `main` ref `cbc6651d60d42c63015bc1b25b5cd8f0c49d5904`:

- all six Ubuntu/macOS/Windows Python 3.9/3.12 unit jobs: **PASS**
- all three public-beta acceptance jobs: **PASS**
- both installer-smoke jobs: **PASS**
- OS-update integration: **PASS**

Representative merged-main suite:

- tests run: **127**
- passed: **126**
- failed: **0**
- skipped: **1**

Both WSA-2026-013 regressions and the concurrent-writer regression passed after merge.

## 6. Finding-specific recheck

### C-A1.4-002

**RESOLVED for WSA-2026-013.**

Native Memory mutation no longer treats loaded code/source availability as write authority.

### Before setup

**PASS.**

Package installation may stage code/registry metadata, but canonical mutation remains denied until setup-complete owner state is present.

### Disabled

**PASS.**

Current disabled state blocks canonical atomics, session digests, promotion and metadata mutation.

### Detached

**PASS.**

Removing the current local extension registry attachment blocks the already-loaded native writer.

### Uninstalled

**PASS.**

Uninstall removes current write authority even though preserved canonical Memory remains on disk and code may remain loaded in the current process.

### Migration-required

**PASS.**

Ordinary writes are fenced. Explicit migration/recovery intent is the only narrow exception and still requires base lifecycle readiness.

### A2.3 Memory lifecycle/write-admission branch

**RESOLVED for WSA-2026-013 only.**

Memory owner lifecycle state is now consumed at the canonical native mutation boundary.

Other A2.3 lifecycle findings remain independent.

### A3.10 / C-A3.10-002 Memory branch

**RESOLVED for WSA-2026-013 only.**

The lifecycle-vs-write-authority contradiction for Memory is closed.

The Automations lifecycle branch remains OPEN under `WSA-2026-028`.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-013`.

The following remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-014` - Memory migration/handoff atomicity;
- `WSA-2026-015` - Memory release/bootstrap identity;
- `WSA-2026-026` - Automations canonical store ownership;
- `WSA-2026-027` - Automations legacy authority live fence;
- `WSA-2026-028` - Automations attachment/component lifecycle divergence.

The whole-system verdict remains **NO-GO**.

Dashboard MC1.4 and owner dogfood remain paused.

## 8. Closure verdict

Required WSA-2026-013 behavior is present on merged Memory `main`:

- native canonical writes consume current registry and setup authority;
- supported, installed, attached, enabled and setup-complete state is required;
- already-loaded code cannot write before setup or after disable/detach/uninstall;
- registry supported/installed flags are enforced;
- migration-required blocks ordinary writes;
- migration uses a narrow explicit intent instead of a global bypass;
- standalone retirement semantics remain intact;
- atomics, session digests, promotion and metadata mutation are covered;
- same-process serialization remains cross-platform while the existing durable cross-process lock remains authoritative;
- final exact-head 12-job workflow passes;
- post-merge 12-job workflow passes;
- representative unit suite is 127 tests, 126 pass, 0 fail, 1 existing skip;
- tested and merged product trees are identical;
- open Memory PRs are zero.

**WSA-2026-013: CLOSED.**
