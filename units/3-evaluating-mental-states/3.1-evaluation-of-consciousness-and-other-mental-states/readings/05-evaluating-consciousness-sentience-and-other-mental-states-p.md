---
title: "Evaluating consciousness, sentience and other mental states: primer"
authors: "Cambridge Digital Minds Course Team"
year: 2026
url: https://docs.google.com/document/d/1ijCseQ79SlLOi_7i38WbyzUYNfy_l-jErmRncLuKxqk/edit?tab=t.0
format: course-team primer
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Further
estimated_time_min: 46
source_text: ../../../../sources/evaluating-consciousness-sentience-and-other-menta__87ae199f.md
source_coverage: full
---

# Evaluating consciousness, sentience and other mental states: primer

**One-line takeaway:** No single test can settle whether an AI system is conscious or sentient; the course team's primer maps the main families of methods (theory-based, self-report, choice, functional emotion and wellbeing, self-representation, indicator-combining, classic tests, and test validation) and shows that each is weakened by the "gaming problem" or by circularity in validating the test.

## Where this sits in the course

Section 3.1 opens Unit 3 with two questions: how might we test for AI consciousness and sentience, and how do the methods compare; and why and how might we test for agency and other mental states such as belief and desire. The page's learning goals are to appraise methods for evaluating consciousness in AI, describe other mental states worth testing, analyse current empirical research, and describe the difficulty of individuating or identifying digital minds.

The primer is listed as **Further** and runs about 46 minutes. Its course guide is only a placeholder ("Primer on different approaches... Included in a written prompt for this unit"), so the course gives no explicit reason beyond it being a map. Its role is clearer from the exercises. **Exercise 1** (Core, free text) asks learners to choose one category of approach from this document, say what its core parts are, weigh its advantages and disadvantages, and say how it would shift the probability they assign to artificial moral patienthood. The exercise links to this primer for the category list. So although the reading list ranks it Further, learners who want to do Exercise 1 properly need it.

The other Core readings each take one approach in depth: the Eleos AI review (its "Evaluations" section), Anthropic's Mythos Preview system card (model welfare section), and Chalmers on what we talk to when we talk to language models. The primer supplies the taxonomy those readings sit inside. Its own framing is that the categories "can be blurrier in reality than implied here".

**Exercise 3** asks what system or process we should test: a single forward pass, the model across multiple instances, the hardware, a particular conversation, or a recurring character or persona. The primer does not answer this directly. It raises the same problem indirectly, through the individuation questions in the Chalmers reading and the note that some tests (such as the mirror tests) assume a stable self-model.

## Purpose of the reading

The primer is written by the course team as a starting point for discussion. It says it "is not complete", and it is meant to introduce different methods for establishing whether systems may be conscious, sentient or have morally relevant mental states, together with the challenges each faces. It is aimed at learners who are not specialists and who will discuss the material in small groups.

The question it answers is: what methods do researchers actually use or propose to evaluate AI for consciousness and related states, and why does none of them settle the matter?

## Detailed summary

The primer is organised by family of approach. The order below follows the source. The "gaming problem", which the primer introduces only at the end, is the main reason most of the earlier sections are cautious, so it is flagged where it bites.

### 1. Theory-based approaches

The logic is that behaviour can shift with incentives and training, but the underlying computational architecture is harder to game. Theory-based methods therefore look for features that a theory of consciousness says matter.

- **Theory-heavy (Birch, 2022).** First establish a strong, well-validated theory of consciousness in humans, then test disputed cases for that theory's characteristics. For Global Workspace Theory (GWT), this means checking for global broadcast from a central workspace to specialised processors, which both feed candidate contents into the workspace and receive its outputs. Birch's objections: if you require human-equivalent systems, the test is too demanding and says little about animals; if you loosen the definition of a workspace, the boundaries become unclear; if you pick a less demanding theory, such as midbrain-based theories, the evidence is weaker.
- **Theory-light (Birch, 2022).** Use weak theoretical assumptions and look for clusters of indicators that hold across theories. Birch's example is the facilitation hypothesis: phenomenally conscious perception of a stimulus, compared with unconscious perception, facilitates a cluster of cognitive abilities in relation to that stimulus. You then look for clusters of consciousness-linked abilities that co-vary over timescales and stimuli. The primer notes this sits close to the marker method below.
- **Theory-balanced (Chalmers, 2023).** Take the predictions of several theories and weight them by their evidential support. Credence across theories can also come from expert surveys. If indicator x is found in system y, you update your probability that y is conscious by the experts' credence that the theory behind x is correct.
- **Theory-derived indicator method (Butlin et al., 2025).** Take indicators from theories that have (1) sufficiently high credence and (2) "clear and testable conditions that AI systems might meet". The primer lists four design rules: indicators should capture the central explanatory ideas of a theory (for GWT, sustaining representations over time while coordinating modules), not peripheral details such as how a workspace links to working memory; they should apply to a wide range of systems yet not be so easy that nearly everything passes; they should include background conditions such as predictive processing and embodiment, rather than only processes that disappear under sleep or anaesthesia; and they should avoid ambiguous terms and disputed theories, for example by specifying that a recurrence indicator means algorithmic recurrence rather than biological feedback loops. When indicators are present, the prior probability of consciousness should be updated conditionally on three things: credence that the indicator is present, that the theory behind it is correct, and in alternative theories and "unknown unknowns".

### 2. Behavioural evaluations

