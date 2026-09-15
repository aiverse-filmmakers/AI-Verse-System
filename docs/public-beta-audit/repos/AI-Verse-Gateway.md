# A1.2 — Independent Repository Audit: AI-Verse-Gateway

**Audit program:** Independent Whole-System Public-Beta Audit  
**Phase:** A1 Independent repository audits  
**Task:** A1.2 AI-Verse-Gateway  
**Audit date:** 2026-09-15  
**Frozen repository ref:** `46c15ee58b028dd7fb8b310327ea705ef618805e`  
**System control baseline:** `550c85c9b04a81c9add0c2474940fd84420e11a4`  
**Repository role reconstructed from itself:** canonical authenticated client/runtime edge and bounded run-loop owner  
**Audit status:** **COMPLETE**  
**Standalone product verdict:** **DOGFOOD BLOCKED**  
**R-a Reconstruction:** COMPLETE / PASS  
**R-b Enforcement:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c Verdict:** COMPLETE / BLOCKED  
**Findings opened:** `WSA-2026-006`, `WSA-2026-007`, `WSA-2026-008`  
**Next task:** A1.3 AI-Verse-Brain

> Audit-completion points measure completed forensic work, not product acceptance. Gateway remains blocked by the finding gate even after A1.2 itself is complete.

## 1. Independence statement

This packet reconstructs AI-Verse-Gateway from the frozen Gateway repository itself.

Substantive evidence came only from:

- files tracked in `aiverse-filmmakers/AI-Verse-Gateway` at the frozen SHA;
- Gateway-owned GitHub repository metadata, commit/PR history and Actions;
- tests, fixtures, benchmarks and cross-owner workflows defined by Gateway.

No sibling repository source was opened to fill a standalone Gateway gap.

Gateway-owned workflows that clone immutable sibling revisions are evidence of what **Gateway tests against those revisions**. They do not independently prove the sibling implementation. All such external claims remain CLAIM-OUTBOUND until A2.

No AI-Verse-System component specification was used as substantive Gateway evidence.

## 2. Pre-task and pre-write drift control

At A1.2 start and immediately before writing this packet:

- Gateway `main` = `46c15ee58b028dd7fb8b310327ea705ef618805e`;
- this exactly matches the A0.2/A0.5 frozen Gateway ref;
- System `main` remained `550c85c9b04a81c9add0c2474940fd84420e11a4` before this audit branch was created;
- open PRs in Gateway and System: **0**;
- no Gateway product file was modified;
- Dashboard MC1.4 remains paused.

No drift invalidated the standalone target.

---

# R-a — Reconstruction

## 3. Repository inventory and canonical roots

The recursive frozen tree is complete and not truncated:

- tracked entries: **87**
- tracked files/blobs: **78**
- tracked directories/trees: **9**

Primary regions:

| Region | Files | Role |
|---|---:|---|
| `src/` | 22 | canonical Gateway runtime/lifecycle/server/store/context implementation |
| `test/` | 13 | canonical behavioral and security tests |
| `fixtures/` | 21 | deterministic runtime/host/owner test doubles |
| `.github/workflows/` | 5 | cross-platform CI and cross-owner acceptance |
| `docs/` | 5 | architecture, protocol, research, rejected evaluations |
| `scripts/` | 3 | integrated acceptance helpers |
| `benchmarks/` | 1 | Context Ladder benchmark |
| root package/security/component files | bounded | product identity, packaging, security, lifecycle descriptor |

There is no tracked build output, vendored dependency tree or generated duplicate runtime implementation inflating the code surface.

The package has no runtime npm dependency set beyond Node built-ins in the audited package lock.

## 4. Product identity, build and license

`package.json`:

- package: `@aiverse/gateway`
- version: `0.1.0-beta.1`
- Node: `>=20`
- ESM
- CLI: `aiverse-gateway -> bin/aiverse-gateway.mjs`
- license: MIT

Top-level `LICENSE` is MIT and GitHub detects MIT.

The repository describes Gateway as the canonical AI-Verse client/runtime edge.

Its user-facing responsibilities are:

- authenticated client ingress;
- system/workspace/session binding;
- run creation and control;
- runtime selection/invocation;
- streaming events;
- bounded context assembly;
- OS-host action routing;
- run checkpoints/recovery;
- Gateway audit receipts.

It is **not** a second Brain, Memory, Data, Skills, Multiple Bots, Connections, Token, Automations or Dashboard owner.

## 5. Canonical ownership and local state

Machine-readable `component.json` says Gateway owns:

- sessions;
- runs;
- run checkpoints;
- Gateway audit receipts.

Executable implementation additionally persists Gateway-owned/derived edge state under the Gateway home:

- session files;
- run files;
- event streams;
- idempotency/control records;
- audit NDJSON;
- Context Ladder fold cards/catalog.

The audit classifies:

### Canonical Gateway edge state

- authenticated session binding;
- run/transcript state required for continuation;
- run checkpoints/status;
- run events/control receipts;
- Gateway audit receipts;
- durable retry/idempotency metadata.

### Derived/rebuildable Gateway context state

- immutable content-addressed fold cards;
- fold catalog;
- archive diagnostics/projections.

Raw Gateway run messages remain canonical source evidence for Gateway-owned conversation/run history. Fold summaries never replace those bytes as canonical truth.

### Explicit non-owners

Gateway docs/component descriptor consistently exclude:

- Brain Goals/strategic truth;
- Memory canonical history;
- Data structured truth;
- reusable Skills;
- Multiple Bots coordination truth;
- Connections credentials;
- Token normalized usage/cost truth;
- Automation schedules;
- Dashboard presentation truth.

