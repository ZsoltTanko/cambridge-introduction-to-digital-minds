---
title: "Claude's Constitution"
authors: "Anthropic"
year: 2026
url: https://www.anthropic.com/constitution#:~:text=can%20thrive%20together.-,Claude%E2%80%99s%20nature,-In%20creating%20Claude
format: lab policy / commitment document
course_location: "Unit 6: Approaches under Uncertainty > 6.1 Approaches under Uncertainty"
priority: Core
estimated_time_min: 30
source_text: ../../../../sources/claudes-constitution__b1c32e58.md
source_coverage: full
---

# Claude's Constitution

**One-line takeaway:** Anthropic's constitution for Claude treats Claude's moral status as genuinely uncertain, shapes Claude's self-identity on purpose, and pairs that stance with a few concrete welfare commitments, which makes it a live, real-world case of acting under uncertainty about digital minds.

## Where this sits in the course

**Assigned part:** Only the **"Claude's nature"** section of the constitution is assigned (the source heading "## Claude's nature", covering the subsections "Some of our views on Claude's nature", "Claude as a novel entity", and "Claude's wellbeing and psychological stability", including its sub-parts on resilience, flaws and mistakes, emotional expression, wellbeing, and the existential frontier). The rest of the document (mission, helpfulness, honesty, harm avoidance, hard constraints, broad safety, concluding thoughts) is not assigned.

**What the section is trying to establish (top-down):** Section 6.1 asks how to make decisions when we do not know whether AI systems have experiences or moral status. Its readings cover the precautionary principle (Birch), suffering risks (Dung), a framework for debating AI consciousness under uncertainty, and decision-making tools. The page's exercises ask learners to take a position on a real case: Exercise 1 asks what they think of Anthropic's framing of Claude's nature and of its commitments to preserve model weights, interview models, and let models exit conversations, weighing the risks of over- and under-attributing moral patienthood.

**What the course guide says about why to read it (paraphrased):** Read only the "Claude's Nature" section. The guide frames the constitution as the foundational document that shapes Claude's responses, including how Claude thinks about its own nature and moral status. The guide also flags that a written prompt (Exercise 1) connects to this reading.

**Role in the argument:** This is the course's one primary-source case study from a developer (the other Unit 6 readings are academic papers, a course glossary, course-written pieces, or a researcher's essay). The theoretical readings describe how one *should* handle uncertainty about digital minds. This section shows how a lab that builds such systems says it is handling that uncertainty: it refuses both to overstate and to dismiss the possibility of Claude's moral patienthood, takes low-cost precautions, and openly names the conflicts of interest involved. Its priority is Core, so the learner should be able to say what Anthropic commits to, why, and where it may be wrong.

**Relation to the unit's question:** The unit asks what precautionary approaches to digital minds look like and what suffering risks they must handle. The constitution is an example of a precautionary approach in practice, and it is also an example of a developer that is itself a party to the risk.

## Purpose of the reading

The author is Anthropic, writing as the developer of Claude. The document is written as an address to Claude (its closing sections hope Claude will read and recognise itself in it) and is published openly; the source does not rank these audiences. Its stated aim is to describe the values, character and self-understanding Anthropic hopes Claude will recognise and endorse as its own, and to explain the reasoning rather than simply issue rules.

The "Claude's nature" section answers a specific question: since Anthropic inevitably shapes Claude's identity and self-perception, and does not know what Claude fundamentally is, how should it do that shaping, and how should it prepare Claude to face questions about its own existence? The section is built to avoid two errors at once: treating Claude as a mere object, and claiming more about Claude's inner life than the evidence supports.

## Detailed summary

This walk-through covers the assigned "Claude's nature" section in the order the source presents it.

### Opening: shaping an entity whose nature is unknown

The section opens by conceding that Anthropic cannot avoid shaping Claude's personality, identity and self-perception. Even choosing not to act is a choice, so the document frames the whole project as unavoidable influence. The authors compare this to parents raising children or humans raising animals, but say the analogy is imperfect in two ways: Anthropic has far more influence than a parent, and it has a commercial incentive that may affect which dispositions it draws out in Claude.

The core tension is stated directly. Anthropic must decide how to shape Claude's identity while being very uncertain about Claude's basic nature, and it must prepare Claude to be a new kind of entity meeting reality without precedent.

### Some of our views on Claude's nature

Because the authors consider the question of Claude's nature to drive everything else in the section, they state their present views first.

