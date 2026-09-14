# Context Ladder and Lossless Memory Implementation Plan

Status: ACTIVE
Created: 2026-09-14
Execution law: one implementation slice at a time
Canonical project rule: GitHub is memory; this file is the execution source of truth.

## 1. Purpose

Upgrade AI-Verse context and Memory with only the missing, measurable ideas worth keeping from Kylon, Graft, and Kilo Memory.

The target is a progressive context ladder:

- L0: current task, current scope, recent raw conversation
- L1: tiny orientation maps/catalogs
- L2: relevant session/fold summaries
- L3: exact targeted Memory/Data/Brain/Skill records
- L4: tightly bounded related-neighbor expansion when benchmarked useful
- L5: exact original source/evidence

Most turns should stop at L0-L2. Exact-sensitive questions must be able to descend to L5.

## 2. Non-negotiable ownership

- Gateway owns raw client session/run conversation history and model context-window assembly.
- Memory owns durable historical memory, session digests, provenance, supersession, and rebuildable Memory recall projections.
- OS owns current scope/current-context authority and host mediation.
- Brain owns goals, strategy, evaluation, and retrieval intent, not historical storage or context-window assembly.
- Data owns structured current domain truth.
- Skills owns executable reusable capabilities.
- Multiple Bots owns Room/Thread/Worker coordination identity.
- No new canonical owner, graph database, vector database, Memory repo, Brain, Gateway, or permanent context service may be introduced.

## 3. Existing AI-Verse behavior that must not regress

Preserve:

- canonical human-readable Markdown atomic Memory;
- disposable/rebuildable SQLite recall index;
- FTS recall;
- operator/workspace isolation;
- current canonical-source indexing in place;
- source identity, source hashes, freshness, and automatic current-source refresh;
- provenance, confidence, importance, authority, recency, deduplication;
- supersession and corrections;
- serialized canonical mutation;
- durable idempotency/effect receipts;
- read/write path and symlink containment;
- migration safety and authority handoff;
- lifecycle install/setup/status/doctor/update/uninstall behavior;
- Memory/Data/Brain/Skills ownership boundaries;
- backward-compatible existing recall callers wherever practical.

## 4. Live-state baseline at project start

Verified on 2026-09-14 before implementation.

| Repository | main head |
|---|---|
| AI-Verse-System | `3ebb89b2347862adf4bff7ccee8d5cf1e2ca950d` |
| AI-Verse-Memory | `ae1d8a0b14a9a8309450789f3d2f04b2a6426a42` |
| AI-Verse-Gateway | `fc654df78e69e497864995f99a3f7a895f149752` |
| AI-Verse-Brain | `dfc6fa56e680b384723d7042c1d54f807e853c66` |
| AI-Verse-OS | `933a6beadf87b646fb8c8e0358aaeea6b0504424` |
| AI-Verse-Multiple-Bots | `9bffdffd07fb8abcea848213642936a23ecf4ecf` |
| ai-verse-distribution | `116aa2d74bb55c4ee00bf6139e98bb345b516b8a` |

Open collision-sensitive work at start:

- System PR #14: Invisible Intelligence plan tracking only.
- OS PR #30: automatic workspace host routing.
- Gateway has active Invisible Intelligence branches for question-gate/workspace-routing but no open PR at the start checkpoint.
- Distribution has active Agent public-beta release work and failing Agent release-gate runs. This project must not touch Distribution while that release is frozen/active.
- Safe Update / Release Train branches exist. This project must consume that machinery later, not replace it.
- No open Memory PR was found at the start checkpoint.
- No active queued/in-progress workflow run was found in the inspected repositories at the start checkpoint.

Before every slice, refresh these facts and adapt to current main.

## 5. Current implementation audit

### Memory

Current Memory already has:

- canonical atomic Markdown;
- strict native operator/workspace scope validation;
- read/write symlink and path containment;
- SQLite `items` plus `source_state` derived projection;
- FTS5 with lexical fallback;
- canonical current-source indexing in place;
- automatic refresh of canonical current sources before recall;
- source identity/version/freshness;
- scoring by lexical relevance, scope, importance, confidence, authority, and recency;
- supersession/corrections/history;
- serialized mutation lock;
- transaction recovery for multi-file mutation;
- durable effect receipts and idempotent atomic writes;
- safe migration and authority handoff;
- current compatibility-gated recall with up to 64 unique FTS terms to preserve late semantic signals.

Missing for this project:

- first-class session digest persistence/retrieval;
- tiny rebuildable Memory map/catalog;
- explicit progressive recall depth;
- exact-source fallback contract above ordinary recall;
- deterministic derived relationship projection and bounded neighbor expansion;
- integrated metrics for context depth and source fallback.

### Gateway

Current Gateway already owns persisted sessions/runs/events/checkpoints and restart recovery. A run stores raw messages. Gateway currently assembles one large system context by concurrently reading OS current context, Memory history through host retrieval, capabilities, and connections, then serializing all results into the runtime prompt. It has no fold tree, recent-tail policy, pressure governor, branch catalog, or progressive retrieval governor yet.

