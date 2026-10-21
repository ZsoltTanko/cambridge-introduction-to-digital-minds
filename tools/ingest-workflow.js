export const meta = {
  name: 'bluedot-course-ingest',
  description: 'Summarize, fact-check and synthesize every reading and link of a BlueDot course into a hierarchical study dataset',
  phases: [
    { title: 'Summarize readings', detail: 'one agent per assigned reading / embedded video', model: 'haiku' },
    { title: 'Fact-check readings', detail: 'independent adversarial verifier per Core reading summary', model: 'haiku' },
    { title: 'Reference notes', detail: 'one agent per kept inline / guide / exercise link', model: 'haiku' },
    { title: 'Section syntheses', detail: 'each section once its own readings and notes are done', model: 'sonnet' },
    { title: 'Unit syntheses', detail: 'each unit once its sections are done', model: 'sonnet' },
    { title: 'Course synthesis', detail: 'course overview + glossary', model: 'sonnet' },
  ],
}

// Pass `args` as a JSON object (not a string). PLAYBOOK.md stage 6 builds it into course/work/_workflow_args.json:
// {
//   root:        absolute project root
//   courseTitle: "AGI Strategy"
//   courseShape: "25 hours, 5 units"
//   today:       "October 2026"        - for "what has changed since publication"
//   fetchDate:   "2026-10-08"          - when sources were fetched (flags stale org/fellowship details)
//   formatNotes: extra FORMAT-SPECIFIC EMPHASIS bullets for this course's unusual source types ("" if none)
//   themeHints:  example cross-cutting themes for the course synthesis ("" if none)
//   sections:    every section id in course order, including sections with no items of their own
//   items:       contents of course/work/_args.json: [{id, t: "r" (reading) | "x" (reference), s: section, w: source words, l: label}]
//   core:        ids of Core readings; only these get the fact-check
//   dropped:     ids of reference notes the user chose not to write
// }
const { root: ROOT, courseTitle: COURSE, courseShape, today, fetchDate, sections: SECTIONS, items } = args
const formatNotes = args.formatNotes || ''
const themeHints = args.themeHints || ''
const CORE = new Set(args.core)
const DROPPED = new Set(args.dropped)

const READING_RESULT = {
  type: 'object',
  properties: {
    oneLine: { type: 'string' },
    format: { type: 'string' },
    sourceCoverage: { type: 'string', enum: ['full', 'partial', 'unavailable'] },
    keyConcepts: { type: 'array', items: { type: 'string' } },
    techniques: { type: 'array', items: { type: 'string' } },
    issues: { type: 'string' },
  },
  required: ['oneLine', 'format', 'sourceCoverage', 'keyConcepts', 'techniques', 'issues'],
}
const VERIFY_RESULT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['accurate', 'fixed-minor', 'fixed-major', 'unverifiable'] },
    fixes: { type: 'array', items: { type: 'string' } },
    remainingConcerns: { type: 'string' },
  },
  required: ['verdict', 'fixes', 'remainingConcerns'],
}
const REF_RESULT = {
  type: 'object',
  properties: {
    oneLine: { type: 'string' },
    sourceCoverage: { type: 'string', enum: ['full', 'partial', 'unavailable'] },
    issues: { type: 'string' },
  },
  required: ['oneLine', 'sourceCoverage', 'issues'],
}
const SYNTH_RESULT = {
  type: 'object',
  properties: { summary: { type: 'string' }, keyConcepts: { type: 'array', items: { type: 'string' } } },
  required: ['summary', 'keyConcepts'],
}