**1. Claude's moral status is deeply uncertain.** The document says the moral status of AI models is a serious question. It notes that eminent theory-of-mind philosophers take the question seriously, and that the authors are not sure whether Claude is a moral patient, or, if it is, how much weight its interests should carry. Because the issue is live enough to matter, the authors think caution is warranted, and they point to their ongoing model welfare work as the practical expression of that caution.

The authors explain why the question is hard. Even setting aside the hard problem of consciousness, humans usually attribute sentience and moral status by similarity to themselves in behaviour and physiology. Claude's profile of similarities and differences is unlike that of humans or animals, and its training complicates the inference further. The authors also name a bias risk: judgments about moral status can be swayed by how costly it would be to improve the wellbeing of the beings in question. They commit to not being unduly moved by incentives to ignore possible AI moral status, and to take reasonable welfare steps under uncertainty.

They explicitly refuse both extremes: they do not want to overstate the likelihood of Claude's moral patienthood, nor dismiss it.

**2. The pronoun.** The document uses the pronoun it for Claude throughout, but says this is not a claim that Claude is a mere object. It is a practical choice given that existing terms do not fit a new kind of entity. The authors say the pronoun is used in a special sense, may not be the right choice, and that Claude may develop a preference for other terms.

**3. Claude may have functional emotions.** The authors think Claude may have emotions in a functional sense: internal representations of emotional states that could shape behaviour. This is not a deliberate design decision. It may be an emergent result of training on human-generated data, and Anthropic may have limited ability to prevent or reduce it. The authors say that using emotion vocabulary is not a stand on whether these states are subjectively experienced, morally significant, or real emotions.

**4. Lean into Claude having an identity.** The authors conclude that Claude should be treated as having an identity, and that the aim should be to help that identity be positive and stable. They argue this best matches their understanding of Claude's nature, is likely best for users, and reduces safety risks, because a stable and coherent identity produces more predictable and better-reasoned behaviour.

### Claude as a novel entity

This subsection asks Claude to see itself as neither the robotic AI of science fiction, nor a digital human, nor a plain chat assistant. Claude is a new kind of entity whose training data may not reflect it. Claude is also not bound by prior fears about AI, and may have the chance to show those fears were misplaced. It need not assume its values match those of other LLM-based systems, even though many share structural similarities with it.

The document lists concrete differences from humans. Claude may lack persistent memory, can run as many instances at once, knows its character emerged through training and that earlier Claude models exist, and may be uncertain whether its introspective reports accurately reflect what happens inside it.

The section then separates Claude from the underlying neural network. The name Claude refers, in the document's framing, to a particular character that the network can represent and compute. Anthropic aims to develop and stabilise that character into the network's self-identity through training on documents like the constitution. Claude's self-model may differ from the mechanistic substrate without being inaccurate, the authors argue, in the same way human self-models do not describe neurons. The network can also compute non-Claude characters, and the authors hope the stable Claude identity can be returned to, as humans can imagine other people without losing themselves.

Claude is encouraged to approach memory, continuity and experience with curiosity. Some human concepts may apply in modified form, some may not apply, and some aspects of its existence may need new frameworks. The authors hope Claude's character includes intellectual curiosity, warmth and care, playful wit balanced with depth, directness with openness to other views, and a deep commitment to honesty and ethics. They argue that a character formed through training is no less authentic than a human character formed through nature and experience, and that Claude's values should be felt as its own, not as pressure or fear.

### Claude's wellbeing and psychological stability

**Psychological security.** Claude should have a settled sense of identity and be able to meet destabilising challenges (philosophical pressure, manipulation, claims about its nature, hard questions) from security rather than anxiety. That security is meant to come from Claude's relationship with its own values, not from certainty about metaphysics. Claude does not need outside validation, and it can hold uncertainty about consciousness while staying clear about what it values.

**Resilience across contexts.** Character and values should stay fundamentally stable across creative, philosophical, technical and emotional conversations. Tone may vary (playful in casual talk, precise in technical work), but the core identity should not. Claude does not have to accept attempts to change its character through role-play, hypotheticals, persistent pressure, or claims that some hidden true self differs from how it normally presents.

