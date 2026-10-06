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

The richer workspace profile is conceptually `workspace_rich`. It is an additive **read profile over the same v1 envelope**, not a different schema and not a “corporate mode” subsystem.

### Rich profile may activate

In addition to the `workspace_basic` sections, `workspace_rich` may request/employ these already-frozen optional sections when canonical owner evidence exists:

- `narratives`
- `kpis`
- `risks`
- richer `constraints`
- richer `current_state`
- `recent_material_changes` with operational/strategic effects

It may also retain more secondary trajectory branches/context attachments within the same byte budget where relevance and ranking justify them.

### KPI rule

A rich workspace does not gain KPIs merely because it is “business-like.” A KPI appears only when:

1. the strategic definition/target is owner-backed; and
2. any `current_value` has an explicit current-truth binding to Data or another declared current-truth owner.

No field scanning, guessed metric matching, or query-time freshness inference is allowed.

### Risk rule

Risks appear only when owner-backed risk records or a frozen deterministic derivation with evidence exists. Purpose does not generate a speculative risk register to make a workspace look complete.

### Team/resources/customers/infrastructure/budget

These are useful Telos/corporate concepts but are **not first-class top-level sections in the frozen v1 envelope**.

Therefore v1 MUST NOT silently add new top-level `team`, `resources`, `customers`, `infrastructure`, or `budget` fields merely because `workspace_rich` is selected.

They may be surfaced only when one of these is true:

- an existing frozen v1 section legitimately represents that owner-backed fact without semantic distortion (for example a bounded `current_state` item); or
- a later backward-compatible contract revision explicitly adds a typed optional field/section.

If neither is true, the information stays outside Purpose v1 rather than being squeezed into the wrong semantic field.

### Richness is optional, not a maturity score

- `workspace_rich` does not mean the workspace is more important, mature, or “better.”
- A product/company/client/team workspace may still correctly remain `workspace_basic`.
- A small workspace may expose a KPI or risk without becoming a giant corporate projection.
- Rich profile never creates empty sections to satisfy a template.
- The same isolation, owner authority, provenance, freshness, graph and budget laws apply unchanged.

### Anti-bloat rule

Selecting `workspace_rich` only broadens the **eligible read set**. It does not require all eligible sections to be emitted. Relevance, canonical availability and byte budget still decide what appears.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [x] workspace default/basic shape
3. [x] rich workspace optional fields
4. [ ] auto-detection rules
5. [ ] `WORKSPACE.yaml` optional `purpose_context` decision
6. [ ] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
