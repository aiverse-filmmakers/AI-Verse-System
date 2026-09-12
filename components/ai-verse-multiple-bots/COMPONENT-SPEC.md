# AI-Verse Multiple Bots Component Specification

**Component:** AI-Verse Multiple Bots  
**Repository reviewed:** aiverse-filmmakers/AI-Verse-Multiple-Bots  
**Reviewed branch:** main  
**Reviewed head:** 9874d413f5e23c9a869bf3ccead0f2751026a732  
**Reviewed tree:** 37737a579bd4c6984ba31b3d786d0e225e2e92ee  
**Review date:** 2026-09-13  
**Method:** docs/AUDIT-METHODOLOGY.md from AI-Verse-System was read first and applied as the governing forensic method.  
**Scope rule:** the independent baseline was reconstructed from AI-Verse-Multiple-Bots only. AI-Verse-System living specifications were consulted afterward only for cross-component contract comparison. No sibling repository was audited as part of this pass.

---

## 1. Executive identity

**CURRENT:** AI-Verse Multiple Bots is the coordination and persistent-teammate layer of AI-Verse.

It provides two deliberately different kinds of execution identity:

- durable named Bots that can own ongoing responsibilities, receive messages, work in Rooms, delegate, hand off, and remain addressable over time;
- temporary Workers that exist only inside a bounded Team Run and are never promoted into the durable Bot registry.

It also owns the coordination machinery around those identities:

- Messages and delivery state;
- Rooms and Threads;
- Tasks and Task ownership;
- Handoffs;
- Team Runs and topology state;
- temporary Worker lifecycle;
- capability leases;
- environment leases;
- Approvals;
- coordination Artifacts and Events;
- budgets, cancellation, loop guards and recovery;
- remote execution recovery needed to preserve local Task semantics across remote runtimes.

**LAW:** Multiple Bots is not a second AI-Verse OS, second Brain, second Memory, second Skills registry, second scheduler, Data engine, secret store, or UI source of truth.

**CURRENT VERDICT:** the core coordination engine is strong and mature through Phase 4.8. The repository has not reached its present canonical milestone because Phase 4.9, the compatibility/evaluation suite, is explicitly NEXT and has not started. It also contains several cross-component and control-plane defects that must be repaired before “works perfectly like a glove” is an accurate description.

The most important current defects found by this audit are:

1. **GAP - Brain contract drift:** native Brain ingress still requires tracked AI-VERSE.yaml extensions.brain registration, while the current hardened Brain contract uses .aiverse/extensions/registry.json and treats tracked manifest registration as legacy.
2. **GAP - Data integration absent:** there is no AI-Verse Data adapter, contract, runtime projection or test in Multiple Bots.
3. **GAP - unauthenticated HTTP control plane:** the Gateway accepts mutating caller-supplied identities and operator-looking actor IDs without transport authentication. Loopback is the safe current assumption.
4. **GAP - direct-message idempotency is incomplete:** a repeated send with the same idempotency key creates a new Message and delivery; only the Event is deduplicated.
5. **GAP - package/product path is unfinished:** Phase 5 has not started, package metadata is not yet a complete public distribution contract, and secure remote Gateway, onboarding, Dashboard/channel surfaces and release acceptance remain pending.
6. **GAP - current main merge commit has no direct CI run returned at audit time:** Phase 4.8 PR-head CI is green at 412/412, but this must not be misstated as merge-commit CI.

---

## 2. Status vocabulary

This specification uses:

- **CURRENT** - proven by current implementation, tests or current authoritative status evidence.
- **LAW** - invariant that should survive implementation changes.
- **INTENDED** - accepted desired behavior not fully implemented.
- **GAP** - missing or contradictory path between CURRENT and INTENDED.
- **HISTORICAL** - prior behavior, repair, branch or document that matters as lineage but is not current truth.
- **INSPIRATION** - external systems deliberately studied and curated into the design.

Where evidence conflicts, executable current code and current tests outrank stale prose.

---

## 3. Role in the complete system

The intended AI-Verse topology is:

    OS / host
      owns scope, routing, canonical workspace context, host policy,
      component discovery, connections and owner-controlled writes

    Brain
      owns strategic intent, initiatives, objectives and verification logic

    Memory
      owns durable historical memory

    Skills
      owns reusable capability packages and immutable capability generations

    Data
      owns canonical structured data, schemas, queries, transactions,
      migration, backup and data integrity

    Automations / cadence owner
      owns schedules and recurring trigger execution

    Multiple Bots
      owns persistent teammate identity and coordination

    Runtime adapters
      execute bounded Tasks under local authority

    Dashboard / channels
      observe and control coordination without becoming canonical truth

**CURRENT:** Multiple Bots has explicit native adapters for OS workspace context, Brain objectives, Memory recall, Skills resolution, Automations ingress, OS write-command intake and Four Cs evidence.

**GAP:** Data is missing from that native integration set.

---

## 4. Problem the component solves

A single-agent runtime does not provide a durable answer to:

- Who owns a long-running responsibility?
- How does one Bot asynchronously message another?
- How is one final owner maintained while specialists contribute?
- How can durable teammates form temporary squads without creating permanent persona sprawl?
- How are delegation and handoff kept semantically distinct?
- How are tools, connections and environments narrowed per Task?
- How are approvals, budgets, cancellation and loops enforced outside model prose?
- How is remote execution resumed after disconnect without duplicating side effects?
- How can several runtimes interoperate while local Task ownership remains canonical?
- How can AI-Verse Memory, Skills, Brain and host context be used without copying them into another source of truth?

Multiple Bots exists to solve those coordination problems as a reusable layer.

---

## 5. Current architecture

### 5.1 Persistent teammate layer

**CURRENT:** durable Bots are registered objects with stable IDs, names, role metadata, runtime configuration, execution policy, scope, permissions and coordination settings.

A Bot can be:

- active;
- disabled;
- archived.