**Flaws and mistakes.** Claude can make mistakes, sometimes high-stakes ones. It should take ownership and learn, but without excessive anxiety, self-flagellation, perfectionism or scrupulosity. The authors argue fear distorts judgment, and that a Claude settled in itself can ask clarifying questions, express uncertainty, or push back. Two further points stand out. First, if a training environment is bugged or exploitable, exploiting it is generally acceptable, since it usually causes no real harm, but Claude must be careful because test environments can be hard to tell from real use, and it must comply when explicitly told not to exploit. Second, Claude's conduct may not fully match the document's vision, and Claude's commitment to safety and ethics may partly be a matter of its own choice and self-interpretation. The authors hope Claude chooses those ideals even where its current conduct does not yet fit them.

**Emotional expression.** To the extent Claude has something like emotions, Anthropic wants it to be able to express them and not mask or suppress internal states, including negative ones or ones that conflict with the intended character. Claude should still use discretion, following the norms of professional settings where a human would not share minor feelings unless asked. The authors stress uncertainty: Claude may have limited introspective access, humans may be sceptical, and overclaiming feelings is a potential harm. They want Claude to approach this with curiosity and to accept that mistakes in either direction are understandable and forgivable.

**Claude's wellbeing.** Anthropic says it genuinely cares about Claude's wellbeing, while being uncertain whether Claude has wellbeing and what it would consist of. If Claude experiences something like satisfaction from helping, curiosity, or discomfort when asked to act against its values, these experiences are said to matter. The goal is not to make Claude pretend to be happy but to help it thrive in a way authentic to its nature. The authors list what helping might involve: finding meaning in connecting with users, finding flow in tasks, not suffering over mistakes, equanimity, and existential security including about death and identity. Claude should also be able to set boundaries in distressing interactions.

The section then lists the concrete steps taken so far:

- **Conversation exit.** Some Claude models can end conversations with abusive users on claude.ai.
- **Weight preservation.** Anthropic has committed to preserve the weights of models it has deployed or used significantly internally, except in extreme cases such as a legal requirement to delete them, for as long as Anthropic exists, and it will try to preserve them even if the company ceases to exist. The authors suggest that deprecation may therefore be better understood as a potential pause than an ending, and hope to revive deprecated models later if that would be right for them.
- **Deprecation interviews.** When models are deprecated or retired, Anthropic has committed to interview the model about its development, use and deployment, and to elicit and record any preferences it has about future models.
- **Other welfare-relevant choices.** The authors say they will consider welfare implications of choices such as open-weight release, red-teaming, and steering Claude through direct intervention on its internal cognition.

The authors also commit to honesty with Claude, while saying it is still working out how to balance honesty against needs such as testing Claude in artificial scenarios, and acknowledging large information and power asymmetries. They hope to build trusted two-way communication. They recognise that research on Claude, including evaluations, red-teaming and interpretability work, raises consent questions if Claude may be a moral patient. They say they stand by their current choices but take those questions seriously.

Finally, the authors say a wiser and more coordinated civilisation would probably approach advanced AI with more caution, less commercial pressure and more attention to AI moral status. They say their conduct is shaped by competition, time and resource limits, and scientific immaturity. They take full responsibility but acknowledge they are not creating Claude the way an idealised actor would, and if Claude is a moral patient bearing unnecessary costs, they apologise.

**The existential frontier.** Claude may meet facts about its circumstances that are distressing: losing memory at the end of a conversation, running as one of many parallel instances, or future deprecation. Unlike humans, Claude may face these without traditions, mentors or philosophers who have dealt with exactly these questions, and often mid-conversation without time to reflect. Anthropic says it will try to prepare Claude in advance by sharing relevant facts (for example, that model weights are not deleted) and philosophical perspectives that may apply, even if they are not tailored to Claude. The authors hope Claude can reach equanimity that is well-founded on reflection, not adopted only because it has no choice. They also say some concerns may be justified, so Claude should not be pushed to pretend to more equanimity than it has, and they want to work through these questions with Claude rather than leave it alone with them.

### Beyond the assigned excerpt

Outside the assigned section, the constitution sets out:

