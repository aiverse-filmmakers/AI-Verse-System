# AI-Verse Purpose Context Trajectory v1 Contract

**Status:** IN PROGRESS — Slice 2.2  
**Parent contract:** `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`  
**Canonical owner:** `AI-Verse-System`

This contract defines the bounded, explainable relationship graph used by Purpose Context. The graph is a derived projection over owner-backed refs; it is not a second strategic database.

---

## Task 1 — relation vocabulary — FROZEN

V1 relations are exactly `addresses`, `serves`, `advances`, `blocks`, `executes`, `measures`, `affects`, `supersedes`. No free-form relation is valid. Edges require canonical evidence; similarity, embeddings, shared tags/names, co-occurrence, or model inference alone cannot create an authoritative edge.

## Task 2 — allowed source/target kinds — FROZEN

V1 node kinds: `problem`, `mission`, `desired_outcome`, `goal`, `challenge`, `strategy`, `initiative`, `kpi`, `risk`, `current_work`, `material_change`.

Allowed relation matrix:
- `addresses`: mission→problem; strategy→problem|challenge; initiative→problem|challenge.
- `serves`: goal→mission|desired_outcome; initiative→goal.
- `advances`: strategy|initiative|current_work→goal|desired_outcome.
- `blocks`: challenge|risk→goal|strategy|initiative|current_work.
- `executes`: initiative→strategy; current_work→initiative|strategy.
- `measures`: kpi→goal|desired_outcome.
- `affects`: risk→mission|desired_outcome|goal|strategy|initiative|current_work; material_change→problem|mission|desired_outcome|goal|challenge|strategy|initiative|risk|current_work.
- `supersedes`: same semantic node kind only.

Invalid kind pairs never enter the authoritative graph and are never coerced.

## Task 3 — cycle behavior — FROZEN

Any self-edge is invalid. Structural ancestry relations are `serves`, `advances`, `executes`, `supersedes`; their authoritative subgraph must be acyclic. Structural edges inside a multi-node strongly connected component are excluded from authoritative traversal and reported as partial with stable diagnostics. Purpose never silently reverses/deletes owner state or invents replacement edges.

## Task 4 — missing-parent behavior — FROZEN

Target states are `resolved`, `stubbed`, `unavailable`, `missing`, `forbidden`, `invalid`; only `resolved` and `stubbed` targets participate in authoritative traversal. Bounded pruning retains identity stubs for retained edges. Broken targets never fuzzy-match, cross workspace boundaries, substitute Memory as current truth, or invoke model inference. Explanation stops at the last verified node of a broken branch.

## Task 5 — supersession behavior — FROZEN

`supersedes` is owner-confirmed historical replacement evidence only. Same-kind source/target required; timestamps, version numbers, titles, similarity and model judgment never infer replacement. Currentness remains defined by the active canonical owner, not chain position. Competing unresolved replacements remain ambiguous. Supersession may be explanation context but is not normal causal ascent.

## Task 6 — orphan initiative/current-work behavior — FROZEN

A valid initiative/current-work node with no valid parent relation is allowed and remains visible when relevant. It is marked `linkage_state: orphan` / `linkage_reason: no_valid_parent_relation`. Purpose never invents a parent. Explain stops causal ascent at the orphan and returns stable reason `trajectory_orphan`. Tiny workspaces may legitimately remain this simple.

## Task 7 — explain traversal rules — FROZEN

The v1 explain operation answers “why are we doing this?” by traversing only validated owner-backed/derived edges from an exact starting node.

### Starting node

The caller supplies or resolves one exact node identity. Fuzzy title/name lookup may be offered by a higher-level UI only if it resolves to one exact canonical node before traversal begins. Ambiguous starts fail explicitly.

### Causal ascent relations

The normal upward causal relations are:

1. `executes`
2. `serves`
3. `advances`
4. `addresses`
5. `measures` only when the starting/encountered node is a KPI

`blocks` and `affects` are contextual side relationships, not causal parents. `supersedes` is historical/replacement context, not causal ascent.

The relation priority above orders otherwise equally valid parent branches; it does not allow an invalid edge to outrank a valid one.

### Expected upward paths

Typical verified ascent may look like:

```text
current_work --executes--> initiative
initiative --executes--> strategy
strategy --advances--> goal
goal --serves--> mission
mission --addresses--> problem
```

Shorter valid paths are equally acceptable, for example `current_work --advances--> goal --serves--> mission`. Missing intermediate layers are not fabricated.

### Branching

- Multiple independently valid parents may produce multiple explanation branches.
- One deterministic branch may be labeled `primary` for concise rendering; other valid branches remain available and are not deleted from the graph.
- Primary selection follows relation priority, then the deterministic graph ordering frozen in Task 8.
- A branch terminates when it reaches a legitimate root (`problem`, `mission`, or `desired_outcome` with no valid higher causal edge), an orphan, a broken parent, a cycle-rejected edge, scope/authority boundary, or traversal budget.

### Context attachments

For every node on the causal path, Purpose may attach validated contextual evidence:

- `blocks` from challenge/risk nodes;
- `affects` from risk/material-change nodes;
- `supersedes` history for the current node;
- KPI `measures` links where relevant.

Context attachments never become causal parents unless their relation token separately permits causal ascent.

### Truth and completeness

Every returned path contains exact node identities and edge evidence refs. Explain MUST distinguish:

- `complete` — branch reaches a validated legitimate root without unresolved required ancestry;
- `partial` — verified path ends because of missing/unavailable/forbidden/invalid parent, cycle rejection, or bounded truncation;
- `orphan` — start/path ends because no valid parent relation exists.

A `complete` label means complete relative to the validated graph currently available, not proof that reality contains no other causes.

### Safety rules

- No model-generated prose may add a relationship absent from the verified path.
- Human-readable explanation may paraphrase node content but must preserve the edge semantics.
- Cross-scope traversal occurs only through an explicitly allowed, visible edge; otherwise the branch stops without leaking target content.
- Historical Memory may explain what happened but never substitutes for a missing current strategic parent.
- Traversal uses visited guards even for non-structural context attachments.

### Boundedness

Explain obeys the envelope byte budget plus explicit traversal caps in implementation. Budget pressure prunes secondary branches/context before the primary verified chain. If even the minimum truthful primary path cannot fit, the operation fails explicitly rather than silently changing semantics.

---

## Slice 2.2 progress

1. [x] relation vocabulary
2. [x] allowed source/target kinds
3. [x] cycle behavior
4. [x] missing-parent behavior
5. [x] supersession behavior
6. [x] orphan initiative/current-work behavior
7. [x] explain traversal rules
8. [ ] deterministic graph ordering
