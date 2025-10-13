import sys, re, pathlib
ok = True
for p in map(pathlib.Path, sys.argv[1:] or ['docs']):
    for f in (p.rglob("*.md") if p.is_dir() else [p]):
        txt = f.read_text(encoding="utf-8", errors="ignore")
        if not re.search(r"^---\s*\n.*?project:\s*.+\n.*?owner:\s*.+\n.*?reviewed:\s*\d{4}-\d{2}-\d{2}\n---", txt, re.S|re.M):
            print(f"[front-matter] Missing/invalid in {f}", file=sys.stderr)
            ok = False
sys.exit(0 if ok else 1)
