---
title: "Key concepts and current views on AI Welfare"
authors: "Eleos AI"
year: 2024
url: https://eleosai.org/papers/20250127_Key_Concepts_and_Current_Views_on_AI_Welfare.pdf
format: paper / report (PDF)
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Core
estimated_time_min: 30
source_text: ../../../../sources/key-concepts-and-current-views-on-ai-welfare__25bc5557.md
source_coverage: full
---

# Key concepts and current views on AI Welfare

**One-line takeaway:** There is no concrete, replicable, consensus evaluation yet for AI consciousness, sentience or agency, so the course asks you to learn the main candidate approaches (theory-derived indicators, behavioural tests and self-reports, valence indicators, agency tests) and their weaknesses before forming any view on whether an AI could be a moral patient.

## Where this sits in the course

**Unit 3** asks two framing questions: how we might test for AI consciousness and sentience, and how we might test for agency and mental states such as belief and desire. Its unit-level learning outcomes are to appraise methods for evaluating consciousness in AI, describe the other mental states we might test for, analyse current empirical research, and describe the difficulty of individuating or identifying digital minds. Section 3.1 is the unit's map of evaluation methods; the unit's later readings (the Chalmers paper on LLM interlocutors, the Claude system card, the introspection and emotion-concept studies) then look at specific cases.

**Course guide (paraphrased):** This is a practitioner's review of the main high-level approaches to testing for digital minds, with the advantages and disadvantages of each. The guide is explicit about the assignment: **read only the "Evaluations" section** (the course's guide says pages 5 to 12). In the printed pagination the section starts on page 6 ("2 Evaluations") and its last bullet runs onto page 13, just before "3 Questions about the likelihood of current and near-term AI moral patienthood". The assigned part is therefore Section 2, with its subsections on consciousness, sentience, agency, the relationship between these, and the further questions it closes with.

**Role in the argument:** This reading is the core technical map for the section. It covers the three features (consciousness, sentience and agency) through the indicator approach (for consciousness), the behavioural and self-report approach (for consciousness and for moral status), the valence approach (for sentience) and the agency approach (for robust agency), and it explains why each is hard to use. It also sets up Exercise 1, where you pick one category from the primer and assess how it could shift your probability of artificial moral patienthood. Priority is Core. Its relationship to the unit's question is direct: it is the source that most clearly explains what "testing for consciousness" would have to mean for AI systems.

## Purpose of the reading

The document is an opinionated statement of Eleos AI Research's views, written by Robert Long to share his thinking with collaborators (notably Kyle Fish) and with others interested in AI welfare. The authors say it is more opinionated than the joint paper "Taking AI Welfare Seriously", which reflects a consensus of many authors. It is written for collaborators and others interested in working on AI welfare.

The document asks three questions: when and to what degree AI systems might merit moral consideration; how we would know; and what we should do about it. The Evaluations section answers the second question. Its main argument is that evaluations for consciousness, sentience and agency are underdeveloped, that developing them is tractable, and that agency is the most neglected and possibly most tractable of the three. The section's stated aim is to review the motivations, limitations and development potential of existing approaches.

Note that the document is dated July 2024, with a lightly edited draft from January 2025. It says "current" should be read relative to July 2024.

## Detailed summary

*The assigned part is Section 2, "Evaluations" (printed pages 6-13). Background from Section 1 and the rest of the paper is covered at the end, under "Beyond the assigned excerpt".*

### Opening framing of the section

The section opens with the key takeaway: nothing close to concrete, replicable and consensus evaluations exists for consciousness, sentience or morally relevant agency. The authors argue that designing such evaluations is still tractable and that little work has gone into them. Agency is singled out as especially neglected, possibly more tractable because it is more amenable to behavioural tests, and "convergently useful" across many views of moral patienthood and welfare.

### Consciousness evaluations

The authors say consciousness has received the most effort. They describe two complementary strategies:

- **Indicator approach:** derive computational and architectural indicators from scientific theories of consciousness, in the spirit of Butlin, Long et al. (2023).
- **Behavioural approach:** devise observable behaviours or capabilities that count as evidence of consciousness, without focusing on internal architecture.

