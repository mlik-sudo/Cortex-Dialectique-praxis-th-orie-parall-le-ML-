#!/usr/bin/env python3
"""
Aggregate benchmark metrics from JSONL results into Prometheus and JSON formats.
"""
import json
import pathlib
import statistics
from typing import List, Dict, Any

RESULTS = pathlib.Path("project-space/benchmarks/results/smoke_results.jsonl")
METRICS_DIR = pathlib.Path("project-space/dashboards/metrics")
METRICS_DIR.mkdir(parents=True, exist_ok=True)
PROM = METRICS_DIR / "bench.prom"
SUMMARY = METRICS_DIR / "summary.json"

def read_rows() -> List[Dict[str, Any]]:
    """Read and parse all rows from the smoke results JSONL file."""
    if not RESULTS.exists():
        return []
    return [json.loads(x) for x in RESULTS.read_text(encoding="utf-8").splitlines() if x.strip()]


def p95(values: List[float]) -> int:
    """
    Calculate the 95th percentile of a list of values.

    Args:
        values: List of numeric values

    Returns:
        95th percentile as integer, or 0 if list is empty
    """
    if not values:
        return 0
    values = sorted(values)
    k = max(0, int(0.95 * (len(values) - 1)))
    return int(values[k])


def main() -> None:
    """Generate Prometheus metrics and JSON summary from benchmark results."""
    rows = read_rows()
    total = len(rows)
    oks = sum(1 for r in rows if r.get("status") == "ok")
    fails = total - oks
    durations = [r.get("duration_ms", 0) for r in rows if isinstance(r.get("duration_ms", 0), (int, float))]
    avg_ms = int(statistics.mean(durations)) if durations else 0
    p95_ms = p95(durations)

    summary = {
        "total": total,
        "ok": oks,
        "fail": fails,
        "success_rate": (oks * 100 // total if total else 0),
        "avg_ms": avg_ms,
        "p95_ms": p95_ms,
    }
    SUMMARY.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# HELP bench_results_total Total results in JSONL",
        "# TYPE bench_results_total counter",
        f"bench_results_total {total}",
        "# HELP bench_results_ok Total OK results",
        "# TYPE bench_results_ok counter",
        f"bench_results_ok {oks}",
        "# HELP bench_results_fail Total FAIL results",
        "# TYPE bench_results_fail counter",
        f"bench_results_fail {fails}",
        "# HELP bench_success_rate_percent Success rate percent",
        "# TYPE bench_success_rate_percent gauge",
        f"bench_success_rate_percent {summary['success_rate']}",
        "# HELP bench_duration_ms_avg Average duration in ms",
        "# TYPE bench_duration_ms_avg gauge",
        f"bench_duration_ms_avg {avg_ms}",
        "# HELP bench_duration_ms_p95 95th percentile in ms",
        "# TYPE bench_duration_ms_p95 gauge",
        f"bench_duration_ms_p95 {p95_ms}",
    ]
    PROM.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("metrics:", PROM, "summary:", SUMMARY)

if __name__ == "__main__":
    main()