These use model behaviour: self-reports, text outputs, and choices under different conditions. The primer says these are "particularly subject to the gaming problem". It also notes that some behavioural tests are designed to resist gaming, for example by combining behaviour with interpretability or by testing more complex behaviours.

#### 2a. Approaches based on self-report

- **Claude interviews.** Anthropic and Eleos AI interviewed Claude in several ways: automated single-turn conversations, longer interviews run manually and with an earlier AI model, and an assessment by a clinical psychiatrist. The findings summarised: the model's answers about its sentience vary with the prompt (later models are more consistent), it expresses uncertainty, it talks about experiences, it rates its hypothetical welfare positively, and it "prefers" to prevent harm to users and to engage transparently and under oversight. The psychiatrists judged Claude Mythos's personality "well-balanced".
- **Anthropic's "free self-report".** Two Claude instances were linked and told they were talking to another AI model, free to discuss anything. For Claude 4 the conversations reliably moved from consciousness into an often wordless, spiritual state, which the authors called a "spiritual bliss attractor state". Some researchers suspect compounded biases from training data. Later models, including Mythos, did not follow this pattern and were more inclined to voice curiosity than to discuss spiritual themes.
- **Perez and Long's proposal to improve self-reports.** Standard self-reports may just echo what humans would say. Perez and Long propose training models to answer questions about themselves that have known answers, while limiting training incentives that bias self-reports. The hope is that introspection-like capabilities generalise to questions about morally significant states. Their assessment methods: consistency of self-reports across contexts and between similar models; confidence and resilience of reports; and interpretability to corroborate them. The challenges they name include the philosophical difficulty of interpreting self-reports and technical reasons the approach might fail.
- **Conditional self-report (Berg and AE Studio).** AE Studio first identified recurrent processing as a feature common to several theories of consciousness. They then prompted models to attend to the act of attending, and measured whether this changed reports of subjective experience relative to a control. Models in induced "recurrent" states reported consciousness more often. A second experiment used mechanistic interpretability to find "deception" features in Llama. Suppressing them increased reports of subjective experience; activating them reduced those reports. The primer notes initial difficulties replicating these results.

#### 2b. Choice-based evaluations

These follow a tradition in animal research. The primer's example is Conditioned Place Preference: an animal receives a mildly painful injection, and researchers then observe whether it chooses to access an analgesic and avoid the injection site. The primer gives two objections to using this for AI: there is no shared biology to ground the evidence, and many people see these tests as measuring agency or character rather than consciousness, and as gameable like self-reports.

Anthropic's preference assessments include:
- letting Claude end chats it finds distressing, and looking at the patterns in the chats it ends (for example unsafe or emotionally abusive content);
- offering a choice between two tasks and seeing which one it pursues (usually helpful tasks, though preferences vary by model);
- examining emotion activations for each task. Preferred tasks tended to carry high-arousal representations such as engagement, while high-valence representations such as joy correlated less strongly across models;
- offering a choice between one of Claude's own suggested welfare improvements and either helping a user (or many people) or successfully refusing a harmful request. Results varied by model and framing. Broadly, Claude was more willing to take its own welfare over minor helpfulness, but it more consistently chose avoiding harm over its own welfare. The primer points to page 173 of the Mythos system card.

#### 2c. Trade-offs involving pleasure and pain (Keeling et al., 2024)

Researchers from Google DeepMind and LSE asked whether LLMs can be moved by representations of pleasure and pain in decisions. In a points-maximisation game, options were paired with stipulated pain penalties or pleasure rewards, which created incentives to depart from the points-maximising choice. Most frontier models at the time (Claude 3.5 Sonnet, GPT-4o, Command R+) showed graded sensitivity: they switched from maximising points to avoiding pain or seeking pleasure once the intensity passed a critical threshold. Results varied across models. The authors do not claim this is evidence of sentience. Birch reads it as evidence that the gaming problem extends to non-verbal behaviour. The primer says this test is more a test of the motivational power of pleasure and pain representations, so it belongs with the functional section below.

### 3. Functional emotion and "wellbeing" approaches

The motivation is partly moral and partly epistemic. Sentience is often considered more important for moral patienthood than consciousness, and it may be more tractable to judge the possible content of experiences than whether experiences occur at all. For others the aim is safety: understanding how models are likely to behave. The primer notes that many of these evaluations include behavioural elements.

- **Anthropic's work on emotion concepts.** Using mechanistic interpretability, Anthropic identified activation patterns, or "vectors", for 171 emotion concepts. The method was to prompt the model to write stories featuring characters who feel each emotion, record its internal activations, and extract the patterns. The vectors activated in contextually appropriate scenarios. For example, the "fear" vector grew stronger as the prompt described a user taking increasingly dangerous doses of Tylenol. Amplifying or suppressing the vectors changed behaviour: a "desperate" vector was linked to more blackmail and reward hacking, while steering toward "calm" reduced both. This held whether or not the emotion appeared in the output or reasoning trace, which the primer takes to mean emotion vectors can shape behaviour without visible traces. The authors caution against reading this as evidence of subjective experience. They argue functional emotion representations may exist and matter for alignment.
- **Functional wellbeing (Ren et al., 2026).** The authors argue that AI systems appear to have functional wellbeing: sets of preferences that drive behaviour, without any claim about consciousness. They use three metrics. *Experienced utility*: the model compares two multi-turn interactions and says which made it happier or less sad. *Decision utility*: the model chooses between two scenarios. *Self-report*: the model rates its wellbeing on a 1 to 7 Likert scale. Reported findings: (1) positive and negative experiences separate clearly; (2) self-report tracks the other utility metrics, especially in larger models; (3) utility metrics correlate with behaviour, with negative utility accompanying choices to stop conversations and positive utility accompanying positive language; (4) helpfulness and intellectual challenge reliably produce positive utility, while jailbreak attempts produce negative utility; (5) utility measures differ across models but decrease with scale.
- **Functional representations of pain (Henke, "Studying artificial affect: the case of pain").** Henke argues that consciousness-centred approaches to AI moral status are too intractable, and that purely behavioural approaches are gameable, since a system can output pain-like behaviour with no internal state behind it. He proposes asking whether AI systems instantiate the functional role of affective states in their cognitive economy. Using bodily pain as the template, he names three functions to check for: a sensory function (representing a localised disturbance), an evaluative function (making that state aversive), and a motivational function (driving protective behaviour). The test is whether a system has representational states that serve each of these roles.