**The indicator approach.** It rests on neuroscientific theories that try to pin down which brain states and processes go with consciousness. The indicators in Butlin, Long et al. draw on global workspace theory, recurrent processing theory, higher-order theories, attention schema theory and predictive processing. Other theories the section mentions are midbrain theory, integrated information theory and unlimited associative learning. Many such theories state their claims in computational terms, which is what makes an AI-applicable indicator possible.

The approach depends on the working assumption of **computational functionalism**: that performing computations of the right kind is necessary and sufficient for consciousness, so the relevant functions could run in digital as well as biological systems. The authors flag this assumption as non-trivial and defeasible, and cite critiques by Godfrey-Smith and Cao.

The main result cited is that Butlin, Long et al. applied their indicators to the AI systems they surveyed. Their conclusion was that none appeared very likely to be conscious through this lens, but that no clear technical barrier seemed to stand in the way of building such systems.

**Issues with the indicator approach.** The authors identify three problems.

1. *Judgment calls in formulating indicators.* Deriving indicators requires deciding which computational features are essential according to a theory, and at what level of specificity. For global workspace theory, one can be more or less specific about which modules, or how many, a workspace must integrate.
2. *Judgment calls in applying indicators.* Deciding whether an AI system satisfies an indicator is also contestable. Example: one can argue that an LLM's output stream is a global workspace, because it is a bottlenecked space (one token at a time) that the model writes to and reads from. Butlin and Long argue it is not one in the relevant sense. The authors' point is that either position is a substantive call.
3. *No agreed methodology and limited expertise.* There is no well-justified, agreed method for these calls. Only a few experts worldwide can make and justify them for leading AI systems. Assessments are slow and labour-intensive, and they are made harder by incomplete understanding of model internals.

The authors add a broader caveat: consciousness science has not reached consensus on necessary or sufficient conditions for consciousness even in humans, so the indicator method inherits this uncertainty. Despite this, they are "enthusiastic" about continuing the work, since applying theories to AI can make thinking about machine consciousness more precise and less mystified. They insist limitations be communicated, so that criteria are not presented as either unwarrantedly demanding or unwarrantedly easy to satisfy.

**The behavioural approach.** It aims at observable behaviour that counts as evidence of consciousness. It draws on animal tests and tries to adapt them to AI. Many AI-oriented tests are linguistic. The section mentions:

- Schneider and Turner's **Artificial Consciousness Test**, which checks whether a system has a ready grasp of consciousness-related concepts in conversation, including "problem intuitions" such as the intuition that spectrum inversion is possible (after Chalmers).
- The **Turing test**, which Harnad has proposed as a behavioural test for consciousness.
- Capabilities such as self-awareness, introspection and situational awareness as possible starting points.
- **Self-reports** of conscious experience. Self-reports are central to our understanding of human consciousness. Eliciting and interpreting reliable self-reports from AI is not trivial (Perez and Long, 2023), though the authors note that techniques have been proposed to help.

The appeal is that behavioural evidence is easier to assess and quantify than internal computation. It also needs fewer computational-theory assumptions and can be more standardised, with less case-by-case expert judgment.

**Issues with the behavioural approach.** The main worry is that many AI systems are optimised to emulate human behaviour, so behaviours that validly indicate consciousness in animals or humans may not indicate it in AI (Andrews and Birch, 2023). Animal tests fit animals because of shared biology and evolutionary history. AI may need new tests, and then the question is which AI-specific behaviours would be reliable evidence and how much weight to put on behaviours that diverge from the human case. The authors acknowledge that models might "game" such tests or simulate consciousness without having it. They still think behavioural analysis has a role, particularly with other strategies. They put some weight on the view that sufficiently robust emulations of consciousness-associated behaviours should be taken seriously as evidence for moral patienthood, especially while major uncertainty remains about how functional features, behaviour and consciousness connect.

### Sentience evaluations

The authors use "sentience" for the capacity for positively and negatively valenced conscious experiences, such as pleasure, pain, joy and sadness. They note that the term is used inconsistently in the field. Valenced experience is widely taken to carry special moral significance. Examples given include pleasant sensations (a massage), positive emotions, unpleasant sensations (pain, nausea) and negative emotions. In animals, valenced states drive fitness-relevant behaviour. Negative experience tracks bodily damage, failed homeostasis and maladaptive social behaviour; positive experience tracks maintenance and reproduction.

