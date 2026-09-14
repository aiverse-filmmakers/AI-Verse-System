# AI-Verse Data Component Specification

**Component:** AI-Verse Data  
**Repository reviewed:** aiverse-filmmakers/AI-Verse-Data  
**Reviewed branch:** main  
**Reviewed head:** 2497b54e5fbdf0fec4621d218302b3df30dbbc03  
**Reviewed head date:** 2026-09-12  
**Fresh standalone review:** 2026-09-13  
**Repository visibility:** private  
**Evidence rule:** this specification was reconstructed from AI-Verse-Data itself using docs/AUDIT-METHODOLOGY.md. Other repositories were not independently audited. Cross-repository evidence appears only where the Data repository itself contains pinned integration contracts or acceptance workflows.


## 2026-09-14 current superseding update

**CURRENT accepted head:** `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`  
**PR #13 release-hardening merge:** `189b13264ab86115d2f21fee3ba8cd5a8dac6581`  
**Invisible Intelligence safe-structure merge:** `579dae596a1c929bbc0e900541d29742c18b875e`

This section supersedes retained 2026-09-13 audit statements where they describe PR #13 as open/unmerged, the materialized extension as registration-only, the real host path as unaccepted, or the final five-component release gate as red.

CURRENT facts:

- PR #13 is merged and its exact ref became the Data revision in the frozen Agent release;
- the materialized `ai-verse-data-host/1.0` engine is callable through the supported host route;
- Data is accepted in clean-machine Agent composition without sibling raw-SQL ownership;
- `579dae596a1c929bbc0e900541d29742c18b875e` adds safe retryable automatic structure ensure for additive/compatible structure only;
- current head `8edde7dca5afa34e300130cc6b8ee2b4170ad40f` advertises trusted host-bound actor support in the installed engine;
- automatic structure organization does **not** grant destructive migration authority;
- incompatible/destructive changes remain explicit `migration_required` / approval-bound and fail closed;
- runtime/Gateway input cannot forge trusted automatic Data identity or provenance;
- cross-repo scenarios E/F pass in Distribution run `34890195270` against this exact Data head.

The remaining Data gaps are broader legacy/standalone adoption, operator recovery/migration ergonomics and cross-version release-train preservation. They are not evidence that the accepted Agent host path is still registration-only.


---

## 1. Executive identity

**CURRENT:** AI-Verse Data is the canonical structured operational-data engine for AI-Verse workspaces.

It exists for facts that need durable structure, validation, relations, queries, transactions, versioning, provenance and safe machine mutation. Typical examples are CRM records, projects, content calendars, production records, inventory, finances, operational state and application-backed records.

Its core architecture is local-first and SQLite-backed, but SQLite is deliberately hidden behind a storage-driver abstraction and a storage-neutral protocol.

The core responsibility can be summarized as:

~~~text
Data = current structured operational truth
Memory = historical recall and remembered context
Brain = direction, goals, reasoning and evaluation
OS = scope, host structure, routing and outer policy
~~~

**LAW:** Data must not become general Memory, Brain state, a scheduler, an OS, a credentials store, or a hidden app-specific database layer that competes with Data itself.

**CURRENT:** the core engine is mature and unusually well hardened for a first release. It includes scoped SQLite storage, Data Spaces, versioned schemas, validated CRUD, safe queries, relations, bounded transactions, optimistic concurrency, idempotency, events, receipts, bulk mutation, backup/export/import, internal migrations, user-schema migrations, quarantine and staged recovery.

**CURRENT PRODUCT-PATH STATUS:** the accepted Agent host path is executable and cross-platform accepted. Safe additive automatic structure organization is CURRENT. Remaining product gaps are narrower: exact legacy/bound-standalone adoption into native workspaces, richer operator migration/recovery promotion UX, and cross-version Safe Update/release-train preservation.

---

## 2. Status vocabulary

This document uses the canonical labels:

- **CURRENT** - proven on reviewed main at 2497b54e5fbdf0fec4621d218302b3df30dbbc03.
- **INTENDED** - desired behavior supported by current architecture or active repository planning but not yet current main.
- **GAP** - required path missing between current behavior and the current or accepted target.
- **LAW** - invariant that should remain true across future implementation.
- **HISTORICAL** - prior behavior, repair, milestone claim or evolution relevant to current architecture.
- **INSPIRATION** - evidenced reference project or technology that informed design, not a requirement by itself.

The original audit's PR #13 status is historical. PR #13 merged as `189b13264ab86115d2f21fee3ba8cd5a8dac6581` and became the accepted Data release ref. Later Invisible Intelligence changes `579dae596a1c929bbc0e900541d29742c18b875e` and `8edde7dca5afa34e300130cc6b8ee2b4170ad40f` are CURRENT post-release evidence for the next candidate.

---

## 3. Role in the complete system

Data is the structured record layer.

A healthy system topology is:

~~~text
AI-Verse OS
  scope / host / routing / outer policy
              |
              v
        AI-Verse Data
  canonical structured records
              |
   +----------+-----------+-----------+
   |          |           |           |
 Brain      Memory       Apps      Dashboard
 reads      evidence     scoped     projections
 facts      references   clients    and controls

Multiple Bots / Connections / Automation
use scoped Data contracts without taking ownership
~~~

**LAW:** integration arrows represent permitted use, not ownership transfer.

**CURRENT:** Data includes adapter surfaces for Multiple Bots, Brain, Memory, Dashboard, Apps, Connections and Automation, but these adapters remain Data-owned contracts. They do not make Data the owner of those components' canonical state.

**CURRENT:** Data installation is designed to preserve sibling registries and avoid modifying sibling repositories or tracked OS files.

**CURRENT:** Data becomes available through the supported OS host/extension route without moving canonical Data ownership into OS.

**CURRENT:** the materialized extension exposes the callable Data host protocol and trusted host-bound actor support. This path is accepted in the frozen Agent release and in Invisible Intelligence scenario E/F composition.

---

## 4. Problem the component solves

Without a canonical structured-data layer, AI systems commonly create:

