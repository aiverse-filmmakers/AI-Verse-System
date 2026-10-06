# AI-Verse Purpose Context Profiles v1 Contract

**Status:** IN PROGRESS — Slice 2.3  
**Parent envelope:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Parent trajectory:** `docs/PURPOSE-CONTEXT-TRAJECTORY-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

Profiles control which already-valid Purpose sections are requested/emitted for a scope. They do not create new canonical truth, new scope types, or new storage.

---

## Task 1 — operator default shape — FROZEN

The default operator projection profile is conceptually `operator_default`.

It always uses the frozen v1 shell:

```yaml
schema_version: "1.0"
scope: operator
scope_kind: operator
identity:
  kind: operator
  id: operator
provenance: {...}
```

### Default semantic retrieval set

When relevant owner-backed truth exists, `operator_default` may include:

- `problems`
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

The following remain supporting/conditional rather than expected operator-default structure:

- `narratives`
- `kpis`
- `risks`
- `current_state`

No optional section is emitted merely because it appears in this profile. Envelope presence rules still apply: absent means not emitted/relevant; present empty means known-empty; attempted unavailable/unknown reads are explicit.

### Operator-specific laws

- `operator` is the person's/global operator strategic scope, not a synthetic workspace.
- Operator Purpose MUST NOT aggregate every workspace's goals, Data databases, KPIs, initiatives, or current work by default.
- Workspace-owned strategy appears in operator Purpose only through a later explicitly allowed cross-scope relationship or an owner-backed operator-level object that references it.
- Native workspace Data is never scanned across all workspaces to manufacture operator KPIs.
- Memory visible to operator scope may provide historical evidence but never becomes current strategic authority.
- Operator identity/name/preferences remain OS-owned; mission/goals/strategy follow the active direction owner for `operator`.
- A valid operator projection can be sparse. It does not require problems, mission, goals, strategy, KPIs, or current work to exist merely to be structurally valid.

### Default usefulness target

For strategic/planning questions, the default operator shape should make it possible, when owner evidence exists, to answer:

> What am I trying to achieve globally, what matters now, what is blocking me, what am I doing about it, and why does the current work matter?

without importing unrelated workspace detail or filling empty corporate-style structure.

### Budget law

`operator_default` uses the envelope's normal bounded budget contract. Profile selection never authorizes exceeding the caller/runtime budget. Under pressure, deterministic pruning rules apply; the required shell and retained causal truth/provenance remain protected.

---

## Slice 2.3 progress

1. [x] operator default shape
2. [ ] workspace default/basic shape
3. [ ] rich workspace optional fields
4. [ ] auto-detection rules
5. [ ] `WORKSPACE.yaml` optional `purpose_context` decision
6. [ ] disabled/irrelevant behavior
7. [ ] explicit cross-scope relationship rules