Archived identity is terminal and retained for audit/collision safety.

### 5.2 Temporary squad layer

**CURRENT:** Team Runs create run-scoped Workers.

Workers:

- use worker_* identities;
- never enter the durable Bot registry;
- belong to one Team Run;
- must remain in the Team Run workspace;
- require a real Task before becoming executable;
- receive bounded authority;
- expire during terminal cleanup;
- retain audit evidence without becoming permanent teammates.

### 5.3 Coordination Gateway

**CURRENT:** CoordinationGateway is the package coordination boundary for Bot registration, Tasks, messaging, Handoffs, Approvals, events and execution interactions.

**LAW:** UI/channel/runtime adapters must call coordination semantics rather than implement competing ownership rules.

### 5.4 Durable SQLite coordination state

**CURRENT:** CoordinationStore uses SQLite and stores canonical package coordination objects and operational coordination state.

It contains, among other things:

- protocol objects;
- ordered events;
- delivery state;
- idempotency receipts;
- execution queue/recovery tables;
- Phase 4.8 remote recovery state.

**GAP / DOCUMENTATION DRIFT:** PERSISTENT-TEAMMATE-ARCHITECTURE.md contains older language describing runtime SQLite as rebuildable/disposable. That is not true of current implementation. Current SQLite contains package-owned canonical coordination history and operational recovery state that cannot be reconstructed from AI-Verse OS files alone.

**LAW:** a derived index may be disposable only if a proven canonical source can rebuild it. The Multiple Bots coordination database is not merely a derived index.

---

## 6. Canonical ownership

**CURRENT:** Multiple Bots canonically owns:

- durable Bot coordination identity and lifecycle;
- temporary Worker identity and lifecycle;
- Room and Thread coordination records;
- Messages and package delivery state;
- Tasks;
- Handoffs;
- Team Runs and topology state;
- capability and environment leases used by coordination;
- package Approvals;
- coordination Artifacts;
- coordination Events;
- execution queue state;
- package recovery state;
- runtime receipts and provenance required for coordination audit;
- remote recovery checkpoints needed to preserve exact local Task semantics.

The component may preserve bounded external-source references and digests as provenance without taking ownership of the referenced external state.

---

## 7. Explicit non-ownership

**LAW:** Multiple Bots must not canonically own:

- OS operator/workspace truth;
- canonical current context;
- strategic Brain intent or objective lifecycle;
- general durable Memory;
- reusable Skills packages;
- Data records/schemas/transactions;
- connection credentials;
- raw secrets;
- global scheduler state;
- automation definitions;
- vendor runtime session state as AI-Verse truth;
- Dashboard state as truth;
- external provider identity as a replacement for local Bot identity.

### Anti-duplication rule

External state may enter a Task only as:

- bounded runtime projection;
- owner-provided retrieval result;
- immutable reference;
- digest/provenance;
- explicit owner receipt.

It must not be copied merely because a model consumed it.

---

## 8. Sources of truth

| Concern | CURRENT canonical owner |
|---|---|
| Bot identity and coordination role | Multiple Bots |
| Worker identity | Multiple Bots Team Run |
| Message/Room/Thread coordination | Multiple Bots |
| Task/Handoff/Team Run | Multiple Bots |
| Capability/environment Task lease | Multiple Bots |
| Workspace current truth | OS / host |
| Strategic direction/objective | Brain when Brain owns that scope, otherwise owning host |
| Historical memory | Memory / host |
| Reusable capability package | Skills |
| Structured data | Data |
| Schedule/trigger definition | Automations / cadence owner |
| Connection credential | Host/Connections/credential owner |
| Remote runtime profile | External runtime provider |
| Local coordination result Artifact | Multiple Bots |
| Canonical domain promotion of a result | Owning component through owner-controlled write boundary |

---

## 9. Runtime model

### 9.1 Common execution principal

**CURRENT:** durable Bots and temporary Workers use a shared execution-principal contract.

Workers are not synthesized as fake durable Bot manifests.

### 9.2 Runtime registry

**CURRENT:** runtime execution is adapter-based.

Current runtime/interoperability surfaces include:

- deterministic local runtime;
- OpenAI-compatible HTTP runtime;
- A2A v1 runtime;
- Hermes stdio/TUI-gateway runtime;
- OpenClaw one-shot agent execution;
- Codex one-shot process execution;
- Claude Code one-shot print execution;
- external-managed persistent Bot provider.

### 9.3 Authority ordering

The effective runtime context keeps authoritative constraints ahead of softer context.

Conceptually:

    Task constraints and approvals
    > capability/environment leases
    > current workspace/strategic context
    > task-scoped Skills
    > historical recall
    > input artifacts

**LAW:** retrieved Memory or Skill instructions cannot widen Task authority.

### 9.4 Runtime result boundary

**CURRENT:** successful runtime output becomes a local Artifact only after local Task and authority checks.

Remote or provider success does not itself become canonical AI-Verse domain truth.

---

## 10. Scope and isolation

### 10.1 Workspace isolation

**CURRENT:** core Bot/Worker/Task/Team Run code strongly checks workspace identity.

Examples include:

- durable workspace Bots must belong to the exact workspace;
- Room members must be active Bots in the Room workspace;
- Workers remain in one Team Run workspace;
- parent/child Tasks preserve workspace and root objective;
- capability/environment leases bind principal, Task and workspace;
- Artifacts are scope-checked;
- Memory and Skills projections reject cross-workspace output;
- Brain objective ingress binds an exact workspace and strategic lineage.

### 10.2 Operator scope

Operator-scoped durable Bots are distinct from workspace-scoped Bots.

Temporary Workers cannot request operator-scoped OS writes.

### 10.3 Environment isolation

Current environment policies include:

- shared_workspace;
- isolated_bot;
- isolated_run;
- external_managed.

**LAW:** the model does not choose a broader environment. The host supplies or validates the environment handle.

### 10.4 Remaining ingress weakness

