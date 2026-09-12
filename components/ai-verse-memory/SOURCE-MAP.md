# AI-Verse Memory Source Map

## Audit identity

- **Repository:** `aiverse-filmmakers/AI-Verse-Memory`
- **Default branch:** `main`
- **Exact reviewed revision:** `f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee`
- **Audit date:** 2026-09-13
- **Methodology:** `AI-Verse-System/docs/AUDIT-METHODOLOGY.md`
- **Evidence boundary:** Memory repository first. External repositories were not independently audited. Only Memory-owned fixtures, integration tests and CI that exercise host contracts were used as cross-repository evidence.

## Evidence hierarchy used

The audit applied this order when sources disagreed:

1. deterministic implementation;
2. tests and current CI;
3. current protocol/contracts;
4. architecture docs;
5. README/integration prose;
6. status/release prose;
7. PR/commit history;
8. inference.

This matters because several Memory docs still describe superseded tracked-host integration behavior.

---

# 1. Repository inventory

The reviewed revision contains 43 tracked blob files.

## Runtime and package surfaces

- `README.md`
- `LICENSE`
- `SECURITY.md`
- `SKILL.md`
- `manifest.json`
- `install.sh`
- `install.ps1`
- `scripts/install.py`
- `scripts/install_engine.py`
- `scripts/memory.py`
- `scripts/memory_engine.py`
- `scripts/os_compat.py`

## Architecture/protocol/migration

- `docs/ARCHITECTURE.md`
- `docs/OS-COMPATIBILITY.md`
- `protocol/MEMORY-PROTOCOL.md`
- `migration/MIGRATION.md`

## Agent integrations

- `integrations/claude-code.md`
- `integrations/codex.md`
- `integrations/hermes.md`

## Templates

- `templates/profile.md`
- `templates/scenario.md`

## Acceptance fixture

- `tests/fixtures/ai-verse-os-v2/... `

## Tests

- `tests/test_memory.py`
- `tests/test_installer.py`
- `tests/test_external_legacy_migration.py`
- `tests/test_native_source_isolation.py`
- `tests/test_canonical_freshness.py`
- `tests/test_os_compatibility.py`
- `tests/test_remote_bootstrap_contract.py`
- `tests/test_semantic_recall_candidates.py`

## CI

- `.github/workflows/test.yml`

No tracked vendor, build or generated dependency subtree was found.

---

# 2. Primary current-truth files

| File | Classification | Evidence |
|---|---|---|
| `scripts/memory_engine.py` | CURRENT implementation | Core storage, indexing, scope, recall, write, supersede, migration, doctor/status |
| `scripts/memory.py` | CURRENT implementation | Shared compatibility wrapper and repaired long-query candidate selection |
| `scripts/install_engine.py` | CURRENT implementation | Native/standalone install, local registry, lifecycle actions, legacy tracked cleanup |
| `scripts/install.py` | CURRENT implementation | Shared fail-closed OS compatibility wrapper and installed-engine packaging |
| `scripts/os_compat.py` | CURRENT contract implementation | Authoritative no-os/compatible/incompatible classifier |
| `protocol/MEMORY-PROTOCOL.md` | CURRENT contract | Memory routing, scope, capture, supersession, privacy |
| `migration/MIGRATION.md` | CURRENT migration intent | Existing history, v0.1 migration, external Memory-first/OS-later process |
| `README.md` | CURRENT high-level product contract | v0.2 native model and local extension lifecycle |
| `SECURITY.md` | CURRENT security boundary | Plaintext/local, no secret manager/ACL/encryption claims |
| `manifest.json` | CURRENT package metadata | v0.2.0, Python >=3.9, no external runtime service |

---

# 3. Implementation evidence by concern

## Source of truth

### `scripts/memory_engine.py`

Key evidence:

- native paths put historical atomics in OS-owned memory layers;
- native index under `runtime/indexes/ai-verse-memory/`;
- standalone home under `.ai-verse-memory/`;
- canonical native current documents are indexed in place;
- `KIND_AUTHORITY` ranks current context/manifest/decisions/profile above historical memory;
- `rebuild()` proves the database is derived.

### `protocol/MEMORY-PROTOCOL.md`

Explicitly states Memory is not a competing source of truth.

## Workspace isolation

### `scripts/memory_engine.py`

Relevant implementation:

- `normalize_scope()`;
- `_native_source_identity_from_parts()`;
- `_native_source_identity()`;
- `_validated_atomic_scope()`;
- `iter_atomic_files()`;
- `_indexed_source_is_valid()`;
- `_purge_invalid_indexed_sources()`;
- `allowed_scopes()`.

Important audit result:

