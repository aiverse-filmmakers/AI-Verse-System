# AI-Verse Memory Component Specification

## Audit record

- **Component:** AI-Verse Memory
- **Repository:** `aiverse-filmmakers/AI-Verse-Memory`
- **Default branch reviewed:** `main`
- **Exact reviewed revision:** `f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee`
- **Audit date:** 2026-09-13
- **Method:** `docs/AUDIT-METHODOLOGY.md`
- **Scope:** Memory only. Cross-repository material was used only where Memory's own tests, contracts or CI exercised an external host path.
- **Tracked implementation inventory:** 43 files at the reviewed revision, excluding no vendor/build subtree because none is tracked.
- **Latest main CI evidence:** workflow run `34709185500`, successful at the reviewed revision across the full configured matrix.

## Executive verdict

AI-Verse Memory is a strong local-first memory engine with a coherent native AI-Verse OS v2 architecture. Its most important architectural decision is already correct:

> In native AI-Verse OS mode, Memory does not become a second profile/context/decision system. The OS remains canonical for current truth, while Memory owns historical atomic memory and a disposable derived index.

The current implementation has real, tested support for:

- native AI-Verse OS v2 detection with fail-closed compatibility;
- standalone compatibility when no AI-Verse OS manifest exists;
- operator and workspace historical atomic memory;
- workspace-isolated recall with explicit cross-workspace escape;
- physical and logical validation of indexed native sources;
- live freshness of canonical profile/context/decision sources;
- historical supersession;
- local extension-registry attachment;
- enable, disable and registry detach;
- clean OS update interoperability;
- in-root legacy v0.1 migration;
- external "Memory first, OS later" migration;
- cross-platform tests on Linux, macOS and Windows;
- Python 3.9 and 3.12 test coverage.

However, **the current v0.2 target is not yet complete under the system audit definition**. Four issues prevent a "works perfectly together like a glove" verdict today:

1. **Native read containment is stronger than native write containment.** Read/index paths reject symlink escapes, but canonical Memory write destinations are created/written without equivalent resolved-path ownership validation. A symlinked workspace or memory parent can redirect a write outside the intended canonical root.
2. **The external legacy migration has an uncovered provenance failure.** If a legacy atomic memory has no `source` value, external `--source-root` apply attempts to make the old path relative to the new OS root and can abort.
3. **Migration copies data but does not complete a machine-enforced canonical authority handoff.** The old standalone store remains intact and writable, dry-run review is not bound to a source snapshot, post-review source drift is not detected, and `migration-complete` does not verify that unresolved items are closed or the old route is retired. This leaves a split-brain risk if an old agent keeps writing to its former store.
4. **Lifecycle and release closure remain incomplete.** There is no explicit uninstall, reconcile or rollback command; registry detach preserves runtime adapters; doctor can PASS while attachment-related checks are warnings; and the public bootstrap installs from mutable `main` with no immutable release currently exposed.

The component is therefore **functionally strong and near its current target, but not current-target complete**.

---

# 1. Component identity

## CURRENT

AI-Verse Memory v0.2.0 is a local-first persistent memory engine for AI agents and compatible agent operating systems.

Its durable data model is:

```text
canonical Markdown
      ↓
rebuildable SQLite index
      ↓
scoped lexical / FTS recall
```

The database is not canonical. It is disposable derived state.

AI-Verse Memory supports two operating modes:

### Native AI-Verse OS v2 mode

The host owns canonical current truth and workspace topology.

Memory owns historical atomic memory inside those host-defined canonical memory layers:

```text
operator/memory/atomic/
workspaces/<id>/memory/atomic/
```

It also derives recall views from selected current canonical sources without copying ownership:

- operator profile;
- operator context;
- operator decisions;
- workspace manifest;
- workspace context;
- workspace decisions;
- root-level memory summaries.

The index lives at:

```text
runtime/indexes/ai-verse-memory/memory.db
```

### Standalone compatibility mode

If `AI-VERSE.yaml` is genuinely absent, Memory preserves the original portable model under:

```text
.ai-verse-memory/
```

This mode owns its own profile, scenarios, atomic memories, evidence and state.

## LAW