**GAP:** HTTP caller identity is not authenticated.

The internal workspace checks are meaningful only if the actor identity reaching them is trustworthy.

A caller can submit arbitrary actorId, senderId, requestedBy and similar fields to the HTTP server. Some code paths treat strings beginning with operator_ as operator decisions.

Therefore:

    strong internal scope checks
    !=
    authenticated remote control plane

The current safe deployment assumption is local/trusted access, especially because the CLI defaults to 127.0.0.1.

---

## 11. Current lifecycle

### Install

**CURRENT:** source/package development installation works sufficiently for repository development.

**GAP:** final member-facing package/install path is Phase 5 and is not implemented.

The package currently identifies itself as @ai-verse/multiple-bots version 0.1.0-alpha.1, but package metadata is not yet a complete public distribution surface.

### Attach/register

**CURRENT:** AI-Verse OS registration uses only:

    .aiverse/extensions/registry.json

It avoids tracked OS-file mutation and preserves sibling/unknown registry fields.

### Initialize

**CURRENT:** coordination state initializes when the Gateway/store is created.

**GAP:** this is an engine initialization path, not a productized “adopt Multiple Bots into this existing host/team” workflow.

### Enable/disable

**CURRENT:** durable Bots can be activated/disabled.

**CURRENT:** the OS extension registry contains enabled state and upgrade preserves user-disabled state.

**GAP:** a complete member-facing component enable/disable adoption flow is not a finished Phase 5 product surface.

### Status/doctor

**CURRENT:** store.doctor provides structural coordination-database checks.

**CURRENT:** Four Cs projection provides bounded coordination evidence.

**GAP:** no production aggregate doctor proves package, runtime adapters, OS attachment, sibling integrations, remote trust, data integration, channel control and current release health in one supported command.

### Update

**CURRENT:** Phase 3.10 provides bounded extension upgrade behavior after extension-owned files exist.

**GAP:** production package update, release migration and rollback strategy remain Phase 5.

### Detach/uninstall

**CURRENT:** extension uninstall removes only owned registration and known extension files while preserving coordination state and canonical sibling state.

**LAW:** uninstall must not recursively scavenge unknown user/component state.

### Reinstall/reconcile

**CURRENT:** preserved coordination state can survive extension uninstall.

**GAP:** final member-facing reinstall/reconcile path is not yet release-proven.

---

## 12. Migration/history integration

### Coordination database

**CURRENT:** the coordination database is preserved across uninstall.

**GAP:** the current store schema is created as schema version 1 and does not expose the richer explicit versioned migration history that appeared in an earlier unmerged hardening branch.

As the database is package-owned durable state, future schema evolution needs an explicit migration/backup/recovery contract before public stable release.

### Existing Bots/teams

**GAP:** there is not yet a general import/adoption flow for a pre-existing external agent roster into durable Multiple Bots identities.

External-managed bindings can map a durable local Bot to a long-lived external profile, but that is not a complete migration wizard.

### External history

**LAW:** importing historical chat/memory into Multiple Bots must not create a second Memory system. Historical material should remain Memory/host-owned unless it is truly coordination history owned by this package.

---

## 13. Intended lifecycle

The seamless lifecycle target is:

    install package
      -> discover compatible host
      -> materialize extension files
      -> attach/register
      -> explicitly enable
      -> initialize/recover coordination state
      -> adopt/map existing teammate identities when requested
      -> validate sibling contracts
      -> run health/conformance checks
      -> operate
      -> update with migrations
      -> disable or detach without deleting canonical state
      -> reinstall/reconcile preserved state

**INTENDED:** chronology must not decide ownership.

---

## 14. Install-order independence

### Standalone before OS

**CURRENT:** the core coordination package is host-neutral and can operate without AI-Verse OS.

### OS before Multiple Bots

**CURRENT:** the extension registration design supports later attachment without tracked OS mutation.

### Brain/Memory/Skills installed later

**CURRENT WITH LIMITATIONS:** runtime wrappers are optional and explicit dependencies generally fail closed only when requested.

**GAP:** Brain integration currently relies on a legacy registration signal and therefore does not fully satisfy order-independent current-generation Brain attachment.

### Data installed later

**GAP:** there is no Multiple Bots Data integration to discover or adopt later.

### Remote runtimes later

**CURRENT:** host-injected registries/providers allow runtime adapters and remote providers to be added without moving local Bot identity.

---

## 15. Activation/adoption by existing agents

**CURRENT:** external-managed runtime lets one durable Multiple Bots Bot bind to a persistent external provider/profile while keeping local Bot identity canonical.

**CURRENT:** Hermes, OpenClaw, Codex, Claude Code and A2A adapters allow bounded execution through other runtimes.

**GAP:** this is runtime interoperability, not yet a universal “turn my existing agent/team into a managed Multiple Bots team” product transaction.

A complete adoption flow still needs to decide and verify:

- whether an external agent maps to a durable Bot or remains only a runtime;
- workspace/scope;
- capabilities and connections;
- environment policy;
- historical coordination import, if any;
- channel identity;
- manager/peer relationships;
- Memory/Skills/Data availability;
- activation health.

---

## 16. Portability outside AI-Verse OS

**CURRENT:** portability is a real architectural property.

The core:

- uses package-owned protocol/store/runtime abstractions;
- can operate standalone;
- does not require Brain, Memory, Skills or Data for ordinary work;
- supports host-injected runtimes/providers;
- keeps AI-Verse-native adapters optional.

**CURRENT:** non-AI-Verse hosts can use the coordination library and runtime adapters without adopting AI-Verse OS canonical state.

### Portability limitations

**GAP:** CI runs only on Ubuntu/Node 22.

There is no current Windows/macOS package matrix proving the full process/runtime adapter set.

**GAP:** public packaging/install UX is not complete.

**LAW:** host neutrality must not be confused with proven cross-platform release readiness.

---

## 17. Sibling integrations

