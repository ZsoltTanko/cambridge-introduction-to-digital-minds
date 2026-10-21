#!/usr/bin/env python3
"""Generate README.md: the index of the study dataset, built from the files on disk."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def frontmatter(path):
    text = path.read_text(errors="replace")
    fm = {}
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    take = re.search(r"\*\*One-line takeaway:\*\*\s*(.+)", text)
    fm["takeaway"] = take.group(1).strip() if take else ""
    return fm


def cell(s):
    return s.replace("|", "/").replace("\n", " ")


def main():
    w = json.loads((ROOT / "course/worklist.json").read_text())
    verdicts = json.loads((ROOT / "course/work/_verdicts.json").read_text())
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    units = {u["number"]: u for u in w["units"]}
    readings_by_section, refs_by_section = {}, {}
    for r in w["readings"]:
        readings_by_section.setdefault(r["section"], []).append(r)
    for x in w["refs"]:
        if not x.get("dropped") and (ROOT / x["summaryFile"]).exists():
            refs_by_section.setdefault(x["section"], []).append(x)

    coverage = Counter()
    not_full = []
    links = json.loads((ROOT / "course/links.json").read_text())
    kinds = Counter(l["kind"] for l in links)
    tiers = Counter(l["tier"] for l in links)
    n_dropped = sum(1 for x in w["refs"] if x.get("dropped"))
    videos = f" + {kinds['embedded-video']} embedded videos" if kinds["embedded-video"] else ""
    n_readings = len(w["readings"])
    n_core = sum(1 for r in w["readings"] if r["priority"] == "Core")
    hours = round(sum(r.get("timeMins") or 0 for r in w["readings"]) / 60)
    n_terms = len(re.findall(r"^### ", (ROOT / "glossary.md").read_text(), re.M))
    out = [
        '<div align="center">',
        "",
        "# Introduction to Digital Minds, mapped",
        "",
        "### Know what every reading argues before you open it.",
        "",
        "A structured study companion to the [Introduction to Digital Minds course]"
        "(https://bluedot.org/courses/digital-minds) from Cambridge Digital Minds and BlueDot Impact: "
        "could an AI system be conscious, could it matter morally, and what should anyone do while nobody knows?<br>"
        f"{n_readings} readings summarised. {len(w['units'])} units synthesised. {n_terms} terms defined. Plain markdown, all cross-linked.",
        "",
        f"![Units](https://img.shields.io/badge/units-{len(w['units'])}-4C6EF5)",
        f"![Readings summarised](https://img.shields.io/badge/readings%20summarised-{n_readings}-4C6EF5)",
        f"![Reading covered](https://img.shields.io/badge/reading%20covered-~{hours}%20hours-4C6EF5)",
        f"![Glossary terms](https://img.shields.io/badge/glossary-{n_terms}%20terms-4C6EF5)",
        "![Format](https://img.shields.io/badge/format-markdown-lightgrey)",
        "",
        "</div>",
        "",
        "## Why this exists",
        "",
        "The course asks one of the stranger questions around, whether some AI systems might be moral patients, and "
        "answering it takes philosophy of mind, neuroscience, interpretability, psychology and law. "
        f"That is {n_readings} papers, posts, system cards and talks, roughly {hours} hours of material, "
        "and it is easy to finish a paper without knowing where it sits in the argument or whether you should have believed it.",
        "",
        "This repo keeps the course's structure and hangs the missing context on it. For every reading you get what it "
        "claims, why the course put it in this unit, how it holds up under criticism, and questions to bring to a "
        "discussion. Above the readings sit syntheses that show how the units answer each other, and a glossary that "
        "says which sense of \"consciousness\" or \"moral standing\" a given author is using.",
        "",
        "> The course's core claim is conditional and modest: there is a **realistic possibility** that some digital "
        "systems matter morally, which is enough to justify acknowledging the issue, assessing it, and preparing, "
        "without asserting that any current system is conscious.",
        "",
        "The units walk from *what matters* (1), to *whether it could be there* (2), to *how we would know* (3), to "
        "*what people believe regardless* (4), to *what follows for building and securing AI* (5), to *how to decide* (6), "
        "to *how to govern* (7), to *what to do next* (8). Each one hands its unresolved problem to the next, and the "
        "[course synthesis](course-synthesis.md) traces those handoffs.",
        "",
        "## What's inside",
        "",
        "| | |",
        "|---|---|",
        "| **[Course synthesis](course-synthesis.md)** | The argument on one page, the unit-by-unit arc, and a toolbox table of every method and framework the course covers with its main limitation. |",
        f"| **[Glossary](glossary.md)** | {n_terms} terms, each linked to where it is introduced. Definitions follow the course's usage, and the glossary says when that is a stipulation rather than consensus. |",
        "| **Unit overviews** | A throughline, a concept map, techniques and trade-offs, open problems and self-test questions for each unit. |",
        "| **Section syntheses** | The core argument, a map of the readings, live debates, suggested study paths and discussion questions. |",
        f"| **{n_readings} reading summaries** | Purpose, a detailed walk-through, evidence, trade-offs, connections to the rest of the course, critique and discussion questions. "
        f"Each of the {n_core} Core readings got an independent fact-check pass. |",
        "| **Course pages and exercises** | The BlueDot page text for every section, kept verbatim, with the course's \"why read this\" guide and the exercises. |",
        "",
        "## Using it",
        "",
        "- **Before a session:** read the section synthesis, then skim the takeaway column in the course map below to decide what to read in full.",
        "- **After a reading:** check the summary's critique and discussion questions against your own take.",
        "- **When a term trips you up:** look it up in the glossary, which links back to the readings that use it.",
        "",
        "Everything is plain markdown with relative links, so it reads fine on GitHub, in any editor, or as context you hand to an LLM.",
        "",
        "This is an unofficial companion. The summaries and syntheses were written by Claude and are no substitute for the "
        "readings themselves; [How this was built](#how-this-was-built) and [Caveats](#caveats) say exactly what was checked and what wasn't.",
        "",
        "## Start here",
        "",
        "- [course-synthesis.md](course-synthesis.md): the course's argument, unit-by-unit arc, digital-minds toolbox, cross-cutting debates",
        "- [glossary.md](glossary.md): every important term, linked to where it's introduced",
        "- `units/<unit>/unit.md`: unit overview with throughline, concept map, techniques and trade-offs, self-test questions",
        "- `units/<unit>/<section>/synthesis.md`: section synthesis with core argument, reading map, debates, study paths, discussion questions",
        "- `units/<unit>/<section>/page.md`: the BlueDot page verbatim, with the course's \"why read this\" guide and exercises (answers behind spoilers)",
        "- `units/<unit>/<section>/readings/`: one deep summary per assigned reading",
        "- `units/<unit>/<section>/references/`: notes on links embedded in page text, reading guides and exercises",
        "- `sources/`: full extracted text of every source (index and original URLs: `sources/manifest.json`), for exact details. "
        "These are copies of third-party works and remain the property of their authors and publishers; "
        "they are included for study reference, so follow each source's own terms before reusing them.",
        "",
        f"Scraped on {w['fetchDate']}.",
        "",
        "## Course map",
        "",
    ]
    for n in sorted(units):
        u = units[n]
        out += [f"### Unit {n}: {u['title']}", "", f"[Unit overview]({u['dir']}/unit.md)", ""]
        for s in [s for s in w["sections"] if s["unit"] == n]:
            est = f" · {s['estimatedTime']} min" if s.get("estimatedTime") else ""
            out += [f"#### {s['id']} {s['title']}", "",
                    f"[Synthesis]({s['dir']}/synthesis.md) · [Page & exercises]({s['dir']}/page.md){est}"
                    f"{' · ' + str(s['numExercises']) + ' exercises' if s['numExercises'] else ''}", ""]
            rs = readings_by_section.get(s["id"], [])
            if rs:
                out += ["| Reading | Priority | Time | Takeaway | Fact-checked |", "|---|---|---|---|---|"]
                for r in rs:
                    fm = frontmatter(ROOT / r["summaryFile"]) if (ROOT / r["summaryFile"]).exists() else {}
                    cov = fm.get("source_coverage", "?")
                    coverage[cov] += 1
                    if cov != "full":
                        not_full.append((r, cov))
                    v = verdicts.get(r["id"], {}).get("verdict")
                    check = {"accurate": "✓", "fixed-minor": "✓ (minor fixes)", "fixed-major": "✓ (major fixes)",
                             "unverifiable": "unverifiable"}.get(v, "—")
                    time = f"{r['timeMins']} min" if r.get("timeMins") else ""
                    out.append(f"| [{cell(r['title'])}]({r['summaryFile']}) | {r['priority']} | {time} | "
                               f"{cell(fm.get('takeaway', ''))} | {check} |")
                out.append("")
            xs = refs_by_section.get(s["id"], [])
            if xs:
                out += ["Notes on linked pages: " + " · ".join(
                    f"[{cell(x['anchor'] if x['kind'] == 'inline-link' else Path(x['summaryFile']).stem)}]({x['summaryFile']})"
                    for x in xs), ""]

    n_ref_notes = sum(len(v) for v in refs_by_section.values())
    v_counts = Counter(v["verdict"] for v in verdicts.values())
    unavailable = [r["url"].split("?X-Amz")[0].split("?response-content")[0] for r in manifest.values()
                   if r.get("status") != "ok"]
    out += [
        "## How this was built",
        "",
        f"- **Scrape:** the course's structured page data (Next.js `__NEXT_DATA__`) for all {len(w['sections'])} sections, "
        "plus the client-rendered 8.2 Next steps page captured in a browser; "
        f"{len(links)} link occurrences classified as assigned readings ({kinds['resource']} resources"
        f"{videos}), "
        f"references ({tiers['reference']} links in page text, reading guides and exercises) and "
        f"{tiers['link-only']} link-only items.",
        "- **Sources:** HTML → markdown, PDFs via pdftotext, Google Docs via their text export, YouTube transcripts via yt-dlp, "
        "LessWrong/EA Forum via their GraphQL API, OSF preprints via the OSF API. Papers behind publisher bot walls "
        "(PhilPapers, Springer, Wiley, SSRN, …) were replaced with open copies (arXiv, author pages) where one could be found; "
        "a few JS-only pages (tools, maps, resource lists) were captured in a browser.",
        f"- **Reading summaries:** {len(w['readings'])}, written by Claude Haiku 5.5 from the source text plus the section page "
        f"({len(w['readings']) - len(not_full)} from the full source; the rest are listed under Caveats).",
        f"- **Fact-checks:** an independent Haiku 5.5 agent re-read the source for each Core reading and corrected the summary in place "
        f"({len(verdicts)} verdicts recorded: {v_counts.get('fixed-minor', 0)} minor fixes, {v_counts.get('fixed-major', 0)} major fixes, "
        f"{v_counts.get('accurate', 0)} accurate as written, {v_counts.get('unverifiable', 0)} unverifiable). "
        "Further/Maybe readings were not independently checked.",
        f"- **Reference notes:** {n_ref_notes}, written by Claude Haiku 5.5. {n_dropped} low-value links (duplicates of assigned "
        "readings, the licence, exercise tools) were not summarised; in `page.md` duplicates point to the assigned reading's summary.",
        "- **Syntheses:** section, unit, course and glossary written by Claude Sonnet 5.5 from the summaries.",
        "",
        "## Caveats",
        "",
        f"- Organisation, fellowship and program details were captured on {w['fetchDate']}; deadlines and open roles go stale.",
        "- Many Core readings are excerpts (the course guide names the sections to read); summaries cover the assigned "
        "excerpt in depth and the rest of the work briefly.",
        f"- Source coverage of reading summaries: {dict(coverage)}.",
    ]
    if not_full:
        out.append("- Readings not summarised from the full source: " + "; ".join(
            f"[{cell(r['title'])}]({r['summaryFile']}) ({cov})" for r, cov in not_full) + ".")
    if unavailable:
        out.append("- Sources that couldn't be fetched: " + ", ".join(unavailable) + ".")
    out += [
        "",
        "## Rebuilding",
        "",
        "```bash",
        "python3 tools/build_dataset.py scrape   # refresh course/course.json from bluedot.org",
        "python3 tools/build_dataset.py layout   # rewrite page.md files and course/links.json",
        "python3 tools/build_worklist.py work    # rebuild course/worklist.json and the agent specs",
        "python3 tools/apply_overrides.py        # re-apply drops and the client-rendered 8.2 page text",
        "python3 tools/build_dataset.py fetch    # download sources (refetch: only failed ones)",
        "python3 tools/check_links.py            # report broken relative links (--fix repairs depth errors)",
        "python3 tools/build_readme.py           # regenerate this index",
        "```",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(out))
    print(f"README.md written: {len(w['readings'])} readings, {n_ref_notes} reference notes, coverage {dict(coverage)}")


if __name__ == "__main__":
    main()