- ad hoc JSON files;
- spreadsheets with unclear authority;
- hidden app-local SQLite files;
- arbitrary SQL generated by a model;
- duplicate CRM/project state in prompts and memories;
- indexes treated as truth;
- records with no schema/version history;
- unsafe concurrent writes;
- mutations without durable receipts;
- cross-workspace leakage;
- migrations that rewrite live state without backup;
- app uninstall paths that destroy business records;
- separate structured stores after installing a new canonical system.

AI-Verse Data replaces those patterns with one scoped structured-data authority per workspace.

**LAW:** a structured operational fact should have one canonical structured owner. Memory may remember it, Brain may reason over it, Dashboard may display it and Apps may mutate it through grants, but those surfaces must not silently become competing canonical stores.

---

## 5. Current architecture

### 5.1 Core layers

**CURRENT:** the repository is layered rather than monolithic.

Important current modules include:

- protocol validation;
- trusted roots and scoped database identity;
- storage-driver contracts;
- SQLite driver and internal schema;
- Data Space and entity-schema catalog;
- record engine;
- query and aggregate engine;
- relations;
- transactions;
- idempotency;
- provenance events and mutation receipts;
- bulk preview/execute;
- backup and portable export/import;
- internal format migrations;
- user-schema migrations;
- corruption quarantine and staged recovery;
- typed client;
- consumer adapters;
- native OS compatibility, registration, lifecycle and health.

### 5.2 Physical storage

**CURRENT:** the native canonical path is:

~~~text
workspaces/<workspace-id>/data/ai-verse-data.sqlite
~~~

Standalone library scope uses:

~~~text
.ai-verse-data/data.sqlite
~~~

Each database embeds scope-binding metadata.

### 5.3 Internal database identity

**CURRENT:** the storage engine uses explicit AI-Verse identity signals, including:

- format: ai-verse-data/sqlite;
- current database format version: 2;
- minimum migratable format: 1;
- SQLite application_id;
- SQLite user_version;
- migration-framework metadata;
- scope binding version 1.

**LAW:** an unrelated SQLite file must never be silently adopted as AI-Verse Data.

### 5.4 Internal tables and logical schemas

**CURRENT:** Data uses engine-owned internal tables rather than generating arbitrary SQL tables from model-defined schemas.

Logical Data Spaces and entity schemas are stored as structured definitions with immutable schema versions and deterministic digests.

**LAW:** user/model schema flexibility must not become arbitrary SQL authority.

### 5.5 SQLite operating mode

**CURRENT:** the SQLite driver enables:

- foreign keys;
- WAL;
- synchronous NORMAL;
- a bounded busy timeout;
- STRICT tables where appropriate;
- integrity diagnostics.

**CURRENT:** better-sqlite3 13.0.3 is the chosen implementation driver behind the public abstraction.

---

## 6. Canonical ownership

**CURRENT:** Data owns:

- Data Spaces;
- entity-schema definitions and versions;
- current and soft-deleted structured records;
- record versions and actor attribution;
- normalized relation index state;
- mutation idempotency ledger;
- Data mutation events;
- Data mutation receipts;
- internal database-format migration ledger;
- Data-specific provenance;
- Data canonical workspace database files.

**LAW:** canonical Data databases are user-owned state even when Data created them. Normal disable, update, detach or uninstall must preserve them.

---

## 7. Explicit non-ownership

Data does not canonically own:

- OS workspace identity or system structure;
- Brain goals, intent, strategy or evaluation objects;
- Memory's historical narrative/canonical memories;
- reusable Skills;
- Multiple Bots task/team/worker coordination state;
- external-system truth when Connections names the external system as canonical;
- credentials or secrets;
- Dashboard system identity;
- scheduler/cadence policy;
- app UI/runtime ownership;
- arbitrary host permissions.

**LAW:** Data adapters must consume trusted host authority without claiming ownership of the host's authority model.

---

## 8. Sources of truth

### 8.1 Structured operational facts

**CURRENT:** the workspace AI-Verse Data database is canonical for local_canonical structured records.

### 8.2 Schemas

**CURRENT:** Data's immutable entity-schema versions and current schema pointer are canonical for Data validation.

### 8.3 Provenance

**CURRENT:** Data mutation events and receipts are canonical evidence of Data mutations.

### 8.4 Host/workspace identity

**CURRENT:** native mode derives workspace identity from the trusted OS root plus the validated WORKSPACE.yaml manifest. The caller cannot grant itself authority by supplying a raw database path.

### 8.5 Memory boundary

**CURRENT:** Memory remains a different truth class.

Data events may be evidence for Memory. Memory may retain references such as Data record/event identifiers. That does not make Memory canonical for the current record.

**LAW:** historical recall must not silently override current Data-owned fields.

---

## 9. Runtime model

### 9.1 Host-neutral library

**CURRENT:** the core can be used programmatically through typed module exports.

A host creates a trusted scope and opens Data through the storage/client boundary.

### 9.2 Typed client

**CURRENT:** createDataClient binds:

- a trusted scope;
- an actor;
- authorization context.

It exposes typed Data operations and returns stable envelopes.

**Important enforcement distinction:** the base DataClient validates and carries authorization, but capabilityRefs are not a universal per-operation authorization engine inside the client itself. Consumer-specific adapters perform additional operation-level permission checks.

**LAW:** callers must not infer that authorization metadata alone proves operation permission.

### 9.3 Native OS runtime on reviewed main

**CURRENT:** main can detect a compatible AI-Verse OS, materialize an extension directory, register Data, resolve workspaces, explicitly initialize a workspace through the programmatic native API, discover installed instructions and expose doctor/status.

**CURRENT:** the materialized main engine.mjs is registrationOnly metadata. Instruction discovery reads it but deliberately does not execute it.

**GAP:** therefore the main extension attachment is not itself an executable Data runtime bridge.

### 9.4 In-flight host runtime

**INTENDED:** PR #13 adds ai-verse-data-host/1.0 with:

