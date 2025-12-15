import json
import os
import subprocess
import sys


def test_proof_pack_harness_pipeline(tmp_path):
    results_dir = tmp_path / "results"
    metrics_dir = tmp_path / "metrics"
    badges_dir = tmp_path / "badges"

    env = os.environ.copy()

    subprocess.run(
        [sys.executable, "project-space/benchmarks/harness/run_all.py"],
        check=True,
        env={**env, "OUTPUT_DIR": str(results_dir)},
    )

    results_jsonl = results_dir / "smoke_results.jsonl"
    assert results_jsonl.exists()

    rows = [json.loads(line) for line in results_jsonl.read_text(encoding="utf-8").splitlines()]
    assert rows
    assert rows[-1]["status"] == "ok"
    assert isinstance(rows[-1]["duration_ms"], int)

    subprocess.run(
        [sys.executable, "project-space/benchmarks/harness/aggregate_metrics.py"],
        check=True,
        env={
            **env,
            "BENCH_RESULTS_JSONL": str(results_jsonl),
            "BENCH_METRICS_DIR": str(metrics_dir),
        },
    )

    summary_path = metrics_dir / "summary.json"
    prom_path = metrics_dir / "bench.prom"
    assert summary_path.exists()
    assert prom_path.exists()

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["total"] >= 1
    assert summary["ok"] >= 1

    subprocess.run(
        [sys.executable, "project-space/benchmarks/harness/regression_guard.py"],
        check=True,
        env={
            **env,
            "BENCH_SUMMARY_JSON": str(summary_path),
            "SR_MIN": "0",
            "P95_MAX_MS": "1000000",
        },
    )

    subprocess.run(
        [sys.executable, "project-space/benchmarks/harness/make_badges.py"],
        check=True,
        env={
            **env,
            "BENCH_RESULTS_JSONL": str(results_jsonl),
            "BENCH_BADGES_DIR": str(badges_dir),
        },
    )

    smoke_svg = badges_dir / "smoke.svg"
    assert smoke_svg.exists()
    assert "<svg" in smoke_svg.read_text(encoding="utf-8")