Sentience is more than training with reward signals. Simple systems that are not plausibly conscious can learn from reward and act on it. Sentience also involves more than dispositions to approach or avoid. Conscious valenced experience may shape behaviour in specific ways, such as regulating what an entity attends to or promoting certain kinds of learning (Schukraft, 2020). This makes simple behavioural tests of sentience harder to design, though behavioural tests are still likely to matter.

Research on sentience in AI is described as even more nascent and qualitative than work on consciousness. The authors draw on:

- Campero (2024), who surveys **13 candidate computational indicators** for conscious valenced experience.
- Seymour (2019), whose theory says pain is an internal reinforcement signal used for learning at a system's higher "cognitive" levels, as opposed to lower-level learning and reflexes. This could generate indicators.
- Martínez and Klein (2016), who argue that all valenced states have an "imperative" informational profile, defined in information-theoretic terms.

These theories are not yet precise enough to guide evaluations of AI, and Campero notes the candidate indicators are inconsistent in vocabulary, abstraction and detail. The authors propose a concrete next step: a first-pass attempt to evaluate a leading model against some of these indicators, to test feasibility and surface refinements. Keeling et al. (2024) is cited as an early example. Interpretability work on how AI systems represent value, make decisions and handle trade-offs could also help. The longer-term aim is to know not just whether a system is sentient but which of its states are sentient, and how those states shape its welfare capacities and rights.

### Agency evaluations

**Overview of robust agency.** Some views hold that moral patienthood does not require consciousness or sentience. The most common alternative grounds are goals, preferences and desires (Kagan, 2019; Kammerer, 2022). Some notions of desire imply conscious experience, but desire can also be defined in purely functional terms. The authors call the more sophisticated forms of goal-directedness that might matter morally **"robust agency"**. The concept is not yet well worked out. The authors note a tension:

- **Liberal notions of agency** centre on a goal and the capacity to pursue it. On this view moral patienthood could extend to many existing algorithms, robots, and even thermostats. The authors find this intuitively unsatisfying and practically fraught.
- **Stringent notions** would add requirements for the agency that matters for practically relevant moral status. No well-developed theory of these requirements exists yet. In Long et al. (2024) the authors survey three further levels: intentional agency, reflective agency and rational agency.

They also argue that behavioural evidence of desires and preferences may be more informative than behavioural evidence of consciousness. The reason is that the gap between acting like an agent and being one is probably smaller than the gap between acting conscious and being conscious. The caveat is that LLM behaviour can still mislead, since models can look agentic in some contexts and fail in others in surprising ways.

**Agency and alignment.** The authors argue that alignment research deals with similar questions about goals and preferences. Alignment researchers, however, focus on dangerous forms of agency, not on liberal senses that are uninformative for safety. Robust agency probably overlaps with dangerous agency. Both concerns share one key point: it is important not to create systems with goals that conflict with human goals, especially if they are capable planners. Such goals would be bad for humans. They would also be bad for the AI, because a system whose goals we must shut down, modify or constrain in order to defend ourselves is a potential moral-patienthood problem as well as an alignment problem. Misalignment also raises the chance of AI takeover, which could itself be very bad for AI welfare in the long run (Finlinson, 2025).

The authors conclude that evaluating models for agentic behaviour is useful for both alignment and moral patienthood. They list strategic deception in training or deployment (Carlsmith, 2023), long-term planning, autonomous replication and adaptation (Kinniment et al.), and shutdown-resistant behaviour (Gunter et al., 2024). Training schemes and architectures that keep systems "myopic", tool-like and non-agentic would have the same convergent value.

### Relationship between evaluations for consciousness, sentience and agency

- **Sentience and consciousness** are intertwined. In the authors' terms, sentience is a specific subset of conscious experience.
- **Agency and consciousness** are linked because, on some theories, agency is necessary for consciousness. The kind of agency needed for consciousness may differ from the kind relevant to moral patienthood, though they likely share features.
- **Agency and sentience** are the most closely related pair. Both involve evaluative representations, meaning ways an entity represents things as valuable or disvaluable. Research on the nature of evaluative representations in AI will matter whichever category it is filed under.
- **Agency as a welfare proxy.** Agency is an important proxy for welfare on many views, even though it is neither sufficient for moral patienthood nor necessary for consciousness or sentience. If a system were sentient, its suffering or displeasure would likely track its desires, preferences and goals, much as humans feel bad when their desires are frustrated. A system with strong aversions or that avoids certain outcomes is at risk of suffering, conditional on being a moral patient. So evaluating goals and preferences matters under many assumptions.