- workspace discovery;
- explicit workspace initialization;
- scoped Data requests;
- trusted local-operator binding;
- a host session that resolves the real workspace and opens the typed client.

The same PR contains a pinned five-component acceptance workflow that exercises Data through the OS host script rather than importing Data internals directly.

**GAP:** this remains unmerged and unverified by executing CI runners.

---

## 10. Scope and isolation

### 10.1 Trusted roots

**CURRENT:** TrustedDataRoot canonicalizes the filesystem root and rejects unsafe derivation.

### 10.2 Workspace binding

**CURRENT:** a database binding includes:

- binding version;
- kind: workspace or standalone;
- workspaceId.

A bound database opened under a conflicting workspace or binding kind fails with a scope conflict.

### 10.3 Native workspace validation

**CURRENT:** native resolution validates:

- compatible OS v2 host;
- safe workspace identifier;
- real non-symlink workspace directory;
- WORKSPACE.yaml presence and size;
- supported schema major;
- exact manifest ID match;
- active/paused/archived status;
- canonical derived Data path.

### 10.4 Cross-workspace rule

**CURRENT:** one normal Data operation targets one workspace database.

Cross-space references can exist between Data Spaces inside the same workspace database, but cross-workspace transactions are not supported.

**LAW:** no model-supplied path may be used to escape workspace scope.

### 10.5 Same logical workspace on different OS roots

**CURRENT:** two separate trusted roots may each contain the same logical workspace ID and remain physically isolated.

---

## 11. Current lifecycle

### 11.1 Package availability

**CURRENT:** package metadata supports Node 22+ and GitHub dependency installation. It remains version 0.1.0-alpha.0 and UNLICENSED.

### 11.2 Install

**CURRENT:** ai-verse-data install --root <os-root>:

- requires a compatible OS;
- materializes Data-owned local extension files;
- updates only Data's extension-registry entry;
- uses an exclusive registry lock;
- re-reads under lock;
- uses lost-update protection;
- atomically replaces registry state;
- preserves unrelated entries and unknown safe metadata;
- does not initialize workspace databases.

### 11.3 Attach/register

**CURRENT:** install/register creates the local extension entry under .aiverse/extensions/registry.json and Data-owned files under .aiverse/extensions/ai-verse-data/.

**LAW:** registration is not health, permission, initialization or authorization.

### 11.4 Enable/disable

**CURRENT on main:** install/update preserve an existing enabled:false state. disable exists.

**GAP on main:** there is no public enable command. Reinstall/update does not intentionally reactivate a disabled extension.

**INTENDED:** PR #13 adds explicit enable while preserving the rule that update does not imply re-enable.

### 11.5 Initialize

**CURRENT:** initWorkspaceData() exists programmatically and creates exactly one requested active workspace database at the canonical path.

It is idempotent when the expected compatible database already exists.

**GAP on main:** the CLI does not expose init, and the materialized extension is not executable. The real native host initialization path therefore depends on the unmerged hardening line.

### 11.6 Status/doctor

**CURRENT:** doctor and status are read-only.

Doctor performs deeper SQLite/integrity/WAL checks. Status is lighter.

**Important distinction:** a report may be healthy while Data is not registered or while the requested workspace database is missing, because those states are currently notices rather than problems.

**GAP:** there is no first-class final readiness verdict that says all of installed + attached + enabled + healthy + scope initialized + authorized are true for the requested operation.

### 11.7 Update

**CURRENT:** update refreshes Data-owned extension material while preserving disabled state and canonical databases.

**LAW:** package update is distinct from database-format migration and user-schema migration.

### 11.8 Disable

**CURRENT:** disable changes only Data's registry availability and preserves extension files and canonical databases.

### 11.9 Uninstall

**CURRENT:** uninstall removes Data-owned extension runtime/registration while preserving canonical workspace databases.

**GAP:** PR #13 includes additional uninstall rollback-safety hardening, which means reviewed main should not be treated as the final hardened uninstall implementation.

### 11.10 Reinstall

**CURRENT:** reinstall can rediscover preserved compatible databases at their canonical workspace paths.

### 11.11 Detach

**CURRENT:** there is no separately named detach command. Uninstall functions as software detachment while preserving canonical Data.

This is acceptable only if documentation consistently describes the semantic distinction.

### 11.12 Reconcile

**GAP:** there is no public Data reconcile/adoption command that examines existing structured stores and decides how to establish one canonical route.

### 11.13 Rollback

**CURRENT:** installer writes contain local rollback/atomicity mechanisms and migrations create safety backup evidence.

**GAP:** there is no unified public lifecycle rollback command.

---

## 12. Migration/history integration

This is the most important incomplete lifecycle area.

### 12.1 Internal database-format migration

**CURRENT:** format v1 can migrate to v2 through an explicit migration framework.

The framework includes:

- migration inspection;
- migration definitions with digests;
- migration ledger;
- pre-migration verified backup;
- incomplete-state detection;
- retry/resume semantics;
- fail-closed normal open until migration completes.

**LAW:** normal open must never silently auto-migrate unknown canonical state.

### 12.2 User-schema migration

**CURRENT:** destructive or shape-changing entity-schema evolution uses explicit preview/execute behavior with:

- bounded planning;
- backfills;
- destructive approval metadata;
- atomic record/schema changes;
- relation-index rebuild;
- idempotent execution;
- provenance.

### 12.3 Older unbound AI-Verse Data databases

**CURRENT:** an older recognized AI-Verse Data database with no scope binding may be bound exactly once when opened with an expected binding.

This is a real backward-compatibility bridge for early unbound Data state.

### 12.4 Already-bound standalone Data

**CURRENT:** a database bound as standalone cannot be reopened as workspace. Binding kind is part of canonical identity and mismatch fails closed.

### 12.5 Backup/export/import binding behavior

**CURRENT:** portable export/import and backup restore preserve binding identity. Destination binding must match the source binding.

That is correct for ordinary restore and prevents accidental cross-workspace import.

**Consequence:** it is not a standalone-to-native adoption mechanism.

