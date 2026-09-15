# A1.4 — Independent Repository Audit: AI-Verse-Memory

**Audit program:** Independent Whole-System Public-Beta Audit  
**Phase:** A1 Independent repository audits  
**Task:** A1.4 AI-Verse-Memory  
**Audit date:** 2026-09-15  
**Frozen repository ref:** `406b14fb4398eb1b16dd5f30e50520e8c3540972`  
**System control baseline:** `12c0003fd17a9cc341a18f3dae97555a1469abca`  
**Repository role reconstructed from itself:** local-first canonical historical-memory owner with derived recall/index projections  
**Audit status:** **COMPLETE**  
**Standalone product verdict:** **DOGFOOD BLOCKED**  
**R-a Reconstruction:** COMPLETE / PASS  
**R-b Enforcement:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c Verdict:** COMPLETE / BLOCKED  
**Findings opened:** `WSA-2026-012`, `WSA-2026-013`, `WSA-2026-014`, `WSA-2026-015`  
**Next task:** A1.5 AI-Verse-Skills

> Audit-completion points measure completed forensic work, not product acceptance. Memory remains behind the dogfood gate because A1.4 found a destructive filesystem BLOCKER and two HIGH authority/lifecycle defects.

## 1. Independence statement

This packet reconstructs AI-Verse-Memory from the frozen Memory repository itself.

Substantive evidence came only from:

- files tracked in `aiverse-filmmakers/AI-Verse-Memory` at the frozen SHA;
- Memory-owned GitHub metadata, commit/PR history and Actions;
- Memory-owned fixtures/tests/workflows.

No sibling source repository was opened to fill a standalone Memory gap.

Memory-owned workflows that clone current OS are evidence only of what Memory exercised at that run time. A2 must independently validate both sides against frozen refs.

No existing AI-Verse-System Memory component specification was used as substantive Memory evidence.

## 2. Pre-task and pre-write drift control

At A1.4 start and immediately before writing:

- Memory `main` = `406b14fb4398eb1b16dd5f30e50520e8c3540972`;
- this exactly matches the A0 frozen Memory ref;
- System `main` = `12c0003fd17a9cc341a18f3dae97555a1469abca`;
- open PRs in Memory and System: **0**;
- no Memory product file was modified;
- Dashboard MC1.4 remains paused.

No drift invalidated the standalone target.

---

# R-a — Reconstruction

## 3. Repository inventory

The frozen recursive tree is complete and not truncated:

- tracked entries: **88**
- scripts/runtime modules: **17**
- test modules: **18**
- workflows: **2**
- canonical architecture/protocol/migration docs: bounded
- test OS fixture included

Primary implementation surfaces:

| Region | Role |
|---|---|
| `scripts/memory.py` | compatibility-gated public module/CLI wrapper |
| `scripts/memory_engine.py` | established Markdown/SQLite Memory engine |
| `scripts/public_beta.py` | current hardening layer for canonical mutation, containment, idempotency, migration and lifecycle state |
| `scripts/session_digest*.py` | durable compact session history + disposable recall projection |
| `scripts/session_promotion.py` | selective digest-to-atomic promotion |
| `scripts/orientation_map.py` | disposable bounded orientation projection |
| `scripts/progressive_recall.py` | catalog/summary/detail/exact-source retrieval |
| `scripts/relationship_projection.py` | disposable explicit-provenance relationship edges |
| `scripts/component.py` | public install/setup/status/doctor/enable/disable/update/uninstall lifecycle |
| `scripts/install_engine.py` | legacy/cross-platform installer and local-extension registry mutation |
| `migration/MIGRATION.md` | standalone-to-native adoption contract |
| `protocol/MEMORY-PROTOCOL.md` | Memory ownership/retrieval laws |

## 4. Product identity

Current metadata:

- product: AI-Verse Memory;
- version: `0.3.0-beta.1`;
- Python: 3.9+;
- platforms: Linux/macOS/Windows;
- license: MIT;
- external services: none required after install;
- vector database: none;
- embedding model: none.

Core product promise:

> canonical historical Memory is human-readable Markdown; SQLite and auxiliary projections are derived/disposable.

## 5. Canonical ownership

Memory owns:

- durable historical atomic memories;
- historical provenance;
- corrections/supersession;
- experiences/workflows/lessons;
- durable session digests as compact historical records;
- minimal migration/authority receipts required to prevent competing Memory ownership.

Memory does **not** own:

- OS current profile/context truth;
- OS decisions;
- workspace topology;
- curated current knowledge;
- Brain strategy;
- Skills package lifecycle;
- external account credentials;
- permission expansion.

Native canonical atomics:

