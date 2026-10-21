#!/usr/bin/env python3
"""Write course/work/_workflow_args.json, the `args` object for tools/ingest-workflow.js."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FORMAT_NOTES = """- Excerpt assignments: many readings are excerpts. When the course guide (in the spec's "guide" and the page) says "Read only" certain sections, or the URL has a #fragment / the title names a section, still read the whole source, but make the Detailed summary a thorough walk-through of the assigned part (that is what learners read) and end it with a short "Beyond the assigned excerpt" subsection on the rest. Say in "Where this sits in the course" exactly which part is assigned.
- Philosophy papers and essays: reconstruct each main argument step by step (premises -> conclusion), the objections the author considers and their replies, and the position's place in the debate (who it agrees and disagrees with). Use "Techniques & methods explained" for the argumentative moves, frameworks, tests or methods the paper explains.
- Course glossaries (written by the course team): list every term with its definition as the course uses it (paraphrased), grouped sensibly; replace "Techniques & methods explained" with "How the terms fit together" and keep "Pros, cons & trade-offs" short (contested definitions, ambiguities). About 600-1,200 words.
- Course-team primers (written by the course team for this course): they frame the unit; follow their structure closely and capture every framework, list, case and open question they present, since the exercises draw on them.
- Lab documents (constitutions, commitments, system cards): focus on the parts relevant to AI welfare, moral status and model wellbeing that the course guide points to, with concrete commitments, evaluations and findings.
- Empirical studies and surveys: give the design (sample, method, measures), the main quantitative results and the stated limitations.
- Sources that are abstract-only or were recovered from a preprint/alternate copy: say so in the file and set source_coverage accordingly."""

THEME_HINTS = ("over- vs under-attribution of moral status; consciousness vs sentience vs agency as routes to moral standing; "
               "computational functionalism vs biological naturalism; the evidential weight of behaviour, self-reports and "
               "interpretability; AI welfare vs AI safety; acting under deep uncertainty (precaution, proportionality, expected value); "
               "law, rights and personhood; public perception, relational AI and societal division")


def main():
    w = json.loads((ROOT / "course/worklist.json").read_text())
    c = json.loads((ROOT / "course/course.json").read_text())["course"]
    args = {
        "root": w["root"],
        "courseTitle": c["title"],
        "courseShape": f'{len(c["units"])} units of about 2 hours each, developed by Cambridge Digital Minds',
        "today": "October 2026",
        "fetchDate": w["fetchDate"],
        "formatNotes": FORMAT_NOTES,
        "themeHints": THEME_HINTS,
        "sections": [s["id"] for s in w["sections"]],
        "items": json.loads((ROOT / "course/work/_args.json").read_text()),
        "core": [r["id"] for r in w["readings"] if r["priority"] == "Core"],
        "dropped": [x["id"] for x in w["refs"] if x.get("dropped")],
    }
    (ROOT / "course/work/_workflow_args.json").write_text(json.dumps(args, ensure_ascii=False))
    print(len(args["items"]), "items,", len(args["core"]), "core,", len(args["dropped"]), "dropped")


if __name__ == "__main__":
    main()
