# Purpose Context / Telos-Inspired Adoption Plan

**Status:** ACCEPTED-INTENT / NOT IMPLEMENTED  
**Priority:** EARLY P1 / first eligible post-repair cross-owner capability  
**External inspiration:** https://github.com/danielmiessler/telos  
**License of inspiration repo:** MIT  
**AI-Verse rule:** borrow the deep-context idea, not a duplicate canonical store

## 1. Purpose

AI-Verse should gain a first-class **Purpose Context** layer that lets an agent understand, before acting:

- what this person, workspace or organization is trying to achieve;
- what matters most now;
- which goals and priorities are active;
- which strategies and constraints govern the work;
- which KPIs or success measures matter;
- what the current state is;
- what recent activity materially changed that state.

The user-facing mental model is:

```text
Purpose Context = why / what matters / where we are going
Memory         = what happened before
Data           = structured current operational truth
Skills         = how to do something
Tools          = what can be acted on
```

This is inspired by Daniel Miessler's Telos project, which demonstrates the value of collecting mission, goals, problems, strategies, KPIs and current activity into one deep-context frame.

AI-Verse must implement the advantage without collapsing its existing ownership model.

## 2. Non-negotiable architecture

**Purpose Context is not a new canonical database and is not a new strategic owner.**

It is a scoped, derived, rebuildable context envelope assembled from canonical AI-Verse owners.

It must never become:

- a second Brain goal store;
- a second OS profile/current-context store;
- a second Data database;
- a second Memory system;
- a hidden Dashboard database;
- a prompt file whose stale copy can overrule current owner state.

The complete envelope should be disposable and reconstructable from owner-backed records plus provenance.

## 3. Canonical owner split

| Purpose Context field | Canonical owner |
|---|---|
| operator/workspace identity and current operating scope | OS |
| stable user preferences and declared working constraints where OS already owns them | OS |
| explicit mission/purpose when treated as strategic intent | Brain, or OS while OS still owns strategic direction |
| goals, desired states, priorities, strategies, initiatives and strategic constraints | current strategic direction owner, normally Brain after explicit handover |
| KPI definitions when part of strategy | Brain |
| current KPI values and structured operational state | Data |
| historical lessons, changes and provenance | Memory |
| live run/session state | Gateway/runtime |
| capability packages | Skills |
| recurring wake/cadence | Automations |
| durable coordination state | Multiple Bots |

No field may be copied into Purpose Context and then become independently editable as a second source of truth.

## 4. Conceptual context envelope

The implementation may evolve, but the product should be able to produce a bounded envelope equivalent to:

```yaml
purpose:
  mission: ...
  desired_outcomes: ...

priorities:
  - ...

goals:
  - id: ...
    objective: ...
    status: ...
    completion_contract: ...

strategies:
  - ...

constraints:
  - ...

kpis:
  - definition: ...
    current_value: ...
    source: ...

current_state:
  - ...

recent_material_changes:
  - ...

provenance:
  owner_refs: ...
  generated_at: ...
  scope: ...
```

This object is a projection. Owner records remain authoritative.

## 5. Read path

The preferred read path is:

```text
current task + system/workspace scope
        -> bounded Purpose Context projection
        -> current owner evidence
        -> Memory/history expansion only when useful
        -> exact source evidence when precision requires it
```

Purpose Context should integrate with the existing context ladder rather than create a parallel retrieval architecture.

For ordinary work, it should give the model a compact orientation layer before deeper Memory/Data retrieval.

## 6. Write path and confirmation law

The model may notice that Purpose Context appears stale, incomplete or contradictory.

It may **propose** a change, but all durable mutation must route to the canonical owner.

High-impact fields require explicit user confirmation before mutation:

- mission/purpose;
- top-level goals;
- priority ordering;
- values;
- strategic constraints;
- strategic authority transfer;
- deletion or replacement of durable strategic intent.

Example:

```text
User: Our main goal is now shipping public beta.

AI-Verse:
This would replace the current top priority with "Ship public beta".
Update your strategic Purpose Context?

[Confirm]
```