- `operator/memory/atomic/`
- `workspaces/<id>/memory/atomic/`

Derived SQLite:

- `runtime/indexes/ai-verse-memory/memory.db`

Standalone canonical root:

- `.ai-verse-memory/`

## 6. Current-truth boundary

Native current sources are indexed **in place**, not copied into a second canonical Memory store.

Memory indexes bounded native source classes such as:

- current context;
- profile;
- decisions;
- workspace manifests;
- memory summaries;
- historical atomics.

Direction ownership is honored when current context is read: frozen/stale OS strategic material is not allowed to re-enter active context merely because historical files still exist.

Current truth outranks Memory history.

## 7. Public-beta hardening architecture

The public wrapper loads:

1. OS compatibility classifier;
2. base engine;
3. `public_beta.py`;
4. calls `public_beta.apply(engine)`.

Therefore the current supported entrypoint replaces the legacy-looking mutation functions with hardened versions before exporting the engine surface.

Current hardening includes:

- realpath/symlink checks for canonical Memory atomics;
- cross-process mutation lock;
- reentrant local lock bookkeeping;
- stale-lock recovery;
- atomic temp-file + fsync + replace writes;
- supersession recovery journal;
- durable retry/effect receipts;
- canonical source freshness validation;
- incremental derived-index updates with rebuild fallback;
- explicit standalone retirement authority.

This distinction matters: older base-engine functions are not the effective public mutation path.

## 8. Canonical capture

Manual/historical `write_atomic`:

- validates Memory type;
- normalizes exact scope;
- serializes canonical mutation;
- rejects retired standalone authority;
- supports durable effect IDs;
- detects changed payload reuse;
- rejects path escape/symlinked canonical Memory owners;
- writes Markdown atomically;
- updates only derived recall projection after canonical success.

Automatic `capture_candidate` additionally requires:

- durable historical classification;
- explicit rejection of current-truth ownership;
- no secret;
- no strategic authority;
- no permission expansion;
- no privacy ambiguity;
- no external-authority transfer;
- bounded source/evidence refs;
- retry-safe `effect_id`.

Automatic corrections require an explicit `supersedes` target.

## 9. Supersession and correction

Current public-beta supersession is transactional inside the target Memory root:

- one global canonical mutation lock;
- new record prepared with `supersedes`;
- old record updated with `superseded_by` and status;
- transaction journal written before paired canonical writes;
- recovery replays incomplete journaled effects;
- cross-scope correction is rejected;
- effect receipt makes retry replay-safe.

Normal recall hides superseded history unless historical recall is explicitly requested.

## 10. Session digests

Session digests are first-class durable compact historical records, not raw transcripts.

The digest API:

- does not accept raw conversation messages;
- binds scope/session/run/topic/source references;
- bounds summary/list/provenance sizes;
- uses deterministic digest identity;
- supports durable effect IDs;
- writes under the same canonical mutation lock;
- applies canonical path confinement;
- re-reads the written digest before recording the effect receipt.

Gateway/raw transcript remains external evidence authority.

## 11. Selective digest promotion

Promotion:

- requires caller-supplied candidates;
- is capped per digest;
- cannot cross digest scope;
- only accepts evidence refs already covered by the digest;
- adds the digest itself as evidence;
- routes every candidate through the existing automatic capture gate;
- corrections still require explicit supersession.

A digest is therefore evidence/navigation, not automatic durable truth.

## 12. Derived orientation map

The orientation map is deliberately derived and small.

It aggregates:

- counts;
- Memory types;
- explicit tags/topics;
- current-source routes;
- recent digest pointers.

It does not copy canonical Memory body text or digest summaries.

The projection carries a deterministic source fingerprint and is rebuilt/refreshed from authoritative current sources.

Hard serialized byte budget:

- default 8192;
- supported 1024-65536.

Diagnostics expose projection shape/freshness, not hidden reasoning or canonical content.

## 13. Progressive recall

Versioned API:

`memory.progressive-recall.v1`

Depths:

- catalog;
- summary;
- detail;
- source.

Summary/detail are bounded navigation/derived retrieval, not exact evidence.

Exact source:

- revalidates authorized scope;
- revalidates path;
- revalidates current source version;
- returns stale/unavailable instead of silently serving changed evidence;
- does not treat session-digest summaries as raw transcript evidence.

Responses remain bounded by configured bytes and item count.

## 14. Relationship projection

Relationship edges come only from explicit canonical metadata/provenance:

- supersedes;
- superseded_by;
- evidence refs;
- digest source bindings;
- session identity.

No body text is converted into inferred graph truth.

The relationship table is derived SQLite state and can be dropped/rebuilt.

