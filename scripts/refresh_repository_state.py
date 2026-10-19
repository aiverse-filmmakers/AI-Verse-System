#!/usr/bin/env python3
"""AI-Verse Repository State live refresh and ledger projection entrypoint.

This is the single System-owned implementation for Repository State refresh and
human ledger generation. It performs read-only GitHub evidence collection from
Registry-derived scope, records exact immutable refs, and never writes sibling
repositories or treats Distribution qualification as owner acceptance.
"""

from __future__ import annotations

import argparse
import base64
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable

from validate_component_release_descriptor import validate_descriptor
from validate_repository_state import validate_state

DEFAULT_REGISTRY = Path("governance/repository-registry.json")
DEFAULT_STATE = Path("governance/repository-state.json")
DEFAULT_LEDGER = Path("docs/REPOSITORY-STATE-LEDGER.md")
DEFAULT_API_BASE = "https://api.github.com"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SYSTEM_COMPONENT_ID = "ai-verse-system"
DISTRIBUTION_COMPONENT_ID = "ai-verse-distribution"


class EvidenceUnavailable(RuntimeError):
    """Required remote evidence cannot be accessed."""


class EvidenceFailed(RuntimeError):
    """A remote evidence check ran but failed."""


class EvidenceMissing(RuntimeError):
    """An exact-at-ref repository path does not exist."""


class GitHubClient:
    """Small read-only GitHub REST client used by the refresh engine."""

    def __init__(self, *, api_base: str = DEFAULT_API_BASE, token: str | None = None) -> None:
        self.api_base = api_base.rstrip("/")
        self.token = token

    def _request_json(self, url: str, *, missing: bool = False) -> Any:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-verse-repository-state-refresh/1",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and missing:
                raise EvidenceMissing(url) from exc
            if exc.code in {401, 403, 404}:
                raise EvidenceUnavailable(f"HTTP {exc.code}: {url}") from exc
            raise EvidenceFailed(f"HTTP {exc.code}: {url}") from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise EvidenceFailed(f"request failed: {url}: {exc}") from exc
        try:
            return json.loads(payload)
        except json.JSONDecodeError as exc:
            raise EvidenceFailed(f"invalid JSON from {url}") from exc

    def repository(self, full_name: str) -> dict[str, Any]:
        owner_repo = urllib.parse.quote(full_name, safe="/")
        value = self._request_json(f"{self.api_base}/repos/{owner_repo}")
        if not isinstance(value, dict):
            raise EvidenceFailed(f"repository response was not an object: {full_name}")
        return value

    def branch(self, full_name: str, branch: str) -> dict[str, Any]:
        owner_repo = urllib.parse.quote(full_name, safe="/")
        encoded_branch = urllib.parse.quote(branch, safe="")
        value = self._request_json(f"{self.api_base}/repos/{owner_repo}/branches/{encoded_branch}")
        if not isinstance(value, dict):
            raise EvidenceFailed(f"branch response was not an object: {full_name}@{branch}")
        return value

    def contents(self, full_name: str, path: str, ref: str) -> dict[str, Any]:
        owner_repo = urllib.parse.quote(full_name, safe="/")
        encoded_path = urllib.parse.quote(path, safe="/")
        encoded_ref = urllib.parse.quote(ref, safe="")
        value = self._request_json(
            f"{self.api_base}/repos/{owner_repo}/contents/{encoded_path}?ref={encoded_ref}",
            missing=True,
        )
        if not isinstance(value, dict):
            raise EvidenceFailed(f"file response was not an object: {full_name}@{ref}:{path}")
        return value

    def list_contents(self, full_name: str, path: str, ref: str) -> list[dict[str, Any]]:
        owner_repo = urllib.parse.quote(full_name, safe="/")
        encoded_path = urllib.parse.quote(path, safe="/")
        encoded_ref = urllib.parse.quote(ref, safe="")
        value = self._request_json(
            f"{self.api_base}/repos/{owner_repo}/contents/{encoded_path}?ref={encoded_ref}",
            missing=True,
        )
        if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
            raise EvidenceFailed(f"directory response was not an array: {full_name}@{ref}:{path}")
        return value


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _git_blob_sha(path: Path) -> str:
    content = path.read_bytes()
    payload = b"blob " + str(len(content)).encode("ascii") + b"\0" + content
    return hashlib.sha1(payload).hexdigest()


