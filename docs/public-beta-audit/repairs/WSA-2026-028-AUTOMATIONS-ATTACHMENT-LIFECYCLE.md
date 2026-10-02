# WSA-2026-028 Closure - Automations Attachment Lifecycle Reconciliation

**Finding:** `WSA-2026-028`  
**Severity / confidence:** MEDIUM / PROVEN  
**Owner:** `AI-Verse-Automations`  
**Repair wave:** R2.5  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Automations could attach an OS extension registry entry and owner bridge, but component lifecycle and host discovery truth could diverge afterward.

At the audited baseline:

- component disable could leave registry `enabled:true`;
- component enable could coexist with preserved registry `enabled:false`;
- uninstall left the registry entry and bridge files installed;
- status did not represent the attachment lifecycle.

The bridge itself checked owner readiness, so the main impact was host discovery/lifecycle contradiction rather than residual execution authority.

Canonical contradiction: `C-A1.9-003`.

## 2. Baseline and repair identity

**Pre-repair Automations ref:** `017eaf3e74d604208c606cc08f4137006f723625`  
**Open Automations PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-028-attachment-lifecycle`  
**Repair PR:** `AI-Verse-Automations#6`  
**Final tested PR head:** `edd096f51523659c3aae899008567ef291f1b15e`  
**Merged Automations ref:** `287ce9d6718ef06e4589a2a3e767c6a9ba376755`  
**Tested/merged product tree:** `9791f8bd1c0c3a2aaf262d76809dd1c440d05a66`

Open Automations PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Component lifecycle is authoritative for attached enable state

When an Automations OS extension is attached, component `enable` and `disable` synchronize the registry entry's `enabled` field.

`attach-os` also derives the resulting enabled field from the current component state rather than preserving a divergent registry value.

### 3.2 Synchronization preserves the existing registry safety boundary

Registry reconciliation reuses the pre-existing safety model:

- fixed registry path;
- path containment and symlink-chain rejection;
- exclusive `registry.json.lock`;
- no lock stealing;
- raw registry text lost-update detection before replacement;
- atomic registry replacement;
- preservation of unrelated top-level fields and extension entries.

Lifecycle configuration mutation is rolled back if synchronized registry mutation cannot acquire the registry lock.

### 3.3 Unattached standalone lifecycle stays side-effect free

Enable/disable/setup do not create `.aiverse/extensions` merely to synchronize a component that has never been attached.

A clean detached installation remains a valid standalone owner state.

### 3.4 Status and doctor expose attachment truth

Lifecycle descriptor now includes attachment truth:

- attached / installed;
- registry enabled state;
- exact owned bridge-file presence;
- consistency with component enabled state.

A discovered attachment mismatch becomes unhealthy rather than silently reporting ready/disabled.

Doctor includes a critical `os-extension-attachment` check using the same status truth.

### 3.5 Uninstall detaches replaceable integration state but preserves canonical data

Uninstall first disables the component owner, then safely detaches the OS integration.

For a valid owned attachment it:

- removes the Automations registry entry;
- removes the exact generated owner engine file;
- removes the exact generated instructions file;
- removes the now-empty extension-owned directory when possible;
- preserves the canonical SQLite database and automation/run definitions.

Unrelated registry fields and other extension entries remain untouched.

### 3.6 Destructive attachment cleanup remains ownership-bound

Detachment validates:

- extension ID and source;
- state-directory digest binding;
- installed/supported state;
- safe non-symlink bridge paths;
- exact generated bridge-file content.

Modified or unsafe bridge files are not deleted.

### 3.7 Reinstall requires explicit reattachment

After uninstall:

- canonical SQLite state remains;
- setup can restore component readiness without automatically materializing host integration;
- status reports detached;
- explicit `attach-os` recreates the current bridge and registration.

This keeps attachment explicit while making lifecycle authoritative whenever an attachment exists.

