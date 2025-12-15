#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  ./benchmarks/compare.sh <baseline_jsonl> <candidate_jsonl>

Both files must be JSONL produced by the harness, with numeric `duration_ms` fields.
Example:
  ./benchmarks/compare.sh project-space/benchmarks/results/smoke_results.jsonl project-space/benchmarks/results/smoke_results.jsonl
EOF
}

if [[ ${1:-} == "-h" || ${1:-} == "--help" ]]; then
  usage
  exit 0
fi

baseline=${1:-}
candidate=${2:-}

if [[ -z ${baseline} || -z ${candidate} ]]; then
  usage
  exit 2
fi

python3 - <<'PY'
import json
import statistics
import sys
from pathlib import Path

baseline = Path(sys.argv[1])
candidate = Path(sys.argv[2])

for p in (baseline, candidate):
    if not p.exists():
        raise SystemExit(f"missing file: {p}")

def read_durations(path: Path) -> list[int]:
    out: list[int] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        val = row.get("duration_ms")
        if isinstance(val, (int, float)):
            out.append(int(val))
    return out

def p95(values: list[int]) -> int:
    if not values:
        return 0
    values = sorted(values)
    k = max(0, int(0.95 * (len(values) - 1)))
    return values[k]

b = read_durations(baseline)
c = read_durations(candidate)

if not b or not c:
    raise SystemExit("no durations found in one or both files")

b_avg = int(statistics.mean(b))
c_avg = int(statistics.mean(c))

b_p95 = p95(b)
c_p95 = p95(c)

def pct(a: int, b: int) -> float:
    if a == 0:
        return 0.0
    return (b - a) * 100.0 / a

print(f"baseline:  n={len(b)} avg_ms={b_avg} p95_ms={b_p95}")
print(f"candidate: n={len(c)} avg_ms={c_avg} p95_ms={c_p95}")
print(f"delta: avg={pct(b_avg, c_avg):+.2f}% p95={pct(b_p95, c_p95):+.2f}%")
PY
"${baseline}" "${candidate}"
