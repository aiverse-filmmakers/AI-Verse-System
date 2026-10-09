# Purpose Context Strategic Mutation Confirmation

**Status:** Core admitted  
**Core release:** `core-purpose-context-public-beta-2026-10-09`  
**Qualified Purpose-aware Gateway runtime:** `1772b75e2add73a524715f746e87b3a6b5561bf6`

Purpose Context is read-only. It may help detect or explain a proposed strategic change, but it never becomes the authority that writes mission, goals, priorities, strategy, or other canonical direction state.

High-impact strategic changes continue through the existing canonical owner path and require explicit user confirmation before owner execution.

## Confirmation flow

The admitted flow is:

```text
strategic change intent
  -> bounded proposal
  -> read current direction owner
  -> route proposal to that exact owner
  -> explicit user confirmation of the exact proposal
  -> build canonical-owner operation
  -> canonical owner executes
  -> canonical owner receipt proves outcome
  -> rebuild Purpose from fresh owner state only after proven success
```

No step gives Purpose Context independent mutation authority.

## 1. Route to the current strategic owner

A strategic proposal is routed only after reading the current direction owner for the exact scope.

The owner status must:

- match the proposal scope;
- name exactly `os` or `brain`;
- preserve a consistent owner record when one is present.

The routed proposal records `target_owner` from that live owner read. Purpose/Gateway does not choose whichever owner is easier to write to, and a stale projection cannot silently reclaim authority.

## 2. Explicit confirmation binds to the exact proposal

Confirmation authority is exactly:

```text
explicit_user
```

The confirmation must bind to:

- the same scope;
- the same current target owner;
- the exact routed proposal fingerprint;
- the granting user;
- a valid confirmation timestamp.

The proposal fingerprint is a deterministic SHA-256 over the normalized routed proposal. If the proposal changes after confirmation, the fingerprint no longer matches and the confirmation cannot be reused.

This prevents a user confirmation for one strategic change from authorizing a different change.

## 3. Confirmation alone does not execute the mutation

A successfully confirmed envelope still reports that:

- a canonical owner operation is required;
- no owner operation has yet been built;
- apply is not yet allowed;
- no mutation has yet executed.

The system therefore distinguishes **user approval** from **canonical owner execution**.

## 4. Build the canonical-owner operation

Only a confirmed strategic proposal can become an owner operation.

The operation is semantically bound to:

- scope;
- target owner;
- change kind;
- operation kind;
- requested change;
- target surface;
- confirmed proposal fingerprint.

The owner operation receives deterministic operation and idempotency identifiers. Before dispatch it is explicitly receipt-free, unexecuted, and not allowed to trigger a Purpose rebuild.

## 5. Canonical owner receipt is the mutation evidence

Execution occurs only through the canonical owner boundary.

The returned owner receipt must match the exact operation, including:

- owner;
- scope;
- operation/request ID;
- idempotency key;
- operation fingerprint.

Receipt outcomes are bounded to:

- `succeeded`;
- `failed`;
- `uncertain`.

A successful effect is accepted only when the canonical owner returns a non-empty receipt ID and proves `effect_occurred=true`.

A failed effect must prove `effect_occurred=false`. If the effect cannot be proven either way, the result remains uncertain rather than being guessed.

## 6. Purpose rebuild occurs only after proven owner success

Purpose may rebuild only after a canonical owner receipt proves a successful effect.

If owner success is not proven:

- Purpose rebuild is skipped;
- no new Purpose projection is treated as evidence of mutation;
- the state remains failed or uncertain according to the owner receipt.

After proven success, the new Purpose projection must come from a fresh OS owner read for the same scope, remain within the runtime budget, and reject stale fallback.

The rebuilt Purpose view is still **not authoritative for the mutation**. The canonical owner receipt remains the mutation evidence.

## Safety invariants

The admitted mutation path guarantees:

- no silent strategic mutation;
- no confirmation without an exact current-owner-routed proposal;
- no reuse of confirmation for a changed proposal;
- no Purpose-owned write path;
- no owner-success claim without a matching canonical receipt;
- no post-write Purpose rebuild after failed/uncertain owner execution;
- no stale Purpose fallback after a successful strategic write;
- no change to workspace isolation or scope authority.

The operational rule is: **Purpose can explain and propose, the user confirms, the canonical owner writes, and only owner receipts prove that the strategic state changed.**
