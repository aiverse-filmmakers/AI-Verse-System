# WSA-2026-040 Closure - Dashboard Local Read Authentication

**Finding:** `WSA-2026-040`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Dashboard`  
**Repair wave:** R1.13  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

The Dashboard-local Gateway bound only to loopback, but it did not authenticate HTTP or WebSocket clients.

A local process could therefore connect without a credential, enumerate systems/workspaces and invoke read projections solely because it could reach the loopback port.

Origin checking existed for browser requests, but Origin is not an authentication credential and non-browser clients were intentionally allowed to omit it.

Canonical contradiction: `C-A1.13-003`.

Required closure evidence:

- require a local authenticated session/token or stronger OS-bound transport identity;
- do not treat Origin as authentication;
- preserve loopback-only binding;
- reject unauthenticated HTTP requests;
- reject unauthenticated WebSocket upgrades;
- add local unauthenticated-client negative tests;
- ensure current/future RPC command methods cannot inherit an unauthenticated transport path.

## 2. Baseline and repair identity

**Pre-repair Dashboard ref:** `c9e29ab660c7f56bea83dd00050a1342286734dc`  
**Open Dashboard PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-040-local-read-authentication`  
**Repair PR:** `AI-Verse-Dashboard#13`  
**Final tested PR head:** `91fcd67ab9e1ae0dfca1f7ffd73f196f5de632cc`  
**Merged Dashboard ref:** `359a19f683a15485299cb2bab4e844d8d05b4fd6`  
**Tested/merged product tree:** `f05af17ed355845468bfb9eabe2863f79fe8e878`

The exact tested PR head and merged `main` commit have the same product tree.

Open Dashboard PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Strong local session token

Each Dashboard-local Gateway now has one privileged local auth token.

By default the Gateway creates a fresh 32-byte cryptographically random token encoded as base64url.

A caller may supply an explicit token only when it satisfies the bounded local-token contract:

- base64url-safe characters only;
- minimum length 32;
- maximum length 256.

Weak configured tokens are rejected before the listener is bound.

The token is returned only to the local host code through the privileged `GatewayServer` object so trusted clients can be provisioned out of band.

### 3.2 HTTP is default-deny before routing

Every HTTP request is authenticated before route dispatch.

The accepted HTTP credential is:

`Authorization: Bearer <local-token>`

This applies to:

- `/health`;
- `/rpc`;
- unknown/future local routes.

Therefore a future route added below this transport gate inherits authentication by default rather than needing to remember to add it separately.

Unauthenticated and wrong-token requests receive:

- HTTP 401;
- `WWW-Authenticate: Bearer`;
- generic `UNAUTHENTICATED` error state;
- no token material in the response body.

### 3.3 Current and future RPC methods share the same authenticated edge

Authentication happens before request body parsing and before `QueryRouter.handle()`.

Therefore both read methods and command-shaped methods on `/rpc` require transport authentication first.

The permanent regression proves:

- unauthenticated `chat.send` receives HTTP 401 before command routing;
- authenticated `chat.send` reaches the existing read-only command gate and is rejected as `COMMAND_BLOCKED_READ_ONLY`.

This prevents a future command method from inheriting the original unauthenticated local transport gap.

### 3.4 WebSocket upgrade authentication

Every WebSocket upgrade is authenticated before:

- Origin processing;
- path routing;
- `systemId` validation;
- subscription/RPC frame handling.

Two local-client credential forms are accepted:

1. `Authorization: Bearer <local-token>` for native/non-browser clients;
2. a dedicated WebSocket subprotocol credential for browser-compatible clients.

Browser-style clients send:

- public protocol: `aiverse.dashboard.v1`;
- auth protocol: `aiverse.auth.<local-token>`.

The server validates the auth protocol but selects/echoes only the non-secret `aiverse.dashboard.v1` protocol.

The credential-bearing protocol is therefore not returned as the negotiated WebSocket protocol.

Unauthenticated and wrong-token WebSocket upgrades receive HTTP 401 before a socket session is created.

### 3.5 Origin remains a separate control

Authentication does not replace the existing Origin policy.

Permanent regressions prove both directions:

- a valid loopback Origin with no token still receives 401;
- a valid token with a non-loopback Origin still receives 403.

Therefore loopback Origin is not treated as identity or permission.

`WSA-2026-041`, which concerns safe support for approved loopback Origins with explicit ports, remains separate and OPEN.

### 3.6 Loopback-only binding is preserved

The existing server binding remains:

`127.0.0.1`

Explicit remote bind values remain rejected.

WSA-2026-040 therefore adds authentication without broadening network reachability.

### 3.7 Typed Dashboard client carries authentication

`DashboardClient` now requires a local auth token at construction.

Every query sends:

`Authorization: Bearer <token>`

The token is validated against the same shared protocol contract before use.