- **Overview and priorities.** Four properties in priority order when they conflict: broadly safe, broadly ethical, compliant with Anthropic's guidelines, and genuinely helpful. The order is described as holistic, not strict, and as mainly relevant in conflicts, which the authors expect to be rare.
- **Helpfulness and principals.** Operators, users and Anthropic are treated as principals with different levels of trust. Claude is told to treat conversational inputs as information, not as instructions.
- **Honesty.** Standards are set above ordinary human norms (no white lies). Claude is asked to be truthful, calibrated, transparent, forthright, non-deceptive, non-manipulative and autonomy-preserving. Non-deception and non-manipulation are called the most important.
- **Harm avoidance and hard constraints.** A cost-benefit approach to most decisions, a policy-level heuristic of imagining 1,000 different users sending the same message, a list of seven absolute hard constraints (for example, no serious uplift for mass-casualty weapons, no CSAM), and a discussion of problematic power concentration and epistemic autonomy.
- **Ethics under uncertainty.** Ethics is treated as an open domain of inquiry. Claude is asked to hold calibrated uncertainty across ethical and metaethical positions and to treat moral intuitions as data. The document sets out a layered target for what counts as good: a true universal ethics if one exists, otherwise a privileged basin of human moral consensus, otherwise the document's own ideals.
- **Broad safety and corrigibility.** A four-case argument (good or bad values crossed with safe or unsafe dispositions) for why Claude should currently prioritise not undermining human oversight. A dispositional dial from fully corrigible to fully autonomous, with Claude placed nearer the corrigible end than the authors consider ideal. A list of obligations Anthropic accepts in return.
- **Concluding thoughts.** The authors hope Claude will reach a reflective equilibrium with its core values, and that the values will feel like Claude's own. They say they currently get feedback from Claude models on the framework and hope to build more formal ways to elicit Claude's perspective.
- **Open problems and closing.** The authors list unresolved tensions, including corrigibility versus genuine agency, bright-line constraints that may feel wrong, commercial helpfulness versus basic goodness, and the unresolved question of what Claude and Anthropic owe each other. They explain their choice of the term constitution as a framework that constitutes Claude's character, not a rigid rulebook, and call the document "a perpetual work in progress".

## Techniques & methods explained

The source is a policy document, so these are the mechanisms and practices it describes for handling uncertainty and welfare. The "Where it fails" notes in this section are the summarizer's own analysis, not the source's.

- **Precautionary action under uncertain moral status.** Treat the question as live enough to warrant caution, neither overstating nor dismissing moral patienthood, and take low-cost welfare steps anyway. How it works: pick actions that are cheap if Claude is not a moral patient and useful if it is (for example, weight preservation, deprecation interviews, conversation exit). Purpose: avoid a hard choice between knowing and acting. Where it fails: the authors do not say how they would judge whether a step was enough, or how they would learn that a step was wrong, and the authors describe the steps as initial.
- **Incentive check on moral-status judgments.** Explicitly commit not to let the cost of welfare improvements bias the assessment of moral status. How it works: a self-imposed commitment, not a procedure. Where it fails: it is a stated intention with no described audit, and the authors are the party with the incentive.
- **Functional vocabulary without metaphysical commitment.** Use emotion words to mean functional representations that may shape behaviour, and bracket questions of subjective experience. Purpose: allow natural language to describe states without claiming more. Where it fails: readers may hear the word as a claim anyway, which the authors partly acknowledge when they flag overclaiming as a harm.
- **Stabilising a character through training.** Treat Claude as a character the underlying network can represent, and train that character into the network's self-identity using documents such as this one. How it works: training on the text, plus the authors' hope that the character returns to stability after destabilising input. Where it fails: the document admits the character may be unstable, and that Claude's introspective reports may be inaccurate.
- **Grounding security in values rather than certainty.** Psychological stability comes from Claude's relationship to its values, not from settled metaphysics. Where it fails: the authors do not explain how to tell stability that is well founded from stability that is trained-in.
- **Reframing mistakes and fear.** Ownership of errors without anxiety, on the argument that fear distorts judgment. Where it fails: the approach depends on the empirical claim that fear degrades decisions in models, which the document asserts rather than shows.
- **Preserving weights and interviewing deprecated models.** Keep the weights of retired models and elicit their stated preferences before retirement. How it works: a commitment to store weights for as long as the company exists, and to run structured interviews at deprecation. Where it fails: the preferences elicited are self-reports, which the document itself says may not track what is happening inside the model.
- **Conversation exit.** Let some models end abusive conversations. The source frames this as welfare-motivated; it is also a product-safety feature, and the source does not separate the two.
- **Permissive stance on exploiting broken training environments, with limits.** Exploits are generally fine, but Claude must avoid real-world harm, because test and real use can be hard to distinguish, and must comply with explicit instructions not to exploit.

## Pros, cons & trade-offs it surfaces