- read/index path containment is strong;
- destination write path does not apply the same physical validation before creating/writing `memory/atomic`.

## Canonical freshness

### `scripts/memory_engine.py`

Relevant implementation:

- `source_state` table;
- `_canonical_source_version()`;
- `_refresh_native_canonical_sources()`;
- `_ensure_historical_source_state()`.

### `tests/test_canonical_freshness.py`

Proves:

- edited canonical current sources refresh before recall;
- new canonical documents are discovered;
- deleted documents are removed;
- source identity/version/freshness are exposed;
- historical atomic memory is intentionally not live-refreshed;
- Brain direction ownership changes invalidate semantic current-context representation.

## Direction ownership

### `scripts/memory_engine.py`

Relevant implementation:

- `_direction_owner_state()`;
- `_operational_current_projection()`;
- `_ownership_aware_current_text()`;
- ownership record included in canonical source version.

This is Memory-owned evidence of a cross-component contract, not an independent Brain audit.

## Recall

### `scripts/memory.py`

The wrapper replaces the old first-12-token FTS behavior with bounded unique term selection up to 64 terms.

### `tests/test_semantic_recall_candidates.py`

Regression for long semantic queries with late task-specific signals.

## Canonical writes

### `scripts/memory_engine.py`

Relevant implementation:

- `atomic_dir_for_scope()`;
- `atomic_path()`;
- `write_atomic()`;
- `update_meta()`;
- `forget_memory()`;
- `supersede()`.

Audit gaps derived directly from these functions:

- destination parent symlink containment is not verified before write;
- no canonical Memory mutation lock;
- direct file writes are not temp-and-replace transactions;
- supersession spans multiple mutations/rebuilds with no transactional boundary.

---

# 4. Installation and lifecycle evidence

## `scripts/install_engine.py`

Current native lifecycle implementation:

- `_ensure_extension_dir()`;
- `_registry_lock()`;
- `_read_local_registry()`;
- `_write_registry_atomic()`;
- `register_local_extension()`;
- `set_local_extension_enabled()`;
- `unregister_local_extension()`;
- `install_native()`;
- `enable_native()`;
- `disable_native()`;
- `detach_native()`.

Current public installer actions:

```text
install
enable
disable
detach
```

Negative evidence from the parser:

- no `uninstall`;
- no `reconcile`;
- no `rollback`.

## Legacy tracked integration cleanup

`_migrate_exact_legacy_marker()` and `_migrate_exact_legacy_registry()` remove only exact Memory-owned obsolete content.

Modified/ambiguous content is deliberately left alone.

This is evidence of conservative ownership preservation.

## Bootstrap

### `install.sh`
### `install.ps1`

Remote installation downloads current installer modules from raw GitHub `main`.

This is evidence for both:

- real public bootstrap;
- lack of immutable release pinning.

---

# 5. Migration evidence

## `migration/MIGRATION.md`

Defines three situations:

1. arbitrary existing Agent-OS history, candidate discovery plus agent distillation;
2. old AI-Verse Memory v0.1 store inside new native OS;
3. external standalone Memory existing before OS.

The document correctly warns against blindly promoting old profile/scenario summaries into current native truth.

## `scripts/memory_engine.py`

Relevant implementation:

- `discover()`;
- `map_legacy_scope()`;
- `_legacy_source()`;
- `migrate_legacy()`;
- `migration_complete()`.

### Concrete external migration defect

Within `migrate_legacy()`, fallback provenance for a record with no source uses the old file relative to the **new OS root**.

That path relation does not exist for a true external source.

### Authority-handoff negative evidence

No implementation in the reviewed tree provides:

- source snapshot/fingerprint manifest for dry run;
- dry-run/apply drift check;
- old-store retirement marker;
- authority handoff receipt;
- validation gate inside `migration_complete()`;
- post-migration reconciliation with later writes in the old store.

These are negative claims based on full tracked-file inventory plus lifecycle/parser inspection, not README omission alone.

---

# 6. Test evidence

## `tests/test_memory.py`

Covers:

- standalone remember/deduplicate/recall/rebuild;
- supersession history;
- forget;
- native mode detection;
- no second native profile;
- operator/workspace physical storage;
- workspace isolation plus operator context;
- explicit cross-workspace recall;
- mislabelled atomic scope rejection;
- post-index scope tamper rejection;
- symlink source escape rejection;
- cross-workspace symlink source rejection;
- doctor isolation failure;
- in-place current context/decision indexing;
- unknown-workspace write refusal;
- legacy project-scope mapping;
- local v0.1 dry/apply migration with unresolved scope.

## `tests/test_native_source_isolation.py`

Strong acceptance coverage for every native source kind:

- memory;
- profile;
- context;
- decision;
- memory summary;
- workspace manifest.

