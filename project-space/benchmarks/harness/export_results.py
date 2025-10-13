#!/usr/bin/env python3
"""Export benchmark results to JSONL and CSV for dashboards."""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
from datetime import datetime
from typing import Iterable, List, Sequence

RESULTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "results"
OUTPUT_JSONL = RESULTS_DIR / "latest.jsonl"
OUTPUT_CSV = RESULTS_DIR / "latest.csv"


def iter_result_files(paths: Sequence[pathlib.Path]) -> Iterable[pathlib.Path]:
    for path in sorted(paths):
        if path.is_file() and path.suffix == ".json":
            yield path


def load_results() -> List[dict]:
    if not RESULTS_DIR.exists():
        return []
    files = list(iter_result_files(sorted(RESULTS_DIR.glob("*.json"))))
    results: List[dict] = []
    for file_path in files:
        try:
            payload = json.loads(file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        payload.setdefault("source_file", file_path.name)
        results.append(payload)
    return results


def write_jsonl(rows: Sequence[dict]) -> None:
    OUTPUT_JSONL.write_text("" if not rows else "\n".join(json.dumps(r, sort_keys=True) for r in rows) + "\n", encoding="utf-8")


def write_csv(rows: Sequence[dict]) -> None:
    if not rows:
        OUTPUT_CSV.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export benchmark results")
    parser.add_argument("--timestamp", action="store_true", help="append export timestamp metadata")
    args = parser.parse_args()

    results = load_results()
    if args.timestamp:
        now = datetime.utcnow().isoformat() + "Z"
        for row in results:
            row.setdefault("exported_at", now)
    write_jsonl(results)
    write_csv(results)
    print(f"Exported {len(results)} results to {OUTPUT_JSONL.name} and {OUTPUT_CSV.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