A host manifest that is present but malformed, unsupported or incomplete is **not** equivalent to "no host". Memory fails closed rather than silently creating standalone state beside an incompatible AI-Verse OS.

---

# 2. Current intended target

The current target, inferred from the v0.2 architecture, the release-hardening PR history, current docs and tests, is:

> Ship a safe, standalone-capable persistent historical-memory engine that can attach to AI-Verse OS v2 at any reasonable install order, preserve the OS as the sole owner of current truth, maintain strict workspace isolation, survive OS updates, and deliberately adopt old Memory state without creating a competing canonical memory system.

That target includes more than engine correctness. It includes:

- package/bootstrap installation;
- host compatibility gating;
- attachment;
- enable/disable/detach;
- canonical storage ownership;
- recall isolation;
- migration;
- current-source freshness;
- update coexistence;
- cross-platform operation;
- clear health/readiness;
- release/distribution;
- safe adoption by already-existing agents.

## Current-target verdict

**PARTIAL: not yet complete.**

The engine core and most native integration are implemented and tested. The blockers are concentrated at the write boundary, migration authority handoff, lifecycle closure and immutable distribution.

---

# 3. Ownership and source-of-truth map

## CURRENT

| Responsibility | Canonical owner in native mode | Memory role |
|---|---|---|
| Operator identity/preferences | OS operator profile | Index in place, do not duplicate |
| Current operator state | OS operator context | Index current operational truth |
| Strategic direction | Current direction owner | Respect ownership marker, never reactivate frozen OS strategy |
| Operator historical memory | Memory in OS memory layer | Canonical atomic history |
| Operator decisions | OS decisions | Index in place |
| Workspace manifest/topology | OS workspace | Index in place |
| Current workspace state | OS workspace context | Index in place |
| Workspace historical memory | Memory in OS memory layer | Canonical atomic history |
| Workspace decisions | OS decisions | Index in place |
| Durable reusable knowledge | OS/knowledge owner | Not swallowed into Memory index |
| Skill execution procedure | Skills owner | Memory may identify promotion candidates only |
| Search/index state | Memory runtime | Derived and rebuildable |
| Extension attachment entry | Host local extension registry | Memory owns only its own entry |
| Standalone profile/scenarios/history | Memory standalone store | Canonical only while standalone mode is active |

## LAW

One responsibility has one canonical writable owner at a time.

Native Memory must never recreate a parallel:

- profile;
- current-context tree;
- decision store;
- knowledge base;
- workspace topology;
- strategic-direction authority.

## LAW

A derived index may increase recall performance but may never become the only surviving truth.

## GAP

Atomic Markdown is described as canonical, but direct manual edits to historical atomic Markdown are intentionally not live-refreshed on the next recall. A rebuild is required. This is acceptable only if the contract is explicit that canonical historical files are engine-managed/immutable between rebuilds. Otherwise the current behavior is a documentation and freshness mismatch.

---

# 4. Native architecture

## CURRENT

The native data path is:

```text
OS canonical current files
        │
        ├── validated physical source identity
        ├── source version / freshness
        ▼
derived SQLite items + FTS
        ▲
        │
Memory-owned atomic historical Markdown
```

Canonical current sources are refreshed incrementally before recall:

- changed files are reindexed;
- newly created eligible canonical documents are discovered;
- deleted documents are removed from SQLite and FTS;
- physical path/scope validity is rechecked before a cached row may be returned.

Atomic historical memory is treated differently:

- it is indexed as historical;
- it is not live-refreshed as if it were current state;
- normal engine writes rebuild the index;
- superseded entries remain available only when history is requested.

## LAW

Current canonical context outranks historical memory.

## LAW

Historical records are superseded, not rewritten to pretend the old state never existed.

## LAW

Memory summaries and atomic memory must never silently overwrite current context.

---

# 5. Direction-ownership interoperability

## CURRENT

Memory reads the OS-owned local direction marker:

```text
.aiverse/direction/ownership.json
```

When the OS owns a scope, Memory may index the full current context.

When Brain owns that scope, Memory projects `CURRENT.md` down to approved operational sections so frozen OS strategy cannot re-enter recall merely because the file bytes remain unchanged.