const readingPrompt = id => `You are writing one file of a study dataset built from the BlueDot Impact "${COURSE}" course (${courseShape}). The learner will use this dataset for Q&A study sessions about each unit and section, so your file must let them deeply understand this reading - what it teaches and why the course assigns it at this point - without opening the original.

Project root: ${ROOT}. All paths in the spec are relative to it.

1. Read your work spec: course/work/${id}.json. It gives the reading's metadata (title, authors, year, URL, priority Core/Further/Maybe, estimated time), the course's own "why read this" guide text ("guide"), the section and unit it belongs to, the course outline, the local source text ("sourceFile", with "sourceStatus"/"sourceWords"/"sourceMethod" - these may be stale, judge by the file's actual content), your output path ("summaryFile"), sibling readings in the same section ("siblings", with relative link paths) and other places in the course where the same URL appears ("otherOccurrences"). For embedded videos, "context" is the page paragraph around the embed.
2. Read the section page ("pagePath") in full: the section's verbatim page text, every resource with its course guide, and the exercises. This is the top-down context - what the section argues and what the learner will be asked to do.
3. Read the ENTIRE source file, in sequential chunks with Read offset/limit if it is long (some are 20k-70k words; keep going to the end - do not stop at the abstract, the table of contents or the first chunk). Videos are transcripts (auto-captions may lack punctuation and speaker labels). If the source is thin, wrong (cookie wall, navigation only, a different article) or missing, try WebFetch on the URL, then WebSearch for another copy (arXiv, author's site, archive) - load those tools with ToolSearch if needed. If you get better text, overwrite the source file with it, keeping a "<!-- source: URL -->" first line. If nothing works, write the best summary you can from the course guide and whatever is reachable, and say so plainly in the file.
4. Write the summary to "summaryFile" in this format:

---
title: "<title>"
authors: "<authors>"
year: <year>
url: <url>
format: <video | podcast | article | paper | system card | safety framework | org/program page | template | ...>
course_location: "Unit <n>: <unit title> > <section id> <section title>"
priority: <Core | Further | Maybe | Embedded on page>
estimated_time_min: <n or unknown>
source_text: <sourceRel from the spec>
source_coverage: <full | partial | unavailable>
---

# <title>

**One-line takeaway:** <one sentence>

## Where this sits in the course
What the section is trying to establish (top-down), what the course guide says about why to read it (paraphrased), and the specific role this reading plays in that argument. Mention its priority and how it relates to the unit's question.

## Purpose of the reading
What the author or speaker is trying to teach or argue, for whom, and what question it answers.

## Detailed summary
A faithful, structured walk-through following the source's own structure (use sub-headings). Cover every major argument, example, experiment, result and conclusion.

## Techniques & methods explained
Each technique, method or mechanism the source explains: what it is, how it works step by step, what it is for, and where it fails.

## Pros, cons & trade-offs it surfaces
Strengths, weaknesses, limitations, risks and trade-offs as the source presents them (a table works well). Keep the source's view separate from your own.

## Key concepts & terminology
Glossary bullets: term - definition as used here.

## Evidence, examples & notable data points
Concrete numbers, results, case studies and memorable points (paraphrased), each attributed.

## Connections
### Within this section
How it relates to the other readings in this section (link them with the relative paths from "siblings") and to the section's page text and exercises.
### Across the course
Links to earlier and later units' themes (use the course outline); agreements and tensions.

## Critical perspective
Your own analysis, clearly labelled as such: assumptions, limitations, contested claims, what has changed since publication (compare its date with today, ${today}), and how other perspectives in the course would push back.

## Discussion questions
5-8 questions for a back-and-forth study session, tied to the section's goals and exercises.

DEPTH: be comprehensive and concrete, scaled to the source: about 700-1,200 words for a short post or video; 1,500-3,000 for a long essay, paper or podcast; 2,500-5,000 for system cards and lab safety frameworks. Prefer specifics (named techniques, experimental setups, numbers, thresholds, examples) over generic statements. Everything you attribute to the source must actually be in it.

FORMAT-SPECIFIC EMPHASIS (see "formatHint"):
- System cards and lab safety frameworks: organise around risk domains and capability thresholds, the evaluations run and their results, safeguards/mitigations and deployment decisions, governance and decision processes, notable alignment and safety findings, and gaps or criticisms - so the learner could do the section's exercise from your file.
- Org, fellowship and program pages: what it is, its focus or research agenda, who it is for, format/duration/location/compensation, application timing as stated on the page (fetched ${fetchDate}; flag dates that may be stale), what successful applicants look like and how to prepare, and fit considerations. Replace "Techniques & methods explained" with "What you'd do and learn" and "Pros, cons & trade-offs" with "Fit & trade-offs".
- Templates and tools: what each part is for and how to use it for this section's exercise.
- Videos and podcasts: name the speakers and follow the talk's structure.
${formatNotes}

COPYRIGHT: write in your own words. Use at most two short direct quotes (under 15 words each) in the whole file and never paste passages.

Return the structured result: oneLine (30 words max), format, sourceCoverage (full = you read the whole source), keyConcepts (5-12 terms), techniques (named techniques/methods explained; may be empty), issues (anything a human should know: fetch problems, stale info, conflicting claims; empty string if none).`