Current one-hop expansion is narrowly intent-gated to historical/correction/provenance queries and does not enable arbitrary multi-hop traversal.

## 15. Scope and visibility

Native workspace recall normally sees:

- requested workspace;
- operator context.

It does not include unrelated workspaces.

Explicit `all_workspaces` exists as a broad retrieval surface, but Memory explicitly states it is not an ACL/multi-user permission engine. Whole-system permission admission is an A2/A4 concern.

Path/source validation rejects:

- cross-workspace symlink aliases;
- source paths resolving outside root;
- source paths whose physical scope differs from lexical scope;
- mislabelled workspace atomics.

## 16. Lifecycle reconstruction

Public lifecycle:

- install;
- setup;
- status;
- doctor;
- enable;
- disable;
- update;
- uninstall.

Expert:

- reconcile;
- detach;
- migrate.

Intended semantics:

- install makes runtime available only;
- setup attaches/initializes/rebuilds;
- setup does not migrate legacy state or transfer authority;
- disable preserves canonical state;
- update preserves enabled/disabled state;
- uninstall removes runtime/integration and preserves Memory state;
- reinstall does not silently reattach;
- reconcile rediscovers preserved setup state.

The lifecycle has material path and authority-enforcement defects below.

## 17. Standalone-to-native migration

Migration is snapshot-bound and dry-run-first.

Dry run records:

- source root;
- source byte/path fingerprint;
- target workspace-topology fingerprint;
- record-by-record mapping;
- unresolved/invalid blockers.

Apply refuses when:

- source changed;
- target workspace topology changed;
- destination ID conflicts.

Migrated canonical records preserve IDs, chronology and provenance.

Authority handoff occurs only after destination verification and no blocking records.

The final cross-root handoff itself is not failure-atomic; see `WSA-2026-014`.

---

# R-b — Enforcement

## 18. Canonical mutation and concurrency

Current strengths:

- one cross-process mutation lock serializes canonical Memory mutations;
- healthy queued lock holders reset a no-progress timeout rather than being globally capped;
- dead/stale holders can recover;
- transaction recovery runs when canonical mutation lock is acquired;
- effect receipts are written under the same lock;
- changed effect-ID payloads fail closed;
- canonical writes are atomic;
- derived SQLite failure falls back to canonical rebuild rather than becoming truth.

Exact-head tests include concurrent writers and stale-lock recovery.

## 19. Filesystem containment

Canonical atomic writes are well hardened:

- native `operator`, `workspaces`, workspace owner, `memory`, `atomic`, year/month and final target are checked;
- owner roots cannot be symlinks;
- final realpath must remain within the canonical owner;
- standalone home cannot be a symlink;
- session-digest directories use the same safe-child machinery.

However, the **component lifecycle/legacy installer** does not apply equivalent full parent-chain confinement to runtime/adapters and still has destructive path escape. See `WSA-2026-012`.

## 20. Lifecycle write authority

Component status distinguishes:

- absent;
- setup-required;
- disabled;
- migration-required;
- ready.

The extension registry stores `supported/installed/enabled`.

However, the canonical native writer does not consume that state as a write gate.

`_assert_writable_authority()` only enforces retirement for standalone mode and returns immediately for native mode.

Therefore lifecycle state is descriptive for native canonical mutation rather than authoritative. See `WSA-2026-013`.

## 21. Migration authority

Good enforcement:

- source drift after review fails closed;
- target workspace topology drift fails closed;
- unresolved records prevent handoff;
- destination records are verified;
- old historical Markdown is preserved;
- standalone current Memory engine refuses writes after a valid retired marker.

But handoff publishes the native complete marker **before** source retirement is durably verified.

This can produce an interrupted dual-writable state. See `WSA-2026-014`.

## 22. Privacy and secret boundary

Memory is explicit that it is local plaintext and not a secret manager.

Automatic capture:

- requires explicit negative secret/privacy assertions;
- contains bounded secret-like pattern rejection;
- blocks strategic/current/permission/external-authority candidates.

This does not become encryption or multi-user ACLs, and docs do not claim that it does.

## 23. Exact-head CI

Frozen Memory head:

`406b14fb4398eb1b16dd5f30e50520e8c3540972`

Exact push run:

`34983522129` — SUCCESS

Actually executed job set:

### Unit matrix
- Ubuntu Python 3.9 — SUCCESS
- Ubuntu Python 3.12 — SUCCESS
- macOS Python 3.9 — SUCCESS
- macOS Python 3.12 — SUCCESS
- Windows Python 3.9 — SUCCESS
- Windows Python 3.12 — SUCCESS

