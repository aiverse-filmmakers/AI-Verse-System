# AI-Verse Purpose Context Profiles v1 Contract

**Status:** IN PROGRESS — Slice 2.3  
**Parent envelope:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Parent trajectory:** `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

Profiles control which already-valid Purpose sections are requested/emitted for a scope. They do not create new canonical truth, new scope types, or new storage.

## Task 1 — operator default shape — FROZEN

`operator_default` is sparse/global and never implicitly aggregates all workspaces or their Data.

## Task 2 — workspace default/basic shape — FROZEN

`workspace_basic` exposes only relevant owner-backed strategic/current-work trajectory and never forces corporate bureaucracy.

## Task 3 — rich workspace optional fields — FROZEN

`workspace_rich` is an additive read profile over the same v1 envelope. It broadens eligible owner-backed reads but never requires fields to exist or creates new top-level corporate truth.

## Task 4 — auto-detection rules — FROZEN

The normal caller profile request is `auto | basic | rich`. Workspace `auto` begins basic and becomes rich only when a rich-only domain is both owner-backed and relevant/requested. Type/name/model judgment/unused budget are insufficient.

## Task 5 — `WORKSPACE.yaml` optional `purpose_context` decision — FROZEN

**Decision: Purpose Context v1 does not add a `purpose_context` block to `WORKSPACE.yaml`.** Profile is request-time/deterministic; existing scope and owner APIs are sufficient; no workspace migration is required.

---

## Task 6 — disabled / irrelevant behavior — FROZEN

Purpose Context v1 distinguishes **feature unavailable/disabled** from **feature irrelevant to the current task**.

### Irrelevant task

When runtime relevance classification determines that Purpose Context is not needed:

- the runtime MUST perform **zero Purpose owner reads** for that turn/run;
- no Purpose projection is assembled;
- no placeholder/empty Purpose object is injected;
- the agent proceeds with its normal existing context path;
- diagnostics may record a bounded non-content reason such as `purpose_skipped_irrelevant`;
- skipping Purpose must not reduce permissions, mutate state, or alter canonical owner truth.

Examples include bounded file renames, simple formatting, or other tasks whose answer does not depend on strategic direction.

### Explicit Purpose request

A direct user request such as “why are we doing this?”, “what should we do next?”, “how does this serve the goal?”, or an explicit Purpose/Dashboard read overrides normal relevance skipping and attempts the exact-scope Purpose read.

### Disabled / unavailable capability

V1 has no per-workspace manifest disable flag. Capability may still be unavailable because the installed OS/runtime version does not provide Purpose, the component is disabled at a higher existing lifecycle boundary, or a required owner/API is unavailable.

In those cases:

- runtime MUST NOT fabricate Purpose content;
- existing non-Purpose functionality continues where safe;
- explicit Purpose requests return an explicit unsupported/unavailable result rather than silently pretending Purpose is empty;
- owner unavailability does not trigger cross-workspace fallback, stale-strategy resurrection, or Memory-as-current fallback;
- failure to load an optional owner may yield a partial projection only under the envelope truth-state rules;
- failure of the required scope/identity/active strategic-owner boundary fails the Purpose read closed.

### Anti-bloat law

Purpose relevance is a read gate, not a prompt decoration. Trivial/unrelated tasks must demonstrate zero Purpose reads in Phase 7 acceptance tests. A caller cannot force Purpose to load globally merely by leaving spare context budget.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [x] rich workspace optional fields
4. [x] auto-detection rules
5. [x] `WORKSPACE.yaml` optional `purpose_context` decision
6. [x] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
