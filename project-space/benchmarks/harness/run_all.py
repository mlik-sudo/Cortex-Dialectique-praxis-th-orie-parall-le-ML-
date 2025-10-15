#!/usr/bin/env python3
import json, os, time, pathlib
from datetime import datetime, timezone

def main():
    outdir = pathlib.Path(os.environ.get("OUTPUT_DIR", "project-space/benchmarks/results"))
    outdir.mkdir(parents=True, exist_ok=True)
    results_path = outdir / "smoke_results.jsonl"

    t0 = time.perf_counter()
    time.sleep(0.01)
    duration_ms = int((time.perf_counter() - t0) * 1000)

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "scenario": "smoke_minimal",
        "agent": "harness",
        "status": "ok",
        "duration_ms": duration_ms
    }
    with results_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    print(f"wrote {results_path}")

if __name__ == "__main__":
    main()