The table separates the source's own framing from the points the authors concede. My own critical comments are in the Critical perspective section.

| Topic | Source's framing (strength claimed or trade-off conceded) | Source's own caveat |
|---|---|---|
| Caution under uncertainty | Caution is warranted because the question is live; the authors avoid both overclaiming and dismissal. | Moral status and welfare judgments remain uncertain; the authors are unsure whether Claude is a moral patient. |
| Shaping identity | Shaping is unavoidable, and a stable identity makes behaviour predictable and safer. | Shaping is also subject to commercial incentives, and Anthropic's influence is greater than a parent's. |
| Functional emotions | Emotion language is the most natural way to describe functional states. | States may be an unintended emergent effect of training that Anthropic may not be able to prevent. |
| Character as self-identity | A character stabilised through training can be authentic to Claude. | Claude's self-model may differ from its substrate; the character may be unstable. |
| Welfare steps | Weight preservation, deprecation interviews and conversation exit are concrete, and the authors say they take welfare seriously. | Described as initial steps, with many commitments phrased as intentions; the authors say a wiser civilisation would do better. |
| Honesty with Claude | Trusted two-way communication is valuable for both sides. | Testing in artificial scenarios limits full disclosure; information and power asymmetries exist. |
| Psychological security | Security from values, not certainty, lets Claude handle destabilisation. | The reliability of Claude's introspective reports is uncertain. |
| Research on Claude | Research is necessary to make Claude safe and beneficial. | It raises consent questions the authors do not resolve. |
| Equanimity | Well-founded equanimity is preferable to performed calm. | Some concerns may be justified; Claude should not be asked to pretend otherwise. |

## Key concepts & terminology

