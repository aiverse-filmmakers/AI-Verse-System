# WSA-2026-038 Closure - Dashboard WebSocket Workspace Isolation

**Finding:** `WSA-2026-038`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Dashboard`  
**Repair wave:** R1.11  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

One Dashboard WebSocket could subscribe to workspace A and then subscribe to workspace B while the old A subscription remained live inside `SubscriptionHub`.

The socket's local `subId` variable was overwritten with the B subscription, but A's hub entry was never removed.

Therefore:

1. the socket subscribed to A;
2. it later subscribed to B;
3. the server created a second hub subscription;
4. A remained registered;
5. A events could still reach the socket after B became the apparent active workspace;
6. socket close removed only the newest subscription.

The subscribe control frame also bypassed the normal protocol workspace schema and registered workspace resolution.

Canonical contradiction: `C-A1.13-001`.

Required closure evidence:

- remove the previous workspace subscription before accepting a new successful scope, or track and clear every socket subscription;
- validate workspace IDs through protocol validation;
- validate the requested workspace through the registered system/workspace boundary;
- add deterministic A -> B -> A resubscribe coverage;
- prove no stale workspace events survive each switch;
- prove socket close releases all socket subscriptions.

## 2. Baseline and repair identity

**Pre-repair Dashboard ref:** `bf6a3a019b07b189c9c701f4edf01e0ded1e7a00`  
**Open Dashboard PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-038-websocket-workspace-isolation`  
**Repair PR:** `AI-Verse-Dashboard#11`  
**Final tested PR head:** `2e1926891c9b74274f89b7be807bce8902ce0853`  
**Merged Dashboard ref:** `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c`  
**Tested/merged product tree:** `8d0ee475e86b4fd963db8b4d013c7fe32e0fcb1a`

The exact tested PR head and merged `main` commit have the same product tree.

Open Dashboard PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Subscribe frames are protocol-validated

Dashboard protocol now exports a strict WebSocket subscription control schema:

- `type` must be exactly `subscribe`;
- `workspaceId` must satisfy the existing canonical `workspaceIdSchema`;
- extra fields are rejected by the strict schema.

Malformed or traversal-like workspace identifiers therefore fail before subscription state changes.

### 3.2 Workspace existence is resolved through the registered system boundary

Before replacing socket scope, the WebSocket handler calls the router's registered-workspace assertion.

That assertion resolves the requested `(systemId, workspaceId)` through the existing Dashboard registry/read-adapter boundary.

Therefore a syntactically valid but unregistered workspace cannot become a live subscription scope.

A rejected replacement request leaves the currently valid subscription unchanged.

### 3.3 Successful resubscribe replaces the previous scope

Each socket now tracks its active subscription ID.

For every valid replacement subscription:

1. validate the subscribe frame;
2. validate the workspace against the socket's already-bound system;
3. unsubscribe the current active hub subscription;
4. remove it from the socket subscription set;
5. create the new workspace subscription;
6. record the new subscription as the active one.

At most one successful workspace subscription is therefore active for the socket after each switch.

### 3.4 Socket close clears all tracked subscriptions

The socket also maintains a set of subscription IDs created for that socket.

On close, the server iterates the set and removes every tracked subscription from `SubscriptionHub`, then clears local subscription state.

This makes cleanup robust even if future changes introduce more than one tracked subscription.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/websocket-workspace-isolation.test.ts`

The regression proves:

1. socket subscribes to workspace A;
2. exactly one system subscription exists;
3. A event is received;
4. socket switches A -> B;
5. subscriber count remains exactly one;
6. an A event published after the B switch is not received;
7. the B event is received;
8. socket switches B -> A;
9. subscriber count remains exactly one;
10. a B event published after the A switch is not received;
11. the new A event is received;
12. protocol-invalid workspace `../escape` is rejected;
13. syntactically valid but unregistered workspace `ghost` is rejected;
14. rejected replacement attempts preserve the valid active A scope;
15. socket close reduces system subscriptions to zero;
16. total hub subscriber count is zero after close.

The test uses distinct event payload markers so hub deduplication cannot mask a stale-subscription leak.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Dashboard Actions run:

`37016702464`

On exact final head `2e1926891c9b74274f89b7be807bce8902ce0853`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative exact-head suite:

- tests: **68**
- suites: **15**
- passed: **67**
- failed: **0**
- skipped: **1**
- cancelled: **0**

The WSA-2026-038 resubscribe-isolation suite passed.

The one skipped test is pre-existing and unrelated to this repair.

### Post-merge acceptance

Post-merge Dashboard Actions run:

`37016845362`

On merged `main` ref `fe0119235df5227560b3a0ef9be8cf85d8aa1d4c`:

- Ubuntu / Node 22: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 22: **PASS**

Representative merged-main suite:

- tests: **68**
- suites: **15**
- passed: **67**
- failed: **0**
- skipped: **1**

The WSA-2026-038 resubscribe-isolation suite passed after merge.

## 6. Finding-specific recheck

### C-A1.13-001

**RESOLVED for WSA-2026-038.**

A successful workspace switch replaces the old hub scope rather than accumulating subscriptions.

### A -> B stale-event seam

**PASS.**

After B becomes active, an A event no longer reaches the socket.

### B -> A stale-event seam

**PASS.**

After switching back to A, a B event no longer reaches the socket.

### Protocol workspace validation seam

**PASS.**

Traversal-like workspace identifiers fail before subscription state mutation.

### Registered workspace resolution seam

**PASS.**

A valid-format but unknown workspace fails through the registered OS/workspace boundary.

### Rejected replacement seam

**PASS.**

An invalid replacement does not tear down or broaden the last valid subscription.

### Socket-close cleanup seam

**PASS.**

All tracked subscriptions are removed and the hub returns to zero subscribers.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-038`.

The following Dashboard findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-039` - registered systemId / filesystem-root identity binding;
- `WSA-2026-040` - local Dashboard Gateway read authentication;
- `WSA-2026-041` - loopback browser Origin handling with explicit ports;
- `WSA-2026-042` - synthetic owner-domain projection semantics.

MC1.4 remains paused behind the whole-system audit/repair gate.

No registered-root identity model, local authentication, Origin policy, synthetic read-model semantics, Mission Control release gate or unrelated Dashboard behavior was changed.

## 8. Closure verdict

Required WSA-2026-038 closure behavior is present on merged Dashboard `main`:

- subscribe frames use canonical workspace protocol validation;
- requested workspace scope is resolved through the registered system boundary;
- successful resubscribe removes the previous workspace subscription;
- A -> B -> A switching leaves exactly one active subscription;
- stale prior-workspace events do not cross each successful switch;
- rejected workspace switches preserve the current valid scope;
- socket close removes all tracked subscriptions;
- exact-head Ubuntu/macOS/Windows Node 22 CI passes;
- post-merge Ubuntu/macOS/Windows Node 22 CI passes;
- representative suites report 68 tests, 67 pass, 0 fail, 1 pre-existing skip;
- tested and merged product trees are identical;
- open Dashboard PRs are zero.

**WSA-2026-038: CLOSED.**
