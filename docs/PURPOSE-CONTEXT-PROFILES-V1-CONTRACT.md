# AI-Verse Purpose Context Profiles v1 Contract

**Status:** IN PROGRESS — Slice 2.3  
**Parent envelope:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Parent trajectory:** `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

Profiles control which already-valid Purpose sections are requested/emitted for a scope. They do not create new canonical truth, new scope types, or new storage.

---

## Task 1 — operator default shape — FROZEN

The default operator projection profile is conceptually `operator_default`.

When relevant owner-backed truth exists, it may include `problems`, `purpose`, `goals`, `priorities`, `challenges`, `strategies`, `initiatives`, `constraints`, `current_work`, `trajectory`, and `recent_material_changes`; `narratives`, `kpis`, `risks`, and `current_state` remain supporting/conditional.

Operator Purpose never implicitly aggregates all workspaces or their Data. A sparse operator projection is valid.

## Task 2 — workspace default/basic shape — FROZEN

The default workspace profile is conceptually `workspace_basic`.

When relevant owner-backed truth exists, it may include `purpose`, `goals`, `priorities`, `challenges`, `strategies`, `initiatives`, `constraints`, `current_work`, `trajectory`, `recent_material_changes`, plus `problems` when explicitly represented by the active strategic owner.

`narratives`, `kpis`, `risks`, and broader `current_state` remain conditional. Tiny workspaces do not require mission, strategy, KPIs, risk register, team structure, customer model, infrastructure model, or budget structure. Orphan work remains visible rather than being assigned invented hierarchy.

## Task 3 — rich workspace optional fields — FROZEN

The richer workspace profile is conceptually `workspace_rich`. It is an additive read profile over the same v1 envelope, not a different schema or corporate subsystem.

It may activate `narratives`, `kpis`, `risks`, richer `constraints`, richer `current_state`, richer `recent_material_changes`, and more secondary trajectory context when canonical owner evidence exists and budget permits.

KPI values require explicit Data/current-truth bindings. Risks require owner-backed records or frozen deterministic derivation. V1 does not silently add first-class top-level `team`, `resources`, `customers`, `infrastructure`, or `budget` fields; those require a legitimate existing v1 representation or later contract extension.

Selecting rich only broadens the eligible read set. It never requires every eligible section to appear.

## Task 4 — auto-detection rules — FROZEN

The normal caller profile request is `auto | basic | rich`. Operator resolves to `operator_default`. Workspace `auto` starts at `workspace_basic` and resolves rich only when at least one rich-only information domain is both owner-backed and relevant/requested. Workspace type/name/model judgment/unused budget alone are insufficient. Explicit basic/rich requests never bypass truth, scope, authority, or budget rules.

---

## Task 5 — `WORKSPACE.yaml` optional `purpose_context` decision — FROZEN

**Decision: Purpose Context v1 does not add a `purpose_context` block to `WORKSPACE.yaml`.**

Rationale:

- exact workspace scope plus existing owner APIs already provide sufficient discovery;
- `auto|basic|rich` is a request-time projection choice, not durable workspace truth;
- persisting a profile flag would create configuration users would have to maintain even though the projection can decide deterministically from current owner state and relevance;
- a durable `enabled` flag would risk making Purpose availability depend on stale workspace metadata rather than current runtime relevance;
- the Phase 1 audit found no owner field that must live in the manifest for v1.

Rules:

- existing `WORKSPACE.yaml` remains unchanged for Purpose v1;
- callers may request `auto|basic|rich` at read time;
- future manifest metadata requires a separately justified contract change and must remain configuration only, never strategic truth;
- implementations MUST NOT create hidden/default `purpose_context` metadata during workspace creation;
- no migration of existing workspaces is required for Purpose v1.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [x] rich workspace optional fields
4. [x] auto-detection rules
5. [x] `WORKSPACE.yaml` optional `purpose_context` decision
6. [ ] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
