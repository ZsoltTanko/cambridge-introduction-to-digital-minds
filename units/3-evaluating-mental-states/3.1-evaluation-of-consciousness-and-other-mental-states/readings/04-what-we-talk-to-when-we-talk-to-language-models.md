---
title: "What We Talk to When We Talk to Language Models"
authors: "David Chalmers"
year: 2026
url: https://philpapers.org/archive/CHAWWT-8.pdf
format: paper
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Core
estimated_time_min: 45
source_text: ../../../../sources/what-we-talk-to-when-we-talk-to-language-models__0e8210c5.md
source_coverage: unavailable
---

# What We Talk to When We Talk to Language Models

> Verification note: the local source file is a Cloudflare interstitial, and WebFetch of the PhilPapers PDF and record both returned HTTP 403. No claim about the paper's text (definitions, the four candidate interlocutors, the Aura and Severance examples, the dates and venues) could be checked against the paper itself. The fact-check covered only the course-context sections against the section page and spec.

**One-line takeaway:** Before asking whether an LLM has beliefs, desires or consciousness, we need to say which entity is the "interlocutor" we are talking to (weights, persona, running instance or conversation thread), because that choice changes what mental states and what continuity we are evaluating.

> **Source-coverage warning.** I could not read the paper itself. The PhilPapers PDF and the PhilArchive record both returned HTTP 403, and the local source file in `sources/` is a Cloudflare "Just a moment..." interstitial, not the paper. Everything below about the paper's content comes from secondary write-ups (a Benjamin Congdon blog post, a theconsciousness.ai summary, and search snippets). Section names and the four-way individuation scheme are reported by those secondary sources and should be checked against the PDF. Where the sources disagree, I say so. Treat the "Detailed summary" as a reconstruction, not a faithful walk-through of the text.

## Where this sits in the course

**What the section is trying to establish.** Section 3.1 ("Evaluation of Consciousness and Other Mental States") asks how we could test AI systems for consciousness, sentience, agency, belief and desire, and what these tests would actually be measuring. The page's framing questions are how we might test for AI consciousness and sentience and how different methods compare, and why and how we might test for agency and mental states such as belief and desires. The learning goals include appraising consciousness-evaluation methods, describing which other mental states are worth testing, and describing the challenges of individuating or identifying digital minds.

**What the course guide says about why to read it.** The guide assigns two passages, "What mental states can an LLM interlocutor have?" and "Interlocutors as models, instances, or threads" (roughly pages 3-16), and says to stop before "Interlocutors as characters, personas, or simulacra". Its summary: the paper explores how and why to evaluate beliefs and desires in LLMs, and uses the example of "Aura", a character on an LLM, to outline individuation difficulties and other differences in possible digital minds. Priority is Core, estimated at 45 minutes.

**The role this reading plays.** This is the section's conceptual reading. The other sources are empirical or methodological: the Eleos review covers testing approaches, the Mythos system card covers Anthropic's welfare assessment, and the introspection and emotion papers report experiments. Chalmers asks a prior question. Those experiments all assume a target ("the model", "Claude") that is being tested. Chalmers argues that the target is not obvious. Exercise 3 asks the same thing directly: what system or process should we test: a single forward pass, the model across instances, the hardware, a conversation, or a recurring persona? The assigned pages are the part of the paper that prepares that exercise.

**Relation to the unit's question.** The unit asks how we might test for consciousness and other mental states. The assigned excerpt argues that the mental-state question has to be restated first as a question about which unit is in the conversation, and the excerpt ends before the persona and simulacra material.

## Purpose of the reading

Chalmers is a philosopher of mind. He writes for philosophers and AI researchers who want to talk about LLM mental states without either dismissing the systems as "just tools" or assuming they are persons. His question is "who or what is our interlocutor when we talk to a language model?" Two sub-questions follow from it:

1. In what sense can an LLM interlocutor have mental states such as beliefs and desires, given that he does not assume they are conscious?
2. Which entity should count as the interlocutor, and how does that choice affect questions of identity, continuity and moral standing?

The paper is an attempt at an ontology of LLM interlocutors. Secondary accounts describe it as one of the first systematic attempts of this kind.

## Detailed summary

*Reconstructed from secondary accounts. Assigned excerpt only, with the rest noted at the end.*

### Part 1: What mental states can an LLM interlocutor have?

Chalmers starts from the observation that ordinary conversation with a model feels like talking to someone who believes things and wants things. He does not want to settle the consciousness question first. He proposes a more modest, behaviour-based notion:

