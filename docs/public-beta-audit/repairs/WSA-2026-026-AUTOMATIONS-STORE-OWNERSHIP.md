# WSA-2026-026 Closure - Automations Canonical Store Ownership

**Finding:** `WSA-2026-026`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Automations`  
**Repair wave:** R2.3  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

The canonical Automations scheduler store did not prove database ownership or format identity before mutation.

At the audited baseline, `connect()` opened whatever `automations.db` existed in the selected state directory. `initialize()` then ran `CREATE TABLE IF NOT EXISTS`, conditionally altered `runs`, and stamped `meta.schema_version=2`.

A structurally foreign but valid SQLite file could therefore be modified before Automations had proven it owned the file. Lifecycle health also used only generic SQLite integrity, so a SQLite-valid foreign store could be treated as healthy owner state.

Canonical contradiction: `C-A1.9-001`.

Required closure evidence:

- durable Automations SQLite identity and format markers;
- no schema mutation of non-empty foreign SQLite;
- exact required schema/index/version verification before ready;
- migrations admitted only from known compatible prior formats;
- regressions for foreign valid SQLite, wrong version, weakened/missing schema and clean creation.

## 2. Baseline and repair identity

**Pre-repair Automations ref:** `caaed83b98026dd955640fc015d181529b91a1c6`  
**Open Automations PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-026-store-identity`  
**Repair PR:** `AI-Verse-Automations#4`  
**Final tested PR head:** `2fca42703abcb22a54ac55113c3f9e4d6d5e62d5`  
**Merged Automations ref:** `e5ec241f1d86e76b15bab5be81e720a827e4fa09`  
**Tested/merged product tree:** `1c5d09d9c0d287b1eb42f031482c6c0f9819899a`

The exact tested PR head and merged `main` commit have the same product tree.

Open Automations PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 The SQLite file carries durable owner and format identity

Current Automations stores now carry three mutually checked identity layers:

- SQLite `PRAGMA application_id = 0x41564155`;
- SQLite `PRAGMA user_version = 2`;
- canonical `meta.owner_id = ai-verse-automations` plus `meta.schema_version = 2`.

Normal `connect()` requires all current markers.

A path named `automations.db` is not authority by itself.

### 3.2 Required schema is verified before normal access

Current canonical access compares the live database against the exact supported semantic schema.

The validation covers:

- the complete required application table set;
- required columns and their declared types/null/default/primary-key properties;
- required foreign-key bindings;
- required explicit indexes;
- SQLite-generated primary-key/unique indexes, including the unique invocation identity.

Missing, extra or weakened application schema fails closed.

### 3.3 Foreign non-empty SQLite fails before schema mutation

For an existing non-empty database, initialization first performs read-only identity/schema classification.

If the file is not the current Automations format, the exact known unmarked v2 format, or the exact known v1 format, initialization raises before running Automations schema creation, ALTER or metadata stamping.

The dedicated regression creates a valid foreign SQLite database with durable foreign data, invokes setup, and proves:

- setup is rejected;
- the database bytes remain unchanged;
- foreign data remains present;
- no Automations `meta` table appears;
- no Automations `automations` table appears.

### 3.4 Migration is restricted to known compatible prior formats

The repair preserves compatibility without restoring broad adoption.

Two legacy forms are admitted:

1. exact v2 Automations schema with `meta.schema_version=2`, no owner marker, and zero SQLite application/user-version markers;
2. exact v1 Automations schema with `meta.schema_version=1`, no owner marker, and zero SQLite application/user-version markers.

No other prior or foreign form is migrated.

### 3.5 The v1 mutation is conditional on exact v1 proof

The historical v1-to-v2 migration adds `runs.claim_owner`.

Previously, initialization could opportunistically add that column to any database containing a suitably named `runs` table.

Now the ALTER is reachable only after the whole database exactly matches the known v1 Automations schema and version identity.

After migration, current v2 owner and format markers are stamped and revalidated.

### 3.6 Store identity is checked at canonical connection time

The repair does not limit ownership proof to setup/update.

Normal `connect()` validates current owner, format version and required schema before returning a canonical connection.

Later marker or schema drift is therefore rejected by Store and Engine code when they open the canonical database.

### 3.7 Lifecycle health consumes owner/schema truth

`integrity_check()` now requires both generic SQLite integrity and current Automations owner/format/schema identity.

`descriptor()` therefore reports the database unhealthy when identity/schema is wrong.

`doctor()` records that failure and does not proceed to operational queries against an invalid or foreign store.

