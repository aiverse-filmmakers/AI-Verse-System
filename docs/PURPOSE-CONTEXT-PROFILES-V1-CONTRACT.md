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

The normal caller profile request is conceptually one of:

```text
auto | basic | rich
```

Operator scope resolves to `operator_default`; `basic`/`rich` workspace labels do not apply to `operator`.

### Workspace `auto` algorithm

For `workspace:<id>`, auto-detection is deterministic and conservative:

1. begin with `workspace_basic`;
2. inspect only already-authorized owner metadata/read capabilities for the exact workspace;
3. consider the current request/relevance need;
4. resolve to `workspace_rich` only when at least one rich-only information domain is both **owner-backed and relevant/requested**, such as:
   - an explicit strategic KPI definition with a valid current-truth binding;
   - owner-backed risks;
   - owner-backed narrative/context needed for the decision;
   - structured current-state evidence beyond the basic trajectory;
   - material-change evidence whose richer context is needed for the task;
5. otherwise remain `workspace_basic`.

### Insufficient signals

None of these is sufficient by itself to choose `workspace_rich`:

- workspace type being `product`, `business`, `client`, `team`, or similar;
- workspace name/title;
- free-text `purpose` description alone;
- number of files/messages;
- age of the workspace;
- perceived importance;
- model judgment that the workspace “looks corporate”;
- unused token budget.

Workspace type may help determine relevance after an owner-backed rich domain is present, but never creates that domain.

### Explicit caller profile

- `basic` forces the eligible read set to `workspace_basic`, while still preserving required truth-state/provenance diagnostics.
- `rich` permits the `workspace_rich` eligible read set, but still cannot fabricate unavailable fields or bypass owner scope/authority.
- `auto` uses the deterministic algorithm above.
- An unsupported profile token fails validation; it does not silently map to `auto`.

### Availability and failure behavior

- If rich evidence is not available, `auto` stays basic rather than probing unrelated/private storage.
- If the user's request specifically requires a rich domain (for example “how are our KPIs doing?”) and its declared owner read is unavailable, the projection reports that domain as unavailable/unknown under the envelope truth-state rules rather than downgrading the question into a misleading basic answer.
- Auto-detection never crosses into another workspace to find richer evidence.

### Determinism and provenance

The projection SHOULD expose non-authoritative profile diagnostics in provenance, equivalent to:

```yaml
profile:
  requested: auto
  resolved: workspace_basic | workspace_rich
  reasons:
    - <stable reason code>
```

Stable example reason codes include `operator_scope`, `workspace_default_basic`, `relevant_kpi_binding_present`, `relevant_risk_domain_present`, `relevant_rich_current_state_present`, and `explicit_profile_request`.

Given the same scope, caller profile request, relevance request, owner capability/results and contract version, profile resolution MUST be deterministic. Budget pruning may reduce emitted richness after selection, but it does not retroactively change the resolved profile.

### No persisted profile assumption yet

Task 4 does not assume a `WORKSPACE.yaml` profile setting exists. Task 5 separately decides whether such metadata is justified. Auto-detection must work without it.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [x] rich workspace optional fields
4. [x] auto-detection rules
5. [ ] `WORKSPACE.yaml` optional `purpose_context` decision
6. [ ] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
