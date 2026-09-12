# Living Specification Protocol

AI-Verse-System is a **living architecture and product-intent repository**.

It is not a one-time documentation project that becomes stale after the first system review.

Its job is to remain the canonical big-picture record of:

- what AI-Verse currently is;
- what each component currently does;
- what each component is supposed to do at the present milestone;
- what is still missing;
- what is being planned;
- what new ideas have been accepted;
- what important fixes changed the architecture;
- what historical failures must not return;
- what the complete system is intentionally becoming.

## Core rule

Whenever a meaningful AI-Verse idea, plan, fix, lifecycle change, integration change, architectural decision, product requirement or discovered gap appears, AI-Verse-System must be updated.

A future chat, agent or contributor should not need the original conversation to understand the latest intent.

## What counts as a documentation-triggering change

Update AI-Verse-System whenever any of these happens:

1. A new system idea is proposed.
2. A previously vague idea becomes an intended requirement.
3. A new component or repository is planned.
4. A component's responsibility changes.
5. A new integration between components is planned.
6. A lifecycle command is added, changed or removed.
7. Install, attach, activate, migrate, doctor, update, disable, detach, uninstall or reconcile behavior changes.
8. A missing implementation is discovered.
9. A feature moves from INTENDED to CURRENT.
10. A feature is abandoned or superseded.
11. A bug or architectural defect is fixed.
12. An audit reveals a new system law.
13. A migration path is introduced or changed.
14. A compatibility assumption changes.
15. A new external inspiration/reference materially affects the design.
16. A release milestone changes.
17. Acceptance evidence changes readiness.
18. A component becomes more or less complete for its current target.
19. A security, ownership, scope or source-of-truth rule changes.
20. The supreme system vision itself changes.

## Capture first, classify second

A new idea should never be lost merely because its final architecture is not yet known.

Use:

`docs/IDEA-INBOX.md`

for new ideas that have not yet been fully placed.

An idea may begin as:

- RAW
- NEEDS-SCOPING
- ACCEPTED-INTENT
- DEFERRED
- REJECTED
- PROMOTED

Once the idea's owner and architectural meaning are clear, promote it into the relevant component specification or system-level document.

The inbox entry remains as provenance and points to its promoted destination.

## Update routing

### Component-local change

Update:

- `components/<component>/COMPONENT-SPEC.md`
- `components/<component>/SOURCE-MAP.md` when new evidence exists
- `components/<component>/QC.md` when readiness or an invariant changes

Examples:

- Brain gains an activation command.
- Memory adds old-agent import.
- Data fixes an isolation flaw.
- Token adds a new collector.

### Cross-component change

Also update:

- `docs/MASTER-PLAN.md`
- relevant component specs on both sides of the integration
- future supreme blueprint once it exists

Examples:

- new shared activation protocol;
- new migration contract;
- new host operation;
- shared extension registry change;
- changed install-order rule.

### New idea without implementation

Record it as **INTENDED** or **OPEN DECISION**, not CURRENT.

If architecture placement is still uncertain, put it in the idea inbox first.

### Implemented change

When implementation lands:

1. move the relevant statement from INTENDED/GAP to CURRENT where appropriate;
2. update the command/lifecycle matrix;
3. update current-target readiness;
4. add the implementation evidence to SOURCE-MAP;
5. update QC;
6. record the change in `docs/SYSTEM-CHANGELOG.md`.

### Fix / repair

A meaningful fix must record all four:

1. the defect;
2. the repair;
3. the invariant learned;
4. whether that invariant applies to other components.

Do not record important repairs only as commit history.

The system specification should explain **why the fix matters**.

## Status transitions

The documentation should visibly reflect transitions such as:

```text
IDEA
  ↓
INTENDED
  ↓
PLANNED
  ↓
IMPLEMENTING
  ↓
CURRENT
  ↓
VERIFIED
```

or:

```text
CURRENT
  ↓
DEFECT FOUND
  ↓
GAP / DEGRADED
  ↓
FIXED
  ↓
VERIFIED
```

Do not leave a feature labeled CURRENT if a new audit proves the supported path is broken.

## Readiness must move with reality

Whenever implementation changes, reassess the current-target dimensions:

- engine/core;
- OS/host integration;
- install/package;
- attach/register;
- activate/adopt;
- scope initialization;
- legacy/history migration;
- doctor/status;
- update;
- disable/detach/uninstall;
- reinstall/reconcile;
- cross-component acceptance;
- release/distribution.

A fix can increase readiness.

A newly discovered missing requirement can lower readiness.

That is expected.

AI-Verse-System is meant to show the truth, not preserve an old completion score.

## Change log

`docs/SYSTEM-CHANGELOG.md` is the concise chronological record of meaningful architecture/product-intent changes to this repository.

It should record:

- date;
- affected component(s);
- change type;
- what changed;
- why;
- where the canonical detail now lives.

The changelog is not a substitute for updating the canonical spec.

## Supreme blueprint maintenance

After the final supreme blueprint is created, it also becomes living.

Whenever a change affects:

- system topology;
- ownership;
- shared lifecycle;
- install order;
- activation/reconciliation;
- migration;
- host/runtime portability;
- system-wide definition of done;

the supreme blueprint must be updated as part of the same documentation change.

## Agent/contributor instruction

Before making or documenting a significant AI-Verse system change:

If the work is a component audit or re-audit, first read `docs/AUDIT-METHODOLOGY.md` and use its applicable lenses and completion checklist. Do not substitute an earlier component summary for a fresh source review.

1. read the relevant component spec;
2. read the relevant open ideas;
3. inspect current implementation evidence;
4. determine whether the change is CURRENT, INTENDED, GAP, HISTORICAL, LAW or INSPIRATION;
5. make the implementation change in the owning repository if that is the task;
6. update AI-Verse-System immediately afterward;
7. update readiness/QC;
8. append the system changelog.

## Non-negotiable rule

**A meaningful AI-Verse change is not fully documented until AI-Verse-System reflects it.**

The component repositories own implementation.

AI-Verse-System owns the evolving big picture.
