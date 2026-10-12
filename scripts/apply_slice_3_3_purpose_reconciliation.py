#!/usr/bin/env python3
"""One-shot Slice 3.3 Purpose Context System-truth reconciliation.

Exact-match only. The script refuses to run if the known stale blueprint text has
moved or changed, so it cannot silently rewrite a different architecture state.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT / "docs" / "FINAL-AI-VERSE-BLUEPRINT.md"
CHANGELOG = ROOT / "docs" / "SYSTEM-CHANGELOG.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one stale block, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    blueprint = BLUEPRINT.read_text(encoding="utf-8")

    blueprint = replace_once(
        blueprint,
        "**Baseline date:** 2026-10-05\n**Scope:**",
        "**Baseline date:** 2026-10-05  \n**Last evidence-first reconciliation:** 2026-10-12  \n**Scope:**",
        "blueprint metadata",
    )

    old_14a = '''### 14A. Purpose Context / Telos-inspired deep context

AI-Verse should add a first-class **Purpose Context** layer that answers:

> Why does this scope exist, what matters most, where is it trying to go, and what changed recently?

This is an **INTENDED derived context layer**, not a new component and not a new canonical owner.

It composes existing owner truth:

- OS: operator/workspace identity, current scope and OS-owned current context;
- Brain/current direction owner: mission/purpose, goals, desired states, priorities, strategies, initiatives and strategic constraints;
- Data: current structured operational truth and KPI values;
- Memory: historical evidence, lessons and provenance;
- Gateway/runtime: live run/session state.

Purpose Context may expose a bounded envelope containing mission, goals, priorities, strategies, constraints, KPIs, current state and recent material changes. The envelope must be rebuildable and must preserve owner/source provenance.

### LAW

Purpose Context must never become a second editable Goal store, Memory store, Data store, OS profile store or Dashboard database.

Mission, goal, priority, value and strategic-constraint changes must route to the current canonical owner. Material strategic changes require explicit user confirmation; a model-generated projection cannot silently redefine intent.

Detailed accepted intent and execution gate:

- `docs/PURPOSE-CONTEXT-TELOS-ADOPTION-PLAN.md`
'''

    new_14a = '''### 14A. Purpose Context / Telos-inspired deep context

**CURRENT / ACCEPTED:** Purpose Context v1 is complete, accepted and Core-admitted through immutable release `core-purpose-context-public-beta-2026-10-09`. Canonical execution state is `COMPLETE / ACCEPTED / CORE ADMITTED`, schema `1.0`, with the final product-value gate `VALUE PROVEN`.

Purpose Context answers:

> Why does this scope exist, what matters most, where is it trying to go, and what changed recently?

It is an **owner-backed, read-only, derived and rebuildable strategic projection**, not a new component and not a new canonical owner.

It composes existing owner truth:

- OS: operator/workspace identity, exact scope and OS-owned current operating context;
- Brain/current direction owner: mission/purpose, goals, desired states, priorities, strategies, initiatives and strategic constraints;
- Data: current structured operational truth and KPI values;
- Memory: historical evidence, lessons and provenance without Memory authority promotion;
- Gateway/runtime: bounded live assembly and delivery without becoming Purpose truth authority.

Accepted v1 supports `operator` and exact `workspace:<id>` scopes, workspace `auto/basic/rich` progressive disclosure, and trajectory/explain behavior that reports missing links and cycles rather than inventing continuity. Rich fields appear only when owner-backed evidence exists.

High-impact strategic mutation remains owner-routed and subject to the applicable explicit confirmation boundary. The accepted runtime envelope is bounded, and the accepted trivial deterministic value fixture adds zero Purpose reads and zero Purpose bytes.

### LAW

Purpose Context has **no stale fallback, no Memory authority promotion, no second Purpose truth store, and no release-lineage rewrite**. It must never become a second editable Goal store, Memory store, Data store, OS profile store or Dashboard database.

Mission, goal, priority, value and strategic-constraint changes route to the current canonical owner. A projection cannot silently redefine intent.

The accepted Purpose Core line is frozen by release evidence. Current Brain, Memory, Skills and Data remain exactly at their admitted Purpose refs; current OS descends from the admitted Purpose OS ref. **Accepted Purpose ancestry does not by itself prove exact owner acceptance of every later descendant revision.** The separate current-owner-acceptance governance gap remains open, and **newer branch movement is not acceptance evidence merely because it is newer**.

Canonical evidence and reconciliation boundary:

- `docs/PURPOSE-CONTEXT-EXECUTION-STATE.md`
- `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`
- `docs/REPOSITORY-TRUTH-RECONCILIATION-2026-10-12.md`
- Distribution release `core-purpose-context-public-beta-2026-10-09`
'''
    blueprint = replace_once(blueprint, old_14a, new_14a, "Purpose section 14A")

    old_p1 = '''### EARLY P1: Purpose Context / Telos-inspired deep context

Once the active whole-system repair program, composed requalification and bounded post-repair independent recheck establish a new safe exact-ref baseline, Purpose Context becomes the **first eligible new cross-owner capability project**.

It must not interrupt the repair sequence, but it also must not be pushed behind unrelated long-range expansion.

Initial implementation should be read-only and owner-backed:

1. versioned Purpose Context projection;
2. OS + Brain + Data composition with optional Memory evidence;
3. context-ladder integration;
4. controlled owner-routed strategic mutation proposals;
5. material-change/current-state projection;
6. simple Dashboard/product projection later.

It is intentionally **not** a new repository or canonical database.
'''

    new_p1 = '''### COMPLETED P1: Purpose Context / Telos-inspired deep context

The planned first post-repair cross-owner capability has been completed and admitted as Purpose Context v1 in `core-purpose-context-public-beta-2026-10-09`.

Accepted v1 delivered the owner-backed read-only projection, OS/Brain/Data composition with optional Memory evidence, context-ladder/runtime integration, controlled owner-routed strategic mutation boundaries, material-change/trajectory/explain projection, scope isolation and the `VALUE PROVEN` gate without creating a new repository or canonical database.

Post-v1 Purpose work is not an automatic continuation of the completed program. Any further expansion must be separately authorized, owner-routed and independently accepted while preserving the v1 ownership, isolation, provenance and no-stale-fallback laws.
'''
    blueprint = replace_once(blueprint, old_p1, new_p1, "Purpose priority section")

    old_override = '''> **Current sequencing override, 2026-10-02:** the Independent Whole-System Public-Beta repair/requalification program is the active execution authority. Do not start new Purpose Context implementation inside those repair waves. Immediately after that program's bounded final recheck establishes a safe baseline, implement the Purpose Context/Telos-inspired project before unrelated lower-priority expansion. Safety or failed-acceptance repairs always retain priority.
'''
    new_override = '''> **Sequencing reconciliation, 2026-10-12:** the October 2 ordering was fulfilled. The repair/requalification baseline preceded Purpose Context, and Purpose Context v1 subsequently completed and was Core-admitted on October 9. That historical gate is no longer a future instruction. Safety or failed-acceptance repairs still retain priority, and any post-v1 Purpose expansion requires a separately authorized acceptance path.
'''
    blueprint = replace_once(blueprint, old_override, new_override, "Purpose sequencing override")

    BLUEPRINT.write_text(blueprint, encoding="utf-8")

    changelog = CHANGELOG.read_text(encoding="utf-8")
    marker = "## 2026-10-12: Reconciled accepted Purpose Context v1 into the living blueprint"
    if marker not in changelog:
        entry = '''## 2026-10-12: Reconciled accepted Purpose Context v1 into the living blueprint

- Reconciled the October 5 living blueprint forward to immutable accepted/admitted Purpose Context v1 evidence instead of regressing accepted implementation to stale prose.
- Recorded Purpose Context as an owner-backed, read-only, rebuildable strategic projection with `operator` and exact `workspace:<id>` scope, progressive disclosure, trajectory/explain truthfulness and owner-routed high-impact mutation boundaries.
- Preserved the accepted laws: no stale fallback, no Memory authority promotion, no second Purpose truth store and no release-lineage rewrite.
- Recorded the evidence boundary that accepted ancestry does not prove exact owner acceptance for every later descendant and that newer branch movement is not acceptance evidence by recency alone.
- Kept the separate Core exact-owner-acceptance blocker and later-slice drift open.

Canonical detail:

- `docs/FINAL-AI-VERSE-BLUEPRINT.md`
- `docs/PURPOSE-CONTEXT-EXECUTION-STATE.md`
- `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`
- `docs/REPOSITORY-TRUTH-RECONCILIATION-2026-10-12.md`

---

'''
        changelog = entry + changelog
        CHANGELOG.write_text(changelog, encoding="utf-8")


if __name__ == "__main__":
    main()