## 4. Permanent regressions

The owner suite now proves:

1. attach preserves unrelated registry data;
2. attachment can execute the atomic owner bridge;
3. existing registry locks are never stolen;
4. divergent registry enabled state makes component status unhealthy;
5. attach reconciles the enabled field back to component truth;
6. attached disable writes registry `enabled:false`;
7. attached enable writes registry `enabled:true`;
8. uninstall removes the Automations registry entry;
9. uninstall removes exact generated bridge files;
10. uninstall preserves the SQLite database;
11. setup after uninstall remains detached;
12. explicit reattach recreates the bridge and enabled registration;
13. enable/disable rolls back component state when the registry lock is busy;
14. uninstall rolls back the temporary component disable when the registry lock is busy;
15. unrelated registry fields and other extension entries survive disable/uninstall;
16. doctor exposes manual component/registry divergence as unhealthy.

## 5. Validation evidence

### Final PR-head acceptance

PR-head workflow:

`37050123823`

On exact final head `edd096f51523659c3aae899008567ef291f1b15e`:

- Ubuntu Python 3.11/3.12/3.13: **PASS**
- macOS Python 3.11/3.12/3.13: **PASS**
- Windows Python 3.11/3.12/3.13: **PASS**
- total matrix: **9 / 9 PASS**
- representative suite: **51 / 51 passed**

### Post-merge acceptance

Merged-main workflow:

`37050285820`

On merged Automations `main` ref `287ce9d6718ef06e4589a2a3e767c6a9ba376755`:

- all 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs: **PASS**
- representative suite: **51 / 51 passed**

The tested PR-head tree and merged-main tree are identical:

`9791f8bd1c0c3a2aaf262d76809dd1c440d05a66`

## 6. Finding-specific recheck

### C-A1.9-003

**RESOLVED for WSA-2026-028.**

Attached host discovery state now follows component lifecycle, and inconsistent/tampered attachment state is visible as unhealthy.

### Enable/disable reconciliation

**PASS.**

Registry enabled state follows component state under the existing registry serialization boundary.

### Uninstall/detach

**PASS.**

Replaceable integration files and registry truth are removed while canonical SQLite state is retained.

### Reinstall

**PASS.**

Setup restores component state without silently reattaching. Explicit attach recreates current integration state.

### Failure/rollback

**PASS.**

Busy registry lock prevents synchronization and restores prior component lifecycle state.

### A2.3 lifecycle graph

**RESOLVED for the WSA-2026-028 component/attachment branch.**

### A3.10 lifecycle/recovery

**RESOLVED for the WSA-2026-028 uninstall/reinstall attachment branch.**

## 7. Wave transition

This closure completes Wave R2:

- R2.1 WSA-2026-007: CLOSED
- R2.2 WSA-2026-013: CLOSED
- R2.3 WSA-2026-026: CLOSED
- R2.4 WSA-2026-027: CLOSED
- R2.5 WSA-2026-028: CLOSED

**R2: 5 / 5 CLOSED = 100%.**

The next dependency-safe repair is:

`R3.1 / WSA-2026-008 - Gateway state linearizability`.

The whole-system verdict remains **NO-GO**.

## 8. Closure verdict

Required WSA-2026-028 behavior is present on merged Automations `main`:

- attached enable/disable follows component truth;
- attach reconciles divergent registration state;
- status and doctor expose attachment consistency;
- synchronization uses lock + lost-update controls;
- lifecycle rolls back on busy attachment lock;
- standalone detached lifecycle remains side-effect free;
- uninstall removes replaceable OS integration state;
- canonical SQLite state is preserved;
- reinstall/reattach behavior is explicit and proven;
- all 9 exact-head CI jobs pass;
- all 9 merged-main CI jobs pass;
- representative suite is 51 / 51;
- tested and merged product trees are identical;
- open Automations PRs are zero.

**WSA-2026-028: CLOSED.**