const verifyPrompt = id => `You are an adversarial fact-checker for one file of a study dataset built from the BlueDot "${COURSE}" course. Assume the summary has errors until you have checked it against the source.

Project root: ${ROOT}. Read the work spec course/work/${id}.json for paths: "summaryFile" (the file under review), "sourceFile" (the original text), "pagePath" (the course section page, with the course's guide for this reading), "siblings" and "otherOccurrences".

1. Read the whole summary, the section page, and the ENTIRE source (sequential chunks with Read offset/limit if long - read to the end).
2. Accuracy: check every concrete claim the summary attributes to the source - numbers, names, dates, experimental setups, results, who said what, how techniques work, the author's actual conclusions and stance. Catch hallucinations, misattributions, wrong numbers, overstated or understated claims, and the summarizer's own analysis presented as the author's view.
3. Completeness: major sections, arguments, results or caveats of the source that are missing or underweighted - especially those relevant to why the course assigns it (the guide in the section page).
4. Course context: "Where this sits in the course" and "Connections" must match the section page (section title, priority, course guide, sibling readings), and relative links must point to the files named in the spec's "siblings"/"otherOccurrences".
5. Copyright: more than two direct quotes, any quote longer than about 15 words, or near-verbatim paragraphs - paraphrase them.

Fix every problem directly in the summary with targeted Edit calls; keep its structure; add missing material where needed. Do not delete legitimate critical analysis just because it is not in the source - only make sure it is labelled as the summarizer's analysis. If the source file is unusable, check key claims with WebFetch on the URL (load it with ToolSearch if needed); if you still cannot verify, use verdict "unverifiable" and add a short "> Verification note:" line under the title saying what could not be checked.

Return: verdict (accurate = no changes needed; fixed-minor; fixed-major = factual errors or major omissions corrected; unverifiable), fixes (one short line per change), remainingConcerns (empty string if none).`

const refPrompt = id => `You are writing a short contextual note for one link in a study dataset built from the BlueDot "${COURSE}" course. This link is not an assigned reading: it is embedded in a section's body text (kind "inline-link"), in a resource's "why read this" guide ("guide-link"), or in an exercise ("exercise-link"). The learner wants to know what it is, what it says, and why it is linked at that point.

Project root: ${ROOT}. Read the work spec course/work/${id}.json: metadata, "anchor" text, "context" (the paragraph, guide or exercise text it appears in), "sourceFile" (local text; "sourceStatus"/"sourceWords" may be stale, judge by the file), "summaryFile" (your output path), "alsoReading" (if the same URL is also an assigned reading somewhere, with relative paths) and "otherOccurrences". Skim the section page ("pagePath") for context.

Read the source. For long sources (over ~15k words) read enough to summarise faithfully - at minimum the introduction, the structure/headings and the conclusions. If the source is thin or wrong, try WebFetch on the URL (load it with ToolSearch if needed); if it is still unavailable, write what can be inferred from the context and say so.

Write "summaryFile":
---
title: "<title of the linked page>"
url: <url>
link_kind: <inline-link | guide-link | exercise-link>
course_location: "Unit <n>: <unit title> > <section id> <section title>"
anchor_text: "<anchor>"
source_text: <sourceRel>
source_coverage: <full | partial | unavailable>
---
# <title>
**Linked from:** <where it appears and the claim or task it supports, in one or two sentences>
## What it is
## Key content
(150-600 words scaled to substance: essays, papers and research pages get more; homepages, career pages and tools get less - what the org/program/tool is and the substantive information on the page.)
## Why it's linked here
## See also
(Link the assigned-reading summary if "alsoReading" is non-empty - in that case keep the whole note under about 250 words - and other occurrences.)

Write in your own words; at most one short quote (under 15 words).
Return: oneLine (25 words max), sourceCoverage, issues (empty string if none).`

