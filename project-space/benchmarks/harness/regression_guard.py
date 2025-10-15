#!/usr/bin/env python3
import argparse, json, pathlib, sys

SUMMARY = pathlib.Path("project-space/dashboards/metrics/summary.json")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sr-min", type=int, default=int((__import__("os").environ.get("SR_MIN", 80))))
    ap.add_argument("--p95-max-ms", type=int, default=int((__import__("os").environ.get("P95_MAX_MS", 1000))))
    args = ap.parse_args()

    if not SUMMARY.exists():
        print(f"ERROR: {SUMMARY} not found", file=sys.stderr)
        sys.exit(2)

    data = json.loads(SUMMARY.read_text(encoding="utf-8"))
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
        sys.exit(1)

    print("REGRESSION OK: thresholds respected.")

if __name__ == "__main__":
    main()