The ownership record contributes to Memory's source-version calculation. Therefore an ownership handover invalidates the derived representation even if `CURRENT.md` itself did not change.

## LAW

Authority changes are semantic source changes.

A derived index must include relevant ownership/authority state in freshness decisions when unchanged source bytes can have a different current meaning.

## HISTORICAL

This rule came from the repair merged in Memory PR #7 after strategic ownership could otherwise have allowed old OS intent to remain recallable after Brain handover.

---

# 6. Scoped recall and isolation

## CURRENT

Native default recall searches operator scope only.

Workspace recall searches:

```text
selected workspace + operator
```

It excludes unrelated workspaces.

Cross-workspace recall requires:

```text
--all-workspaces
```

Native indexed sources are validated by both:

1. lexical path identity;
2. resolved physical path identity.

A source is rejected if the lexical and physical identities disagree, if it crosses a workspace/kind boundary, or if it resolves outside the repository.

Cached native rows are revalidated before recall and purged if no longer valid.

## LAW

Workspace isolation is both logical and physical.

Metadata labels alone are not enough. Physical file ownership and resolved path containment must agree.

## GAP

This law is enforced strongly on **read/index sources**, but not symmetrically on **canonical write destinations**.

`normalize_scope()` accepts a workspace based on a directory containing `WORKSPACE.yaml`. `atomic_dir_for_scope()`, `ensure_layout()` and `atomic_path()` then create/write through those paths without first proving that the destination parent chain is non-symlinked and resolves inside the correct canonical ownership root.

This means a symlinked workspace directory, `memory/`, or `atomic/` parent can redirect a write outside the intended scope even though the resulting source will later be rejected by read/index validation.

This is a current security/isolation defect, not merely a future hardening idea.

---

# 7. Memory write model

## CURRENT

Supported historical atomic types include:

- fact;
- preference;
- constraint;
- decision for legacy compatibility;
- state;
- project_state as a legacy alias;
- entity;
- event;
- experience;
- workflow.

Native writes normalize current ownership:

- stable identity/preferences belong in profile;
- current state belongs in context;
- settled choices belong in decisions;
- reusable knowledge belongs in knowledge;
- historical events/transitions/lessons belong in atomic Memory;
- proven execution methods are candidates for Skills.

The engine:

- validates a known native scope;
- refuses writes to missing workspaces;
- performs exact active-text deduplication per scope;
- writes Markdown;
- rebuilds the derived index.

## GAP

Canonical Memory mutation is not serialized or transactional.

Examples:

- two concurrent writers can race;
- `supersede` creates the new memory and rebuilds before marking the old memory superseded, so a crash can leave both active;
- `update_meta` and migration destination writes are direct file replacements, not atomic temp-and-replace transactions;
- rebuild resets database tables without a Memory-wide lifecycle lock;
- no durable idempotency key/effect receipt exists beyond exact text deduplication.

This is acceptable for a small single-writer prototype, but not the final multi-agent system target.

## INTENDED

The Memory effect boundary should eventually support:

- physical destination containment validation before any write;
- serialized canonical mutation;
- atomic file replacement;
- durable idempotency/effect receipts for routed writes;
- transaction-safe supersession semantics;
- recovery after interrupted migration/rebuild.

This should remain Memory-owned implementation, not become a generic OS file mutation API.

---

# 8. Installation and attachment

## CURRENT

Remote bootstrap:

- shell downloads `install.py`, `install_engine.py` and `os_compat.py`;
- PowerShell does the same;
- local repository installation can use repository-local sources.

The shared compatibility gate classifies:

- `no-os`;
- `compatible`;
- `incompatible`.

Native install then:

1. installs the engine under `scripts/ai-verse-memory/`;
2. installs Claude and Codex skill adapters;
3. conservatively removes exact obsolete Memory-owned tracked integration stanzas;
4. attaches `ai-verse-memory` through `.aiverse/extensions/registry.json`;
5. initializes the index;
6. runs doctor;
7. leaves old standalone state untouched.

Native install does **not** currently add a Memory block to tracked `AGENTS.md`, `CLAUDE.md`, `AI-VERSE.yaml` or `skills/registry.yaml`.

Registry mutation has:

