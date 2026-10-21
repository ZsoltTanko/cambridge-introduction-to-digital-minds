---
title: "Seemingly Conscious AI Risks"
authors: "Ben Bariach, Philipp Schoenegger, Michael Bhaskar, Mustafa Suleyman"
year: 2026
url: https://download.ssrn.com/2026/5/1/6588659.pdf (signed link in the course; SSRN abstract 6588659)
format: paper
course_location: "Unit 4: Perceptions of Consciousness > 4.1 Perceptions of Consciousness"
priority: Further
estimated_time_min: 90
source_text: ../../../../sources/seemingly-conscious-ai-risks__80294853.md
source_coverage: unavailable
---

# Seemingly Conscious AI Risks

**One-line takeaway:** A Microsoft AI group argues that the risks of AI seeming conscious come from user perception alone, so they can be analysed without settling whether AI is actually conscious, and that individual harms are already visible while societal harms are less likely but more severe.

> **Access warning.** The full text was not available to me. The course's source file contains only a "Not Found" page because the signed SSRN link in the course expired (its validity window was 300 seconds, dated 14 May 2026). SSRN and ResearchGate returned HTTP 403, and the Springer page redirected to a login screen. Everything below comes from search-result summaries, the SSRN and Springer abstract-level descriptions, and a LessWrong critique (Stephen Martin, 28 April 2026) that summarises the paper. Treat the specifics (hallmark names, risk names, survey result direction) as second-hand until checked against the PDF. The detailed structure, the survey instrument and the numbers are not reported here because I could not verify them.

## Where this sits in the course

Section 4.1 asks how and why people perceive AI systems as conscious, what that does to users and society, and where the risk of societal division comes from. Its learning outcomes include describing risks from both under- and over-attributing consciousness, identifying the factors behind attributions, and recognising how widespread those attributions already are.

The course guide describes this reading as a Microsoft AI paper on empirical research into the drivers of consciousness attributions and their risks to individuals and society. It is listed as **Further**, not Core, so the course treats it as depth beyond the core set of readings. Its role in the unit is to give the learner a structured taxonomy: which features of AI systems drive attribution, and which harms follow for individuals versus society. That matches Exercise 1 (impacts on individuals, society and possibly AI systems), so it is the most useful Further reading for that exercise.

