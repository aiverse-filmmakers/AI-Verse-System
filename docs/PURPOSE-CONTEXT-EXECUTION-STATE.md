# Purpose Context — Task-Level Execution State

**Purpose:** durable continuation checkpoint for `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`  
**Rule:** read the implementation plan first, then this file, then completed slice audits linked here. Update this file after every individual task.  
**Execution discipline:** execute exactly one task at a time and in plan order unless the user explicitly requests a bounded number of consecutive tasks; even then, complete and persist each task before beginning the next.  
**Current admitted Core baseline:** `core-repaired-public-beta-2026-10-06`  
**Last updated:** 2026-10-06

---

## Current execution pointer

- **Phase:** 1 — Fresh owner/interface audit before implementation
- **Current slice:** **1.3 — Audit Data, Memory, runtime, and Dashboard integration surfaces**
- **Slice state:** IN PROGRESS
- **Completed slices:** 0.1, 1.1, 1.2
- **Audited Data ref:** `aiverse-filmmakers/AI-Verse-Data@6e8781ff1dcd96a35dfb27868bd60605361483d0`
- **Completed in Slice 1.3:** Tasks 1-2
- **NEXT task:** **Slice 1.3 / Task 3 — audit Memory recent changes/history/provenance queries**
- **Do not start Task 4 until Task 3 is complete and recorded here.**
- No Purpose Context behavior/code has been implemented yet; Phase 1 remains audit-only.

---

## Completed slice closures

### Slice 0.1 — canonical implementation plan

**Status:** COMPLETE

- plan: `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`
- planning PR: `#189`
- merge: `b0b4a356ee33d86161e4ec9b3a6f9ed95b958c8e`

### Slice 1.1 — OS scope/current-context/workspace/direction-owner audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION  
**Audited ref:** `aiverse-filmmakers/AI-Verse-OS@e74a4e05b1f891e6f871f34a298bf10363a11d88`  
**Detailed closure:** `docs/PURPOSE-CONTEXT-SLICE-1.1-AUDIT.md`

Key retained decisions:

- Purpose uses exact `operator` / `workspace:<id>` scopes only.
- Use OS `current-context` as the ownership-aware current-context read boundary.
- Direction-owner state is the sole strategic-owner selector.
- Frozen OS strategy never becomes fallback truth under Brain ownership.
- OS-owned strategic Markdown needs bounded deterministic adapters; no arbitrary scraping.
- Purpose is conditionally injected into the existing context ladder; trivial tasks must produce zero Purpose reads.

### Slice 1.2 — Brain strategic model/direction audit

**Status:** COMPLETE / ACCEPTED FOR CONTINUATION WITH CARRIED FINDINGS  
**Audited ref:** `aiverse-filmmakers/AI-Verse-Brain@7c77b053df627e61b3d7f11d029500ab61095c9c`  
**Detailed closure:** `docs/PURPOSE-CONTEXT-SLICE-1.2-AUDIT.md`  
**Closure commit:** `16f119325f5a00ef7a5a65c038e72db0ac8661e9`

Final Telos→Brain mapping:

| Telos concept | Decision |
|---|---|
| Problem | minimal new canonical strategic semantic required; prefer `intent:problem` before a new kind |
| Mission | minimal new canonical strategic semantic required; prefer `intent:mission` |
| Narrative | derive from owner-backed state for v1 |
| Goal | existing strategic `intent:goal`; keep execution `goal` service distinct |
| Challenge | derive from active gaps/blockers/constraints for v1 |
| Strategy | minimal new canonical strategic semantic required; prefer `intent:strategy`; **not** `strategy_rule` |
| Initiative | existing canonical `initiative` |

Key retained Brain decisions:

- Add one stable bounded read-only Brain strategic snapshot contract in Phase 3; OS must not read Brain private storage.
- Validate trajectory refs before exposing them as authoritative graph edges; current `serves`/gap/source refs are not fully typed/referentially enforced.
- Preserve one strategic owner per scope; never infer owner from object presence or Brain availability.
- Keep strategic intent Goal semantics separate from execution-grade Goal service semantics.
- `strategy_rule` is learned operating doctrine and must not be used as the Telos business/project Strategy node.
- Narrative and Challenge should remain derived in v1 unless usage proves a canonical lifecycle is necessary.

Exact-ref Brain test evidence:

- CI run `37183204509` — **SUCCESS** — 6 OS/Python matrix jobs + package smoke; Ubuntu/Python 3.12 reports **242 tests passed**.
- OS Direction Ownership Contract run `37183204505` — **SUCCESS**.
- Skills Receipt Contract run `37183204511` — **SUCCESS**.
- Release Descriptor run `37183204489` — **FAILURE** due a pre-existing invalid/unreachable declared descriptor revision (`5d29b42a337bd078898c2e2ec876831a9ea421fa`).