### Public-beta acceptance
- Ubuntu — SUCCESS
- macOS — SUCCESS
- Windows — SUCCESS

### Installer smoke
- Ubuntu — SUCCESS
- Windows — SUCCESS

### OS update integration
- Ubuntu — SUCCESS

Total exact-head jobs inspected: **12 / 12 successful**.

Every inspected job has actual steps. This is executable green evidence, not an empty-run artifact.

## 24. Test breadth

The repository has 18 test modules covering:

- canonical freshness;
- lifecycle;
- exact source;
- external migration;
- installer/registry behavior;
- core Memory capture/recall/supersession;
- native source isolation;
- semantic candidates;
- session digests/promotion;
- orientation map;
- progressive recall;
- relationship projection;
- relationship-neighbor runtime;
- context/neighbor benchmark harnesses;
- public-beta hardening;
- OS compatibility;
- remote bootstrap contract.

Notable exact-head negative tests include:

- symlinked canonical Memory parents;
- cross-workspace symlink/source aliases;
- mislabelled scopes;
- concurrent writers;
- stale mutation locks;
- changed effect payload reuse;
- unresolved migration;
- source drift after migration review;
- disabled/update lifecycle state preservation;
- invalid registry preservation.

The missing lifecycle parent-chain and disabled-write tests map directly to the findings below.

## 25. OS-update evidence limitation

Memory's `os-update-integration` workflow clones current OS main for one path.

That run is valid evidence for the environment exercised on 2026-09-15, but it is not an immutable pair proof because OS main can move.

The second path pins an older pre-registry OS commit for forward-update testing.

A2 must revalidate current frozen Memory ↔ frozen OS composition.

## 26. Release identity

Accepted release descriptor:

- version: `0.3.0-beta.1`;
- revision: `031e1e77c97ed3c9012235c7ffe0a4ece05e3695`.

Frozen current main:

`406b14fb4398eb1b16dd5f30e50520e8c3540972`

Commit comparison:

- current main is **119 commits ahead** of the accepted revision;
- later source includes major production features such as session digests, Context Ladder/progressive recall, orientation map, relationship projection and public-beta hardening;
- current manifest/engine/installer still identify as `0.3.0-beta.1`.

Additionally:

- remote `install.sh` hardcodes raw GitHub `main/scripts`;
- remote `install.ps1` hardcodes the same mutable `main/scripts`;
- `install_engine.py` defaults its source ref to `main`.

README release language says accepted bootstrap references are pinned to the exact immutable artifact after acceptance.

This drift is recorded as `WSA-2026-015`.

---

# R-c — Contradictions and findings

## 27. C-A1.4-001 — lifecycle filesystem safety is weaker than canonical Memory containment

**Source A:** README/security/migration contract say native reads/writes validate physical containment and symlinked/escaping destination paths are rejected.

**Source B:** component lifecycle/installer:

- runtime path is `<target>/scripts/ai-verse-memory`;
- adapter paths are under `.claude/skills` and `.agents/skills`;
- copy operations do not validate every parent realpath;
- uninstall checks only whether the final runtime/adapter directory itself is a symlink;
- it then calls `shutil.rmtree()`.

A symlinked parent such as `scripts -> /external/path` makes `target/scripts/ai-verse-memory` a normal final directory outside the target, so the final `is_symlink()` check is false and recursive deletion operates outside the selected root.

**Higher authority:** executable lifecycle/installer implementation.

**Finding:** `WSA-2026-012`.

## 28. C-A1.4-002 — native lifecycle state does not gate canonical mutation

**Source A:** install/setup contract says install does not attach or initialize authority; disabled state means Memory is disabled; uninstall removes integration/runtime while preserving state.

**Source B:** effective canonical writer calls `_assert_writable_authority`, whose native branch immediately returns without checking registry attachment, setup receipt, installed flag, enabled flag or migration-required state.

**Higher authority:** executable public-beta writer/lifecycle implementation.

**Finding:** `WSA-2026-013`.

## 29. C-A1.4-003 — migration promises singular writable authority but handoff publication is not failure-atomic

**Source A:** migration law says no migration leaves two declared writable canonical Memory stores.

**Source B:** `_retire_legacy_authority` writes, in order:

1. native `authority-handoff.json` with `status=complete`;
2. source `AUTHORITY.json` with `status=retired`;
3. legacy writer backup/stub.

No cross-root journal or two-phase commit protects the sequence.

**Higher authority:** executable migration implementation.

**Finding:** `WSA-2026-014`.

## 30. C-A1.4-004 — accepted immutable beta and mutable current bootstrap share one version identity

**Source A:** accepted release descriptor pins beta.1 to `031e1e77…`; README says bootstrap references are pinned to the exact artifact after acceptance.

