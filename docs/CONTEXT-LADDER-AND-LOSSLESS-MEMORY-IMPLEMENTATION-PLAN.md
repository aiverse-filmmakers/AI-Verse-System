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
Complete: 13
In progress: 1
Blocked: 0
Remaining after current: 11
Current: E3
Next after current: E4

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

- Status: COMPLETE
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
- Evidence:
  - Core repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Core branch: `context-ladder/b1-orientation-map`.
  - Core PR #15, merged 2026-09-14.
  - Core PR head: `443b63c992c12909620205961fd1d6bf71a80c7a`.
  - Core merge/main SHA: `3fceb2a41eb33db5aef539cc668470e1d43d74be`.
  - Core PR Test run `34857742063`: success, 12/12 jobs green.
  - Orientation projection is disposable SQLite derived from active atomic Memory metadata, refreshed indexed current-owner sources, and canonical session-digest projection.
  - Projection contains compact routing metadata only: counts, Memory types, source kinds/routes, explicit tags/topics, and recent digest pointers. It does not copy atomic text, current-source bodies, digest summaries, or raw transcripts.
  - Tests prove strict workspace/operator visibility, deterministic rebuild equivalence, projection deletion/rebuild recovery, stale signal removal after canonical changes, no canonical rewrites, and representative output more than 4x smaller than authoritative source bytes.
  - Core post-merge run `34859761890` exposed a pre-existing serialized canonical-write lock weakness under Windows contention. B1 acceptance remained open until that owner-boundary weakness was resolved rather than accepting a flaky gate.
  - PR #16 head `65158027b60b48c412e60502de99ab7a46b091d9`, merge `4f5d500d8b758433b1b67aa09983780ed6bae261`; PR run `34860235855` succeeded. Wait budget changed from total queue age to holder-progress age.
  - PR #17 head `986e5aa2d744832f78fd2a37d8274fded33f126e`, merge `33dbcec3a257ed3bba4913968a1d30b0436951b3`; PR run `34867418069` succeeded. Healthy-holder wait was widened while retaining the stale-lock ceiling.
  - PR #18 head `0c38b26218a6ee4ef5856d2bfeb902260f706d85`, merge `597cc9d04e9588c03360fcd284c8b053c5a0ed7a`; PR run `34867815048` succeeded. Synthetic progress timing was made scheduler-stable without changing production semantics.
  - PR #19 head `bd90e6e1a4954d62281eacc3c9bd50aaf409bb15`, merge `d0452bb318ec5cffe00e3ecaf18d670ffc89d172`; PR run `34868413374` succeeded. Normal canonical mutations now incrementally synchronize changed atomic rows instead of rebuilding all derived SQLite state, with full canonical rebuild fallback when the disposable DB is absent.
  - PR #20 head `7bb1a3044143c952e714ffbe85731488b001a79c`, merge/final Memory main `ced610cdacef0df50cc8ee16a4cf886240f257ce`; PR run `34869169369` succeeded 12/12. Lock semantics now use a bounded 120-second live-owner lease, 2-second dead-process grace, holder-progress reset, and the 600-second ambiguous stale-lock threshold.
  - Final post-merge Memory main Test run `34869401845`: success, 12/12 jobs green across Linux/macOS/Windows, Python 3.9/3.12, installer smoke, public-beta acceptance, and OS update integration.
  - Final accepted B1 Memory main: `ced610cdacef0df50cc8ee16a4cf886240f257ce`.

#### B2. Catalog budget, freshness, and diagnostics