- a shared lock file;
- maximum registry size validation;
- schema validation;
- sibling/unknown-field preservation;
- compare-before-replace;
- atomic `os.replace`.

## LAW

Optional components attach through component-owned local integration state and must not dirty sibling-owned tracked host files.

## GAP

The lock has no stale-lock lease/recovery protocol. A process crash after lock creation can leave a persistent "busy" condition until repaired manually.

## GAP

The remote installer fetches mutable `main`. There is no current immutable release artifact exposed by the repository. This violates the system's release law for member-facing stable installs.

---

# 9. Lifecycle matrix

| Stage | CURRENT behavior | Status |
|---|---|---|
| Install | Real shell, PowerShell and Python installer paths | COMPLETE |
| Host compatibility | Shared fail-closed v2 classifier | COMPLETE |
| Attach/register | Local extension registry, idempotent, sibling-preserving | COMPLETE |
| Enable | Installer `--action enable` | COMPLETE |
| Disable | Installer `--action disable`, preserves state | COMPLETE |
| Activate/adopt | Attachment makes capability host-discoverable, but no separate canonical-adoption transaction | PARTIAL |
| Initialize | `init` creates layout/index | COMPLETE |
| Scope initialization | Operator paths automatic, workspace writes require existing OS workspace | COMPLETE WITH LIMITATIONS |
| Migrate/import | Legacy atomic migration + candidate discovery for arbitrary history | PARTIAL |
| Doctor | Structural/runtime/index/isolation checks; attachment/adapters/migration mostly warnings | COMPLETE WITH LIMITATIONS |
| Status | Memory counts/index/migration status | COMPLETE |
| Update | Re-run install can repair/update; OS update interoperability tested | COMPLETE WITH LIMITATIONS |
| Disable/detach | Real local registry operations, state preserved | COMPLETE WITH LIMITATIONS |
| Uninstall | No public uninstall command | MISSING |
| Reinstall | Re-running install can rediscover/preserve canonical state | COMPLETE WITH LIMITATIONS |
| Reconcile | No dedicated Memory reconcile command | MISSING |
| Rollback | No public rollback path | MISSING |
| Authority handoff from legacy store | Procedural/manual only | PARTIAL |

### Important detach nuance

`detach` removes the local extension registry entry but deliberately preserves:

- engine files;
- Claude adapter;
- Codex adapter;
- canonical Memory.

The installer may also have installed a Hermes user-local skill.

Therefore the current operation is accurately a **local registry detach**, not proof that every runtime discovery surface can no longer invoke Memory.

A mature detach contract must either close every discovery path opened by attachment or explicitly define which preserved adapters are inert unless the registry says attached.

---

# 10. Existing-agent and legacy-history migration

This is the most important current-target area.

## CURRENT: legacy AI-Verse Memory atomic store

The dedicated `migrate-legacy` workflow supports:

- local old `.ai-verse-memory/`;
- external old standalone project via `--source-root`;
- dry run by default;
- explicit `--apply`;
- `global -> operator`;
- `project:<id>`, `client:<id>` and `workspace:<id>` only when the matching OS workspace exists;
- unresolved scopes left unresolved rather than leaked;
- preserved IDs and chronology;
- preserved provenance when present;
- old source left untouched;
- symlinked/escaping legacy memory files rejected;
- post-copy rebuild.

## LAW

Old standalone profile/scenario summaries must not be blindly promoted into new native profile/current context.

Those old summaries may be stale, derived or overlap newer canonical OS truth.

They require deliberate human/agent distillation into the correct new canonical owner.

## CURRENT: arbitrary existing agent history

`discover` can scan a source tree for candidate Markdown/text/JSON/YAML/CSV history and rank likely files for review.

It deliberately does not bulk-ingest every transcript or file.

The connected agent is expected to distill durable history and write only useful atomic memories.

This is an intentional anti-warehousing design, not a missing vector database.

## GAP: external provenance failure

The external migration path has a concrete uncovered defect.

During apply, if an old atomic memory lacks `source`, fallback provenance is built using:

```python
old_path.relative_to(root)
```

For an external `--source-root`, `old_path` is outside the new OS `root`, so this can raise and abort the migration.