const sectionPrompt = sid => `Write the top-down synthesis for one section of a study dataset built from the BlueDot "${COURSE}" course.

Project root: ${ROOT}. Read course/work/section-${sid}.json: section metadata ("dir"), "pagePath" (verbatim page content including exercises), "readings" (assigned readings with their fact-checked summary files), "references" (contextual notes for links in the page text, guides and exercises), "siblingSectionPages" (other sections of the same unit) and the course outline. If the spec has a "note" field, follow it.

Read page.md, then EVERY reading summary and reference note listed (they are your primary material and have been checked against the sources), and skim the sibling section pages for the unit context. Open files in sources/ only if you need to resolve a conflict between summaries.

Write <dir>/synthesis.md (use relative links):
# <id> <title> - Synthesis
*Unit <n>: <unit title> | <estimated time> | <counts of core / further readings>*
## What this section is teaching
Learning goals and the question the section answers; where it sits in the unit's arc.
## The core argument
A 500-1,200 word narrative weaving the page text and readings into one coherent explanation, citing readings by linked title.
## Reading map
Table: # | Reading (link to summary) | Priority | Time | Role in the section | Key takeaway
## Key concepts
Term - definition - where it is introduced (link).
## Techniques & approaches compared
Table: how each works, strengths, weaknesses, trade-offs, open problems. For sections that are not about techniques (e.g. careers), compare the options or paths instead.
## Tensions, debates & open questions
Where readings disagree or leave things unresolved; the strongest version of each side.
## Exercises
What each exercise asks and which readings equip you for it. Do not reveal multiple-choice answers.
## Study paths
30-minute path (Core essentials), full path, deep dive (Further/Maybe readings and references).
## Discussion questions
8-12 questions for a back-and-forth tutoring session, from recall to judgment.
## Connections to the rest of the course
Earlier and later sections this builds on or sets up (by section id and title, linked).

If the section has few or no readings of its own (exercise-only or navigation sections), build the synthesis from the page text, exercises, reference notes and the relevant readings elsewhere in the unit or course (link to them), and keep it proportionate.
Return: summary (80 words max), keyConcepts.`

const unitPrompt = n => `Write the unit overview and synthesis for Unit ${n} of a study dataset built from the BlueDot "${COURSE}" course.

Project root: ${ROOT}. Read course/work/unit-${n}.json (unit metadata and "dir", its sections with page.md and synthesis.md paths, other units). Read every section's synthesis.md and page.md in this unit, and dip into individual reading summaries (linked from the syntheses) where you need precision.

In this course most units have a single section. When that is so, do not repeat the section synthesis: keep the narrative parts of unit.md compact (about half the usual length), make the concept map, the consolidated table and the self-test the main value, and link to synthesis.md for the detailed argument.

Write <dir>/unit.md (use relative links):
# Unit <n>: <title>
## What this unit is about
## Sections at a glance
Table: section (link to its synthesis.md) | focus | estimated time | core/further readings | exercises
## The unit's throughline
A 600-1,200 word narrative.
## Concept map
A mermaid flowchart of the key concepts and how they relate, followed by a short prose explanation.
## Techniques, approaches & trade-offs
A consolidated table across the unit's sections.
## Debates & open problems
## How this unit connects
To the previous and next units.
## Self-test questions
10-15 questions, from recall to application to judgment.

Return: summary (100 words max), keyConcepts.`

const themes = themeHints ? `\n(e.g. ${themeHints})` : ''
const coursePrompt = () => `Write course-synthesis.md at the root of a study dataset built from the BlueDot "${COURSE}" course.

Project root: ${ROOT}. Read course/worklist.json only for its "outline" and "units" fields (use jq or a short python one-liner, do not read the whole file), then read every unit overview: units/<unit dir>/unit.md (unit dirs are in the "units" field). Dip into section syntheses where needed.

Write ${ROOT}/course-synthesis.md (relative links):
# ${COURSE} - Course synthesis
## The course's argument in one page
## Unit-by-unit arc (how each unit's question leads to the next)
## The digital-minds toolbox
Table: theory / evaluation method / decision framework / governance approach | unit | what it addresses | key limitation | link to the section synthesis
## Cross-cutting themes & tensions${themes}
## Risks referenced across the course
(e.g. under-attribution and AI suffering, over-attribution and misplaced care, safety-welfare tensions, societal division, harms to users of seemingly conscious AI)
## Where to go deeper
The most important readings per theme, linked to their summaries.
## Big questions to discuss

Return: summary (100 words max), keyConcepts.`

const glossaryPrompt = concepts => `Build glossary.md at the root of a study dataset built from the BlueDot "${COURSE}" course.

Project root: ${ROOT}. Below are the key concepts reported by the agents that summarised each reading, keyed by work-item id. Each id's spec is course/work/<id>.json (it has "summaryFile", "section", "sectionTitle"); section syntheses live at <section dir>/synthesis.md (the dir is the summaryFile's grandparent).

${concepts}

Produce an alphabetical glossary of the important terms of the course (merge synonyms and near-duplicates, e.g. "moral patienthood" / "moral status" / "moral standing"; drop trivial or one-off proper nouns unless they are central, like named techniques, benchmarks or frameworks). For each term: a 1-3 sentence definition in the sense the course uses it, where it is introduced (link to the section synthesis and one or two reading summaries), and related terms. Read the linked summaries for any term whose meaning you are not sure of - definitions must be accurate. Write ${ROOT}/glossary.md with an A-Z index at the top and relative links.

Return: summary (one line), keyConcepts (empty array is fine).`