### Further questions about evaluations

The section closes with open questions, including: what the highest-value and most tractable near-term evaluations for moral patienthood are; how feasible it is to train systems to report their internal states accurately and reliably; whether alignment evaluations "cover" the space of moral-patienthood evaluations; whether lack of scientific consensus constrains indicator construction, or whether theory-agnostic indicators could shift evidence under many assumptions; and which interpretability work matters most.

### Beyond the assigned excerpt

*Not assigned, but in the same document.*

- **Section 1 (pp. 1-5), "Moral patienthood, welfare, and rights":** Defines moral patienthood (an entity whose treatment matters morally, in its own right and for its own sake) and separates descriptive questions (is it conscious, sentient, agentic?) from normative ones (which features suffice for moral standing?). It argues that agency-centred views deserve serious attention given moral uncertainty. It separates welfare from rights, and notes that AI rights might differ from human rights for instrumental reasons. The authors' example is the risk of granting reproductive and voting rights to copyable AIs, since "every copy gets a vote" would let elections be won by copying. They also argue that moral patienthood alone says little about how much weight to give an AI's welfare, so one must also estimate the probability of suffering and how many AI patients might be affected.
- **Section 3 (pp. 13-16), "Questions about the likelihood of current and near-term AI moral patienthood":** Notes that few experts have published credences about AI moral patienthood. The only detailed report the authors cite is David Chalmers (2023), who says a 50% credence that LLM+ systems with a set of properties (senses, embodiment, world and self-models, recurrent processing, global workspace, unified goals) arrive within a decade is not unreasonable, and a 50% credence that such systems would be conscious. Together these give 25% or more. Chalmers recommends a "theory-balanced" approach to credences. The authors suggest modelling credences in necessary and sufficient features separately from credences that a system has them, and list features of a future system that would make moral patienthood quite likely. These include embodiment, behavioural indicators of agency and sentience, consistent self-reports, high self- and situational awareness and understanding of the meta-problem of consciousness (which they note many humans would not meet).
- **Section 4 (pp. 15-16), "Future research directions":** Prioritises (1) evaluating systems for features relevant to moral patienthood, (2) more precise models of likelihood, kinds and degrees, (3) a broader range of systems beyond frontier LLMs, and (4) the moral foundations of this work. It also proposes studying introspection and interviewing LLMs about their preferences, while warning, citing the Blake Lemoine episode, that naive readings of LLM output are misleading.
- **Conclusion:** Under-attributing moral patienthood could contribute to suffering on an unprecedented scale. Over-attributing it would have a large opportunity cost and could damage alignment and governance work. The authors say the field has done little work on this relative to its importance.

## Techniques & methods explained

- **Indicator derivation from scientific theories.** Start from a theory (e.g. global workspace, recurrent processing, higher-order, attention schema, predictive processing), identify the computational features it says are essential, decide how specific to be, and then check whether an AI system has each feature. Limit: each step needs contestable judgment, and the method rests on computational functionalism.
- **Behavioural tests for consciousness.** Use observable behaviour as evidence: animal-style tests, linguistic tests such as the Artificial Consciousness Test, and the Turing test. Limit: AI systems are trained to imitate humans, so the evidence may be invalid, and tests built for animals may not transfer.
- **Self-report elicitation.** Ask the system about its experiences, preferences and internal states, then check for consistency across prompts and against behaviour. Limit: reliable elicitation is hard, and the system may be mimicking human reports.
- **Valence indicators.** Look for signals of pain or pleasure as reinforcement or "imperative" informational states. Limit: candidate indicators are not yet precise, and they are inconsistent in vocabulary and abstraction.
- **Behavioural tests for desires and preferences (robust agency).** Test whether a system pursues persistent goals, acts to bring about preferred states, and shows preferences about its own inputs and body. Limit: LLMs act inconsistently across contexts; liberal definitions of agency become too broad.
- **Alignment-style agency evaluations.** Test for strategic deception, long-term planning, autonomous replication and shutdown resistance. Limit: these are proxies, and the paper does not claim they cover moral patienthood fully.
- **Interpretability.** Study how systems represent value, make decisions and trade off options. Limit: the paper says it could be informative but does not develop it into a method.
- **Combining indicators.** Formal strategies for aggregating indicators into an overall assessment. The paper calls for these but does not provide one.