**Source B:** current main is 119 commits ahead, still versioned `0.3.0-beta.1`, while remote shell/PowerShell bootstrap downloads from mutable `main`.

**Higher authority:** current version sources, immutable descriptor, commit comparison and bootstrap scripts.

**Finding:** `WSA-2026-015`.

## 31. WSA-2026-012 — lifecycle parent-symlink escape can write or recursively delete outside the selected target

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** destructive lifecycle / filesystem containment  
**Affected repo:** `AI-Verse-Memory`  
**Affected journeys:** install, setup, uninstall, adapter installation/removal, runtime replacement

### Summary

Memory's canonical writer has strong owner-path containment, but lifecycle runtime/adapter operations do not validate every parent realpath.

A symlinked parent can redirect lifecycle writes and recursive uninstall deletion outside the selected target root.

### Concrete destructive path

Native runtime:

`target/scripts/ai-verse-memory`

Uninstall:

1. computes that lexical path;
2. checks `runtime.is_symlink()`;
3. if false, executes `shutil.rmtree(runtime)`.

If `target/scripts` is a symlink to an external directory and the external `ai-verse-memory` child is a normal directory:

- `runtime.is_symlink()` is false;
- `shutil.rmtree(runtime)` recursively deletes that external directory.

Equivalent parent-chain risk exists for adapter paths under:

- `.claude/skills/ai-verse-memory`;
- `.agents/skills/ai-verse-memory`.

Install/setup copying can also write outside root through those parent symlinks.

### Why BLOCKER

This is proven user-data/filesystem destruction risk from a supported lifecycle command.

### Required closure evidence

After A6 authorizes repair:

1. establish a single safe-target helper for every lifecycle path;
2. reject symlink/junction/reparse parent components;
3. compare final parent/target realpaths against the selected target root before copy/remove;
4. never `rmtree` a lexical target until containment is proven;
5. add negative tests for symlinked `scripts`, `.claude`, `.claude/skills`, `.agents`, `.agents/skills`, runtime and adapter directories;
6. prove external sentinel files survive install/setup/uninstall on supported platforms.

## 32. WSA-2026-013 — native canonical writes ignore install/setup/attachment/enable lifecycle authority

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** lifecycle authority / canonical writes  
**Affected repo:** `AI-Verse-Memory`  
**Affected journeys:** pre-setup use, disable, detach, uninstall, migration-required state

### Summary

Native canonical Memory mutation is not gated by native component lifecycle state.

### Observed behavior

Effective `write_atomic`, session-digest writes and related mutation paths call:

`public_beta_assert_writable_authority(root, mode)`

The implementation:

- enforces retired authority only for standalone mode;
- returns immediately in native mode.

It does not verify:

- local registry entry exists;
- `supported=true`;
- `installed=true`;
- `enabled=true`;
- setup receipt says setup complete;
- current state is not migration-required.

Therefore code already present in a source checkout or already-loaded process can mutate canonical native Memory:

- after package install but before setup;
- after disable;
- after detach;
- after uninstall if code remains loaded/externally invoked;
- while lifecycle reports migration-required.

Current lifecycle tests verify that status changes and state is preserved, but do not attempt a write while disabled/detached/uninstalled.

### Impact

Lifecycle controls can report Memory unavailable while canonical Memory state still changes.

This undermines operator expectations, separation of install from setup, and safe disable/detach semantics.

### Required closure evidence

After A6 authorizes repair:

- native write readiness must consume the authoritative local extension/setup state;
- normal writes must require supported + installed + attached + enabled + setup-complete;
- migration-required state must permit only explicitly authorized migration/recovery writes;
- lifecycle-internal bootstrap operations need a narrow explicit exception rather than globally bypassing the gate;
- add tests proving canonical atomics, session digests, promotion and metadata mutation fail before setup and after disable/detach/uninstall.

## 33. WSA-2026-014 — standalone-to-native authority handoff is not failure-atomic across the two roots

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** migration / canonical authority transfer  
**Affected repo:** `AI-Verse-Memory`  
**Affected journeys:** Memory-first adoption, crash recovery, canonical owner handoff

### Summary

The migration copy is careful, but the final cross-root authority handoff is ordered non-transactionally.

### Observed sequence

`_retire_legacy_authority`:

1. writes target native `authority-handoff.json` as `complete`;
2. writes source `.ai-verse-memory/AUTHORITY.json` as `retired`;
3. optionally backs up/replaces the legacy writer with a retirement stub.

A failure writing the source marker after step 1 leaves:

- target marker = complete;
- old source authority still active.