### 12.6 Existing native workspace Data

**CURRENT:** reinstall/update discovers a compatible database only at the validated canonical workspace path.

### 12.7 Competing structured stores

**GAP:** there is no supported workflow for:

~~~text
existing standalone AI-Verse Data
+
new native workspace Data target
~~~

or:

~~~text
existing arbitrary agent database
+
AI-Verse Data activation
~~~

that proves which source is canonical, imports/adopts intentionally, verifies the result, retires the old writable route and records an adoption receipt.

### 12.8 Duplicate-canonical prevention

**LAW:** activation must not initialize an empty workspace Data database if eligible pre-existing structured truth is awaiting adoption in a known legacy route.

**GAP:** the current native initializer only reasons about the target canonical path. It does not discover or reconcile a previously bound standalone Data store or arbitrary old-agent structured store.

### 12.9 Native migration command/path

**GAP:** the core migration engine exists, but the current native CLI has no migrate command. PR #13's host engine also focuses on discover/init/request and does not establish a complete operator migration/adoption UX for a migration_required workspace.

This leaves a mismatch between excellent migration machinery and incomplete native product wiring.

---

## 13. Intended lifecycle

**INTENDED:** the seamless lifecycle should be:

~~~text
package available
  -> host compatible
  -> attach/register
  -> explicit enable
  -> discover target scope
  -> discover eligible existing canonical/legacy state
  -> adopt/migrate if required
  -> initialize only if no canonical state exists
  -> verify health/readiness
  -> authorize operation
  -> use

later:
  update
  -> preserve enablement intent
  -> migrate only through explicit plan if required
  -> verify

disable/detach/uninstall
  -> preserve canonical records

reinstall/reconcile
  -> rediscover one canonical store
  -> never create a second editable truth
~~~

**LAW:** initialize-new is the last branch after safe discovery/adoption, not the default answer to unknown legacy state.

---

## 14. Install-order independence

### 14.1 Component metadata coexistence

**CURRENT:** Data's native coexistence tests exercise representative registry orders with Memory, Brain, Multiple Bots, Skills and unrelated extension entries represented as fixtures.

The tests verify:

- only Data's registry entry changes;
- unrelated entries and unknown metadata survive;
- disabled sibling state survives;
- lifecycle creates no databases by itself;
- seeded Data survives disable/update/uninstall/reinstall;
- tracked OS files remain unchanged.

### 14.2 Real ecosystem order

**CURRENT:** the merged release-hardening line plus subsequent Agent Distribution clean-machine gates prove real multi-repository composition. Distribution A-F additionally exercises Data through the accepted host path and destructive boundary.

---

## 15. Activation/adoption by existing agents

### 15.1 Fresh native workspace

**CURRENT core capability:** Data can explicitly initialize a fresh active workspace through its native API.

**CURRENT product path:** the OS/Data host bridge is merged and accepted; safe structure ensure can initialize/evolve only the admitted additive structure.

### 15.2 Agent that already has AI-Verse Data at the canonical path

**CURRENT:** compatible state is rediscovered and reopened.

### 15.3 Agent that has an old unbound AI-Verse Data database

**CURRENT low-level capability:** one-time binding exists.

**GAP:** there is no end-user adoption command that safely locates, previews and performs this transition in the native host workflow.

### 15.4 Agent that has a bound standalone Data database

**GAP:** no supported native adoption exists.

### 15.5 Agent that has structured truth in another database/system

**GAP:** no generic legacy importer exists. This should remain explicit, schema-aware and provenance-preserving rather than becoming unsafe automatic database copying.

### 15.6 Canonical handover requirement

**LAW:** adoption must be a visible authority handover. After successful adoption, exactly one route is writable as canonical for the adopted structured responsibility.

---

## 16. Portability outside AI-Verse OS

**CURRENT:** the core engine is host-neutral enough to use outside AI-Verse OS programmatically.

Strong portability traits include:

- storage-neutral protocol;
- trusted scope abstraction;
- driver boundary;
- standalone scope;
- actor/authorization passed by host;
- no dependency on Memory or Brain for core CRUD/query;
- SQLite local storage;
- typed client.

**CURRENT limitation:** the native CLI lifecycle deliberately requires AI-Verse OS and does not silently fall back to standalone mode.

**INTENDED in PR #13 docs:** the first member beta treats Data-before-OS as package availability before later attachment, not as creating a random standalone canonical store and guessing how to merge it later.

**GAP:** if standalone usage is offered as a real user product again, it needs an explicit adoption/migration contract before it can be claimed install-order seamless with native OS.

---

## 17. Sibling integrations

### 17.1 OS

**CURRENT:** compatibility detection, local extension registration, workspace resolution, native health and lifecycle exist.

**CURRENT:** executable host bridge is merged, callable and accepted. OS invokes Data through its supported engine rather than opening SQLite.

### 17.2 Brain

**CURRENT:** Data provides a read-only Brain adapter for structured queries/aggregates and provenance.

**LAW:** Brain may reason over Data without becoming Data's owner.

**INTENDED hardening:** PR #13 further scopes provenance visibility and documents the trusted-host authorization boundary.

### 17.3 Memory

**CURRENT:** Memory bridge provides stable Data references and candidate/evidence structures without automatically writing Memory.

**LAW:** Data events are audit facts, not automatic memories.

**GAP on main:** PR #13 repairs exact event lookup beyond the first bounded event page and tightens evidence/reference consistency. Until merged, current main's Memory evidence path is not the final hardened contract.

### 17.4 Multiple Bots

**CURRENT:** Bots adapter applies lease/capability checks over the typed client and preserves task-linked provenance.

**GAP on main:** PR #13 identifies provenance-scope leakage paths and adds secure wrapping.

### 17.5 Apps

**CURRENT:** Apps declare Data needs and receive a scoped kit. App uninstall preserves Data.

**Known current defect:** nested transaction/bulk operations can classify delete as update on main, allowing delete authority to tunnel through a kit that deliberately does not grant delete.

**INTENDED:** PR #13 closes this defect.

