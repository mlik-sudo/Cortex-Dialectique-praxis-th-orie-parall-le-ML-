from pathlib import Path

def test_harness_layout():
    assert Path("project-space/benchmarks/harness/run_all.py").exists()
    assert Path("project-space/benchmarks/harness").exists()