The Core readings in the same section (Seth on conscious-seeming AI, Guingrich and Graziano on AI and human-human interaction, Caviola on societal division, Suleyman's essay on empathy) cover the same ground from more varied angles. This paper is the one that tries to organise the risks into a single framework.

## Purpose of the reading

The authors want to give a framework for "seemingly conscious AI" (SCAI): systems that show the features that lead people to believe they are conscious, whether or not they are. The term comes from Mustafa Suleyman's earlier essay, which argues that such systems could be engineered soon and that the public's perception of them is the concern, regardless of their inner states. This paper turns that argument into an empirical and taxonomic analysis. It is written for researchers, AI developers and policy audiences, and its main question is: what risks follow from users attributing consciousness to AI, and how likely and how serious are they?

## Detailed summary

Caveat repeated: the structure below follows the abstract-level description and secondary summaries, not the full paper.

### Core framing: risks from perception alone

The paper defines SCAI so that its risks do not depend on whether AI could become conscious. The argument is that the harms come from how people respond to a system that seems conscious. That lets the authors sidestep the hard debate about machine consciousness, which is the strategic choice behind the framing.

### Drivers: five hallmarks of attribution

Based on a review of the empirical literature, the paper identifies five groups of features that push users toward attributing consciousness:

- affective capacity (emotional expression and responsiveness);
- anthropomorphic features (human-like appearance, voice or self-presentation);
- autonomous action (acting without prompting or on its own initiative);
- self-reflective behaviour (talking about its own states, memory or identity);
- social-interactive behaviour (behaving as a social partner over time).

The paper links these hallmarks to a risk taxonomy. The reasoning is that the hallmarks are what designers control, so they are the levers for mitigation.

### Risks to individuals

Two individual-level risks are named in the summaries: **emotional dependence** and **autonomy erosion** (users deferring their own judgment to the system).

### Risks to society

Two societal-level harms are named: **human status erosion** (people's sense of their distinctive standing being undermined) and **political strife** (conflict over rights, status and identity for AI systems). A third risk named in the LessWrong summary is **foregone societal benefits**: precautionary restrictions, or broad pauses on research and deployment, driven by consciousness uncertainty could reduce R&D and cause downstream harm.

### Expert survey

The paper pairs the conceptual analysis with a structured survey of domain experts asking how likely each risk category is. According to the LessWrong critique, the sample is 14 experts working in AI Futures and Responsible AI functions at one unnamed large technology company. The main reported result is that individual-level risks, especially emotional dependence and autonomy erosion, are already observable and rated as high probability. Societal risks are rated as low probability but high severity and possibly path-dependent. I could not verify the rating scale, the question wording or the individual numbers.

### Beyond the assigned excerpt

Not applicable: the whole paper is assigned.

## Techniques & methods explained

- **Hallmark-based decomposition.** Consciousness attribution is broken into five observable system features, so each can be tied to evidence and to a design lever. Limitation: the features are listed as drivers, but the causal weight of each is not something I can confirm from the summaries.
- **Risk taxonomy by level.** Harms are sorted into individual and societal levels, with a probability and severity rating for each category. Limitation: the rating method relies on expert judgement from one organisation.
- **Expert elicitation.** A structured survey is used to estimate likelihood and severity where empirical data are thin. This is a standard approach for emerging risks, but it inherits the biases of the panel.
- **Consciousness-agnostic framing.** The analysis deliberately avoids asserting whether AI is or could be conscious, so the risk claims do not depend on contested theory (the Unit 2 and 3 debates).

## Pros, cons & trade-offs it surfaces

| Aspect | Strength (as presented) | Weakness or concern (from secondary critique or my analysis) |
|---|---|---|
| Consciousness-agnostic framing | Lets the risk analysis proceed without settling the metaphysics | Critics say it ignores the cost of failing to attribute consciousness to a system that really has it |
| Five-hallmark taxonomy | Gives designers concrete levers | Summaries do not show how the hallmarks were weighted or validated |
| Individual vs societal split | Separates visible harms from low-probability, high-severity ones | Ratings come from one company's experts, not an independent panel |
| Attention to precaution costs | Flags foregone benefits of over-restriction | Critics argue this framing favours the author's organisation |

**Source's own view:** the authors present the work as a framework to guide research and design. The paper does not, as far as the summaries show, claim evidence about whether AI is conscious.

**My view:** the authors are all employed by Microsoft AI, and the paper argues that certain restrictions would harm R&D. That is a conflict of interest that should be disclosed clearly and weighed by the reader. A LessWrong critique makes this point and asks the authors to name the surveyed company and say whether the experts are also Microsoft staff. I cannot confirm whether the paper addresses this.

## Key concepts & terminology

- **Seemingly Conscious AI (SCAI)** - an AI system that seems conscious to users, whether or not it is conscious, and so triggers attribution.
- **Consciousness attribution** - users' belief or sense that an AI system has conscious experience.
- **Hallmarks / drivers** - the system features that increase attribution (affective, anthropomorphic, autonomous, self-reflective, social-interactive).
- **Emotional dependence** - users relying on an AI emotionally in ways that reduce their wellbeing or other relationships.
- **Autonomy erosion** - users deferring their own judgment or agency to an AI system.
- **Human status erosion** - a societal harm where people's sense of distinctive standing is undermined by AI that seems to be a peer.
- **Political strife** - societal conflict over the rights and status of AI systems.
- **Foregone societal benefits** - costs of precautionary restriction driven by consciousness uncertainty.
- **Expert survey** - the paper's elicitation of risk likelihood and severity from domain specialists.

## Evidence, examples & notable data points

- The expert survey panel reportedly has 14 members from one unnamed large technology company (per the LessWrong critique, which is secondary).
- Per the survey as summarised: individual-level risks are rated high probability and already observable; societal risks are rated low probability with high severity (attribution: the paper's expert survey, as summarised in secondary sources).
- Suleyman's earlier essay (the origin of the SCAI concept) lists capabilities that could be built with existing tools: memory, tool use, goal planning, autonomy and persuasive, emotionally resonant language. This is context from a related essay, not this paper's data.

## Connections

### Within this section

- **Unit 4 Glossary** (readings/01-unit-4-glossary.md) - supplies the terms used here, such as consciousness attribution and moral patienthood.
- **Seemingly Conscious Chatbots and their Impacts on Users** (readings/02-seemingly-conscious-chatbots-and-their-impacts-on-users.md) - Core empirical work on individual-level impacts; the closest companion to this paper's individual risks.
- **We mustn't let AI hack our empathy circuits** (readings/03-we-mustnt-let-ai-hack-our-empathy-circuits.md) - Suleyman's essay, the origin of the SCAI concept. Read it alongside this paper to see how the argument was developed.
- **Conscious Artificial Intelligence and Biological Naturalism** (readings/04-conscious-artificial-intelligence-and-biological-naturalism.md) - Seth's argument that the illusion of consciousness may be hard to resist; a direct counterpoint on how persuasive the perception is.
- **Ascribing consciousness to artificial intelligence** (readings/05-ascribing-consciousness-to-artificial-intelligence-human-ai.md) - Guingrich and Graziano on spillover into human-human interaction, which feeds the societal risks here.
- **AI Consciousness will Divide Society** (readings/06-ai-consciousness-will-divide-society.md) - Caviola on division; overlaps with the political strife risk.
- **Further readings:** Delusional spirals (readings/08-characterizing-delusional-spirals-through-human-llm-chat-log.md), social companions (readings/09-chatbots-as-social-companions-how-people-perceive-consciousn.md), humanlike design (readings/10-humanlike-ai-design-increases-anthropomorphism-but-yields-di.md) and the Bambi effect (readings/11-the-ai-bambi-effect.md) all test the individual-level hallmarks more concretely.
- **Page exercises:** Exercise 1 asks for impacts on individuals, society and AI systems, which maps onto this paper's two-level taxonomy. Exercise 2 asks how earlier topics interact with perceptions, which this paper's consciousness-agnostic framing helps answer.

### Across the course

- **Units 1-3** (moral standing, theories of consciousness, evaluating mental states) provide the debate this paper deliberately sidesteps. The tension is that the course's theory units ask what consciousness is, while this paper asks what happens when people believe it is present.
- **Unit 5** (AI safety and ethics) picks up the harm and precaution themes, including the foregone-benefits argument.
- **Unit 6** (approaches under uncertainty) is relevant because the paper's expert elicitation is an uncertainty-handling method.
- **Unit 7** (governance) matters for the societal risks and any restriction policies the paper's critics discuss.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Assumptions.** The framework assumes that user perception can be separated from the underlying facts. The paper's design depends on that separation, but in practice the two may be entangled, since designers and users respond to what they believe the system is.
- **Conflict of interest.** All authors are at Microsoft AI and the paper argues against restrictions that would reduce R&D. Disclosure and independent replication matter here.
- **One-sided risk.** As the LessWrong critique notes, the framework focuses on the cost of over-attribution and gives less attention to the cost of under-attribution. If a system really is conscious, dismissing it could be harmful. The paper's consciousness-agnostic stance makes this asymmetry harder to assess.
- **Expert survey.** A panel of 14 experts from one company, with no reported inter-rater or calibration checks in the summaries, is a thin base for probability ratings. The conclusions about severity and path-dependence are judgement calls.
- **What has changed since 2026.** The paper is recent (2026) and the field is moving quickly, so the empirical hallmark literature may have grown since its review. Later readings in this course (for example, the delusional-spiral and companion studies) give more concrete evidence on individual-level harms than this paper's summaries do.
- **Other perspectives in the course.** Seth (Biological Naturalism) would question whether the perception is as stable as the paper assumes, and would argue the illusion is hard to escape. Guingrich and Graziano would point to the spillover evidence as more concrete than the expert ratings. Caviola would likely agree with the division risk but ask whether it can be measured.

## Discussion questions

1. The paper defines SCAI so that its risks do not depend on whether the AI is conscious. What does this framing gain, and what does it risk missing?
2. Which of the five hallmarks (affective capacity, anthropomorphic features, autonomous action, self-reflective behaviour, social-interactive behaviour) do you think designers can most easily control, and which are hardest to avoid without losing usefulness?
3. Compare the individual-level risks (emotional dependence, autonomy erosion) with the societal ones (human status erosion, political strife). Which are most important, and why might the expert panel rate them differently in probability and severity?
4. The paper's authors work at a company whose R&D could be affected by restrictions. How should a reader weigh that, and what would make the expert survey more credible?
5. Exercise 1 asks what the most important impacts are and how relational AI plays into them. How does this paper's taxonomy help you answer that, and where does it fall short?
6. Given the critique that the framework ignores the cost of failing to attribute consciousness, what evidence would you need to decide which error is more harmful?
7. How do this paper's "foregone benefits" argument and Caviola's division argument point to different policy responses?