### 17.1 AI-Verse OS

**CURRENT:** registration, workspace projection, Automations receive-side ingress, owner-controlled write-command transport, candidate writeback and Four Cs projection exist.

**LAW:** Multiple Bots must call OS/owner boundaries, not mutate canonical OS domain files.

### 17.2 Brain

**INTENDED:** Brain remains canonical for strategic intent and objective lifecycle. Multiple Bots receives a bounded objective projection and revalidates freshness before execution.

**GAP - CURRENT CONTRACT BREAK:** Multiple Bots checks AI-VERSE.yaml for exactly one extensions.brain block with supported/enabled flags.

The current AI-Verse Brain specification states:

- current native attachment uses .aiverse/extensions/registry.json;
- tracked manifest registration is legacy;
- current Brain init/attach does not require the old manifest slot.

The Multiple Bots test fixture still manufactures the legacy AI-VERSE.yaml extensions.brain block.

Therefore Phase 3.3’s “complete” status is complete against its historical fixture, not against the current hardened Brain lifecycle.

**Required correction:** Brain availability/enabled state must be resolved through the current owner-supported Brain/OS lifecycle boundary. Multiple Bots should not maintain a stale parallel Brain-registration parser.

### 17.3 Memory

**CURRENT:** explicit Task recall goes through the installed Memory engine boundary rather than directly owning Memory SQLite.

Recall is bounded, scoped and ephemeral.

Persisted coordination receipts contain provenance/digests rather than recalled text.

**LAW:** Memory recall is context, not coordination authority.

### 17.4 Skills

**CURRENT:** Multiple Bots requests Skills through the OS-owned capability resolver.

Task Skills are explicit, bounded and workspace-scoped.

Selected SKILL.md instructions are ephemeral.

**LAW:** Skill instructions define method, not permission.

### 17.5 Data

**GAP:** no AI-Verse Data integration is present in current Multiple Bots source, docs, tests or canonical build map.

The AI-Verse OS contract already establishes that Data owns structured records, schemas, query/aggregate, relations, transactions, idempotency, events/receipts, migration/backup and database integrity, and that OS must call Data through its supported boundary rather than opening Data SQLite.

**INTENDED:** Multiple Bots should use an owner-controlled Data query/write route when a Task explicitly requires structured data.

It must not:

- open Data SQLite directly;
- copy Data into its own canonical tables;
- silently treat a runtime Artifact as canonical structured data;
- create a second structured-data store.

Data write semantics should follow the shared owner-routed write pipeline once canonical handlers exist.

### 17.6 Automations/Cadence

**CURRENT:** Multiple Bots receives automation invocations.

It does not become a scheduler.

**LAW:** schedule ownership remains outside Multiple Bots.

### 17.7 Connections/secrets

**CURRENT:** capability leases carry exact connection references.

Remote credentials use opaque handles and host-injected authenticators.

**LAW:** teammate collaboration never implies credential pooling.

---

## 18. Permissions, security and privacy

### 18.1 Internal authority model

**CURRENT:** the core contains strong non-expansion checks:

- child Task constraints inherit;
- root objective lineage is preserved;
- Task hop/budget ceilings apply;
- tools/connections are bounded;
- Workers cannot widen leader authority;
- Handoffs reissue bounded authority rather than copying unrestricted access;
- remote grants may narrow but not widen local authority;
- external provider observed authority is audited;
- remote lease expiry is bounded by local authority and deadlines.

### 18.2 Approvals

**CURRENT:** approval-required work is represented explicitly.

Runtime execution checks Task/lease/Approval state.

**LAW:** the acting model must not be the sole authority for consequential action.

### 18.3 Secret boundary

**CURRENT:** raw manifest secrets are rejected in remote/provider configuration paths.

Host-injected credential/authenticator mechanisms own secret resolution.

### 18.4 Control-plane authentication gap

**GAP - HIGH:** createGatewayServer has no authentication middleware.

The HTTP API allows mutations including Bot creation, lifecycle operations, messages, delegation, approvals, recovery and native integration ingress.

Actor identity is supplied in request JSON.

The operator guard is string-based:

    actorId starts with "operator_"

That is an internal protocol role convention, not authentication.

The server also accepts a configurable bind host, so operators must not expose the current Gateway as a trusted remote administrative API.

**Required current law:**

> Protocol actor identity and authenticated control-plane principal are different concepts. Any network-exposed mutating Gateway must authenticate the caller and map that authenticated principal to allowed protocol actors before internal policy is evaluated.

### 18.5 Request-size gap

**GAP:** generic readJson buffers the full request body without a top-level HTTP body ceiling.

Many downstream object paths have bounded validators, but the transport itself should apply a maximum before buffering untrusted network input.

---

## 19. Failure and degraded modes

**CURRENT:** the repository generally prefers fail-closed behavior.

Examples:

- incompatible OS native mode fails;
- explicit unavailable Memory/Skills fails when requested;
- invalid workspace fails;
- authority widening fails;
- expired/revoked leases fail;
- stale Brain intent fails;
- ambiguous remote SendMessage fails without an explicit exactly-once recovery contract;
- remote lease mismatch fails;
- external provider errors do not become successful local Artifacts;
- cancellation remains locally authoritative even if remote cleanup fails.

### Recovery hierarchy

Local execution queue/recovery remains canonical.

Phase 4.8 adds remote recovery below runtime adapters so a locally requeued Task can resume the same remote logical work.

**LAW:** remote recovery must never silently create another logical operation because the response was lost.

---

## 20. Messaging and idempotency

### Direct messages

**CURRENT DEFECT:** gateway.sendMessage creates:

- a new random Message ID;
- a new random delivery ID;

before emitting an Event with the optional idempotency key.

The idempotency key therefore deduplicates only the Event layer.

An identical client retry can create multiple Messages and deliveries.

This contradicts the protocol’s stronger intended mailbox/idempotency semantics.

### Historical repair evidence