**LAW:** nested operations must never inherit broader authority than the outer adapter intended.

### 17.6 Dashboard

**CURRENT:** read-only projections expose spaces, schemas, records, aggregates, events and health without exposing raw DB paths.

**INTENDED hardening:** PR #13 corrects cross-space reference resolution and wrapper state behavior.

### 17.7 Connections

**CURRENT:** Connections authority supports explicit one-way import with external source references and provenance. It does not silently implement bidirectional sync.

**LAW:** importing an external record does not make the local copy canonical unless authority semantics explicitly say so.

### 17.8 Automation

**CURRENT:** committed Data events can be polled as facts.

**LAW:** Data emits facts. It does not become the scheduler or recurrence engine.

---

## 18. Permissions, security and privacy

### 18.1 Host-bound authority

**CURRENT:** actor and authorization context come from the host boundary.

Registration itself grants no Data permission.

### 18.2 Capability adapters

**CURRENT:** Bots and Apps add adapter-specific capability checks.

**Known current issue:** main contains adapter paths where nested operations or provenance queries are insufficiently scoped. PR #13 contains explicit repairs.

### 18.3 Permanent permission law

**LAW:** effective authority must be rechecked at the actual operation being executed, including every operation nested inside transaction/bulk envelopes.

The safe model is:

~~~text
host policy
INTERSECT
workspace policy
INTERSECT
principal grant
INTERSECT
task/app lease or manifest grant
INTERSECT
operation-specific Data policy
~~~

Delegation may narrow authority. It may never increase it.

### 18.4 Provenance visibility

**LAW:** read access to receipt/event provenance must be at least as scoped as read access to the underlying record/entity. Hidden-vs-nonexistent resources should not become an existence side channel.

### 18.5 SQL boundary

**CURRENT:** normal public protocol/client operations do not accept raw SQL or arbitrary canonical database paths.

### 18.6 Filesystem containment

**CURRENT:** native roots, extension paths, workspaces and canonical DB paths reject traversal, unsafe absolutes, symlink escape and malformed identifiers.

### 18.7 Secrets

**CURRENT:** Data records may contain references, but Data is not intended to become the canonical secret vault.

### 18.8 Local-first

**CURRENT:** canonical workspace databases are local files by default. Portability artifacts are explicit.

---

## 19. Failure and degraded modes

### 19.1 Database identity conflict

Fail closed.

### 19.2 Scope conflict

Fail closed. No silent rebind.

### 19.3 Format migration required

Normal open fails until explicit migration.

### 19.4 Incomplete migration

Fail closed and diagnose.

### 19.5 Corruption

Quarantine/write blocking plus diagnostic recovery path.

### 19.6 Recovery

**CURRENT:** recovery can inspect and stage a verified candidate into a separate destination with the same binding.

**GAP:** promotion is explicitly manual-explicit-not-implemented. There is no supported atomic product-level promotion/rollback transaction that replaces a damaged canonical DB after staging.

### 19.7 Missing Data database

Native discovery reports missing.

Initialization must be explicit.

### 19.8 Disabled extension

Runtime selection should not expose Data.

### 19.9 Registry lock contention

Fail closed. Stale locks are not stolen.

### 19.10 CI infrastructure failure

**CURRENT evidence:** main head Actions run 34695862605 is red. Five of six matrix legs passed; ubuntu Node 22 failed before retrievable step/log evidence.

**HISTORICAL / PR evidence:** PR #13 records the same no-step runner failure pattern across CI, Release Smoke and Five-Component Release Acceptance and attributes it to account/hosted-runner eligibility rather than a deterministic code failure.

**LAW:** infrastructure failure may be classified accurately, but a red/unexecuted gate must never be relabeled green.

---

## 20. Important historical repairs

### 20.1 Storage identity hardening

**HISTORICAL:** early storage work established explicit application/user versions and fail-closed handling for unrelated SQLite files.

**Law established:** database format identity must be machine-verifiable.

### 20.2 One-time binding of early unbound databases

**HISTORICAL:** scope work added a safe bridge from the earliest unbound AI-Verse Data database shape to explicit scope binding.

**Law established:** backward compatibility can add identity once, but later identity changes must not be guessed.

### 20.3 Optimistic concurrency and idempotency

**HISTORICAL:** later phases hardened stale-write handling and durable replay.

**Law established:** retries and competing writers must not silently duplicate or overwrite canonical mutations.

### 20.4 Backup before internal migration

**HISTORICAL:** migration work made verified backup part of migration evidence.

**Law established:** canonical-format migration requires a proven recovery point.

### 20.5 Quarantine and staged recovery

**HISTORICAL:** corruption handling was separated from silent repair.

**Law established:** corrupted canonical state should be diagnosed and staged, not silently rewritten.

### 20.6 Cross-platform repairs

**HISTORICAL:** Phase 5 required multiple macOS/Windows fixes including canonical realpath handling for /var vs /private/var, separator-normalized snapshots and worker-exit/file-lock cleanup behavior.

**Law established:** path identity and lifecycle tests must use platform-real semantics rather than POSIX textual assumptions.

### 20.7 Post-release hardening audit

**HISTORICAL / in-flight:** after main declared FIRST RELEASE COMPLETE, PRs #12 and #13 found real product-path and authorization defects.

PR #13 supersedes #12.

Repairs include:

- Apps delete tunneling;
- Bots/Apps provenance scoping;
- hidden receipt/event existence leakage;
- secure client scope descriptor preservation;
- live closed-state wrapper behavior;
- Memory exact event lookup/evidence binding;
- Dashboard cross-space references;
- record-list cursor rejection;
- Connections/Automation parser hardening;
- uninstall rollback safety;
- explicit enable;
- real host runtime;
- stale lifecycle/release documentation;
- real five-component acceptance workflows.

**Law established:** internal task completion is not enough. Release acceptance must exercise the supported member/host path and adversarial cross-component boundaries.

---

## 21. Permanent laws established by repairs

