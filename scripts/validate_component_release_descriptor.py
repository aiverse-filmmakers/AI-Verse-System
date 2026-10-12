#!/usr/bin/env python3
"""Validate AI-Verse Component Release Descriptor v1.

This is a specification/CI validator. It is not a runtime health, migration,
or release owner.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "ai-verse.component-release/v1"
INFRASTRUCTURE_CONTRACT = "ai-verse.infrastructure-upgrade/v1"
IDENTITY_CONTRACT = "ai-verse.durable-identity-reference/v1"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
COMPONENT_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
MACHINE_TOKEN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]*$")
RECIPE_ID = re.compile(r"^[a-z0-9][a-z0-9._/-]*$")
PLATFORMS = {"linux", "macos", "windows"}
RELEASE_STATUS = {"candidate", "accepted"}
SOURCE_TYPES = {"git", "npm", "pypi", "archive"}
MIGRATION_COMPATIBILITY = {"none-required", "compatible", "explicit-migration", "blocked"}
CHANGE_CLASSIFICATION = {"non-breaking", "breaking"}
CHECKPOINT_POLICIES = {"not-required", "owner-evidence-required", "unsupported"}
RECIPE_DISPOSITIONS = {"OPTIONAL", "REQUIRED"}
PATH_MODES = {"direct", "chain-step"}
LEGACY_RETIREMENT = {"after-postconditions", "not-applicable"}

TOP_LEVEL_KEYS = {
    "schema_version",
    "component_id",
    "version",
    "revision",
    "release_status",
    "package",
    "supported_platforms",
    "runtime_requirements",
    "lifecycle",
    "state",
    "migration",
    "authority",
    "evidence",
    "semantics",
}
LIFECYCLE_KEYS = {"install", "setup", "status", "doctor", "enable", "disable", "update", "uninstall"}
STATE_REQUIRED = {
    "canonical_state_owned",
    "preserve_on_update",
    "preserve_on_uninstall",
    "preserve_unknown_user_files",
}
AUTHORITY_KEYS = {
    "grants_permissions",
    "changes_direction_owner",
    "changes_scope",
    "enables_disabled_component",
    "exposes_remote_listener",
}
INFRASTRUCTURE_KEYS = {
    "contract_version",
    "owner",
    "current_generation",
    "no_match_disposition",
    "recipes",
}
RECIPE_KEYS = {
    "recipe_id",
    "recipe_version",
    "from_generations",
    "to_generation",
    "target_binding",
    "disposition",
    "detect_operation",
    "preconditions",
    "apply_operation",
    "verify_operation",
    "identity_contract",
    "identity_evidence_ref",
    "reference_repair",
    "postconditions",
    "recovery",
    "idempotent",
    "idempotency_evidence_kind",
    "path_mode",
    "legacy_retirement",
    "member_summary",
}


def _object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def _exact_keys(
    obj: dict[str, Any],
    expected: set[str],
    path: str,
    errors: list[str],
    *,
    optional: set[str] | None = None,
) -> None:
    optional = optional or set()
    missing = expected - set(obj)
    unknown = set(obj) - expected - optional
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"{path}: unknown keys: {', '.join(sorted(unknown))}")


def _bool(obj: dict[str, Any], key: str, path: str, errors: list[str]) -> bool | None:
    value = obj.get(key)
    if not isinstance(value, bool):
        errors.append(f"{path}.{key}: expected boolean")
        return None
    return value


def _machine_token(value: Any, path: str, errors: list[str]) -> str | None:
    if not isinstance(value, str) or not (2 <= len(value) <= 120) or not MACHINE_TOKEN.fullmatch(value):
        errors.append(f"{path}: expected machine identifier without whitespace or command syntax")
        return None
    return value


def _token_array(value: Any, path: str, errors: list[str], *, nonempty: bool = True) -> list[str]:
    if not isinstance(value, list) or (nonempty and not value):
        errors.append(f"{path}: expected {'non-empty ' if nonempty else ''}array of machine identifiers")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        token = _machine_token(item, f"{path}[{index}]", errors)
        if token is not None:
            result.append(token)
    if len(result) != len(set(result)):
        errors.append(f"{path}: duplicates are not allowed")
    return result


def _accepted_evidence_kinds(root: dict[str, Any]) -> set[str]:
    evidence = root.get("evidence")
    if not isinstance(evidence, dict):
        return set()
    acceptance = evidence.get("acceptance")
    if not isinstance(acceptance, list):
        return set()
    return {
        item.get("kind")
        for item in acceptance
        if isinstance(item, dict) and isinstance(item.get("kind"), str) and item.get("status") == "pass"
    }


def _validate_infrastructure(
    infrastructure: Any,
    *,
    component_id: Any,
    revision: Any,
    checkpoint_policy: Any,
    accepted_evidence_kinds: set[str],
    errors: list[str],
) -> None:
    path = "$.migration.infrastructure"
    infra = _object(infrastructure, path, errors)
    if not infra:
        return

    _exact_keys(infra, INFRASTRUCTURE_KEYS, path, errors)

    if infra.get("contract_version") != INFRASTRUCTURE_CONTRACT:
        errors.append(f"{path}.contract_version: expected {INFRASTRUCTURE_CONTRACT!r}")

    owner = infra.get("owner")
    if not isinstance(owner, str) or not (2 <= len(owner) <= 80) or not COMPONENT_ID.fullmatch(owner):
        errors.append(f"{path}.owner: invalid canonical component id")
    elif isinstance(component_id, str) and owner != component_id:
        errors.append(f"{path}.owner: must equal descriptor component_id")

    current_generation = _machine_token(infra.get("current_generation"), f"{path}.current_generation", errors)

    if infra.get("no_match_disposition") != "BLOCKED/REVIEW":
        errors.append(f"{path}.no_match_disposition: must be BLOCKED/REVIEW")

    recipes = infra.get("recipes")
    if not isinstance(recipes, list):
        errors.append(f"{path}.recipes: expected array")
        return

    if recipes and checkpoint_policy == "unsupported":
        errors.append(f"{path}: recipes cannot be published when checkpoint_policy is unsupported")

    seen_recipe_ids: set[str] = set()
    source_to_target: dict[str, str] = {}
    source_to_recipe: dict[str, str] = {}

    for index, recipe_value in enumerate(recipes):
        recipe_path = f"{path}.recipes[{index}]"
        recipe = _object(recipe_value, recipe_path, errors)
        if not recipe:
            continue
        _exact_keys(recipe, RECIPE_KEYS, recipe_path, errors)

        recipe_id = recipe.get("recipe_id")
        if not isinstance(recipe_id, str) or not (2 <= len(recipe_id) <= 120) or not RECIPE_ID.fullmatch(recipe_id):
            errors.append(f"{recipe_path}.recipe_id: invalid recipe id")
            recipe_id = f"<invalid-{index}>"
        elif recipe_id in seen_recipe_ids:
            errors.append(f"{recipe_path}.recipe_id: duplicate recipe id {recipe_id!r}")
        else:
            seen_recipe_ids.add(recipe_id)

        recipe_version = recipe.get("recipe_version")
        if not isinstance(recipe_version, str) or not (1 <= len(recipe_version) <= 40):
            errors.append(f"{recipe_path}.recipe_version: expected non-empty version string")

        from_generations = _token_array(recipe.get("from_generations"), f"{recipe_path}.from_generations", errors)
        to_generation = _machine_token(recipe.get("to_generation"), f"{recipe_path}.to_generation", errors)

        if current_generation is not None and current_generation in from_generations:
            errors.append(f"{recipe_path}.from_generations: current_generation cannot be a migration source")
        if to_generation is not None and to_generation in from_generations:
            errors.append(f"{recipe_path}: source and target generation cannot be identical")

        for source in from_generations:
            if source in source_to_target:
                errors.append(
                    f"{recipe_path}.from_generations: source {source!r} is already claimed by recipe {source_to_recipe[source]!r}; ambiguous paths are forbidden"
                )
            elif to_generation is not None:
                source_to_target[source] = to_generation
                source_to_recipe[source] = recipe_id

        target_binding = _object(recipe.get("target_binding"), f"{recipe_path}.target_binding", errors)
        if target_binding:
            _exact_keys(target_binding, {"component_revision"}, f"{recipe_path}.target_binding", errors)
            bound_revision = target_binding.get("component_revision")
            if not isinstance(bound_revision, str) or not SHA40.fullmatch(bound_revision):
                errors.append(f"{recipe_path}.target_binding.component_revision: expected exact lowercase 40-character Git SHA")
            elif isinstance(revision, str) and bound_revision != revision:
                errors.append(f"{recipe_path}.target_binding.component_revision: must equal descriptor revision")

        if recipe.get("disposition") not in RECIPE_DISPOSITIONS:
            errors.append(f"{recipe_path}.disposition: expected OPTIONAL or REQUIRED")

        for operation_key in ("detect_operation", "apply_operation", "verify_operation"):
            _machine_token(recipe.get(operation_key), f"{recipe_path}.{operation_key}", errors)

        _token_array(recipe.get("preconditions"), f"{recipe_path}.preconditions", errors)

        if recipe.get("identity_contract") != IDENTITY_CONTRACT:
            errors.append(f"{recipe_path}.identity_contract: expected {IDENTITY_CONTRACT!r}")
        _machine_token(recipe.get("identity_evidence_ref"), f"{recipe_path}.identity_evidence_ref", errors)

        repair = _object(recipe.get("reference_repair"), f"{recipe_path}.reference_repair", errors)
        if repair:
            _exact_keys(repair, {"required", "operations"}, f"{recipe_path}.reference_repair", errors)
            repair_required = _bool(repair, "required", f"{recipe_path}.reference_repair", errors)
            operations = repair.get("operations")
            if not isinstance(operations, list):
                errors.append(f"{recipe_path}.reference_repair.operations: expected array")
                operations = []
            if repair_required is True and not operations:
                errors.append(f"{recipe_path}.reference_repair.operations: required repair needs at least one owner operation")
            if repair_required is False and operations:
                errors.append(f"{recipe_path}.reference_repair.operations: must be empty when repair is not required")
            seen_operations: set[tuple[str, str]] = set()
            for operation_index, operation_value in enumerate(operations):
                operation_path = f"{recipe_path}.reference_repair.operations[{operation_index}]"
                operation = _object(operation_value, operation_path, errors)
                if not operation:
                    continue
                _exact_keys(operation, {"owner", "operation"}, operation_path, errors)
                operation_owner = operation.get("owner")
                if not isinstance(operation_owner, str) or not (2 <= len(operation_owner) <= 80) or not COMPONENT_ID.fullmatch(operation_owner):
                    errors.append(f"{operation_path}.owner: invalid canonical component id")
                operation_id = _machine_token(operation.get("operation"), f"{operation_path}.operation", errors)
                if isinstance(operation_owner, str) and operation_id is not None:
                    pair = (operation_owner, operation_id)
                    if pair in seen_operations:
                        errors.append(f"{operation_path}: duplicate owner repair operation")
                    seen_operations.add(pair)

        _token_array(recipe.get("postconditions"), f"{recipe_path}.postconditions", errors)

        recovery = _object(recipe.get("recovery"), f"{recipe_path}.recovery", errors)
        if recovery:
            _exact_keys(recovery, {"whole_install_lkg_required", "owner_checkpoint_required"}, f"{recipe_path}.recovery", errors)
            lkg = _bool(recovery, "whole_install_lkg_required", f"{recipe_path}.recovery", errors)
            if lkg is False:
                errors.append(f"{recipe_path}.recovery.whole_install_lkg_required: must be true")
            owner_checkpoint_required = _bool(recovery, "owner_checkpoint_required", f"{recipe_path}.recovery", errors)
            if owner_checkpoint_required is True and checkpoint_policy != "owner-evidence-required":
                errors.append(
                    f"{recipe_path}.recovery.owner_checkpoint_required: descriptor checkpoint_policy must be owner-evidence-required"
                )

        idempotent = _bool(recipe, "idempotent", recipe_path, errors)
        if idempotent is False:
            errors.append(f"{recipe_path}.idempotent: must be true")

        idempotency_kind = recipe.get("idempotency_evidence_kind")
        if not isinstance(idempotency_kind, str) or not (1 <= len(idempotency_kind) <= 80):
            errors.append(f"{recipe_path}.idempotency_evidence_kind: expected non-empty evidence kind")
        elif idempotency_kind not in accepted_evidence_kinds:
            errors.append(
                f"{recipe_path}.idempotency_evidence_kind: must name passing descriptor acceptance evidence"
            )

        path_mode = recipe.get("path_mode")
        if path_mode not in PATH_MODES:
            errors.append(f"{recipe_path}.path_mode: expected direct or chain-step")
        elif path_mode == "direct" and current_generation is not None and to_generation != current_generation:
            errors.append(f"{recipe_path}.path_mode: direct recipe must target current_generation")

        if recipe.get("legacy_retirement") not in LEGACY_RETIREMENT:
            errors.append(f"{recipe_path}.legacy_retirement: invalid value")

        member_summary = recipe.get("member_summary")
        if not isinstance(member_summary, str) or not (1 <= len(member_summary.strip()) <= 240):
            errors.append(f"{recipe_path}.member_summary: expected concise non-empty text up to 240 characters")

    if recipes and current_generation is not None:
        if not any(isinstance(recipe, dict) and recipe.get("to_generation") == current_generation for recipe in recipes):
            errors.append(f"{path}.recipes: at least one recipe must reach current_generation")

        for source in sorted(source_to_target):
            seen: set[str] = set()
            generation = source
            while generation != current_generation:
                if generation in seen:
                    errors.append(f"{path}.recipes: migration chain cycle detected from source {source!r}")
                    break
                seen.add(generation)
                target = source_to_target.get(generation)
                if target is None:
                    errors.append(
                        f"{path}.recipes: source {source!r} does not have a complete unique chain to current_generation"
                    )
                    break
                generation = target


def validate_descriptor(data: Any) -> list[str]:
    errors: list[str] = []
    root = _object(data, "$", errors)
    if not root:
        return errors

    _exact_keys(root, TOP_LEVEL_KEYS, "$", errors)

    if root.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"$.schema_version: expected {SCHEMA_VERSION!r}")

    component_id = root.get("component_id")
    if not isinstance(component_id, str) or not (2 <= len(component_id) <= 80) or not COMPONENT_ID.fullmatch(component_id):
        errors.append("$.component_id: invalid canonical component id")

    version = root.get("version")
    if not isinstance(version, str) or not (1 <= len(version) <= 80):
        errors.append("$.version: expected non-empty version string")

    revision = root.get("revision")
    if not isinstance(revision, str) or not SHA40.fullmatch(revision):
        errors.append("$.revision: expected exact lowercase 40-character Git SHA")

    if root.get("release_status") not in RELEASE_STATUS:
        errors.append("$.release_status: expected candidate or accepted")

    package = _object(root.get("package"), "$.package", errors)
    if package:
        _exact_keys(package, {"repository", "source_type"}, "$.package", errors, optional={"package_name", "integrity"})
        repository = package.get("repository")
        if not isinstance(repository, str) or not REPOSITORY.fullmatch(repository):
            errors.append("$.package.repository: expected owner/repository")
        if package.get("source_type") not in SOURCE_TYPES:
            errors.append("$.package.source_type: unsupported source type")
        for key in ("package_name", "integrity"):
            if key in package and package[key] is not None and not isinstance(package[key], str):
                errors.append(f"$.package.{key}: expected string or null")

    platforms = root.get("supported_platforms")
    if not isinstance(platforms, list) or not platforms:
        errors.append("$.supported_platforms: expected non-empty array")
    else:
        if any(p not in PLATFORMS for p in platforms):
            errors.append("$.supported_platforms: contains unsupported platform")
        if len(platforms) != len(set(platforms)):
            errors.append("$.supported_platforms: duplicates are not allowed")

    runtime = _object(root.get("runtime_requirements"), "$.runtime_requirements", errors)
    if runtime:
        _exact_keys(runtime, {"python", "node", "other"}, "$.runtime_requirements", errors)
        for key in ("python", "node"):
            if runtime.get(key) is not None and not isinstance(runtime.get(key), str):
                errors.append(f"$.runtime_requirements.{key}: expected string or null")
        other = runtime.get("other")
        if not isinstance(other, list) or any(not isinstance(x, str) or not x for x in other):
            errors.append("$.runtime_requirements.other: expected array of non-empty strings")
        elif len(other) != len(set(other)):
            errors.append("$.runtime_requirements.other: duplicates are not allowed")

    lifecycle = _object(root.get("lifecycle"), "$.lifecycle", errors)
    if lifecycle:
        _exact_keys(lifecycle, LIFECYCLE_KEYS, "$.lifecycle", errors)
        for key in LIFECYCLE_KEYS:
            _bool(lifecycle, key, "$.lifecycle", errors)

    state = _object(root.get("state"), "$.state", errors)
    if state:
        _exact_keys(state, STATE_REQUIRED, "$.state", errors, optional={"state_format"})
        _bool(state, "canonical_state_owned", "$.state", errors)
        for key in ("preserve_on_update", "preserve_on_uninstall", "preserve_unknown_user_files"):
            value = _bool(state, key, "$.state", errors)
            if value is False:
                errors.append(f"$.state.{key}: must be true for safe-update v1")
        if "state_format" in state and state["state_format"] is not None and not isinstance(state["state_format"], str):
            errors.append("$.state.state_format: expected string or null")

    migration = _object(root.get("migration"), "$.migration", errors)
    if migration:
        _exact_keys(
            migration,
            {
                "compatibility",
                "change_classification",
                "from_versions",
                "requires_explicit_migration",
                "owner_controlled",
                "checkpoint_policy",
            },
            "$.migration",
            errors,
            optional={"infrastructure"},
        )
        compatibility = migration.get("compatibility")
        if compatibility not in MIGRATION_COMPATIBILITY:
            errors.append("$.migration.compatibility: invalid value")
        change_classification = migration.get("change_classification")
        if change_classification not in CHANGE_CLASSIFICATION:
            errors.append("$.migration.change_classification: expected non-breaking or breaking")
        from_versions = migration.get("from_versions")
        if not isinstance(from_versions, list) or any(not isinstance(v, str) or not v for v in from_versions):
            errors.append("$.migration.from_versions: expected array of non-empty version strings")
        elif len(from_versions) != len(set(from_versions)):
            errors.append("$.migration.from_versions: duplicates are not allowed")
        explicit = _bool(migration, "requires_explicit_migration", "$.migration", errors)
        owner_controlled = _bool(migration, "owner_controlled", "$.migration", errors)
        if owner_controlled is False:
            errors.append("$.migration.owner_controlled: must be true")
        checkpoint_policy = migration.get("checkpoint_policy")
        if checkpoint_policy not in CHECKPOINT_POLICIES:
            errors.append("$.migration.checkpoint_policy: invalid value")
        if compatibility == "explicit-migration" and explicit is not True:
            errors.append("$.migration: explicit-migration requires requires_explicit_migration=true")
        if compatibility in {"none-required", "compatible", "blocked"} and explicit is True:
            errors.append("$.migration: requires_explicit_migration must be false unless compatibility is explicit-migration")
        if compatibility == "none-required" and isinstance(from_versions, list) and from_versions:
            errors.append("$.migration: none-required must not declare from_versions")
        if compatibility == "blocked" and root.get("release_status") == "accepted":
            errors.append("$.migration: blocked descriptor cannot have release_status=accepted")
        if change_classification == "breaking":
            if compatibility not in {"explicit-migration", "blocked"}:
                errors.append("$.migration: breaking change must use explicit-migration or blocked compatibility")
            if not isinstance(from_versions, list) or not from_versions:
                errors.append("$.migration: breaking change must declare at least one from_version")
        if "infrastructure" in migration:
            _validate_infrastructure(
                migration.get("infrastructure"),
                component_id=component_id,
                revision=revision,
                checkpoint_policy=checkpoint_policy,
                accepted_evidence_kinds=_accepted_evidence_kinds(root),
                errors=errors,
            )

    authority = _object(root.get("authority"), "$.authority", errors)
    if authority:
        _exact_keys(authority, AUTHORITY_KEYS, "$.authority", errors)
        for key in AUTHORITY_KEYS:
            value = _bool(authority, key, "$.authority", errors)
            if value is True:
                errors.append(f"$.authority.{key}: must be false for normal update train")

    evidence = _object(root.get("evidence"), "$.evidence", errors)
    if evidence:
        _exact_keys(evidence, {"ci", "acceptance"}, "$.evidence", errors)
        for group in ("ci", "acceptance"):
            items = evidence.get(group)
            if not isinstance(items, list) or not items:
                errors.append(f"$.evidence.{group}: expected non-empty evidence array")
                continue
            for index, item in enumerate(items):
                path = f"$.evidence.{group}[{index}]"
                item_obj = _object(item, path, errors)
                if not item_obj:
                    continue
                _exact_keys(item_obj, {"kind", "status", "revision"}, path, errors, optional={"run_id", "url"})
                if not isinstance(item_obj.get("kind"), str) or not item_obj.get("kind"):
                    errors.append(f"{path}.kind: expected non-empty string")
                if item_obj.get("status") != "pass":
                    errors.append(f"{path}.status: publishable evidence must be pass")
                ev_revision = item_obj.get("revision")
                if not isinstance(ev_revision, str) or not SHA40.fullmatch(ev_revision):
                    errors.append(f"{path}.revision: expected exact lowercase 40-character Git SHA")
                elif isinstance(revision, str) and ev_revision != revision:
                    errors.append(f"{path}.revision: must equal descriptor revision")
                if "run_id" in item_obj and item_obj["run_id"] is not None and not isinstance(item_obj["run_id"], (str, int)):
                    errors.append(f"{path}.run_id: expected string, integer, or null")
                if "url" in item_obj and item_obj["url"] is not None and not isinstance(item_obj["url"], str):
                    errors.append(f"{path}.url: expected string or null")

    semantics = _object(root.get("semantics"), "$.semantics", errors)
    if semantics:
        _exact_keys(semantics, {"release_metadata_only", "live_health_truth"}, "$.semantics", errors)
        if semantics.get("release_metadata_only") is not True:
            errors.append("$.semantics.release_metadata_only: must be true")
        if semantics.get("live_health_truth") is not False:
            errors.append("$.semantics.live_health_truth: must be false")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("descriptor", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.descriptor.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate_descriptor(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VALID {data['component_id']} {data['version']} {data['revision']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())