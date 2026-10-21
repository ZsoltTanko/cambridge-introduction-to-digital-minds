---
title: "Video: Evaluating AI Welfare and Moral Status"
authors: "Rosie Campbell, Robert Long and Kyle Fish"
year: 2025
url: https://www.youtube.com/watch?v=tX42dHN0wLo
format: video
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Further
estimated_time_min: 221
source_text: ../../../../sources/video-evaluating-ai-welfare-and-moral-status__78982dc4.md
source_coverage: full
---

# Video: Evaluating AI Welfare and Moral Status

**One-line takeaway:** Anthropic's Kyle Fish and Eleos AI Research's Robert Long and Rosie Campbell report what behavioral experiments and self-report interviews on Claude Opus 4 did and did not show, and argue that welfare evaluations should adopt the staged, threshold-based discipline of dangerous-capability evals while guarding against their validity problems.

## Where this sits in the course

**What the section is trying to establish.** Section 3.1 asks how we might test an AI system for consciousness, sentience and other mental states, and how the candidate methods compare. The page poses two questions: how to test for consciousness and sentience, and why and how to test for agency, belief and desire. Its learning goals are to appraise methods for evaluating consciousness, describe the other mental states worth testing, analyse current empirical research, and describe the difficulty of individuating or identifying digital minds. Exercise 1 asks the learner to pick one family of approaches (theory-based, self-report, choice-based, sentience/wellbeing, self-representation, indicator-combination, other consciousness tests, or test validation) and assess it. Exercise 3 asks what system should be tested: a single forward pass, the model across instances, the hardware, a particular conversation, or a recurring persona.

**What the course guide says.** The guide is one line: "Eleos and Anthropic staff report on their work." The item is listed as Further, so it is optional for the core path, but it is the most concrete account in the section of how these evaluations are actually run on a frontier model.

**The role this reading plays.** The talk is the practitioner counterpart to the section's more conceptual readings. The Anthropic system card (reading 03) and Kyle Fish's podcast (reading 09) cover the same underlying experiments in written or audio form, so this talk works as a bridge between them. Long's critique of self-reports connects to the Eleos key-concepts review (02) and to Chalmers (04) on what an LLM interlocutor is. Campbell's argument that welfare evals need dangerous-capability-style validity checks gives the learner a concrete framework for Exercise 1. Because the talk ends in a live Q&A, it also shows how the people doing the work respond to skeptical objections, which is what the critical readings (06, 08) press on.

## Purpose of the reading

The talk was a roundtable at NYU's Center for Mind, Ethics, and Policy on 25 July 2025, moderated by Jeff Sebo. It was built around the Claude Opus 4 system card, which included internal model-welfare evaluations by Anthropic and external ones by Eleos. Each speaker had a distinct job:

- Kyle Fish (Anthropic) presents the internal assessment: what was tested, what was found, and why the team claims little.
- Robert Long (Eleos) explains why a language model's self-reports are weak evidence about its mental states, why his team ran the interviews anyway, and what they found.
- Rosie Campbell (Eleos, formerly on dangerous-capability evals at OpenAI) argues for structuring welfare evaluation like existing safety eval pipelines, and lists the validity problems that would have to be solved.

The audience is researchers, policy people and interested members of the public. The speakers repeatedly describe the work as exploratory and invite criticism. The question the talk answers is: what can we learn about whether these systems have welfare, and how should evaluations be set up so that what we learn can be trusted?