The current external migration test supplies `source="standalone:test"`, so it does not exercise this failure.

The fallback should be based on the validated legacy source root/display path, not the new OS root.

## GAP: migration is not snapshot-bound

The dry-run report contains result/scope mapping, but no source digest or immutable migration manifest.

Therefore:

1. user reviews dry run;
2. old agent may continue changing history;
3. apply reads whatever exists at apply time;
4. reviewed bytes and applied bytes are not cryptographically/structurally bound.

For a real authority handoff, dry run and apply need source snapshot identity or explicit drift detection.

## GAP: no canonical retirement transaction

After copy, the old standalone store remains fully usable.

That is good for preservation, but there is no machine-enforced distinction between:

- preserved historical archive;
- still-active canonical writer.

`migration-complete` only writes a marker in the new store. It does not:

- validate zero unresolved/invalid blockers;
- bind to a reviewed source snapshot;
- prove representative recall;
- mark the old store retired/read-only;
- prove the old agent no longer routes writes there;
- record an authority handoff receipt;
- detect new writes to the old store after migration.

This is the principal split-brain risk.

## LAW: migration authority handoff

A migration may preserve the old bytes indefinitely, but after adoption there must be exactly one **active writable canonical route** for that responsibility.

Preserved evidence is not the same as preserved authority.

A safe final sequence is:

```text
discover old authority
        ↓
freeze or fingerprint source
        ↓
dry-run mapping bound to source snapshot
        ↓
validate all records / unresolved cases
        ↓
apply idempotently with journal/receipts
        ↓
verify new canonical state and representative recall
        ↓
record authority handoff
        ↓
retire old route from active writes
        ↓
keep old bytes as read-only evidence/archive if desired
```

## GAP: migration transactionality

Migration writes records one at a time and rebuilds at the end.

There is no migration journal/rollback. A later error can leave earlier records already copied.

Re-running is partly resumable because existing IDs are skipped, but this is not equivalent to an explicit resumable transaction.

## GAP: schema preflight

Legacy frontmatter is permissively parsed. Invalid numeric metadata can fail during indexing/rebuild after some files have already been copied.

A complete migration should validate all migratable records before mutating destination state.

---

# 11. Health and readiness

## CURRENT

`doctor` verifies required core conditions including:

- detected mode;
- canonical store/index writability;
- SQLite;
- index rebuild;
- native workspace/source isolation.

It also reports integration checks for:

- Claude adapter;
- Codex adapter;
- adapter parity;
- local extension attachment;
- absence of obsolete tracked registration;
- clean tracked AGENTS/CLAUDE integration;
- legacy store presence;
- migration marker.

## Health depth

Current doctor reaches approximately:

- **STRUCTURAL:** strong;
- **ATTACHMENT:** observed but usually warning-level;
- **RUNTIME:** SQLite/rebuild tested;
- **DEPENDENCY:** minimal because runtime is stdlib-only;
- **OPERATIONAL:** limited;
- **SYSTEM:** not proven by Memory doctor alone.

## GAP

A missing or disabled local attachment does not make doctor fail. Missing adapters and unfinished migration are also warnings.

Therefore:

> `doctor: PASS` does not mean "Memory is attached, enabled, migrated, adopted and system-ready."

The system must keep those states separate.

This is consistent with the wider AI-Verse readiness law, but the Memory docs/UX should state the depth explicitly.

---

# 12. Security and privacy

## CURRENT strengths

- local plaintext canonical data;
- no cloud memory service required;
- no vector database required;
- no credential requirement;
- explicit "not a secret manager" boundary;
- workspace recall isolation;
- explicit cross-workspace opt-in;
- read/index physical path containment;
- malformed/incompatible OS fail-closed;
- local extension registry symlink protection;
- legacy source file symlink/escape rejection;
- destructive forget requires `--yes`.

## LIMITATIONS

Memory does not provide:

- encryption at rest;
- ACLs;
- multi-user isolation;
- secret storage;
- caller authentication;
- a permission engine.

Those are correctly not claimed.

## Cross-component permission boundary

Memory currently validates storage scope, not caller authorization.

In the final owner-routed write pipeline, the host should validate caller permission/approval and Memory should revalidate the requested scope/effect at its own write boundary.

