# AI-Verse Infrastructure Generation and Upgrade Recipe Contract

**Status:** Canonical contract for Safe Infrastructure Slice 2.2  
**Contract ID:** `ai-verse.infrastructure-upgrade/v1`  
**Owner:** AI-Verse System for shared law; component owners for every published recipe  
**Carrier:** optional `migration.infrastructure` inside `ai-verse.component-release/v1`

## 1. Purpose

This contract defines the minimum machine-readable metadata a component owner must publish when an admitted AI-Verse release can detect or apply a structural/infrastructure migration.

It does not create a second release catalog, a global migration registry, a central identity registry, or a generic AI migration engine. The canonical carrier remains the existing component release descriptor. Components with no real structural migration responsibility do not publish this block.

## 2. Core law

Structural mutation is owner-controlled and evidence-bound.

Distribution may discover, plan, checkpoint, sequence, invoke, verify and report a recipe. Distribution may not invent the migration, convert prose into mutation steps, substitute shell/file operations for an owner handler, or infer an unsupported path from similarity.

If no unique admitted path exists, the result is `BLOCKED/REVIEW` and no structural mutation occurs.

## 3. Descriptor placement

A component release descriptor may add:

```json
{
  "migration": {
    "infrastructure": {
      "contract_version": "ai-verse.infrastructure-upgrade/v1",
      "owner": "ai-verse-os",
      "current_generation": "workspace-layout/v2",
      "no_match_disposition": "BLOCKED/REVIEW",
      "recipes": []
    }
  }
}
```

The block is optional. Its absence means the descriptor does not publish shared structural-upgrade recipes. Absence is not permission for Distribution or an agent to guess one.

`owner` must equal the descriptor's canonical `component_id`.

## 4. Infrastructure generations

`current_generation` is an owner-controlled machine identifier for the structural state expected by that component revision.

Generation identifiers:

- are not member-facing names;
- do not replace durable entity IDs;
- do not imply filesystem identity;
- do not grant ownership of another component's state;
- are interpreted only by the canonical owner.

Version 1 deliberately accepts explicit finite source-generation sets rather than free-form opaque ranges. This prevents an orchestrator from having to guess ordering or comparison semantics for owner-defined generation strings.

## 5. Recipe identity and target binding

Every recipe has a stable `recipe_id` plus `recipe_version`.

Every recipe carries `target_binding.component_revision`, which must equal the exact immutable `revision` of the enclosing component release descriptor. The admitted AI-Verse release set that contains that component revision provides the exact System release binding.

A recipe therefore cannot silently float to a later component revision or release.

## 6. Source and target path semantics

Each recipe declares:

- `from_generations`: explicit accepted source generations;
- `to_generation`: the exact generation produced by that recipe;
- `path_mode`: `direct` or `chain-step`.

A `direct` recipe must terminate at the descriptor's `current_generation`.

A `chain-step` recipe may terminate at an intermediate generation or at `current_generation`. A planner may compose chain steps only when the output generation of one step exactly matches an admitted source generation of the next step and the resulting path is unique.

Multiple valid paths, cycles, missing links, unrecognized generations or stale detection evidence are `BLOCKED/REVIEW`. AI reasoning must not choose among ambiguous mutation paths.

## 7. Disposition

Every executable recipe declares exactly one disposition:

- `OPTIONAL`: current installation remains supported and the structural improvement requires explicit apply intent;
- `REQUIRED`: target software cannot safely activate or remain supported without the admitted structural migration.

`BLOCKED/REVIEW` is not an executable recipe disposition. It is the mandatory result when no uniquely admitted recipe can safely handle the detected state.

A normal `aiverse update` never silently applies an `OPTIONAL` recipe.

## 8. Owner lifecycle operations

Recipes contain opaque machine operation identifiers, not commands:

- `detect_operation`;
- `apply_operation`;
- `verify_operation`.