1. **LAW:** one canonical structured-data owner per responsibility.
2. **LAW:** Data database identity and workspace binding fail closed on mismatch.
3. **LAW:** normal public APIs expose structured operations, not arbitrary SQL or raw canonical paths.
4. **LAW:** package update is separate from database migration.
5. **LAW:** Data migration must have verified backup/recovery evidence.
6. **LAW:** canonical Data survives normal disable, uninstall and reinstall.
7. **LAW:** registration is not permission, health, initialization or authorization.
8. **LAW:** update must not imply re-enable. Re-enable is explicit.
9. **LAW:** nested transaction/bulk operations must re-enforce the same or narrower authority as their parent adapter.
10. **LAW:** provenance visibility must not reveal entities the caller is not authorized to read.
11. **LAW:** Memory may reference Data evidence but does not automatically become Data's mirror.
12. **LAW:** Data events are facts, not an embedded scheduler.
13. **LAW:** native initialization must not create a second canonical store when eligible legacy structured truth requires adoption.
14. **LAW:** recovery staging and canonical promotion are distinct destructive-risk boundaries.
15. **LAW:** release claims require the exact supported host/product path, not only direct internal imports.
16. **LAW:** runner/infrastructure failure does not count as a passing release gate.
17. **LAW:** cross-platform canonical path logic must compare real filesystem identity, not fragile textual assumptions.

---

## 22. Inspirations and curated references

### 22.1 Kylon

**INSPIRATION:** docs/RESEARCH-AND-DECISIONS.md records Kylon as a reference for a first-class structured database/application layer.

The architecture does not simply clone Kylon. AI-Verse Data adds its own ownership, workspace, provenance, migration, host and adapter boundaries.

### 22.2 SQLite

**INSPIRATION:** official SQLite behavior around WAL, isolation, STRICT tables, JSON and integrity materially informs the engine.

SQLite is implementation machinery, not the public Data contract.

### 22.3 better-sqlite3

**INSPIRATION / implementation choice:** selected as the mature Node SQLite driver for the first release.

### 22.4 node:sqlite review

**HISTORICAL research:** Node's built-in sqlite surface was considered but not chosen as the first-release production driver.

**LAW:** technology research is evidence for a decision, not a requirement to adopt every referenced project.

---

## 23. Current gaps and contradictions

### 23.1 Release-complete claim versus current main product path

**Contradiction:** main commit, README, Phase 5 status and release acceptance say first release complete 41/41.

**Current implementation:** materialized extension engine is registrationOnly and release acceptance directly imports internal Data APIs.

**Verdict:** engine/library acceptance is strong, but the claimed full product release is overstated on reviewed main.

### 23.2 PRD says implementation not started

**Contradiction:** docs/PRD.md still says Implementation: Not started despite a large implemented codebase.

**Verdict:** stale documentation.

### 23.3 Public phase markers are stale

**Contradiction:** src/index.ts still reports foundation phase 4.1 while release docs say Phase 5.6 complete.

PR #13 repairs this.

### 23.4 Main lacks enable

**Contradiction:** the lifecycle supports disabled state but has no public main command to reverse it.

PR #13 repairs this.

### 23.5 Programmatic init exists but product path is incomplete

**Contradiction:** docs describe native workspace initialization, but current CLI lacks init and current materialized engine cannot perform it.

PR #13 supplies host init.

### 23.6 Health versus readiness

**Contradiction risk:** doctor healthy can mean the environment is not broken even if Data is unregistered or the scope has no database.

That is valid health semantics but insufficient as a final readiness verdict.

### 23.7 Migration engine versus native migration UX

**Contradiction:** migration machinery is sophisticated, but no native migration/adoption command completes the member path for migration_required or standalone legacy state.

### 23.8 Standalone capability versus native adoption

**Contradiction:** standalone scope exists in the core, but a bound standalone database cannot become a workspace database through current backup/import because binding equality is enforced.

This is safe behavior, but it means seamless adoption is missing.

### 23.9 Recovery staging versus recovery completion

**Contradiction:** staged recovery is implemented, but promotion is explicitly not implemented.

### 23.10 Distribution

**Contradiction:** first release is called complete while package version remains 0.1.0-alpha.0, license remains UNLICENSED, public registry/version/license decisions are deferred, and no latest GitHub release exists.

This may be acceptable for repository-authorized development use, not for an immutable member/public release claim.

### 23.11 CI status

**Contradiction:** release docs say passed, but exact current main head CI is red and the in-flight final hardening workflows are also red/unexecuted due runner infrastructure.

---

## 24. Desired future state

**INTENDED:** Data should feel like a native structured-data capability that can be added at any point without data ambiguity.

A mature operator experience should support:

1. install or make package available;
2. attach/register to the current host;
3. explicitly enable if needed;
4. inspect existing scope and legacy structured state;
5. preview required adoption/migration;
6. back up original canonical evidence;
7. adopt or migrate with provenance;
8. initialize only when there is no existing canonical data to preserve;
9. verify readiness;
10. expose Data dynamically through the host;
11. preserve Data through update/disable/uninstall;
12. safely rediscover it on reinstall;
13. promote a verified recovery candidate through an explicit safe transaction if disaster recovery is required.

The end state should preserve the current strong engine rather than replace it.

---

## 25. Definition of done

Data is truly done for the current seamless AI-Verse milestone when all of the following are true:

### Engine

- core CRUD/query/schema/relations/transactions remain green;
- OCC/idempotency/provenance/bulk remain green;
- backup/export/import remain verified;
- internal and user-schema migrations remain fail closed;
- corruption/recovery remains safe.

### Native host

- the real executable Data extension/host bridge is merged;
- the supported OS host dynamically discovers it;
- install order does not require host config regeneration;
- explicit enable/disable is symmetric.

### Existing state

- native adoption handles an old unbound Data database safely;
- bound standalone Data has an explicit supported adoption/handover route if such state is eligible;
- arbitrary foreign structured stores are either explicitly unsupported with a migration contract requirement or have safe importers;
- two competing canonical structured stores cannot remain writable after adoption.