Memory should not absorb general OS policy management.

---

# 13. Retrieval and scalability

## CURRENT

Recall uses:

- SQLite FTS5 when available;
- lexical fallback otherwise;
- bounded candidates;
- exact scope filtering;
- post-candidate lexical matching;
- custom ranking using overlap, scope, importance, confidence, authority and recency.

The public wrapper preserves up to 64 unique FTS terms so long semantic queries retain late task-specific signals.

## HISTORICAL

PR #6 repaired a real interoperability failure where Brain-style retrieval prompts placed useful task signals after a generic prefix and the previous first-12-token FTS candidate window could exclude them.

## GAP

Current candidate bounds are pragmatic, not scale-proof:

- FTS returns at most 200 candidates before ranking;
- lexical fallback orders and caps at 2000 before post-filtering;
- every normal Memory write performs a full rebuild.

At large history scale this can create recall misses or write latency.

This is not a blocker for the current small local core, but it is a final-scale requirement.

---

# 14. Runtime portability

## CURRENT

The core is Python stdlib plus SQLite.

Supported adapters/documentation exist for:

- Claude Code;
- Codex;
- Hermes;
- generic file-aware Agent-OS repositories through standalone mode.

Claude and Codex adapter parity is tested.

Hermes installation is opportunistic and user-local when Hermes is detected.

## GAP

There is no Hermes acceptance job proving complete attach/disable/detach behavior.

The user-local Hermes skill also has no corresponding uninstall lifecycle in this repository.

---

# 15. Release and distribution

## CURRENT

- repository manifest version: `0.2.0`;
- MIT license;
- remote shell/PowerShell bootstrap;
- no runtime third-party Python package dependency;
- CI succeeds at current main.

## GAP

The public install path resolves mutable files from `main`.

At audit time, no latest GitHub release was exposed and no tag namespace was available through the repository refs queried.

Therefore release/distribution is **not complete** under the AI-Verse immutable-release law.

A member-facing release should install a specific immutable version whose behavior matches its docs and acceptance evidence.

---

# 16. Documentation truth and drift

## CURRENT truth sources

The strongest current prose is:

- `README.md`;
- `protocol/MEMORY-PROTOCOL.md`;
- `migration/MIGRATION.md`;
- `docs/OS-COMPATIBILITY.md`.

## DOCUMENTATION DRIFT

### `integrations/claude-code.md`

It still says native install adds a Memory block to `AGENTS.md` and registers in `skills/registry.yaml`.

That is historical behavior superseded by the local extension registry.

### `docs/ARCHITECTURE.md`

It still describes the core largely as v0.1 and diagrams profile/scenario ownership without clearly distinguishing the current native v0.2 ownership model.

### `SKILL.md`

Its health wording refers to "capability registry entry" and "canonical AGENTS integration" in a way that can be read as the old tracked integration model, while current code expects local registry attachment and clean tracked AGENTS state.

## LAW

Current implementation and passing tests outrank stale prose.

The stale prose must be repaired, not used to redefine current architecture backward.

---

# 17. Historical repairs and permanent laws

| Repair | Historical defect/risk | Permanent law |
|---|---|---|
| PR #1 | Standalone architecture would duplicate native OS profile/context | Native Memory stores history inside host-owned topology and does not create a second current-truth system |
| PR #2 | Scope metadata alone could be fooled by symlink/path ownership | Isolation must validate logical and physical source identity |
| PR #3 | Derived canonical-source rows could become stale | Current canonical sources must refresh/invalidate derived recall state |
| PR #4 | Optional Memory integration dirtied tracked OS files | Optional components attach through local component-owned state and preserve sibling-owned tracked files |
| PR #5 | Unsupported/malformed OS could silently fall back to standalone | Presence of an incompatible owner manifest fails closed before writes |
| PR #6 | Long semantic queries lost late task signals | Bounded retrieval must preserve task-specific signals before ranking |
| PR #7 | Old OS strategy could reappear after Brain direction handover | Derived recall must honor current authority semantics, not only file bytes |
| PR #8 | Registry races and lifecycle/order issues | Shared local registry mutation must be serialized and attachment lifecycle must preserve canonical user state |