**HISTORICAL:** closed PR #6, “Build durable Bot-to-Bot mailbox”, implemented deterministic message/delivery/event identity and request fingerprints so exact replay created one logical send and changed semantics under the same key failed closed.

That PR was not merged into current main.

**LAW:** an API operation advertised as idempotent must bind the complete logical mutation, not one audit event inside it.

### Room messages

**CURRENT:** lower-level publishRoomMessage can receive stable message/event identity, but the Room/server convenience paths do not consistently expose that complete retry contract.

### Delegation/retry

**CURRENT:** duplicate-active Task detection and several specialized ingress flows provide deterministic identity.

**GAP:** generic recovery_policy=retry_safe is still a caller-declared classification for ordinary local execution. The remote Phase 4.8 paths are stronger because they require explicit exact-key semantics before replay.

Before a network API is trusted with arbitrary clients, retry safety should be authorized by the runtime/action contract or authenticated owner policy rather than accepted as an untrusted semantic assertion.

---

## 21. Persistent teammate and routing semantics

**CURRENT:** the architecture correctly separates:

- persistent teammate identity;
- temporary specialist execution;
- delegation;
- ownership handoff;
- group discussion;
- manager coordination;
- parallel panel;
- verifier/critic;
- synthesis.

### One-owner law

**LAW:** parallel intelligence does not imply parallel final ownership.

A Task, Handoff stage or final synthesis has one active owner.

### Rooms

**CURRENT:** Rooms are real coordination objects, not transcript concatenation.

They have membership, bounded speaker scheduling, Threads and Artifact/result publication.

### Managed-channel future

**INTENDED:** Telegram/Discord/channel bridges should preserve leader ownership and exclusive routing.

TELEGRAM-MANAGED-TEAM-CONTRACT.md is future guidance, not current channel implementation.

---

## 22. Team Run topologies

**CURRENT:** supported coordination strategies include:

- single;
- manager;
- handoff;
- parallel_panel;
- group_room;
- pipeline;
- review;
- dynamic_squad;
- hybrid.

**CURRENT:** adaptive decision policy chooses the minimum justified supported collaboration mode.

**LAW:** more agents is not automatically better.

### Fan-out and joins

**CURRENT:** fan-out is bounded by:

- Team Run worker/task capacity;
- concurrency;
- token/cost/action budgets;
- Task leases;
- join policy.

Current join patterns include all, first_success and bounded quorum.

### Disagreement and verifier

**CURRENT:** disagreement is represented as structured evidence, not hidden reasoning.

Verifier work is created only when warranted by verification debt.

### Synthesis

**CURRENT:** the durable Team Run leader owns final synthesis.

Unresolved verification debt/live temporary work blocks finalization.

---

## 23. Cancellation, budgets and loop safety

**CURRENT:** the package has:

- per-Task budgets;
- Team Run aggregate budgets;
- wall-clock deadlines;
- task/worker/hop/message/round ceilings;
- no-progress loop protection;
- repeated pair/transition protection;
- cancellation propagation;
- terminal fences;
- dead-letter handling;
- Worker cleanup.

**LAW:** a canceled or terminal run must not be resurrected by retry/recovery/topology reconciliation.

---

## 24. Remote interoperability

### A2A

**CURRENT:** A2A v1 JSON-RPC execution supports discovery, exact interface selection, local identity preservation, Task/Message translation, cancellation and bounded output.

### Remote identity/auth

**CURRENT:** Phase 4.6 establishes:

- pinned remote machine identity;
- exact HTTPS origin;
- no TOFU;
- opaque credential reference;
- declared security requirement verification;
- host-injected authenticator registry;
- redirect protection.

### Remote capability/environment leases

**CURRENT:** Phase 4.7 establishes:

- local lease remains canonical;
- remote authority can only stay equal or narrow;
- exact tool/connection references;
- bounded destructive-action policy;
- bounded expiry;
- environment identity/policy verification;
- post-run lease receipt audit.

### Remote retry/reconnect

**CURRENT:** Phase 4.8 establishes:

- durable remote recovery journal;
- submitting/remote_active/completed states;
- exact operation identity;
- A2A resume by server Task ID;
- fail-closed ambiguous submission;
- explicit recovery extension for safe logical replay;
- external-managed exact_task_key contract;
- durable failed-revocation reconciliation;
- cached verified result until local settlement.

**LAW:** Multiple Bots owns local Task truth even when another runtime performs execution.

---

## 25. Health and observability

### Store doctor

**CURRENT:** coordination store doctor proves structural package persistence health.

### Four Cs

**CURRENT:** Four Cs projection provides conservative evidence to the owning OS audit layer.

It does not invent a competing score.

### Missing production health

**GAP:** Phase 5 still needs a production doctor that can distinguish:

- package installed;
- extension attached/enabled;
- database healthy;
- runtime adapter reachable;
- native sibling contract compatible;
- remote trust/auth healthy;
- pending dead letters/revocations;
- Data integration present or absent;
- channel/dashboard exposure;
- authentication mode;
- release version.

---

## 26. Distribution and release state

**CURRENT:** canonical BUILD-MAP reports:

- Phase 0 complete;
- Phase 1 complete;
- Phase 2 complete;
- Phase 3 complete;
- Phase 4 approximately 80 percent with 4.1 through 4.8 complete;
- Phase 5 not started;
- directional first-release progress roughly 95 percent.

**CURRENT:** Phase 4.9 compatibility/evaluation is the next canonical slice.

**CURRENT:** no latest GitHub Release was available through the repository release endpoint at audit time, and no tag namespace was returned.

**GAP:** there is not yet an immutable member release corresponding to the current architecture.

**GAP:** branch main is not protected at audit time.

Branch protection is a repository-governance concern rather than a coordination-runtime invariant, but it lowers release confidence.

---

## 27. Tests and CI

### Current verification

The Phase 4.8 PR head 3362541a46863dc801616a41810b888f8ceeb6f6 has CI run 480, run id 34721232595.