## 6. Adapter and integration architecture

### OS host adapter

Gateway uses a versioned JSON-subprocess host contract:

`ai-verse-brain-bridge/1.0`

`HostClient` exposes:

- describe;
- current-context read;
- legacy/progressive Memory retrieval;
- capability listing;
- connection metadata listing;
- action authorization;
- action execution.

Protocol and request-ID mismatch fail closed.

### Brain Goal adapter

Gateway defines a separate:

`ai-verse-goal-owner/1.0`

with:

- `goal.get`
- `goal.evaluate`

No fallback Goal database exists. Missing Goal-owner configuration fails closed.

### Runtime adapters

Implemented runtime choices:

- deterministic, test-only;
- OpenAI-compatible HTTP;
- generic JSON subprocess.

Runtime selection does not transfer domain ownership.

### Subprocess boundary

The generic subprocess runner:

- uses `shell:false`;
- bounds stdin/stdout/stderr;
- has a timeout;
- passes a filtered environment plus explicitly named variables;
- supports AbortSignal;
- rejects invalid JSON/protocol envelopes in higher adapters.

## 7. Server/API surface

Gateway exposes:

- unauthenticated minimal `GET /health`;
- authenticated `GET /status`;
- authenticated `GET /v1/models`;
- `POST /v1/chat/completions`;
- `POST /v1/runs`;
- `GET /v1/runs/:id`;
- event SSE;
- diagnostics;
- pause/resume/cancel/approval controls;
- bounded Automation wake ingress.

The effective principal comes from the verified bearer credential, not caller-supplied actor/user headers.

Browser origins must be explicitly allowed when an Origin header is present.

Request bodies and configured run budgets are bounded.

## 8. Lifecycle reconstruction

Advertised CLI lifecycle:

- install;
- setup;
- status;
- doctor;
- serve;
- enable;
- disable;
- update;
- uninstall;
- explicit destructive `uninstall --purge`.

Intended semantics:

- install creates Gateway's local lifecycle root only;
- setup binds one OS root/runtime and creates one bearer identity;
- API token plaintext is shown once;
- provider secret **values** are not stored in Gateway config, only environment-variable names;
- normal uninstall preserves Gateway state;
- purge is the explicit destructive state-removal path.

Lifecycle enforcement has material defects recorded later in `WSA-2026-006` and `WSA-2026-007`.

## 9. Run state machine and Goal continuation

Core run states include:

- queued;
- running;
- awaiting_approval;
- resuming;
- paused;
- parked;
- paused_no_progress;
- paused_recovery_required;
- blocked;
- budget_limited;
- failed;
- canceled;
- completed.

Goal-bound continuation:

1. reads owner Goal;
2. binds goal ID/version/activation epoch;
3. executes a bounded turn;
4. collects evidence;
5. asks the Goal owner for verdict;
6. before another autonomous turn, re-reads exact Goal binding;
7. changed binding revokes the continuation lease.

Configured/requested budgets are intersected so requests can narrow but not widen outer limits.

## 10. Runtime action admission and ownership

The runtime receives only two tool classes:

- `aiverse_action`;
- bounded `aiverse_context`.

For side effects, Gateway:

1. validates tool shape;
2. strips/rejects runtime attempts to inject trusted authority/provenance fields;
3. derives trusted run/session/scope/evidence/runtime/budget fields;
4. calls OS `authorize_action`;
5. pauses for approval when required;
6. reauthorizes immediately before an approved effect;
7. calls OS `request_action`;
8. records tool outcome in Gateway run state.

Current bounded routes include:

- migration import/pending clarification;
- workspace organization;
- Memory capture/session digest;
- Skills learning candidates;
- structured Data organization/read;
- temporary Workers;
- explicit-consent permanent Bots;
- explicit-consent Automations.

Gateway does not directly open sibling canonical stores in the reviewed `src/` implementation.

## 11. Context Ladder / context pressure architecture

Current Gateway includes substantial context-management behavior beyond the original edge loop.

### Context governor

- no compaction when pressure is low;
- soft pressure schedules fold work while preserving the current invocation;
- cache-sensitive soft context can remain untouched;
- hard pressure compacts only the older prefix;
- configured recent raw tail remains verbatim unless an emergency bounded shrink is required;
- compaction must be strictly smaller than source prefix;
- unresolved pressure fails closed before runtime invocation;
- persisted `run.messages` remain canonical.

### Fold store

Fold cards are:

- immutable;
- content addressed;
- scope-bound to system/workspace/principal;
- ordered;
- source-fingerprinted;
- recursively validated;
- limited to completed canonical runs;
- rebuilt into a derived catalog.

Tampering, source drift, child drift, cross-workspace composition and invalid order fail closed.

### Archive retrieval

- compact searches return summary/card evidence without unfolding raw messages;
- exact-sensitive queries can boundedly unfold canonical raw source;
- stale source fingerprints fail closed;
- cross-workspace reads fail closed;
- message/byte bounds apply;
- safe diagnostics expose IDs/refs/depth, not raw prompt bodies or chain-of-thought.

### Progressive owner context

Normal turns use bounded current owner views and shallow historical orientation. Deeper summary/detail/source reads are intent-driven and bounded. Exact Gateway source fallback revalidates principal/system/workspace visibility and source fingerprint.

## 12. Deliberately rejected architecture

Two current Gateway evaluations explicitly reject bloat:

### F1 copy-on-write branch catalog

Rejected because current AI-Verse has no canonical branch/fork identity and immutable fold cards already physically share pre-divergence history.

### I1 cross-owner orientation map