- Status: COMPLETE
- Next: NO
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
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/b2-catalog-budget-freshness`.
  - PR #21, merged 2026-09-14.
  - Final PR head: `fd51a7d6b39528de2ce60773a406544ffad79a42`.
  - Merge/main SHA: `15e81e3958b7f6b69fdf63021556706004bdb8a6`.
  - PR Test run `34871933644`: final conclusion success on attempt 2. Attempt 1 had one Windows Python 3.12 full-suite runner stall in the pre-existing 8-writer concurrency test; the same Windows 3.12 focused public-beta acceptance passed in that attempt, Windows 3.9 full suite passed, and the unchanged Windows 3.12 job rerun `104071952512` passed completely.
  - Post-merge Memory main Test run `34872782122`: success, 12/12 jobs green.
  - Orientation schema v2 now carries deterministic `source_fingerprint` evidence over only authorized atomic Memory versions, refreshed current-source versions, and canonical session-digest versions.
  - Unrelated workspace changes do not perturb another workspace fingerprint; authorized atomic/current-source/digest changes do.
  - Public orientation reads rebuild from current owner evidence and overwrite stale stored projection rows rather than trusting cached derived state.
  - Serialized UTF-8 output is hard-bounded by `max_bytes` or `AI_VERSE_ORIENTATION_MAP_MAX_BYTES`, default 8192 and supported range 1024-65536.
  - Deterministic budget pressure removes only optional route-path samples, older session pointers, lower-ranked topics, then route entries while preserving scope, fingerprint, counts, Memory-type counts, and source-kind counts.
  - `get_orientation_map_diagnostics` exposes bytes, transparent byte-based token estimate, budget, truncation, freshness, source counts, visible-scope count, and returned-entry counts without canonical content or hidden reasoning.
  - Existing B1 isolation/rebuild/no-canonical-write behavior remains green.

### Phase C: Progressive Memory recall and exact evidence

#### C1. Versioned progressive recall API

- Status: COMPLETE
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
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/c1-progressive-recall`.
  - PR #22, merged 2026-09-14.
  - Final PR head: `735b89c69e69f2bf0f7fdbac62308c17c0bffc54`.
  - Merge/main SHA: `25c7304aa9e288dc2f8b747e7b453b76cfd5c500`.
  - PR Test run `34877283843`: success, 12/12 jobs green.
  - Post-merge Memory main Test run `34877535172`: success, 12/12 jobs green.
  - Added one additive `memory.progressive-recall.v1` surface; legacy `recall()` implementation and caller contract remain unchanged.
  - `catalog` reuses the B2 orientation projection rather than introducing a second catalog/index.
  - `summary` and `detail` reuse existing scoped session-digest recall plus existing scoped Memory/current-source recall.
  - Progressive responses are query-bound, provenance-bearing, item-capped, and deterministically hard-bounded by serialized UTF-8 bytes.
  - Workspace isolation is preserved and the progressive API exposes no all-workspace mode.
  - Each returned item carries available evidence pointers and whether deeper evidence exists.
  - `source` is advertised as the next depth from detail but remains unavailable in C1; summaries/details are explicitly navigation/bounded detail, not exact evidence.
  - Tests prove catalog reuse, summary/detail contracts, deterministic budgets, Alpha/Beta isolation, version/depth/query fail-closed behavior, evidence pointers, and legacy-recall non-regression.

#### C2. Exact-source evidence fallback

