#!/usr/bin/env python3
"""Ensure Markdown files contain YAML front matter."""
from __future__ import annotations

import sys
from pathlib import Path


ERROR_TEMPLATE = (
    "{path}: missing YAML front matter. Add a leading '---' block with metadata."
)


def has_front_matter(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"{path}: unable to read file ({exc}).", file=sys.stderr)
        return False

    lines = text.splitlines()
    if not lines:
        return False

    # Skip any UTF-8 BOM or whitespace-only lines before content.
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    if idx >= len(lines) or lines[idx].strip() != "---":
        return False

    idx += 1
    while idx < len(lines) and lines[idx].strip() != "---":
        idx += 1

    return idx < len(lines)


def main(argv: list[str]) -> int:
    if len(argv) <= 1:
        return 0

    missing = False
    for name in argv[1:]:
        path = Path(name)
        if not has_front_matter(path):
            print(ERROR_TEMPLATE.format(path=path), file=sys.stderr)
            missing = True
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
