#!/usr/bin/env python3
"""Validate the AI-Verse Repository Registry v1.

This validator protects static repository identity/ownership semantics. It does not
read or infer dynamic Repository State, live HEADs, CI outcomes, release pins, or
drift.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "ai-verse.repository-registry/v1"
REGISTRY_ID = "ai-verse.repository-network"
REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
COMPONENT_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LIFECYCLES = {"active", "experimental", "retired", "external"}
RELEASE_PROFILES = {"Core", "Agent", "Full"}
ACCEPTANCE_KINDS = {"system-governance", "distribution-native", "component-native"}
SURFACE_CLASSES = {"governance", "release-orchestrator", "runtime-component"}

TOP_LEVEL_KEYS = {"schema_version", "registry_id", "admission_policy", "repositories", "semantics"}
ADMISSION_KEYS = {"identity_key", "unregistered_first_class_release", "distribution_registry_authority"}
SEMANTICS_KEYS = {"static_registry_only", "current_name_is_routing_metadata", "dynamic_state_authority", "human_ledger_authority"}
ENTRY_REQUIRED = {
    "repository_id",
    "repository_full_name",
    "component_id",
    "canonical_responsibility",
    "lifecycle",
    "rollout_wave",
    "release_profiles",
    "distribution_ships",
    "component_release_descriptor_path",
    "owner_acceptance",
    "system_refs",
    "surface_classification",
}
ENTRY_OPTIONAL = {"direct_compatibility_dependencies"}
OWNER_ACCEPTANCE_KEYS = {"kind", "discovery_paths"}


def _object(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return {}
    return value


def _exact_keys(obj: dict[str, Any], expected: set[str], path: str, errors: list[str], *, optional: set[str] | None = None) -> None:
    optional = optional or set()
    missing = expected - set(obj)
    unknown = set(obj) - expected - optional
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"{path}: unknown keys: {', '.join(sorted(unknown))}")


def _unique_string_list(value: Any, path: str, errors: list[str], *, allow_empty: bool = True) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{path}: expected array")
        return []
    if not allow_empty and not value:
        errors.append(f"{path}: expected non-empty array")
    if any(not isinstance(item, str) or not item for item in value):
        errors.append(f"{path}: expected non-empty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{path}: duplicates are not allowed")
    return value


def validate_registry(data: Any) -> list[str]:
    errors: list[str] = []
    root = _object(data, "$", errors)
    if not root:
        return errors

    _exact_keys(root, TOP_LEVEL_KEYS, "$", errors)

    if root.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"$.schema_version: expected {SCHEMA_VERSION!r}")
    if root.get("registry_id") != REGISTRY_ID:
        errors.append(f"$.registry_id: expected {REGISTRY_ID!r}")

    admission = _object(root.get("admission_policy"), "$.admission_policy", errors)
    if admission:
        _exact_keys(admission, ADMISSION_KEYS, "$.admission_policy", errors)
        if admission.get("identity_key") != "repository_id":
            errors.append("$.admission_policy.identity_key: must be repository_id")
        if admission.get("unregistered_first_class_release") != "block":
            errors.append("$.admission_policy.unregistered_first_class_release: must be block")
        if admission.get("distribution_registry_authority") is not False:
            errors.append("$.admission_policy.distribution_registry_authority: must be false")

    semantics = _object(root.get("semantics"), "$.semantics", errors)
    if semantics:
        _exact_keys(semantics, SEMANTICS_KEYS, "$.semantics", errors)
        if semantics.get("static_registry_only") is not True:
            errors.append("$.semantics.static_registry_only: must be true")
        if semantics.get("current_name_is_routing_metadata") is not True:
            errors.append("$.semantics.current_name_is_routing_metadata: must be true")
        if semantics.get("dynamic_state_authority") != "governance/repository-state.json":
            errors.append("$.semantics.dynamic_state_authority: must point to governance/repository-state.json")
        if semantics.get("human_ledger_authority") is not False:
            errors.append("$.semantics.human_ledger_authority: must be false")

    repositories = root.get("repositories")
    if not isinstance(repositories, list) or not repositories:
        errors.append("$.repositories: expected non-empty array")
        return errors

    seen_repository_ids: dict[int, int] = {}
    seen_names: dict[str, int] = {}
    seen_components: dict[str, int] = {}
    entries: list[dict[str, Any]] = []

    for index, item in enumerate(repositories):
        path = f"$.repositories[{index}]"
        entry = _object(item, path, errors)
        if not entry:
            continue
        entries.append(entry)
        _exact_keys(entry, ENTRY_REQUIRED, path, errors, optional=ENTRY_OPTIONAL)

        repository_id = entry.get("repository_id")
        if type(repository_id) is not int or repository_id <= 0:
            errors.append(f"{path}.repository_id: expected positive integer GitHub repository ID")
        else:
            if repository_id in seen_repository_ids:
                errors.append(f"{path}.repository_id: duplicate stable repository ID also used by repositories[{seen_repository_ids[repository_id]}]")
            else:
                seen_repository_ids[repository_id] = index

        repository_full_name = entry.get("repository_full_name")
        if not isinstance(repository_full_name, str) or not REPOSITORY.fullmatch(repository_full_name):
            errors.append(f"{path}.repository_full_name: expected current owner/repository routing name")
        else:
            if repository_full_name in seen_names:
                errors.append(f"{path}.repository_full_name: duplicate current routing name")
            else:
                seen_names[repository_full_name] = index

        component_id = entry.get("component_id")
        if not isinstance(component_id, str) or not (2 <= len(component_id) <= 80) or not COMPONENT_ID.fullmatch(component_id):
            errors.append(f"{path}.component_id: invalid canonical component id")
        else:
            if component_id in seen_components:
                errors.append(f"{path}.component_id: duplicate canonical component id")
            else:
                seen_components[component_id] = index

        responsibility = entry.get("canonical_responsibility")
        if not isinstance(responsibility, str) or not (10 <= len(responsibility) <= 600):
            errors.append(f"{path}.canonical_responsibility: expected 10-600 character string")

        lifecycle = entry.get("lifecycle")
        if lifecycle not in LIFECYCLES:
            errors.append(f"{path}.lifecycle: invalid lifecycle")

        rollout_wave = entry.get("rollout_wave")
        if type(rollout_wave) is not int or rollout_wave not in {1, 2, 3}:
            errors.append(f"{path}.rollout_wave: expected 1, 2, or 3")

        profiles = _unique_string_list(entry.get("release_profiles"), f"{path}.release_profiles", errors)
        if any(profile not in RELEASE_PROFILES for profile in profiles):
            errors.append(f"{path}.release_profiles: contains unsupported profile")

        distribution_ships = entry.get("distribution_ships")
        if not isinstance(distribution_ships, bool):
            errors.append(f"{path}.distribution_ships: expected boolean")

        descriptor_path = entry.get("component_release_descriptor_path")
        if descriptor_path is not None and (not isinstance(descriptor_path, str) or not descriptor_path):
            errors.append(f"{path}.component_release_descriptor_path: expected non-empty string or null")

        owner_acceptance = _object(entry.get("owner_acceptance"), f"{path}.owner_acceptance", errors)
        acceptance_kind = None
        if owner_acceptance:
            _exact_keys(owner_acceptance, OWNER_ACCEPTANCE_KEYS, f"{path}.owner_acceptance", errors)
            acceptance_kind = owner_acceptance.get("kind")
            if acceptance_kind not in ACCEPTANCE_KINDS:
                errors.append(f"{path}.owner_acceptance.kind: invalid acceptance kind")
            _unique_string_list(owner_acceptance.get("discovery_paths"), f"{path}.owner_acceptance.discovery_paths", errors, allow_empty=False)

        _unique_string_list(entry.get("system_refs"), f"{path}.system_refs", errors, allow_empty=False)

        surface = entry.get("surface_classification")
        if surface not in SURFACE_CLASSES:
            errors.append(f"{path}.surface_classification: invalid surface classification")

        dependencies = entry.get("direct_compatibility_dependencies")
        if dependencies is not None:
            deps = _unique_string_list(dependencies, f"{path}.direct_compatibility_dependencies", errors)
            for dep in deps:
                if not COMPONENT_ID.fullmatch(dep):
                    errors.append(f"{path}.direct_compatibility_dependencies: invalid component id {dep!r}")
                if dep == component_id:
                    errors.append(f"{path}.direct_compatibility_dependencies: component cannot depend on itself")

        if distribution_ships is True:
            if lifecycle != "active":
                errors.append(f"{path}: Distribution-shipped repository must be active")
            if not profiles:
                errors.append(f"{path}: Distribution-shipped repository requires at least one release profile")
            if surface != "runtime-component":
                errors.append(f"{path}: Distribution-shipped repository must be runtime-component")
            if not isinstance(descriptor_path, str) or not descriptor_path:
                errors.append(f"{path}: Distribution-shipped repository requires component release descriptor path")
            if acceptance_kind != "component-native":
                errors.append(f"{path}: Distribution-shipped repository requires component-native owner acceptance")
        elif surface == "runtime-component":
            errors.append(f"{path}: runtime-component must declare distribution_ships=true in Registry v1")

        if surface == "governance" and descriptor_path is not None:
            errors.append(f"{path}: non-runtime control-plane repository must not declare component release descriptor")
        if surface == "release-orchestrator" and descriptor_path is not None:
            distribution_owner_descriptor = (
                component_id == "ai-verse-distribution"
                and acceptance_kind == "distribution-native"
                and descriptor_path == "release/component-release.json"
            )
            if not distribution_owner_descriptor:
                errors.append(f"{path}: release-orchestrator descriptor is only allowed for Distribution-native owner evidence")

    registered_components = set(seen_components)
    for index, entry in enumerate(entries):
        dependencies = entry.get("direct_compatibility_dependencies") or []
        for dependency in dependencies:
            if dependency not in registered_components:
                errors.append(f"$.repositories[{index}].direct_compatibility_dependencies: unregistered component dependency {dependency!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "registry",
        nargs="?",
        type=Path,
        default=Path("governance/repository-registry.json"),
        help="Registry JSON to validate (default: governance/repository-registry.json)",
    )
    args = parser.parse_args()

    try:
        data = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate_registry(data)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VALID {data['registry_id']} repositories={len(data['repositories'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
