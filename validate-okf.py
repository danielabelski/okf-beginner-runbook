#!/usr/bin/env python3
"""Tiny OKF Markdown validator with no external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
BAD_PATH_RE = re.compile(r"(^|[(/\\])([A-Za-z]:\\|/home/)")
RESERVED_MARKDOWN = {"index.md", "log.md", "agents.md"}
VALID_STATUSES = {"draft", "stable", "deprecated"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate basic OKF Markdown frontmatter and portable links."
    )
    parser.add_argument("folder", help="Path to an OKF knowledge base folder")
    return parser.parse_args()


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def has_content(path: Path) -> bool:
    return bool(path.read_text(encoding="utf-8").strip())


def parse_frontmatter(lines: list[str]) -> dict[str, object] | None:
    """Parse YAML frontmatter into a simple dict. Returns None on failure."""
    if not lines or lines[0] != "---":
        return None
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return None

    body = lines[1:end]
    result: dict[str, object] = {}
    current_key: str | None = None
    current_list: list[str] = []

    for line in body:
        stripped = line.strip()
        if not stripped:
            continue
        # Simple key: value
        if ":" in stripped and not stripped.startswith("-"):
            # Flush any pending list
            if current_key is not None and current_list:
                result[current_key] = current_list
                current_list = []
                current_key = None
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip("\"'")
            if value:
                result[key] = value
            else:
                # Nested mapping starts; mark key for potential list
                current_key = key
        elif stripped.startswith("- ") and current_key is not None:
            # List item under current key
            item = stripped[2:].strip().strip("\"'")
            current_list.append(item)

    if current_key is not None and current_list:
        result[current_key] = current_list

    return result


def check_frontmatter(path: Path, root: Path, failures: list[str], warnings: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    name = rel(path, root)

    if not lines or lines[0] != "---":
        failures.append(f"{name}: missing opening frontmatter line '---'")
        return

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        failures.append(f"{name}: missing closing frontmatter line '---'")
        return

    body = lines[1:end]
    type_lines = [line for line in body if line.startswith("type:")]
    if not type_lines:
        failures.append(f"{name}: missing root-level type field")
        return

    value = type_lines[0].split(":", 1)[1].strip().strip("\"'")
    if not value:
        failures.append(f"{name}: type field is empty")

    # v0.2 optional field checks (warnings only, not failures)
    fm = parse_frontmatter(lines)
    if fm is not None:
        # Check generated field
        if "generated" in fm:
            # generated is a nested mapping; check raw lines for by/at
            has_by = any("by:" in line for line in body)
            has_at = any("at:" in line for line in body)
            if not has_by or not has_at:
                warnings.append(
                    f"{name}: 'generated' is present but missing 'by' and/or 'at' sub-fields"
                )

        # Check status field
        if "status" in fm:
            status_val = str(fm["status"]).strip().strip("\"'")
            if status_val not in VALID_STATUSES:
                warnings.append(
                    f"{name}: 'status' is '{status_val}' but should be one of: draft, stable, deprecated"
                )

        # Check verified field (advisory: note if no human: actor)
        if "verified" in fm:
            verified_text = "\n".join(body)
            if "human:" not in verified_text:
                warnings.append(
                    f"{name}: 'verified' is present but no 'human:' actor found (advisory)"
                )


def check_links(path: Path, root: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        clean = target.split("#", 1)[0].strip()
        if BAD_PATH_RE.search(clean):
            failures.append(f"{rel(path, root)}: machine-specific link path: {target}")


def check_okf_version(root: Path, warnings: list[str]) -> None:
    """Check root index.md for okf_version declaration."""
    index_path = root / "index.md"
    if not index_path.exists():
        return
    lines = index_path.read_text(encoding="utf-8").splitlines()
    fm = parse_frontmatter(lines)
    if fm is None:
        return
    if "okf_version" in fm:
        version = str(fm["okf_version"]).strip().strip("\"'")
        if version not in ("0.1", "0.2"):
            warnings.append(
                f"index.md: 'okf_version' is '{version}' but recognized versions are '0.1' and '0.2'"
            )


def validate(root: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []

    if not root.exists() or not root.is_dir():
        return [f"{root}: folder does not exist"], []

    for required in ("index.md", "log.md"):
        path = root / required
        if not path.exists():
            failures.append(f"{required}: missing at root")
        elif not has_content(path):
            failures.append(f"{required}: exists but is empty")

    check_okf_version(root, warnings)

    for path in sorted(root.rglob("*.md")):
        name = path.name.lower()
        if name in RESERVED_MARKDOWN:
            if not has_content(path):
                failures.append(f"{rel(path, root)}: reserved file is empty")
        else:
            check_frontmatter(path, root, failures, warnings)
        check_links(path, root, failures)

    return failures, warnings


def main() -> int:
    args = parse_args()
    root = Path(args.folder).expanduser().resolve()
    failures, warnings = validate(root)

    exit_code = 0

    if failures:
        print(f"FAIL: {len(failures)} issue(s) found in {root}")
        for failure in failures:
            print(f"- {failure}")
        exit_code = 1

    if warnings:
        print(f"WARN: {len(warnings)} warning(s) found in {root}")
        for warning in warnings:
            print(f"- {warning}")

    if not failures and not warnings:
        total = sum(1 for _ in root.rglob("*.md"))
        print(f"PASS: checked {total} Markdown file(s) in {root}")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
