# Safe Infrastructure Slice 5.1 - Cross-Repo Regression and Destructive-Negative Tests

**Status:** IN PROGRESS  
**Canonical slice:** 5.1  
**Outcome:** add a composed qualification layer that proves the Safe Infrastructure laws still hold together across Distribution plus the current OS/Skills owner contracts, without changing product semantics.

## Refreshed starting refs

Frozen before any Slice 5.1 product/test write:

- `aiverse-filmmakers/AI-Verse-System@db42146189d2d869925d26668a6683cf437fdd80`
- `aiverse-filmmakers/ai-verse-distribution@10d04c723e5918506f1f76aabf1c59bfa23f7b8b`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

No owner/product drift was found after Slice 4.4. The currently admitted OS and Skills descriptors still publish no live structural migration recipe, so real-member structural apply remains a truthful no-op while synthetic admitted fixtures exercise mutation semantics.

## Existing coverage inventory

Distribution already has focused coverage for the individual mechanisms Slice 5.1 must compose, including:

- `tests/test_update_cli.py`, `tests/test_core_update_plan.py`, `tests/test_infrastructure_update_gate.py` for update/apply and read-only planning boundaries;
- `tests/test_experience_overview.py`, `tests/test_experience_entrypoint.py` for whole-install doctor and upgrade preview UX;
- `tests/test_lkg_recovery.py`, `tests/test_recovery_orchestrator.py`, `tests/test_restore_cli.py` for Last-Known-Good and restore safety;
- `tests/test_infrastructure_upgrade_apply.py`, `tests/test_infrastructure_upgrade_recovery_edges.py` for explicit structural apply, stale-plan refusal, interruption/resume and final-health behavior;
- `tests/test_update_repeat_chain_acceptance.py` for repeated/skip update chain behavior;
- `tests/test_adapters.py` for adapter command routing;
- `tests/test_safe_infrastructure_transition_contract.py` for transition-contract compatibility.

OS separately owns Workspace generation and Workspace-to-personal capability promotion semantics. Skills separately owns the immutable managed `aiverse-skills` generation lifecycle. Slice 5.1 must not duplicate either owner implementation.

## Adaptive task list

- [ ] **5.1-T1** Freeze fresh System/Distribution/OS/Skills refs and inventory the existing focused coverage so the new gate tests composed invariants rather than duplicating single-slice tests.
- [ ] **5.1-T2** Add a dedicated Distribution Safe Infrastructure regression suite that composes read-only planning, normal update semantics, doctor fan-out truth, OPTIONAL/REQUIRED/BLOCKED gating, stale-plan refusal, idempotent apply/replay, retained recovery, destructive restore failure, and concise member-output invariants.
- [ ] **5.1-T3** Add cross-owner contract checks that pin the current OS and Skills owner refs/evidence and prove the present Workspace relocation decision, OS promotion identity semantics, managed Skills ownership boundary, and unsupported structural directions remain fail-closed without inventing migrations.
- [ ] **5.1-T4** Add explicit destructive-negative cases for losing/rotating the sole recovery point, mutating during previews, source drift, unsupported recipe/relocation, failed owner verification/final health, unsafe reference repair, restore-target destruction, credential/external-state overclaim, and injected mid-upgrade interruption.
- [ ] **5.1-T5** Add/extend a dedicated CI gate so the composed regression suite runs on the supported Distribution matrix and cannot silently disappear from normal qualification; keep existing broad gates and normal Distribution CI intact.
- [ ] **5.1-T6** Qualify unchanged OS and Skills owner-native gates at the frozen refs, then qualify the exact Distribution PR head and merged main; classify any unrelated broad-gate failure separately rather than weakening the Slice 5.1 acceptance authority.
- [ ] **5.1-T7** Record exact evidence and acceptance results in System, mark Slice 5.1 complete only after all composed and destructive-negative assertions are green, then stop before Slice 5.2.

## Protected boundaries

- Do not change `aiverse update` apply semantics.
- Do not make any preview path mutate state.
- Do not add a production structural migration merely to make a test mutate something.
- Do not duplicate OS Workspace/capability owner logic inside Distribution.
- Do not duplicate Skills generation ownership inside Distribution.
- Do not weaken LKG retention, recovery-required truth, identity-change semantics, reference-repair verification, or final whole-install health.
- Do not claim external effects or excluded credentials are restored when the recovery contract does not cover them.
- Do not start Slice 5.2 in this execution unit.

## Acceptance target

Slice 5.1 closes only if the composed gate proves at minimum:

- normal `aiverse update` retains shipped apply semantics;
- `update --plan`, doctor, upgrade preview and restore preview are read-only;
- doctor fan-out preserves owner-local truth and cannot convert an owner failure to aggregate PASS;
- OPTIONAL work is never hidden inside update;
- REQUIRED work blocks unsafe activation and remains explicit;
- BLOCKED/REVIEW and unsupported structural states preserve protected state;
- stale plans fail before owner mutation;
- repeated apply/update and skip-version chains remain safe;
- current unsupported Workspace relocation remains rejected without mutation;
- Workspace-to-personal promotion keeps identity-changing semantics and compatibility evidence rather than pretending continuity;
- user custom files survive admitted promotion/update/restore paths;
- the sole valid LKG cannot be lost during failed rotation or failed restore;
- restore replaces only declared covered scope and cannot destroy its retained target;
- secrets/credentials and external side effects remain truthfully excluded or separately handled;
- injected mid-upgrade failure remains recoverable;
- supported adapters converge on the same lifecycle commands;
- default member output stays understandable without internal paths, generations, IDs or migration terminology.

## NEXT

Implement 5.1 only after this start/task record is merged and green. No Slice 5.1 Distribution or owner product/test change is permitted before that point.