- Status: COMPLETE
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
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-Memory`.
  - Branch: `context-ladder/c2-exact-source`.
  - PR #23, merged 2026-09-14.
  - Final PR head: `62444f253532255eaf5d3b8795fae802285d988c`.
  - Merge/main SHA: `2606bf6524fd67b4a3930fb7d98de54a3d483fb1`.
  - PR Test run `34878580347`: final success on attempt 2. Attempt 1 failed only in the pre-existing synthetic Windows Python 3.9 mutation-lock queue test; every C2 exact-source test had already passed, Windows Python 3.12 full suite passed, and the unchanged Windows 3.9 rerun `104093425179` passed completely.
  - Post-merge Memory main Test run `34879367921`: final success on attempt 2, 12/12 jobs green. Attempt 1 was externally interrupted after four minutes in the pre-existing 8-writer Windows Python 3.12 concurrency test after all C2 exact-source tests passed; unchanged rerun job `104109959305` passed completely.
  - `memory.progressive-recall.v1` now supports `depth="source"` through the same API and requires the prior detail item as `evidence_ref`.
  - Indexed atomic/current-source descent revalidates request scope, evidence scope, canonical path, identity, physical containment, and current source version before returning canonical UTF-8 source content.
  - Changed sources return `status="stale"` with no content; deleted/unsafe sources return `status="unavailable"` with no guessed detail.
  - Cross-workspace evidence and tampered path pointers fail closed.
  - Large sources return deterministic query-centered exact windows under the same byte budget with explicit character/line coverage and truncation metadata.
  - Session digests remain navigation. Source depth validates the canonical digest, then returns `external_source_required` plus bounded Gateway source refs/coverage rather than upgrading the digest summary into transcript evidence.
  - Tests prove exact date/number/path/config/ID/quote/state recovery, atomic Memory source reads, stale and deleted sources, cross-workspace rejection, path tampering rejection, bounded large-source windows, digest external-source routing, and stale digest detection.

#### C3. OS host progressive-history bridge

- Status: COMPLETE
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
- Evidence:
  - Repository: `aiverse-filmmakers/AI-Verse-OS`.
  - Branch: `context-ladder/c3-progressive-history-bridge`.
  - PR #42, merged 2026-09-14.
  - Final PR head: `8d192bedfe311eb33720ffb33d95e9bb948e02e0`.
  - Merge/main SHA: `156f15f162c6d63159b54d3ad87e0342ec7cf9aa`.
  - Corrected-head PR workflows all succeeded: Direction Ownership `34885133569`, OS Write Command Boundary `34885133534`, OS Brain Permission Contract `34885133439`, Repository QC `34885133475`, Five-Component Public Beta `34885133545`, Four Repo Acceptance `34885133535`, Invisible Intelligence Automation Consent `34885133421`, Permanent Bot Consent `34885133419`, Temporary Worker `34885133428`.
  - Initial PR head `5c37094a0b3d4b514f9109e338f6484b1def876b` already passed all owner/composition/regression gates except Repository QC; that failure was only a new test-fixture parent-directory bug and commit `8d192bedfe311eb33720ffb33d95e9bb948e02e0` fixed the fixture without changing bridge semantics.
  - Post-merge OS main workflows all succeeded: Direction Ownership `34885346812`, OS Write Command Boundary `34885346721`, OS Brain Permission Contract `34885346714`, Repository QC `34885346682`, Five-Component Public Beta `34885346879`, Four Repo Acceptance `34885346749`.
  - Existing `retrieve_history(query, scope)` remains byte-for-byte behaviorally unchanged and still returns `[]` when Memory is absent.
  - New `retrieve_history_progressive` is advertised dynamically only when installed Memory actually exposes `memory.progressive-recall.v1`; absent/incompatible Memory is not falsely advertised.
  - OS validates scope, version, depth, query, item count, byte budget, and source `evidence_ref` scope before invoking Memory.
  - Workspace requests may use only their own workspace evidence plus operator evidence already visible under established Memory scope law; operator requests cannot descend into workspace evidence.
  - The bridge routes to Memory `progressive_recall` and validates returned version/depth/scope/budget without persisting or copying canonical Memory state into OS.
  - Four Repo Acceptance now composes the accepted C2 Memory SHA `2606bf6524fd67b4a3930fb7d98de54a3d483fb1` and proves real legacy recall plus catalog/summary/detail/source exact-evidence routing.

### Phase D: Derived Memory relationships

#### D1. Deterministic relationship projection

- Status: COMPLETE
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
- Evidence:
  - Memory PR #24 final head `ee5d73a328be0adc3dc994065ec22e79eb85eef0`.
  - PR Test run `34886444235`: 12/12 jobs green on the unchanged final head.
  - Merge/main SHA `11956647f0d7a8e79aacd052e101b31104152b7a`.
  - Post-merge Test run `34886772023`: 12/12 jobs green.
  - Projection is disposable/rebuildable, explicit-provenance-only, scope isolated, stale-edge removing, and adds no neighbor traversal.
  - D1 acceptance complete; ten of 25 slices are accepted.

#### D2. Bounded neighbor recall benchmark and ship/reject gate

- Status: COMPLETE
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
- Evidence:
  - Initial Memory PR #25 benchmark was later found invalid as a ship/reject gate because its expected answers were already direct-recall records, so it could not demonstrate positive neighbor value by construction.
  - Corrective benchmark PR #27 final head `f3dc19be30649ef0cec7368694f807e08c4ecfde`.
  - Corrective PR Test run `34890392950`: success, 12/12 jobs.
  - Corrected representative benchmark: direct-only recall recovered 1/4 scenarios; the one-hop candidate recovered 4/4.
  - Corrected apples-to-apples candidate added about 14.1% context, returned three relevant neighbors and zero irrelevant neighbors, with zero workspace leakage, zero stale neighbors, and zero canonical mutation.
  - Cross-platform latency remained bounded to explicit history/provenance requests: macOS about 15.1 -> 28.2 ms, Ubuntu about 15.8 -> 36.3 ms, Windows 3.9 about 47.8 -> 145.7 ms, Windows 3.12 about 24.2 -> 226.0 ms.
  - Corrective benchmark merged as Memory main `1be6a9715f574dc4dd5a4988592e49e8f7ef4c74`; post-merge Test run `34890743187`: success, 12/12 jobs.
  - Runtime ship PR #28 final head `55598172f11cec564dbdffc55db7643264e8fd76`.
  - PR #28 Test run `34891343587`: accepted 12/12 on unchanged rerun after one pre-existing Windows mutation-lock race; all D2 runtime tests passed.
  - Runtime merge/main SHA `620252ef361b32d60881d734c58035b155e18b38`.
  - Post-merge Test run `34891787879`: success, 12/12 on attempt 2 after one unrelated Windows public-beta concurrency timeout.
  - Ship/reject decision: REJECT generic/unbounded relationship traversal; SHIP only the benchmark-proven narrow path in detail-depth progressive recall: one hop, at most four neighbors, explicit historical/correction or provenance/evidence intent, established scope and byte/result budgets, no expansion for ordinary current-truth queries, and exact-source descent preserved.
  - D2 acceptance complete; eleven of 25 slices are accepted.

### Phase E: Gateway lossless fold tree

#### E1. Immutable fold-card and catalog storage foundation

- Status: COMPLETE
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
- Evidence:
  - Gateway Windows atomic-state prerequisite PR #17 head `30978c08b5ca014bdc27560bb61f4e0aa12b46ae`; CI run `34888813873` succeeded 6/6 on unchanged attempt 2, and Temporary Worker `34888813879`, Permanent Bot `34888813896`, and Automation Recommendation `34888814218` compositions all succeeded.
  - PR #17 merged as Gateway `0e2a99c6e1703dc5cb1141214ee17d0efa8feb2e`; post-merge CI `34900827729` succeeded 6/6.
  - E1 PR #18 final head `ef13f635ac8d4feb8655ba5cb598d871e1acfcf2`.
  - E1 PR CI `34901220511`: success, 6/6; composition runs `34901220414`, `34901220516`, and `34901220469`: all success.
  - E1 merged as Gateway main `463e455656b29d4f0d5aee251212a59b3a61fad8`.
  - Post-merge CI `34901336099`: success, 6/6.
  - E1 adds content-addressed immutable fold cards, exact ordered raw-message range fingerprints, immutable child-card fingerprints, scope-bound coverage, byte/token estimates, generator/validation metadata, a disposable rebuildable catalog, exact raw-source resolution, recursive descendant reachability, tamper detection, and restart-safe reads.
  - `run-engine.mjs` and prompt assembly were unchanged; Gateway-owned raw `run.messages` remain canonical and intact.
  - E1 acceptance complete; twelve of 25 slices are accepted.

#### E2. Fold creation and recursive roll-up

- Status: COMPLETE
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
- Evidence:
  - E2 PR #19 final head `4b7f0676349ef602a41172844782033923047895`.
  - PR CI `34901901782`: success, 6/6; composition runs `34901901774`, `34901901840`, and `34901901817`: all success.
  - E2 merged as Gateway main `c601d1dd0bcd3fcdeb1a8abf51dc433c2f400688`.
  - Post-merge CI `34902013764`: success, 6/6.
  - E2 performs no work below the explicit pressure threshold, selects oldest completed session history first, requires an injected summarizer, and rejects summaries that are not strictly smaller before any fold card is written.
  - Level-1 cards cover complete ordered run-message ranges. Adjacent unparented same-level cards recursively roll up with bounded fan-in; acceptance tests prove level-1 -> level-2 -> level-3 creation and exact recovery of all original descendant messages in order.
  - Failed summarization leaves raw history and existing fold state unchanged; Gateway-owned raw `run.messages` remain canonical.
  - E2 acceptance complete; thirteen of 25 slices are accepted.

#### E3. Lossless unfold and archive search

- Status: IN PROGRESS
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
- Next: YES
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

Current implementation slice: **E1. Immutable fold-card and catalog storage foundation**

Do not start E2 until:
- current Gateway raw session/run ownership is re-audited after Invisible Intelligence changes and no competing transcript owner is introduced;
- the pre-existing Gateway CI baseline is made deterministic without weakening production behavior or hiding a real product failure;
- fold cards are immutable derived artifacts over Gateway-owned raw run messages, with raw messages left intact and exactly retrievable;
- each card has deterministic immutable identity, level, scope/session binding, ordered source/child references, coverage, source fingerprint, byte/token estimates, summary, generator metadata, creation time, and explicit validation state;
- card writes are retry-safe and conflicting/tampered immutable artifacts fail closed;
- references to child cards are scope-safe and cannot silently mutate the referenced card;
- the fold catalog is disposable/rebuildable from immutable card files and restart-safe;
- E1 creates storage/validation only: no context-pressure folding, summary generation policy, recursive roll-up, or runtime prompt replacement is added before E2;
- identity, immutability, ordering, coverage, scope isolation, raw-source preservation, catalog rebuild, tamper detection, and restart tests pass;
- full Gateway CI is green;
- E1 exact PR/merge/run evidence is written here.


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


### Slice completion checkpoint: B1

Verified on 2026-09-14:

- AI-Verse-Memory core B1 PR #15 merged at `3fceb2a41eb33db5aef539cc668470e1d43d74be`; PR Test run `34857742063` succeeded 12/12.
- Post-merge contention exposed a real pre-existing canonical mutation lock weakness, so B1 acceptance remained open through follow-up PRs #16-#20.
- PR #19 removed full derived-index rebuilds from normal serialized mutation and retained lossless rebuild fallback.
- PR #20 finalized lock semantics with bounded live-owner lease, fast dead-owner recovery, holder-progress reset, and conservative ambiguous-lock staleness.
- Final accepted Memory main: `ced610cdacef0df50cc8ee16a4cf886240f257ce`.
- Final post-merge Test run `34869401845`: success, 12/12 jobs.
- B1 acceptance is complete. Five of 25 slices are accepted.

### Slice start checkpoint: B2

Verified before B2 implementation on 2026-09-14:

- AI-Verse-Memory main: `ced610cdacef0df50cc8ee16a4cf886240f257ce`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34869401845`: success, 12/12 jobs.
- B1 orientation projection and its concurrency hardening are present on current main.
- AI-Verse-System main: `ebe41f669ffdbabf13c44b1038e8bdf7f95ed0c4`; this plan refreshes onto that exact live state before B2 code changes.
- B2 is Memory-only and must extend the existing orientation projection rather than create another catalog/store.