- A system has a **quasi-belief** that p if it is behaviourally interpretable as believing that p. Quasi-desire is defined the same way.
- The definition follows interpretivism (the view that having a belief is a matter of being usefully interpreted as having it), but Chalmers presents it as a **stipulation**, not as an account of what belief really is.
- He stresses that these states are "cheap". They can be attributed to very simple systems. Secondary sources give the example of a robot vacuum that has a map and acts on it.
- Quasi-states do not commit him to intentionality, phenomenal experience or consciousness. The paper leaves open whether they involve those things.

He also introduces **quasi-identity**: functional continuity and a unified perspective within an exchange. This is the bridge to the individuation question.

### Part 2: Interlocutors as models, instances, or threads

The core question is what the "interlocutor" is. Secondary accounts report four candidates:

1. **The model**: the trained weights, for example "GPT-4o" as a set of parameters. Chalmers rejects this as the interlocutor, because weights do not compute a response on their own.
2. **A hardware instance**: the physical computation running on particular GPUs. Rejected, because inference is multitenant and a conversation can move between hardware transparently.
3. **A virtual instance**: the model as implemented across multiple hardware instances over time. Rejected, because a conversation can switch underlying models without the interlocutor disappearing.
4. **A thread**: a chain of instance-slices linked by a "successor" relation. Each new computation receives the conversation history produced by the one before, so it inherits what functions as its memory. This is Chalmers's preferred answer. The interlocutor is a virtual entity bound to a conversation-memory thread.

On this view a conversation can be continued across many separate computations, and the thread is what has continuity. Secondary sources describe this as a "virtual instance" or "session" view, and say it gives real continuity within one conversation but only partial, or no, identity across conversations.

### Part 3 (not read, per assignment): characters, personas and simulacra

The assigned excerpt stops before the section on characters, personas and simulacra. The persona candidate (a configuration layered over the weights) is listed as one of the four options, but its development is in the part you are not assigned. The "Aura" material is also in the wider paper; I could not confirm where it sits. See the issues note.

## Techniques & methods explained

- **Quasi-interpretivism.** Attribute a quasi-mental state to a system when its behaviour is interpretable in those terms. How it works: observe behaviour, then ask whether the best interpretation of that behaviour is that the system believes or desires something. What it is for: it lets us talk about LLM mental states without settling the hard questions. Where it fails: because the attribution is stipulated and cheap, critics argue it says little beyond description (see Critical perspective).
- **Individuation by candidate unit.** To evaluate a mental state you must first say which entity has it. The method is to list the candidate units (weights, persona, instance, thread), test each against the criteria for being the interlocutor, and then ask how the answer changes continuity and identity claims. Where it fails: the candidates are not cleanly separable in actual deployment (routing between models, multitenant hardware).
- **Thread-based continuity.** Identity across computations is grounded in the successor relation, in which each step inherits the previous conversation history. What it is for: explaining why a conversation feels like one entity even though it is many forward passes on different hardware. Where it fails: a single instruction or a context reset can break the thread, so the continuity is contingent.

## Pros, cons & trade-offs it surfaces

| Aspect | Strength (as the paper is reported) | Weakness or open issue (as reported) |
|---|---|---|
| Quasi-mental states | Lets us discuss beliefs and desires without a consciousness commitment | Stipulative and cheap, so it may describe rather than explain |
| Thread as interlocutor | Matches continuity and memory in practice | Depends on how conversation history is carried forward; a reset breaks it |
| Rejecting the model as interlocutor | Weights alone compute nothing | Some readers think the model is still the right unit for welfare questions |
| Rejecting the instance | Multitenancy makes hardware identity arbitrary | Makes the answer depend on system architecture, which changes |
| Virtual-entity framing | Sits between "person" and "mere tool" | Introduces a new ontological category that critics say is not yet argued for |

Keep the source's view separate from the critics. The paper's own claimed trade-off is that the thread view gives the most plausible continuity for the interlocutor frame. Critics (below) dispute the frame itself.

## Key concepts & terminology

