#!/usr/bin/env python3
"""
Generate SVG badges from benchmark results for visualization in README.
"""
import json
import pathlib
from typing import List


def compute_success_rate(lines: List[str]) -> int:
    """
    Compute success rate from JSONL lines.

    Args:
        lines: List of JSONL strings

    Returns:
        Success rate as percentage (0-100)
    """
    total = 0
    ok = 0
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        total += 1
        try:
            obj = json.loads(ln)
            ok += 1 if obj.get("status") == "ok" else 0
        except Exception:
            pass
    return 0 if total == 0 else int(100 * ok / total)


def color_for(rate: int) -> str:
    """
    Get badge color based on success rate.

    Args:
        rate: Success rate percentage (0-100)

    Returns:
        Hex color code
    """
    if rate >= 80:
        return "#4c1"
    if rate >= 50:
        return "#fe7d37"
    return "#e05d44"


def main() -> None:
    """Generate SVG badges from benchmark results."""
    indir = pathlib.Path("project-space/benchmarks/results")
    badge_dir = pathlib.Path("project-space/dashboards/badges")
    badge_dir.mkdir(parents=True, exist_ok=True)

    src = indir / "smoke_results.jsonl"
    lines = src.read_text(encoding="utf-8").splitlines() if src.exists() else []
    rate = compute_success_rate(lines)
    color = color_for(rate)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="170" height="20" role="img" aria-label="smoke:{rate}%">
<linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>
<rect rx="3" width="170" height="20" fill="#555"/>
<rect rx="3" x="60" width="110" height="20" fill="{color}"/>
<path fill="{color}" d="M60 0h4v20h-4z"/>
<rect rx="3" width="170" height="20" fill="url(#a)"/>
<g fill="#fff" text-anchor="start" font-family="DejaVu Sans,Verdana,Geneva" font-size="11">
  <text x="6" y="14">smoke</text>
  <text x="68" y="14">{rate}% pass</text>
</g></svg>"""
    (badge_dir / "smoke.svg").write_text(svg, encoding="utf-8")
    print(f"badge: {badge_dir/'smoke.svg'}")

if __name__ == "__main__":
    main()
