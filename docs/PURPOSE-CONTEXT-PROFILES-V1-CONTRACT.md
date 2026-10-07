# AI-Verse Purpose Context Profiles v1 Contract

**Status:** COMPLETE — Slice 2.3 contract frozen  
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

Purpose Context v1 adds no `purpose_context` block to `WORKSPACE.yaml`. Profile is request-time/deterministic; existing scope and owner APIs are sufficient; no workspace migration is required.

## Task 6 — disabled / irrelevant behavior — FROZEN

Irrelevant tasks perform zero Purpose reads. Explicit Purpose requests attempt the exact scope. Unavailable capability returns explicit unsupported/unavailable state and never fabricates content or falls back across workspace/owner boundaries.

---

## Task 7 — explicit cross-scope relationship rules — FROZEN

Purpose Context v1 is single-scope by default. A projection bound to `operator` or `workspace:<id>` MUST NOT enumerate, search, or merge other strategic scopes merely to complete a trajectory.

A cross-scope edge is authoritative only when **all** of the following are true:

1. the source-side canonical owner explicitly records a relationship to an exact canonical target ref;
2. the target ref includes its exact owner, scope, kind and id under the canonical ref contract;
3. existing owner/OS visibility and workspace-isolation rules authorize the caller to resolve the target;
4. the relation type and semantic source/target kinds are valid under the trajectory contract;
5. the target resolves exactly or may be represented as a safe validated identity stub;
6. the edge retains provenance proving the declared cross-scope relationship.

### Allowed direction

V1 permits both operator→workspace and workspace→operator relationships when explicitly owner-backed and authorized. Workspace→different-workspace relationships are also possible only when explicitly declared and authorized; they are never discovered by scanning neighboring workspaces.

Examples that may be valid:

- an operator-level goal explicitly serves a workspace initiative by canonical ref;
- a workspace initiative explicitly advances an operator-level goal;
- one workspace initiative explicitly depends on/serves a goal in another workspace when both scopes permit that relation.

The relation must still be one of the frozen v1 trajectory relation tokens. Cross-scope status does not create a new relation type.

### Projection behavior

- The bound scope remains the projection's authority/identity scope even when a visible cross-scope node is referenced.
- A cross-scope target does **not** authorize recursive loading of the target scope's complete Purpose projection.
- By default, materialize only the minimum target identity/provenance needed for the validated edge and explanation path.
- Deeper target detail requires a separate owner-authorized read and must remain bounded/relevant.
- Cross-scope traversal obeys the same cycle, missing-parent, budget, freshness, and deterministic-ordering rules as same-scope traversal.

### Privacy/fail-closed behavior

If the exact target cannot be read because it is hidden or unauthorized, classify the target/edge as forbidden under the trajectory contract. The current projection may state that an explicit relationship exists but cannot expose hidden target content unless even existence is sensitive under the owner boundary; it never leaks names, statements, or metadata from a forbidden scope.

Purpose MUST NOT:

- infer cross-scope relations from matching names/tags/text;
- aggregate all workspace goals under operator Purpose;
- import operator mission/goals into every workspace by default;
- treat Memory visibility overlays as strategic cross-scope authority;
- use Dashboard `systemId` or filesystem location as a cross-scope identity;
- follow a cross-scope edge into unrelated objects in the target scope without explicit refs.

### Cross-scope modification law

Purpose remains read-only. A future edit involving a cross-scope relation must route each durable mutation to the canonical owner of the object being changed and satisfy that scope's confirmation/authority rules. Merely seeing a cross-scope relation grants no mutation authority.

---

## Slice 2.3 final status

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [x] rich workspace optional fields
4. [x] auto-detection rules
5. [x] `WORKSPACE.yaml` optional `purpose_context` decision
6. [x] disabled/irrelevant behavior
7. [x] explicit cross-scope relationship rules

**Slice 2.3: COMPLETE / CONTRACT FROZEN.**

Acceptance verdict:

- tiny workspaces avoid fake corporate structure: PASS;
- rich workspaces can expose optional owner-backed domains without changing engine/schema: PASS;
- workspace isolation remains fail-closed: PASS;
- operator does not implicitly aggregate all workspaces: PASS;
- no manifest migration/config bloat is required for v1: PASS.

**Phase 2: COMPLETE / V1 CONTRACT FROZEN.**

**NEXT:** Phase 3 / Slice 3.1 / Task 1 — expose confirmed/current strategic objects through a Brain Purpose/strategy snapshot read surface.
