#!/usr/bin/env python3
"""Create simple JSON badges summarizing benchmark runs."""

from __future__ import annotations

import json
import math
import pathlib
from statistics import mean
from typing import List

RESULTS_DIR = pathlib.Path(__file__).resolve().parent.parent / "results"
BADGE_DIR = pathlib.Path(__file__).resolve().parents[2] / "dashboards" / "badges"


def load_results() -> List[dict]:
    payloads: List[dict] = []
    for json_file in sorted(RESULTS_DIR.glob("*.json")):
        try:
            payloads.append(json.loads(json_file.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    return payloads


def summarize(payloads: List[dict]) -> dict:
    if not payloads:
        return {
            "agent": "codex",
            "runs": 0,
            "mean_wall_time_sec": 0,
            "mean_cpu_time_sec": 0,
            "p95_errors": 0,
        }
    wall = [row.get("wall_time_sec", 0) for row in payloads]
    cpu = [row.get("cpu_time_sec", 0) for row in payloads]
    errors = sorted(row.get("errors", 0) for row in payloads)
    p95_idx = min(len(errors) - 1, math.floor(0.95 * len(errors)))
    return {
        "agent": payloads[-1].get("agent", "codex"),
        "runs": len(payloads),
        "mean_wall_time_sec": round(mean(wall), 2) if wall else 0,
        "mean_cpu_time_sec": round(mean(cpu), 2) if cpu else 0,
        "p95_errors": errors[p95_idx] if errors else 0,
    }


def main() -> int:
    BADGE_DIR.mkdir(parents=True, exist_ok=True)
    summary = summarize(load_results())
    badge_path = BADGE_DIR / "codex.json"
    badge_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote badge summary to {badge_path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