A failure before/while writer retirement can also leave an older writer executable.

There is no migration handoff journal spanning source and target.

Current component status can detect some inconsistent states as migration-required, but `WSA-2026-013` means native canonical writes do not honor that lifecycle block, so an interrupted handoff can be dual-writable in practice.

Current tests cover successful retirement and unresolved-record no-handoff, not injected failure between authority-publication steps.

### Impact

The architecture's central singular-authority invariant can be violated during partial migration failure.

Two writable historical Memory routes can diverge.

### Required closure evidence

After A6 authorizes repair:

1. implement an explicit resumable handoff transaction;
2. publish target `complete` only after source retirement is durably verified;
3. use pending/prepared states and stable handoff ID on both roots;
4. make normal target writes fail while handoff is incomplete;
5. make retry idempotently resume every interruption point;
6. add fault-injection tests after target prepare, source marker write, writer backup and writer stub replacement;
7. prove no interruption point exposes two writable canonical routes.

## 34. WSA-2026-015 — accepted Memory artifact identity and remote bootstrap are not pinned to current immutable source

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** release/version/bootstrap reproducibility  
**Affected repo:** `AI-Verse-Memory`  
**Affected journeys:** remote install, support/debugging, release identification

### Summary

The accepted beta.1 release descriptor pins an older immutable revision, while current main is 119 commits newer with material production behavior but still identifies as the same beta version. Legacy remote bootstrap fetches mutable `main`.

### Observed behavior

Accepted:

- `0.3.0-beta.1`
- `031e1e77c97ed3c9012235c7ffe0a4ece05e3695`

Frozen current:

- `406b14fb4398eb1b16dd5f30e50520e8c3540972`
- 119 commits ahead
- still `0.3.0-beta.1`.

Remote:

- `install.sh` -> `.../AI-Verse-Memory/main/scripts`
- `install.ps1` -> same mutable main
- installer default ref -> `main`.

### Impact

Version-only diagnostics cannot distinguish accepted beta.1 from materially newer source, and legacy remote bootstrap can install moving, not-yet-accepted code.

The formal immutable release descriptor remains correct for its pinned revision, bounding severity to LOW in this standalone phase. A5 must revisit release-set consequences.

### Required closure evidence

After A6/A5 authorization:

- assign post-release development main a distinct version identity or issue a new accepted immutable beta;
- pin remote bootstrap to an immutable accepted ref by default;
- make intentional development-main install explicit;
- add bootstrap tests that assert immutable release pinning;
- align README, manifest, SKILL, engine/installer version and release descriptor semantics.

---

# R-c — Completeness and verdict

## 35. Lifecycle matrix

| Lifecycle area | Standalone state | Conclusion |
|---|---|---|
| install | PARTIAL | correct availability semantics, but parent-symlink escape WSA-012 |
| setup | PARTIAL | explicit/no migration transfer, but lifecycle path escape + writer gate defect |
| status | VERIFIED | structured state model |
| doctor | VERIFIED/PARTIAL | read-only layered checks, but cannot compensate for writer gate |
| enable | PARTIAL | registry state changes, canonical writer ignores it |
| disable | FAILED AS AUTHORITY GATE | state says disabled while canonical writes remain possible |
| update | VERIFIED/PARTIAL | preserves enablement; same lifecycle path issue |
| uninstall | **FAILED / BLOCKER** | parent-symlink rmtree can delete external directory |
| reinstall | VERIFIED/PARTIAL | preserved state/reconcile design coherent |
| detach | FAILED AS WRITE GATE | attachment removed but loaded/source writer can still mutate |
| reconcile | VERIFIED/PARTIAL | explicit recovery; path/write-gate issues remain |
| migrate dry-run | VERIFIED | snapshot-bound |
| migrate apply/copy | VERIFIED | scope/provenance/drift checks |
| authority handoff | CONTRADICTED | non-failure-atomic WSA-014 |
| atomic remember | VERIFIED | serialized, atomic, replay-safe |
| automatic capture | VERIFIED | bounded historical safety gate |
| supersession | VERIFIED | journaled pair mutation |
| forget | VERIFIED | explicit confirmation + confined canonical file |
| session digest | VERIFIED | immutable bounded durable history |
| progressive recall | VERIFIED | bounded and exact-source revalidated |
| cross-platform | VERIFIED | 12/12 exact-head jobs |

## 36. 46-lens completeness matrix