## Newly derived law from this audit

The PR #2 isolation law must be symmetric:

> Physical ownership validation is required at both the read boundary and the canonical write boundary.

## Newly derived law from this audit

The migration law must distinguish data preservation from authority preservation:

> Old bytes may remain, but old writable authority must not remain active after canonical adoption.

---

# 18. Inspiration and deliberate non-goals

## INSPIRATION

No dedicated external inspiration/research lineage is recorded in the reviewed repository.

The implementation visibly relies on established local-software primitives:

- Markdown as inspectable durable representation;
- SQLite / FTS5 as a local rebuildable index;
- filesystem isolation and symlink validation;
- GitHub Actions for portability/acceptance.

These are implementation technologies, not documented provenance claims.

## Deliberate non-goals in the current core

The repository explicitly avoids making the core depend on:

- vector search;
- embeddings;
- a knowledge graph;
- web dashboard;
- daemon/background server;
- automatic cloud sync;
- multi-user ACL system;
- transcript warehouse;
- separate summarization LLM.

Optional future semantic tiers are allowed only as derived adapters. They may never replace Markdown as canonical truth.

---

# 19. Completeness matrix

| Dimension | Audit status | Reason |
|---|---|---|
| ENGINE / CORE | COMPLETE WITH LIMITATIONS | Core recall/history/supersession/index works; concurrency and large-scale limits remain |
| ARCHITECTURE / CONTRACT | COMPLETE WITH LIMITATIONS | Ownership model is strong; docs drift remains |
| INSTALL / PACKAGE | COMPLETE WITH LIMITATIONS | Real cross-platform install; mutable-main bootstrap |
| HOST INTEGRATION | COMPLETE WITH LIMITATIONS | Real local registry + OS-update acceptance; hot adoption semantics not fully proven |
| ATTACH / REGISTER | COMPLETE | Idempotent, sibling-preserving local registry |
| ACTIVATE / ADOPT | PARTIAL | No explicit authority/adoption transaction |
| SCOPE INITIALIZATION | COMPLETE WITH LIMITATIONS | Existing workspaces only; destination symlink containment defect |
| MIGRATION / LEGACY | PARTIAL | Real migration exists but external provenance bug and no authority handoff |
| HEALTH / DOCTOR | COMPLETE WITH LIMITATIONS | Strong structural/runtime checks; attachment/readiness warnings do not fail |
| PERMISSION / SAFETY | PARTIAL | Scope safety strong on reads; caller authorization external; write containment gap |
| CROSS-COMPONENT READ | COMPLETE WITH LIMITATIONS | Canonical OS sources + direction ownership supported |
| CROSS-COMPONENT WRITE | PARTIAL | CLI/engine writes exist, but no shared authorized owner-routed transaction/receipts |
| UPDATE / UPGRADE | COMPLETE WITH LIMITATIONS | OS update path tested; Memory itself uses moving main rather than immutable upgrade |
| DISABLE / DETACH / UNINSTALL | PARTIAL | Enable/disable/registry-detach exist; no uninstall and discovery closure unverified |
| REINSTALL / RECONCILE | PARTIAL | Reinstall/repair works; no explicit reconcile |
| CROSS-PLATFORM | COMPLETE | Linux/macOS/Windows CI, Python 3.9/3.12 |
| ACCEPTANCE | COMPLETE WITH LIMITATIONS | 44 unit tests per matrix job plus installer/OS-update acceptance; missing critical negative paths |
| RELEASE / DISTRIBUTION | MISSING | No immutable member release path evidenced |
| DOCUMENTATION CONSISTENCY | PARTIAL | README/protocol current, architecture/integration docs stale |

---

# 20. Exact work remaining before Memory "works like a glove"

Priority order:

1. **Fix canonical write-path containment.**
   - Reject symlinked/cross-root operator/workspace/memory/atomic destination parents.
   - Validate lexical and resolved ownership before every create/write/migrate/supersede/delete mutation.
   - Add negative tests for workspace-root, memory-dir and atomic-dir symlink redirects.

2. **Fix external legacy migration provenance fallback.**
   - Build fallback provenance relative to the validated legacy source root.
   - Add external migration tests with blank/missing `source`.