Tests direct file symlinks and parent-directory symlinks for:

- cross-scope redirects;
- outside-root redirects.

Proves cached-row rejection, purge and rebuild refusal.

Important negative coverage observation:

These tests attack **indexed sources**, not symlinked canonical **write destination parents** before a Memory write.

## `tests/test_canonical_freshness.py`

Covers current-source update/new/delete freshness, direction handover and intentional historical atomic non-live-refresh behavior.

## `tests/test_installer.py`

Covers:

- native compatibility detection;
- standalone marker idempotence;
- local registry idempotence;
- unknown sibling field preservation;
- exact legacy tracked cleanup;
- ambiguous legacy preservation;
- registry lock contention;
- enable/disable/detach canonical-state preservation;
- invalid registry refusal.

Negative coverage:

- no stale-lock recovery;
- no runtime discovery proof after detach;
- no uninstall/reconcile.

## `tests/test_external_legacy_migration.py`

Covers:

- external source dry run;
- apply;
- source store byte preservation;
- operator/workspace mapping;
- source-file symlink rejection.

Important coverage hole:

The migrated fixtures explicitly provide `source="standalone:test"`.

Therefore the missing-source external fallback path is not tested.

Also absent:

- source drift between dry run/apply;
- old-store writes after migration;
- validated authority retirement;
- crash recovery/journaling.

## `tests/test_os_compatibility.py`

Covers:

- no manifest;
- supported 2.x;
- unsupported v3;
- malformed/duplicate/incomplete manifests;
- no-write behavior on incompatible host.

## `tests/test_remote_bootstrap_contract.py`

Confirms shell/PowerShell bootstrap fetch all three installer modules.

---

# 7. CI evidence

## Workflow

`.github/workflows/test.yml`

## Latest main run

- **Run:** `34709185500`
- **Head:** `f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee`
- **Conclusion:** success
- **Date:** 2026-09-12

## Successful jobs

- test, Ubuntu, Python 3.9;
- test, Ubuntu, Python 3.12;
- test, macOS, Python 3.9;
- test, macOS, Python 3.12;
- test, Windows, Python 3.9;
- test, Windows, Python 3.12;
- installer smoke, Ubuntu;
- installer smoke, Windows;
- OS-update integration, Ubuntu.

The inspected Ubuntu/Python 3.9 log reports:

```text
Ran 44 tests
OK
```

## Memory-owned cross-repository acceptance

The CI workflow itself clones AI-Verse OS only to exercise Memory's declared host contract.

It verifies:

### Current OS -> Memory -> OS update

- tracked OS remains clean after Memory install;
- local registry exists and is ignored;
- actual OS update command succeeds;
- registry survives;
- Memory engine survives.

### Pre-registry OS -> Memory -> OS update forward

- Memory can attach without dirtying tracked host files;
- host update later adds registry hook;
- registry survives;
- Memory remains installed.

This evidence is valid for Memory integration because the test is owned and run by Memory.

It does **not** constitute a general audit of AI-Verse OS.

---

# 8. PR and historical repair map

All visible PRs #1 through #8 are merged.

| PR | Title | Historical significance |
|---|---|---|
| #1 | Upgrade AI-Verse Memory for native AI-Verse OS v2 | Establishes native v0.2 architecture and deliberate legacy migration |
| #2 | Harden Memory isolation across all native sources | Physical/logical source containment and revalidation |
| #3 | Refresh canonical Memory sources before recall | Fresh current-source derived state |
| #4 | Install Memory through the local OS extension registry | Removes tracked host integration edits and adds OS-update acceptance |
| #5 | Fail closed on incompatible AI-Verse OS hosts | Shared tri-state compatibility gate |
| #6 | Preserve late semantic signals in recall candidates | Repairs bounded FTS candidate selection for long semantic queries |
| #7 | Honor Brain direction ownership in canonical context recall | Prevents frozen OS strategy re-entry after authority handover |
| #8 | Release hardening: converged attachment lifecycle | Registry serialization, lifecycle actions, external Memory-first/OS-later migration |

## Repair-to-law mapping

### PR #2

**Repair:** read/index source containment.

**Law:** scope safety needs both lexical and resolved physical identity.

**New audit extension:** apply the same law to canonical writes.

### PR #3

**Repair:** stale current-source derived rows.

**Law:** derived state must track canonical freshness.

### PR #4

**Repair:** optional component edited tracked host files.

**Law:** optional attachment must preserve sibling ownership.

### PR #5

**Repair:** unsupported host could be misclassified as standalone.

**Law:** incompatible owner manifest fails closed before writes.

### PR #7

**Repair:** stale strategic meaning after authority handover.

