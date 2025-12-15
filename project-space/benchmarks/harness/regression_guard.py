#!/usr/bin/env python3
import argparse
import json
import os
import pathlib
import sys

DEFAULT_SUMMARY = pathlib.Path("project-space/dashboards/metrics/summary.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sr-min", type=int, default=int(os.environ.get("SR_MIN", 80)))
    ap.add_argument(
        "--p95-max-ms", type=int, default=int(os.environ.get("P95_MAX_MS", 1000))
    )
    args = ap.parse_args()

    summary_path = pathlib.Path(os.environ.get("BENCH_SUMMARY_JSON", str(DEFAULT_SUMMARY)))

    if not summary_path.exists():
        print(f"ERROR: {summary_path} not found", file=sys.stderr)
        raise SystemExit(2)

    data = json.loads(summary_path.read_text(encoding="utf-8"))
    sr = int(data.get("success_rate", 0))
    p95 = int(data.get("p95_ms", 0))

    print("summary.json =", json.dumps(data, indent=2))
    ok = True
    reasons = []
    if sr < args.sr_min:
        ok = False
        reasons.append(f"success_rate {sr}% < {args.sr_min}%")
    if p95 > args.p95_max_ms:
        ok = False
        reasons.append(f"p95_ms {p95} > {args.p95_max_ms}")

    if not ok:
        print("REGRESSION FAIL:", "; ".join(reasons))
        raise SystemExit(1)

    print("REGRESSION OK: thresholds respected.")


if __name__ == "__main__":
    main()