Carried Brain repair requirement:

- The release-descriptor red gate must be repaired on or before the first Purpose-related Brain descendant is accepted, and before final Core vNext qualification.
- Final Purpose cross-owner acceptance must pin exact component refs; the existing OS Direction workflow clones moving OS `main` and cannot be the sole qualification evidence.

---

# Current Slice 1.3 task checklist

Audit in this exact order:

1. [x] Data current KPI values and operational truth
2. [x] Data freshness/provenance metadata
3. [ ] Memory recent changes/history/provenance queries
4. [ ] runtime/context-ladder injection points
5. [ ] Dashboard read/write boundaries
6. [ ] exact workspace scoping behavior in each component

## Slice 1.3 / Task 1 — Data current KPI values and operational truth

**Status:** COMPLETE  
**Audited ref:** `aiverse-filmmakers/AI-Verse-Data@6e8781ff1dcd96a35dfb27868bd60605361483d0`  
**Data `main` at audit:** same exact repaired Core ref.

Durable findings:

- Data exposes stable public read surfaces including client/query/provenance and a deliberately read-only Brain adapter.
- Existing records plus bounded queries/aggregates are sufficient for current KPI/operational values when an application schema explicitly stores or deterministically derives them.
- Data must not infer KPI meaning by scanning arbitrary schemas. A strategic KPI definition must carry or resolve to an owner-backed Data binding; without one, the current value is unavailable.
- Strategic KPI definitions/targets remain strategic-owner truth; Data provides mapped current values/evidence only.
- Purpose must use public Data interfaces, never SQLite/private storage.

## Slice 1.3 / Task 2 — Data freshness/provenance metadata

**Status:** COMPLETE  
**Audited ref:** `aiverse-filmmakers/AI-Verse-Data@6e8781ff1dcd96a35dfb27868bd60605361483d0`

Durable findings:

- Canonical Data records expose `version`, `createdAt`, `updatedAt`, actor attribution, schema version and delete metadata. These are the primary record-level recency/current-version signals.
- The read-only Brain adapter adds `answeredAt`, scope, actor, authorization and record count. `answeredAt` is the **read time**, not proof that the underlying record itself changed recently; Purpose must never confuse answer time with source freshness.
- Data provenance provides immutable mutation events and durable receipts with `committedAt`, trusted workspace binding, space/entity/record identity, before/after versions, actor, request/transaction/idempotency IDs and integrity-checked event/receipt linkage.
- Event/receipt readers verify SHA-256 integrity and fail closed on corruption. Data events are structured audit facts and explicitly are **not Memory**.
- There is no universal Data-wide freshness TTL/staleness policy. Purpose must evaluate freshness from the owner record/event timestamps plus the freshness requirement of the specific Purpose field/KPI contract.
- Query pages return full record snapshots and therefore retain per-record `updatedAt`/version metadata. Aggregate results return only aggregate values; they do not intrinsically expose a `max(updatedAt)`/source-watermark freshness proof.
- Therefore an aggregate-backed KPI needs one of: a declared companion freshness query/event watermark, a typed Purpose/Data wrapper that returns source freshness metadata, or an explicit `freshness: unknown` state. Purpose must not label a bare aggregate as fresh merely because it was computed now.
- `DataProvenance.listEvents` is bounded/filterable and can support material-change detection for Data-owned operational facts, but those events remain audit evidence; semantic materiality belongs to Purpose/Brain/Memory projection logic, not Data.

Primary evidence inspected:

- `src/protocol/types.ts`
- `src/query/types.ts`
- `src/brain/adapter.ts`
- `src/provenance/types.ts`
- `docs/EVENTS-RECEIPTS-PROVENANCE-V0.1.md`

### Slice 1.3 acceptance criteria

- every planned integration has a declared existing or required new owner API;
- Purpose code does not read private storage formats directly when a stable owner API can be used or added;
- exact repos required for P1-P5 are known before implementation begins.

---

# Resume instructions for another agent/chat

1. Read `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`.
2. Read this file for the live pointer.
3. Read completed slice audit files only when their detailed evidence/decisions are needed.
4. Continue **only** with **Phase 1 / Slice 1.3 / Task 3 — audit Memory recent changes/history/provenance queries**.
5. Start from repaired Memory baseline `b0cae8cd8da38aa657fbc736c575177aa75e5ec7` unless fresh inspection proves current `main` is a deliberate descendant; record the exact ref actually audited.
6. After Task 3, update this file before Task 4.