**Law:** authority state is part of semantic source freshness.

### PR #8

**Repair:** attachment race and install-order gaps.

**Law:** shared registry mutation is serialized and lifecycle operations preserve user state.

---

# 9. Documentation drift map

## `README.md`

Current and aligned with the local extension registry architecture.

## `protocol/MEMORY-PROTOCOL.md`

Current and aligned with native ownership.

## `migration/MIGRATION.md`

Current intent, but stronger than enforcement around migration completion.

## `docs/OS-COMPATIBILITY.md`

Current and matches implementation.

## `docs/ARCHITECTURE.md`

Stale/partially historical:

- still describes the architecture as v0.1;
- emphasizes standalone profile/scenario structure;
- does not fully represent native v0.2 local-registry/current-source ownership.

## `integrations/claude-code.md`

Stale:

- claims native installer adds a standing block to `AGENTS.md`;
- claims native installer registers in tracked `skills/registry.yaml`.

Current code and CI prove the opposite.

## `integrations/codex.md`

Mostly compatible conceptually, but its standing-contract description should be checked against the current local extension model.

## `SKILL.md`

Core routing guidance is current.

Health wording referring to "capability registry entry" and "canonical AGENTS integration" is ambiguous/stale relative to the current local extension/clean-tracked-host model.

---

# 10. Security evidence and negative-space findings

## Explicit security documentation

`SECURITY.md` says Memory is not:

- a secret manager;
- encrypted-at-rest storage;
- an ACL system;
- multi-user isolation.

It warns against automatically persisting secrets and sensitive credentials.

## Strong implemented protections

- incompatible host no-write;
- workspace recall isolation;
- source symlink containment;
- stale invalid source purge;
- legacy source-file escape rejection;
- registry symlink validation;
- registry atomic replacement;
- destructive forget confirmation.

## Missing/partial protections found

- write destination parent containment;
- canonical Memory write serialization;
- migration transaction journal;
- stale registry-lock recovery;
- caller authorization at Memory CLI boundary;
- source snapshot binding for migration review.

---

# 11. Release/distribution evidence

## Repository state

- manifest version: `0.2.0`;
- default branch: `main`;
- current main branch is not protected;
- remote install scripts fetch mutable `main`.

## Immutable release evidence

A query for the repository's latest GitHub release returned no release.

A query for the tag reference namespace returned no available tag namespace.

Therefore no immutable Memory release was evidenced during this audit.

This supports the QC classification:

```text
RELEASE / DISTRIBUTION = MISSING for stable member release
```

Current main remains valid development evidence.

---

# 12. Inspiration/provenance evidence

No tracked research, inspiration or external-reference document exists in the 43-file repository inventory.

No PR description in the visible #1-#8 history identifies an external framework/project as a design source.

Accordingly:

- no external architecture inspiration is claimed;
- Markdown and SQLite/FTS5 are treated as implementation foundations, not attributed design provenance;
- absence of documented inspiration is recorded rather than filled by inference.

---

# 13. Negative claims and how they were established

| Claim | Verification basis |
|---|---|
| No uninstall command | Full installer parser inspection |
| No reconcile command | Full installer and engine parser inspection |
| No rollback command | Full lifecycle command inspection |
| No migration handoff/retirement command | Full tree + migration/lifecycle parser inspection |
| No immutable release evidenced | GitHub release/tag ref queries plus mutable-main bootstrap |
| No explicit inspiration corpus | Full tracked tree + PR history |
| No vector/embedding runtime dependency | Manifest + architecture + runtime implementation |
| No second native profile/scenario created | Native path implementation + tests |
| No tracked native AGENTS/skills registration on current install | Installer implementation + smoke/OS-update CI |
| No write-parent symlink test | Full test inventory and source-isolation test inspection |
| No blank-source external migration test | Full external migration test inspection |

---

# 14. Evidence confidence notes

## High confidence

- ownership model;
- native/standalone modes;
- local extension lifecycle;
- workspace read isolation;
- canonical current-source freshness;
- external missing-source migration defect;
- write-destination containment gap;
- CI state;
- documentation drift.

These are directly supported by current code/tests.

## Medium confidence / integration dependent

- whether registry detach fully prevents all agent runtime discovery;
- whether the host performs sufficient caller permission checks before invoking Memory;
- hot adoption behavior in every supported runtime.

Memory does not independently prove those host/runtime behaviors.

They are therefore recorded as unverified/partial, not asserted failures.

## Not claimed

No independent conclusion is made here about the general correctness of:

- AI-Verse OS;
- Brain;
- Skills;
- Data;
- Multiple Bots;
- Connections.

Only Memory-owned cross-repository contract evidence was used.