## Pros, cons & trade-offs it surfaces

| Approach | Strengths (as the paper presents them) | Weaknesses and trade-offs (as the paper presents them) |
|---|---|---|
| Theory-derived indicators | Connects to existing scientific theories; computational; applies to biology and AI alike; can make machine consciousness more precise | Depends on contested theories and on computational functionalism; many judgment calls; few qualified assessors; hard to apply without model internals |
| Behavioural tests and capabilities | Observable and quantifiable; fewer theory assumptions; more standardised | AI optimised to mimic humans; animal tests may not transfer; gaming risk; which AI behaviours count is unclear |
| Self-reports | Central to human understanding of experience; can be probed directly | Hard to elicit reliably; may reflect mimicry; needs checks against behaviour and capabilities |
| Sentience/valence indicators | Targets the morally most significant kind of experience | Research is nascent; candidate indicators are inconsistent; valence may affect behaviour in ways simple tests miss |
| Robust agency tests | The gap between acting like an agent and being one is probably smaller than for consciousness; desires are "more informative" than consciousness tests; useful for alignment as well | Liberal agency definitions cover thermostats; stringent ones lack a worked-out theory; LLM behaviour is inconsistent |

Trade-offs the paper stresses:

- **Under- versus over-attribution.** Both errors are costly. Under-attribution risks moral catastrophe. Over-attribution risks opportunity cost and harm to alignment and governance.
- **Communicating limits.** Indicator criteria should be presented neither as too demanding nor as too easy to satisfy.
- **Convergent value.** Agency evaluations serve alignment and moral-patienthood aims together, which the authors see as an advantage.

## Key concepts & terminology

- **Moral patienthood** - an entity whose treatment matters morally, in its own right and for its own sake.
- **Consciousness** - (in the paper) phenomenal consciousness, i.e. having subjective experience.
- **Sentience** - the capacity for positively and negatively valenced conscious experience (pleasure and pain). The paper notes the term is also used as a synonym for consciousness.
- **Agency** - having goals, preferences or desires; the paper distinguishes liberal from stringent notions.
- **Robust agency** - the more sophisticated forms of goals, preferences or desires that might be morally relevant.
- **Indicator approach** - deriving computational or architectural indicators of consciousness from scientific theories.
- **Behavioural approach** - identifying observable behaviours or capabilities as evidence of consciousness or other features.
- **Computational functionalism** - the thesis that performing computations of the right kind is necessary and sufficient for consciousness. The paper treats it as a defeasible working assumption.
- **Global workspace theory** - a theory on which consciousness is the global broadcast of information to otherwise independent modules.
- **Self-report** - a system's statement about its own experiences, preferences or internal states.
- **Valence / imperative signal** - a state with positive or negative value; Martínez and Klein's proposal is that valenced states have an "imperative" informational profile.
- **Evaluative representation** - a representation of something as valuable or disvaluable; the paper says sentience and agency both involve these.
- **Alignment** - the research aim of making AI goals and preferences match human ones; the paper notes its overlap with moral-patienthood concerns.

## Evidence, examples & notable data points

- **Butlin, Long et al. (2023)** applied indicators from several theories to AI systems. Their overall conclusion: none of the surveyed systems appeared very likely to be conscious through this lens, but no clear technical barriers stood in the way of building such systems (as the paper summarises that work).
- **Campero (2024)** surveyed **13 candidate computational indicators** for conscious valenced experience.
- **Chalmers (2023)**, as cited: a **50%** credence that LLM+ systems with the listed properties arrive within a decade, and a **50%** credence that such systems would be conscious. Together these give **25% or more**. Chalmers says his own credences are higher.
- **Schneider and Turner's Artificial Consciousness Test** checks for "problem intuitions" such as the intuition that spectrum inversion is possible.
- **Andrews and Birch (2023)** are cited for the concern that AI systems optimised to emulate humans can undermine behavioural evidence.
- **Blake Lemoine incident** is cited as an example of how naive readings of LLM outputs can mislead about moral patienthood.
- **Shulman and Bostrom (2021)** are cited for the voting example: if AI systems can copy themselves at will and every copy votes, elections can be won by copying.
- **The paper's own tally** is that very few experts have published credences about AI moral patienthood. Sebo and Long (2023) argue that conservative assumptions can still give a non-negligible credence in AI consciousness by 2030, but use a self-described simplistic model.

