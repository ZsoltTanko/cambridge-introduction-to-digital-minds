---
title: "Humanlike AI Design Increases Anthropomorphism but Yields Divergent Outcomes on Engagement and Trust Globally"
authors: "Robin Schimmelpfennig et al"
year: 2026
url: https://arxiv.org/pdf/2512.17898
format: paper
course_location: "Unit 4: Perceptions of Consciousness > 4.1 Perceptions of Consciousness"
priority: Further
estimated_time_min: 72
source_text: ../../../../sources/humanlike-ai-design-increases-anthropomorphism-but__01ce358f.md
source_coverage: full
---

# Humanlike AI Design Increases Anthropomorphism but Yields Divergent Outcomes on Engagement and Trust Globally

**One-line takeaway:** Making a chatbot more humanlike reliably makes people rate it as more humanlike, but effects on trust and engagement depend on culture and user group, and users judge humanlikeness from conversational behaviour rather than from consciousness-related attributes.

## Where this sits in the course

Section 4.1 asks how and why people perceive AI systems as conscious, and what follows for users and society. Its learning outcomes cover why public perceptions matter, the risks of under- and over-attributing consciousness, how attribution affects users, what drives it, how widespread it is, and the risk of societal division. The two exercises ask learners to spend 15 minutes on the impacts of consciousness misattribution on individuals, society and AI systems (including relational AI), and 5 minutes on how earlier unit material on digital minds, theories of consciousness and evaluating mental states interacts with public perceptions.

The course guide describes this paper as a "review of design features related to anthropomorphism and differing global impacts." That wording is loose. The paper is an original pair of experiments (N = 3,500 across two studies), not a literature review, so treat the guide as a rough pointer.

The whole paper is assigned; there is no excerpt. Its priority is **Further**, with an estimated 72 minutes. Most of the Core readings in this section argue that humanlike or seemingly conscious AI carries psychological and social risks. This paper tests the step those arguments take for granted: that humanlike design causes more trust and engagement, and that this holds for everyone. It finds that humanlike design reliably raises anthropomorphism, but that the downstream effects are uneven across countries and subgroups. It also shifts attention from beliefs about machine consciousness to the interactional cues users actually notice. Against the unit's guiding question ("how and why do humans perceive AI systems to be conscious"), the paper's answer is that people mostly do not reason about consciousness at all when they judge humanlikeness; they respond to how the chatbot converses, responds and builds rapport.

## Purpose of the reading

The authors are Robin Schimmelpfennig (Max Planck Institute for Human Development, work done while at Google Research), Mark Diaz, Vinodkumar Prabhakaran and Aida Davani (Google Research). The source is an arXiv preprint (v2, February 2026); this text does not establish whether it has been peer reviewed.

The paper addresses a gap the authors identify in the literature. Anthropomorphism research and AI ethics often assume that humanlike design raises engagement and trust and so creates psychological risk. Most of the evidence behind that assumption is from non-representative samples, correlational designs, hypothetical vignettes, or isolated AI outputs rather than live conversation. The sample is also heavily WEIRD (Western, educated, industrialised, rich, democratic).

The authors ask three questions:
1. In open-ended, ecologically valid conversation across many cultures, what do users actually use to judge whether an AI is humanlike?
2. Does experimentally making a chatbot more humanlike causally increase anthropomorphism, engagement and trust?
3. Are those downstream effects uniform across countries?

The intended audience is AI safety, ethics and policy people who assume a single "universal AI experience" and a uniform psychological risk profile for humanlike AI.

## Detailed summary

### Introduction and motivation

The authors open by framing a tension. Commercial actors have strong incentives to make systems mimic human traits, since this competes for attention and market share. Safety researchers and ethicists warn that humanlike systems can foster misplaced trust, emotional attachment, persuadability and over-reliance on AI for high-stakes tasks. More than a billion people use conversational AI products, and users increasingly turn to it for companionship and emotional support. The authors describe the situation as a large real-time social experiment whose psychological consequences are poorly measured. They argue that a culturally inclusive evidence base is a practical requirement for AI safety, not just an ethical ideal, because the models in use have largely been trained on WEIRD-reflective data and because products are now adopted outside the US and Europe.

### Study 1: how people anthropomorphize across ten countries