Rejected because existing owner projections already supply six of seven proposed orientation domains and the missing Bot domain has no supported read-only owner boundary. Gateway refuses to invent a second cross-owner graph.

These are CURRENT architecture decisions, not missing implementations.

---

# R-b — Enforcement

## 13. Authentication and remote exposure

Verified current protections:

- loopback bind by default;
- non-loopback serving requires configured `allow_remote` plus `behind_tls_proxy`;
- Gateway itself does not claim public TLS termination;
- all application routes except minimal health require bearer auth;
- bearer verifier uses salted scrypt and timing-safe comparison;
- caller `x-actor-id` is not authentication;
- origin allowlist applies to browser-origin requests;
- body size limits apply;
- authenticated per-principal rate limiting exists.

A4 should specifically adversarially test unauthenticated invalid-bearer load because scrypt verification is synchronous and occurs before the authenticated principal rate limiter. A1.2 records this as an adversarial target, not a separate finding yet.

## 14. Scope, isolation and secret handling

Current enforcement/tests verify:

- caller-controlled storage IDs reject traversal/path forms;
- sessions bind system/workspace/principal;
- an existing session cannot be silently rebound by an explicit conflicting workspace request;
- progressive/fold evidence is scoped by system/workspace/principal;
- operator retrieval cannot descend into workspace-only history;
- cross-workspace fold/archive access fails closed;
- provider credentials are referenced by environment-variable name;
- runtime attempts to forge owner scope, provenance, consent, budgets, permissions, Connections or durable IDs are rejected;
- secret-bearing automatic historical/organization paths are suppressed.

Concurrent first-binding enforcement has a race recorded in `WSA-2026-008`.

## 15. Permission, approval and consent enforcement

The reviewed runtime path enforces:

- discovery/context is not permission;
- OS authorization occurs before action execution;
- OS denial blocks;
- OS approval requirement pauses the run;
- an explicit approval causes a second OS authorization check immediately before effect;
- owner still requiring approval after that check blocks execution;
- model output cannot manufacture approval/consent.

Current tests cover:

- direct durable-Bot consent;
- affirmative consent after a clear recommendation;
- repeated need without consent does not create a Bot;
- temporary-only requests do not count as durable consent;
- advice questions do not count as durable consent;
- direct recurring Automation instruction;
- affirmative recurring consent;
- cadence mismatch rejection;
- missing timezone rejection;
- recursive Automation creation suppression;
- automatic organization skips owner actions that require approval.

## 16. Durability, recovery and replay

Verified:

- run/session/event state is persisted under Gateway home;
- interrupted running/resuming/waiting-tool work becomes `paused_recovery_required`;
- Gateway does not pretend arbitrary provider process execution resumes transparently;
- completed-session Memory digest handoff can fail/retry without reopening canonical completed run;
- organization review proposal/result state survives restart;
- fold work is durable and rebuilt/validated;
- sequential idempotency conflict is tested;
- operation IDs with changed sequential payload are rejected.

However, current concurrency semantics are not linearizable; see `WSA-2026-008`.

## 17. Test suite and exact-head CI

`npm run check` performs syntax checks of core runtime files and executes 13 test files spanning:

- clean install/lifecycle;
- core loop contracts;
- security/recovery;
- fold storage/engine/archive/guards;
- context governor;
- progressive context;
- deep context tool;
- rejected branch/orientation evaluations;
- Context Ladder benchmark.

Frozen merge head:

`46c15ee58b028dd7fb8b310327ea705ef618805e`

Exact-head push CI:

- run `34992616000`;
- Linux Node 20: SUCCESS;
- Linux Node 22: SUCCESS;
- macOS Node 20: SUCCESS;
- macOS Node 22: SUCCESS;
- Windows Node 20: SUCCESS;
- Windows Node 22: SUCCESS.

All six jobs actually executed:

- checkout;
- Node setup;
- `npm install --ignore-scripts`;
- `npm run check`.

This is real executable evidence, not an empty runner record.

## 18. Exact merged PR-head integration evidence

Current merge commit is Gateway PR #31:

- PR head: `a08056e3809b17198082523365902273a525f656`;
- merge commit: frozen `46c15ee58b028dd7fb8b310327ea705ef618805e`.

The source tree merged into the frozen head passed:

| Workflow | Run | Result |
|---|---:|---|
| CI | `34990219447` | SUCCESS |
| Context Ladder Integrated Acceptance | `34990219367` | SUCCESS |
| Invisible Intelligence Automation Recommendation Boundary | `34990219479` | SUCCESS |
| Invisible Intelligence Permanent Bot Composition | `34990219501` | SUCCESS |
| Invisible Intelligence Temporary Worker Composition | `34990219558` | SUCCESS |

Job-level inspection confirms the PR-only gates actually executed:

- real Gateway -> OS -> Memory Context Ladder composition;
- recurring recommendation without schedule creation;
- full recurring-consent composition;
- explicit-consent durable Bot composition;
- bounded temporary Worker composition and non-durable cleanup.

These remain Gateway-owned integration claims. A2 validates the other side independently.

## 19. Historical evolution and research provenance

Recent Gateway history shows incremental repair/evolution rather than one monolithic rewrite:

- question-minimization runtime policy;
- owner-confirmed workspace routing;
- safe Memory routing;
- Skills learning candidate routing;
- restart-safe session digest;
- automatic structured Data routing;
- temporary Worker route;
- explicit durable Bot consent;
- recurring Automation recommendation/consent;
- Context Ladder context pressure/folding/progressive retrieval;
- cross-owner J2 acceptance and exact-source fallback repairs.