| # | Lens | A1.4 state | Conclusion |
|---:|---|---|---|
| 1 | Product identity | VERIFIED | local-first historical Memory |
| 2 | Architecture | VERIFIED | Markdown canonical, SQLite derived |
| 3 | Ownership | VERIFIED | history/provenance only |
| 4 | Source of truth | VERIFIED | canonical Markdown vs disposable projections explicit |
| 5 | Provenance | VERIFIED | source/evidence/migration refs preserved |
| 6 | Scope | VERIFIED/PARTIAL | retrieval/canonical source scope strong; lifecycle gate weak |
| 7 | Isolation | VERIFIED/PARTIAL | Memory reads/writes strong, lifecycle paths WSA-012 |
| 8 | Privacy/local-first | VERIFIED | plaintext limitations explicit |
| 9 | Installation | CONTRADICTED | WSA-012 |
| 10 | Attachment/registration | PARTIAL | registry robust, writer does not require attachment |
| 11 | Activation/adoption | PARTIAL | setup explicit; write authority + handoff issues |
| 12 | Initialization | PARTIAL | setup semantics clear; lifecycle paths not fully confined |
| 13 | Migration/legacy | CONTRADICTED | WSA-014 |
| 14 | Update/upgrade | PARTIAL | state preserved; release identity drift |
| 15 | Disable/detach/uninstall | CONTRADICTED | WSA-012/013 |
| 16 | Install-order independence | PARTIAL | standalone/native supported; full system deferred |
| 17 | Discovery | VERIFIED | OS compatibility + local registry |
| 18 | Readiness | PARTIAL | status is truthful, but runtime write enforcement disagrees |
| 19 | Health/doctor | VERIFIED/PARTIAL | layered/read-only; cannot prove lifecycle authority |
| 20 | Permissions/approvals | EXTERNAL BY DESIGN | Memory is not permission engine |
| 21 | Security/path safety | **CONTRADICTED** | lifecycle destructive escape |
| 22 | Idempotency/replay | VERIFIED | effect IDs under canonical mutation lock |
| 23 | Concurrency/locking | VERIFIED | global canonical mutation serialization |
| 24 | Failure/recovery | PARTIAL | supersession recovery strong; handoff failure atomicity weak |
| 25 | Capability taxonomy | VERIFIED | history not Skills/Brain/scheduler |
| 26 | Runtime/agent portability | VERIFIED | local Python + Claude/Codex/Hermes adapters |
| 27 | Integration boundaries | VERIFIED AS MEMORY CLAIMS | sibling side A2 |
| 28 | Cross-component writes | PARTIAL | owner capture APIs strong; lifecycle admission weak |
| 29 | Read path/retrieval | VERIFIED | source freshness/scope/progressive descent |
| 30 | Data/schema evolution | VERIFIED/PARTIAL | historical migration strong; release version drift |
| 31 | Performance/bounds | VERIFIED | retrieval/digest/orientation byte/item limits |
| 32 | Product/UX | VERIFIED/PARTIAL | clear CLI; lifecycle controls not fully authoritative |
| 33 | Automation/cadence | NOT-OWNED | no scheduler ownership |
| 34 | Agent behavior | VERIFIED | automatic capture fails closed on risky classes |
| 35 | Apps/UI projections | NOT-APPLICABLE | no UI ownership |
| 36 | Release/distribution | PARTIAL | immutable descriptor valid; current/bootstrap drift |
| 37 | Cross-platform | VERIFIED | 12 exact-head jobs across OS families |
| 38 | Documentation consistency | CONTRADICTED | lifecycle/migration/release claims exceed edge implementation |
| 39 | Historical-learning | VERIFIED | explicit experience/lesson/correction model |
| 40 | Inspiration/reference | LIMITED | no ungrounded external authority inferred |
| 41 | Negative-space | VERIFIED | no secret/Brain/Skills/current-truth takeover found |
| 42 | Architecture-vs-operation | PARTIAL | strong core, lifecycle/migration gaps |
| 43 | Current-target readiness | **BLOCKED** | BLOCKER + HIGH findings |
| 44 | Final seamless-system gap | UNVERIFIED BY DESIGN | A2-A5 |
| 45 | Scope-creep | VERIFIED | relationship/progressive features bounded and derived |
| 46 | Definition of done | VERIFIED | full standalone packet + closure evidence |

## 37. Negative-space checks

Within frozen canonical Memory roots, A1.4 found no evidence that Memory:

- makes SQLite canonical;
- silently copies native current truth into Memory atomics;
- stores raw Gateway transcripts as session digests;
- automatically promotes every session digest into atomics;
- lets a digest cross workspace scope during promotion;
- treats relationship projection as canonical fact truth;
- performs arbitrary multi-hop graph expansion;
- stores Skill package code;
- takes Brain strategic ownership;
- installs/owns a scheduler;
- claims encryption/ACL/multi-user security it does not implement;
- silently migrates active legacy authority during setup;
- allows unresolved migration records to publish a normal successful handoff;
- permits changed effect-ID payloads to replay as the original effect;
- accepts physical cross-workspace source aliases for normal native recall.

