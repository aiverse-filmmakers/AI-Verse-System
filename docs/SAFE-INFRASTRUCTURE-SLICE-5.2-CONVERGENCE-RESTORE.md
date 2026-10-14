# Safe Infrastructure Slice 5.2 - Real Convergence and Restore Qualification

**Status:** IN PROGRESS  
**Canonical slice:** 5.2  
**Outcome:** prove a real admitted older Core installation can converge toward the current architecture, exercise real owner-defined capability promotion where mutation is admitted, and restore exactly covered state from the retained Last-Known-Good recovery point without inventing unsupported Workspace relocation.

## Refreshed starting refs

Frozen before any Slice 5.2 implementation write:

- `aiverse-filmmakers/AI-Verse-System@69ea1553f8545350a0ab54211ed22e1ba8844b61`
- `aiverse-filmmakers/ai-verse-distribution@1f4559d88966e2a2ff26ca563d7a035ebc69a90b`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

No Safe Infrastructure drift occurred after Slice 5.1.

## Real fixture inventory

The implementation route is derived from shipped history rather than invented migration state:

- Distribution `core_lineage.json` retains real released Core history anchored at `core-public-beta-2026-09-13` and identifies `core-stable-2026-10-10` as a real released predecessor.
- The current explicit transition contract admits the real non-noop software transition `core-stable-2026-10-10` -> `core-first-run-rc1-2026-10-12`, backed by `real-and-synthetic-populated-os-only-preservation` evidence. Slice 5.2 must use this admitted route rather than broadening transition authority to older September releases without evidence.
- Existing `PopulatedCoreFixture` coverage provides realistic member state including profile/Brain/Memory data, multiple Workspaces, custom files, local and Workspace skills, SQLite data, connections, automations and Distribution history. Slice 5.2 will bind that realistic state to the real admitted release transition rather than treating a purely synthetic release pair as sufficient.
- OS owner-native Workspace infrastructure tests preserve the real historical domain-first/nested drift example `workspaces/YouTube/channel-a/WORKSPACE.yaml`. Current owner truth intentionally classifies it `BLOCKED/REVIEW`, reports nested/invalid slot findings and does not relocate it. No production Workspace relocation recipe is admitted, so Slice 5.2 must prove safe refusal and preservation instead of inventing a physical move.
- OS owner-native capability promotion is a real admitted mutation: Workspace-local capability -> personal/local provider. It preserves content/provenance/history, intentionally changes qualified identity, creates a compatibility mapping, retires the live Workspace source only after verification, supports stale-plan refusal and idempotent replay, and keeps custom user files.
- Current Distribution structural orchestration intentionally has no production trusted owner detector/executor adapter. This was correct while admitted release descriptors published no `migration.infrastructure`. Slice 5.2 may add only a narrow trusted adapter required to invoke an already owner-defined operation; it must not reproduce owner mutation logic inside Distribution.

## Adaptive task list

- [ ] **5.2-T1** Freeze the real historical/current fixture set and exact owner contracts: real admitted Core software transition, historical Workspace nested-layout drift, current direct Workspace contract, Workspace-to-personal capability promotion, LKG/restore coverage and supported runtime adapter commands.
- [ ] **5.2-T2** Build one realistic historical populated Core fixture bound to the real `core-stable-2026-10-10` -> `core-first-run-rc1-2026-10-12` transition and prove software update preserves member-owned state while reaching the admitted target.
- [ ] **5.2-T3** Prove Workspace convergence truth without inventing migration: current/fresh `workspaces/<id>` fixtures converge on the same owner contract, while the real nested historical drift produces one plain-English review recommendation, remains read-only through doctor/upgrade preview and is preserved unchanged because no relocation recipe is admitted.
- [ ] **5.2-T4** Exercise the real OS Workspace-to-personal capability promotion through a narrow trusted owner boundary: practical preview/recommendation, explicit apply, intentional qualified-identity change, provenance/history/custom-file preservation, compatibility/reference verification, consumer resolution from another Workspace, stale-plan refusal and idempotent replay. If Distribution requires an adapter, implement only command/result translation to the owner CLI and never duplicate owner logic.
- [ ] **5.2-T5** Compose the real software update plus admitted owner mutation with Last-Known-Good: retain the pre-action recovery point, perform the admitted changes, add realistic covered local changes, prove restore preview is read-only, apply restore, and verify exactly covered state reproduces the retained point while excluded external/credential state is not falsely claimed restored.
- [ ] **5.2-T6** Prove fresh-versus-upgraded convergence and runtime convergence: package-owned/generated/migratable current contracts match between a fresh current fixture and the upgraded historical fixture, durable identities/user state follow owner policy, and Claude/Codex/Gateway-compatible lifecycle requests resolve to the same update/doctor/upgrade/restore commands without internal IDs or paths.
- [ ] **5.2-T7** Qualify exact owner-native evidence plus exact Distribution PR head and merged main on the supported matrix, record acceptance evidence in System, mark Slice 5.2 complete only if convergence/restore/doctor/runtime/identity invariants pass, then stop before Slice 5.3.

## Protected boundaries

- Do not invent a production Workspace relocation recipe while the OS owner declares nested historical layout review-only.
- Do not broaden Core update transitions beyond existing evidence merely to create an older fixture.
- Do not duplicate OS capability promotion implementation in Distribution.
- Do not treat capability promotion as identity-preserving: `workspace:<workspace>:<name>` -> `local:<name>` is an intentional identity change with compatibility evidence.
- Do not mutate on doctor, update planning, upgrade preview or restore preview.
- Do not overwrite unknown/custom member files or lose Workspace assets/outputs.
- Do not rotate away the sole valid LKG before the next mutation is qualified.
- Do not claim credentials or external effects are restored unless the recovery contract explicitly covers them.
- Do not start Slice 5.3 in this execution unit.

## Acceptance target

Slice 5.2 closes only if:

- the real admitted older Core transition executes with realistic populated state and preserves member-owned state;
- current/fresh and upgraded historical fixtures satisfy the same current package-owned/generated contracts where convergence is supported;
- unsupported historical Workspace relocation is surfaced clearly and remains non-mutating;
- real owner-defined capability promotion succeeds only through explicit apply and retains truthful identity-change/reference evidence;
- another Workspace can consume the promoted capability through the compatibility mapping;
- a pre-action Last-Known-Good survives update/promotion and restore reproduces exactly the declared covered state;
- restore preview is truthful and read-only and failed/unsupported operations do not destroy the retained target;
- doctor aggregation remains truthful;
- supported runtime adapters converge on the same lifecycle commands;
- member-facing output remains concise, plain-English and free of internal paths, generations, release IDs and migration jargon.

## NEXT

Implement Slice 5.2 only after this start/task record is merged and Contract Validation is green. No Slice 5.2 product/test write is permitted before that point.
