#!/usr/bin/env python3
"""Apply the manual decisions that layout and build_worklist don't know about.

- course/drops.json: reference-note ids the user chose not to write. Marks them dropped in the work list, removes
  them from section specs and cross-links, and repoints their page.md rows to the assigned reading's summary
  (duplicates) or to "link only".
- course/client_rendered/<section id>.md: page text that only renders in a browser. Appended to that section's
  page.md and flagged in its section spec.

Idempotent. Re-run after every `build_dataset.py layout` or `build_worklist.py work`.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    os.chdir(ROOT)
    w = json.loads(Path("course/worklist.json").read_text())
    drops_p = Path("course/drops.json")
    drop = set(json.loads(drops_p.read_text())) if drops_p.exists() else set()

    reading_by_url = {}
    for r in w["readings"]:
        reading_by_url.setdefault(r["url"], []).append(r)
    dropped_files = set()
    for x in w["refs"]:
        if x["id"] not in drop:
            continue
        x["dropped"] = True
        dropped_files.add(x["summaryFile"])
        sdir = os.path.dirname(os.path.dirname(x["summaryFile"]))
        page = Path(sdir, "page.md")
        old = f"[summary]({os.path.relpath(x['summaryFile'], sdir)})"
        if x["alsoReading"]:
            rd = reading_by_url[x["url"]][0]
            new = f"assigned reading in {rd['section']} — [summary]({os.path.relpath(rd['summaryFile'], sdir)})"
        else:
            new = "not summarised (link only)"
        page.write_text(page.read_text().replace(old, new, 1))
    Path("course/worklist.json").write_text(json.dumps(w, indent=1, ensure_ascii=False))

    client_rendered = {p.stem: p.read_text().strip() for p in Path("course/client_rendered").glob("*.md")}
    for s in w["sections"]:
        if s["id"] not in client_rendered:
            continue
        page = Path(s["dir"], "page.md")
        text = page.read_text()
        if client_rendered[s["id"]] not in text:
            page.write_text(text.rstrip() + "\n\n" + client_rendered[s["id"]] + "\n")

    for p in Path("course/work").glob("section-*.json"):
        spec = json.loads(p.read_text())
        spec["references"] = [r for r in spec["references"] if r["id"] not in drop]
        if spec["id"] in client_rendered:
            spec.setdefault("note", "This section's page text renders client-side and was captured in a browser (see "
                                    "the end of page.md). Read the source files its page text links to directly, "
                                    "and profile each item it lists in the synthesis.")
        p.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    for p in Path("course/work").glob("i*.json"):
        spec = json.loads(p.read_text())
        base = os.path.dirname(spec["summaryFile"])
        spec["otherOccurrences"] = [o for o in spec.get("otherOccurrences", [])
                                    if os.path.normpath(os.path.join(base, o["path"])) not in dropped_files]
        p.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    print(f"{len(drop)} reference notes dropped; client-rendered text applied to {sorted(client_rendered)}")


if __name__ == "__main__":
    main()