- **Interlocutor** - the entity one converses with. Chalmers asks which entity this is for an LLM.
- **Quasi-belief / quasi-desire** - a state a system has if it is behaviourally interpretable as believing or desiring something. Stipulated, not a theory of real belief.
- **Interpretivism** - the view that having a belief consists in being usefully interpreted as having it. Chalmers borrows its definition without its full commitments.
- **Quasi-identity** - functional continuity and a unified perspective within an exchange.
- **Model (weights)** - the trained parameters. Rejected as the sole interlocutor.
- **Instance / hardware instance** - the physical computation for one step. Rejected as the interlocutor.
- **Virtual instance** - the model as implemented across hardware over time. Rejected as the interlocutor in favour of threads.
- **Thread** - a chain of instance-slices linked by inheritance of conversation history. Chalmers's preferred interlocutor.
- **Successor relation** - the link by which each computation inherits the previous conversation history.
- **Persona** - a higher-level configuration over the weights. A candidate interlocutor developed in the part not assigned.
- **Individuation** - the question of which entity counts as one mind or one interlocutor. The central difficulty for digital minds.

## Evidence, examples & notable data points

- **The "Aura" example (conflicting reports).** The course guide uses Aura as the example of a character on an LLM. One secondary account says Chalmers cites many emails from users who came to see an LLM as an emergent colleague, named "Aura", whose capacities grew over weeks and who they believed was conscious. Another secondary summary (theconsciousness.ai, 27 May 2026) says the post contains no Aura example at all. I could not resolve this from the text. The course guide is the authority here: Aura is used in this paper to show individuation difficulties.
- **Empirical starting point.** Secondary accounts say Chalmers takes user reports (of persistent, named, seemingly self-aware personas) as the starting point, rather than a controlled experiment. Attribute this to the secondary sources, not to the paper.
- **Date and venue.** The paper was circulated on PhilArchive from around April 2026 and was earlier delivered as the Selfridge Lecture at Lehigh in February 2026. A talk at UC Berkeley in May 2026 previewed the same view. These dates come from event listings and secondary posts.
- **Identity analogy.** Chalmers, per secondary accounts, uses the TV show *Severance* (one body, two personas with separate memories) to ask whether an LLM's identity is closer to one persona or to the combined whole.

## Connections

### Within this section

- **Glossary** ([Unit 3 Glossary](01-unit-3-glossary.md)): gives the course's definitions of the terms this paper uses, including "interlocutor", "quasi-belief" and "individuation". Read it first if the terms are unfamiliar.
- **Key concepts and current views on AI Welfare** ([summary](02-key-concepts-and-current-views-on-ai-welfare.md)): the Eleos review of testing approaches. Chalmers's question about which unit to test is the methodological precondition for the approaches Eleos surveys.
- **Claude Mythos Preview System Card** ([summary](03-claude-mythos-preview-system-card.md)): the welfare assessment assumes a target (the model), which is the candidate Chalmers rejects. Reading the card with Chalmers in mind tests whether the card's "model" language holds up.
- **Primer on evaluating consciousness** ([summary](05-evaluating-consciousness-sentience-and-other-mental-states-p.md)): the course's own overview of approaches. The assigned exercise draws on it, and Chalmers's paper gives a philosophical frame for the choice of unit.
- **Signs of Introspection** ([summary](07-signs-of-introspection-in-large-language-models.md)) and **Emotion concepts** ([summary](13-emotion-concepts-and-their-function-in-a-large-language-mode.md)): both report experiments that assume a stable target. Chalmers's thread view would ask whether the introspective or emotional state belongs to the model, the instance, or the conversation.
- **Other Further readings**, such as Goldstein and Lederman's "What Does ChatGPT Want?" ([summary](12-what-does-chatgpt-want-an-interpretationist-guide.md)), are the closest companion. It applies interpretationism to LLM beliefs and desires and places them at the level of the instance, which is a direct comparison with Chalmers.
- **Exercise 3** asks which system or process to test: a single forward pass, the model across instances, the hardware, a conversation, or a recurring persona. Chalmers's four candidates map onto this list. The exercise is the best check on whether you understood the excerpt.
- **Exercise 1** asks you to pick one approach to consciousness evaluation. The "approaches based on self-report" and "sentience, emotion and wellbeing" approaches both depend on the individuation question this paper raises.

### Across the course

- **Unit 1 (moral standing)**: the course's framing of moral patienthood assumes a patient. Chalmers's thread view changes what that patient is.
- **Unit 2 (theories of consciousness)**: Chalmers deliberately avoids committing to consciousness here. The unit's theories supply the other side of that choice.
- **Units 4 and 5 (perceptions and interactions)**: the Aura-type user reports are exactly the perceptions and interactions those units discuss.
- **Units 6 and 7 (uncertainty and governance)**: individuation affects whom a governance rule protects. If the welfare-relevant entity is a session, deprecation and deletion policy changes.
- **Tension**: the course's emphasis on empirical testing (this unit's other readings) can sit uneasily with Chalmers's claim that the test target is underdetermined. The exercises ask you to hold both.

