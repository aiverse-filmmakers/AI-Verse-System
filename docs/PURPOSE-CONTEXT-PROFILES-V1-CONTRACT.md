# AI-Verse Purpose Context Profiles v1 Contract

**Status:** IN PROGRESS — Slice 2.3  
**Parent envelope:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Parent trajectory:** `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

Profiles control which already-valid Purpose sections are requested/emitted for a scope. They do not create new canonical truth, new scope types, or new storage.

---

## Task 1 — operator default shape — FROZEN

The default operator projection profile is conceptually `operator_default`.

Required shell:

```yaml
schema_version: "1.0"
scope: operator
scope_kind: operator
identity:
  kind: operator
  id: operator
provenance: {...}
```

When relevant owner-backed truth exists, the default operator profile may include `problems`, `purpose`, `goals`, `priorities`, `challenges`, `strategies`, `initiatives`, `constraints`, `current_work`, `trajectory`, and `recent_material_changes`. `narratives`, `kpis`, `risks`, and `current_state` remain supporting/conditional.

Operator Purpose never implicitly aggregates all workspaces or their Data. A sparse operator projection is valid; no missing strategic section is fabricated merely to make the profile look complete.

---

## Task 2 — workspace default/basic shape — FROZEN

The default workspace profile is conceptually `workspace_basic` and is the safe starting profile for every `workspace:<id>` unless Task 4 auto-detection explicitly selects a richer read.

Required shell:

```yaml
schema_version: "1.0"
scope: workspace:<id>
scope_kind: workspace
identity:
  kind: workspace
  id: <id>
  name: <owner-backed when available>
  type: <owner-backed when available>
provenance: {...}
```

### Basic semantic retrieval set

When relevant owner-backed truth exists, `workspace_basic` may include:

- `purpose`
- `goals`
- `priorities`
- `challenges`
- `strategies`
- `initiatives`
- `constraints`
- `current_work`
- `trajectory`
- `recent_material_changes`

`problems` may also appear when the active strategic owner explicitly represents the problem the workspace exists to address.

The following are not part of the expected basic shape and stay conditional:

- `narratives`
- `kpis`
- `risks`
- broader structured `current_state`

### Basic-workspace laws

- A tiny workspace may legitimately contain only identity plus `current_work`, one initiative, one goal, or no strategic objects yet.
- Basic profile does not require mission, strategy, KPI, risk register, team structure, customer model, infrastructure model, or budget fields.
- An orphan initiative/current-work item remains visible under the trajectory orphan rules; Purpose does not invent hierarchy to make the workspace look mature.
- Workspace Purpose reads only the exact bound workspace plus owner APIs that are already authorized to expose operator historical context; such Memory visibility does not import operator strategic mission/goals into the workspace.
- `workspace_basic` never scans neighboring workspaces for “related” goals, Data or history.
- Workspace identity/type is descriptive metadata and does not itself create strategic content.

### Product goal

A new/simple workspace should receive useful trajectory context without feeling like enterprise project-management software. The profile should answer, when evidence exists:

> What is this workspace trying to achieve, what is happening now, what is blocking it, and how does the current work connect upward?

without requiring corporate-style fields that the workspace does not naturally own.

### Budget law

The normal v1 bounded-output contract applies. Basic profile receives no special right to fill unused bytes with irrelevant sections.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [ ] rich workspace optional fields
4. [ ] auto-detection rules
5. [ ] `WORKSPACE.yaml` optional `purpose_context` decision
6. [ ] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