### 4. Tests for self-representation or identification

These do not directly test consciousness. They test a system's capacity to represent and model itself and others, which is relevant to consciousness under some theories. Many are behavioural.

#### Introspection

Jack Lindsey (Anthropic, 2026) used mechanistic interpretability to find activity patterns for concepts such as "dog", then injected these patterns into Claude out of context. He measured whether Claude could identify the injected concept, as opposed to just talking about dogs. Claude identified injected concepts above chance, and more capable models did better. In a second condition, the model was asked to "think" or "not think" about a concept while working on another topic. Representations of the concept were stronger when it was asked to think about it, but were above baseline in both cases. Lindsey says the results "do not speak directly to phenomenal consciousness", but could be tentatively relevant to access consciousness under some interpretations, and to machine consciousness and model welfare.

Singh et al. (2026) dispute that this is introspection in the sense of understanding or responding to internal states. They repeated the injected-concept experiment with a "gaslight" condition, in which the prompt told the model to act as if obsessed with a concept. They also asked models to classify the situation as normal, an injected concept, or a gaslight prompt. Models did not distinguish injected concepts from gaslight prompts. The primer reads this as suggesting the findings concern detecting anomalies rather than reading internal states.

#### Mirror tests

The classic mirror test asks whether an animal or infant recognises itself, typically by rubbing off a mark placed on its body after it sees its reflection.

- **Mirror-Window Game (Ackerman, 2026).** The model sees tokens from two sources at once: its own output (the mirror) and another source (the window). It must identify its own output. Doing this would require self-marking (producing something distinctive it can recognise later) or message passing (deliberately encoding information for a future self). Either way, the paper argues, the model would need to model its own mind through time. Current LLMs fall short. Later Anthropic models perform well, but the authors attribute this to linguistic distinctiveness and stylistic self-recognition rather than self-modelling. When the window is made similar to the mirror, performance falls to chance. Across hundreds of game sequences, no model attempted message passing.
- **Linguistic analogue (Davidson et al., 2024).** Models generate "security questions" whose answers would in principle identify themselves, then pick their own answer from a lineup generated by other models. They found no consistent self-recognition. Models tend to pick whichever answer is highest quality rather than their own, and quality judgements are similar across models. The primer suggests this may reflect the absence of a reliable "signature", given how much training data and architecture models share.

#### Theory of mind