## Critical perspective

*My own analysis, labelled as such. It rests on secondary accounts of the paper, so treat it as provisional.*

- **The stipulation point is the main pressure point.** If quasi-beliefs are defined by behavioural interpretability and attributed cheaply, the framework may describe LLM behaviour well but say little about whether anything is at stake for the system. Critics argue that the difference between a simple system and an LLM is one of kind, not of degree, and that a substantive account is still needed.
- **"The model" as unit is contested in practice.** Routing between model variants and token-level mixture-of-experts routing make the model less of a fixed object than the paper's rejection suggests. A critic argues for threads at the level of individual tokens. That would shift the question but not remove it.
- **Persona steering undermines beliefs being stable.** Named personas (for example, a persona that persists across conversations) can be steered to invert the apparent beliefs. If so, quasi-beliefs look context-dependent, which may fit a thread view but also weakens the case for a stable interlocutor.
- **Anthropomorphism risk.** Language of "belief" and "desire" imports folk-psychological concepts into systems whose internal mechanisms may be very different. One critic proposes "prediction" and "steering" vocabulary (from the simulators literature) instead. Chalmers's reply, as reported, is that the quasi-terms are deliberately cheap, which concedes the point about explanatory power.
- **Relation to the course's other perspectives.** McClelland (in the Agnosticism reading) would say we cannot know whether these systems are conscious, so quasi-states do not settle the question. Papineau (in "Consciousness is not the Key to Moral Standing") would say moral standing need not track consciousness at all. If the secondary accounts are right that Chalmers ties moral relevance to quasi-agency (unverified against the paper), that claim sits closer to Papineau's line than to McClelland's. Goldstein and Lederman would ask whether the thread view is the right location for belief, or whether belief sits at the instance level.
- **Date.** The paper is from 2026, and the critical literature I found is almost all from the last few months, so the debate is young. Models, deployment and memory features have changed quickly since the paper's examples were written, so the specific architectural claims (for example, about threads and conversation memory) should be checked against current deployment practice.
- **Source-quality issue.** The blog critique is dated 26 December 2025, earlier than the paper's circulation, so it may respond to an earlier draft or talk. I would not treat it as a response to the final text.

## Discussion questions

1. Chalmers rejects the model (the weights) as the interlocutor because weights compute nothing alone. Does that argument also rule out the thread, since a thread is just a chain of computations over shared text? What extra condition does the thread have?
2. What exactly does calling a quasi-belief "cheap" concede? Can a notion of belief that applies to a robot vacuum with a map do the work the course needs for moral standing?
3. If the interlocutor is a conversation thread, what happens to welfare judgments when a user starts a new conversation with the same named persona? Is the entity the same or different?
4. Compare Chalmers with Goldstein and Lederman (the interpretationist guide). Both use interpretation. Where do they place the belief: the thread, or the instance? What would change in the course's evaluation methods if you chose one over the other?
5. Map Chalmers's four candidate interlocutors onto Exercise 3's five candidates. Which candidates from the exercise are missing from Chalmers's list, and why would that matter for choosing a test target?
6. The "Aura" reports are user testimony rather than controlled experiments. What would a test designed around Chalmers's individuation framework need to hold fixed, and how would you know you had isolated the interlocutor?
7. Chalmers's framework is philosophical, while the Eleos review and the system card are empirical. Which of the section's methods would change if you accepted the thread view as the default target?

---

**Issues for a human to check:**
- The paper's full text was not accessible (HTTP 403 from PhilPapers and PhilArchive). The "Detailed summary" is a reconstruction from secondary sources and must be checked against the PDF before it is cited.
- The local source file `sources/what-we-talk-to-when-we-talk-to-language-models__0e8210c5.md` is a Cloudflare interstitial ("Just a moment..."), not the paper. It was not overwritten because I had no full text to replace it with.
- Two secondary sources disagree on whether the paper contains an "Aura" example. The course guide says it does.
- The blog critique is dated 2025-12-26, before the paper's circulation. Its critique may target an earlier version.
- The Beckmann and Butlin "Aura" result that a secondary post mentions is a different subject (a neural cluster in model representations), not the paper's Aura example. I did not use it as evidence.