`docs/RESEARCH.md` records benchmark inputs from OpenClaw, Open WebUI, Hermes API server and OpenAI Agents SDK.

Those references are inspiration/benchmark evidence only. No external system is treated as AI-Verse authority.

No GitHub Release objects are published for Gateway at the frozen point. Formal release-set acceptance remains an A5 concern.

---

# R-c — Contradictions and findings

## 20. Contradiction register

### C-A1.2-001 — lifecycle commands/status disagree with live operational state

**Source A:** README/lifecycle CLI presents `setup -> ready`, `disable -> disabled`, normal uninstall -> absent/preserved-state lifecycle.

**Source B:** current implementation:

- `setupComponent` writes config before validating it and before host verification finishes;
- `setEnabled(false)` only edits the config file;
- a running server keeps the already-loaded config and checks `enabled` only once at startup;
- live `/status` reads the in-memory config;
- `doctorComponent` does not include `config.enabled` in its verdict;
- normal uninstall removes on-disk integration/config files but does not stop an already-running server.

**Higher-authority source:** executable lifecycle/server implementation.

**Classification:** implementation defect / lifecycle truth split.

**Finding:** `WSA-2026-007`.

### C-A1.2-002 — durable retry-binding claim is stronger than concurrency enforcement

**Source A:** README states an `Idempotency-Key` “durably binds retries to the original payload” and reuse with another payload is rejected.

**Source B:** `claimIdempotency` performs `readJson -> check -> atomicJson`. The semantic check is outside the serialized file-write critical section. Two concurrent first claims can both observe no prior record and both return `state: new`.

**Higher-authority source:** executable store implementation.

**Classification:** implementation defect / concurrency gap.

**Finding:** `WSA-2026-008`.

### C-A1.2-003 — privileged pause/cancel semantics are not protected from stale run writers

**Source A:** security/README present pause/cancel as authenticated privileged controls.

**Source B:** `saveRun` serializes the file write but replaces current run state with a previously captured candidate, preserving only newer archive diagnostics. Execution has asynchronous event/write boundaries after runtime output. A concurrent pause/cancel can persist terminal/control state and abort the controller, then an already-held stale `run` object can later overwrite that state before the next abort/status check.

**Higher-authority source:** executable run/store implementation.

**Classification:** implementation defect / control-state race.

**Finding:** `WSA-2026-008`.

## 21. WSA-2026-006 — destructive purge is not confined to a validated Gateway-owned root

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** destructive lifecycle / filesystem safety  
**Affected repo:** `AI-Verse-Gateway`  
**Affected journeys:** install/uninstall/reinstall, operator recovery, dogfood safety

### Summary

The supported CLI accepts arbitrary `--home PATH`. `gatewayHome()` resolves that path, and `uninstallComponent({ purge:true })` performs recursive forced removal of the entire resolved path without first proving that the target is a Gateway-owned installation root.

### Expected law

A destructive component purge must be confined to a verified component-owned root and must refuse filesystem roots, user/system roots, unrelated directories, symlink/realpath escapes and missing/wrong ownership markers.

### Observed behavior

Current path:

`CLI --home -> path.resolve(home) -> rm(home, { recursive:true, force:true })`

There is:

- no requirement that `install.json` exists;
- no check that its `component_id` is `ai-verse-gateway`;
- no realpath ownership boundary check;
- no refusal of `/`, a user home, repository root or arbitrary writable directory;
- no bounded list of Gateway-owned children for purge.

The audit did **not** execute a destructive reproduction against real data. The code path is unambiguous.

### Impact

A typo, bad automation argument or unsafe custom Gateway home can recursively delete unrelated user/system data.

Per the audit protocol, proven data-loss risk is BLOCKER severity.

### Required closure evidence

After A6 authorizes repair:

1. destructive purge must require a valid Gateway ownership marker at the exact realpath target;
2. refuse filesystem roots, broad user/system roots and unsafe/symlink targets;
3. prefer deleting known Gateway-owned children rather than arbitrary recursive target deletion;
4. add cross-platform negative tests for unrelated directory, missing marker, wrong marker, root-like targets and safe custom home;
5. re-audit uninstall/reinstall lifecycle on the repaired exact ref.

## 22. WSA-2026-007 — lifecycle state is not operationally authoritative

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** setup/disable/uninstall/status lifecycle truth  
**Affected repo:** `AI-Verse-Gateway`  
**Affected journeys:** setup, status/doctor, serve, disable/enable, uninstall, remote exposure

### Summary

Gateway lifecycle state is primarily file-backed but not coordinated with the live server process, and setup commits state before its own readiness verification is safely complete.

### Observed behavior

#### Setup can report or leave contradictory readiness

`setupComponent`:

1. builds config;
2. writes config;
3. then calls host `describe`;
4. returns `state: ready`.

It does not call `validateConfig(config)` before commit.

Therefore:

- an unsafe/invalid configuration can be persisted before later `loadConfig` rejects it;
- a host verification failure can leave a structurally valid config behind even though setup failed;
- a later fast `status` can report `ready` based on config shape even though the setup call failed operationally.

#### Disable does not disable a live server

`setEnabled(false)` only rewrites `config.json`.

`startServer` checks `config.enabled` only at process startup and then retains the in-memory object.

A server already running before the CLI disable:

- continues listening;
- continues authenticating/serving requests;
- exposes live `/status` from stale in-memory config.

Meanwhile a separate CLI `status` reads disk and reports `disabled`.

#### Doctor disagrees with disabled state

`doctorComponent` validates structure/dependencies/host/runtime/security but never makes `config.enabled === false` produce a disabled verdict. A disabled on-disk component can still return doctor `state: ready`.