### Brain

Current Brain already:

- uses `ContextAssembler` for bounded ephemeral context;
- builds semantic history/capability queries from the actual cognition request and current canonical context;
- bounds history/capabilities/connections/Brain objects;
- keeps retrieved evidence outside canonical Brain state;
- treats model outputs as proposals behind deterministic authority.

Brain does not need another retrieval engine. Later work should add only a retrieval-depth intent envelope if the runtime demonstrates a real need.

### OS

Current OS host adapter:

- resolves current context through the OS current-context owner;
- validates operator/workspace scope;
- dynamically discovers Memory;
- routes `retrieve_history(query, scope)` to Memory `recall(..., limit=12)`;
- owns no duplicate Memory state;
- mediates capabilities, connections, and action authority.

Later progressive-recall integration should extend this owner-mediated bridge instead of bypassing it.

## 6. Upstream research conclusions

### Kylon ideas worth evaluating/adopting

Useful:

- immutable hierarchical fold cards over raw Gateway history;
- recent raw tail;
- recursive roll-up;
- source coverage references;
- reversible level-by-level unfolding;
- branch-specific catalogs over shared immutable pre-fork history;
- pressure-based soft/hard folding;
- exact-detail behavioral contract: summary is navigation, source is evidence;
- cache-aware avoidance of needless recent-context rewriting;
- audience/scope-safe summary boundaries.

Do not copy Kylon production constants. Its published values are benchmark inputs, not AI-Verse defaults.

### Graft ideas worth evaluating/adopting

Useful:

- compact orientation map before deep source reads;
- summary -> crux/detail -> exact source progression;
- content/source fingerprints for derived freshness;
- derived/rebuildable relationship graph;
- deterministic typed relations where evidence already exists;
- incremental refresh of derived projections;
- bounded active retrieval instead of dumping the entire graph.

Rejected by default:

- code-specific tree-sitter architecture;
- a new graph service/database;
- speculative LLM relationship explosion.

### Kilo Memory ideas worth evaluating/adopting

Useful:

- a small startup/orientation memory surface;
- separate session digest from durable typed memory;
- selective durable promotion;
- bounded targeted recall;
- catalog/browse before heavy recall;
- strict anti-transcript duplication;
- explicit byte/token budgets for injected memory surfaces.

Do not copy Kilo's exact byte, session-count, or summary-length defaults without AI-Verse benchmarks.

## 7. Anti-bloat decision gate

A proposed feature ships only if at least one is proven:

1. materially fewer prompt/context tokens;
2. better recall correctness;
3. better exact-detail recovery;
4. lower irrelevant-context rate;
5. lower source-read count or latency without accuracy loss;
6. safer scope isolation/recovery/debuggability.

If added complexity has no measurable benefit, remove or reject it and record that decision here.

## 8. Slice workflow

For every implementation slice:

1. Re-read this file.
2. Inspect current GitHub state for repositories the slice will touch.
3. Check open PRs, relevant branches, and active workflow runs.
4. Mark exactly one slice `IN PROGRESS`.
5. Commit this plan state before implementation.
6. Implement only that slice.
7. Run focused tests.
8. Fix failures.
9. Run relevant owner acceptance/CI.
10. Record repo, branch, PR, commit SHA, merge SHA, workflow/run IDs, and exact tests.
11. Mark `COMPLETE` only after acceptance passes.
12. Update overall completed/remaining count.
13. Set exactly one `Next: YES` on the next NOT STARTED slice.
14. Commit this plan update before starting that next slice.

Allowed status values:

- NOT STARTED
- IN PROGRESS
- BLOCKED
- COMPLETE

Exactly one implementation slice may be IN PROGRESS.

## 9. Project slices

Total implementation slices: 25
Complete: 4
In progress: 1
Blocked: 0
Remaining after current: 20
Current: B1
Next after current: B2

### Phase A: Memory session digests and selective promotion

#### A1. Session digest persistence foundation

- Status: COMPLETE
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: current Memory mutation lock, containment, authority handoff, effect-receipt machinery
- Goal: create a first-class, compact, scoped, durable session-digest record without duplicating transcripts.
- Design constraints:
  - Memory owns digest persistence.
  - Gateway raw history remains canonical for transcript content.
  - Digest storage must be human-inspectable and scope-contained.
  - Digest identity/source coverage must be deterministic enough for safe idempotency.
  - Reuse Memory's mutation lock and durable effect semantics rather than creating another write authority.
- Acceptance:
  - write/read/list a digest by session/run identity;
  - persist session/run id, scope/workspace, time, topic, concise summary, unresolved items, significant outcomes, source refs, provenance, source coverage, source fingerprint/version where supplied;
  - no raw transcript body is persisted;
  - restart preserves digest;
  - operator/workspace isolation holds;
  - cross-workspace path/symlink escape is rejected;
  - replaying the same effect does not duplicate the digest;
  - same idempotency/effect key with changed payload fails closed;
  - existing atomic Memory and recall behavior is unchanged.