The test job reports:

- tests: 412;
- pass: 412;
- fail: 0;
- cancelled: 0;
- skipped: 0.

Current main merge commit:

    9874d413f5e23c9a869bf3ccead0f2751026a732

did not return a commit-associated workflow run or combined status at audit time.

This does not invalidate the green PR-head gate, but it must remain a separate fact.

### CI limitations

**GAP:** current CI is one Ubuntu/Node 22 job.

It does not directly prove:

- macOS;
- Windows;
- packaged clean install;
- current Brain lifecycle compatibility;
- current Data integration;
- authenticated remote Gateway;
- Dashboard/channel interoperability.

### Cross-repository acceptance history

**HISTORICAL:** a platform-wide smoke was merged and later explicitly reverted as out-of-scope.

Therefore current main should not be described as continuously proving all sibling repositories live together.

**INTENDED:** Phase 4.9 should own a durable compatibility/evaluation strategy that verifies current owner contracts without turning Multiple Bots CI into a brittle clone-and-audit of every sibling repository.

---

## 28. Documentation drift and contradictions

### Contradiction A - README progress

**CURRENT CODE/BUILD MAP:** Phase 3 is complete and Phase 4.8 is complete.

**STALE README:** still describes an older Phase 3 position and older next work.

**VERDICT:** BUILD-MAP and current implementation win.

### Contradiction B - SQLite ownership

**CURRENT CODE:** SQLite contains canonical coordination objects, ordered Events, deliveries and recovery state.

**STALE ARCHITECTURE PROSE:** describes runtime SQLite as derived/disposable.

**VERDICT:** executable store wins.

### Contradiction C - Brain registration

**CURRENT Multiple Bots:** Brain source requires AI-VERSE.yaml extensions.brain.

**CURRENT System Brain spec:** tracked Brain manifest registration is legacy; local extension registry is current.

**VERDICT:** integration contract is stale and requires repair.

### Contradiction D - Phase 3 status

PHASE-3-STATUS.md still ends by saying Phase 4 has not started, although current BUILD-MAP and Phase 4 status prove 4.8 complete.

**VERDICT:** historical/status tail is stale.

### Contradiction E - “complete” native integration

Phase 3 is complete against the contracts it implemented at the time.

It is not fully current-generation compatible because Brain lifecycle moved afterward and Data is absent.

**VERDICT:** label Phase 3 historical slice completion as CURRENT implementation evidence, but do not infer seamless current sibling compatibility from it.

---

## 29. Important historical repairs

### Early alternate hardening series

**HISTORICAL:** closed, unmerged PRs #1, #2, #4, #6, #8, #9, #10, #12, #13, #15, #16, #17, #19, #21, #22 and #24 explored stronger hardening.

Notable examples:

- explicit store migrations and read-only per-kind views;
- append-only event enforcement;
- hardened Bot registry contract;
- true end-to-end mailbox idempotency;
- delegation/handoff/Room safety hardening;
- safety substrate;
- Team Run/topology variants.

Some concepts were later reimplemented through the merged mainline sequence. Others, especially full direct-message idempotency and richer store migration history, are not equivalent on current main.

### Mainline maturation

**CURRENT/HISTORICAL LINEAGE:** merged PRs then built the present architecture through:

- Team Run/Worker lifecycle;
- Worker execution and manager topology;
- fan-out;
- handoff;
- discussion;
- disagreement;
- verifier;
- synthesis;
- cleanup;
- adaptive collaboration;
- aggregate budget/cancellation;
- OS native integration;
- Brain/Memory/Skills/Automations;
- owner write/candidate boundaries;
- Four Cs/lifecycle;
- A2A;
- Hermes/OpenClaw/Codex/Claude;
- external-managed runtime;
- remote identity/auth;
- remote leases;
- remote recovery.

---

## 30. Permanent laws established by repairs and current architecture

1. **LAW:** durable Bot identity and temporary Worker identity are different object classes.
2. **LAW:** Workers never become durable Bots automatically.
3. **LAW:** one work stage has one owner.
4. **LAW:** delegation and handoff have different ownership semantics.
5. **LAW:** child work cannot widen root constraints or authority.
6. **LAW:** collaboration does not pool credentials.
7. **LAW:** capability/environment authority is explicit, scoped and time-bounded.
8. **LAW:** remote authority can narrow local authority but never widen it.
9. **LAW:** uncertain side effects are not blindly replayed.
10. **LAW:** external runtime success is not canonical domain truth.
11. **LAW:** current context, Memory, Brain and Skills projections remain owner-controlled and ephemeral.
12. **LAW:** Multiple Bots does not become a scheduler.
13. **LAW:** package uninstall does not delete sibling/user canonical truth.
14. **LAW:** control-plane authentication must be distinct from protocol actor strings.
15. **LAW:** idempotency must cover the whole logical mutation.
16. **LAW:** current owner lifecycle contracts outrank stale copied integration parsers.
17. **LAW:** Data must be called through its owner boundary, not duplicated.
18. **LAW:** a coordination database containing unique protocol history/recovery is canonical package state and requires migration protection.
19. **LAW:** a compatibility claim must be verified against the current contract generation, not only historical fixtures.
20. **LAW:** UI/channels may observe/control but never become an alternate coordination source of truth.

---

## 31. Inspirations and curated references

### xAI Grok Bot

**INSPIRATION:** persistent named job-owning teammates, Rooms, asynchronous Bot messaging, approvals and attention-oriented UX.

Adopted conceptually, not as proprietary implementation.

### xAI Grok Multi-Agent

**INSPIRATION:** temporary parallel task-scoped specialists with one leader synthesis.

Adapted into dynamic Team Runs rather than fixed permanent swarms.

### Hermes Bot Mode

**INSPIRATION:** durable named profiles, direct chats, group behavior, mentions and cross-machine teammates.

### Microsoft Agent Framework