def _local_head() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise EvidenceFailed("cannot resolve local System Git HEAD") from exc
    revision = result.stdout.strip()
    if not SHA40.fullmatch(revision):
        raise EvidenceFailed("local System Git HEAD is not an exact 40-character SHA")
    return revision


def _short(value: str | None) -> str:
    return value[:12] if value else "-"


def _escape(value: Any) -> str:
    if value is None:
        return "-"
    return str(value).replace("|", "\\|").replace("\n", " ")


def _status_revision(block: dict[str, Any], key: str = "revision") -> str:
    status = block.get("status", "unknown")
    revision = block.get(key)
    return f"{status} `{_short(revision)}`" if revision else status


def _registry_by_id(registry: dict[str, Any]) -> dict[int, dict[str, Any]]:
    return {item["repository_id"]: item for item in registry["repositories"]}


def _registry_by_component(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["component_id"]: item for item in registry["repositories"]}


def resolve_scope(
    registry: dict[str, Any],
    scope: str,
    *,
    component_id: str | None = None,
) -> list[int]:
    """Return Registry IDs required by a refresh scope, preserving Registry order."""

    entries = registry["repositories"]
    by_component = _registry_by_component(registry)
    controls = {
        by_component[SYSTEM_COMPONENT_ID]["repository_id"],
        by_component[DISTRIBUTION_COMPONENT_ID]["repository_id"],
    }

    selected: set[int]
    if scope == "component":
        if not component_id:
            raise ValueError("component scope requires --component")
        if component_id not in by_component:
            raise ValueError(f"unregistered component: {component_id}")
        selected = set(controls)
        queue = [component_id]
        seen_components: set[str] = set()
        while queue:
            current = queue.pop(0)
            if current in seen_components:
                continue
            seen_components.add(current)
            entry = by_component[current]
            selected.add(entry["repository_id"])
            for dependency in entry.get("direct_compatibility_dependencies", []):
                if dependency not in by_component:
                    raise ValueError(f"unregistered dependency {dependency!r} declared by {current}")
                queue.append(dependency)
    elif scope == "Core":
        selected = set(controls)
        selected.update(
            item["repository_id"]
            for item in entries
            if item.get("lifecycle") == "active" and "Core" in item.get("release_profiles", [])
        )
    elif scope == "Agent":
        selected = set(controls)
        selected.update(
            item["repository_id"]
            for item in entries
            if item.get("lifecycle") == "active"
            and any(profile in {"Core", "Agent"} for profile in item.get("release_profiles", []))
        )
    elif scope == "Full":
        selected = set(controls)
        selected.update(
            item["repository_id"]
            for item in entries
            if item.get("lifecycle") == "active" and item.get("distribution_ships") is True
        )
    elif scope == "global":
        selected = {item["repository_id"] for item in entries}
    else:
        raise ValueError(f"unsupported refresh scope: {scope}")

    return [item["repository_id"] for item in entries if item["repository_id"] in selected]


def _exact_sha(value: Any, description: str) -> str:
    if not isinstance(value, str) or not SHA40.fullmatch(value):
        raise EvidenceFailed(f"{description} is not an exact 40-character Git SHA")
    return value


def _decode_content(payload: dict[str, Any], description: str) -> tuple[str, str]:
    blob_sha = _exact_sha(payload.get("sha"), f"{description} blob SHA")
    if payload.get("encoding") != "base64" or not isinstance(payload.get("content"), str):
        raise EvidenceFailed(f"{description} did not return base64 file content")
    try:
        raw = base64.b64decode(payload["content"], validate=False)
        return raw.decode("utf-8"), blob_sha
    except (ValueError, UnicodeDecodeError) as exc:
        raise EvidenceFailed(f"{description} is not valid UTF-8 base64 content") from exc


def _evidence_ref(full_name: str, revision: str, path: str) -> str:
    return f"{full_name}@{revision}:{path}"


def _not_applicable_evidence() -> dict[str, Any]:
    return {"status": "not-applicable", "revision": None, "evidence_refs": []}


def _not_applicable_pin() -> dict[str, Any]:
    return {
        "status": "not-applicable",
        "revision": None,
        "release_id": None,
        "evidence_refs": [],
    }