#### Uninstall does not stop a live server

Normal uninstall removes install/config/adapter files, but no running-process control exists. The existing process retains loaded config, store and auth verifier and can remain live until independently stopped.

The clean-install acceptance test closes the live server **before** disable/uninstall, so it does not cover this lifecycle gap.

### Impact

An operator can believe Gateway is disabled or absent while a previously started network listener remains active. Status/doctor/setup can expose mutually inconsistent readiness truth.

This is a major lifecycle/security reliability failure with realistic impact.

### Required closure evidence

After A6 repair authorization:

- setup must validate configuration and host compatibility before publishing a ready configuration, or commit transactionally with rollback;
- live service state must have one authoritative control mechanism;
- disable/uninstall must stop or make an existing process refuse further requests, or the CLI must explicitly implement service-process coordination;
- `status`, `doctor` and live `/status` must agree on disabled/absent/ready semantics;
- tests must exercise disable/uninstall **while the server is live**, failed setup rollback, invalid remote setup and restart behavior.

## 23. WSA-2026-008 — durable state transitions are not linearizable under concurrency

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** concurrency / idempotency / session binding / run control  
**Affected repo:** `AI-Verse-Gateway`  
**Affected journeys:** run creation/retry, Automation wake replay, session isolation, pause/cancel, approval/control

### Summary

Atomic file replacement prevents malformed JSON, but several semantic read-check-write operations occur outside one serialized mutation/transition. Concurrent requests can therefore violate the higher-level idempotency, binding and privileged-control contracts.

### 23.1 Idempotency reservation race

`claimIdempotency`:

1. reads the idempotency DB;
2. checks prior record;
3. modifies that in-memory copy;
4. calls serialized `atomicJson`.

Two concurrent first claims for the same namespace/key can both complete steps 1-2 before either write and both return `state: new`.

Consequences include:

- two runs for one client idempotency key;
- two Automation wake runs for one invocation ID;
- two control operations passing first-admission;
- conflicting payload claims not being reliably rejected under concurrent first use.

The current test verifies only sequential changed-payload rejection.

The separate atomic-JSON stress test proves files remain valid, not semantic compare-and-reserve atomicity.

### 23.2 First session binding race

`createSession` similarly does:

`read existing -> validate binding -> atomic write new session`.

Two concurrent first requests with the same caller-supplied session ID but different workspace bindings can both see no existing session and both pass initial validation before last-writer-wins persistence.

That weakens the stated invariant that a session is durably bound to one system/workspace/principal.

### 23.3 Pause/cancel can be overwritten by stale execution state

`saveRun(run)` uses a serialized file mutation but replaces current state with the caller's previously captured candidate; it only preserves a newer `archive_diagnostics` extension.

The execution loop holds mutable run objects across asynchronous boundaries. One concrete interleaving is:

1. runtime result is already in the execution loop's local `run`;
2. execution awaits assistant event streaming;
3. an authenticated cancel/pause request loads current run, persists `canceled`/`paused`, emits control event and aborts the controller;
4. execution resumes after the event await and calls `saveRun(run)` with its stale `running` candidate;
5. that save can overwrite the just-persisted control state;
6. for a non-tool single-turn run, execution can then call `complete()` before another signal/status guard.

`complete()` can schedule post-completion Memory digest and organization review, so the inconsistency is not limited to a cosmetic status field.

### Impact

Possible effects include:

- duplicate run/provider cost;
- duplicate owner actions because separate duplicate runs receive separate run-bound idempotency identities;
- conflicting first session bindings;
- pause/cancel requests that do not remain authoritative;
- post-completion owner routing after an operator believed a run was canceled.

### Required closure evidence

After A6 repair authorization:

1. make idempotency claim+compare+reservation one atomic mutation;
2. make first session binding an atomic create-or-validate operation;
3. add run revision/CAS or a transition function that rejects stale writers and preserves terminal/control states;
4. check cancellation/control state again immediately before every durable transition/effect boundary;
5. add deterministic concurrent tests for:
   - identical first idempotency claims;
   - conflicting same-key first claims;
   - same new session ID with conflicting workspaces;
   - pause during result streaming;
   - cancel during result streaming;
   - cancel between authorization and owner result handling;
   - no background digest/organization effect after a successfully persisted cancel.

---

# R-c — Completeness and verdict

## 24. Lifecycle matrix

| Lifecycle area | Standalone state | Evidence conclusion |
|---|---|---|
| install | VERIFIED | local marker/state root only |
| setup | CONTRADICTED | non-transactional readiness, WSA-007 |
| status | PARTIAL | fast disk state, can disagree with live server |
| doctor | PARTIAL | deep checks, but disabled config can still report ready |
| serve | VERIFIED/PARTIAL | loopback/remote startup guard works; live lifecycle not coordinated |
| enable | PARTIAL | disk config only; running process semantics not authoritative |
| disable | FAILED | live process can continue serving, WSA-007 |
| update | PARTIAL | explicit npm/git source update; no rollback proof in Gateway |
| normal uninstall | PARTIAL/FAILED LIVE | state preserved, but live service is not stopped |
| purge | FAILED / BLOCKER | arbitrary resolved home can be recursively removed, WSA-006 |
| run create/retry | CONTRADICTED UNDER CONCURRENCY | WSA-008 |
| session binding | CONTRADICTED UNDER CONCURRENCY | WSA-008 |
| approval | VERIFIED | explicit grant + late OS reauthorization |
| pause/cancel | CONTRADICTED UNDER CONCURRENCY | stale writer can overwrite control state |
| restart recovery | VERIFIED | in-flight work becomes recovery-required; no fake provider resume |
| Goal continuation | VERIFIED AS GATEWAY CONTRACT | exact lease revalidation; external owner deferred A2 |
| migration routing | VERIFIED AS GATEWAY CONTRACT | exact source binding/clarification path |
| Context Ladder | VERIFIED | bounded, scoped, fingerprinted, raw source preserved |
| cross-platform | VERIFIED | Node 20/22 x Linux/macOS/Windows exact-head CI |

