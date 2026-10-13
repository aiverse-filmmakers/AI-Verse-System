# Safe Infrastructure Slice 4.4 - Upgrade Apply Orchestration, Resume and Verification

**Status:** IN PROGRESS  
**Canonical slice:** 4.4  
**Outcome:** implement explicit `aiverse upgrade --apply` orchestration by extending the shipped Distribution lifecycle engine, while keeping owner migration logic behind admitted owner lifecycle operations.

## Refreshed starting refs

Refreshed before Slice 4.4 product implementation:

- `aiverse-filmmakers/AI-Verse-System@64717ca18123c333ebc64fd0a1412329ad13618a`
- `aiverse-filmmakers/ai-verse-distribution@15e03219185f484cbbc4c5887d967ddc5630d1a6`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

System main advanced after the Safe Infrastructure 4.3 closure because another canonical program was updating independent roadmap/governance files. The Safe Infrastructure roadmap itself still reads `SLICE 4.3 COMPLETE`, 14/18 complete, 77.8%, with Slice 4.4 as the only next Safe Infrastructure execution unit.

## Canonical acceptance target

Slice 4.4 must prove all of the following before closure:

- exact upgrade plan is revalidated against source state immediately before apply;
- Last-Known-Good is secured before owner mutation;
- admitted owner handlers execute in dependency-safe order;
- partial failure is resumable/recoverable/truthful;
- canonical Identity Hardening conditions are revalidated;
- required reference repairs and postconditions are verified;
- failed upgrade never reports success;
- restore remains available after upgrade;
- OPTIONAL upgrades require explicit apply intent;
- REQUIRED upgrades remain explicit and separate from normal software update;
- completion output explains practical improvement, preservation and health without migration jargon.

## Inventory and implementation boundary

### Distribution substrate to REUSE/EXTEND

- `ExperienceOrchestrator.upgrade_plan()` already provides the read-only whole-install structural preview and exact admitted-release selection.
- `InfrastructureUpdateGate` already validates exact component descriptors, owner infrastructure metadata, unique recipe path, OPTIONAL / REQUIRED / BLOCKED disposition, identity contract reference, reference-repair declarations, LKG requirement and idempotency evidence.
- `StateStore.lifecycle_transaction()` already provides the cross-process lifecycle lock and receipt generation boundary.
- `StateStore.begin_effect()` / `commit_effect()` already provide crash-visible pending owner-effect ownership and exact-operation resume semantics.
- `RecoveryOrchestrator.ensure_last_known_good()` already provides the verified rotating whole-install Last-Known-Good guard before mutation.
- `RecoveryOrchestrator.restore()` already preserves the retained LKG target after unrelated later local mutations.
- internal `doctor()` and `require_final_health()` already provide the shipped final-health authority and must not be replaced by member overview formatting.

### Canonical owner logic to REUSE, not duplicate

Phase 3 proved current owner behavior:

- Workspace physical relocation is not currently admitted. `workspaces/<workspace-id>` remains the canonical OS slot, so Slice 4.4 must not manufacture a Workspace move recipe.
- OS owns the admitted Workspace-to-personal capability promotion transaction. Its native `plan-promotion` / `apply-promotion` flow revalidates source generation/digest, stages and verifies the target, preserves source history, records explicit identity change (`qualified_identity_preserved: false`) and exposes validated compatibility repair for the retired qualified ID.
- Skills continues to own only the managed `aiverse-skills` immutable-generation lifecycle. No managed Skills structural migration defect is currently admitted.

The shared infrastructure contract intentionally carries opaque `detect_operation`, `apply_operation`, `verify_operation`, owner pre/postconditions and owner reference-repair operation IDs. Distribution may sequence/invoke those IDs but may not translate them into file operations or free-form shell commands.

### Current admitted release reality

The currently admitted Core OS and Skills descriptors do **not** publish `migration.infrastructure`. Therefore the real current member installation has no structural recipe to apply and `aiverse upgrade --apply` must truthfully return a healthy no-op for that release.

Slice 4.4 will implement the generic orchestration path and qualify executable behavior using exact admitted synthetic release/owner fixtures around the real Distribution contracts. It will not invent a production migration or rewrite current owner release descriptors merely to force a live mutation.

## Final adaptive task list

- [ ] **4.4-T1** Freeze refreshed refs and the real owner/transaction inventory above before any Slice 4.4 product implementation; classify current production no-recipe behavior and reject invented Workspace/Skills migrations.
- [ ] **4.4-T2** Extend the infrastructure plan evidence so an apply can be bound deterministically to the exact admitted release, component, source detection evidence and exact recipe path, while keeping preview read-only and owner operation IDs opaque.
- [ ] **4.4-T3** Implement explicit `upgrade --apply` orchestration in Distribution: acquire the existing lifecycle transaction, recover/resume only the exact pending upgrade operation, re-plan immediately before mutation, secure LKG first, then invoke admitted owner operations in deterministic component/recipe/reference-repair order through a trusted owner lifecycle executor.
- [ ] **4.4-T4** Verify owner preconditions, identity/reference evidence, repair results, recipe postconditions and final whole-install health before success; persist truthful completion/resume evidence without changing the installed software release receipt or hiding REQUIRED work inside normal update.
- [ ] **4.4-T5** Keep default member output concise and non-technical for no-op, success, stale-plan/refusal and recovery-required cases while retaining full machine-readable evidence under `--json`; preserve existing `doctor --component`, update and restore semantics.
- [ ] **4.4-T6** Add focused positive and destructive-negative coverage for: current no-recipe no-op, explicit OPTIONAL apply, REQUIRED explicit apply, stale source re-plan refusal, LKG-before-mutation ordering, dependency-safe chain execution, required reference repair, identity/postcondition failure, injected mid-upgrade interruption with exact resume, failed final health, idempotent replay and retained restore availability.
- [ ] **4.4-T7** Qualify the exact Distribution PR head and exact merged main across the full Distribution CI matrix; then record exact evidence, update canonical Safe Infrastructure counters/roadmap, close Phase 4 at 4/4 and stop before Phase 5 / Slice 5.1.

## Protected boundaries

- Do not add `update --apply`; shipped `aiverse update` semantics remain unchanged.
- Do not auto-apply OPTIONAL structural work during software update.
- Do not run free-form commands from descriptor metadata.
- Do not make Distribution own Workspace layout, capability identity or managed Skills generation semantics.
- Do not claim identity continuity across Workspace -> personal capability promotion.
- Do not clear or bypass a pending lifecycle owner effect except through the exact matching resume path.
- Do not rotate/destroy the retained LKG after owner mutation merely to make the upgraded state the recovery target.
- Do not report success if any required owner verification, reference repair or final health check fails.

## NEXT

Complete 4.4-T1 through 4.4-T7 only. Do not start Safe Infrastructure Slice 5.1 in this execution unit.