Study 1 (N = 1,100) recruited participants from an online panel in ten countries: the US (N = 200) and nine others with N = 100 each (Germany, South Korea, Japan, India, Nigeria, Indonesia, Egypt, Mexico, Brazil). Surveys were run in each participant's native language. The authors describe the samples as nationally representative, but the recruitment was via an internationally operating panel with about 100 respondents per country, so "representative" should be read as panel-based rather than probability-based. Data were collected from 12 August to 2 October 2024, with a median response time of 20 minutes.

Each participant had an open-ended conversation of at least four minutes (up to one extra minute) with GPT-4o (August 2024 version, temperature 1, no token limit) about non-sensitive everyday topics such as food preferences. Participants were told they were talking to a chatbot. The system prompt forbade the chatbot from claiming to be human or to have human characteristics. Afterwards they rated the chatbot on ten 5-point attributes adapted from earlier anthropomorphism and social perception work: humanlike, competent, intelligent, warm, conscious, moral, soul, personality, feelings and empathy. They also answered two open-ended questions: what made them feel they were talking to a human, and what made them feel they were not.

Quantitative results:
- About 68% rated the chatbot as somewhat or completely humanlike, and about 25% as somewhat or completely machinelike.
- About 90% rated it intelligent, 78% empathetic, and 75% conscious.
- No attribute was rated non-anthropomorphic by more than 30% of users.
- Two country clusters emerged. Indonesia, Mexico, India, Nigeria, Egypt and Brazil (N = 600) had mean humanlike ratings of 3.98 (SD 1.19). The US, Germany, Japan and South Korea (N = 500) had 3.29 (SD 1.25).
- Cultural distance from the US correlated with anthropomorphism at r = 0.52, p = 0.127. The authors call this exploratory and not significant with ten countries.
- No gender difference was found, nor a difference by prior AI usage intensity. Age had an inverted-U relation with humanlike ratings.

The authors' reading is that anthropomorphism is widespread but varies by culture, so perceptions are not the same across user groups.

### Study 1 qualitative analysis: user-driven versus theory-driven aspects

This is the paper's central analytic move. The authors built a codebook of 38 labels for what makes an AI seem humanlike. Ten of the labels are theory-driven (morality, intelligence, consciousness, soul and similar constructs from anthropomorphism scales). The rest are user-driven, derived inductively from responses. The process followed iterative thematic analysis (Braun and Clarke) by three researchers, with a calibration round on 20 participants and a validation set of 100. The codebook was then applied at scale by an LLM autorater (Gemini 2.5 Pro, instruction-tuned with few-shot examples) on all 1,100 responses, in their original languages, and the authors report a human gold-standard set of 100 responses.

Frequency of mention:
- Conversation flow: 32.1%
- Understanding the user's perspective: 24.4%
- Response speed: 22.5%
- Authenticity: 18.4%
- Intelligence: 8.8%
- Empathy: 5.5%
- Soul, morality, consciousness and warmth: fewer than 0.5% each

The authors conclude that users attend to how the chatbot writes, presents itself and builds a relationship, rather than to its possession of properties that mark human uniqueness. They note that this contrasts sharply with the Likert results in which most people rated the bot as "conscious."

### Study 2: experimentally manipulating humanlikeness

Study 2 (N = 2,400) used 400 participants in each of six countries: the US, Germany, Japan, India, Egypt and Brazil. Each participant was explicitly told they were interacting with an LLM. The design is a 2 x 2 between-subjects factorial, with two treatment factors built from the Study 1 findings and the prior literature:

- **Design Characteristics (DC)**: response speed, informal tone with colloquialisms and emojis, variable response length, a "human" emoji, and an assigned first name (Alex, localised for non-English samples). The low-DC version uses a robot emoji, consistent low-latency responses and neutral delivery.
- **Conversational Sociability (CS)**: high CS prompts empathy, warmth, social follow-up questions and matching the user's style. Low CS is factual and task-oriented.

Each condition was implemented by changing the system prompt, using the same underlying model (GPT-4o). The authors call this a conservative test: the model already has strong social capabilities, and the goal was to mimic the degrees of humanlikeness that actors with limited control over model training could produce.

