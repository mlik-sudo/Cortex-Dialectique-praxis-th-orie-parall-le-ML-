#!/usr/bin/env python3
"""Offline security helpers for environments without package installs.

This is intentionally conservative: it does not try to exactly reproduce detect-secrets
hashing/verification, but provides a lightweight "tripwire" scan plus front-matter checks.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys
from typing import Iterable, List, Sequence, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULT_INCLUDE = (
    "docs",
    "policies",
    "security",
    "scripts",
    "project-space",
)
DEFAULT_EXCLUDE = {
    ".git",
    "__pycache__",
    "dashboards/badges",
    "project-space/benchmarks/results",
    "security/detect-secrets.baseline",
    "project-space/security/detect-secrets.baseline",
    ".secrets.baseline",
}

SECRET_PATTERNS: Sequence[Tuple[str, re.Pattern[str]]] = (
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Google API Key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Slack Token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,48}")),
    ("GitHub Token", re.compile(r"gh[pousr]_[0-9A-Za-z]{36}")),
    ("Stripe Secret", re.compile(r"sk_live_[0-9A-Za-z]{24}")),
    ("Twilio SID", re.compile(r"AC[0-9a-fA-F]{32}")),
    (
        "UUID-like secret",
        re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"),
    ),
)


def _is_binary(path: pathlib.Path) -> bool:
    try:
        chunk = path.read_bytes()[:1024]
    except (OSError, PermissionError):
        return True
    return b"\0" in chunk


def iter_candidate_files(include: Sequence[str]) -> Iterable[pathlib.Path]:
    for rel in include:
        start = ROOT / rel
        if not start.exists():
            continue
        if start.is_file():
            if not _is_binary(start):
                yield start
            continue
        for path in start.rglob("*"):
            if not path.is_file():
                continue
            rel_path = path.relative_to(ROOT)
            rel_str = str(rel_path)
            if any(
                rel_str.startswith(prefix + os.sep) or rel_str == prefix
                for prefix in DEFAULT_EXCLUDE
            ):
                continue
            if _is_binary(path):
                continue
            yield path


def scan_for_patterns(paths: Sequence[pathlib.Path]) -> List[str]:
    findings: List[str] = []
    for file_path in paths:
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except (OSError, UnicodeDecodeError):
            continue
        for name, pattern in SECRET_PATTERNS:
            for match in pattern.finditer(text):
                findings.append(
                    f"{name} match in {file_path.relative_to(ROOT)} -> {match.group(0)[:12]}…"
                )
    return findings


def run_detect_secrets(include: Sequence[str]) -> int:
    findings = scan_for_patterns(list(iter_candidate_files(include)))
    if findings:
        print("[detect-secrets] potential secrets detected (offline stub):")
        for line in findings:
            print("  -", line)
        return 1
    print("[detect-secrets] scan clean (offline stub).")
    return 0


def run_gitleaks(include: Sequence[str]) -> int:
    findings = scan_for_patterns(list(iter_candidate_files(include)))
    if findings:
        print("[gitleaks] potential findings (offline stub):")
        for line in findings:
            print("  -", line)
        return 1
    print("[gitleaks] scan clean (offline stub).")
    return 0


def run_front_matter(paths: Sequence[str]) -> int:
    script = ROOT / "security" / "check_front_matter.py"
    cmd = [sys.executable, str(script), *paths]
    return os.spawnvpe(os.P_WAIT, sys.executable, cmd, os.environ)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run offline security hooks")
    parser.add_argument(
        "--include", nargs="*", default=list(DEFAULT_INCLUDE), help="roots to scan"
    )
    parser.add_argument(
        "--front-matter", nargs="*", default=["docs"], help="paths to enforce front-matter"
    )
    args = parser.parse_args(argv)

    include = args.include or list(DEFAULT_INCLUDE)

    status = 0
    if run_front_matter(args.front_matter) != 0:
        status = 1
    if run_detect_secrets(include) != 0:
        status = 1
    if run_gitleaks(include) != 0:
        status = 1
    return status


if __name__ == "__main__":
    sys.exit(main())