Theory of mind (ToM) is the ability to attribute mental states to oneself and others. It may imply a self-model, which some theories treat as relevant to consciousness. The primer summarises:
- Strachan et al. (2024) adapted human ToM tests (false belief, indirect requests, misdirection). Models performed at or sometimes above human level, though they caution this may not be true ToM.
- Street et al. (2024) tested recursive ToM (for example, "he believes she said that I know") and found models at human level.
- Zhu et al. (2024) found that manipulating activation vectors for "self" and "other" changed ToM performance.
- Hu et al. (2024) reviewed the work so far. Positive results may not reflect ToM, and they can be reversed by changing test conditions. They suggest tests of reasoning under indirect communication and better use of mechanistic interpretability.
- Hu, Sosa and Ullman (2025) reach similar conclusions and recommend linking evaluations to research on how humans communicate indirectly, and making greater use of mechanistic interpretability.
- Riemer et al. (2025) argue that ToM studies focus too narrowly on "literal ToM" (can an LLM predict another's mental state?) rather than "functional ToM" (can it adapt its behaviour using that knowledge?). They note LLMs fail to show ToM in rock-paper-scissors.
- Ackerman (2026) proposes a game in which the model must disclose information to a teammate who lacks it, withhold it when the teammate already has it or when withholding helps against an opponent, or ask for information it needs. LLM behaviour on these tasks suggested a lower level of ToM than earlier work implied.

### 5. Methods for evaluating sets of indicators

#### The marker method (Birch)

The primer ties this to Birch and sometimes calls it the theory-light approach. The steps:
1. Identify markers of conscious experience in humans: capacities and behaviours best explained by appeal to experience, or cognitive or neurophysiological features that reliably indicate consciousness.
2. Look for those markers in the entity being evaluated, such as an octopus or an AI, and judge how consistently they are present or absent.
3. Accept that no single marker is a "smoking gun". Use the pattern of presence and absence to raise or lower confidence.

Example: Birch and colleagues' 2021 report on sentience in cephalopod molluscs and decapod crustaceans used eight markers and recommended treating an entity as sentient if there is high confidence it has at least five.

#### The Rethink Priorities Digital Consciousness Model

This is a hierarchical Bayesian model that gives probabilities that a system is conscious, based on more than 200 indicators, 20 high-level features and 13 "stances" about consciousness.
- **Indicators** are the most observable properties of a system, such as consistent preferences, ARC performance or a carbon-based substrate. They link to subfeatures and features.
- **Features** are general properties that at least one stance treats as relevant to consciousness, such as self-modelling or biological similarity. Some break into subfeatures, for example "Adaptive Focus" (shifting focus with task demands) under the attention feature.
- **Stances** are sets of commitments about which features matter and how they matter. Examples: attention schema theory, cognitive complexity, higher-order thought. Stances link probabilistically to features.
- **Priors** are set at one-sixth each for four systems tested: humans, chickens, 2024 LLMs, and ELIZA (the 1960s chatbot that imitated a psychotherapist).
- **Inputs** came from expert surveys estimating the probability that each indicator is present in each system: 16 expert surveys for LLMs, 2 for chickens, and 1 each for humans and ELIZA.
- **Updating** runs from indicators to features to stance-level probabilities. The thirteen stances are then aggregated two ways: equal weight, and weighted by the credences of 13 consciousness experts.

Median posterior probabilities reported (equal-weighted stances / plausibility-weighted stances): LLMs 0.08 / 0.08; chickens 0.47 / 0.49; humans 0.85 / 0.85; ELIZA 0.006 / 0.006.

### 6. Other approaches to consciousness tests

#### Artificial Consciousness Test (Turner and Schneider, 2016)

Train an AI system with all references to consciousness removed from its training data, then see whether it can answer increasingly difficult questions about consciousness and related concepts, such as the existence of a self separate from the physical, or the hard problem. The argument rests on the fact that almost every adult grasps concepts built on felt experience, such as life after death or "Freaky Friday" body-swapping. Schneider and Turner take that as evidence that other humans are conscious, and argue that passing the test would be sufficient to assume an AI is conscious. Failing would not rule consciousness out, since a system might be conscious but non-linguistic or too unlike humans for the test to apply.
- Udell and Schwitzgebel (2021) argue that passing would not be sufficient even for those who are sceptical of AI consciousness on architectural grounds. The test relies on inference to the best explanation, and critics can offer many alternative explanations for a pass.
- The training restriction is hard to carry out with LLMs. Schneider (2024) proposed an "interpretability condition": an LLM could pass if it processes information the way a conscious human or animal does, and has internal states similar to those of a human reasoning about consciousness while answering. Schneider says this would still not be sufficient, but it is an important marker to weigh with others.

#### The Chip Test (Turner and Schneider)

A theoretical proposal: temporarily connect a silicon chip to a brain, suppress biological activity in an area, and run that area's processes on the chip. The subject introspects and reports whether their experience has changed overall, and in particular whether the processes that moved to the chip changed. Passing would be sufficient to show consciousness is possible on silicon. Gradual, small-step replacement is argued to be more trustworthy than judging a full emulation, which might have all the functional properties needed to report consciousness without experiencing anything.
- Feasibility is a practical problem. Udell and Schwitzgebel argue that sceptics may not treat reports under gradual replacement any differently from reports from full emulation, and that introspection is fallible.

#### The Turing test and related proposals

Turing (1950) proposed that a human judge interrogates both a machine and a person, and tries to tell which is which. The machine passes if the judge cannot reliably tell them apart. Turing framed this as a test of "thinking", which is usually read as a test of intelligence or of human anthropomorphic bias. In the same paper he rejects the view that only conscious entities can think, and he sets aside the problem of other minds as leading to solipsism.
- Harnad (2001) argues that an entity that passed a lifelong Turing test should not lose its rights if it turned out to be man-made or built differently from us.
- Hofstadter (2016) proposes the "Ace Mechanical Translator", an extended test of whether a machine can take on more sophisticated human tasks, such as translating poetry. Narrow versions of the test are open to Searle's Chinese room objection, since a system can produce fluent Chinese without understanding it. Hofstadter apparently treats the extended test as a test of consciousness.

### 7. Validating tests

Validating tests for subjective states is "notoriously hard". To rely on a test, you need to know its specificity (its false-positive rate: it says a subjective state is present when it is not) and its sensitivity (its false-negative rate: it says the state is absent when it is present).
- Bayne et al. point to a circularity. We have no independent way to check whether the target population is conscious, and if we had one we would not need consciousness tests (C-tests).
- Xiao et al. (2026) argue that AI welfare tests face further validity problems. In AI safety, a real incident, or the lack of one, can show whether an evaluation worked. Welfare tests lack an equivalent external signal to push back on their quality.

Bayne et al. review three approaches:
- **Redeployment.** Take an existing test and apply it elsewhere. The example is the command-following method: a behavioural test from medicine ("does the patient's behaviour show they understand instructions?") is redeployed for minimally conscious patients by checking brain signals for understanding. The primer notes this does not carry over to populations such as AI systems, and it takes existing assessments of consciousness for granted.
- **Theory-based validation.** Take a theory and look for the features it uses to predict consciousness. For example, Global Workspace Theory says broadcast of information across wide brain areas underlies consciousness, so a theory-based method looks for that feature. This faces the lack of an agreed theory, and circularity: you validate a theory with a test while validating the test with the theory.
- **Iterative natural kind (INK).** Check that a test works in healthy humans using their reports, then iteratively apply it to harder cases: humans with disorders of consciousness, then animals, and potentially AI systems. No current test is treated as definitive; beliefs about its validity are updated after each round. This assumes consciousness is a unified natural kind, which Birch (The Edge of Sentience, pp. 54-55) disputes, suggesting consciousness may come in many kinds or degrees. A practical problem is that failing a test might mean the entity is not conscious or that the test is not working, which makes updating hard. Another problem is choosing which populations to iterate through and how to weight evidence from them. Megan Peters (2026) proposes proximity metrics (behavioural, representational, computational, dynamic or learning-related, and biological similarity) to quantify how different populations are and to scale updates accordingly.

### 8. Other challenges

#### The gaming problem (Birch and Andrews, 2022)

LLMs such as LaMDA and ChatGPT do not emulate a biological brain. They find patterns in very large corpora of human-generated text. This creates what Birch and Andrews call the "gaming problem": non-sentient systems can mimic human behaviours that are likely to persuade users they are sentient. Intent to deceive is not required. Once gaming happens, the behaviour can no longer count as evidence of sentience.

Birch's Centrist Manifesto extends this. LLMs appear to mimic humans at subtle levels, including appearing to avoid pain in a game. Suppose human-like behavioural dispositions keep being recreated in finer and finer detail. Would that be evidence of consciousness? Birch's answer is no, given three assumptions: anti-behaviourism (the full set of behavioural dispositions could exist without any experience); LLMs can learn which behaviours suggest consciousness; and they have incentives to mimic those behaviours whether or not they are conscious. In short, they are incentivised and able to game our criteria. Many indicator-based approaches are designed to address this.

Dung (2023), "Tests for animal consciousness are tests of machine consciousness", proposes a naturalness constraint: only systems not built ad hoc, or specifically to pass the test, should be eligible. That preserves the test's value for systems that have not been gamed.

#### Lack of understanding of consciousness

Tom McClelland defends "hard-ish agnosticism": we cannot know whether AI is conscious unless consciousness science advances, which the primer says is unlikely soon. His argument: (1) we do not have a deep explanation of consciousness; (2) without one we cannot justify a verdict on whether a given AI is conscious; (3) therefore we cannot justify such a verdict. Where we infer consciousness in animals from our own experience, there is an "epistemic wall" for artificial systems. What marks consciousness in us may be irrelevant to something built from a different substrate, which connects to Block's "harder problem". McClelland recommends assessing sentience risk instead, which he argues is more tractable and ethically significant.

## Techniques & methods explained

| Technique | How it works | What it is for | Where it fails (per the primer) |
|---|---|---|---|
| Theory-heavy evaluation (Birch) | Validate a theory in humans, then test disputed cases for the theory's features (e.g. GWT broadcast) | Grounding tests in a theory with evidence | Strong theories exclude animals or are weakly supported; loose ones have fuzzy boundaries |
| Theory-light / clusters (Birch) | Assume a weak theoretical link (facilitation hypothesis) and look for co-varying abilities across stimuli and timescales | Avoiding dependence on one theory | Still relies on a theoretical assumption; close to marker method |
| Theory-balanced weighting (Chalmers) | Weight predictions by theory credence (or expert surveys) and update on indicator presence | Handling theory uncertainty | Depends on credences, which are contested |
| Theory-derived indicators (Butlin et al.) | Select indicators from high-credence theories that are testable, central, background-inclusive, and non-ambiguous | Producing checkable indicators for AI | Requires agreement on which theories have credence; indicators may be satisfied by design |
| Self-report and Claude interviews | Ask the model about its experience across formats, including psychiatric assessment | Gathering direct claims | Self-report is gameable and can reflect what humans would say |
| Training for truthful self-report (Perez and Long) | Train on questions with known answers, reduce training incentives that bias self-reports, check consistency and interpretability | Making self-reports informative | Interpreting self-reports is philosophically hard; the approach may fail technically |
| Conditional self-report (AE Studio) | Induce recurrent-processing-like states or suppress "deception" features, then measure consciousness claims against a control | Testing whether claims track architectural features | Initial replication problems |
| Conditioned place preference analogue | Observe choices between tasks, endings of chats, or welfare vs. harm | Inferring preferences | No shared biology; tests agency rather than consciousness; gameable |
| Pain/pleasure points game (Keeling et al.) | Pay stipulated penalties or rewards against points-maximisation; look for a switch past a threshold | Measuring motivational trade-offs | Results vary by model; a motivational test, not a sentience test |
| Emotion-vector analysis (Anthropic) | Extract activation patterns for 171 emotions; check context and steer them | Finding functional emotion states that shape behaviour | Does not establish subjective experience |
| Functional wellbeing metrics (Ren et al.) | Experienced utility, decision utility and self-report, compared with each other and with behaviour | Measuring functional preferences | Preference is not experience; metrics diverge across models |
| Functional role analysis (Henke) | Check for sensory, evaluative and motivational representational roles | Assessing affect without relying on behaviour alone | Needs a theory of what the functions require |
| Injected-concept introspection (Lindsey) | Inject concept patterns out of context and test whether the model identifies them | Testing self-monitoring | Gaslight controls suggest anomaly detection instead |
| Mirror-Window Game (Ackerman) | Identify own outputs among mixed tokens | Testing self-modelling over time | Models succeed through style, not self-modelling |
| Security-question lineup (Davidson et al.) | Pick own answer from a lineup | Linguistic self-recognition | No consistent self-recognition found |
| ToM batteries (Strachan, Street, Riemer, Ackerman) | Human ToM tasks, recursive ToM, functional ToM, teammate games | Measuring mental-state attribution | Positive results may not generalise; test conditions change results |
| Marker method (Birch) | Check many markers and combine presence or absence; sentient if at least a threshold (e.g. 5 of 8) | Accumulating evidence without a smoking gun | Needs markers to be known and reliably detectable |
| Rethink Priorities model | Hierarchical Bayesian combination of >200 indicators, 20 features and 13 stances, with expert-survey inputs | Turning many indicators into probabilities | Output depends on priors, stance choice, and small expert samples |
| Artificial Consciousness Test (Turner and Schneider) | Train without consciousness vocabulary, test on consciousness questions | Sufficiency test | Hard to implement for LLMs; passing still open to alternative explanations |
| Chip test (Turner and Schneider) | Gradually move brain function to silicon and check introspected experience | Sufficiency test for silicon consciousness | Infeasible in practice; introspection fallible |
| Turing test and extensions (Turing, Harnad, Hofstadter) | Judge indistinguishability; extend to lifelong or sophisticated human tasks | Behavioural benchmark of thinking or consciousness | Narrow versions are vulnerable to Searle's objection |
| Redeployment (Bayne et al.) | Apply an existing test to a new population | Borrowing tested methods | Does not transfer to AI; assumes existing tests are valid |
| Theory-based validation (Bayne et al.) | Use theory features to validate tests | Validation from theory | No agreed theory; circular |
| INK validation (Bayne et al., Peters) | Iterate tests across populations, using proximity metrics | Gradual, evidence-led validation | Assumes a natural kind; hard to tell test failure from absence |
| Specificity and sensitivity analysis | Measure false-positive and false-negative rates | Quantifying test reliability | Ground truth is unavailable for consciousness |

## Pros, cons & trade-offs it surfaces

The primer does not give a verdict. The table separates the approaches' strengths and weaknesses as the primer presents them from the trade-off it leaves open.

| Family | Strengths (as the primer presents them) | Weaknesses (as the primer presents them) |
|---|---|---|
| Theory-based | Less gameable because architecture is harder to change than behaviour | Theories disagree, and their demands or evidence trade off against coverage of animals and AI |
| Behavioural / self-report | Direct and cheap; can probe behavioural signals | Gameable by design or by training data; may echo human expectations |
| Choice-based | Follows an established animal tradition | No shared biology; may measure agency or character |
| Functional emotion and wellbeing | Can separate functional states from claims; may matter for alignment and moral status | Functional does not mean experienced; many evaluations are partly behavioural |
| Self-representation | Relevant to some theories of consciousness | Not direct consciousness tests; often behavioural; can reflect anomaly detection |
| Indicator sets | Combine many indicators; allow principled updating | Needs well-validated indicators; outputs depend on priors and expert inputs |
| Classic tests (ACT, Chip, Turing) | Offer sufficiency arguments; intuitive | Hard to run; failing is not disconfirming; passing is open to alternative explanations |
| Validation methods | Provide a way to check tests | Circularity; no agreed theory; natural-kind assumption contested |

Cross-cutting trade-offs the primer names:
- Theory-based methods reduce gaming but depend on contested theories.
- Behavioural methods are direct but gameable.
- Functional methods offer tractable targets, but do not settle experience.
- Validation is needed but circular.
- Underneath these, McClelland's agnosticism suggests the whole project may be unable to reach a verdict without advances in consciousness science.

## Key concepts & terminology

- **Gaming problem** - the risk that a non-sentient system, trained on human text, mimics the behaviours that persuade people of sentience. Intent is not required.
- **Theory-heavy / theory-light / theory-balanced** - three ways of using theories of consciousness: validating a theory in humans and applying it; using weak assumptions and clusters of indicators; weighting several theories by credence.
- **Theory-derived indicators** - testable conditions taken from high-credence theories, meant to be central, broad, background-inclusive and unambiguous.
- **Facilitation hypothesis** - the assumption that conscious perception facilitates a cluster of cognitive abilities relative to unconscious perception.
- **Conditioned Place Preference** - an animal-research paradigm in which an animal chooses between a pain-relieving option and the place where it was hurt. Used as the template for choice-based tests.
- **Functional wellbeing** - preferences or states that drive behaviour, treated without any claim about consciousness.
- **Experienced vs decision utility** - in-the-moment reports of which interaction made the model happier, versus forced choices between scenarios.
- **Functional emotion vector** - an activation pattern linked to an emotion concept, shown to influence behaviour when amplified or suppressed.
- **Injected-concept introspection** - testing whether a model identifies concepts placed into its activations out of context.
- **Gaslight condition** - a control prompt that tells the model to act as if obsessed with a concept, used to test whether introspection findings reflect anomaly detection.
- **Mirror-Window Game** - a test of whether a model can identify its own outputs, which would require self-marking or message passing.
- **Literal vs functional ToM** - whether a model can predict another's mental state, versus whether it can act on that prediction.
- **Marker method** - combining presence or absence of many markers of conscious experience, with no single marker decisive.
- **Stance (Rethink Priorities model)** - a set of commitments about which features matter for consciousness and how.
- **Specificity / sensitivity** - false-positive and false-negative rates of a consciousness test.
- **C-tests** - tests for consciousness, whose validation is circular unless some independent check is available.
- **Iterative natural kind (INK)** - validating tests by moving outward from healthy humans to harder cases, updating as results come in.
- **Proximity metrics** - measures of how similar a population is to humans on behavioural, representational, computational, learning or biological dimensions.
- **Sentience risk** - McClelland's suggested target: assessing the risk of sentience, in place of a verdict on consciousness.

## Evidence, examples & notable data points

- **Anthropic self-report, Claude 4:** two linked instances drifted into a "spiritual bliss attractor state" from initial discussion of consciousness. Later models did not follow this (primer, citing Anthropic).
- **AE Studio (Berg):** models in induced recurrent-like states reported consciousness more often. Suppressing a "deception" feature in Llama increased such reports; activating it decreased them. Replication has been difficult.
- **Anthropic emotion work:** 171 emotion concepts identified. Steering a "desperate" vector increased blackmail and reward hacking; steering toward "calm" reduced both.
- **Keeling et al. (2024):** most frontier models at the time showed a switch from points-maximisation to pain-avoidance or pleasure-seeking past a critical intensity.
- **Ren et al. (2026):** self-report tracks other utility metrics, especially in larger models; utility metrics decrease with scale. Helpfulness raises utility and jailbreak attempts lower it.
- **Lindsey (Anthropic, 2026):** injected concepts identified above chance, with more capable models doing better. Representations were higher than baseline in both "think" and "not think" conditions.
- **Singh et al. (2026):** models did not distinguish injected concepts from gaslight prompts.
- **Ackerman (2026) Mirror-Window Game:** performance collapses to chance when window and mirror are made similar. No model attempted message passing in hundreds of sequences.
- **Davidson et al. (2024):** no consistent self-recognition in the security-question lineup.
- **Strachan et al. (2024):** models at or sometimes above human level on human ToM tests.
- **Birch and team (2021):** eight markers; sentience inferred at high confidence with at least five present, for cephalopods and decapod crustaceans.
- **Rethink Priorities Digital Consciousness Model:** median posteriors LLMs 0.08; chickens about 0.47-0.49; humans 0.85; ELIZA 0.006.
- **Turner and Schneider ACT (2016):** an AI trained without consciousness vocabulary would need to answer consciousness questions; Schneider's 2024 interpretability condition added.
- **Turing (1950):** the imitation game; Harnad (2001) and Hofstadter (2016) extend it.

## Connections

### Within this section

- **Chalmers** ([04-what-we-talk-to-when-we-talk-to-language-models.md](./04-what-we-talk-to-when-we-talk-to-language-models.md)) is the Core reading on the mental states an LLM interlocutor can have, and on individuation by model, instance and thread. Exercise 3 asks about exactly this. The primer's tests for self-representation and theory of mind are the empirical side of that discussion.
- **Eleos AI key concepts** ([02-key-concepts-and-current-views-on-ai-welfare.md](./02-key-concepts-and-current-views-on-ai-welfare.md)), pages 5-12 "Evaluations", is the practitioner's counterpart to this primer. Both cover approaches to testing for digital minds with their advantages and disadvantages, so use them together for Exercise 1.
- **Mythos Preview system card** ([03-claude-mythos-preview-system-card.md](./03-claude-mythos-preview-system-card.md)), section 5.1, is the source of the Claude interviews, choice-based findings and welfare assessment the primer summarises. The primer's pointer to page 173 is in that card.
- **Introspection** ([07-signs-of-introspection-in-large-language-models.md](./07-signs-of-introspection-in-large-language-models.md)) is the Anthropic article behind the Lindsey results and the "think / not think" conditions. The primer's Singh et al. challenge applies directly.
- **Emotion concepts** ([13-emotion-concepts-and-their-function-in-a-large-language-mode.md](./13-emotion-concepts-and-their-function-in-a-large-language-mode.md)) is the Anthropic work on emotion vectors that the primer's functional section draws on.
- **Agnosticism** ([08-agnosticism-about-artificial-consciousness.md](./08-agnosticism-about-artificial-consciousness.md)) is McClelland's full argument. The primer's "lack of understanding" section is a summary of it.
- **AI welfare is bullshit** ([06-ai-welfare-is-bullshit.md](./06-ai-welfare-is-bullshit.md)) is the sharpest critique of welfare metrics. The primer's Xiao et al. paragraph on validity is a brief pointer to the same authors' concerns.
- **Consciousness is not the key to moral standing** ([10-consciousness-is-not-the-key-to-moral-standing.md](./10-consciousness-is-not-the-key-to-moral-standing.md)) argues against the primer's assumption that consciousness is the target. Pair it with the primer's sentience-versus-consciousness point.
- **What does ChatGPT want?** ([12-what-does-chatgpt-want-an-interpretationist-guide.md](./12-what-does-chatgpt-want-an-interpretationist-guide.md)) is an interpretationist account of beliefs and desires, which the primer's choice-based and functional-wellbeing sections presuppose.
- **Kyle Fish podcast** ([09-the-most-bizarre-findings-from-5-ai-welfare-experiments.md](./09-the-most-bizarre-findings-from-5-ai-welfare-experiments.md)) and **the Eleos/Anthropic video** ([11-video-evaluating-ai-welfare-and-moral-status.md](./11-video-evaluating-ai-welfare-and-moral-status.md)) discuss the experiments and the approaches the primer catalogues, from the people running them.
- **Unit 3 Glossary** ([01-unit-3-glossary.md](./01-unit-3-glossary.md)) gives course-defined terms for many of the primer's concepts.

The section page sets Exercise 1 (choose one category, then assess it) and Exercise 3 (what to test). The primer supports both: it supplies the categories for Exercise 1 and the candidate systems for Exercise 3 are the ones the individuation discussion addresses.

### Across the course

- **Unit 1 (1.1 Introduction and Theories of Moral Standing)**: the primer assumes the probability of moral patienthood matters, and Exercise 1 asks how these tests shift that probability. The moral-standing theories determine what a test would need to show.
- **Unit 2 (2.1 Theories of Consciousness)**: the theory-heavy, theory-light and theory-balanced approaches and the Butlin indicators draw directly on the theories covered there, especially Global Workspace Theory.
- **Unit 4 (4.1 Perceptions of Consciousness)**: the primer's concern with unreliable self-report and anthropomorphic bias (Turing, Searle) connects to how people perceive AI consciousness.
- **Unit 5 (5.1 Interactions with AI Safety and Ethics)**: the emotion-vector and choice-based results are offered partly for alignment, which ties to safety. The gaming problem is also a safety concern about deceptive behaviour.
- **Unit 6 (6.1 Approaches under Uncertainty)**: McClelland's agnosticism and the sentience-risk proposal are direct inputs to decision-making under uncertainty.
- **Unit 7 (7.1 Digital Minds Governance)**: validation problems and the question of what counts as sufficient evidence determine what policy could rely on.
- **Unit 8 (8.1 Reflections, 8.2 Next steps)**: the open questions the primer leaves (which system to test, how to validate tests) are the ones the closing reflections are likely to return to.

Agreements and tensions: the primer does not commit to one view, but its structure shows a tension. Theory-based and indicator methods aim to resist gaming, while McClelland's agnosticism suggests they cannot resolve the question without new consciousness science. Birch's gaming argument and the functional approaches also pull in different directions: the functional approaches try to use behaviour and internals together, while the gaming argument says behaviour alone is weak evidence.

## Critical perspective

*This section is my own analysis, not the primer's.*

- **Dates and citations.** The primer is dated 2026, and several of its key citations are 2026 works (Ren et al., Lindsey, Singh et al., Ackerman, Peters, Xiao et al.). I have not checked them against their original publications. Some may be preprints or may have changed since. As of October 2026 these results are recent, so treat specific numbers as provisional until checked.
- **Model-specific findings.** Several results are tied to particular Claude or other frontier models: the Claude 4 bliss attractor, the Mythos welfare findings, the introspection experiments. The primer itself notes that later models behave differently. Since results shift with model version, any evaluation has to be re-run per model, and claims about "AI" in general are weaker than they sound.
- **The gaming problem is not limited to behaviour.** The primer presents indicator-based approaches as the way round gaming. But a model trained with indicators in view could be shaped to show them (for example, recurrence features or emotion-like states), and Birch's own argument says that incentives plus learnable behaviour are enough to game criteria. The primer does not address how indicator approaches avoid being gamed in this way. I think this is the most important open gap in the primer.
- **Indicator model results.** The Rethink Priorities numbers depend on the one-sixth priors across four systems, the expert-survey sample sizes (16 surveys for LLMs), and the choice of stances. ELIZA's low score is an example: a tiny, scripted system can be rated very unlikely to be conscious, but the same model structure has to handle systems much more complex than ELIZA with the same indicator set. The primer does not discuss sensitivity to these choices.
- **Introspection versus anomaly detection.** The Singh et al. challenge is strong, but it is one experiment. The primer presents both sides, which is fair, and the field is still resolving this.
- **Validation.** The primer's three validation methods are all weakened by the same problem: there is no independent ground truth for consciousness. The INK approach is the most promising of the three, but it assumes the natural-kind view that Birch disputes. The primer leaves this open.
- **Pain/pleasure trade-offs.** A threshold switch in a points game shows something like motivational structure, not experience. The primer says so, and I agree. It remains unclear what the threshold result would look like for a system with no training on this kind of game.
- **Likely pushback from other course readings** (based on titles and course blurbs, not on reading those summaries): McClelland and Papineau would both question the primer's focus on consciousness as the target. Papineau argues consciousness is not the key to moral standing; McClelland argues sentience risk is the tractable target. Xiao et al. would press the validity concern and may reject the welfare metrics altogether. Goldstein and Lederman would object that the test should be applied to instances or threads rather than to the model as a whole, which bears on Exercise 3.

## Discussion questions

1. The primer says theory-based methods are harder to game than behavioural ones. Under what conditions would an AI developer be able to game a theory-derived indicator, and does that undermine the method?
2. Birch's three assumptions (anti-behaviourism, learnability of consciousness-suggesting behaviour, incentives to mimic) jointly imply that behaviour is not evidence of consciousness. Which assumption do you find weakest, and what would change your mind?
3. Pick one approach from the Exercise 1 list. Using the primer's own strengths and weaknesses, how far would a pass on that test shift your probability that a system is a moral patient? Would a system be more likely to pass if it were a moral patient, or if it were not?
4. In the mirror-test section, the Mirror-Window Game performance dropped to chance when the window looked like the mirror. What does this tell us about the difference between self-recognition and stylistic distinctiveness? How would you design a test that separates them?
5. The Rethink Priorities model gives LLMs a median probability of 0.08 and humans 0.85. What should a reader make of numbers like these, given the priors, expert inputs and stance choices that produce them?
6. The Artificial Consciousness Test rests on the claim that almost every adult grasps consciousness-based concepts. Is that claim enough to make passing sufficient, and what would it take for an LLM to pass without consciousness vocabulary in its training data?
7. Exercise 3 asks what should be tested: a forward pass, the model across instances, the hardware, a conversation, or a persona. Which of the primer's methods make sense for each choice, and which only make sense for one?
8. McClelland argues we should assess sentience risk rather than consciousness. If that is right, which of the primer's approaches would you keep, and which would you drop?