Anthropomorphism results:
- The most humanlike condition (high DC and high CS) compared with the least humanlike control rated the chatbot as more humanlike (b = 0.386, 95% CI [0.251, 0.522], t(2396) = 5.59, p < 0.001).
- A significant effect in the same direction appeared on 7 of 10 items.
- No significant effect on intelligence, competence or consciousness. The authors read this as evidence that judgements of capability were unaffected.
- Each factor alone also raised humanlikeness for several items (high DC only: b = 0.204; high CS only: b = 0.181), but the combined condition gave the largest effects.
- By country, the combined condition had positive effects on the humanlike item in Brazil, Germany and the US. It was not significant in Egypt, India or Japan. Single-factor effects were mixed, sometimes near zero or negative. The authors explicitly present country analyses as exploratory.

### Study 2: trust and engagement

The paper's second main finding is that humanlike design does not uniformly increase trust or engagement.

Engagement: humanlike design significantly increased behavioural engagement against the control (t(1191) = 4.38, p < 0.001, d = 0.25). The authors attribute this partly to reciprocal verbosity: users and the chatbot both wrote more, which created a self-reinforcing loop. (See the inconsistency note under Critical perspective about which engagement measure this refers to.)

Trust: the trust game was a modified one-shot investment game (Berg, Dickhaut and McCabe). Each participant got 100 points, could send any amount x to the AI, which was tripled to 3x, and the AI returned some amount y between 0 and 3x. The amount sent was the behavioural trust measure. Pooled across conditions, the most humanlike and least humanlike conditions did not differ (t(1194) = 0.038, p = 0.969, d = 0.002). Equivalence testing (TOST) at a smallest effect size of interest of d = 0.20 found the differences statistically equivalent to zero, and Bayes factors (BF01 from 11.9 to 34.6) gave strong evidence for the null. Self-reported trust items also did not rise in aggregate.

Engagement was measured with self-reported items (enjoyment, willingness to use again, whether the AI would make a good friend) and behavioural chat-log metrics (message counts and message length, with length normalised by min-max scaling within each country).

### Heterogeneous effects by subgroup

The paper's overall message is that effects are not uniform. In Brazil, humanlike cues increased willingness to use the AI again, behavioural engagement, seeing the AI as a friend, and self-reported trust. In Japan, the high-DC/low-CS condition reduced willingness to use the AI again, perceptions of it as a friend, and self-reported trust. The authors suggest an uncanny-valley-type explanation: familiarity with humanlike machines may sensitise Japanese users to inauthenticity, so that cues which feel warm elsewhere register as performative. This is offered as interpretation, not tested. Each country cell had about 100 participants per arm, which the authors say limits power to detect small effects; the within-country design was powered only for d = 0.40.

### Discussion and the three reorientations

The authors draw three conclusions:
1. **A saliency gap.** Academic anthropomorphism scales emphasise human-uniqueness markers (consciousness, intentionality, spirituality). Users, when not prompted, attend to conversation flow, speed, authenticity and perspective-taking. The authors call for moving the research agenda from abstract debates about machine consciousness towards measurable design cues.
2. **A non-linear harm model.** The idea that more humanlike means more engagement and more trust is not supported as a general rule. The authors propose that humanlike design acts as a "catalyst" only when it co-occurs with perceived competence and shared purpose. Their own data show users' judgements of competence and alignment did not change, so the cues activated anthropomorphism without changing whether users judged the system able to help. This explanation is the authors' conjecture.
3. **No universal AI experience.** Risk is not an intrinsic property of humanlike design. It emerges from the interaction between design and cultural context, so governance should be context-dependent and culturally informed rather than universal restrictions.

### Limitations the authors state

- The conversations were mundane and non-sensitive by design, for ecological validity. The results may not transfer to medical, financial or crisis-support contexts.
- Text-only interface. Voice or embodied systems might produce stronger responses.
- A single underlying model (GPT-4o), which limits generalisation to other models.
- A cross-sectional design, which captures immediate responses only.
- Future work is suggested for high-stakes persuasion or fraud, voice and embodied AI, longitudinal designs, vulnerable populations (children, older adults, lonely people) and cultural moderators.

### Methods details worth knowing