## 38. Evidence limitations

- No sibling repository was independently validated in A1.4.
- The OS-update workflow uses current OS main for one integration path, so A2 must recreate immutable frozen-pair evidence.
- The BLOCKER path escape is established from unambiguous parent-symlink + `shutil.rmtree` semantics; no destructive reproduction was performed.
- Disabled/pre-setup native write admission is established from the effective writer and lifecycle code; no product test was added because A0-A6 is read-only.
- Cross-root migration fault injection does not currently exist; ordering is directly visible in executable code.
- Formal Distribution release acceptance belongs to A5.

## 39. Evidence inventory

- `E-A1.4-001`: frozen tree/repository metadata.
- `E-A1.4-002`: README/manifest/SKILL/security identity and ownership.
- `E-A1.4-003`: architecture/protocol/migration contracts.
- `E-A1.4-004`: public wrapper and public-beta patch installation.
- `E-A1.4-005`: canonical path containment implementation.
- `E-A1.4-006`: mutation lock/atomic/idempotency implementation.
- `E-A1.4-007`: capture/forget/supersession implementation.
- `E-A1.4-008`: session digest/promotion implementation.
- `E-A1.4-009`: progressive recall/orientation/relationship implementation.
- `E-A1.4-010`: component lifecycle implementation.
- `E-A1.4-011`: installer/extension registry implementation.
- `E-A1.4-012`: migration authority-handoff ordering.
- `E-A1.4-013`: 18-module test inventory.
- `E-A1.4-014`: exact-head Test run `34983522129`.
- `E-A1.4-015`: 12 exact-head successful jobs and executed steps.
- `E-A1.4-016`: current lifecycle test coverage gap for disabled writes.
- `E-A1.4-017`: lifecycle parent-symlink coverage gap.
- `E-A1.4-018`: migration tests cover success/unresolved but not interruption between authority markers.
- `E-A1.4-019`: accepted release descriptor `031e1e77…`.
- `E-A1.4-020`: accepted release -> current main comparison, 119 commits ahead.
- `E-A1.4-021`: remote bootstrap scripts hardcode mutable main.
- `E-A1.4-022`: recent Context Ladder/relationship/benchmark commit history.
- `E-A1.4-023`: live pre-write ref/open-PR recheck.

## 40. Standalone verdict

**AI-Verse-Memory at `406b14fb4398eb1b16dd5f30e50520e8c3540972`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

Strong areas include:

- clear canonical ownership;
- local-first human-readable truth;
- derived-index discipline;
- excellent source freshness and workspace isolation;
- robust canonical atomic path confinement;
- cross-process serialized mutation;
- durable effect-id semantics;
- journaled supersession;
- conservative automatic capture;
- explicit current-truth boundary;
- compact digest architecture;
- bounded progressive/exact-source retrieval;
- derived-only relationship graph;
- broad cross-platform executable CI.

Current dogfood blockers:

1. `WSA-2026-012` BLOCKER lifecycle parent-symlink destructive escape;
2. `WSA-2026-013` HIGH native lifecycle state does not gate canonical writes;
3. `WSA-2026-014` HIGH migration authority handoff is not failure-atomic;
4. `WSA-2026-015` LOW release/version/bootstrap reproducibility drift.

No Memory product repair is made during A1.4.

## 41. Progress after audit acceptance

- weighted audit progress: **13 / 100 = 13%**
- weighted remaining: **87%**
- tracker tasks complete: **9 / 51**
- tracker tasks remaining: **42 / 51**
- phases fully complete: **1 / 7**
- phases not yet complete: **6 / 7**
- A1 repository audits complete: **4 / 14**
- A1 repository audits remaining: **10 / 14**
- A1 weighted progress: **8 / 28**
- next task: **A1.5 AI-Verse-Skills**

## 42. Task completion record

**Task:** A1.4 AI-Verse-Memory  
**Reviewed repository ref:** `406b14fb4398eb1b16dd5f30e50520e8c3540972`  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / DOGFOOD BLOCKED  
**Contradictions:** `C-A1.4-001` through `C-A1.4-004`  
**Findings opened:** `WSA-2026-012` through `WSA-2026-015`  
**Inherited findings:** unchanged  
**Standalone verdict:** COMPLETE / DOGFOOD BLOCKED  
**Tracker change:** A1.4 COMPLETE; accepted progress 13/100; A1.5 NEXT  
**Next task:** A1.5 AI-Verse-Skills