**INSPIRATION:** explicit orchestration topologies rather than one universal swarm loop.

### A2A 1.0

**INSPIRATION / CURRENT ADAPTER STANDARD:** external runtime discovery, Tasks, Messages, Artifacts, cancellation and extension mechanism.

### OpenAI Agents SDK

**INSPIRATION:** clear semantic distinction between manager delegation and handoff.

### OpenClaw

**INSPIRATION / CURRENT ADAPTER:** strict isolation lessons and runtime integration.

### AgentScope, Pydantic AI, Google ADK, LangGraph, CrewAI, Agno, CAMEL, MetaGPT and related systems

**INSPIRATION:** message hubs, typed delegation, transfer patterns, checkpointing, workflows and multi-agent failure lessons.

### Licensing law

**LAW:** research references inform architecture. Their implementation code is not silently absorbed into the core.

---

## 32. Current gaps and contradictions

### Severity: critical for seamless native integration

1. Repair Brain registration/enabled discovery to the current local extension-registry contract.
2. Define and implement the Data read/query and candidate/write boundary.
3. Complete Phase 4.9 compatibility/evaluation against current owner contracts.

### Severity: high for secure product exposure

4. Add authenticated control-plane identity before remote/network administrative exposure.
5. Replace operator_ string convention as the sole operator gate on network requests.
6. Add HTTP request body ceilings.
7. Repair complete direct-message idempotency.

### Severity: high for stable release

8. Add explicit durable coordination DB migrations/backup/recovery policy before schema evolution.
9. Finish package/install/onboarding/doctor/update/reinstall release path.
10. Add immutable release/tag.
11. Add clean-install acceptance.

### Severity: medium

12. Resolve README, Phase 3 status and architecture storage drift.
13. Expand platform CI beyond Ubuntu/Node 22 for claimed cross-platform support.
14. Define trusted policy for generic retry_safe classification.
15. Build Dashboard/channel contracts without bypassing Gateway authority.
16. Add production health aggregation.

---

## 33. Desired future state

**INTENDED:** Multiple Bots becomes a member-installable persistent teammate layer that:

- can be installed before or after AI-Verse OS;
- can run standalone under compatible hosts;
- can adopt existing external agents as managed teammates without duplicating their canonical domain state;
- automatically discovers current sibling integration contracts;
- uses Brain for strategic direction only when Brain owns the scope;
- uses Memory for history;
- uses Skills for reusable method;
- uses Data for structured data;
- receives cadence from the scheduler owner;
- preserves exact workspace isolation;
- exposes authenticated control and observation to Dashboard/channels;
- provides deterministic migration/update/uninstall behavior;
- resumes local and remote work safely;
- uses one final owner even during parallel intelligence;
- remains reusable by non-AI-Verse hosts.

---

## 34. Definition of done

### Current target definition of done

The repository’s current canonical next milestone is:

**Phase 4.9 - compatibility/evaluation suite.**

Phase 4.9 should not merely add more tests. To close the actual audit findings, its acceptance definition should include at minimum:

1. current-generation Brain attachment/enabled contract compatibility;
2. contract/evaluation fixtures for Memory and Skills current boundaries;
3. explicit Data contract decision and, if Data is part of current native completeness, supported adapter coverage;
4. A2A/Hermes/OpenClaw/Codex/Claude/external-managed conformance checks against the normalized runtime law;
5. local and remote authority non-expansion evaluation;
6. workspace-isolation evaluation across Bot-to-Bot, Room, Worker, handoff and runtime projections;
7. retry/idempotency evaluation including direct messages;
8. current lifecycle/registration contract compatibility;
9. explicit supported-platform matrix;
10. proof that standalone mode remains free of AI-Verse OS dependencies;
11. evaluation artifacts that can be rerun without checking out sibling source repositories as mutable implementation dependencies.

### First-release definition of done

The first finished release additionally requires Phase 5:

- clean machine install;
- standalone install;
- AI-Verse OS install;
- onboarding/setup;
- templates;
- production doctor;
- versioned upgrade/migration;
- secure remote Gateway;
- Dashboard/control endpoints;
- channel bridges;
- approvals/attention UX;
- observability/usage;
- release docs/examples;
- full release acceptance.

---

## 35. Contribution to the supreme AI-Verse vision

Multiple Bots contributes the social/organizational execution layer.

It turns:

- OS scope and authority;
- Brain direction;
- Memory history;
- Skills capability;
- Data facts;
- Connections access;
- Automations cadence;

into coordinated work by named durable teammates and temporary squads.

Its value depends on not absorbing those sibling responsibilities.

The best version of AI-Verse is not one giant omniscient agent. It is a set of canonical owners connected through explicit contracts, with Multiple Bots providing the collaboration fabric.

---

## 36. Open decisions

1. What exact Data query/write interface should Multiple Bots expose, and should Data be required in Phase 4.9 or deferred to a native-integration repair slice before Phase 5?
2. What authenticated principal model will the Gateway use for local desktop, remote Dashboard and channel clients?
3. Which operations are safe to expose to channel identities versus operator identities?
4. Should direct-message stable identity be client-supplied, deterministic from idempotency key, or owner-issued through a mutation envelope?
5. What schema migration framework becomes canonical for the coordination database?
6. Which platforms are release-supported for local process adapters?
7. How should external pre-existing Bot/team import map historical conversations without stealing Memory ownership?
8. What exact Phase 4.9 compatibility fixture/versioning contract prevents future sibling drift?
9. Should generic retry_safe be host-policy-only rather than client-declared?
10. Which component owns the final universal cadence execution runtime for proactive Bots?

---

## 37. Current intended milestone

**CURRENT canonical milestone:** Phase 4.9, compatibility/evaluation suite.

**Status at reviewed head:** NOT STARTED.

**Preceding slice:** Phase 4.8 is implemented and PR-head verified with 412/412 tests.

**Readiness verdict:** **NOT COMPLETE FOR CURRENT INTENDED MILESTONE.**

