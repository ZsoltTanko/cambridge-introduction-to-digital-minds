#!/usr/bin/env python3
"""Report relative markdown links in the dataset that point to files that don't exist."""
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def broken_links():
    out = defaultdict(list)
    for md in ROOT.glob("**/*.md"):
        # sources/ is verbatim text; course/ holds raw captures whose links are relative to the page they are appended to
        if md.is_relative_to(ROOT / "sources") or md.is_relative_to(ROOT / "course"):
            continue
        for target in LINK_RE.findall(md.read_text(errors="replace")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = unquote(target.split("#")[0])
            if path and not (md.parent / path).exists():
                out[str(md.relative_to(ROOT))].append(target)
    return out


def fix(bad):
    """Repair links whose only fault is the number of ../ segments: rewrite when exactly one file matches."""
    import os
    files = [f for f in ROOT.glob("units/**/*.md")] + [ROOT / "course-synthesis.md", ROOT / "glossary.md"]
    fixed = 0
    for rel_md, targets in bad.items():
        md = ROOT / rel_md
        text = md.read_text()
        for t in targets:
            path, _, anchor = t.partition("#")
            tail = re.sub(r"^(\.\./|\./)+", "", unquote(path))
            matches = [f for f in files if f.exists() and str(f).endswith("/" + tail)]
            if len(matches) == 1:
                new = os.path.relpath(matches[0], md.parent) + (f"#{anchor}" if anchor else "")
                text = text.replace(f"]({t})", f"]({new})")
                fixed += 1
        md.write_text(text)
    return fixed


if __name__ == "__main__":
    bad = broken_links()
    if "--fix" in sys.argv:
        print(f"fixed {fix(bad)} links")
        bad = broken_links()
    for f, targets in sorted(bad.items()):
        print(f)
        for t in targets:
            print("   ", t)
    print(f"\n{sum(map(len, bad.values()))} broken links in {len(bad)} files")
    sys.exit(1 if bad else 0)