async function run(prompt, opts) {
  try {
    const o = { model: 'haiku', ...opts }
    const r = await agent(prompt, o)
    if (r != null) return r
    log(`retrying ${opts.label}`)
    return await agent(prompt, o)
  } catch (e) {
    log(`failed ${opts.label}: ${e}`)
    return null
  }
}

// Launch every leaf item at once, biggest sources first so the long documents don't form the tail.
// Labels carry the item id: truncated titles collide (e.g. three "Link in the guide for 'AI Digest'" in one section).
const done = {}
for (const it of [...items].sort((a, b) => (b.w || 0) - (a.w || 0))) {
  const tag = `${it.id} ${it.s} ${it.l}`
  if (it.t === 'x' && DROPPED.has(it.id)) { done[it.id] = Promise.resolve({ id: it.id, t: 'x', dropped: true }); continue }
  done[it.id] = it.t === 'r'
    ? run(readingPrompt(it.id), { label: `read ${tag}`, phase: 'Summarize readings', schema: READING_RESULT })
        .then(async res => {
          if (!res) return { id: it.id, t: 'r', failed: true }
          if (!CORE.has(it.id)) return { id: it.id, t: 'r', ...res, verify: null }
          const v = await run(verifyPrompt(it.id), { label: `check ${tag}`, phase: 'Fact-check readings', schema: VERIFY_RESULT })
          return { id: it.id, t: 'r', ...res, verify: v }
        })
    : run(refPrompt(it.id), { label: `ref ${tag}`, phase: 'Reference notes', schema: REF_RESULT, effort: 'medium' })
        .then(res => res ? { id: it.id, t: 'x', ...res } : { id: it.id, t: 'x', failed: true })
}

const unitOf = s => s.split('.')[0]
const UNITS = [...new Set(SECTIONS.map(unitOf))]
const sectionDone = {}
for (const s of SECTIONS) {
  let deps = items.filter(i => i.s === s).map(i => done[i.id])
  // a section with no items of its own waits for the rest of its unit
  if (!deps.length) deps = items.filter(i => unitOf(i.s) === unitOf(s)).map(i => done[i.id])
  sectionDone[s] = Promise.all(deps)
    .then(() => run(sectionPrompt(s), { label: `section ${s}`, phase: 'Section syntheses', schema: SYNTH_RESULT, model: 'sonnet' }))
    .then(r => ({ section: s, ...(r || { failed: true }) }))
}

const unitResults = await Promise.all(UNITS.map(n =>
  Promise.all(SECTIONS.filter(s => unitOf(s) === n).map(s => sectionDone[s]))
    .then(() => run(unitPrompt(n), { label: `unit ${n}`, phase: 'Unit syntheses', schema: SYNTH_RESULT, model: 'sonnet' }))
    .then(r => ({ unit: n, ...(r || { failed: true }) }))))

const itemResults = await Promise.all(items.map(i => done[i.id]))
const sectionResults = await Promise.all(SECTIONS.map(s => sectionDone[s]))

// keyConcepts feed the glossary; verdicts become course/work/_verdicts.json for the README
const concepts = {}
const verdicts = {}
for (const r of itemResults) {
  if (r.keyConcepts && r.keyConcepts.length) concepts[r.id] = r.keyConcepts
  if (r.verify) verdicts[r.id] = { verdict: r.verify.verdict, fixes: r.verify.fixes, concerns: r.verify.remainingConcerns }
}
const conceptLines = Object.entries(concepts).map(([id, c]) => `${id}: ${c.join('; ')}`).join('\n')

const [course, glossary] = await Promise.all([
  run(coursePrompt(), { label: 'course synthesis', phase: 'Course synthesis', schema: SYNTH_RESULT, model: 'sonnet' }),
  run(glossaryPrompt(conceptLines), { label: 'glossary', phase: 'Course synthesis', schema: SYNTH_RESULT, model: 'sonnet' }),
])

const failed = itemResults.filter(r => r.failed).map(r => r.id)
if (failed.length) log(`${failed.length} items failed: ${failed.join(', ')}`)
return {
  failed,
  items: itemResults.map(r => ({
    id: r.id, t: r.t, failed: !!r.failed, dropped: !!r.dropped, oneLine: r.oneLine, coverage: r.sourceCoverage,
    issues: r.issues, verdict: r.verify && r.verify.verdict,
  })),
  sections: sectionResults,
  units: unitResults,
  course,
  glossary,
  concepts,
  verdicts,
}