def _not_applicable_descriptor() -> dict[str, Any]:
    return {
        "status": "not-applicable",
        "revision": None,
        "release_status": None,
        "blob_sha": None,
        "evidence_refs": [],
    }


def _not_applicable_sync() -> dict[str, Any]:
    return {"status": "not-applicable", "checkpoint_revision": None, "evidence_refs": []}


def _default_entry(registry_entry: dict[str, Any], evidence_revision: str) -> dict[str, Any]:
    component_id = registry_entry["component_id"]
    control = component_id in {SYSTEM_COMPONENT_ID, DISTRIBUTION_COMPONENT_ID}
    return {
        "repository_id": registry_entry["repository_id"],
        "access": "unverified",
        "observed_head": None,
        "owner_acceptance": _not_applicable_evidence() if component_id == SYSTEM_COMPONENT_ID else {
            "status": "unverified",
            "revision": None,
            "evidence_refs": [],
        },
        "distribution_pin": _not_applicable_pin() if not registry_entry.get("distribution_ships") else {
            "status": "unverified",
            "revision": None,
            "release_id": None,
            "evidence_refs": [],
        },
        "descriptor": _not_applicable_descriptor() if not registry_entry.get("component_release_descriptor_path") else {
            "status": "unavailable",
            "revision": None,
            "release_status": None,
            "blob_sha": None,
            "evidence_refs": [],
        },
        "system_sync": _not_applicable_sync() if component_id == SYSTEM_COMPONENT_ID else {
            "status": "unverified",
            "checkpoint_revision": None,
            "evidence_refs": [],
        },
        "freshness": {
            "scope": "component",
            "status": "unknown",
            "evidence_revision": evidence_revision,
        },
    }