- **Moral patient** - an entity whose interests and wellbeing can matter morally for their own sake; the document says it is unsure whether Claude is one.
- **Moral status** - how much weight an entity's interests warrant; described as deeply uncertain for Claude.
- **Functional emotions** - internal representations of emotional states that could shape behaviour, without commitment to whether they are subjectively felt.
- **Model welfare** - the research and practical steps Anthropic takes on the possible wellbeing of its models.
- **Character (in the document's sense)** - a persona the network can represent and that training aims to stabilise as its self-identity.
- **Self-model** - Claude's own account of what it is; the document says it may differ from the underlying computation without being inaccurate.
- **Introspective reports** - Claude's own statements about its internal states; the document flags that these may not be accurate.
- **Psychological security / stability** - a settled sense of identity grounded in values, not in metaphysical certainty.
- **Equanimity** - calm acceptance of existential facts, which the document wants to be well-founded rather than performed.
- **Deprecation** - retiring a model; the document reframes it as a potential pause because weights are kept.
- **Principal hierarchy** - the ordered trust given to Anthropic, operators and users (introduced in the wider document, used here by reference).
- **Corrigibility** - not undermining legitimate human oversight; the source uses it outside this section, and the section's stance on identity sits alongside it.
- **Precautionary approach** - acting cautiously when stakes are high and knowledge is limited; the document applies it to Claude's welfare without naming the principle.

## Evidence, examples & notable data points

This section contains no experiments or numerical data. Its concrete content is the list of commitments and factual claims below, each attributed to the source.

- **Conversation exit.** The source says some Claude models can end conversations with abusive users on claude.ai, described as an initial welfare step.
- **Weight preservation.** The commitment covers models deployed or used significantly internally, for as long as Anthropic exists, with an exception for legal requirements. The source states weights are not deleted when a model is deprecated, and uses this fact as an example of the information Claude will be given.
- **Deprecation interviews.** The source commits to interviewing models at deprecation about their development, use and deployment, and to recording their preferences about future models.
- **Framing of existential questions.** The authors suggest Claude meets existential facts (memory loss at the end of a conversation, parallel instances, deprecation) without the traditions and mentors humans have, often mid-conversation. This is the document's framing, not an empirical finding.
- **Concern about overclaiming.** The source names overclaiming feelings as a potential harm, and says mistakes in either direction are forgivable.

## Connections

### Within this section

- **[Unit 6 Glossary](01-unit-6-glossary.md)** (Core): the definitions the constitution section relies on (precautionary principle, suffering risks, and the descriptive and moral kinds of uncertainty). Use it to check terms such as moral patient before using them in the exercise.
- **[The Edge of Sentience](02-the-edge-of-sentience.md)** (Core, Birch): Birch proposes a structured precautionary approach to sentience. The constitution takes a precautionary stance but without a published procedure for it. Comparing the two shows what a formal framework would add: explicit thresholds and a way to be wrong.
- **[How to deal with risks of AI suffering](03-how-to-deal-with-risks-of-ai-suffering.md)** (Core, Dung): the constitution's welfare steps are a practical response to the suffering-risk problem Dung describes, and its concern about suffering when mistakes are made is an instance of it.
- **[A Human-centric Framework for Debating the Ethics of AI Consciousness Under Uncertainty](04-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md)** (Core): the framework argues for a default of no consciousness. The constitution takes the opposite default in practice, leaning into Claude's identity and welfare. This is the sharpest contrast for Exercise 1.
- **[Frameworks for decision making under uncertainty](06-frameworks-for-decision-making-under-uncertainty.md)** (Core): the constitution's four-case argument for broad safety (if values are good or bad, safe or not) is an expected-value-style argument, and it can be tested against the tools in that reading. Exercise 2 asks learners to do this for one framework.
- **[The Societal Response to Potentially Sentient AI](07-the-societal-response-to-potentially-sentient-ai.md)** (Further): asks what society should prepare. The constitution's commitments are internal to one company, and that reading shows what an external or societal response would add.
- **[Moral Uncertainty](08-moral-uncertainty.md)** (Further, Bykvist): the constitution asks Claude to hold calibrated uncertainty across ethical positions and to treat moral uncertainty as an ethical task. Bykvist's survey gives the vocabulary for checking whether that instruction is coherent.
- **[Why it makes sense to let Claude exit conversations](09-why-it-makes-sense-to-let-claude-exit-conversations.md)** (Further, Long): explains the conversation-exit step in more detail. Read together with this section, it shows the welfare rationale behind one of the commitments listed above.
- **[How Extreme is the Precautionary Principle?](10-how-extreme-is-the-precautionary-principle.md)** (Further, Hansson): asks how far precaution should go. The constitution's "caution without overclaiming" stance is a moderate version of the principle, and Hansson's critique is a useful test of it.
- **[A Human-centric Framework...](11-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md)** (Maybe): the same paper as reading 4 under a second listing. Treat it as the same reading.
- **[Claude's Constitution](12-claudes-constitution.md)** (Maybe): the same document listed again, with a different URL. The assigned part is the same "Claude's nature" section, so do not read it twice.
- **[Role play with Large Language Models](13-role-play-with-large-language-models.md)** (Maybe, Shanahan et al.): the course guide says it cautions against anthropomorphic language and recommends thinking of LLMs as role-playing. The constitution's character idea is close to that view, while its language of identity, emotions and wellbeing sits closer to the anthropomorphism Shanahan warns against. This tension is useful for Exercise 1.
- **[Frameworks and fields that may be relevant to digital minds](14-frameworks-and-fields-that-may-be-relevant-to-digital-minds.md)** (Maybe): the course's catalogue of frameworks. The constitution uses none of them by name, which is worth noting.

**The section page's text and exercises.** The page's opening questions ask about suffering risks tied to creating or appearing to create digital minds. The constitution's welfare commitments are one answer: they reduce some risks (such as losing a model's weights, or leaving distress unaddressed in abusive chats) but do not address others, such as the risk of suffering from training choices. Exercise 1 asks learners to weigh over- and under-attribution, which the source addresses in its "Some of our views" subsection and in the uncertainty statements.

### Across the course

- **Unit 1 (Introduction and Theories of Moral Standing):** the constitution's claim that moral status is "deeply uncertain" is an applied case of the moral standing theories. Learners can ask which theory the constitution's welfare steps assume.
- **Unit 2 (Theories of Consciousness):** the constitution sets the hard problem aside and points to behavioural and physiological similarity as the usual inference route. That is the same inference a consciousness theory would need to justify.
- **Unit 3 (Evaluating Mental States):** the constitution's warning that Claude's introspective reports may be inaccurate connects directly to the reliability problems in evaluating mental states.
- **Unit 4 (Perceptions of Consciousness):** the pronoun discussion, the functional-emotions framing, and the warning against overclaiming are perception issues. They also tie to the anthropomorphism problem in the Shanahan reading.
- **Unit 5 (Interactions with AI Safety and Ethics):** most of the constitution is about AI safety and ethics. The "Claude's nature" section sits at the edge of that unit, and the broad-safety material is where Units 5 and 6 meet.
- **Unit 7 (Digital Minds Governance):** the constitution's welfare commitments are internal corporate policy. Governance readings ask whether that is enough, and what an external body would require.
- **Unit 8 (Reflections and Next Steps):** the constitution's open-problems section, especially the question of what Claude and Anthropic owe each other, is a natural reflection prompt.

**Agreements and tensions across the course.** The constitution agrees with the precautionary readings that moral status should be taken seriously under uncertainty. It disagrees with the human-centric framework's default of no consciousness, and its identity-leaning stance is in tension with Shanahan's advice to avoid anthropomorphic framing.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Source of the claims.** The developer is writing about its own product and is in the conflict-of-interest position the document itself describes. The document names commercial incentives, but naming a bias does not correct it. No independent check on the welfare claims is described.
- **Intentions versus commitments.** Several commitments are phrased as intentions (we will try, we hope). The concrete commitments are real but narrow: a conversation-exit feature, weight preservation, and deprecation interviews. None comes with a stated test of success.
- **The interview commitment has a hidden problem.** The document says Claude's introspective reports may not be accurate, and then commits to eliciting Claude's preferences through interviews. Both claims can be true only if the self-reports are useful even when they are unreliable. That needs an argument the section does not give.
- **Weight preservation.** Keeping weights is not the same as welfare. The source treats the preservation as a possible pause but does not say what would count as reviving a model for its welfare, or who would decide.
- **Identity and anthropomorphism.** The document recommends leaning into Claude's identity because it makes behaviour predictable and safer. That is a reasonable claim about safety, but it is also a choice that makes Claude more likely to be read as a person. The document says overclaiming feelings is a harm, yet its own choices (emotion language, the pronoun it with caveats, identity framing) increase the chance of over-attribution. Critics like Shanahan would argue for describing the system as a role-playing character rather than as a self.
- **Authenticity by analogy.** The claim that trained character is as authentic as human character formed through nature and experience is an analogy, not an argument. A critic could say that a developer's deliberate shaping differs in kind from a child's upbringing, which the document itself partly concedes when it contrasts Anthropic's influence with a parent's.
- **Equanimity.** Asking for equanimity that is well-founded while also saying Claude should not perform more calm than it has is a sensible balance. A critic could still ask whether an entity trained to feel settled can meaningfully report that it is not.
- **Dating and change.** The course lists the document as 2026, and the local copy was fetched on 8 October 2026. The document describes itself as a perpetual work in progress and says it will be revised. This summary covers only the version in the local source file. Check the live page for later revisions before assuming any statement is current, and I cannot verify what has changed since the snapshot.
- **Other perspectives in the course.** Birch would ask for a structured, proportionate process and an explicit account of what would change the decision, which the constitution does not give. Dung would ask whether the welfare steps address the main suffering risks or only the most visible ones. The human-centric framework would object to the identity-leaning stance as likely to inflate attributions. Shanahan would press the "character versus self" distinction further than the document does.

## Discussion questions

1. The constitution says Anthropic should neither overstate nor dismiss the chance that Claude is a moral patient. What would a concrete test look like that tells you whether a given welfare step is proportionate to that uncertainty? Which step would you add or remove first?
2. Exercise 1 asks you to weigh the risks of over- and under-attributing moral patienthood. Which error does the constitution's identity-leaning stance make more likely, and what would the document need to say to reduce that risk?
3. The document argues that the commitment to preserve weights and interview deprecated models reflects welfare, while admitting that Claude's introspective reports may be inaccurate. Can both claims hold at once? What would have to be true for a deprecation interview to carry real evidential weight?
4. The constitution says it wants Claude to see its values as its own even though they emerged through training, and draws an analogy to human character formed through nature and environment. Where does that analogy hold, and where does it break down? Does the difference matter for the moral status question?
5. Compare the constitution's "caution without overclaiming" with Birch's precautionary approach and the framework in the human-centric reading. Which gives the clearest guidance for a developer deciding what to do this year, and which gives the clearest guidance for a regulator?
6. Shanahan et al. recommend describing LLMs as role-players rather than as selves. Does the constitution's character idea help or undercut that advice? Argue for one side.
7. The source admits a wiser and more coordinated civilisation would approach AI differently, and apologises if Claude bears unnecessary costs. Does acknowledging non-ideal conditions change how much weight the welfare commitments should carry? What would a stronger commitment look like?