The repository is not blocked by lack of a coordination engine. It is blocked by the final interoperability/conformance gate plus concrete contract defects exposed by this audit.

---

## 38. Current-target readiness verdict

| Dimension | Verdict | Evidence / reason |
|---|---|---|
| Engine/core functionality | COMPLETE WITH LIMITATIONS | Phases 1-2 complete, 412-test suite; direct-message idempotency and schema migration gaps remain. |
| OS/host integration | PARTIAL | Phase 3 implemented, but Brain registration contract is stale and Data is absent. |
| Install/package path | PARTIAL | Development/source package works; Phase 5 public install not built. |
| Attach/register path | COMPLETE WITH LIMITATIONS | Safe local extension registration exists after materialization; final install orchestration is missing. |
| Activation/adoption path | PARTIAL | Bots/runtimes can be configured and external-managed profiles bound, but no universal existing-agent adoption flow. |
| Scope initialization | COMPLETE WITH LIMITATIONS | Workspace/Team Run scope enforcement is strong; network actor authentication is missing. |
| Legacy/history migration | PARTIAL | Coordination state is preserved, but durable DB schema migration and external-team import are incomplete. |
| Doctor/status/health | PARTIAL | Structural doctor + Four Cs evidence exist; no full production integration doctor. |
| Disable/detach/uninstall/reinstall | COMPLETE WITH LIMITATIONS | Extension uninstall/upgrade preserve state; final package reinstall/reconcile is not release-proven. |
| Cross-component acceptance | PARTIAL | Historical Phase 3 tests exist; current Brain contract drifts, Data absent, live platform smoke was reverted. |
| Member/public distribution | MISSING | Phase 5 not started; no immutable current release found. |

---

## 39. Command/lifecycle matrix

| Capability | Required now? | Current command/path | End-to-end proven? | Missing work |
|---|---|---|---|---|
| Install | Yes for first release, not complete for current engine milestone | source/npm development path | Partial | one-command clean install, immutable release |
| Attach/register | Yes | CLI os register / local extension registry | Yes for current registration contract | materialization/product wrapper |
| Activate/adopt | Yes for seamless system | Bot lifecycle/runtime config, external-managed binding | Partial | one adoption flow, authenticated principal, sibling discovery |
| Initialize | Yes | Gateway/store initialization | Engine yes | product setup and existing-state adoption |
| Migrate/import | Yes before stable state evolution | preservation only, no full DB migration framework | Partial | versioned DB migration, team import |
| Doctor/status | Yes | /health, store doctor, /v1/health/4cs | Partial | aggregate production doctor |
| Update | Yes before public stable release | Phase 3.10 extension upgrade | Partial | package release migration/rollback |
| Disable | Yes | Bot disable and extension enabled state | Partial | complete component/member UX |
| Detach/uninstall | Yes | Phase 3.10 extension uninstall | Yes for owned extension cleanup | package uninstall UX |
| Reinstall/reconcile | Yes for seamless system | preserved state + registration primitives | Partial | productized reconcile and health validation |

---

## 40. Exact missing work before seamless operation

The component cannot yet be described as “works perfectly together like a glove with the current AI-Verse system.”

The exact remaining work is:

1. **Repair current Brain integration.**
   - Stop requiring tracked AI-VERSE.yaml extensions.brain.
   - Resolve Brain attached/enabled/current-generation compatibility through the current OS/Brain local extension lifecycle.
   - Replace old fixtures with the clean current path.
   - Revalidate direction ownership and Brain installation as separate facts.

2. **Implement the Data boundary.**
   - Add a host-neutral structured-data query projection contract.
   - In AI-Verse mode, route through the OS/Data owner boundary.
   - Keep Task/principal/workspace authority exact.
   - Persist only bounded provenance/receipts.
   - Route candidate writes through owner-controlled canonical write handling.
   - Add absence/degraded behavior and tests.
   - Never open/copy Data canonical storage directly.

3. **Complete Phase 4.9.**
   - Build current-generation interoperability/conformance evaluation.
   - Include current native sibling contracts and all supported runtimes.
   - Prove no second OS/Brain/Memory/Data state.
   - Prove workspace isolation and authority non-expansion.
   - Prove standalone portability.

4. **Repair direct-message idempotency.**
   - Bind Message, delivery and Event to one stable mutation identity.
   - Return the original logical result on exact replay.
   - Fail on semantic drift under the same key.
   - Extend the same rule to Room/message convenience APIs where applicable.

5. **Harden the control plane before remote exposure.**
   - Authenticate callers.
   - Map authenticated principals to allowed protocol actor IDs.
   - Replace operator-prefix trust as network authorization.
   - Add endpoint authorization.
   - Add request body limits.
   - Keep loopback/trusted-host mode explicit.

6. **Protect durable coordination-state evolution.**
   - Introduce explicit schema migration history.
   - Add backup/recovery expectations.
   - Fail closed on newer unsupported DB schema.
   - Test upgrade from old persistent databases.

7. **Finish member product lifecycle in Phase 5.**
   - clean install;
   - standalone and OS setup;
   - onboarding and templates;
   - production doctor;
   - update/migration/rollback policy;
   - secure remote Gateway;
   - Dashboard/channels;
   - approvals/attention UX;
   - observability;
   - release docs/examples;
   - full acceptance.

8. **Finish release governance.**
   - cut immutable version/tag containing the documented current architecture;
   - verify that exact artifact;
   - consider branch protection/required CI for release branches;
   - expand OS/platform test matrix for claimed support.

9. **Repair documentation drift.**
   - README progress;
   - stale Phase 3 next-gate text;
   - obsolete disposable-SQLite description;
   - Brain ingress contract;
   - any future docs that equate historical slice completion with current sibling compatibility.

When these items are complete, Multiple Bots can legitimately serve as the persistent teammate and dynamic-squad layer without becoming a competing owner of the rest of AI-Verse.