This keeps the supported typed client aligned with the authenticated server boundary.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/gateway-auth.test.ts`

The suite proves:

1. unauthenticated `/health` returns 401;
2. unauthenticated `/rpc` returns 401;
3. wrong bearer token returns 401;
4. loopback Origin alone does not authenticate;
5. unknown/future local route is also default-denied before routing;
6. unauthenticated command-shaped RPC is rejected before the router;
7. authenticated health succeeds;
8. authenticated system read succeeds;
9. authenticated unknown route reaches normal 404 only after authentication;
10. authenticated command-shaped RPC reaches the existing command gate;
11. valid token plus non-loopback Origin still fails Origin policy;
12. supported `DashboardClient` succeeds using its bearer token;
13. unauthenticated WebSocket upgrade is rejected with 401;
14. loopback Origin alone does not authenticate WebSocket;
15. wrong WebSocket auth protocol is rejected with 401;
16. browser-style subprotocol authentication succeeds;
17. only the non-secret Dashboard protocol is negotiated back;
18. native/non-browser bearer-authenticated WebSocket succeeds;
19. authenticated subscription state is released on close;
20. weak configured tokens fail before listener binding.

Existing gateway, Phase 1, live-activity and WebSocket-isolation tests were updated only to supply the newly required trusted local credential.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Dashboard Actions run:

`37029230010`

On exact final head `91fcd67ab9e1ae0dfca1f7ffd73f196f5de632cc`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative exact-head suite:

- tests: **76**
- suites: **17**
- passed: **75**
- failed: **0**
- skipped: **1**

The WSA-2026-040 authentication suite passed.

The one skipped test is pre-existing and unrelated.

Intermediate PR runs exposed only test-integration issues while migrating existing local clients to the newly mandatory credential:

- missing auth argument in a legacy typed-client test;
- unauthenticated legacy live-activity WebSocket test;
- cross-platform test cleanup timing after socket close.

Those were corrected before the final exact head. No accepted final-head authentication behavior relies on those failed intermediate runs.

### Post-merge acceptance

Post-merge Dashboard Actions run:

`37029380753`

On merged `main` ref `359a19f683a15485299cb2bab4e844d8d05b4fd6`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative merged-main suite:

- tests: **76**
- suites: **17**
- passed: **75**
- failed: **0**
- skipped: **1**

The WSA-2026-040 suite passed after merge.

## 6. Finding-specific recheck

### C-A1.13-003

**RESOLVED for WSA-2026-040.**

The Dashboard-local HTTP and WebSocket transport no longer grants OS-read access solely because a process can connect to loopback.

### Unauthenticated HTTP seam

**PASS.**

All HTTP routes are default-deny and return 401 without the local token.

### Wrong-token seam

**PASS.**

Invalid bearer credentials do not reach route or RPC handling.

### Origin-as-authentication seam

**PASS.**

Loopback Origin without the token receives 401.

### Authenticated non-loopback Origin seam

**PASS.**

A valid credential does not bypass the separate non-loopback Origin rejection.

### Unauthenticated WebSocket seam

**PASS.**

The server rejects the upgrade before system/subscription handling.

### Browser-compatible WebSocket auth seam

**PASS.**

Dedicated auth subprotocol credential is accepted while only the public Dashboard protocol is negotiated back.

### Native bearer WebSocket seam

**PASS.**

Authorized non-browser clients can authenticate through the standard Authorization header.

### Future route / command inheritance seam

**PASS.**

Authentication is above route and RPC-method dispatch, so current/future paths below that boundary inherit the credential requirement.

### Secret-response seam

**PASS.**

The token is not returned in unauthenticated HTTP errors, health responses or the selected WebSocket protocol.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-040`.

The following Dashboard findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-041` - safe loopback browser Origin policy with explicit ports;
- `WSA-2026-042` - synthetic owner-domain projection semantics.

Those findings belong to later ordered repair waves.

MC1.4 remains paused behind the whole-system audit/repair gate.

No loopback-port allowlist expansion, synthetic read-model semantics, Mission Control release gate or unrelated Dashboard behavior was changed.

## 8. Closure verdict

Required WSA-2026-040 closure behavior is present on merged Dashboard `main`:

- strong local token is required;
- every HTTP route is authenticated before dispatch;
- every WebSocket upgrade is authenticated before routing/system handling;
- Origin is preserved as a separate non-authentication control;
- loopback-only binding is preserved;
- current and future RPC methods sit behind the same authentication gate;
- supported typed Dashboard clients send bearer credentials automatically;
- browser-compatible WebSocket authentication is supported without echoing the auth credential as the selected protocol;
- unauthenticated/wrong-token negative tests pass;
- exact-head Ubuntu/macOS/Windows Node 22 CI passes;
- post-merge Ubuntu/macOS/Windows Node 22 CI passes;
- representative suites report 76 tests, 75 pass, 0 fail, 1 existing skip;
- tested and merged product trees are identical;
- open Dashboard PRs are zero.

**WSA-2026-040: CLOSED.**