## 25. 46-lens completeness matrix

| # | Lens | A1.2 state | Standalone conclusion |
|---:|---|---|---|
| 1 | Product identity | VERIFIED | canonical authenticated client/runtime edge |
| 2 | Architecture | VERIFIED | edge/run/store/context layers are coherent |
| 3 | Ownership | VERIFIED | domain truth remains external |
| 4 | Source of truth | VERIFIED/PARTIAL | clear owners; live lifecycle truth splits under WSA-007 |
| 5 | Provenance | VERIFIED | run/tool/source fingerprints and receipts preserved |
| 6 | Scope | VERIFIED/PARTIAL | deterministic scope checks; concurrent first-bind race WSA-008 |
| 7 | Isolation | VERIFIED/PARTIAL | cross-workspace reads fail closed; session race remains |
| 8 | Privacy/local-first | VERIFIED | local state, env-name credentials, bounded diagnostics |
| 9 | Installation | VERIFIED | independent Gateway install marker/root |
| 10 | Attachment/registration | VERIFIED | OS/Goal adapters explicit |
| 11 | Activation/adoption | VERIFIED/PARTIAL | server/runtime adoption exists; live lifecycle issue |
| 12 | Initialization | CONTRADICTED | setup transaction/readiness WSA-007 |
| 13 | Migration/legacy integration | VERIFIED AS ROUTER | migration is owner-routed, not a second store |
| 14 | Update/upgrade | PARTIAL | explicit update exists; rollback not proven |
| 15 | Disable/detach | CONTRADICTED | live disable not authoritative |
| 16 | Uninstall/reinstall | CONTRADICTED | live uninstall + unsafe purge |
| 17 | Install-order independence | PARTIAL | Gateway composes via adapters; full graph deferred A2/A3 |
| 18 | Discovery | VERIFIED | configured host plus owner-projected capabilities/context |
| 19 | Readiness | CONTRADICTED | setup/status/doctor/live state can disagree |
| 20 | Health/doctor | PARTIAL | deep checks real; disabled semantics wrong |
| 21 | Permissions/approvals | VERIFIED | OS floor + late approval recheck |
| 22 | Security/path safety | CONTRADICTED | WSA-006 destructive path |
| 23 | Idempotency/replay | CONTRADICTED | sequential good, concurrent reservation race |
| 24 | Concurrency/locking | CONTRADICTED | WSA-008 |
| 25 | Failure/recovery | VERIFIED/PARTIAL | restart/digest/fold recovery good; control race remains |
| 26 | Capability taxonomy | VERIFIED | actions/context/runtime adapters stay distinct |
| 27 | Runtime/agent portability | VERIFIED | deterministic, OpenAI-compatible, JSON-subprocess |
| 28 | Integration boundaries | VERIFIED AS GATEWAY CLAIMS | sibling side deferred A2 |
| 29 | Cross-component writes | VERIFIED AS ROUTER CLAIM | final write delegated through OS/owner |
| 30 | Read path/retrieval | VERIFIED | progressive/context/fold reads are bounded/scoped |
| 31 | Data/schema evolution | EXTERNAL / ROUTED | Gateway does not own Data schema |
| 32 | Performance/bounds | VERIFIED/PARTIAL | context/body/action budgets + J1 benchmark; no production SLO |
| 33 | Product/UX | VERIFIED/PARTIAL | OpenAI-compatible UX strong; lifecycle truth defect material |
| 34 | Automation/cadence | VERIFIED AS GATEWAY BOUNDARY | consent/wake behavior tested |
| 35 | Agent behavior | VERIFIED AS GATEWAY BOUNDARY | temporary/durable specialist gates tested |
| 36 | Apps/UI projections | VERIFIED | OpenAI-compatible edge; Dashboard presentation not owned |
| 37 | Release/distribution | PARTIAL | beta package/component descriptor; no GitHub release object |
| 38 | Cross-platform | VERIFIED | six exact-head CI jobs |
| 39 | Documentation consistency | CONTRADICTED | lifecycle/idempotency claims stronger than implementation |
| 40 | Historical-learning | VERIFIED | repair history and rejected evaluations retained |
| 41 | Inspiration/reference | VERIFIED | research inputs explicitly documented |
| 42 | Negative-space | VERIFIED for reviewed canonical roots | no sibling canonical-store takeover found |
| 43 | Architecture-vs-operation | PARTIAL/CONTRADICTED | owner architecture strong; lifecycle/concurrency gaps |
| 44 | Current-target readiness | **BLOCKED** | WSA-006 BLOCKER + WSA-007/008 HIGH |
| 45 | Final seamless-system gap | UNVERIFIED BY DESIGN | A2-A5 own whole-system proof |
| 46 | Scope-creep / definition-of-done | VERIFIED | F1/I1 explicitly reject unsupported new authority layers |

## 26. Negative-space checks

Within reviewed canonical Gateway roots, A1.2 found no evidence that Gateway:

