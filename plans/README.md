# Implementation Plans

This directory contains implementation plans for work intended to be carried out in the AI-Verse repositories.

## Plan Maker / implementation-plan maker

For the planning method, PRD or architecture-plan template, start with [Plan Maker](../docs/PLAN-MAKER.md). The folders below hold actual implementation plans; they are not alternative methods.

## Folder meanings

- `in-progress/`: plans that are ready for implementation or are actively being implemented. Each plan has an explicit outcome, proportional acceptance and status; substantial programs add phases and slices.
- `completed/`: plans whose implementation and acceptance evidence are complete. Completed plans remain as historical records.
- `blocked/`: plans paused because evidence requires a protected plan amendment, missing owner decision, unresolved dependency, or another explicit blocker.
- `archive/`: superseded or retired plans that remain useful for history.

## Plan status

A plan is not implementation code and does not claim that a feature is shipped. The owning implementation repository and current acceptance evidence remain authoritative.

Plans use the Adaptive Implementation Planning method in `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`:

- permanent laws and non-negotiables;
- dependency-safe phases;
- slices with fixed outcomes and acceptance criteria;
- adaptive execution tasks discovered at the start of each slice;
- explicit evidence, validation, blockers, drift, and next steps.

Discovery may adapt the route, but it may not silently change the destination, canonical ownership, safety requirements, preservation requirements, or acceptance criteria. Protected changes require a recorded plan amendment before implementation continues.

For plans in `in-progress/`, keep a useful execution checkpoint and distinguish intended work from shipped implementation. Substantial multi-slice programs update their accepted slice progress; compact plans do not need phase counters.