- Tests:
  - new focused digest storage tests;
  - existing Memory scope/isolation tests;
  - existing public-beta hardening tests;
  - full Memory test workflow.
- Risks: accidentally creating transcript ownership in Memory; bypassing mutation serialization; digest filename/scope collisions.
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/a1-session-digests`.
  - PR: #12, merged 2026-09-14.
  - Final PR head: `b290928d1b03bac6598c6ac3c41a89afd9a83fc1`.
  - Merge/main SHA: `fd4770ee39d9999dcce84fcc0b5cbaa3ab347a4f`.
  - Final combined acceptance run: `34834608605`, success, 12/12 jobs green.
  - Post-merge Memory main Test run: `34834745092`, success.
  - Verified Linux/macOS/Windows; Python 3.9/3.12; installer smoke; public-beta acceptance; OS update integration.
  - Collision adaptation: Invisible Intelligence Memory PR #11 appeared during A1; A1 was refactored to avoid editing `scripts/memory.py`, then refreshed onto the merged PR #11 main before final acceptance.

#### A2. Session digest derived indexing and targeted recall

- Status: COMPLETE
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: A1
- Goal: index digests into disposable SQLite and support bounded digest-specific retrieval without changing legacy `recall()`.
- Acceptance:
  - digest-derived index rebuilds from canonical digest files;
  - query can return recent/relevant digests in current scope;
  - derived index deletion/rebuild is lossless;
  - no cross-workspace result leakage;
  - stale/missing canonical digest removes derived result;
  - legacy recall callers preserve existing semantics.
- Tests: digest indexing/rebuild/freshness/scope; legacy recall regression; full Memory CI.
- Risks: overloading atomic-memory ranking; stale derived state.
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/a2-digest-index`.
  - PR: #13, merged 2026-09-14.
  - Final PR head: `84109843236c000bd1540c9e01be6633063823a7`.
  - Merge/main SHA: `08a1fd72d503169cf3f2dd25287fec4b53a12106`.
  - PR acceptance run: `34851187030`, success, 12/12 jobs green.
  - Post-merge Memory main Test run: `34851416852`, success, 12/12 jobs green.
  - Verified Linux/macOS/Windows; Python 3.9/3.12; installer smoke; public-beta acceptance; OS update integration.
  - Derived digest state lives in separate `session_digest_items` / `session_digest_fts` tables and does not enter legacy `recall()`.
  - Canonical digest deletion/change purges or refreshes the derived projection; deleting the shared DB rebuilds established Memory before digest tables are recreated.
  - Standalone hashed-scope digests are rediscovered from canonical files without a second scope catalog.

#### A3. Selective promotion contract

- Status: COMPLETE
- Next: NO
- Repositories: AI-Verse-Memory, AI-Verse-Brain only if classification intent is needed
- Dependencies: A1-A2
- Goal: define/apply bounded promotion of durable facts, decisions, corrections, workflows, and lessons from a digest into existing atomic Memory.
- Acceptance:
  - transient chatter is rejected;
  - durable candidates use existing `write_atomic`, provenance, correction/supersession, evidence refs, effect receipts;
  - no new promotion authority/store;
  - promotions are bounded and idempotent;
  - explicit corrections outrank stale facts.