- opens a sibling canonical database directly;
- creates a fallback Goal database;
- treats client actor headers as authentication;
- stores plaintext Gateway bearer tokens;
- writes provider API-key values into config;
- treats capability discovery as permission;
- allows runtime output to inject trusted owner scope/provenance/consent fields;
- silently creates a durable Bot without admitted explicit consent;
- silently creates a recurring Automation from repeated need alone;
- recursively creates Automations from Automation-triggered runs;
- promotes a full transcript automatically into Memory;
- treats fold summaries as canonical raw history;
- exposes raw prompt bodies/chain-of-thought through advanced diagnostics;
- crosses workspace/principal boundaries in fold/progressive exact-source retrieval;
- claims transparent arbitrary provider-process recovery;
- invents a branch catalog or cross-owner orientation graph without an owner.

Negative claims are limited to the frozen tracked canonical implementation/tests.

## 27. Adversarial targets deferred to A4

A1.2 records these for later hostile testing rather than over-claiming:

- unauthenticated invalid-bearer CPU pressure, because synchronous scrypt runs before authenticated principal rate limiting;
- high-rate SSE connection/resource exhaustion;
- malformed/manual config values not created by normal setup;
- remote proxy/origin deployment mistakes;
- subprocess adapter that ignores termination or forks children;
- disk-full/permission-loss behavior during append-only events/audit.

## 28. Outbound cross-repository claims for A2

These are Gateway claims only.

### OS

Gateway claims:

- OS exposes `ai-verse-brain-bridge/1.0`;
- OS owns action authorization and final host routing;
- discovery/current-context/Memory/Skills/Data/Connections views arrive through that host.

### Brain

Gateway claims:

- Brain owns Goals/strategic intent;
- Goal continuation requires a separate `ai-verse-goal-owner/1.0`;
- no configured Goal owner means Goal-bound autonomous continuation is unavailable;
- exact version/activation-epoch changes revoke continuation.

### Memory

Gateway claims:

- historical retrieval comes through OS/Memory owner projections;
- completed meaningful sessions may produce compact owner-routed digests;
- raw Gateway transcripts remain Gateway run evidence and are not wholesale Memory imports.

### Skills

Gateway claims:

- capability discovery/instructions are owner-routed through OS;
- learned-skill candidates cannot receive runtime-forged identity/provenance.

### Data

Gateway claims:

- structured truth reads/writes route through OS/owner contracts;
- runtime cannot inject trusted Data scope/actor/idempotency.

### Multiple Bots

Gateway claims:

- one bounded automatic temporary specialist may be admitted under strict evidence/budget/runtime gates;
- durable Bots require explicit consent;
- Gateway does not own canonical Bot registry/coordination.

### Automations

Gateway claims:

- repeated responsibility may be recommended without schedule creation;
- durable recurrence requires explicit consent;
- owner wake ingress creates an ordinary bounded Gateway run;
- one invocation ID is intended to be replay-safe, subject to WSA-008.

### Connections

Gateway claims:

- it consumes bounded owner metadata and does not own external credential truth.

### Token

Gateway claims:

- runtime-reported usage/cost is operational run evidence/budget input;
- canonical normalized Token/cost truth is not Gateway-owned.

### Dashboard / client UI

Gateway claims:

- it provides OpenAI-compatible and richer run/event/control surfaces;
- presentation/control-room truth remains outside Gateway.

### Distribution

Gateway publishes package/component lifecycle metadata suitable for external installation/release composition. Formal release-set truth is deferred to A5.

## 29. Evidence inventory

### E-A1.2-001 — frozen tree and repository metadata
Source: recursive Git tree/repository metadata at `46c15ee58b028dd7fb8b310327ea705ef618805e`.  
Supports: complete 87-entry inventory, public repo, JavaScript, MIT.

### E-A1.2-002 — identity/package/component contract
Sources: `README.md`, `package.json`, `component.json`, `LICENSE`.  
Supports: product role, version, Node baseline, canonical owned/not-owned state.

### E-A1.2-003 — architecture/protocol/security
Sources: `docs/ARCHITECTURE.md`, `docs/PROTOCOL.md`, `SECURITY.md`.  
Supports: owner map, run state machine, host/Goal contracts, threat-model claims.

### E-A1.2-004 — lifecycle/CLI implementation
Sources: `src/cli.mjs`, `src/paths.mjs`, `src/config.mjs`, `src/lifecycle.mjs`.  
Supports: lifecycle reconstruction and WSA-006/007.

### E-A1.2-005 — server/auth boundary
Sources: `src/server.mjs`, `src/auth.mjs`.  
Supports: bearer principal, origins, loopback/remote guard, body/rate limits, live lifecycle evidence.

### E-A1.2-006 — store/durability implementation
Sources: `src/store.mjs`, `src/util.mjs`.  
Supports: session/run state, atomic replacement, idempotency implementation, recovery and WSA-008.

### E-A1.2-007 — run engine and privileged controls
Source: `src/run-engine.mjs`.  
Supports: budgets, Goal lease, tool authority, approval recheck, pause/cancel, stale-state race, post-completion handoffs.

### E-A1.2-008 — adapter/runtime/subprocess boundaries
Sources: `src/host-adapter.mjs`, `src/goal-owner.mjs`, `src/runtime.mjs`, `src/subprocess.mjs`.  
Supports: owner routing, versioned protocols, bounded subprocess/env.

### E-A1.2-009 — Context Ladder implementation
Sources: context governor, fold store/engine/archive, progressive context.  
Supports: raw-source canonicality, immutable folds, scope/fingerprint/budget enforcement.

### E-A1.2-010 — core test suite
Source: 13 `test/*.test.mjs` files executed by package check.  
Supports: lifecycle happy path, security, owner routes, Context Ladder, recovery.