These identifiers resolve only through the canonical owner's admitted lifecycle surface.

They are not shell commands, executable paths, scripts supplied by Distribution, or free-form AI instructions. The shared contract intentionally has no field for arbitrary command text.

`preconditions` and `postconditions` are owner-defined machine condition identifiers. They provide deterministic evidence hooks without moving domain logic into Distribution.

## 9. Identity law

Every recipe imports the canonical shared identity contract:

`ai-verse.durable-identity-reference/v1`

The recipe also supplies `identity_evidence_ref`, an owner-published evidence/contract reference describing the identity guarantee for that migration.

This contract does not redefine whether a Workspace path move preserves Workspace identity or whether a capability provider transfer changes qualified identity. Those decisions remain with the canonical identity and component-owner contracts.

Missing, conflicting or unsupported identity evidence blocks apply.

## 10. Reference repair

Every recipe declares a `reference_repair` object.

When repair is required, every repair operation names:

- the canonical owner responsible for the reference domain;
- that owner's lifecycle `operation` identifier.

Distribution may sequence those owner operations. It may not directly rewrite another owner's durable reference.

A recipe cannot complete successfully while a required reference repair remains unverified.

## 11. Recovery

Every recipe declares:

```json
{
  "recovery": {
    "whole_install_lkg_required": true,
    "owner_checkpoint_required": true
  }
}
```

`whole_install_lkg_required` is always true under Safe Infrastructure v1. A structural apply may not start until the Slice 2.1 Last-Known-Good guarantee is satisfied.

If `owner_checkpoint_required` is true, the enclosing component descriptor must use `migration.checkpoint_policy = "owner-evidence-required"`.

Owner-native transaction checkpoints and the Distribution whole-install LKG remain separate layers.

## 12. Idempotency

Every recipe must declare `idempotent: true` and name `idempotency_evidence_kind`.

That evidence kind must be present in the enclosing descriptor's accepted evidence. A recipe that cannot prove idempotency is not publishable under this contract.

Applying a recipe twice must not duplicate content, repeat destructive moves, mint replacement identity accidentally, or re-run legacy retirement destructively.

## 13. Legacy retirement

`legacy_retirement` is one of:

- `after-postconditions`: old writable infrastructure may retire only after target verification and required reference repair succeed;
- `not-applicable`: no writable legacy route is retired by the recipe.

Cleanup can never precede proof.

## 14. Member summary

`member_summary` is concise plain-English text suitable for a preview such as:

> Improve this setup to the current project structure.

The default member experience must not require generation IDs, recipe IDs, repository paths, hashes or handler names. Technical identifiers remain available in detailed/JSON evidence.

## 15. Planning algorithm

A conforming planner must:

1. read the admitted target release and exact component descriptor;
2. invoke the owner detector without mutation;
3. obtain the exact source generation and source evidence;
4. select only recipes whose explicit source set contains that generation and whose target binding matches the exact descriptor revision;
5. resolve either one direct recipe or one unique exact chain to `current_generation`;
6. verify disposition, preconditions, identity evidence, reference-repair obligations, recovery requirements and idempotency evidence;
7. return `OPTIONAL`, `REQUIRED` or `BLOCKED/REVIEW`;
8. keep preview read-only;
9. on explicit apply, revalidate the source evidence immediately before mutation;
10. invoke owner operations in dependency-safe order and verify every postcondition before legacy retirement or success.

No step permits free-form AI inference to create a missing mutation path.

## 16. Relationship to later slices

Slice 2.2 defines and validates only this shared metadata contract.

Later slices may:

- add OS-owned Workspace generation/recipes only if a real migration is required;
- add OS/Skills capability placement/promotion recipes according to canonical scope ownership;
- teach Distribution to aggregate/plan/apply admitted recipes;
- qualify direct and chained migrations, stale-plan refusal, idempotency and destructive-negative behavior.

Those later implementations must consume this contract rather than creating sibling recipe formats.