#!/usr/bin/env python3
import json, time, os, pathlib
from datetime import datetime

def main():
    outdir = pathlib.Path(os.environ.get("OUTPUT_DIR", "project-space/benchmarks/results"))
    outdir.mkdir(parents=True, exist_ok=True)
    results_path = outdir / "smoke_results.jsonl"

    record = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "scenario": "smoke_minimal",
        "agent": "harness",
        "status": "ok",
        "duration_ms": 123
    }
    with results_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    print(f"wrote {results_path}")

if __name__ == "__main__":
    main()