### Migration

- migration_required has a supported native command/host operation;
- safety backup, execution, verification and receipt are exposed at the product layer.

### Recovery

- staged recovery has a supported explicit promotion/rollback path, or the current milestone explicitly and truthfully documents manual promotion as out of scope.

### Permissions

- PR #13 authority fixes are merged;
- nested transaction/bulk permissions cannot tunnel broader rights;
- provenance cannot leak hidden entity existence.

### Readiness

- health and readiness are clearly distinct;
- the host can determine installed, attached, enabled, healthy, initialized, migration state and authorization for a requested scope.

### Acceptance

- normal CI executes and passes;
- package/CLI smoke executes and passes;
- real five-component acceptance executes and passes through the supported host path;
- post-merge main is green.

### Distribution

- the intended member/public artifact has an explicit version/license/distribution decision;
- immutable release evidence matches the documented architecture.

---

## 26. Contribution to the supreme AI-Verse vision

Data contributes four critical system properties.

### 26.1 Structured truth without turning the OS into a database

It keeps operational state first-class while preserving OS ownership boundaries.

### 26.2 Safe machine mutation

It gives agents typed, bounded, versioned, idempotent mutation semantics rather than letting models edit arbitrary databases.

### 26.3 Provenance

Events and receipts create a durable evidence trail that Brain, Memory, Bots, Apps and automation layers can reference without duplicating canonical records.

### 26.4 Local-first portability

SQLite plus explicit exports make the core portable while the host boundary can remain replaceable.

**LAW:** the supreme system should compose around Data, not absorb Data's canonical store into another component.

---

## 27. Open decisions

1. What exact public command/protocol names should represent Data adoption and native database migration: adopt, activate, migrate, reconcile, or a composed lifecycle transaction?
2. Should standalone-to-workspace adoption rewrite binding in place after a verified backup, export/import into a new canonical file with an adoption receipt, or use another explicit handover format?
3. How should a successfully adopted old store be retired: archive/rename, read-only marker, tombstone manifest, or another durable noncanonical state?
4. What is the supported recovery promotion mechanism after a staged candidate is verified?
5. Should readiness be exposed as a Data command, an OS aggregate lifecycle contract, or both?
6. What exact member distribution mechanism replaces repository-authorized GitHub installation?
7. What version/license state constitutes the first immutable member release?

---

## 28. Current intended milestone

Two repository signals must be reconciled.

**Declared CURRENT milestone on main:** Phase 5.6, Task 41/41, first release complete.

**Effective CURRENT hardening target evidenced by the repository after that declaration:** a five-component beta in which Data:

- installs in different component orders;
- is dynamically discovered by a pre-existing OS host config;
- can explicitly initialize a workspace through the host;
- supports real structured queries through that host;
- can be disabled and explicitly re-enabled;
- preserves canonical records through uninstall/reinstall;
- respects hardened adapter permissions/provenance;
- passes component doctors;
- does not mutate tracked OS state.

That effective target is embodied by open PR #13.

**Verdict:** the first-release engine milestone is substantially complete, but the current product milestone is still in release hardening and is not 100 percent complete.

---

## 29. Current-target readiness verdict

### Overall verdict

**PASS WITH MATERIAL GAPS. NOT YET 100 PERCENT SEAMLESS.**

The engine itself is close to a release-quality first local structured-data layer.

The current blocker is productization/integration rather than a missing database foundation.

### What is already strong

- storage engine;
- schema and CRUD model;
- safe query boundary;
- transactions and OCC;
- idempotency/provenance;
- bulk safety;
- backup/export/import;
- internal migration framework;
- user-schema migration;
- quarantine and staged recovery;
- workspace isolation;
- native registry safety;
- lifecycle preservation of canonical data;
- extensive tests;
- cross-platform hardening history.

### What prevents a 100 percent verdict

1. main's extension engine is not the real host runtime;
2. known adapter/lifecycle defects remain on main and are only fixed in PR #13;
3. PR #13's CI and five-component acceptance have not executed green;
4. bound standalone/legacy adoption is missing;
5. migration_required lacks complete native product wiring;
6. recovery promotion remains manual/unimplemented;
7. readiness is not a first-class combined verdict;
8. distribution remains alpha/unlicensed/GitHub-only rather than immutable member release.

---

## 30. Implementation completeness by dimension

| Dimension | Verdict | Evidence / remaining gap |
|---|---|---|
| ENGINE / CORE | COMPLETE | Real SQLite engine, schemas, CRUD, query, relations, transactions, OCC, idempotency, provenance, bulk |
| ARCHITECTURE / CONTRACT | COMPLETE WITH LIMITATIONS | Strong boundaries, but PRD and some phase markers are stale |
| INSTALL / PACKAGE | COMPLETE WITH LIMITATIONS | GitHub install path works by design; package remains alpha and UNLICENSED |
| HOST INTEGRATION | PARTIAL on main | Compatibility/registry/workspace APIs exist; executable host bridge is only in PR #13 |
| ATTACH / REGISTER | COMPLETE | Safe local extension materialization and registry mutation |
| ACTIVATE / ADOPT | MISSING for legacy structured state | No canonical standalone/old-agent adoption transaction |
| SCOPE INITIALIZATION | COMPLETE WITH LIMITATIONS | Programmatic init is strong; main product path lacks executable host init |
| MIGRATION / LEGACY | PARTIAL | Internal and schema migration engines complete; native migration UX and standalone/foreign adoption missing |
| HEALTH / DOCTOR | COMPLETE WITH LIMITATIONS | Deep read-only checks exist; no final combined readiness verdict |
| PERMISSION / SAFETY | PARTIAL on main | Strong core safety, but known adapter permission/provenance bugs fixed only in PR #13 |
| CROSS-COMPONENT READ | COMPLETE WITH LIMITATIONS | Adapters exist; some scope/reference bugs fixed only in PR #13 |
| CROSS-COMPONENT WRITE | COMPLETE WITH LIMITATIONS | Data mutations are strong; Apps nested-delete authority bug remains on main |
| UPDATE / UPGRADE | COMPLETE WITH LIMITATIONS | Package update safe; DB migration is separate but lacks native product operation |
| DISABLE / DETACH / UNINSTALL | PARTIAL on main | Disable/uninstall preserve data; no enable on main; uninstall hardening only in PR #13 |
| REINSTALL / RECONCILE | PARTIAL | Reinstall rediscovers canonical path; no legacy reconcile/adoption command |
| CROSS-PLATFORM | COMPLETE WITH LIMITATIONS | Matrix and repair history strong; current exact head has one runner failure |
| ACCEPTANCE | PARTIAL / EXTERNALLY BLOCKED | Internal release test exists; real host acceptance in PR #13 is unexecuted due runner infrastructure |
| RELEASE / DISTRIBUTION | PARTIAL | 0.1.0-alpha.0, UNLICENSED, GitHub-only, no immutable current release artifact |
| DOC CONSISTENCY | PARTIAL | PRD, phase constants, lifecycle surfaces and release claims drift from implementation |