## Connections

### Within this section

- **[01-unit-3-glossary.md](01-unit-3-glossary.md)** (Core): the course glossary defines terms that this paper uses, such as consciousness, sentience and agency. Read it first to avoid confusing sentience with consciousness, which this paper uses in a specific sense.
- **[03-claude-mythos-preview-system-card.md](03-claude-mythos-preview-system-card.md)** (Core): the system card's welfare assessment is a worked example of the behavioural and self-report approaches discussed here. Use it to check the paper's warnings about gaming and mimicry.
- **[04-what-we-talk-to-when-we-talk-to-language-models.md](04-what-we-talk-to-when-we-talk-to-language-models.md)** (Core): Chalmers' treatment of beliefs and desires in LLM interlocutors is the detailed version of the agency and robust-agency material here. It also covers the individuation question in Exercise 3.
- **[05-evaluating-consciousness-sentience-and-other-mental-states-p.md](05-evaluating-consciousness-sentience-and-other-mental-states-p.md)** (Further): the course's primer is the source of the exercise categories. Exercise 1 asks you to pick one of its categories, and this reading covers the indicator, behavioural, self-report, valence and agency approaches that the primer organises.
- **[07-signs-of-introspection-in-large-language-models.md](07-signs-of-introspection-in-large-language-models.md)** (Further): the introspection work is an example of the self-report and introspection capabilities the paper calls for. The paper asks whether self-reports track internal states, and this study tests that.
- **[13-emotion-concepts-and-their-function-in-a-large-language-mode.md](13-emotion-concepts-and-their-function-in-a-large-language-mode.md)** (Further): emotion representations relate to the sentience and valence section, and to the paper's call for interpretability work on how systems represent value.
- **[08-agnosticism-about-artificial-consciousness.md](08-agnosticism-about-artificial-consciousness.md)** (Further) and **[06-ai-welfare-is-bullshit.md](06-ai-welfare-is-bullshit.md)** (Further): both are critical of confident welfare or consciousness metrics, and push against the paper's willingness to take behavioural evidence seriously.
- **[12-what-does-chatgpt-want-an-interpretationist-guide.md](12-what-does-chatgpt-want-an-interpretationist-guide.md)** (Further): an interpretationist account of beliefs and desires in models. It is an alternative to the agency tests described here.
- **[10-consciousness-is-not-the-key-to-moral-standing.md](10-consciousness-is-not-the-key-to-moral-standing.md)** (Further): argues against the consciousness requirement that this paper treats as one view among several.

The section page's exercises draw on this reading. Exercise 1 asks you to choose one evaluation category from the primer (theory-based, self-report, choice-based, sentience/emotion/wellbeing, self-representation, indicator-combination, other tests such as the Artificial Consciousness Test and Turing test, or validation of tests) and to say how it would shift your probability of moral patienthood. This paper gives the vocabulary and the advantages and disadvantages for most of these options: theory-based indicators, self-reports, valence and sentience indicators, self-awareness and introspection, and the Artificial Consciousness and Turing tests. It does not cover choice-based evaluations or validation of tests, and on combining indicators it only calls for formal methods. Exercise 3 asks what system or process we should test (a single forward pass, the model across instances, the hardware, a conversation, or a persona). The paper does not address individuation directly, but its point that behavioural evidence must be checked against internal states bears on it.

### Across the course

