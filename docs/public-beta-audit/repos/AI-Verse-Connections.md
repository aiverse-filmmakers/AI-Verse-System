# A1.10 - Independent Repository Audit: AI-Verse-Connections

**Audit date:** 2026-09-15  
**Frozen ref:** `baaac641558dbff1c2eabb0b5ec785a633f49a5b`  
**System baseline:** `208de1e80fd200820e41df9dc8d6e295111c1494`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-029` through `WSA-2026-033`  
**Inherited evidence limitation:** `WSA-2026-003`  
**Next:** A1.11 AI-Verse-Apps

## Independence and drift control

A1.10 used only the frozen Connections repository, its executable code, repository-local tests, package/component metadata, repository history and GitHub repository/workflow metadata.

At task start and pre-write recheck:

- Connections main remained exactly `baaac641558dbff1c2eabb0b5ec785a633f49a5b`;
- System main remained `208de1e80fd200820e41df9dc8d6e295111c1494`;
- no open scoped PR existed;
- no Connections product file was modified;
- Dashboard MC1.4 remained paused.

The frozen repository tree contains **36 tracked entries**.

## Reconstructed ownership

AI-Verse Connections is the canonical external-connection control plane and final provider edge.

It owns:

- connection identity/configuration;
- connection system/workspace scope;
- opaque credential handles;
- encrypted local vault state and environment-backed handles;
- provider adapters;
- live verification;
- connection authorization/health/revocation state;
- discovered MCP catalog evidence;
- explicit capability admission;
- connection approval;
- external execution receipts;
- idempotency reservations;
- rate/call budgets;
- final provider-edge enforcement.

It does not claim ownership of:

- Brain goals or strategy;
- Memory;
- Skills;
- scheduler/Automations truth;
- Gateway session/run state;
- Dashboard state;
- OS global policy;
- canonical local copies of third-party SaaS data.

External provider data remains externally canonical and every result is labeled `untrusted_external`.

## Credential model

The canonical registry stores opaque handles only, including:

- `env:NAME`;
- `vault:id`;
- `none`.

The local vault uses:

- AES-256-GCM;
- scrypt-derived 32-byte key;
- random salt;
- random IV;
- authentication tag.

The master key comes from `AIVERSE_CONNECTIONS_MASTER_KEY` and is not stored by Connections.

Secrets are resolved only inside trusted provider adapters immediately before request construction.

Ordinary list/receipt paths do not intentionally include secret values.

Generic API callers cannot inject Authorization, Cookie, X-API-Key or hop-by-hop transport headers.

MCP bearer credentials are injected only by the adapter.

## Connection-state separation

A connection intentionally separates:

- configured;
- liveVerified;
- healthy;
- authorized;
- approved.

Registration is not authorization.

Verification is not admission.

Admission is not connection approval.

Approval is not a permanent final-edge bypass.

Revocation and re-auth clear current execution authority.

## Generic API provider

Generic API connections define:

- exact base URL;
- origin;
- allowed methods;
- allowed path prefixes;
- read-only health method/path;
- credential mode;
- call/size/time budgets;
- optional explicit private-network permission.

Execution:

- validates the method;
- validates a requested path prefix;
- builds a target URL;
- requires the target origin to match;
- adds trusted credential headers;
- disables redirects;
- bounds request/response size;
- applies timeout;
- labels external response untrusted.

The path authorization order contains a HIGH bypass under `WSA-2026-033`.

## MCP provider

Frozen Connections targets stateless HTTP MCP `2026-07-28`.

Verification performs:

- `server/discover`;
- advertised protocol-version check;
- `tools/list`;
- optional `resources/list`;
- bounded pagination;
- tool/resource fingerprinting;
- self-reported server identity capture separate from security origin;
- prompt-injection/tool-poisoning signal detection.

New MCP tools are not admitted automatically.

Tool/schema changes:

- clear the changed capability admission;
- set review required;
- revoke connection approval.

MCP execution requires an admitted capability and sends the specific tool name at the provider edge.

## Network boundary

By default Connections requires HTTPS and blocks private/reserved/local targets.

Before a request it resolves DNS and rejects discovered private/reserved addresses unless explicit private-network access is enabled.

Provider requests:

- remain on the registered origin;
- disable redirects;
- have bounded body/response size and timeout.

The DNS check and actual fetch are separate name resolutions rather than one pinned address. Because the repository wording says DNS resolution reduces rebinding exposure rather than claiming a complete anti-rebinding guarantee, A1.10 records this as an adversarial A4 follow-up rather than opening a separate standalone finding here.

## Capability and approval model

Each admitted capability records:

- AI-Verse capability name;
- provider source kind/name;
- admission state;
- review-required state;
- risk class;
- source fingerprint.

Connection approval fingerprints the currently admitted reviewed capability set.

Write/admin risk additionally requires explicit per-action approval at execution.

The service API receives delegated capability and per-action approval evidence from its caller. This repo does not authenticate that upstream caller itself.

A1.10 therefore records trusted delegated-grant and approval provenance as inbound seam claims for A2 rather than assuming sibling enforcement.

## Final-edge execution path

The documented final-edge law says current authority must be the intersection of:

- component ready state;
- connection enabled state;
- system scope;
- workspace scope;
- live authorization/health;
- admitted capability;
- delegated capability;
- per-action approval;
- rate/call budgets;
- current revocation state.

Connections correctly reloads the connection immediately before provider execution and re-runs connection/capability checks.

However, it does not recalculate the complete documented intersection. Component lifecycle and rate budgets are not re-read at the final edge. See `WSA-2026-032`.

## Idempotency and receipts

When supplied, an idempotency key creates an append-only `pending` reservation before the provider request.

A concurrent duplicate with the same connection/capability/key is blocked.

Successful and provider-error terminal receipts are replayed rather than externally re-executed.

A terminal local failure under the same key blocks automatic reuse.

One conservative limitation remains: a process crash or pre-provider exception after a pending reservation can leave the key pending indefinitely because no pending-reservation recovery protocol exists. Since this fails closed and cannot itself repeat an external side effect, A1.10 records it as a recovery limitation rather than a standalone public-beta safety finding.

## System/workspace scope

Connection policy correctly checks:

- request system ID equals the connection system ID;
- workspace is in the connection allowlist when that allowlist is non-empty.

But the **installation-level system binding** created by setup is not enforced when connection records are created or executed. See `WSA-2026-030`.

## C-A1.10-001 - destructive purge trusts an arbitrary configured Connections home

**Source A:** public lifecycle exposes explicit destructive `uninstall --purge`.

**Source B:** default home can be replaced directly by `AIVERSE_CONNECTIONS_HOME`; the programmatic service constructor also accepts an arbitrary home path.

**Source C:** purge executes recursive forced removal of the complete home path.

**Source D:** no ownership marker, expected directory identity, safe-root check, broad-directory refusal or bounded known-child deletion is required before removal.

**Higher-authority source:** executable lifecycle/state-store implementation.

**Finding:** `WSA-2026-029`.

## WSA-2026-029 - Connections purge can recursively delete an unrelated configured directory

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** destructive lifecycle / filesystem containment  
**Affected repo:** `AI-Verse-Connections`

### Summary

`uninstall({ purge: true })` calls the state store's `purgeAll()`.

`purgeAll()` performs recursive forced deletion of `this.home`.

`this.home` can come from the `AIVERSE_CONNECTIONS_HOME` environment variable or the public `ConnectionsService({home})` constructor.

No Connections ownership proof is required.

### Impact

A typo, unsafe environment value or automated lifecycle invocation can delete unrelated user data under a broad custom home directory.

This is a proven destructive data-loss path and therefore a dogfood BLOCKER.

### Required closure evidence

After repair authorization:

- create a durable Connections ownership marker;
- validate the realpath before any destructive removal;
- refuse filesystem roots, user home, broad system/user directories, foreign directories and missing/wrong ownership markers;
- prefer deletion of known Connections-owned children;
- add negative purge tests for unrelated directory, broad path, missing marker, wrong marker and safe custom owned path.

## C-A1.10-002 - installation system binding is not part of connection registration/execution authority

**Source A:** README/component contract says setup binds the installation to an explicit AI-Verse system scope.

**Source B:** lifecycle setup stores `lifecycle.systemId`.

**Source C:** `addGeneric`/`addMcp` accept any caller-supplied connection `systemId`; `baseConnection` only checks that it is non-empty.

**Source D:** execution checks the request against the connection's system ID but does not require either to match lifecycle `systemId`.

**Higher-authority source:** executable lifecycle, registry and execution policy.

**Finding:** `WSA-2026-030`.

## WSA-2026-030 - Connections setup system scope is not enforced by canonical connection or execution state

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** system scope isolation / canonical installation binding  
**Affected repo:** `AI-Verse-Connections`

### Summary

A Connections state boundary can be set up for `sys-a` and then register a connection whose own system ID is `sys-b`.

Execution succeeds when the caller supplies `sys-b`, because the policy compares only request -> connection and ignores installation lifecycle scope.

Repeated setup can also replace the lifecycle system ID without reconciling existing connection system IDs.

### Impact

One canonical Connections home can silently contain and execute external authority for systems other than the system to which setup claims the installation is bound.

That weakens system isolation and makes lifecycle scope non-authoritative.

### Required closure evidence

After repair authorization:

- enforce exact lifecycle-system binding at connection creation;
- re-check lifecycle system ID at the provider edge;
- reject setup rebind while foreign-scoped connections exist unless an explicit migration/rebind workflow is used;
- add two-system negative tests for add/verify/admit/approve/execute and setup rebind.

## C-A1.10-003 - MCP credential-origin reuse guard exists on add but not on reauth

**Source A:** research/security law says bearer tokens are resource/origin scoped and token passthrough is forbidden.

**Source B:** `addMcp` scans existing MCP records and rejects one credential handle reused across different MCP origins.

**Source C:** `reauth` simply replaces `credentialHandle` and clears status, without applying the same cross-origin uniqueness rule.

**Source D:** next `verify` resolves that handle and sends it as a bearer token to the connection's registered MCP origin.

**Higher-authority source:** executable registry/admission/MCP adapter.

**Finding:** `WSA-2026-031`.

## WSA-2026-031 - MCP re-authentication can bypass the cross-origin bearer credential isolation rule

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** credential origin binding / token passthrough prevention  
**Affected repo:** `AI-Verse-Connections`

### Summary

Initial MCP registration correctly prevents one credential handle from being reused across different server origins.

Reauth does not.

An existing connection for origin B can be reauthenticated with a handle already used by origin A.

Although approval is cleared, verification of B sends that bearer credential to B before approval can be restored.

### Impact

A credential intended for one MCP security origin can be disclosed to another origin through a supported Connections lifecycle path, violating the repository's explicit anti-token-passthrough rule.

### Required closure evidence

After repair authorization:

- centralize credential-origin binding validation and apply it to add, reauth and verification;
- make verification fail before credential resolution/transmission when binding conflicts;
- add two-origin tests proving add and reauth both reject handle reuse and same-origin rotation remains supported.

## C-A1.10-004 - final-edge implementation does not recompute documented lifecycle and budget authority

**Source A:** security contract says the full authority intersection includes component enabled/setup state and current rate/budget limits and is recalculated immediately before provider execution.

**Source B:** execute checks lifecycle once at function entry.

**Source C:** execute checks usage budget once before idempotency reservation.

**Source D:** after the explicit `beforeFinalEdge` boundary, execution reloads only the connection and re-runs connection/capability policy before adapter execution.

**Source E:** different idempotency keys do not serialize the budget check, so concurrent calls can independently observe the same remaining budget.

**Higher-authority source:** executable execution/policy implementation.

**Finding:** `WSA-2026-032`.

## WSA-2026-032 - final provider edge omits component lifecycle and current budget rechecks

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** final-edge authority / concurrency / safety budgets  
**Affected repo:** `AI-Verse-Connections`

### Summary

Connection-level revocation and narrowing are reloaded at the final provider edge.

Component lifecycle and usage budgets are not.

Therefore:

- a concurrent component disable/uninstall after initial planning does not itself fence the already-planned call;
- concurrent executions with distinct idempotency keys can both pass the same rate/day budget before either has recorded an attempted external call;
- the final provider-edge check does not correct either condition.

### Impact

External effects can occur after a current component-level authority fence or beyond configured execution budgets.

This is especially material for write/admin capabilities, even though per-action approval and connection-level authority remain separately enforced.

### Required closure evidence

After repair authorization:

- re-read lifecycle state immediately before adapter execution;
- make the budget reservation/check atomic across concurrent executions;
- count provider-edge reservations in the budget;
- release/terminalize reservations consistently;
- add deterministic races for disable/uninstall and maxCallsPerMinute/maxCallsPerDay.

## C-A1.10-005 - generic path policy checks raw path before URL normalization

**Source A:** Generic API policy claims explicit path-prefix allowlists bound external authority.

**Source B:** `buildRequest` checks the raw caller path with string prefix logic before constructing the WHATWG URL.

**Source C:** WHATWG URL construction normalizes dot-segments, including percent-encoded dot-segments.

**Source D:** after URL construction, implementation re-checks only origin, not normalized pathname against the admitted prefixes.

**Executable reproduction:** with allowed prefix `/v1`, raw path `/v1/%2e%2e/admin` passes the raw prefix condition while Node URL normalization produces pathname `/admin`.

**Finding:** `WSA-2026-033`.

## WSA-2026-033 - Generic API encoded dot-segments can escape the admitted path prefix

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** external path authorization / provider-edge containment  
**Affected repo:** `AI-Verse-Connections`

### Summary

Generic API path permission is applied before canonical URL normalization.

For example, with admitted prefix:

`/v1`

the caller path:

`/v1/%2e%2e/admin`

passes the raw `/v1/` prefix test.

Node's URL parser normalizes it to:

`/admin`

The request remains on the same origin, so the later origin check passes and the trusted adapter adds the connection credential.

### Impact

A caller can reach an endpoint on the registered service origin that is outside the explicitly admitted path prefix.

This can expose broader API authority than the operator intended and can carry the trusted credential to that unintended path.

### Required closure evidence

After repair authorization:

- construct/canonicalize the URL before authorization;
- validate the normalized pathname against canonical normalized admitted prefixes;
- reject dot-segment and encoded path-confusion forms;
- cover percent-encoded dot segments, mixed-case encodings, plain `..`, encoded separators and query-only variations;
- verify the final outbound pathname is still admitted immediately before fetch.

## Lifecycle and state behavior

Non-purge uninstall preserves canonical state by marking lifecycle installed/setup/enabled false.

Disable also preserves registry/vault/receipts.

Update correctly declares software replacement as externally managed by Distribution and does not silently migrate state.

A1.10 does not independently prove Distribution's side.

State files are JSON/NDJSON rather than an identity-bearing database.

Schema-version and structural validation are comparatively weak, but the material destructive risk is already captured by `WSA-2026-029`; no additional standalone finding is opened for malformed/foreign JSON adoption in A1.10.

## Exact-head hosted CI

Frozen head:

`baaac641558dbff1c2eabb0b5ec785a633f49a5b`

GitHub Actions run:

`34775251071` - repository run conclusion **FAILURE**

All six matrix jobs terminated before workflow step execution:

- Windows Node 22: `103772074523` - `steps: null`
- Ubuntu Node 22: `103772074622` - `steps: null`
- macOS Node 20: `103772074628` - `steps: null`
- Ubuntu Node 20: `103772074631` - `steps: null`
- Windows Node 20: `103772074634` - `steps: null`
- macOS Node 22: `103772074694` - `steps: null`

No checkout, install, syntax check or test step executed.

This is the exact condition already registered as `WSA-2026-003`.

A1.10 does **not** classify the run as a product test failure and does not open a duplicate CI finding.

Repository-local integration tests cover:

- lifecycle state preservation;
- encrypted vault handles/no raw-secret persistence;
- system/workspace/final connection revocation checks;
- sequential rate budgets;
- private-network default denial;
- concurrent same-key idempotency;
- MCP discovery/admission/schema-change re-review;
- untrusted result labeling.

Those tests are useful executable specifications, but current GitHub-hosted evidence does not prove they executed at the frozen head.

## Release/current-history evidence

Frozen current head is the implementation commit:

`baaac641558dbff1c2eabb0b5ec785a633f49a5b`

Its parent is the founding architecture/research commit:

`76be3558eb6670b21195064b04acdd7d6dd41490`

Package and component metadata agree on:

`0.1.0-beta.1`

The repository explicitly calls this a public-beta candidate.

A1.10 does not use missing hosted release/tag evidence as a standalone defect; immutable release qualification belongs to A5.

The pre-existing System documentation drift for Connections remains `WSA-2026-002` and is not duplicated here.

## Negative-space checks

A1.10 found no evidence that Connections:

- stores raw vault secrets in the canonical registry;
- intentionally writes raw secrets to execution receipts;
- accepts caller-injected Authorization/Cookie/API-key transport headers;
- auto-admits newly discovered MCP tools;
- treats self-reported MCP server identity as the registered security origin;
- silently preserves approval after MCP descriptor/schema drift;
- follows HTTP redirects;
- intentionally lets external results become local canonical Data;
- treats external content as trusted;
- silently broadens workspace allowlists during execution;
- ignores connection-level revoke at the final edge;
- silently executes a write/admin capability without the request's explicit approval flag;
- replays a completed same-key provider side effect;
- purges canonical state during ordinary non-destructive uninstall.

## Evidence limitations / downstream claims

A1.10 does not independently validate sibling implementations.

Claims carried into A2 include:

- upstream callers supply trustworthy delegated capability leases;
- upstream callers supply trustworthy per-action approval provenance;
- Distribution owns software update/replacement;
- OS/Gateway/Bots must not bypass Connections for external credentials/effects;
- external provider data remains externally canonical unless Data owns a separate sync contract.

Claims carried into A4 include:

- DNS check and fetch use separate resolution operations and should receive an explicit DNS-rebinding adversarial test;
- pending idempotency reservations have no crash recovery and should be tested for operator recoverability.

Because hosted current-head CI never executed, A5 must not treat run `34775251071` as acceptance evidence.

## Evidence IDs

- `E-A1.10-001` frozen Connections tree/repository metadata.
- `E-A1.10-002` README/component/package ownership identity.
- `E-A1.10-003` security/research trust and final-edge laws.
- `E-A1.10-004` credential manager/vault implementation.
- `E-A1.10-005` canonical state-store/lifecycle implementation.
- `E-A1.10-006` generic connection registration/verification.
- `E-A1.10-007` MCP registration/origin credential reuse guard.
- `E-A1.10-008` capability admission/connection approval.
- `E-A1.10-009` revoke/reauth implementation.
- `E-A1.10-010` system/workspace/delegated policy implementation.
- `E-A1.10-011` final-edge execution/idempotency/receipt implementation.
- `E-A1.10-012` rate/call budget implementation.
- `E-A1.10-013` generic API request/path/header policy.
- `E-A1.10-014` MCP discovery/execution adapter.
- `E-A1.10-015` bounded HTTP/network controls.
- `E-A1.10-016` repository-local core integration tests.
- `E-A1.10-017` repository-local limits integration tests.
- `E-A1.10-018` repository-local MCP/idempotency integration tests.
- `E-A1.10-019` Node WHATWG URL normalization reproduction for encoded dot segments.
- `E-A1.10-020` exact-head CI run `34775251071`.
- `E-A1.10-021` six exact-head no-step hosted jobs.
- `E-A1.10-022` frozen implementation/founding commit history.
- `E-A1.10-023` live pre-write ref/open-PR recheck.

## Verdict and progress

**AI-Verse-Connections at `baaac641558dbff1c2eabb0b5ec785a633f49a5b`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

New findings:

1. `WSA-2026-029` BLOCKER - arbitrary configured home can be recursively purged.
2. `WSA-2026-030` HIGH - setup system binding is not enforced by canonical connection/execution state.
3. `WSA-2026-031` HIGH - MCP reauth bypasses cross-origin bearer-handle isolation.
4. `WSA-2026-032` HIGH - final-edge lifecycle and budget authority are not fully rechecked.
5. `WSA-2026-033` HIGH - Generic API normalized path can escape admitted prefix.

Inherited:

- `WSA-2026-002` System Connections documentation drift.
- `WSA-2026-003` hosted CI/evidence availability.

No Connections product repair is made during A1.10.

After acceptance:

- weighted audit: **25 / 100 = 25%**
- remaining: **75%**
- tasks: **15 / 51 complete**
- tasks remaining: **36 / 51**
- phases fully complete: **1 / 7**
- phases incomplete: **6 / 7**
- A1 repositories: **10 / 14 complete**
- A1 repositories remaining: **4 / 14**
- A1 weight: **20 / 28**
- next task: **A1.11 AI-Verse-Apps**