---

## 31. Command/lifecycle matrix

| Capability | Required now? | CURRENT main command/path | End-to-end proven on real product path? | Missing work |
|---|---|---|---|---|
| Install | Yes | ai-verse-data install --root | Partly | Real post-hardening host acceptance not green |
| Package before OS | Yes as availability | npm/GitHub package only | Library-level | Must not create competing standalone canonical state |
| Attach/register | Yes | install -> local extension registry | Yes for registration | Main attachment is metadata-only runtime |
| Enable | Yes | None on main | No | Merge explicit enable from PR #13 |
| Disable | Yes | ai-verse-data disable --root | Yes at lifecycle level | Pair with enable and host-discovery acceptance |
| Activate/adopt | Yes for existing agents/state | None | No | Implement explicit canonical adoption/reconcile transaction |
| Initialize | Yes | initWorkspaceData() API | Not through main materialized engine | Merge/verify host init path |
| Discover existing canonical DB | Yes | discoverWorkspaceData() | Yes at target path | Extend to eligible legacy/adoption sources |
| Internal migrate | Yes when required | storage migration API | Core yes, product path no | Native command/host operation |
| User-schema migrate | Yes when required | schema migration API/client | Engine yes | Keep explicit preview/approval product UX |
| Import portable backup | Advanced | backup API | Engine yes | Not a cross-binding adoption mechanism |
| Doctor | Yes | ai-verse-data doctor | Yes as health | Add/compose readiness semantics |
| Status | Yes | ai-verse-data status | Yes as light health | Add/compose readiness semantics |
| Update | Yes | ai-verse-data update | Yes at lifecycle level | Verify with PR #13 real host gate |
| Recovery stage | Yes for corruption | recovery API | Engine yes | Product command and promotion remain incomplete |
| Recovery promote | Required for complete disaster recovery | None | No | Explicit atomic promotion/rollback |
| Detach | Semantically yes | uninstall is effective detach | Partly | Clarify naming/contract |
| Uninstall | Yes | ai-verse-data uninstall | Yes at main test level | Merge rollback hardening from PR #13 |
| Reinstall | Yes | install | Yes for canonical-path DB | Real host acceptance plus legacy reconcile |
| Reconcile | Yes for seamless later adoption | None | No | Implement state discovery/adoption planning |
| Rollback | Required for destructive-risk lifecycle | Internal atomic/backup mechanisms | Not as one operator flow | Define migration/recovery/adoption rollback UX |
| Release verify | Yes | CI + release acceptance | No at current exact state | Restore runners, execute all gates, merge, rerun main |

---

## 32. Exact missing work before seamless operation

The shortest evidence-backed path to "works perfectly together like a glove" is:

### R1. Finish and verify the active hardening line

1. Restore GitHub-hosted runner eligibility/usage so jobs actually start.
2. Rerun PR #13:
   - normal six-leg CI;
   - Release Smoke;
   - Five-Component Release Acceptance.
3. Require actual executed green results, not no-step failures.
4. Review that PR #13 still contains all intended authority/lifecycle/host fixes.
5. Merge PR #13.
6. Rerun the same release gates on main.
7. Update release/status documentation to the merged exact revision.

### R2. Implement native existing-state adoption

Add a supported adopt/reconcile flow that handles at least:

1. canonical workspace DB already present and healthy -> reuse;
2. recognized old unbound AI-Verse Data DB -> preview, backup, bind/adopt with receipt;
3. recognized bound standalone AI-Verse Data -> explicit verified handover into workspace identity without leaving two writable canonical stores;
4. older migratable format -> backup + migrate through a supported product operation;
5. target and legacy store both exist -> fail conflict, never choose silently;
6. unrecognized foreign DB -> explicit unsupported/import-required result, never silently bootstrap over it.

The flow must be idempotent and provenance-bearing.

### R3. Expose native migration

Provide a supported CLI/host operation for migration_required state that:

- previews migration;
- creates/verifies backup;
- executes migration;
- verifies current format and integrity;
- returns a receipt;
- resumes or fails safely after interruption.

### R4. Complete disaster-recovery promotion

Turn staged verified recovery into a supported explicit promotion process with:

- same-binding enforcement;
- pre-promotion backup of current canonical file when possible;
- atomic replacement;
- integrity verification;
- rollback path;
- receipt/provenance.

### R5. Add unified readiness

Expose or compose a readiness result that truthfully distinguishes:

~~~text
package available
host compatible
registered
enabled
engine callable
workspace initialized
database current
database healthy
authorized
ready for requested operation
~~~

Do not weaken existing doctor semantics. Add readiness rather than conflating terms.

### R6. Finish immutable distribution

For the intended member/public milestone:

1. decide version;
2. decide license;
3. decide package/release channel;
4. create an immutable release artifact;
5. ensure its code equals the documented architecture;
6. require the real product-path acceptance gates on that immutable revision.

Until these steps are complete, Data should be described as a strong engine and active beta/release candidate, not a fully finished seamless member release.