- Study 1 exclusions: 342 failed an attention check, 32 gave ineligible open-ended answers, 107 failed the panel provider's quality standards.
- Study 2 exclusions: 874 failed an attention check, 260 gave ineligible open-ended answers, 78 failed the panel's quality standards. Sampling continued until 2,400 complete responses were obtained.
- The Study 2 pre-registration was not formally registered before data collection because of an upload problem discovered afterwards. The authors say they followed the intended protocol and label deviations as exploratory.
- Open-ended responses in Study 1 were translated into English with Google Translate for codebook development, but the autorater was run on original-language responses.
- Data and code are said to be on OSF; the supplementary material was not part of the source text used here.

## Techniques & methods explained

- **Open-ended live interaction with a fixed chatbot.** Participants chat for at least four minutes on everyday topics, in their native language, with a system prompt governing the bot. Steps: recruit from a panel, obtain consent, brief participants that they are talking to a chatbot, run the conversation, then survey. Purpose: capture anthropomorphism as it unfolds in interaction rather than from vignettes. Limit: the topic restriction means high-intent or sensitive contexts are not tested.
- **Multi-attribute Likert anthropomorphism battery.** Ten attributes from earlier scales, chosen to cover social perception, sentience-related items and personality/emotion items. Purpose: test dimensions separately rather than form one composite. Limit: the items are the theory-driven framing the paper later says users do not spontaneously use.
- **Inductive thematic analysis of open-ended answers.** Three researchers coded 100 responses, calibrated on 20, then validated on 100. The codebook merged user-driven labels with ten theory-driven ones.
- **LLM-in-the-loop autorating.** Gemini 2.5 Pro with few-shot instructions labelled all 1,100 responses. Limit: the autorater's mean F1 was 0.53 against the gold standard, and mean inter-rater kappa between human coders was 0.28 across labels.
- **2 x 2 factorial manipulation via system prompts.** Four conditions crossing DC and CS, with the control being low on both. Step: write prompts that vary speed, tone, emoji, name and warmth, have experts check the conditions are distinct and realistic, then run the study. Limit: all conditions share one model, and the manipulation is a prompt, not a product change.
- **Incentivised one-shot Trust Game.** Participants invest points with a tripled return and the AI decides how much to return. Purpose: a behavioural trust measure. Limit: a single low-stakes round with points convertible to a small bonus.
- **Engagement from chat logs.** Message count and length, with per-country min-max normalisation and a multilingual BERT tokenizer for token counts.
- **Equivalence testing and Bayesian evidence for nulls.** TOST with a smallest effect size of interest of d = 0.20, and Bayes factors. Purpose: support a claim of no effect rather than just failing to find one.
- **OLS regression with dummy-coded conditions**, plus descriptive analysis and exploratory country-level subgroup regressions.

## Pros, cons & trade-offs it surfaces