### E-A1.2-011 — exact-head CI
Run `34992616000`; six Node 20/22 x Linux/macOS/Windows jobs SUCCESS.  
Supports: current frozen source executes complete `npm run check` cross-platform.

### E-A1.2-012 — current merged PR-head integration
PR #31 head `a08056e3809b17198082523365902273a525f656`; runs `34990219367`, `34990219479`, `34990219501`, `34990219558`, `34990219447`.  
Supports: PR-only cross-owner composition on exact source merged to frozen head.

### E-A1.2-013 — current lifecycle test coverage gap
`test/clean-install.test.mjs` explicitly closes the live server before disable/uninstall.  
Supports: WSA-007 is not covered by the green happy-path lifecycle test.

### E-A1.2-014 — concurrency test coverage gap
`test/security-and-recovery.test.mjs` covers sequential idempotency conflict and valid atomic file replacement, but no concurrent semantic idempotency/session/control transition.  
Supports: WSA-008.

### E-A1.2-015 — destructive purge trace
`parseArgs --home` + `gatewayHome(path.resolve)` + `uninstallComponent rm(home,{recursive:true,force:true})`.  
Supports: WSA-006.

### E-A1.2-016 — rejected architecture evaluations
Sources: F1 and I1 evaluation docs/tests.  
Supports: scope-control / no invented branch or cross-owner graph authority.

### E-A1.2-017 — history and research provenance
Sources: current/recent commits, Gateway PR history, `docs/RESEARCH.md`.  
Supports: repair sequence and benchmark provenance.

### E-A1.2-018 — GitHub release state
Gateway GitHub Releases endpoint returned no release objects at the frozen point.  
Supports: release lens limitation only; A5 owns release-set validation.

### E-A1.2-019 — live control-state recheck
Sources: live Gateway/System refs and open PR search immediately before packet creation.  
Result: frozen Gateway ref unchanged, System baseline unchanged, zero Gateway/System open PRs.

## 30. Evidence limitations

- A1.2 does not independently verify sibling repo correctness.
- Cross-owner workflow success proves Gateway composition against pinned revisions only.
- The destructive purge defect was **not executed against real data**; static implementation evidence is unambiguous and sufficient for a data-loss BLOCKER.
- Concurrent race findings were not added as new product tests because A0-A6 is read-only for product repos; the interleavings are established from executable read/check/write ordering.
- No real external OpenAI-compatible provider was required for exact-head CI; deterministic/subprocess paths and protocol behavior are tested.
- No production network latency/throughput SLO is claimed.
- Remote hostile-load testing is deferred to A4.
- No GitHub Release object exists; broader release/candidate validation is deferred to A5.

## 31. Standalone definition of done

A1.2 evidence collection is complete because:

- the exact frozen ref remained stable;
- repository shape/canonical roots are classified;
- identity/build/license/ownership are reconstructed;
- lifecycle/server/runtime/store/run/context boundaries are inspected;
- all relevant current tests and CI are inspected;
- security, isolation, permissions, idempotency, concurrency and recovery are inspected;
- all 46 lenses are classified;
- contradictions are recorded explicitly;
- negative-space checks are bounded;
- external claims are extracted without validating the sibling side;
- material defects have stable findings and closure evidence.

## 32. Standalone verdict

**AI-Verse-Gateway at `46c15ee58b028dd7fb8b310327ea705ef618805e`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

Strong current areas include:

- clear owner boundaries;
- bearer identity and loopback-default security;
- late OS authorization/approval recheck;
- conservative Bot/Automation consent;
- fail-closed Goal-owner absence;
- cross-platform test coverage;
- restart-safe run/digest/organization behavior;
- scoped/fingerprinted Context Ladder retrieval and derived folding;
- explicit rejection of unowned architecture bloat.

However, current Gateway cannot pass the dogfood gate because:

1. `WSA-2026-006` is a **BLOCKER** data-loss risk in destructive purge;
2. `WSA-2026-007` is **HIGH** lifecycle truth/live-service inconsistency;
3. `WSA-2026-008` is **HIGH** non-linearizable concurrency affecting idempotency/session/control semantics.

No product repair is made during A1.2.

## 33. Progress after audit acceptance

- weighted audit progress: **9 / 100 = 9%**
- weighted remaining: **91%**
- tracker tasks complete: **7 / 51**
- tracker tasks remaining: **44 / 51**
- phases fully complete: **1 / 7**
- phases remaining/not-yet-complete: **6 / 7**
- A1 repository audits complete: **2 / 14**
- A1 repository audits remaining: **12 / 14**
- A1 weighted progress: **4 / 28**
- next task: **A1.3 AI-Verse-Brain**

These are audit-completion metrics only. Dogfood remains blocked.

## 34. Task completion record

**Task:** A1.2 AI-Verse-Gateway  
**Reviewed repository ref:** `46c15ee58b028dd7fb8b310327ea705ef618805e`  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / DOGFOOD BLOCKED  
**Evidence read:** Sections 3-19 and evidence inventory  
**Tests/CI inspected:** exact-head six-job CI + exact merged PR-head PR-only integration gates  
**Contradictions:** `C-A1.2-001`, `C-A1.2-002`, `C-A1.2-003`  
**Findings opened:** `WSA-2026-006`, `WSA-2026-007`, `WSA-2026-008`  
**Findings inherited:** `WSA-2026-001` through `WSA-2026-005` unchanged  
**Negative-space checks:** Section 26  
**Evidence limitations:** Section 30  
**Standalone verdict:** COMPLETE / DOGFOOD BLOCKED  
**Tracker change:** A1.2 COMPLETE; accepted audit progress 9/100; A1.3 NEXT  
**Next task:** A1.3 AI-Verse-Brain