This closes the prior health-truth contradiction without addressing the independent live legacy-definition finding.

## 4. Permanent regressions

A dedicated `tests/test_store_identity.py` suite proves:

1. clean setup creates a ready store with all durable owner/version markers;
2. a valid foreign SQLite file is rejected before Automations schema mutation;
3. foreign file bytes and data remain unchanged after rejection;
4. exact unmarked v2 Automations state is adopted and stamped;
5. exact v1 Automations state migrates `runs.claim_owner` and stamps current identity;
6. update can adopt the exact compatible unmarked format;
7. a missing required table fails health and update;
8. a missing required index fails health and update;
9. wrong schema-version metadata makes status unhealthy;
10. doctor reports invalid canonical-store identity without querying foreign operational tables;
11. incompatible stores are not repaired in place.

The complete pre-existing owner suite also remains green, including concurrency, event replay, restart recovery, lifecycle, OS extension and webhook-security behavior.

## 5. Validation evidence

### Final PR-head acceptance

Final PR-head CI:

`37045314691`

On exact final head `2fca42703abcb22a54ac55113c3f9e4d6d5e62d5`:

- Ubuntu Python 3.11: **PASS**
- Ubuntu Python 3.12: **PASS**
- Ubuntu Python 3.13: **PASS**
- macOS Python 3.11: **PASS**
- macOS Python 3.12: **PASS**
- macOS Python 3.13: **PASS**
- Windows Python 3.11: **PASS**
- Windows Python 3.12: **PASS**
- Windows Python 3.13: **PASS**

Representative exact-head suite:

- tests run: **41**
- passed: **41**
- failed: **0**
- skipped: **0**

### Post-merge acceptance

Merged-main CI:

`37045503553`

On merged Automations `main` ref `e5ec241f1d86e76b15bab5be81e720a827e4fa09`:

- all 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs: **PASS**
- representative suite: **41 / 41 passed**

The tested PR-head tree and merged-main tree are identical:

`1c5d09d9c0d287b1eb42f031482c6c0f9819899a`

## 6. Finding-specific recheck

### C-A1.9-001

**RESOLVED for WSA-2026-026.**

A valid foreign SQLite file is no longer sufficient to acquire Automations canonical-store authority.

### Foreign valid SQLite

**PASS.**

The file is rejected before Automations schema writes and preserved unchanged.

### Wrong owner/version identity

**PASS.**

Current canonical access and lifecycle health fail closed.

### Missing/weakened schema

**PASS.**

Missing required table/index state is rejected and is not silently repaired.

### Clean database creation

**PASS.**

A new empty store is created with current schema and durable identity.

### Known compatible migration

**PASS.**

Only exact known v1/v2 Automations formats are admitted for migration/adoption.

### A2.3 lifecycle/readiness graph

**RESOLVED for the WSA-2026-026 canonical-store-health branch only.**

Ready database health now includes owner/format/schema truth.

The separate live legacy-definition and OS attachment lifecycle contradictions remain under WSA-2026-027 and WSA-2026-028.

### A3.2 migration/adoption

**RESOLVED for the WSA-2026-026 store-format admission branch only.**

Foreign stores are not adopted; exact known prior Automations formats have explicit bounded migration paths.

### A3.7 replay and A3.10 recovery

Existing event replay and restart/recovery regressions remain green under both exact-head and merged-main full suites.

This closure does not claim to close the independent live legacy authority or attachment reconciliation branches.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-026`.

The following remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-027` - post-setup legacy definition conflict is not a live execution kill fence;
- `WSA-2026-028` - component lifecycle and attached OS registry lifecycle diverge.

The whole-system verdict remains **NO-GO**.

Dashboard MC1.4 and owner dogfood remain paused.

## 8. Closure verdict

Required WSA-2026-026 behavior is present on merged Automations `main`:

- current SQLite owner and format identity is durable and mandatory;
- exact required schema is validated before canonical access;
- foreign non-empty SQLite is rejected before Automations schema mutation;
- only exact known compatible v1/v2 formats are migrated;
- v1 mutation is conditional on exact prior-format proof;
- wrong version and weakened/missing schema fail closed;
- lifecycle health reports invalid canonical-store identity as unhealthy;
- doctor does not query operational tables from an invalid store;
- all 9 exact-head CI jobs pass;
- all 9 merged-main CI jobs pass;
- representative suite is 41 / 41;
- tested and merged product trees are identical;
- open Automations PRs are zero.

**WSA-2026-026: CLOSED.**