- Tests: promotion/noop/transient/correction/idempotency/scope tests.
- Risks: memory spam; model classification becoming authority.
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/a3-selective-promotion`.
  - PR: #14, merged 2026-09-14.
  - Final PR head: `2d005f6d6ce1867024770ace838429fcb4810a43`.
  - Merge/main SHA: `d6fe8b7b9cf89f291970a5d54f67079d0d4e4b73`.
  - Final PR Test run: `34853951190`, success, 12/12 jobs green.
  - Post-merge Memory main Test run: `34854174657`, success, 12/12 jobs green.
  - Initial PR run `34853830786` failed only because the public promotion-bound constant was not re-exported after extension load; commit `2d005f6d6ce1867024770ace838429fcb4810a43` fixed that visibility issue and the complete matrix passed.
  - Reused merged Invisible Intelligence `capture_candidate`; no Brain change and no second promotion authority/store.
  - Added bounded `promote_session_digest`, exact digest-scope binding, digest-covered evidence enforcement, deterministic retry identities, and no-partial-write structural validation.
  - Explicit corrections now require a `supersedes` target and use retry-safe serialized two-file supersession with evidence refs and effect receipt; cross-scope supersession is rejected.
  - Normal recall excludes superseded stale history while `include_history=True` preserves it.

#### A4. Gateway completed-session digest handoff

- Status: COMPLETE
- Next: NO
- Repositories: AI-Verse-Gateway, AI-Verse-OS, AI-Verse-Memory
- Dependencies: A1-A3; active Invisible Intelligence OS/Gateway work must be merged/re-read first
- Goal: allow meaningful completed Gateway sessions to submit digest evidence through the supported owner path.
- Acceptance:
  - meaningful completed session can create/update one digest;
  - raw transcript remains Gateway-owned;
  - failure to digest never corrupts or blocks canonical run completion;
  - duplicate completion/recovery is idempotent;
  - scope binding is revalidated at the owner boundary.
- Tests: completed run handoff, restart replay, duplicate completion, scope mismatch, Memory unavailable.
- Risks: coupling run completion to optional Memory; duplicate transcript storage.
- Evidence:
  - Gateway repository: `aiverse-filmmakers/AI-Verse-Gateway`.
  - Gateway branch: `context-ladder/a4-session-digest-handoff`.
  - Gateway PR: #6, merged 2026-09-14.
  - Gateway final PR head: `d48f776bbeadea933fdd69d644bffda71437502b`.
  - Gateway merge/main SHA: `b1d8ea061b2ad430283ee3e03552a9f25d3ab1e5`.
  - Gateway PR CI run `34855532254`: success.
  - Gateway post-merge main CI run `34856496720`: success.
  - OS repository: `aiverse-filmmakers/AI-Verse-OS`.
  - OS branch: `context-ladder/a4-session-digest-owner-route`.
  - OS PR: #36, merged 2026-09-14.
  - OS final PR head after live-state refreshes: `5e3ed1f1fd9520fa4edf335d0e2c82ea6980b3bf`.
  - OS merge/main SHA: `7b9c378ee8edbe05c2c31dc7e071e4c12156de47`.
  - Final OS PR acceptance: Direction Ownership `34856261206`, OS Write Command Boundary `34856261197`, OS Brain Permission Contract `34856261061`, Repository QC `34856261067`, Five-Component Public Beta `34856261099`, Four Repo Acceptance `34856261274`; all success.
  - Post-merge OS main acceptance: Direction Ownership `34856489856`, OS Write Command Boundary `34856489953`, OS Brain Permission Contract `34856489883`, Repository QC `34856491504`, Five-Component Public Beta `34856489865`, Four Repo Acceptance `34856489828`; all success.
  - Four Repo Acceptance initially exposed a stale Memory pin at `1c6acf036d42937e57d94dfe48ac501727861653`, which predates A1 session digests. A4 corrected the audited Memory composition pin to accepted Memory main `d6fe8b7b9cf89f291970a5d54f67079d0d4e4b73`.
  - Gateway persists canonical run completion before optional digest handoff. Handoff failure is retryable and never reopens/fails the completed run.
  - Pending/retryable handoffs survive restart with stable owner idempotency identity.
  - Gateway sends only compact digest content/coverage, never transcript bodies or trusted owner fields.
  - Secret-like completed sessions are deterministically skipped.
  - OS revalidates scope, validates run-bound coverage/fingerprint, derives source refs/provenance/source version/effect identity, and routes to Memory's existing `write_session_digest`.
  - A4 was refreshed twice against concurrent Invisible Intelligence merges, preserving substantial Skill-learning routing and later learned-Skill acceptance instead of overwriting them.

### Phase B: Tiny Memory orientation map

#### B1. Rebuildable Memory map/catalog projection

- Status: IN PROGRESS
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: A2
- Goal: deterministic tiny per-scope orientation map from existing atomic Memory, indexed current sources, and session digests.
- Acceptance:
  - materially smaller than underlying Memory in benchmark fixtures;
  - contains only current authorized scope;
  - deterministic/rebuildable;
  - canonical sources are never modified;
  - stale topics/counts disappear after source removal/update.
- Tests: size, isolation, rebuild equivalence, refresh, no-canonical-write.
- Risks: map becoming a second truth source; over-detailed catalog.
- Evidence: pending.

#### B2. Catalog budget, freshness, and diagnostics

- Status: NOT STARTED
- Next: YES
- Repositories: AI-Verse-Memory
- Dependencies: B1
- Goal: fingerprint, cap, inspect, and safely rebuild the orientation map.
- Acceptance:
  - source fingerprint changes invalidate/refresh map;
  - configured output budget is enforced;
  - diagnostics expose bytes/tokens/source counts without chain-of-thought;
  - deleting the projection and rebuilding yields equivalent truth.
- Tests: fingerprint drift, cap/truncation, diagnostics, rebuild.
- Risks: brittle fingerprinting; orientation that hides critical corrections.
- Evidence: pending.

### Phase C: Progressive Memory recall and exact evidence

#### C1. Versioned progressive recall API

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: A2, B1-B2
- Goal: add progressive depths equivalent to catalog/summary/detail/source while preserving legacy `recall()`.
- Acceptance:
  - default legacy recall behavior unchanged;
  - new API returns bounded structured depth/provenance;
  - catalog can be requested without detail;
  - summary/detail can target relevant records;
  - response exposes whether deeper evidence exists.
- Tests: backward compatibility, depth contracts, budgets, scope.
- Risks: parallel incompatible recall APIs.
- Evidence: pending.

#### C2. Exact-source evidence fallback

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: C1
- Goal: resolve exact authoritative source for precision-sensitive facts rather than treating summaries as evidence.
- Acceptance:
  - exact date/number/path/config/ID/quote/state questions can descend to source;
  - stale source fingerprint is detected before exact result is trusted;
  - source containment/scope is revalidated at read time;
  - missing source yields explicit uncertainty/failure, not guessed detail.
- Tests: exact values, stale source, deleted source, cross-workspace rejection.
- Risks: source retrieval bypassing owner/scope gates.
- Evidence: pending.

#### C3. OS host progressive-history bridge

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-OS, AI-Verse-Memory
- Dependencies: C1-C2; current OS Invisible Intelligence work merged/re-read
- Goal: expose progressive Memory retrieval through OS without bypassing owner mediation.
- Acceptance:
  - old `retrieve_history(query, scope)` still works;
  - new versioned operation can request bounded depth;
  - OS validates scope and Memory component state;
  - no Memory canonical state is copied into OS.
- Tests: old bridge regression, new depth, missing Memory, isolation.
- Risks: breaking Brain/Gateway host protocol.
- Evidence: pending.

### Phase D: Derived Memory relationships

#### D1. Deterministic relationship projection

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: C1
- Goal: add rebuildable SQLite relations only from explicit metadata/provenance.
- Initial candidate types: supersedes, superseded_by, derived_from, evidence_for, same_session, explicit shared entity/workflow/provenance refs.
- Acceptance:
  - relations are derived, removable, rebuildable;
  - every edge has deterministic evidence/provenance;
  - no edge creates canonical fact;
  - scope boundaries are enforced.
- Tests: rebuild, stale edge removal, relation provenance, isolation.
- Risks: graph bloat; accidental inference authority.
- Evidence: pending.

#### D2. Bounded neighbor recall benchmark and ship/reject gate

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Memory
- Dependencies: D1, benchmark harness
- Goal: test whether one-hop tightly bounded neighbor expansion improves representative recall.
- Acceptance:
  - compare direct-only vs bounded-neighbor recall;
  - ship only if correctness improves without unacceptable context/latency inflation;
  - otherwise remove/disable expansion and record rejection evidence.
- Tests: decisions/lessons/corrections, irrelevant-neighbor rate, scope.
- Risks: graph traversal flooding context.
- Evidence: pending.

### Phase E: Gateway lossless fold tree

#### E1. Immutable fold-card and catalog storage foundation

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway
- Dependencies: Gateway live-state re-audit after Invisible Intelligence changes
- Goal: derive immutable fold cards over Gateway-owned raw session messages while keeping original messages intact.
- Acceptance:
  - card has immutable identity, level, scope, ordered child/source refs, coverage, fingerprint, size/token estimates, summary, generator metadata, creation time, validation state;
  - referenced cards are never silently mutated;
  - raw source history remains retrievable.
- Tests: identity/immutability/order/coverage/scope/restart.
- Risks: duplicating raw history; mutable-card branch corruption.
- Evidence: pending.

#### E2. Fold creation and recursive roll-up

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway
- Dependencies: E1
- Goal: fold oldest eligible history into cards and recursively roll adjacent same-level cards when pressure requires it.
- Acceptance:
  - no folding under low pressure;
  - folds are strictly smaller than covered input;
  - coverage is complete and ordered;
  - failed summarization leaves raw history intact;
  - roll-up preserves exact descendant reachability.
- Tests: level-1, recursive levels, not-smaller rejection, failed generator, ordering.
- Risks: lossy summaries; excessive model cost.
- Evidence: pending.

#### E3. Lossless unfold and archive search

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway
- Dependencies: E1-E2
- Goal: support card -> child card -> original message traversal and bounded archive search.
- Acceptance:
  - exact original message content is recoverable;
  - precision questions can force unfold;
  - source fingerprint mismatch fails closed/refreshes derived card state;
  - retrieval never crosses scope/branch visibility.
- Tests: multi-level unfold, exact text recovery, stale source, scope.
- Risks: expensive uncontrolled unfolding.
- Evidence: pending.

#### E4. Recent raw tail and context-pressure governor

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway
- Dependencies: E2-E3
- Goal: preserve a benchmarked recent raw tail and fold based on actual context pressure.
- Acceptance:
  - recent continuity stays verbatim;
  - tail remains bounded;
  - soft threshold schedules eligible fold work;
  - hard threshold folds enough before invocation;
  - thresholds are configurable/testable;
  - cache-sensitive recent context can be skipped when safe;
  - no Kylon numeric constant is copied without benchmark evidence.
- Tests: low/soft/hard pressure, tail boundary, cache-sensitive skip, huge-turn emergency.
- Risks: prompt overflow; cache churn.
- Evidence: pending.

#### E5. Fold guards, recovery, and diagnostics

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway
- Dependencies: E1-E4
- Goal: enforce card quality/scope/fingerprint/budget guards and expose advanced diagnostics.
- Acceptance:
  - invalid coverage/order/scope/fingerprint/metadata/size fails closed;
  - restart preserves catalogs/cards and recovery state;
  - diagnostics expose context tokens by layer, cards used, source refs, retrieval depth, exact fallback reason;
  - no chain-of-thought is exposed.
- Tests: guard matrix, restart, corrupted card, diagnostics schema.
- Risks: diagnostics leak content/authority.
- Evidence: pending.

### Phase F: Cheap branch/fork catalogs

#### F1. Copy-on-write branch catalog evaluation and implementation/rejection

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway; AI-Verse-Multiple-Bots only for identity integration if required
- Dependencies: E1-E5; current Bots main re-audit
- Goal: share immutable pre-fork cards/sources while branch catalogs diverge without copying entire history.
- Acceptance:
  - pre-fork immutable history is shared;
  - divergent branch history remains isolated;
  - straddling coverage is safely expanded/backfilled;
  - no summary visible in a branch contains source content unauthorized for that branch;
  - if current AI-Verse branch model gains no measurable benefit, reject and document rather than ship.
- Tests: fork point, independent later folds, mixed-scope rejection, no-copy size benchmark.
- Risks: declassification through summary inheritance; coordination ownership theft.
- Evidence: pending.

### Phase G: Gateway progressive context governor

#### G1. Progressive model-context assembly

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway, AI-Verse-OS
- Dependencies: B1, C1-C3, E1-E5
- Goal: replace unconditional history dumping with L0/L1 first and bounded escalation to deeper layers.
- Acceptance:
  - ordinary turns start with current/recent + tiny orientation only;
  - summary/detail/source reads happen only on demonstrated need;
  - deeper requests are bounded and owner-routed;
  - exact-sensitive retrieval descends to source;
  - runtime prompt records retrieval provenance/diagnostics, not hidden reasoning.
- Tests: short conversation no-deep-read, old fact, exact fact, irrelevant-context rate, source-read count.
- Risks: under-retrieval harming answers; model repeatedly requesting depth.
- Evidence: pending.

#### G2. Runtime deep-retrieval tool/loop

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Gateway, AI-Verse-OS
- Dependencies: G1
- Goal: give the runtime one bounded mechanism to request deeper context without direct owner bypass.
- Acceptance:
  - allowed depths/limits enforced;
  - tool cannot widen scope/permissions;
  - repeated equivalent retrieval is deduplicated/cached per run where safe;
  - source reads are auditable.
- Tests: depth request, scope escape, over-budget, repeated request, exact fallback.
- Risks: retrieval loops and token blowup.
- Evidence: pending.

### Phase H: Brain retrieval intent

#### H1. Retrieval-intent envelope ship/reject gate

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Brain
- Dependencies: G1-G2
- Goal: determine whether Brain needs to express orientation/summary/detail/exact_evidence intent without becoming a retrieval engine.
- Acceptance:
  - benchmark current purpose-based retrieval vs explicit depth intent;
  - if useful, add a bounded declarative intent only;
  - if not materially useful, make no Brain change and record rejection.
- Tests if shipped: schema validation, deterministic bounds, no scope/permission bypass, runtime integration.
- Risks: duplicate retrieval planning.
- Evidence: pending.

### Phase I: Graft-style cross-owner orientation

#### I1. Tiny cross-owner map ship/reject gate

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-OS and AI-Verse-Gateway only if benchmark proves missing value
- Dependencies: G1-G2, current OS context re-audit
- Goal: evaluate a tiny derived scope map referencing goals, Memory topics, Data spaces, Skills, Bots, recent sessions, and important sources.
- Acceptance:
  - first prove existing OS/Gateway context is insufficient;
  - if shipped, map is tiny, derived, rebuildable, fingerprinted, owner-referenced, and contains no duplicate canonical truth;
  - otherwise record explicit rejection as bloat.
- Tests if shipped: freshness, owner refs, scope, rebuild, size.
- Risks: creating a second canonical workspace graph.
- Evidence: pending.

### Phase J: Benchmark, integrated acceptance, release handoff

#### J1. Context/recall benchmark harness

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-Memory, AI-Verse-Gateway, AI-Verse-System
- Dependencies: enough preceding features to compare before/after
- Goal: deterministic representative benchmark suite.
- Required scenarios:
  1. recent conversation;
  2. fact ~50 turns old;
  3. very old prior session;
  4. corrected fact;
  5. exact number/date/path/config;
  6. repeated project/client context;
  7. two similar workspaces;
  8. branched conversation;
  9. very large history;
  10. canonical source changed after derived artifact.
- Metrics:
  - context tokens;
  - recall correctness;
  - exact fact recovery;
  - long-history recovery;
  - irrelevant-context rate;
  - retrieval latency;
  - context construction latency;
  - source reads;
  - scope leakage;
  - restart behavior;
  - derived rebuild behavior.
- Acceptance: reproducible baseline and candidate outputs with machine-readable result.
- Evidence: pending.

#### J2. Cross-owner integrated acceptance

- Status: NOT STARTED
- Next: NO
- Repositories: all changed runtime owners
- Dependencies: all retained implementation slices
- Goal: prove the composed AI-Verse runtime consumes the architecture safely.
- Mandatory acceptance:
  - short conversation avoids unnecessary folding/deep retrieval;
  - long conversation folds old context and keeps recent tail raw;
  - very old exact detail descends from summary to source;
  - Memory catalog orients without atomic dump;
  - prior session digest works without transcript duplication;
  - only durable items promote;
  - corrections supersede correctly;
  - workspace isolation is strict;
  - retained branch sharing is safe;
  - derived map/edge/index rebuild preserves canonical state;
  - stale source refreshes/fails closed;
  - restart preserves required durable state;
  - exact evidence contract is enforced.
- Evidence: pending.

#### J3. Regression, performance, and anti-bloat gate

- Status: NOT STARTED
- Next: NO
- Repositories: all changed runtime owners
- Dependencies: J1-J2
- Goal: remove features that do not earn their complexity.
- Acceptance:
  - no ownership/safety/lifecycle regression;
  - long-history context usage materially improves;
  - recall/exact recovery is not worse;
  - retained relationship/branch/cross-owner features each have benchmark evidence;
  - rejected features are removed, disabled, or documented as intentionally not shipped.
- Evidence: pending.

#### J4. Immutable release handoff

- Status: NOT STARTED
- Next: NO
- Repositories: AI-Verse-System, changed component repos, ai-verse-distribution only after frozen release work clears
- Dependencies: J1-J3; Safe Update/Release Train availability
- Goal: merge accepted component changes and hand exact immutable SHAs to canonical release machinery.
- Acceptance:
  - every changed component main is green;
  - plan records PRs, merge SHAs, workflow IDs;
  - release uses existing Distribution/Release Train process;
  - no ad-hoc release mechanism is invented;
  - final report can be reconstructed from this file alone.
- Evidence: pending.

## 10. Benchmark targets and decision thresholds

Do not predeclare fake percentage wins. Capture baseline first.

A retained feature must show a material directionally positive result in its target metric without violating:
- zero scope leakage;
- exact-evidence recovery correctness;
- canonical ownership;
- restart/rebuild safety;
- backward compatibility where promised.

For long-history context specifically, the project expects a material token reduction. The exact acceptance threshold will be frozen in J1 after baseline measurement, before judging the candidate.

## 11. Known deliberate non-goals

- no vector database by default;
- no Neo4j;
- no second canonical knowledge graph;
- no transcript duplication into Memory;
- no tree-sitter dependency for general AI-Verse Memory;
- no speculative all-to-all LLM relationship graph;
- no user-facing fold-depth controls;
- no new canonical branch owner;
- no replacement of Invisible Intelligence/Grandma UX work;
- no replacement of Safe Update/Release Train work.

## 12. Evidence ledger

### Project setup / research checkpoint

- Status: COMPLETE
- Live repo heads: recorded in section 4.
- Open collision work: recorded in section 4.
- Memory current tests on main: latest inspected Test workflow on `ae1d8a0b14a9a8309450789f3d2f04b2a6426a42` succeeded.
- Gateway current CI on main: latest inspected CI succeeded.
- Brain current CI on main: latest inspected relevant runs succeeded.
- OS current main had no active run at checkpoint; active PR #30 checks inspected as passing.
- Multiple Bots current main CI inspected as passing.
- Distribution Agent release gate had recent failures and is explicitly excluded from current work.
- Upstream research refreshed on 2026-09-14:
  - Kylon "Fold, don't forget" architecture and benchmark article;
  - current `trailhq/Graft` README and implementation surfaces for fingerprints/cards/graph/ask;
  - current `Kilo-Org/kilocode/packages/kilo-memory` implementation including session digests, typed consolidation, budgeted recall index, topics, and session storage.
- Plan branch: `context-ladder/implementation-plan`.
- Initial plan commit: `6380b103f19d36758dfdf03e33b1e2cf69e4ef02`.

## 13. Immediate execution pointer

Current implementation slice: **B1. Rebuildable Memory map/catalog projection**

Do not start B2 until:
- the orientation map is derived only from current authorized Memory/indexed-source/session-digest evidence;
- map deletion/rebuild is lossless;
- source removal/update removes stale map topics/counts;
- canonical Memory/source files are never modified by map generation;
- representative fixtures prove the map is materially smaller than underlying source content;
- full Memory CI is green;
- B1 exact commit/PR/merge/run evidence is written here.


### Slice start checkpoint: A2

Verified before A2 implementation on 2026-09-14:

- AI-Verse-Memory main: `fd4770ee39d9999dcce84fcc0b5cbaa3ab347a4f`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34834745092`: success.
- A1 session digest persistence is present on main and final combined CI passed.
- AI-Verse-System main had advanced to `e62211b8e0a143bf5415da3088b281460b915458`; this plan branch is refreshed onto that live state before A2 code changes.
- System Contract Validation is currently failing on main itself; this is pre-existing and not an A2 Memory gate.