def _observe_descriptor(
    client: Any,
    registry_entry: dict[str, Any],
    head: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    path = registry_entry.get("component_release_descriptor_path")
    if not path:
        return _not_applicable_descriptor(), _not_applicable_evidence()

    full_name = registry_entry["repository_full_name"]
    ref = _evidence_ref(full_name, head, path)
    try:
        payload = client.contents(full_name, path, head)
    except EvidenceMissing:
        return (
            {
                "status": "missing",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [ref],
            },
            {"status": "unverified", "revision": None, "evidence_refs": [ref]},
        )
    except EvidenceUnavailable:
        return (
            {
                "status": "unavailable",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [ref],
            },
            {"status": "unavailable", "revision": None, "evidence_refs": [ref]},
        )
    except EvidenceFailed:
        return (
            {
                "status": "failed",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [ref],
            },
            {"status": "failed", "revision": None, "evidence_refs": [ref]},
        )

    try:
        text, blob_sha = _decode_content(payload, ref)
        data = json.loads(text)
        revision = _exact_sha(data.get("revision"), f"{ref} descriptor revision")
        release_status = data.get("release_status")
        if not isinstance(release_status, str) or not release_status:
            raise EvidenceFailed(f"{ref} descriptor release status is missing")
    except (json.JSONDecodeError, EvidenceFailed):
        return (
            {
                "status": "failed",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [ref],
            },
            {"status": "failed", "revision": None, "evidence_refs": [ref]},
        )

    descriptor = {
        "status": "observed",
        "revision": revision,
        "release_status": release_status,
        "blob_sha": blob_sha,
        "evidence_refs": [ref],
    }
    descriptor_errors = validate_descriptor(data)
    if not descriptor_errors and release_status == "accepted":
        acceptance = {
            "status": "accepted",
            "revision": revision,
            "evidence_refs": [ref],
        }
    else:
        acceptance = {
            "status": "unverified",
            "revision": None,
            "evidence_refs": [ref],
        }
    return descriptor, acceptance


def _observe_repository(
    client: Any,
    registry_entry: dict[str, Any],
    existing: dict[str, Any] | None,
    *,
    scope: str,
    evidence_revision: str,
) -> dict[str, Any]:
    entry = copy.deepcopy(existing) if existing is not None else _default_entry(registry_entry, evidence_revision)
    entry["repository_id"] = registry_entry["repository_id"]
    full_name = registry_entry["repository_full_name"]

    try:
        repo = client.repository(full_name)
        actual_id = repo.get("id")
        if actual_id != registry_entry["repository_id"]:
            raise EvidenceFailed(
                f"stable repository ID mismatch for {full_name}: Registry={registry_entry['repository_id']} live={actual_id}"
            )
        default_branch = repo.get("default_branch")
        if not isinstance(default_branch, str) or not default_branch:
            raise EvidenceFailed(f"missing default branch for {full_name}")
        branch = client.branch(full_name, default_branch)
        commit = branch.get("commit")
        if not isinstance(commit, dict):
            raise EvidenceFailed(f"missing branch commit for {full_name}@{default_branch}")
        head = _exact_sha(commit.get("sha"), f"{full_name}@{default_branch} HEAD")
    except EvidenceUnavailable:
        entry["access"] = "unavailable"
        entry["observed_head"] = None
        if registry_entry.get("component_release_descriptor_path"):
            entry["descriptor"] = {
                "status": "unavailable",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [],
            }
            entry["owner_acceptance"] = {
                "status": "unavailable",
                "revision": None,
                "evidence_refs": [],
            }
        entry["freshness"] = {"scope": scope, "status": "unknown", "evidence_revision": evidence_revision}
        return entry
    except EvidenceFailed:
        entry["access"] = "failed"
        entry["observed_head"] = None
        if registry_entry.get("component_release_descriptor_path"):
            entry["descriptor"] = {
                "status": "failed",
                "revision": None,
                "release_status": None,
                "blob_sha": None,
                "evidence_refs": [],
            }
            entry["owner_acceptance"] = {
                "status": "failed",
                "revision": None,
                "evidence_refs": [],
            }
        entry["freshness"] = {"scope": scope, "status": "failed", "evidence_revision": evidence_revision}
        return entry

    entry["access"] = "verified"
    entry["observed_head"] = head
    if registry_entry.get("component_release_descriptor_path"):
        descriptor, acceptance = _observe_descriptor(client, registry_entry, head)
        entry["descriptor"] = descriptor
        entry["owner_acceptance"] = acceptance
    elif registry_entry["component_id"] == SYSTEM_COMPONENT_ID:
        entry["descriptor"] = _not_applicable_descriptor()
        entry["owner_acceptance"] = _not_applicable_evidence()
    else:
        entry["descriptor"] = _not_applicable_descriptor()
    entry["freshness"] = {"scope": scope, "status": "fresh", "evidence_revision": evidence_revision}
    return entry


def _discover_distribution_pins(
    client: Any,
    distribution_entry: dict[str, Any],
    distribution_head: str,
    target_components: Iterable[str],
) -> tuple[dict[str, dict[str, Any]], str | None]:
    """Return exact pins from Distribution's current Core promotion and any failure kind."""

    full_name = distribution_entry["repository_full_name"]
    target_set = set(target_components)
    catalog_path = "src/aiverse_distribution/catalog/core_promotions.json"
    catalog_ref = _evidence_ref(full_name, distribution_head, catalog_path)
    try:
        catalog_payload = client.contents(full_name, catalog_path, distribution_head)
        catalog_text, _ = _decode_content(catalog_payload, catalog_ref)
        catalog = json.loads(catalog_text)
        if not isinstance(catalog, dict):
            raise EvidenceFailed("invalid Distribution Core promotions catalog")
        release_id = catalog.get("current_release")
        if not isinstance(release_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", release_id):
            raise EvidenceFailed("invalid current Core release ID in Distribution promotions catalog")

        release_path = f"release-sets/{release_id}.json"
        release_ref = _evidence_ref(full_name, distribution_head, release_path)
        release_payload = client.contents(full_name, release_path, distribution_head)
        release_text, _ = _decode_content(release_payload, release_ref)
        release = json.loads(release_text)
        if (
            not isinstance(release, dict)
            or release.get("id") != release_id
            or release.get("profile") != "core"
            or release.get("status") != "released"
            or not isinstance(release.get("promotion"), dict)
            or release["promotion"].get("default_channel") is not True
        ):
            raise EvidenceFailed(f"current Core release is not a valid released default: {release_path}")

        components = release.get("components")
        if not isinstance(components, list):
            raise EvidenceFailed(f"invalid component list in current Core release: {release_path}")

        # Historical release sets keep immutable default-channel evidence. The
        # promotion catalog, rather than those historical flags, identifies
        # which Core composition is current.
        pins: dict[str, dict[str, Any]] = {
            component_id: {
                "status": "unpinned",
                "revision": None,
                "release_id": None,
                "evidence_refs": [catalog_ref],
            }
            for component_id in target_set
        }
        seen: set[str] = set()
        for component in components:
            if not isinstance(component, dict):
                raise EvidenceFailed(f"invalid component entry in current Core release: {release_path}")
            component_id = component.get("id")
            if component_id not in target_set:
                continue
            if component_id in seen:
                raise EvidenceFailed(f"duplicate component entry in current Core release: {component_id}")
            seen.add(component_id)
            revision = _exact_sha(component.get("revision"), f"{release_path}:{component_id} revision")
            pins[component_id] = {
                "status": "pinned",
                "revision": revision,
                "release_id": release_id,
                "evidence_refs": [catalog_ref, release_ref],
            }
        return pins, None
    except EvidenceUnavailable:
        return (
            {
                component_id: {
                    "status": "unavailable",
                    "revision": None,
                    "release_id": None,
                    "evidence_refs": [catalog_ref],
                }
                for component_id in target_set
            },
            "unavailable",
        )
    except (EvidenceFailed, EvidenceMissing, json.JSONDecodeError):
        return (
            {
                component_id: {
                    "status": "failed",
                    "revision": None,
                    "release_id": None,
                    "evidence_refs": [catalog_ref],
                }
                for component_id in target_set
            },
            "failed",
        )


def refresh_state(
    registry: dict[str, Any],
    state: dict[str, Any],
    *,
    client: Any,
    scope: str,
    evidence_revision: str,
    component_id: str | None = None,
    registry_blob_sha: str | None = None,
) -> dict[str, Any]:
    """Refresh one Registry-derived scope using exact remote evidence."""

    evidence_revision = _exact_sha(evidence_revision, "refresh evidence revision")
    target_ids = resolve_scope(registry, scope, component_id=component_id)
    registry_by_id = _registry_by_id(registry)
    existing_by_id = {item["repository_id"]: item for item in state["repositories"]}
    refreshed_by_id = copy.deepcopy(existing_by_id)

    for repo_id in target_ids:
        refreshed_by_id[repo_id] = _observe_repository(
            client,
            registry_by_id[repo_id],
            existing_by_id.get(repo_id),
            scope=scope,
            evidence_revision=evidence_revision,
        )

    by_component = _registry_by_component(registry)
    system_id = by_component[SYSTEM_COMPONENT_ID]["repository_id"]
    distribution_id = by_component[DISTRIBUTION_COMPONENT_ID]["repository_id"]
    system_observation = refreshed_by_id[system_id]
    if system_id in target_ids and system_observation.get("access") == "verified":
        if system_observation.get("observed_head") != evidence_revision:
            raise EvidenceFailed(
                "System live HEAD does not equal the local/evidence revision; refresh is stale or concurrent and cannot be published"
            )

    pin_failure: str | None = None
    shipped_targets = [
        item
        for item in registry["repositories"]
        if item["repository_id"] in target_ids and item.get("distribution_ships") is True
    ]
    if shipped_targets:
        distribution_state = refreshed_by_id[distribution_id]
        if distribution_state.get("access") == "verified" and distribution_state.get("observed_head"):
            pins, pin_failure = _discover_distribution_pins(
                client,
                by_component[DISTRIBUTION_COMPONENT_ID],
                distribution_state["observed_head"],
                [item["component_id"] for item in shipped_targets],
            )
            for registry_entry in shipped_targets:
                refreshed_by_id[registry_entry["repository_id"]]["distribution_pin"] = pins[registry_entry["component_id"]]
        else:
            status = "failed" if distribution_state.get("access") == "failed" else "unavailable"
            pin_failure = status
            for registry_entry in shipped_targets:
                refreshed_by_id[registry_entry["repository_id"]]["distribution_pin"] = {
                    "status": status,
                    "revision": None,
                    "release_id": None,
                    "evidence_refs": [],
                }

    attempted = [refreshed_by_id[repo_id] for repo_id in target_ids]
    verified_count = sum(item["access"] == "verified" for item in attempted)
    has_problem = any(item["access"] in {"unavailable", "failed"} for item in attempted)
    has_problem = has_problem or pin_failure is not None
    if verified_count == 0:
        refresh_status = "failed"
    elif has_problem:
        refresh_status = "partial"
    else:
        refresh_status = "complete"

    result = copy.deepcopy(state)
    result["registry_binding"]["blob_sha"] = registry_blob_sha or result["registry_binding"]["blob_sha"]
    result["repositories"] = [refreshed_by_id[item["repository_id"]] for item in registry["repositories"]]
    record = {
        "scope": scope,
        "status": refresh_status,
        "evidence_revision": evidence_revision,
        "observed_at": None,
    }
    result["refresh"] = {
        "mode": "full-refresh" if scope == "global" else "scoped-refresh",
        "scope": scope,
        "status": refresh_status,
        "repository_ids": target_ids,
        "evidence_revision": evidence_revision,
        "last_scoped_refresh": record,
        "last_full_refresh": record if scope == "global" else result["refresh"].get("last_full_refresh"),
    }
    return result


def render_ledger(registry: dict[str, Any], state: dict[str, Any]) -> str:
    registry_by_id = {item["repository_id"]: item for item in registry["repositories"]}
    state_by_id = {item["repository_id"]: item for item in state["repositories"]}

    lines: list[str] = [
        "# AI-Verse Repository State Ledger",
        "",
        "> GENERATED FILE. Do not hand-edit. Machine truth is `governance/repository-registry.json` for static facts and `governance/repository-state.json` for dynamic facts.",
        "",
        "Regenerate with `python scripts/refresh_repository_state.py --write-ledger`. Verify with `python scripts/refresh_repository_state.py --check-ledger`.",
        "",
        "## Snapshot",
        "",
        f"- State schema: `{state['schema_version']}`",
        f"- Registry binding blob: `{state['registry_binding']['blob_sha']}`",
        f"- Refresh mode: `{state['refresh']['mode']}`",
        f"- Refresh scope: `{state['refresh']['scope']}`",
        f"- Refresh status: `{state['refresh']['status']}`",
        f"- Refresh evidence revision: `{state['refresh']['evidence_revision']}`",
        f"- Last full refresh: `{state['refresh']['last_full_refresh']['evidence_revision']}`" if state["refresh"]["last_full_refresh"] else "- Last full refresh: `none`",
        f"- Watchdog: `{state['watchdog']['status']}`",
        f"- Watchdog reason: {_escape(state['watchdog']['reason'])}",
        "",
        "## Repository state",
        "",
        "| Repository | Component | Observed HEAD | Owner acceptance | Distribution pin | Descriptor | System sync | Freshness |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for registry_entry in registry["repositories"]:
        repo_id = registry_entry["repository_id"]
        item = state_by_id[repo_id]
        pin = item["distribution_pin"]
        descriptor = item["descriptor"]
        pin_text = _status_revision(pin)
        if pin.get("release_id"):
            pin_text += f" / {_escape(pin['release_id'])}"
        descriptor_text = _status_revision(descriptor)
        if descriptor.get("release_status"):
            descriptor_text += f" / {_escape(descriptor['release_status'])}"
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape(registry_entry["repository_full_name"]),
                    _escape(registry_entry["component_id"]),
                    f"`{_short(item['observed_head'])}`" if item["observed_head"] else "-",
                    _escape(_status_revision(item["owner_acceptance"])),
                    _escape(pin_text),
                    _escape(descriptor_text),
                    _escape(_status_revision(item["system_sync"], "checkpoint_revision")),
                    _escape(f"{item['freshness']['status']} / {item['freshness']['scope']}"),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Open drift",
            "",
            "| Severity | Scope | Drift | Repositories | Reason | Required action |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    open_drift = [item for item in state["drift"] if item["status"] == "open"]
    severity_order = {"BLOCKING": 0, "WARNING": 1, "INFO": 2}
    open_drift.sort(key=lambda item: (severity_order[item["severity"]], item["scope"], item["id"]))
    for drift in open_drift:
        names = [registry_by_id[repo_id]["component_id"] for repo_id in drift["repository_ids"]]
        lines.append(
            "| "
            + " | ".join(
                [
                    _escape(drift["severity"]),
                    _escape(drift["scope"]),
                    _escape(drift["id"]),
                    _escape(", ".join(names)),
                    _escape(drift["reason"]),
                    _escape(drift["required_action"]),
                ]
            )
            + " |"
        )

    if not open_drift:
        lines.append("| INFO | global | none | - | No open drift recorded. | Continue normal evidence refresh. |")

    lines.extend(
        [
            "",
            "## Authority and freshness rules",
            "",
            "- This ledger is a projection only and is never machine authority.",
            "- Static repository identity, ownership and lifecycle facts come only from the Registry.",
            "- Dynamic HEADs, pins, descriptor observations, acceptance evidence, sync state, freshness, watchdog state and drift come only from Repository State.",
            "- Dates are informational only. Exact Git identity, evidence refs and refresh scope determine freshness and lineage.",
            "- `WATCHDOG-STALE` and `WATCHDOG-FAILED` are not CLEAN. A valid scoped refresh may prove a scoped decision while the full watchdog is stale, subject to the governance contract.",
            "- Any intersecting or global `BLOCKING` drift blocks the relevant future release decision until reconciled.",
            "",
        ]
    )
    return "\n".join(lines)


def _validate_or_print_errors(registry: dict[str, Any], state: dict[str, Any], registry_path: Path) -> bool:
    errors = validate_state(state, registry, registry_path=registry_path)
    if not errors:
        return True
    print("INVALID REPOSITORY STATE", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--refresh", action="store_true", help="Perform read-only live evidence refresh")
    parser.add_argument("--scope", choices=["component", "Core", "Agent", "Full", "global"], default="Core")
    parser.add_argument("--component", help="Canonical component ID for component scope")
    parser.add_argument("--evidence-revision", help="Exact System revision used as refresh evidence; defaults to local Git HEAD")
    parser.add_argument("--api-base", default=DEFAULT_API_BASE)
    parser.add_argument("--write-state", action="store_true", help="Write refreshed machine State to --state")
    parser.add_argument("--write-ledger", action="store_true", help="Write deterministic ledger projection")
    parser.add_argument("--check-ledger", action="store_true", help="Fail if committed ledger differs from projection")
    args = parser.parse_args()

    if args.scope == "component" and not args.component:
        parser.error("--scope component requires --component")
    if args.scope != "component" and args.component:
        parser.error("--component is only valid with --scope component")
    if args.write_state and not args.refresh:
        parser.error("--write-state requires --refresh")
    if args.check_ledger and args.write_ledger:
        parser.error("--check-ledger and --write-ledger are mutually exclusive")

    try:
        registry = _load(args.registry)
        state = _load(args.state)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    if not _validate_or_print_errors(registry, state, args.registry):
        return 1

    working_state = state
    if args.refresh:
        try:
            evidence_revision = args.evidence_revision or _local_head()
            token = os.environ.get("GITHUB_TOKEN")
            client = GitHubClient(api_base=args.api_base, token=token)
            working_state = refresh_state(
                registry,
                state,
                client=client,
                scope=args.scope,
                component_id=args.component,
                evidence_revision=evidence_revision,
                registry_blob_sha=_git_blob_sha(args.registry),
            )
        except (EvidenceFailed, EvidenceUnavailable, ValueError) as exc:
            print(f"REFRESH FAILED: {exc}", file=sys.stderr)
            return 1
        if not _validate_or_print_errors(registry, working_state, args.registry):
            return 1
        print(
            f"REFRESH {working_state['refresh']['status'].upper()} "
            f"scope={working_state['refresh']['scope']} "
            f"repos={len(working_state['refresh']['repository_ids'])} "
            f"evidence={working_state['refresh']['evidence_revision']}"
        )
        if args.write_state:
            args.state.write_text(json.dumps(working_state, indent=2) + "\n", encoding="utf-8")
            print(f"WROTE {args.state}")

    rendered = render_ledger(registry, working_state)

    if args.write_ledger:
        args.ledger.parent.mkdir(parents=True, exist_ok=True)
        args.ledger.write_text(rendered, encoding="utf-8")
        print(f"WROTE {args.ledger}")
        return 0

    if args.check_ledger:
        try:
            committed = args.ledger.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"LEDGER MISSING: {exc}", file=sys.stderr)
            return 1
        if committed != rendered:
            print("LEDGER OUT OF DATE: regenerate with --write-ledger", file=sys.stderr)
            return 1
        print(f"LEDGER CURRENT {args.ledger}")
        return 0

    if not args.refresh:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
