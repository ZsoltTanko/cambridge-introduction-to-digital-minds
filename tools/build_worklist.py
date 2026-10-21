#!/usr/bin/env python3
"""Turn course/links.json + sources/manifest.json into the work list consumed by the ingest workflow."""
import json
import os
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def rel(from_file_dir, target):
    return os.path.relpath(ROOT / target, ROOT / from_file_dir)


ORG_PAGES = ("digitalminds.cam", "digitalminds.news", "digitalminds.guide", "futureimpact.group", "matsprogram.org",
             "sentientfutures.ai", "otherminds.ai", "ai-cognition.org", "prism-global.com", "airisk.mit.edu")
LAB_DOCS = ("anthropic.com/constitution", "anthropic.com/research/deprecation-commitments")


def format_hint(l, src):
    url, method = l["url"], (src or {}).get("method", "")
    title, authors = (l.get("title") or "").lower(), (l.get("authors") or "").lower()
    if "youtu" in url:
        return "video"
    if "80000hours.org/podcast" in url:
        return "podcast"
    if "glossary" in title:
        return "course glossary (written by the course team)"
    if "docs.google.com/document" in url and url.endswith("/copy"):
        return "template"
    if "docs.google.com/document" in url and ("course" in authors or "cdm" in authors or "digital minds" in authors):
        return "course-team primer (written by the course team)"
    if "system card" in title:
        return "system card / lab document"
    if any(d in url for d in LAB_DOCS):
        return "lab policy / commitment document"
    if any(d in url for d in ORG_PAGES):
        return "org / fellowship / program page"
    if "forum.effectivealtruism.org/topics/" in url:
        return "forum topic page (collection of posts)"
    if method == "pdf":
        return "paper / report (PDF)"
    return "article / blog post / web page"