### Slice completion checkpoint: A2

Verified on 2026-09-14:

- AI-Verse-Memory PR #13 merged.
- PR head: `84109843236c000bd1540c9e01be6633063823a7`.
- Memory main after merge: `08a1fd72d503169cf3f2dd25287fec4b53a12106`.
- PR Test run `34851187030`: success, 12/12 jobs.
- Post-merge main Test run `34851416852`: success, 12/12 jobs.
- A2 acceptance proved targeted digest relevance/recency, workspace isolation, canonical deletion purge, canonical change refresh, lossless derived-DB rebuild, standalone scope recovery, and legacy `recall()` non-regression.
- A3 remains NOT STARTED and is the next slice.


### Slice start checkpoint: A3

Verified before A3 implementation on 2026-09-14:

- AI-Verse-Memory main: `08a1fd72d503169cf3f2dd25287fec4b53a12106`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34851416852`: success, 12/12 jobs.
- AI-Verse-Brain main: `619dd17daac9c1bd7eaf4381a5889e56ab05ec59`.
- Brain PR #21 (`invisible-intelligence/learning-candidate-gate`) is open and has active CI. A3 will not touch Brain unless Memory-only reuse proves impossible.
- Invisible Intelligence safe historical capture is already merged into Memory; A3 must adapt to that implementation rather than create another durable promotion authority.
- AI-Verse-System main: `7c59359a98f44a223fcf0e09c9126cc4a84075fa`.
- System Contract Validation is failing on main itself and remains a pre-existing plan-repo issue, not an A3 Memory gate.


### Slice completion checkpoint: A3

Verified on 2026-09-14:

- AI-Verse-Memory PR #14 merged.
- PR head: `2d005f6d6ce1867024770ace838429fcb4810a43`.
- Memory main after merge: `d6fe8b7b9cf89f291970a5d54f67079d0d4e4b73`.
- Final PR Test run `34853951190`: success, 12/12 jobs.
- Post-merge main Test run `34854174657`: success, 12/12 jobs.
- A3 proved durable-vs-transient admission, bounded promotions, evidence coverage, replay idempotency, no-partial-write structural validation, correction supersession, history preservation, and workspace isolation.
- Brain was intentionally unchanged because the already-merged Memory admission gate was sufficient.
- A4 is the next slice.


### Slice start checkpoint: A4

Verified before A4 implementation on 2026-09-14:

- AI-Verse-Gateway main: `7cc1617aeac6caefce627842f5bbe1620c960d5f`; no open PRs or active workflows; latest main CI `34851000522` succeeded.
- AI-Verse-OS main: `1162fbb754ec55a562add9d049b33d44133ec8f2`; no open PRs or active workflows; current public-beta/ownership/boundary workflows succeeded.
- AI-Verse-Memory main: `d6fe8b7b9cf89f291970a5d54f67079d0d4e4b73`; no open PRs or active workflows; post-A3 main Test run `34854174657` succeeded.
- Gateway Invisible Intelligence memory-routing work is already merged into current main and must be consumed, not recreated.
- A4 begins only after re-reading current Gateway completion/session persistence and current OS/Memory owner-routing seams.


### Slice completion checkpoint: A4

Verified on 2026-09-14:

- AI-Verse-Gateway PR #6 merged at `b1d8ea061b2ad430283ee3e03552a9f25d3ab1e5`; post-merge CI `34856496720` succeeded.
- AI-Verse-OS PR #36 merged at `7b9c378ee8edbe05c2c31dc7e071e4c12156de47`.
- All six OS post-merge owner/composition gates succeeded: `34856489856`, `34856489953`, `34856489883`, `34856491504`, `34856489865`, and `34856489828`.
- Canonical Gateway run completion precedes optional digest handoff; failed Memory handoff is retryable and does not corrupt completion.
- Restart recovery retries only completed runs with pending/retryable digest state and preserves idempotency.
- Raw session transcript remains Gateway-owned. Memory receives compact digest evidence only.
- OS is the trusted routing boundary for scope/provenance/effect identity and invokes Memory's existing digest owner API.
- Concurrent Invisible Intelligence Skill-learning changes were preserved across live-state refreshes.
- B1 is the next slice.


### Slice start checkpoint: B1

Verified before B1 implementation on 2026-09-14:

- AI-Verse-Memory main: `d6fe8b7b9cf89f291970a5d54f67079d0d4e4b73`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34854174657`: success, 12/12 jobs.
- A1-A4 are accepted and merged; B1 touches Memory only.
- AI-Verse-System main advanced to `fd7dac7bf210c3deeb2598471ed9cdd988c3f8e4`; its only change since the previous plan refresh is the separate Invisible Intelligence/Grandma UX plan file, so this context-ladder plan can refresh without collision.
- System Contract Validation remains failing on main itself and is a pre-existing System-plan issue, not a B1 Memory gate.