Low-risk factual state changes may follow the existing owner-specific write/approval policy. Purpose Context itself never grants authority to bypass those policies.

## 7. Current-state and activity behavior

Telos-style activity is useful, but AI-Verse should not create a second canonical activity log merely for this feature.

Instead, Purpose Context may project recent material changes from owner-backed events, receipts, Data changes, Goal changes and Memory provenance.

Example:

```text
GOAL
Launch Dashboard MVP

MATERIAL CHANGES
- Gateway lifecycle blocker closed.
- Packaging failure became the current blocker.
- Dashboard work remains gated by the repair program.
```

The projection should emphasize changes that alter goals, priority, feasibility, blockers or current state.

## 8. Earliest implementation gate

This feature must **not** interrupt or contaminate the active Independent Whole-System Public-Beta repair sequence.

The earliest normal implementation gate is:

1. complete the ordered repair program through its composed requalification;
2. complete the bounded post-repair independent recheck and establish a new safe exact-ref baseline;
3. freeze the owner contracts that Purpose Context will consume;
4. begin Purpose Context as the **first eligible new cross-owner capability project**, before unrelated lower-priority expansion work.

It should not be pushed to the end of Apps, packs, channels, federation or other long-range expansion.

Safety, data-integrity, authority and failed-acceptance repairs still outrank it whenever they appear.

## 9. Recommended implementation slices

### Slice P1: read-only owner-backed projection

- define a versioned Purpose Context envelope;
- compose OS + Brain + Data owner reads;
- include Memory provenance/history only when useful;
- include explicit source/owner references;
- prove the projection can be deleted and rebuilt.

### Slice P2: context-ladder integration

- inject bounded Purpose Context during relevant planning/work turns;
- add budget/freshness rules;
- avoid loading it when irrelevant;
- descend to exact owner evidence for sensitive facts.

### Slice P3: controlled mutation proposals

- detect proposed mission/goal/priority/constraint changes;
- route writes to the current canonical owner;
- require explicit confirmation for high-impact strategic changes;
- preserve idempotency and receipts.

### Slice P4: material-change projection

- project recent owner-backed activity that changes blockers, feasibility or priority;
- avoid raw event spam;
- preserve exact provenance.

### Slice P5: product surface

- show a simple human-readable Purpose view in the product shell/Dashboard;
- keep internal component ownership invisible to ordinary users;
- allow edits only through owner-routed commands.

## 10. Acceptance criteria

Purpose Context is not complete until:

1. no new canonical database or competing truth store exists;
2. every field resolves to a declared owner;
3. stale projections cannot overrule current owner state;
4. mission/goal/priority changes require the correct confirmation/authority path;
5. current KPI values come from Data or another declared current-truth owner;
6. historical context remains Memory-owned;
7. the envelope is scope-bound and workspace-isolated;
8. the projection is rebuildable;
9. the context ladder can include/exclude it based on relevance and budget;
10. exact-source descent is available for sensitive facts;
11. clean restart does not create duplicate Purpose state;
12. Dashboard/UI remains a projection, not the owner.

## 11. Explicit non-goals

Do not:

- create an `AI-Verse-Telos` repository merely because the inspiration project is separate;
- copy Telos as one giant canonical Markdown file;
- move Brain goals into OS;
- move Data KPIs into Brain as duplicate operational truth;
- turn Memory into current strategic state;
- let Dashboard edit a private local copy;
- silently rewrite the user's mission, values or priorities;
- treat a model-generated summary as stronger than owner evidence.

## 12. Provenance

External inspiration:

- Daniel Miessler, Telos: https://github.com/danielmiessler/telos
- Telos describes a framework for deep context around mission, goals, problems, strategies, KPIs and current activity.
- The AI-Verse design intentionally adapts that concept to AI-Verse's existing canonical-owner architecture rather than importing Telos as a competing subsystem.

No Telos implementation code is copied by this document.
