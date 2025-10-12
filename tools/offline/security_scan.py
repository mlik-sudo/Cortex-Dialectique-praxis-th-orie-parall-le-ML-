#!/usr/bin/env python3
"""Offline security helpers for environments without package installs."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
from typing import Iterable, List, Sequence, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULT_INCLUDE = (
    "docs",
    "project-space",
    "policies",
    "security",
)
DEFAULT_EXCLUDE = {
    ".git",
    "__pycache__",
    "dashboards/badges",
    "project-space/benchmarks/results",
}

SECRET_PATTERNS: Sequence[Tuple[str, re.Pattern[str]]] = (
    ("AWS Access Key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Google API Key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("Slack Token", re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,48}")),
    ("GitHub Token", re.compile(r"gh[pousr]_[0-9A-Za-z]{36}")),
    ("Stripe Secret", re.compile(r"sk_live_[0-9A-Za-z]{24}")),
    ("Twilio SID", re.compile(r"AC[0-9a-fA-F]{32}")),
    ("Heroku API", re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")),
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
            if any(str(rel_path).startswith(prefix + os.sep) or str(rel_path) == prefix for prefix in DEFAULT_EXCLUDE):
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
                findings.append(f"{name} match in {file_path} -> {match.group(0)[:12]}…")
    return findings


def load_baseline(path: pathlib.Path) -> List[str]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    results = data.get("results", {})
    baseline = []
    for file_path, entries in results.items():
        for entry in entries:
            baseline.append(f"{file_path}:{entry.get('hashed_secret', '')}")
    return baseline


def run_detect_secrets(baseline: pathlib.Path, include: Sequence[str]) -> int:
    baseline_refs = set(load_baseline(baseline))
    findings = scan_for_patterns(list(iter_candidate_files(include)))
    new_findings = [f for f in findings if f not in baseline_refs]
    if new_findings:
        print("[detect-secrets] potential secrets detected:")
        for line in new_findings:
            print("  -", line)
        return 1
    print("[detect-secrets] no secrets detected (offline stub).")
    return 0


def run_gitleaks(include: Sequence[str]) -> int:
    findings = scan_for_patterns(list(iter_candidate_files(include)))
    if findings:
        print("[gitleaks] potential findings:")
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
    parser.add_argument("--baseline", default="security/detect-secrets.baseline")
    parser.add_argument("--include", nargs="*", default=list(DEFAULT_INCLUDE))
    parser.add_argument("--front-matter", nargs="*", default=["docs"])
    args = parser.parse_args(argv)

    baseline_path = ROOT / args.baseline
    include = args.include or list(DEFAULT_INCLUDE)

    status = 0
    if run_front_matter(args.front_matter) != 0:
        status = 1
    if run_detect_secrets(baseline_path, include) != 0:
        status = 1
    if run_gitleaks(include) != 0:
        status = 1
    return status


if __name__ == "__main__":
    sys.exit(main())