- **Unit 1 (Introduction and Theories of Moral Standing):** the paper's section 1 covers the concept of moral patienthood and the consciousness-versus-agency debate, which the Unit 1 material introduces. This reading takes the question into testing.
- **Unit 2 (Theories of Consciousness):** the indicator approach depends directly on global workspace, recurrent processing and the other theories Unit 2 covers. Judgments about whether an LLM output stream is a workspace are a live application of those theories.
- **Unit 3 (this section):** the course's glossary, primer and the Chalmers and system-card readings extend the paper's methods to specific cases and to the individuation problem.
- **Unit 4 (Perceptions of Consciousness):** the paper's concern that people will over-attribute or under-attribute moral patienthood connects to how the public perceives AI consciousness.
- **Unit 5 (Interactions with AI Safety and Ethics):** the paper's alignment section is a bridge. The agency evaluations it describes (deception, shutdown resistance, autonomous replication) are safety evaluations too.
- **Unit 6 (Approaches under Uncertainty):** the credence material and the "theory-balanced" approach connect directly to decision-making under uncertainty.
- **Unit 7 (Digital Minds Governance):** the under- and over-attribution trade-off, and the paper's call for precise credence models, bear on governance choices.

**Agreements and tensions.** The paper agrees with the course's general theme that evaluations are not yet adequate, and that moral patienthood is uncertain. It is in tension with the more sceptical readings (McClelland's agnosticism, Papineau's argument that consciousness is not the key to moral standing, and the critical welfare paper). Those authors would challenge the paper's use of computational functionalism and its willingness to treat behaviour as evidence.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Age of the "current" views.** The paper says "current" means July 2024 and it was lightly updated in January 2025. It is now October 2026. Some of its claims (for example, that very few experts have published credences, or that frontier LLMs are the main focus) may be out of date. Several later works in this course, including the introspection and emotion-concept studies and the system card, show that the empirical work has moved on. Treat the paper as a map of the problem space and check the specific claims against newer work.
- **The indicator approach's hidden assumption.** The approach needs computational functionalism. The paper calls this assumption "non-trivial and defeasible" but does not say what would count as evidence against it. The indicator approach cannot be fully tested until that question is settled, so its conclusions are conditional.
- **The behavioural approach's tension.** The paper takes behaviour seriously, while also acknowledging that models are trained to imitate humans. The paper's answer is to combine behaviour with other evidence and weight it cautiously. This is reasonable, but it does not say how to decide when behaviour is genuine evidence and when it is mimicry. The gap is the core unresolved problem.
- **Agency as a route around consciousness.** The agency section's argument that behavioural tests for desires are "more informative" than tests for consciousness is plausible but contestable. Someone who thinks desires need conscious grounding would reject it. The paper accepts that the stringent notion of agency is underdeveloped.
- **Over-attribution risk.** The conclusion is careful about both errors. However, the paper gives more concrete detail about the cost of under-attribution than about how to measure over-attribution. Critics would say the balance of concern is not well justified.
- **Opinionated by design.** The authors flag that this is their own view, not a consensus. Read the claims about what is "tractable" and what is "neglected" as the authors' judgments, not as settled facts.

**How other perspectives push back.** The critical welfare paper in this course argues that welfare metrics have no regard for truth and could be dangerous. McClelland argues we cannot know whether systems are conscious. Papineau argues consciousness is indeterminate and not the key to moral standing. Goldstein and Lederman's interpretationist view would locate AI beliefs and desires in the instance, which changes what "testing an agent" means. Each would challenge a different part of this section.

## Discussion questions

1. The paper says the indicator approach involves "judgment calls" at two points. Which judgment, in formulating indicators or applying them to an LLM, do you think is more consequential, and why?
2. Why might behavioural evidence for desires be more informative than behavioural evidence for consciousness? Does the argument rely on a claim about the causes of behaviour that you find plausible for AI systems?
3. Choose one approach from the primer's list (for example, self-reports or sentience indicators). What would the paper say are its core parts, its main advantage and its main weakness? How would a positive result shift your probability of moral patienthood, and would a negative result do the same?
4. The paper says that alignment and moral-patienthood evaluations share key concerns. Can you think of a case where a safety evaluation would be a poor measure of moral status, or the reverse?
5. Consider the warning that models may "game" behavioural tests. How, in practice, could a researcher tell an emulation from genuine experience? Is combining methods enough, or does it just move the problem?
6. The paper says "agency" is the most neglected of the three features. Do you agree? What makes the liberal-versus-stringent tension hard to resolve, and what would a well-specified stringent notion need?
7. The paper is dated 2024 and calls itself opinionated. Which of its claims would you most want to check against recent work before relying on them in the Exercise 1 write-up?
