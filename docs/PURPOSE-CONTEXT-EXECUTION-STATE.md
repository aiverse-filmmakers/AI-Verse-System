# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Rule:** read the implementation plan first, then this file, then completed slice audits linked here. Update this file after every individual task.  
**Execution discipline:** execute exactly one task at a time and in plan order unless the user explicitly requests a bounded number of consecutive tasks; even then, complete and persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-06

---

## Current execution pointer

- **Phase:** 2 — Freeze the Purpose Context v1 contract
- **Current slice:** **2.1 — Versioned envelope schema**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2, 1.3
- **NEXT task:** **Slice 2.1 / Task 4 — freeze provenance format**
- **Do not start Task 5 until Task 4 is complete and recorded here.**
- Phase 1 owner/interface audit is complete.
- No Purpose Context behavior/code has been implemented yet.
- Slice 2.1 contract path: `docs/PURPOSE-CONTEXT-V1-CONTRACT.md`.

---

## Completed slice closures

### Slice 0.1 — canonical implementation plan

**Status:** COMPLETE  
**Plan:** `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Merged planning PR:** `#189`  
**Merge:** `b0b4a356ee33d86161e4ec9b3a6f9ed95b958c8e`

### Slice 1.1 — OS scope/current-context/workspace/direction-owner audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION  
**Audited ref:** `aiverse-filmmakers/AI-Verse-OS@e74a4e05b1f891e6f871f34a298bf10363a11d88`  
**Detailed closure:** `docs/PURPOSE-CONTEXT-SLICE-1.1-AUDIT.md`

Retained decisions:

- exact strategic scopes only: `operator` / `workspace:<id>`;
- use OS current-context and direction-owner boundaries;
- no stale OS strategy fallback under Brain ownership;
- OS strategy needs a bounded adapter, not arbitrary Markdown scraping;
- Purpose later joins the existing context ladder conditionally;
- carried OS schema repair: workspace manifest max length should align with runtime max 128.

### Slice 1.2 — Brain strategic model/direction audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED FINDINGS  
**Audited ref:** `aiverse-filmmakers/AI-Verse-Brain@7c77b053df627e61b3d7f11d029500ab61095c9c`  
**Detailed closure:** `docs/PURPOSE-CONTEXT-SLICE-1.2-AUDIT.md`

Frozen audit-level Telos mapping:

| Telos concept | Decision |
|---|---|
| Problem | minimal new strategic semantic; prefer `intent:problem` |
| Mission | minimal new strategic semantic; prefer `intent:mission` |
| Narrative | derive in v1 |
| Goal | existing strategic `intent:goal`; execution Goal remains separate |
| Challenge | derive in v1 |
| Strategy | minimal new strategic semantic; prefer `intent:strategy`; not `strategy_rule` |
| Initiative | existing canonical `initiative` |

Retained requirements:

- add one bounded Brain strategic snapshot API;
- validate trajectory refs before exposing graph edges;
- preserve one strategic owner per scope;
- repair the pre-existing Brain release-descriptor red gate before Purpose Brain acceptance/Core vNext.

### Slice 1.3 — Data, Memory, Gateway/runtime and Dashboard integration audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED REPAIRS  
**Detailed closure:** `docs/PURPOSE-CONTEXT-SLICE-1.3-AUDIT.md`  
**Closure creation commit:** `68dc986ec13637d019f8a25c845fdaecb8a47320`

Audited exact refs:

- Data `6e8781ff1dcd96a35dfb27868bd60605361483d0`
- Memory `b0cae8cd8da38aa657fbc736c575177aa75e5ec7`
- Gateway `089aaa6440bbbbb9f41195eafe123ad2e06d5625`
- Dashboard `2c1d1a57f7cb27eec166d4fea10dbb335250c518`

Retained decisions:

- Data current values require explicit KPI/source bindings; no arbitrary field inference.
- Data source freshness comes from record/event provenance, not adapter read time; aggregate freshness requires companion evidence or stays unknown.
- Memory supplies bounded historical/material-change evidence candidates and never outranks current owner truth.
- Gateway is runtime/context-assembly owner: OS composes Purpose, Gateway relevance-gates/injects it and accounts for its token/latency cost. Trivial tasks must create zero Purpose reads.
- Do not create a second persistent cross-owner orientation graph.
- Dashboard owns zero domain truth; Purpose reads are projections and future edits must route through OS/active owner confirmation boundaries.
- Operator Purpose requires a deliberate operator/system-scoped Dashboard read; do not fake it as a workspace.
- Native Data is workspace-bound; operator Purpose must never aggregate all workspace databases implicitly.
- Memory workspace visibility may include operator historical context, but this does not import operator strategic Purpose into a workspace.
- Dashboard workspace-ID protocol currently diverges from canonical OS/Data/Gateway IDs (Dashboard permits uppercase/underscore and caps at 64; canonical is lowercase alnum/hyphen up to 128). Repair before Purpose Dashboard qualification.

Confirmed owner/API direction after Phase 1:

| Owner | Reuse | Bounded addition currently justified |
|---|---|---|
| OS | current-context, scope, direction-owner | Purpose composer/read/explain |
| Brain | Goal/direction/object reads | strategic snapshot + Phase-2-frozen missing strategic semantics |
| Data | client/query/provenance/read adapters | optional thin typed KPI binding wrapper |
| Memory | recall/orientation/progressive recall/digests | thin material-change evidence query if required |
| Gateway | progressive context + context governor | Purpose relevance gate + owner read/injection diagnostics |
| Dashboard | registry/query/disposable projections | Purpose read queries; owner-routed commands only after Phase 8 |

Confirmed repositories required by current P1-P5 program:

`AI-Verse-System`, `AI-Verse-OS`, `AI-Verse-Brain`, `AI-Verse-Data`, `AI-Verse-Memory`, `AI-Verse-Gateway`, `AI-Verse-Dashboard`, and final `ai-verse-distribution` qualification. Skills/Automations/Multiple Bots/Connections remain optional unless later bounded evidence proves they are needed.

---

## Carried repair register

1. **Brain release descriptor:** pre-existing invalid/unreachable declared revision; must be green before Purpose Brain acceptance/Core vNext.
2. **Dashboard workspace-ID contract:** align with canonical OS/Data/Gateway IDs before Purpose Dashboard qualification.
3. **OS workspace manifest schema:** align maximum ID length with runtime max 128.
4. **Brain trajectory refs:** validate typed target existence/kind/scope/status before Purpose presents authoritative edges.
5. **Data aggregate freshness:** never infer source freshness from query execution time.
6. **Final qualification:** use pinned exact component refs; moving-main workflows are insufficient as final release evidence.

---

# Phase 2 / Slice 2.1 task checklist

Freeze in this exact order:

1. [x] `schema_version` — frozen as required string `"1.0"`; unsupported major versions fail closed; breaking semantics require a major bump. Contract commit: `3cf8c48fde4950ac69ff30e11e22d308210fab43`.
2. [x] supported scope kinds — exactly `operator` and `workspace`; workspace scope is `workspace:<id>` using canonical lowercase alnum/hyphen IDs up to 128 chars; no implicit all-workspace/global scope. Contract commit: `95ba626b02de0c7d62a16060d1c228eeaa1548ed`.
3. [x] required vs optional fields — required envelope fields are `schema_version`, `scope`, `scope_kind`, `identity`, `provenance`; semantic sections are relevance-driven optional projections; absence is not equivalent to unknown/unavailable/empty. Contract commit: `2a17d8fbfefc8699685af831150f40a453a0d2ce`.
4. [ ] provenance format
5. [ ] freshness format
6. [ ] canonical ref format
7. [ ] deterministic ordering rules
8. [ ] unknown/unavailable field behavior
9. [ ] bounded size/budget rules
10. [ ] rebuildability contract

Slice 2.1 acceptance requirements:

- a versioned schema exists;
- absent optional fields are distinguishable from unknown/unavailable owner reads;
- stale owner reads are represented, not silently treated as current;
- no generated field can become independently editable.

---

# Resume instructions for another agent/chat

1. Read `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`.
2. Read this file for the authoritative live pointer.
3. Read `docs/PURPOSE-CONTEXT-V1-CONTRACT.md` for the currently frozen Slice 2.1 contract.
4. Read Slice 1.1/1.2/1.3 audit documents only when detailed owner evidence is needed.
5. Continue **only** with **Phase 2 / Slice 2.1 / Task 4 — freeze provenance format**.
6. Phase 2 is a contract-freeze phase: update System contract/docs first; do not begin owner implementation code before the relevant contract tasks are complete.
7. Persist the execution-state document after Task 4 before Task 5.
