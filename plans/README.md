# Implementation Plans

This directory contains implementation plans for work intended to be carried out in the AI-Verse repositories.

**Find commercial access/licensing work here:** [Authorized OS Access: Skool Membership and Revocable App Licensing](in-progress/AUTHORIZED-OS-ACCESS-AND-SKOOL-LICENSING-2026-10-28.md). Research-only at creation, 0/7 slices, no app lock shipped; provider verification and execution-path audit are required before implementation.

## Folder meanings

- `in-progress/`: plans that are ready for implementation or are actively being implemented. Each plan has a fixed destination, phases, slices, acceptance criteria, required evidence, and an explicit status.
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

For plans in `in-progress/`, agents should update the plan before and after each slice, keep progress measured by completed slices, and distinguish intended work from shipped implementation.