def main():
    links = json.loads((ROOT / "course/links.json").read_text())
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    data = json.loads((ROOT / "course/course.json").read_text())
    reading_by_key = {}
    for l in links:
        if l["tier"] == "reading":
            reading_by_key.setdefault(l["sourceKey"], []).append(l)

    sections = OrderedDict()
    for u in data["units"]:
        for c in u["chunks"]:
            sid = f"{u['unitNumber']}.{c['chunkOrder']}"
            sdir = next((l["sectionDir"] for l in links if l["section"] == sid), None)
            if sdir is None:
                import re
                slug = lambda s: re.sub(r"[^a-z0-9]+", "-", re.sub(r"[’'`\"]", "", s.lower())).strip("-")[:60].rstrip("-")
                sdir = f"units/{u['unitNumber']}-{slug(u['title'])}/{sid}-{slug(c['chunkTitle'])}"
            sections[sid] = {"id": sid, "title": c["chunkTitle"], "unit": int(u["unitNumber"]),
                             "unitTitle": u["title"], "dir": sdir,
                             "url": f"https://bluedot.org/courses/digital-minds/{u['unitNumber']}/{c['chunkOrder']}",
                             "estimatedTime": c.get("estimatedTime"), "itemIds": [],
                             "numExercises": len(c["exercises"])}

    readings, refs = [], []
    for i, l in enumerate(links):
        if l["tier"] == "link-only":
            continue
        src = manifest.get(l["sourceKey"], {})
        sdir = str(Path(l["summaryFile"]).parent)
        item = {
            "id": f"i{i:03d}", "kind": l["kind"], "section": l["section"],
            "sectionTitle": l["sectionTitle"], "unit": l["unit"], "unitTitle": l["unitTitle"],
            "sectionUrl": l["sectionUrl"], "pagePath": f"{l['sectionDir']}/page.md",
            "url": l["url"], "summaryFile": l["summaryFile"], "sourceFile": l["sourceFile"],
            "sourceRel": rel(sdir, l["sourceFile"]), "sourceStatus": src.get("status", "missing"),
            "sourceWords": src.get("words") or 0, "sourceMethod": src.get("method", "?"),
            "formatHint": format_hint(l, src),
        }
        if l["tier"] == "reading":
            item.update(title=l.get("title") or "Embedded video", authors=l.get("authors"), year=l.get("year"),
                        priority=l.get("coreFurtherMaybe") or "Embedded on page", timeMins=l.get("timeMins"),
                        guide=l.get("guide") or "", context=l.get("context") or "")
            readings.append(item)
        else:
            others = [r for r in reading_by_key.get(l["sourceKey"], [])]
            item.update(anchor=l["anchor"], context=l.get("context") or "",
                        alsoReading=[{"section": r["section"], "path": rel(sdir, r["summaryFile"]),
                                      "title": r.get("title")} for r in others])
            refs.append(item)
        sections[l["section"]]["itemIds"].append(item["id"])

    # siblings: every reading summary in the same section, for cross-linking
    for r in readings:
        r["siblings"] = [{"title": o["title"], "path": rel(str(Path(r["summaryFile"]).parent), o["summaryFile"]),
                          "priority": o["priority"]}
                         for o in readings if o["section"] == r["section"] and o["id"] != r["id"]]
    # other occurrences of the same URL elsewhere in the course
    by_url = {}
    for x in readings + refs:
        by_url.setdefault(x["url"], []).append(x)
    for x in readings + refs:
        x["otherOccurrences"] = [{"section": o["section"], "kind": o["kind"],
                                  "path": rel(str(Path(x["summaryFile"]).parent), o["summaryFile"])}
                                 for o in by_url[x["url"]] if o["id"] != x["id"]]

    units = []
    for u in data["units"]:
        n = int(u["unitNumber"])
        secs = [s for s in sections.values() if s["unit"] == n]
        units.append({"number": n, "title": u["title"], "dir": str(Path(secs[0]["dir"]).parent),
                      "sectionIds": [s["id"] for s in secs]})

    outline = "\n".join(
        f"Unit {u['number']}: {u['title']}\n" + "\n".join(
            f"  {s} {sections[s]['title']}" for s in u["sectionIds"]) for u in units)

    out = {"root": str(ROOT), "fetchDate": "2026-10-08", "outline": outline,
           "units": units, "sections": list(sections.values()), "readings": readings, "refs": refs}
    (ROOT / "course/worklist.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    bad = [x for x in readings + refs if x["sourceStatus"] != "ok"]
    print(f"{len(readings)} readings, {len(refs)} references, {len(sections)} sections, "
          f"{len(bad)} items with non-ok source")
    for x in bad:
        print("  ", x["sourceStatus"], x["url"])


if __name__ == "__main__":
    main()


def write_work_files():
    """One spec file per work item so each agent reads only its own context."""
    w = json.loads((ROOT / "course/worklist.json").read_text())
    wd = ROOT / "course/work"
    wd.mkdir(exist_ok=True)
    items = {x["id"]: x for x in w["readings"] + w["refs"]}
    for x in items.values():
        (wd / f"{x['id']}.json").write_text(json.dumps({**x, "courseOutline": w["outline"],
                                                       "projectRoot": w["root"], "fetchDate": w["fetchDate"]},
                                                      indent=1, ensure_ascii=False))
    for s in w["sections"]:
        spec = {**s, "courseOutline": w["outline"], "projectRoot": w["root"],
                "pagePath": f"{s['dir']}/page.md",
                "readings": [{"id": i, "title": items[i]["title"], "priority": items[i]["priority"],
                              "timeMins": items[i]["timeMins"], "summaryFile": items[i]["summaryFile"],
                              "url": items[i]["url"]} for i in s["itemIds"] if "priority" in items[i]],
                "references": [{"id": i, "kind": items[i]["kind"], "anchor": items[i]["anchor"],
                                "summaryFile": items[i]["summaryFile"], "url": items[i]["url"]}
                               for i in s["itemIds"] if "anchor" in items[i]],
                "siblingSectionPages": [f"{o['dir']}/page.md" for o in w["sections"]
                                        if o["unit"] == s["unit"] and o["id"] != s["id"]]}
        (wd / f"section-{s['id']}.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    for u in w["units"]:
        secs = [s for s in w["sections"] if s["unit"] == u["number"]]
        spec = {**u, "courseOutline": w["outline"], "projectRoot": w["root"],
                "sections": [{"id": s["id"], "title": s["title"], "page": f"{s['dir']}/page.md",
                              "synthesis": f"{s['dir']}/synthesis.md", "estimatedTime": s["estimatedTime"]}
                             for s in secs],
                "otherUnits": [{"number": o["number"], "title": o["title"], "dir": o["dir"]}
                               for o in w["units"] if o["number"] != u["number"]]}
        (wd / f"unit-{u['number']}.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False))
    compact = [{"id": x["id"], "t": "r" if "priority" in x else "x", "s": x["section"],
                "w": x["sourceWords"], "l": (x.get("title") or x.get("anchor") or "")[:40]}
               for x in items.values()]
    (ROOT / "course/work/_args.json").write_text(json.dumps(compact, ensure_ascii=False, separators=(",", ":")))
    print(f"wrote {len(items)} item specs, {len(w['sections'])} section specs, {len(w['units'])} unit specs; "
          f"args {len(json.dumps(compact))} bytes")


if __name__ == "__main__" and len(__import__("sys").argv) > 1 and __import__("sys").argv[1] == "work":
    write_work_files()