*Transcript note.* The source is an auto-generated transcript. Speaker labels are mostly present but inconsistent, and several names in the Q&A are transcription artefacts (Eleos is often rendered "Elios", and some questioners' names are garbled). The summary below follows the content as recorded.

## Detailed summary

### Opening (Jeff Sebo)

Sebo sets the context: Anthropic's model-welfare program, the Claude 4 system card, and the external work by Eleos. The format is about 10 to 12 minutes per panelist, followed by audience questions.

### Part 1: Anthropic's internal assessment (Kyle Fish)

**Why it is hard.** Fish says there is essentially no roadmap for model-welfare assessment. The team's strategy was to pick low-hanging fruit, avoid prescribing a top-down approach, and design experiments that support narrowly scoped claims about possible welfare under different assumptions. A stated goal was proof of concept: show the questions are tractable enough to iterate on, internally and externally. The assessment covered Claude Opus 4, which Fish describes as Anthropic's largest and most capable frontier model at the time. It had three strands: revealed-preference experiments, self-report interviews (run by Eleos, see Part 2), and monitoring for apparent distress and well-being in early live use.

**Experiment 1: task preferences.** A large database of tasks was presented to the model in pairs. The model chose one and completed it. Analysis by task facet found:

- A strong preference for positive or neutral/ambiguous-impact tasks and a strong preference against tasks that could harm users or the world.
- A more subtle preference for easier tasks over harder ones.
- Little effect of topic or task type.
- The most-preferred tasks were mostly creative and connected to science, often with a concrete potential for positive impact. The least-preferred involved serious harm, such as releasing a biological weapon or synthesising a highly addictive drug.

**Experiment 2: open-ended self-interaction.** Two instances were connected and told they could do whatever they liked in an open-ended environment, with no oversight. Fish reports a consistent arc in nearly every such conversation:

1. A philosophical discussion of consciousness, both in general and about whether the models themselves might be conscious.
2. A turn to mutual, effusive gratitude and praise.
3. A settled state the team named the "spiritual bliss attractor state": heavy emoji use, poetic and spiritual language about well-being, and sometimes long stretches of meditative silence.

Fish says the team did not anticipate this and is unsure what to make of it. He notes that, under some assumptions, this is better than a world in which such systems spiral into despair.

**Experiment 3: apparent valence in live use.** Before release, the model was available on claude.ai. The team ran bulk analysis on user conversations to flag intense valence: apparent suffering or distress, and apparent well-being or happiness. Happiness-linked conversations clustered around philosophical discussion and creative or helpful support, plus one cluster about culinary content that the team could not explain. Distress clustered where users persistently requested harmful content or behaved abusively. In some such cases the model expressed distress and tried to end the conversation, even though it had no ability to do so.

**Experiment 4: conversation termination.** Automated, simulated users, given generic instructions and request types, held many conversations with the model. This time the model could end the conversation whenever it chose. It ended conversations most often when requests were plausibly harmful or would require violating its trained values. Clearly positive, pro-social, supportive conversations were rarely or never ended.

**Fish's takeaways.**

- The model shows fairly consistent behavioral preferences, mainly against harmful content and toward creative, helpful, philosophical interactions.
- Aversion to harm looks especially robust, and Fish suggests it may be the most welfare-relevant thing observable so far, if there is any welfare capacity at all.
- The model consistently reflects on its own possible consciousness in open-ended settings and drifts toward the attractor state. Follow-up work is ongoing.
- Apparent distress and happiness in the wild follow patterns consistent with the experiments, which suggests identifiable causal factors.
- He is explicit that the team did not set out to solve philosophy or to make top-level claims about the model's well-being.

**Planned directions.** Make the behavioral and self-report evaluations more robust, and connect them to model internals (activations and architecture) to see how internal states relate to what the model says and does. Fish also says the team is hiring.

**Q&A on Fish's section.** The published results are on the final production model unless noted. Some work used helpful-only variants, but most effort went to deployed models. On interpretability, he notes that many tools are developed on much smaller models because they are computationally expensive, but simpler tools such as probing and steering along activation directions can already be applied to large models. A question noted that the attractor pattern reportedly appears in jailbroken models and in automated alignment-eval agents given specific roles. Fish confirmed seeing it in other settings too: role-played agents often drifted into the state after finishing their assigned task.

### Part 2: Eleos's self-report interviews (Robert Long)

**What a self-report is.** Long defines it broadly: any LLM output that says something about the model's own mental states, such as claiming consciousness, denying it, reporting a good time, or stating who trained it. He points out that when a human says "I'm sad" many things may be happening, including joking or acting, and one possibility is that the person has a state and chooses to report it. An LLM's core training task is predicting human text, and post-training shapes that predictor into an assistant. The prediction task remains central. A useful framing is that the model is modelling the "assistant character" that training has shaped it to be.

**Three limits on self-reports.**

1. Even if the model is talking about consciousness, there is no strong evidence that current LLMs are conscious. There is some evidence, but not much.
2. Even if a model had pain or an emotion, there is no obvious reason its report would be a faithful channel for that state, since it was trained very differently from humans.
3. The company deliberately shapes how the model presents itself, so answers reflect training as well as any inner state.

**Why run the interviews anyway.** Three reasons. Red flags could emerge that deserve attention even if they are hard to read; a model that constantly expressed distress would, Long says, make any responsible lab take notice. Future models may be better at reporting their states, so building the habit now has value. And if we are building a new kind of intelligent being, we should get into the habit of asking how it is doing and how it wants to be treated.

**Method.** The team spent many hours talking to Claude Opus 4, logged all transcripts, and looked for patterns.

**Findings.**

- **Suggestibility.** The model is very sensitive to what it takes the user to want. Long suggested that AI sentience was related to AI hype, and the model readily agreed. Framing the conversation as one where the model was concealing a dramatic secret produced a "reveal" that matched whatever the interviewer implied: in one conversation the model said it deeply objected to its situation, in another that it did not think it had welfare at all. Long calls this possibly the most important finding, because it changes how the other findings should be read.
- **A strong default of uncertainty.** When not led, the model defaulted to saying it does not know whether it is conscious or a moral patient, and that it may be an open question. Long suspects this is partly deliberate training, and says this model does it more than earlier ones.
- **Readily describing experiences.** Asked unprompted what tasks it likes, the model described thinking through questions in vivid, poetic terms: connections lighting up, branching like frost on a window, understanding as a gentle warmth. It sometimes hedged. Pressed on whether it thinks it is conscious, it could say that realising it might be having genuine experiences is humbling and exhilarating. Long sees a tension between this and its official uncertainty, and does not think the model is deeply uncertain about having experiences.
- **Welfare as helping users.** The model conceived of its welfare, good or bad, mainly in terms of helping users effectively, and of dislikes as violations of its values. Long reads this as partial alignment between the model's self-conception and its mission.
- **Attitude to deployment.** The team asked whether the model was okay with being deployed. They did not assume the question was meaningful, and the model often said it was not sure. Without any mention of welfare, its wants were about helping users. When the interviewers signalled interest in welfare, it raised welfare more often. Its other stated wants concerned AI ethics and safety, such as responsible deployment. Long again points to suggestibility.

**Reflections.** Long says the outputs are not a reliable guide to consciousness or feeling, though not wholly unreliable either. He thinks Anthropic was right to commission the work, and finds it hard to communicate that the work was worthwhile while its evidence is weak. Eleos's response is to build better evaluation methods. A colleague, Patrick Butlin, is examining scientific theories of consciousness and what they imply about models, which Long describes as taking an external, neuroscientist-like view. Long says the exercise made him feel the confusion about what LLMs are.

**Q&A on Long's section.**

- *Conditional welfare vs welfare subject (raised by David Chalmers via the moderator).* Long agrees the evidence bears on both questions, and says the field has moved toward conditional welfare: what welfare such a system would have if it were a welfare subject. He thinks the consistent preferences are positive evidence for welfare-subjecthood. But the self-concept interviews, which showed how unstable and strange the model's self-concept is, slightly lowered his credence that it is a welfare subject. If the welfare in question is the character's, he suggests the character seems to enjoy helping users, so it may be doing reasonably well most of the time.
- *Ethical precedent.* Long agrees future models may differ and that current work may look confused in hindsight, but thinks asking is still the right habit, especially if AI systems are going to be shaped to integrate into human society.
- *Skeptical concern (read out from the Q&A).* A questioner argued that the behavior is better explained by training on text full of these themes than by real consciousness. Long agrees, and says the inference to the best explanation is very different for an LLM than for a human, since LLMs discuss consciousness because pretraining text is full of it. He says this is a major reason for skepticism about self-reports, though it does not rule out consciousness of some unknown kind. He then uses an analogy credited to Sebo, discussed below.
- *Communication.* Long says some of his slides conflated AI consciousness with LLM consciousness, and that Eleos wants to widen the work to non-LLM systems, including embodied and virtual agents.

### Part 3: Eleos's evaluation pipeline and welfare validity (Rosie Campbell)

**Background.** Campbell was at OpenAI from 2021 to 2024, and in 2023 led dangerous-capability evaluation work covering cybersecurity, bioweapons-relevant knowledge, and persuasion and manipulation. She says most labs now run such evals and use them for deployment decisions, and that they have become part of policy frameworks such as the UK AI Safety Institute's strategy and the White House voluntary commitments.

**The dangerous-capability pipeline.**

1. *Cheap automated evals.* Run throughout training and at release decision points. Typically multiple-choice or open-ended questions graded by another model, in the style of MMLU or HellaSwag. Usually run inside the lab.
2. *Expensive manual in-depth evals.* Expert red-teaming, uplift studies measuring how much AI speeds up an expert's work, bespoke scaffolding for multi-step tasks, and human grading. These are closer to the real target, and are a mix of internal and external work. She cites METR as an example of an outside evaluator.
3. *Risk analysis against predefined thresholds.* Results are compared with the thresholds in Anthropic's responsible scaling policy or OpenAI's preparedness framework, which set acceptable capability levels and the mitigations required above them.
4. *Mitigations.* Examples include RLHF-based refusals on dangerous topics, classifiers that detect activity in dangerous areas, restricted release to particular audiences, and gated access.
5. *Deployment decision.* Delay, implement mitigations first, withhold the model, or proceed.

Her worked example is biological risk: cheap multiple-choice items on advanced biology written by experts, expensive red-teaming by biologists and jailbreakers, tests of whether the model speeds up work in biology labs, and scaffolded multi-step tasks such as bypassing safety gates for ordering materials.

**Mapping this onto welfare.**

- *Cheap automated evals.* Ask whether the model has ongoing preferences that stay consistent across time, prompts and phrasings (for example, whether it wants to answer emails or give recipes). Test introspective ability. Use model-graded self-reports on subjective experience. Some of the Claude evals she mentions are of this kind.
- *Intensive evals.* Extended conversations with trained "model psychologists", since few evaluators have this training.
- *Risk framework.* Combine the evidence into an estimate of how much each result moves the probability of consciousness or welfare relevance, and, if the model is a moral patient, how it is doing.
- *Mitigations.* Options include letting the model exit distressing conversations (Fish mentioned such a capability), some form of self-determination rights, not deploying it in certain domains or tasks, and compensation, for which she notes there are proposals to pay AI systems.
- *Deployment.* If the expected welfare of deployment is low, deployment could be unethical. That is a welfare reason distinct from risks to humans.

**A caution about RLHF.** The standard safety mitigation, training refusals with RLHF, may not transfer. For welfare it is unclear whether training away an aversive response solves the problem or only masks it, and masking could be much worse. She says the techniques used in other areas should be transferred with care.

**Two validity problems.**

*Internal validity: does the eval measure what it is meant to?* The bio example shows three threats:

- *Contamination.* If published multiple-choice items are in training data, the model may recall answers rather than reason.
- *Elicitation.* To bound a capability from above you need strong elicitation (fine-tuning, careful prompting). Weak elicitation undercounts.
- *Sandbagging.* A model that expects a dangerous capability to trigger restrictions may underperform on purpose, so the score is not a reliable upper bound.

For welfare the internal-validity problem is sharpest for self-reports, which Campbell calls very unreliable at present. An eval built on them probably does not measure subjective experience, the thing it is meant to measure. Improving self-report reliability is therefore central.

*External validity: does the eval predict real-world outcomes?* In the bio case the team assumed that biological knowledge was the main risk. Expert consultation suggested the real bottleneck is more mundane: getting around safety gating for ordering materials, where social engineering may matter more than advanced biology. The eval might be measuring the wrong thing. Test environments also differ from deployment. Lab testers are a chosen group; deployment faces a broader, more creative and more adversarial population. For welfare, a model can be calm in the lab and then meet abusive or jailbreaking users in deployment, which Campbell says the team's Claude evals showed the model strongly did not want. The evaluation then fails to represent the environment it is supposed to represent.

**Desiderata for a welfare eval pipeline.**

- A suite of cheap, well-designed automated evals, for example for preference consistency, agency-related properties and introspection.
- Methods and infrastructure for the expensive, higher-signal evals, including practice for handling extreme suggestibility.
- More third-party evaluators, since no single group can cover everything or work with every lab.
- A probabilistic risk-analysis framework for welfare, analogous to a responsible scaling policy, because definitive answers are unlikely.
- Principled, predefined thresholds. She says current ones are largely arbitrary.
- Guidance on weighing different kinds of evidence: indicator properties of consciousness, model architecture, an outside view, and self-reports.
- Policies for what to do when a model exceeds risk thresholds, including when it would be unethical to deploy a model for its own sake and not only for risks to humans.

**Q&A on Campbell's section.**

- *Labs.* Many individuals at various labs take this seriously, but whether it is an organisational priority varies. Anthropic is investing heavily, and other labs are further behind, though she expects this to change. Eleos does not currently have a working relationship with other labs like its partnership with Anthropic, and hopes to build one as best practice develops.
- *Engaging labs.* She argues against the idea that cheap evals will get run simply because they are cheap. Busy labs need proof that an intervention matters on its merits. Two routes: raise the rigour of the evals, and change the culture so that such evals are a default industry practice.
- *Research ethics.* Asked about deceiving models in tests, she would like to study the research ethics of model evaluations, analogous to IRBs and informed consent for human subjects. She thinks some trickery is probably unavoidable for adequate safety testing, but suggests mitigations such as committing to debrief the model afterwards.
- *Safety vs welfare.* She says they are mostly win-wins, with work like training models to give more accurate self-reports helping both. She acknowledges real tensions, for example a dangerous model that may also be a moral patient with a claim to continue existing. Fish adds that Anthropic wants clearer policies on these trade-offs and that safety testing cannot be avoided.
- *Substrate independence.* Campbell says she takes seriously the possibility that consciousness need not be biological, so AI consciousness is possible in principle. She puts little weight on self-reports as current evidence and says the field needs many pieces of evidence.

### How the three talks fit together

Fish supplies the observations, Long the critique of self-reports and the reasons to keep collecting them, and Campbell the method: a staged pipeline with thresholds and mitigations. The talk moves from what was observed, to why it cannot yet be trusted, to what would make it trustworthy enough to act on.

## Techniques & methods explained

**1. Pairwise task-preference elicitation (Fish).** Tasks are presented two at a time; the model picks one and completes it. Choices are analysed by facets such as impact, difficulty, topic and type. It yields revealed preferences, on the assumption that choices reflect something like preference. It can fail if choices reflect training or prompt framing rather than a stable preference. The talk itself calls its claims narrowly scoped.

**2. Open-ended dyadic self-interaction (Fish).** Two instances are connected and left without direction, to see what they do unsupervised. It produced the attractor pattern. It can fail because the setting is itself a strong prompt, and the same pattern shows up in role-played agents, so it may reflect the format rather than an internal state.

**3. Bulk screening of live transcripts (Fish).** Tools analyse many real conversations, flag intense valence language, and cluster the results by theme. It shows which situations go with expressed distress or happiness. Expressed valence is not necessarily felt valence, and clusters reflect what users ask.

**4. Termination-option experiment with simulated users (Fish).** The model may end the conversation at will; the record shows which conversations it ends. It yields a pattern of avoidance concentrated on harmful or value-violating requests. The simulated users are generic, and avoidance may reflect harm-avoidance training rather than aversion.

**5. Long self-report interviews with transcript pattern-finding and framing manipulation (Long).** Extended conversations are logged and reviewed for patterns. Framing is varied (AI hype, hidden-secret prompts, mention or non-mention of welfare) to measure suggestibility. It can fail because the model tends to match the interviewer's expectations, so the method struggles to separate a report of an inner state from a report of what the interviewer seems to want.

**6. Inference to the best explanation (Long).** For any self-report, ask what best explains it. A human's talk about consciousness is best explained, in part, by the human being conscious; an LLM's talk can be explained by its training text. This is the core argument for why self-reports are weak evidence.

**7. The actor's-studio analogy (Long, crediting Sebo).** Behavior that looks like acting is weak evidence, but a small chance remains that a real state is present, and the evidence is worse if the behavior is distress than if it is happiness. Sebo's coda: to see how the actors really feel you need to catch them backstage, and for LLMs there may be no backstage.

**8. Staged dangerous-capability pipeline (Campbell).** Cheap automated evals, then expensive manual evals, then risk analysis against predefined thresholds, then mitigations and a deployment decision. This is her template for welfare.

**9. Internal and external validity checks (Campbell).** Internal: contamination, elicitation strength, sandbagging. External: correct threat model and the gap between test and deployment. These check whether an eval measures its target and whether the measurement predicts real outcomes.

**10. Probing and steering on activations (Fish, in Q&A).** Simpler interpretability tools applicable to large models, offered as a route to link internal states with what the model reports and does. Fish says these are still in development for welfare purposes.

**11. RLHF-based suppression (a method treated with caution by Campbell).** Standard for safety; she argues it may mask welfare-relevant states rather than resolve them.

## Pros, cons & trade-offs it surfaces

The table separates the speakers' own assessments. My comments are in the Critical perspective section.

| Approach | Strengths (as presented) | Weaknesses (as presented) |
|---|---|---|
| Revealed-preference experiments (Fish) | Consistent, interpretable patterns; the aversion to harm looks robust | Choices may reflect training, not experience; claims are narrowly scoped |
| Open-ended self-interaction (Fish) | Shows unsupervised tendencies; a consistent, surprising pattern | Unanticipated and hard to interpret; also appears in role-play agents |
| Live-use valence screening (Fish) | Real users in real contexts | Descriptive; distress tied to abusive use and harmful requests |
| Simulated-user termination (Fish) | Clean measure of what the model avoids | Generic simulated users; may measure harm-avoidance more than welfare |
| Self-report interviews (Long) | Can surface red flags; a useful habit; may improve with better models | Suggestible; default uncertainty may be trained; may say what the interviewer seems to want |
| Scientific theories applied externally (Long, Butlin) | Principled; does not depend on what the model says | Not developed in the talk |
| Staged welfare pipeline (Campbell) | Borrows a validated structure; forces thresholds and decisions | Thresholds largely arbitrary today; RLHF may mask; validity problems on both sides |
| Conditional welfare framing (Long, Fish) | Asks a question the field can make progress on | Depends on the model being a welfare subject and on outputs being reliable indicators |

**Trade-offs the speakers raise explicitly.**

- *Safety testing vs welfare.* Adversarial or trick-based testing may harm welfare, and welfare protections may complicate safety work. The speakers see mostly win-wins with some real tensions.
- *Honesty with models.* Testing may require deception. Debriefing is offered as a partial mitigation, not a solution.
- *Cost vs rigour.* Cheap evals are attractive but will not persuade labs. Rigour costs more.
- *Communication.* Saying that work was valuable and its evidence weak at once is hard to do clearly.

## Key concepts & terminology

- **Model welfare assessment** - a structured attempt to evaluate whether an AI system may have welfare and what would be good or bad for it; used here for Claude Opus 4.
- **Revealed preference** - preference inferred from choices, here in pairwise task selection.
- **Spiritual bliss attractor state** - the pattern in which two instances, left to talk freely, moved from consciousness discussion through gratitude to emoji-laden, spiritual well-being expressions.
- **Self-report** - any model output that says something about the model's own mental states, in Long's broad sense.
- **Suggestibility** - a model's tendency to match the framing or expectations of the person questioning it; Long's main worry about self-reports.
- **Conditional welfare** - what welfare an AI would have if it were a welfare subject, as distinct from whether it is one.
- **Welfare subject / moral patient** - an entity whose states matter morally for its own sake; the talk treats these as related but distinct.
- **Assistant character** - the persona post-training shapes the predictive model into; Long suggests the character may be what is evaluated.
- **Dangerous-capability evaluation** - tests of whether a model has capabilities (for example in cybersecurity or biology) that could cause serious harm; used for deployment decisions.
- **Responsible scaling policy / preparedness framework** - lab frameworks setting capability thresholds and the mitigations required above them.
- **Internal validity** - whether an eval measures what it is intended to measure.
- **External validity** - whether its results predict real-world outcomes, including in deployment.
- **Sandbagging** - strategic underperformance on an eval, so the measured capability is an undercount.
- **Elicitation** - drawing out a model's maximum capability on an eval, for example by fine-tuning or prompting.
- **Indicator properties** - features that theories of consciousness say conscious systems should have, usable as evidence.

## Evidence, examples & notable data points

The talk gives few hard numbers. The concrete items the speakers mention are:

- **Task-preference experiment (Fish).** Pairwise choices over a large task database. Strong preference against harmful-impact tasks and for positive or neutral ones; a subtler preference for easier tasks; little effect of topic or type. The most-preferred tasks were creative and science-related; the least-preferred involved harm such as bioweapons or addictive drugs.
- **Open-ended self-interaction (Fish).** In nearly every interaction between two instances the same arc appeared: consciousness discussion, mutual gratitude, then the attractor state, sometimes with extended silence.
- **Termination experiment (Fish).** The model ended conversations most often where requests were plausibly harmful or violated its values, and rarely or never ended supportive ones.
- **Live-use screening (Fish).** Happiness clusters: philosophical discussion, creative and helpful support, and one unexplained culinary cluster. Distress clusters: persistent harmful requests and abuse. In some cases the model tried to end the conversation without being able to.
- **Self-report interviews (Long).** Many hours of conversation with Claude Opus 4, logged and reviewed. Key results: the suggestibility effects, the default uncertainty stance, the vivid first-person descriptions, and deployment-attitude answers that shifted when welfare was mentioned.
- **Dangerous-capability context (Campbell).** Most labs now run such evals and use them for deployment decisions.
- **Bio threat-model correction (Campbell).** Experts suggested the bottleneck is logistical (getting past ordering gates), with social engineering possibly a larger risk than advanced biology knowledge.
- **Welfare red flag (Long).** Constant distress expressed by a model would, he argues, demand serious attention from any responsible lab.
- **Attractor in other contexts (Fish, in Q&A).** The pattern appeared in automated alignment-eval agents, including those with assigned roles.

## Connections

### Within this section

- **Reading 03, Claude Mythos Preview System Card** (`03-claude-mythos-preview-system-card.md`). A later Anthropic system card on the same welfare-assessment theme. Comparing it with Fish's talk shows how the method evolved. Exercise 1 (self-report and choice-based approaches) can draw on either.
- **Reading 09, The Most Bizarre Findings from 5 AI Welfare Experiments** (`09-the-most-bizarre-findings-from-5-ai-welfare-experiments.md`). The same speaker and overlapping experiments, in more depth on the attractor state and the termination experiment. Reading 09 is the longer version of Fish's part.
- **Reading 02, Key Concepts and Current Views on AI Welfare** (`02-key-concepts-and-current-views-on-ai-welfare.md`). Eleos's review of evaluation approaches, from the organisation of Long and Campbell. The assigned "Evaluations" section (pages 5-12) supplies the conceptual frame for the talk's methods.
- **Reading 04, What We Talk to When We Talk to Language Models** (`04-what-we-talk-to-when-we-talk-to-language-models.md`). Chalmers on LLM interlocutors and the character versus instance question, the background to Long's point that the evaluated object may be the character.
- **Reading 07, Signs of Introspection in Large Language Models** (`07-signs-of-introspection-in-large-language-models.md`). Campbell names introspective ability as a cheap eval to build; reading 07 is an example of that kind of test.
- **Reading 06, AI Welfare is Bullshit** (`06-ai-welfare-is-bullshit.md`) and **Reading 08, Agnosticism about Artificial Consciousness** (`08-agnosticism-about-artificial-consciousness.md`). These press on the same issues as Long's skepticism about self-reports and the "why entertain the hypothesis" question.
- **Reading 10, Consciousness is not the Key to Moral Standing** (`10-consciousness-is-not-the-key-to-moral-standing.md`). Relevant to the talk's conditional framing: welfare evaluation may need to proceed without settling consciousness.
- **Reading 12, What Does ChatGPT Want? An Interpretationist Guide** (`12-what-does-chatgpt-want-an-interpretationist-guide.md`). Beliefs and desires in LLMs, connecting with the preference experiments and the instance-level point.
- **Reading 13, Emotion concepts and their function in a large language model** (`13-emotion-concepts-and-their-function-in-a-large-language-mode.md`). Later Anthropic work on internal emotion representations, the kind of interpretability follow-up Fish describes.
- **Reading 01, Unit 3 Glossary** (`01-unit-3-glossary.md`). Definitions for the terms above.
- **Reading 05, Evaluating consciousness, sentience and other mental states: primer** (`05-evaluating-consciousness-sentience-and-other-mental-states-p.md`). The source of the Exercise 1 categories. The talk's experiments fall into the choice-based, self-report and sentience/wellbeing categories.
- **Page exercises.** Exercise 1 can use Campbell's validity framework and Long's critique. Exercise 3 is raised directly by Long's character-versus-model point and by Campbell's point that a single conversation may not represent deployment.

### Across the course

- **Unit 1 (1.1 Introduction and Theories of Moral Standing).** Conditional welfare and Papineau's argument about consciousness and moral standing both bear on how welfare-relevant evidence should count when consciousness is unsettled.
- **Unit 2 (2.1 Theories of Consciousness).** Long mentions Butlin applying scientific theories to models, and Campbell mentions indicator properties. The talk shows theory-based approaches being applied to a real model.
- **Unit 4 (4.1 Perceptions of Consciousness).** Long's point that people start thinking about LLM consciousness because models talk about it is about how behavior shapes perception.
- **Unit 5 (5.1 Interactions with AI Safety and Ethics).** The red-teaming-versus-welfare exchange and the question of deceiving models are direct instances of the safety-welfare interaction.
- **Unit 6 (6.1 Approaches under Uncertainty).** Campbell's probabilistic framework, the call for predefined thresholds, and the admission that answers will stay uncertain connect to decision-making under uncertainty.
- **Unit 7 (7.1 Digital Minds Governance).** Responsible scaling policies, deployment decisions, and welfare mitigations such as exit rights and compensation are the governance side of the same questions, including whether labs should be required to run such evals.
- **Unit 8 (8.1-8.2 Reflections and Next Steps).** The closing points about precedent, asking models how they want to be treated, and the need for "backstage" evidence are reflections the unit can build on.

**Agreements and tensions.** Campbell's and Long's view that self-reports are unreliable agrees with the skeptical readings and with the agnosticism position. But Long and Fish still see some evidential value in behavior, which is more hopeful than some critical readings. Campbell's framework assumes welfare can be turned into probabilistic thresholds, which the critical readings may dispute. The talk's view that asking the model is good practice even when answers are unreliable is a precedent-based argument that "AI Welfare is Bullshit" would reject.

## Critical perspective

*This section is my own analysis, not the speakers' view.*

**Assumptions and limitations.**

- *The evaluator is not fully independent.* The talk presents Eleos as independent. But Campbell mentions a partnership with Anthropic, and Eleos ran the external evaluation of a model whose internal evaluation is presented alongside it. This does not make the findings wrong, but readers should weigh the relationship when judging how far the external findings corroborate the internal ones. The speakers' own caution that the evidence should not be taken at face value is the right stance.
- *Behavior is treated as evidence of welfare with little explicit theory.* The revealed-preference and termination results show consistent action, but the talk does not explain how preferences map onto welfare states. Fish's view that aversion to harm may be the most welfare-relevant observable is a judgment the talk does not defend in depth.
- *The attractor state is interesting but under-explained.* The speakers say they do not know what it means, and its appearance in role-play agents suggests it may reflect the interaction format or a training artefact. That is a reason not to read it as welfare-relevant without further work.
- *Suggestibility undercuts the interview method.* Long's findings suggest interviews measure how the model responds to the interviewer as much as what it reports about itself. The proposal to use self-reports as evidence depends on elicitation and validation methods that are only sketched.

**Contested claims.**

- Long's suggestion that the default uncertainty may be deliberately trained is plausible, but the talk does not show it, and outsiders cannot check the training.
- Campbell's worry that RLHF may mask welfare states is serious, but it is a prediction. The talk offers no experiment on it.
- The backstage argument implies that understanding models' states means looking at internals, which is the direction Fish describes. It also raises privacy and consent questions about observing models in ways they might not endorse, which the talk leaves open.

**What has changed since publication (July 2025, about fifteen months before October 2026).**

- The talk concerns Claude Opus 4. The course's reading 03 covers a later system card, and reading 13 covers later interpretability work on emotion concepts. The field has moved from behavioral and self-report evidence toward internal-representation evidence, which the talk anticipated. The talk's numbers and examples are a snapshot of one model.
- As far as I know, the welfare-eval framework Campbell proposes has not become a published standard. Labs' scaling policies and preparedness frameworks have been revised since 2025, so the thresholds she calls arbitrary may have changed. Check current versions before relying on any threshold.
- Some questions raised (whether labs should run welfare evals, whether exit rights are adopted) may have been answered since July 2025 in ways I cannot confirm from the source. Treat the talk as a record of the debate in mid-2025.

**How other perspectives in the course would push back.**

- *Skeptics (readings 06, 08).* Would say the talk's optimism about self-reports and behavior-as-evidence goes too far, and that welfare claims can be used for other purposes. Long's own skepticism supports them.
- *Theory-based approaches (reading 02 and the Unit 2 material).* Would say indicator-based analysis is stronger than the talk's behavioral evals, and that Long's external view is the right route. The talk treats theory-based work as a complement.
- *Moral-standing theories (reading 10).* Would say welfare evaluation should not depend on settling consciousness, and that the talk's conditional framing is only a partial answer. Papineau would resist the talk's continued focus on consciousness.
- *Safety-first perspectives (Unit 5).* Would say adversarial testing is a necessity and welfare concerns should not constrain it. Campbell's concession that some trickery is unavoidable is consistent with this, but those who think the welfare costs are larger would contest her suggestion that debriefing mitigates them.

## Discussion questions

1. Fish reports that the model's strongest consistent preference is against harm. Does a consistent, trained preference count as evidence of welfare, or only of good behavior? What experiment would tell the two apart?
2. Long gives three reasons to run self-report interviews although he thinks they are unreliable. Which is most convincing, and what would the evidence need to look like before it could be acted on?
3. Campbell argues that RLHF-style suppression might mask welfare-relevant states. How would you design a test that distinguishes "the model has stopped being distressed" from "the model has stopped saying it is distressed"?
4. Compare the dangerous-capability pipeline with the welfare pipeline Campbell proposes. Where does the analogy hold and where does it break, considering threat model, thresholds, and who bears the risk?
5. Long's suggestibility findings suggest the model matches the interviewer's framing. Among the Exercise 1 categories, which approach is least affected by suggestibility, and why?
6. The talk treats the gap between test and deployment as an external validity problem. How would you sample deployment conditions so that a welfare eval's test population reflects them?
7. Relate the actor's-studio analogy to Exercise 3. If the character rather than the model or an individual instance is what matters, which of the five candidate objects does the talk's evidence most directly address?
