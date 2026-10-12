#!/usr/bin/env python3
"""Validate an AI-Verse durable entity reference v1 envelope.

This validator enforces only the System-owned shared envelope. Owner-specific
identifier and scope semantics remain authoritative in the canonical owner.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_KEYS = {"owner", "kind", "id"}
OPTIONAL_KEYS = {"scope"}
ALLOWED_KEYS = REQUIRED_KEYS | OPTIONAL_KEYS
MAX_LENGTHS = {"owner": 128, "kind": 128, "id": 1024, "scope": 1024}


def validate_reference(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["$: expected object"]

    missing = REQUIRED_KEYS - set(data)
    unknown = set(data) - ALLOWED_KEYS
    if missing:
        errors.append(f"$: missing keys: {', '.join(sorted(missing))}")
    if unknown:
        errors.append(f"$: unknown keys: {', '.join(sorted(unknown))}")

    for key in sorted(ALLOWED_KEYS & set(data)):
        value = data[key]
        if not isinstance(value, str):
            errors.append(f"$.{key}: expected string")
            continue
        if not value:
            errors.append(f"$.{key}: expected non-empty string")
            continue
        if len(value) > MAX_LENGTHS[key]:
            errors.append(f"$.{key}: exceeds maximum length {MAX_LENGTHS[key]}")

    return errors


def load_reference(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="JSON durable-reference envelope")
    args = parser.parse_args(argv)

    try:
        data = load_reference(args.path)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate_reference(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("valid durable entity reference v1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