3. **Implement migration authority handoff.**
   - Fingerprint/freeze the reviewed source.
   - Detect dry-run-to-apply drift.
   - Preflight all records.
   - Journal applied records.
   - Verify target state.
   - Record a handoff receipt.
   - Retire the old route from active writes without deleting evidence.
   - Make `migration-complete` conditional on verified criteria.

4. **Serialize canonical Memory effects.**
   - Atomic writes.
   - Transaction-safe supersession.
   - Safe rebuild coordination.
   - Durable idempotency/effect receipts for routed writes.

5. **Close lifecycle semantics.**
   - Define registry detach versus full detach/uninstall.
   - Prove preserved adapters cannot make a detached component appear active unintentionally.
   - Add uninstall/reconcile or explicitly document the supported equivalent.

6. **Make health/readiness depth explicit.**
   - Keep structural doctor separate from attachment/operational/system readiness.
   - Provide a truthful aggregate status path.

7. **Repair current documentation drift.**
   - `docs/ARCHITECTURE.md`;
   - `integrations/claude-code.md`;
   - health language in `SKILL.md`.

8. **Ship an immutable release.**
   - tag/version current architecture;
   - point member install docs to immutable artifacts;
   - run acceptance against the exact release.

9. **Add large-history performance acceptance before scale demands it.**
   - candidate recall quality;
   - rebuild/write cost;
   - optional semantic adapter only if needed.

---

# 21. Final intended state

## INTENDED

A finished AI-Verse Memory should feel like a native memory substrate regardless of installation order:

```text
install package
      ↓
host compatibility
      ↓
attach
      ↓
enable
      ↓
initialize
      ↓
discover old state if any
      ↓
review/fingerprint migration
      ↓
apply idempotently
      ↓
verify
      ↓
handoff canonical authority
      ↓
retire old writable route
      ↓
healthy scoped recall/write
```

An agent that existed before Memory should be able to adopt it without:

- losing history;
- silently duplicating current truth;
- keeping two writable canonical memory systems;
- crossing workspace boundaries;
- reinstalling the whole OS;
- depending on a particular agent vendor;
- depending on cloud memory infrastructure.

That is the component-level definition of "works perfectly together like a glove".

---

# 22. Classification summary

## CURRENT

- local-first Markdown historical memory;
- rebuildable SQLite/FTS index;
- native OS v2 and standalone modes;
- canonical current-source indexing without ownership theft;
- workspace-isolated recall;
- source freshness;
- supersession;
- local extension attachment;
- enable/disable/registry detach;
- OS update coexistence;
- legacy atomic migration;
- external Memory-first/OS-later migration path;
- direction-ownership-aware recall;
- cross-platform green CI.

## INTENDED

- explicit safe canonical adoption by existing agents;
- migration bound to reviewed source state;
- single writable authority after adoption;
- fully serialized canonical effects;
- lifecycle closure and immutable release.

## GAP

- write-destination symlink containment;
- external blank-source migration failure;
- no enforced legacy authority retirement;
- no dry-run/apply drift detection;
- no migration journal/validated completion;
- no uninstall/reconcile/rollback;
- detach discovery closure unverified;
- canonical mutation concurrency;
- warning-level doctor attachment semantics;
- stale docs;
- mutable-main distribution;
- large-scale recall/write limits.

## LAW

- one canonical owner per responsibility;
- current canonical truth beats historical memory;
- SQLite is derived;
- isolation is logical and physical;
- physical containment applies to reads and writes;
- incompatible hosts fail closed;
- optional components do not dirty sibling-owned tracked state;
- strategic ownership changes alter recall semantics;
- history is superseded, not rewritten;
- migration may preserve evidence but must retire duplicate writable authority.

## HISTORICAL

PRs #1 through #8 show the component evolving from portable standalone memory into a native OS v2 memory engine, then hardening isolation, freshness, attachment, compatibility, semantic recall, direction ownership and lifecycle/order independence.

## INSPIRATION

No explicit external design-inspiration corpus is recorded in the repository. Markdown, SQLite/FTS5 and standard filesystem/GitHub tooling are implementation foundations rather than documented architectural provenance.