### Slice completion checkpoint: B2

Verified on 2026-09-14:

- AI-Verse-Memory PR #21 merged.
- Final PR head: `fd51a7d6b39528de2ce60773a406544ffad79a42`.
- Memory main after merge: `15e81e3958b7f6b69fdf63021556706004bdb8a6`.
- PR Test run `34871933644`: final success on attempt 2; unchanged rerun job `104071952512` cleared the single transient Windows Python 3.12 full-suite stall from attempt 1.
- Post-merge main Test run `34872782122`: success, 12/12 jobs.
- B2 proved source-fingerprint drift across atomic/current-source/session-digest evidence, unrelated-workspace stability, stale derived-row replacement, deterministic hard byte caps, content-free diagnostics, deletion/rebuild equivalence, and B1 regression safety.
- B2 acceptance is complete. Six of 25 slices are accepted.

### Slice start checkpoint: C1

Verified before C1 implementation on 2026-09-14:

- AI-Verse-Memory main: `15e81e3958b7f6b69fdf63021556706004bdb8a6`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34872782122`: success, 12/12 jobs.
- B1-B2 orientation projection, fingerprint, budget, diagnostics, and concurrency hardening are present on current main.
- AI-Verse-System main: `28b15a4d61f752e5da62a885a9de8d0702cdc3f7`; this plan refreshes onto that exact live state before C1 code changes.
- C1 is Memory-only and must preserve legacy `recall()` while adding one bounded versioned progressive retrieval surface.


### Slice completion checkpoint: C1

Verified on 2026-09-14:

- AI-Verse-Memory PR #22 merged.
- Final PR head: `735b89c69e69f2bf0f7fdbac62308c17c0bffc54`.
- Memory main after merge: `25c7304aa9e288dc2f8b747e7b453b76cfd5c500`.
- PR Test run `34877283843`: success, 12/12 jobs.
- Post-merge main Test run `34877535172`: success, 12/12 jobs.
- C1 proved one owner-preserving progressive API over B2 orientation + existing digest/index recall, deterministic byte/item budgets, explicit evidence pointers, strict workspace isolation, and unchanged legacy `recall()`.
- Exact `source` depth intentionally remained unavailable until C2.
- C1 acceptance is complete. Seven of 25 slices are accepted.

### Slice start checkpoint: C2

Verified before C2 implementation on 2026-09-14:

- AI-Verse-Memory main: `25c7304aa9e288dc2f8b747e7b453b76cfd5c500`.
- Memory open PRs: none.
- Memory active workflow runs: none.
- Latest Memory main Test run `34877535172`: success, 12/12 jobs.
- C1 progressive recall v1 is present on current main and remains the only new progressive retrieval API.
- AI-Verse-System main: `0bc115ba3a81e5cfa85d33f02bf5891465fb610e`; this plan refreshes onto that exact live state before C2 code changes.
- C2 is Memory-only and must extend C1 `depth="source"` rather than create a second exact-source surface.


### Slice completion checkpoint: C2

Verified on 2026-09-14:

- AI-Verse-Memory PR #23 merged.
- Final PR head: `62444f253532255eaf5d3b8795fae802285d988c`.
- Memory main after merge: `2606bf6524fd67b4a3930fb7d98de54a3d483fb1`.
- PR Test run `34878580347`: final success on attempt 2; unchanged Windows Python 3.9 rerun job `104093425179` cleared the single synthetic mutation-lock queue interruption from attempt 1.
- Post-merge main Test run `34879367921`: final success on attempt 2, 12/12 jobs; unchanged Windows Python 3.12 rerun job `104109959305` cleared a four-minute external interruption in the pre-existing 8-writer concurrency test.
- C2 proved same-API source descent, exact canonical value recovery, source freshness/version checks, containment and scope revalidation, deleted-source uncertainty, cross-workspace/tampered-pointer rejection, bounded query-centered source windows, and correct Gateway pointer behavior for session digests.
- C2 acceptance is complete. Eight of 25 slices are accepted.

### Slice start checkpoint: C3

Verified before C3 implementation on 2026-09-14:

- AI-Verse-Memory main: `2606bf6524fd67b4a3930fb7d98de54a3d483fb1`; no open PRs or active workflows; final post-C2 main Test run `34879367921` succeeded 12/12.
- AI-Verse-OS main: `b08cc8c05c56fad7bc390f391292bdfbdd7d23e0`; no open PRs or active workflows.
- AI-Verse-System main: `03c5b71a4ed5bef6d5d1c030c60bb8c18bed7d5e`; this plan refreshes onto that exact live state before C3 code changes.
- C3 must extend the current OS host adapter and preserve existing Brain/Gateway `retrieve_history` callers rather than replace the host protocol.


### Slice completion checkpoint: C3

Verified on 2026-09-14:

- AI-Verse-OS PR #42 merged.
- Final PR head: `8d192bedfe311eb33720ffb33d95e9bb948e02e0`.
- OS main after merge: `156f15f162c6d63159b54d3ad87e0342ec7cf9aa`.
- Corrected-head PR gates all green: `34885133569`, `34885133534`, `34885133439`, `34885133475`, `34885133545`, `34885133535`, `34885133421`, `34885133419`, `34885133428`.
- Post-merge standard OS gates all green: `34885346812`, `34885346721`, `34885346714`, `34885346682`, `34885346879`, `34885346749`.
- C3 preserved legacy history retrieval, added dynamic versioned progressive Memory routing, proved missing/incompatible Memory truthfulness, bounded scope-safe source evidence handoff, and real C2 Memory exact-source composition without OS canonical state duplication.
- C3 acceptance is complete. Nine of 25 slices are accepted.

### Slice start checkpoint: D1

Verified before D1 implementation on 2026-09-14:

- AI-Verse-Memory main: `2606bf6524fd67b4a3930fb7d98de54a3d483fb1`; no open PRs or active workflows; latest accepted main Test run `34879367921` succeeded 12/12.
- AI-Verse-OS main: `156f15f162c6d63159b54d3ad87e0342ec7cf9aa`; C3 is merged and all standard post-merge OS gates are green.
- AI-Verse-System main: `272ee3fb968c33fe69dd1d7f8c786686d9cbc35a`; this plan refreshes onto that exact live state before D1 code changes.
- D1 is Memory-only. It may create only a disposable deterministic relationship projection; it must not change canonical Memory ownership or add traversal/neighbor recall.


### Slice completion checkpoint: D1

Verified on 2026-09-14:

- AI-Verse-Memory PR #24 merged from `context-ladder/d1-relationship-projection`.
- Final PR head: `ee5d73a328be0adc3dc994065ec22e79eb85eef0`.
- PR Test run `34886444235`: success, 12/12 jobs.
- Memory main after merge: `11956647f0d7a8e79aacd052e101b31104152b7a`.
- Post-merge main Test run `34886772023`: success, 12/12 jobs.
- D1 proved deterministic rebuilds, stale-edge removal, malformed/dangling reference rejection, workspace isolation, canonical-file non-mutation, supersession, digest/source provenance, and O(n) same-session projection.
- D1 introduced no semantic inference and no neighbor traversal.
- D1 acceptance is complete. Ten of 25 slices are accepted.

### Slice start checkpoint: D2

Verified before D2 implementation on 2026-09-14:

- AI-Verse-Memory main: `11956647f0d7a8e79aacd052e101b31104152b7a`; D1 is merged and post-merge Test run `34886772023` is 12/12 green.
- Existing runtime recall remains direct-only. D1 exposes deterministic relationship reads but does not expand recall through them.
- D2 is Memory-only and is a benchmarked ship/reject gate. It must not create a second canonical graph, relax scope, or alter exact-evidence authority.
- The candidate is limited to one hop with explicit hard bounds; runtime expansion may ship only if the benchmark proves material correctness value without unacceptable context/latency inflation.


### Slice completion checkpoint: D2

Verified on 2026-09-15:

- The original PR #25 benchmark conclusion was superseded after review found the control was not capable of proving positive recall value.
- Corrective benchmark PR #27 head `f3dc19be30649ef0cec7368694f807e08c4ecfde` passed Test run `34890392950` 12/12 and merged as `1be6a9715f574dc4dd5a4988592e49e8f7ef4c74`; post-merge Test run `34890743187` passed 12/12.
- Fair benchmark evidence improved representative correctness from 1/4 direct-only to 4/4 with three relevant neighbors, zero irrelevant neighbors, zero scope leakage, zero stale neighbors, zero canonical mutation, and about 14.1% apples-to-apples context inflation.
- The absolute latency cost was acceptable only for explicit history/provenance retrieval, not for ordinary recall, so D2 kept generic traversal rejected and shipped a much narrower runtime path.
- Runtime PR #28 head `55598172f11cec564dbdffc55db7643264e8fd76` adds detail-depth, one-hop, max-four-neighbor expansion only for explicit history/correction or provenance/evidence intent. Current-truth queries and other depths do not expand relationships.
- PR #28 Test run `34891343587` reached full acceptance after an unchanged rerun of the pre-existing Windows mutation-lock race; all new D2 runtime acceptance tests passed.
- Memory main after runtime merge: `620252ef361b32d60881d734c58035b155e18b38`.
- Post-merge main Test run `34891787879`: success, 12/12 on attempt 2 after an unrelated Windows public-beta concurrency timeout was rerun unchanged.
- D2 acceptance is complete. Eleven of 25 slices are accepted.

### Slice start checkpoint: E1

Verified before E1 implementation on 2026-09-14:

- AI-Verse-Gateway main: `7ed7974d865e6eae9f0a01056e0756b59f2b44e4`; no open PRs or active workflows at initial audit.
- Gateway owns durable sessions, runs, run checkpoints/events, and gateway audit receipts. Raw conversational history is currently preserved in Gateway run JSON `messages`; E1 must derive from it without rewriting or promoting it into another canonical store.
- Current Gateway `src/store.mjs` stores sessions/runs/events and has no fold-card or archive-card store yet.
- Current Gateway `src/run-engine.mjs` invokes runtimes from persisted `run.messages`, so E1 must not alter prompt assembly or folding policy.
- Latest inspected Gateway main CI `34886514508` had a pre-existing Windows Node 20-only failure. The first attempt failed the recurring-recommendation run while all other matrix lanes passed; an unchanged Windows Node 20 rerun failed a different clean-install run while the previously failing test passed. Earlier main evidence showed another different host-backed test failing only on Windows Node 20. This is being treated as a test-harness determinism prerequisite, not silently ignored.
- E1 storage design is additive: immutable derived cards plus a rebuildable catalog, with raw source bytes/messages preserved and exact source references retained.
- AI-Verse-System main at this checkpoint: `8e46c964e3b018440ecd78a1e66ba62ee3397cc1`; concurrent Invisible Intelligence work remains separate from this plan branch.


### Slice completion checkpoint: E1

Verified on 2026-09-15:

- Gateway storage-hardening prerequisite PR #17 merged as `0e2a99c6e1703dc5cb1141214ee17d0efa8feb2e` after exact-head CI reached 6/6 and all three Invisible Intelligence compositions remained green.
- Gateway post-prerequisite main CI `34900827729` passed 6/6.
- E1 PR #18 head `ef13f635ac8d4feb8655ba5cb598d871e1acfcf2` passed CI `34901220511` 6/6 plus all three composition gates.
- E1 merged as Gateway main `463e455656b29d4f0d5aee251212a59b3a61fad8`; post-merge CI `34901336099` passed 6/6.
- Fold cards are immutable/content-addressed and contain only compact summary plus references/metadata, not copied raw message history.
- Level-1 cards retain exact ordered source ranges and fingerprints; recursive cards retain exact ordered child IDs and fingerprints. Scope mismatches and in-flight sources fail closed.
- Raw Gateway run messages remain canonical and can be resolved exactly through card references after restart; child tampering is detected rather than silently rewriting ancestry.
- The catalog is disposable/rebuildable derived state with a deterministic fingerprint over catalog entries.
- E1 acceptance is complete. Twelve of 25 slices are accepted.

### Slice start checkpoint: E2

Verified before E2 implementation on 2026-09-15:

- AI-Verse-Gateway main: `463e455656b29d4f0d5aee251212a59b3a61fad8`; E1 post-merge CI `34901336099` is 6/6 green.
- E2 may create cards only through the accepted immutable E1 store. It must not delete or rewrite raw `run.messages`, mutate referenced cards, or change canonical Gateway session/run ownership.
- E2 owns fold creation policy and recursive same-level roll-up only. Archive search/unfold policy remains E3; context-pressure policy remains E4.
- No fold should occur below the configured pressure threshold. Every accepted fold must be strictly smaller than its covered input, preserve ordered complete coverage, and keep exact descendant reachability.
- Failed or oversized summarization must leave raw history and existing cards untouched.


### Slice completion checkpoint: E2

Verified on 2026-09-15:

- E2 PR #19 head `4b7f0676349ef602a41172844782033923047895` passed CI `34901901782` 6/6 and all three existing composition workflows.
- E2 merged as Gateway main `c601d1dd0bcd3fcdeb1a8abf51dc433c2f400688`; post-merge CI `34902013764` passed 6/6.
- The accepted engine performs no fold below the explicit pressure threshold and chooses oldest completed session history first.
- Gateway does not select or invent a summarization provider in E2; folding requires an injected summarizer and rejects empty/failed output.
- Every candidate summary must be strictly smaller than the covered input before E1 immutable storage is invoked.
- Recursive roll-up uses only adjacent unparented same-level cards and preserves exact descendant source reachability; tests reach level 3 over eight completed runs and recover all original messages in canonical order.
- Failed or oversized summarization leaves raw history and existing cards untouched.
- E2 acceptance is complete. Thirteen of 25 slices are accepted.

### Slice start checkpoint: E3

Verified before E3 implementation on 2026-09-15:

- AI-Verse-Gateway main: `c601d1dd0bcd3fcdeb1a8abf51dc433c2f400688`; E2 post-merge CI `34902013764` is 6/6 green.
- E3 must reuse E1 exact recursive source resolution and E2 cards. It must not create a second archive, copy raw transcripts, or weaken source fingerprints.
- Archive search must be bounded and scope-safe. Precision retrieval may force exact unfold, but ordinary search should return compact card evidence first.
- Stale source or child fingerprint evidence must fail closed and be surfaced as stale derived state rather than returning unverified original content.
- E4 remains the owner of live context-pressure integration and recent-raw-tail policy; E3 does not modify runtime prompt assembly.