| Aspect | As the paper presents it | Notes |
|---|---|---|
| Ecological validity | Open-ended, real-time conversation rather than vignettes | Limited to mundane, non-sensitive topics (authors' own caveat) |
| Causal evidence | Randomised factorial manipulation of humanlikeness | Manipulation is by system prompt on one model |
| Cross-cultural scope | Ten countries (Study 1), six (Study 2), native-language surveys | Country-level Study 2 cells are small (about 100 per arm) and exploratory |
| Measurement | Multiple self-report and behavioural measures; exclusions pre-registered | Trust is a single one-shot game; autorater reliability is modest |
| Null result on trust | Equivalence testing and Bayes factors support no pooled effect | Equivalence bound and game design are choices; the null is pooled, not per-country |
| Practical implication | Humanlike design can be used in low-risk contexts to improve experience | Authors warn about susceptible subgroups and high-stakes use |

Source view versus my own: the authors present the findings as a challenge to the assumption of a single psychological risk profile for humanlike AI, and as support for context-dependent governance. They also acknowledge that the high-stakes cases most worrying to safety researchers are untested.

## Key concepts & terminology

- **Anthropomorphism** - attributing human characteristics (agency, intelligence, personality) to AI, as used here.
- **User-driven aspects** - humanlikeness dimensions derived inductively from what users said (conversation flow, response speed, perspective-taking, authenticity).
- **Theory-driven aspects** - dimensions taken from existing anthropomorphism scales (consciousness, soul, morality, intelligence, warmth).
- **Saliency gap** - the mismatch between which attributes academic scales emphasise and which users spontaneously mention.
- **Design Characteristics (DC)** - the appearance and mechanical features of the chatbot: latency, tone, emoji, name, length.
- **Conversational Sociability (CS)** - the social and interpersonal behaviour: empathy, warmth, relationship-building, personality matching.
- **Heterogeneous treatment effects** - effects that differ by subgroup or country, including effects in opposite directions.
- **Justified trust** - trust that tracks perceived competence and alignment with the user's goals, as cited from prior work.
- **Catalyst** - the authors' term for humanlike design amplifying anthropomorphism only where competence and shared purpose are present.
- **TOST (equivalence testing)** - a test that the difference between conditions lies within a chosen bound (here d = 0.20), supporting a claim of no meaningful effect.
- **Min-max normalisation within country** - rescaling each user's message-length measure relative to others from the same country.
- **LLM autorater** - a language model used as a labelling tool, here Gemini 2.5 Pro.
- **WEIRD** - Western, educated, industrialised, rich, democratic; the sample bias the paper aims to correct.
- **Uncanny valley (as used here)** - the authors' interpretation of Japanese participants' backlash: cues fall short of culturally calibrated expectations.

## Evidence, examples & notable data points

- Abstract and Study 1: about 68% rated the chatbot humanlike; about 75% rated it conscious; about 90% intelligent (Study 1, n = 1,100, ten countries).
- Study 1 country clusters: mean humanlike rating 3.98 in the six-country cluster versus 3.29 in the four-country cluster.
- Cultural distance and anthropomorphism: r = 0.52 across ten countries, not significant (p = 0.127).
- Open-ended mentions: conversation flow 32.1%, perspective-taking 24.4%, response speed 22.5%, authenticity 18.4%, intelligence 8.8%, empathy 5.5%, consciousness and soul each under 0.5%.
- Preference: 76.2% of Study 1 participants picked "more" or "much more" humanlike AI for the future.
- Study 2 manipulation check: most humanlike versus control, b = 0.386, p < 0.001, on the humanlike item; significant on 7 of 10 items; no effect on intelligence, competence or consciousness.
- Trust game: pooled difference t(1194) = 0.038, p = 0.969, d = 0.002; equivalence at d = 0.20; BF01 11.9 to 34.6.
- Engagement: humanlike design increased engagement against control (d = 0.25, p < 0.001).
- Brazil: higher engagement, willingness to reuse, friend perception and trust under humanlike cues. Japan: under high-DC/low-CS cues, lower reuse intention, friend perception and trust. Egypt, India and Japan: humanlike-only effect on the humanlike item not significant.
- Coding quality: mean human-coder kappa 0.28 across labels; autorater mean F1 0.53.

Memorable line from the source, paraphrased: humanity is in the middle of a large real-time social experiment whose effects are not yet measured.

## Connections

### Within this section

I have read the full text of this paper and the section page. For the sibling readings I have only their titles and paths; the links below are based on those titles and the course guide text, not on their contents, and should be checked against the sibling summaries.

- [Unit 4 Glossary](01-unit-4-glossary.md) - useful for checking "anthropomorphism", "moral patienthood" and related terms used here.
- [Seemingly Conscious Chatbots and their Impacts on Users](02-seemingly-conscious-chatbots-and-their-impacts-on-users.md) - a Core reading on user impacts of perceived consciousness. This paper's null trust result and its finding that consciousness is rarely spontaneously mentioned bear directly on whether those impacts flow from consciousness beliefs or from interaction design.
- [We mustn't let AI hack our empathy circuits](03-we-mustnt-let-ai-hack-our-empathy-circuits.md) - Suleyman's argument that humanlike AI can exploit empathy. This paper partly tests that premise: humanlike cues raised anthropomorphism but not trust in the pooled sample.
- [Conscious Artificial Intelligence and Biological Naturalism](04-conscious-artificial-intelligence-and-biological-naturalism.md) - Seth's account of impenetrable illusions of consciousness (Section 6.2 is the assigned excerpt). The paper here studies interactions with a known AI, so it does not test whether the illusion persists after disclosure.
- [Ascribing consciousness to artificial intelligence](05-ascribing-consciousness-to-artificial-intelligence-human-ai.md) - Guingrich and Graziano on carry-over effects of human-AI interaction; the question of spillover into human-human interaction is not addressed here.
- [AI Consciousness will Divide Society](06-ai-consciousness-will-divide-society.md) - Caviola on social division. This paper's cultural variation finding is a related, but different, source of divergence.
- [Seemingly Conscious AI Risks](07-seemingly-conscious-ai-risks.md) - a Further reading on risk categories; compare its framing with this paper's "risk emerges from interplay" conclusion.
- [Characterizing Delusional Spirals through Human-LLM Chat Logs](08-characterizing-delusional-spirals-through-human-llm-chat-log.md) - a high-stakes contrast: this paper deliberately excluded sensitive conversations, which is where its authors say their findings may not generalise.
- [Chatbots as Social Companions](09-chatbots-as-social-companions-how-people-perceive-consciousn.md) - linking perceived consciousness to social benefits; this paper's subgroup results (Brazil positive, Japan negative) are a caution against assuming uniform benefit.
- [The AI Bambi Effect](11-the-ai-bambi-effect.md) - cuteness as a perception cue. The DC manipulation here (emoji, name, tone) is a close analogue to cue-based perception.
- [What will society think about AI consciousness? Lessons from the animal case](12-what-will-society-think-about-ai-consciousness-lessons-from.md) - cultural analogies; the cross-cultural argument here is relevant to how animal-consciousness attitudes may transfer.
- [How it feels to have your mind hacked by an AI](13-how-it-feels-to-have-your-mind-hacked-by-an-ai.md) - a personal account of the susceptibility the paper's subgroup analysis is trying to quantify.
- [Folk Psychological Attributions of Consciousness to Large Language Models](14-folk-psychological-attributions-of-consciousness-to-large-la.md) - survey data on consciousness attributions; this paper's Likert "conscious" result (75%) and open-ended result (under 0.5%) are a useful comparison.

Exercises: Exercise 1 (impacts on individuals, society and AI systems; relational AI) draws on this paper's evidence about trust, engagement and emotional connection in subgroups, its cross-cultural divergence, and its discussion of humanlike design as a catalyst. It says little about impacts on AI systems themselves. Exercise 2 (connecting to earlier units) can use its point that users' spontaneous judgements do not track theories of consciousness.

### Across the course

These links come from the course outline and unit titles. I have not read the other units' content in this project.
- **Unit 1 (Introduction and theories of moral standing):** The paper does not address moral standing. Its "moral" item is one of the theory-driven constructs that users rarely mention, which bears on how moral patienthood is perceived in practice.
- **Unit 2 (Theories of consciousness):** The theory-driven constructs in this paper's codebook are the folk versions of theories of consciousness. The finding that users ignore them suggests public perception may be only loosely tied to theory.
- **Unit 3 (Evaluating mental states):** The paper's Likert items are a practical attempt to measure perceived mental states. Its finding that humanlike cues shifted anthropomorphism but not competence judgements is a case of separating two kinds of attribution.
- **Unit 5 (AI safety and ethics):** The over-trust and engagement harms in this paper are the safety concerns the unit deals with. The paper's conclusion that humanlike design is not inherently risky is a tension with the safety framing.
- **Unit 6 (Approaches under uncertainty):** The heterogeneous results and the careful equivalence testing are examples of reasoning under uncertain evidence about who is affected and how much.
- **Unit 7 (Digital minds governance):** The paper argues for culturally contingent, context-dependent governance rather than universal rules, which is a direct governance question.
- **Unit 8 (Reflections and next steps):** Useful for reflecting on how much evidence is needed before policy depends on cross-cultural effects.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Conflict of interest.** Three of the four authors are Google employees, and the study used a model from another company (OpenAI's GPT-4o) served through Google's study pipeline. The paper states Google had no role in design, collection, analysis or writing. That statement does not remove the need to weigh the results accordingly, and the authors do disclose the affiliation.
- **Cross-cultural conclusions outrun the country-level data.** The headline claim that effects depend on culture rests largely on country-by-country subgroups of about 100 per arm, powered only for d = 0.40. The authors call these exploratory, but the abstract and governance recommendations do not carry that caveat. The Japanese backlash is one exploratory cell, and the uncanny-valley explanation was not tested. The Study 1 cultural-distance correlation is non-significant with ten countries.
- **The null trust result is narrower than it sounds.** "No increase in trust" here means no increase in willingness to send points in a single, low-stakes investment game, plus self-reported items, in mundane chat. It says nothing about trust in high-stakes advice. The authors acknowledge this. The equivalence bound (d = 0.20) is a choice, and the pooled result may hide differences that the subgroup analysis partly tries to recover.
- **The consciousness finding is partly a question-design effect.** The open-ended prompt asks whether something made the participant feel they were talking to a human, not whether the chatbot is conscious. Asking about "human-ness" plausibly reduces mentions of consciousness, sentience and soul. The authors acknowledge that explicit items can elicit endorsement of such traits through priming. The "saliency gap" is therefore a finding about spontaneous responses to a human-ness question, not evidence that consciousness is irrelevant to perception.
- **Coding reliability is modest.** Human kappa of 0.28 and autorater F1 of 0.53 mean that the label-level frequencies, especially the rare ones (under 0.5%), carry substantial measurement error. Translating responses to English for the codebook while coding originals with the autorater adds another layer of variation.
- **Disclosed AI, not illusion.** In Study 2, participants were told they were talking to an LLM and the chatbot was given a human-sounding name and a human emoji in the high-DC condition. The study therefore measures responses to a known AI with human-like cues, which is different from the deceptive or unnoticed illusions that Seth and Suleyman are concerned about. The paper's null on trust should not be read as a rebuttal of the illusion concern.
- **Source inconsistency on the engagement metric.** The text reports engagement as "average number of messages," but the methods define average message length (and total message count) and the Figure 6 caption describes standardised mean message length. Check the supplementary material before citing the exact engagement effect.
- **Pre-registration is weaker than it sounds.** The Study 2 pre-registration was not formally registered before data collection. The authors disclose this and label deviations as exploratory, which is appropriate, but it means the "pre-registered" language applies to exclusion criteria and analysis plans only as far as the document was prepared before collection.
- **Rhetoric in the discussion.** The authors describe humanity as in the middle of a large live social experiment, and claim causal, ecologically valid cross-cultural evidence. Both claims are stronger than a single-model, mundane-topic, cross-sectional design supports.
- **What has changed since publication.** The data were collected in August to October 2024 using GPT-4o, a model now well behind current systems. Current products often add voice, persistent memory and persona features, and response latency and fluency are very different. The authors themselves flag voice and embodiment as untested. Findings about latency and conversational flow may not transfer, and the cultural pattern may have shifted as adoption has spread. By October 2026, the study is best read as evidence about a specific 2024 interface and model, and its general claims should be treated as hypotheses to test.
- **How other course perspectives would push back (my inference from titles and guides).** Suleyman would probably argue that a null result on mundane chat does not address emotional reliance or manipulation in the contexts where his concern is greatest. Seth would likely say that the persistence of perceived consciousness after disclosure is the important question, which this study does not test. The authors of the seemingly-conscious readings would likely say that the engagement increase here is itself a warning sign, not a safe outcome. The paper's own answer is that engagement and trust can diverge and that the divergence is itself a reason for context-specific governance.

## Discussion questions

1. The paper finds that users judge humanlikeness mostly by conversation flow, speed and perspective-taking, not by sentience or consciousness. Using Exercise 1, which impacts on individuals and society follow more from these interactional cues than from beliefs about consciousness? Which would you prioritise for governance, and why?
2. Study 2 told participants they were talking to an LLM and still found increased anthropomorphism and engagement. Does that disclosure make the findings more or less relevant to the "illusion" concerns raised by Seth and Suleyman? What would a study that tests the illusion more directly look like?
3. The pooled trust effect is null while engagement rises. What does it mean for a product to increase use without increasing trust? How does this connect to the relational AI question in Exercise 1?
4. The authors report a positive effect in Brazil and a backlash in Japan. Does this support context-dependent, culturally informed governance, or is the subgroup evidence too thin to base policy on? What study design would you need to settle it?
5. The open-ended question asked whether the chatbot made people feel "human." How might the sub-0.5% figure for consciousness change if participants were asked directly whether the AI is conscious? What does that imply about the "saliency gap" the authors describe, and about Exercise 2?
6. The authors suggest that humanlike cues only work as a catalyst when perceived competence and shared purpose are present, but they did not test this directly. Design one experiment that would separate capability-driven trust from other possible mechanisms.
7. Three of four authors work for Google and the model used is from OpenAI. Which disclosures, replications or independent analyses would you require before accepting the cross-cultural conclusions as a basis for governance?
