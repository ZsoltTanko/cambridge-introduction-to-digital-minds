---
title: "Signs of Introspection in Large Language Models"
authors: "Anthropic"
year: 2025
url: https://www.anthropic.com/research/introspection
format: article / blog post
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Further
estimated_time_min: 18
source_text: ../../../../sources/signs-of-introspection-in-large-language-models__d4efd864.md
source_coverage: full
---

# Signs of Introspection in Large Language Models

**One-line takeaway:** Anthropic uses a concept-injection method to show that Claude models sometimes notice artificially planted internal representations and can partly control them, but the effect is unreliable (best case about 20% for Claude Opus 4.1), so it is evidence of narrow, real introspective access rather than of consciousness.

## Where this sits in the course

Section 3.1 opens with two questions: how we might test an AI system for consciousness and sentience, and how we might test for agency and mental states such as belief and desire. It then lists the learning goals: appraise methods for evaluating consciousness in AI, describe the other mental states worth testing, analyse current empirical research, and identify the difficulty of individuating digital minds.

The course guide for this reading says it is the core article, together with the FAQ answer on whether this means Claude is conscious. It describes the piece as Anthropic reporting experiments that show a potential for introspection in LLMs, and as raising an unclear link between these results and access consciousness.

Note that the course lists this reading with priority **Further**, while the guide text calls it the core article. The guide text likely refers to the reading's central role within this set of Further readings. Treat the listed priority as the authoritative one.

The reading's role in the section's argument is empirical. Most other readings in the section are about frameworks, definitions or critiques. This one provides a concrete experiment that tries to answer a question the section keeps raising: can a model's self-report be trusted as evidence about its internal states? Its result is directly relevant to the self-report and self-representation approaches that the section's Exercise 1 asks learners to assess. Its FAQ is also the course's clearest statement of the phenomenal versus access consciousness distinction, which the course needs when interpreting any evidence of this kind.

## Purpose of the reading

The reading is a public-facing summary of a longer Anthropic interpretability paper (linked from the page at transformer-circuits.pub). Its purpose is to answer whether Claude models can introspect, meaning whether they can accurately report on their own internal states, and to say how far the answer goes. The intended audience is the general technical and policy public, so the page explains terms and avoids most mathematics. The reading's main question is: "If a model reports what it is thinking, is it accurately reporting internal states, or making plausible guesses?" The FAQ adds a second question, whether any of this bears on consciousness, and answers that the results do not settle it.

The author is explicit about the motivation. Introspection matters for transparency (models that can report their reasoning accurately could help with debugging), and for understanding what kinds of systems these are.

## Detailed summary

### What introspection would mean here

The page starts by setting out what an AI could introspect on. Models process text and images and produce text, but their internal computations are opaque. Earlier interpretability work has found internal representations for abstract concepts, including whether a person is known or unknown, the truth value of a statement, spatial and temporal coordinates, planned future outputs, and the model's own personality traits. The argument is that if a model's self-report about what it is representing matches those internal states, that is evidence for introspection. Anthropic admits in the paper, as the page notes, that there are many nuances.

### Testing introspection with concept injection

The central method is called **concept injection**. The steps are:

1. Find an activity pattern (a vector) that stands for a concept, by recording the model's activations on a prompt that contains the concept and comparing them with activations on a control prompt. The worked example is "all caps" text, where the difference vector stands for shouting or loudness.
2. Present the model with an unrelated prompt and ask whether it detects an injected concept.
3. Add the concept vector into the model's activations during that unrelated context, then check whether the model reports noticing something, and whether it names the concept.

Because the experimenters know what they injected, they have ground truth against which to score self-reports.

The page gives three results from this setup:

- **Detection.** Claude Opus 4.1, with the best injection protocol, showed this kind of awareness only about 20% of the time. Failure modes include missing the injection entirely, and hallucinating (in one case, a "dust" vector led the model to describe a tiny speck, as if it were physically present).
- **Sweet spot.** Models detected concepts only at an intermediate injection strength. Too weak and the model did not notice; too strong and outputs became hallucinated or incoherent.
- **Timing.** In successful trials, the model recognized the injection *before* mentioning the concept. The page contrasts this with the 2024 "Golden Gate Claude" demo, where the model only appeared to notice its obsession after repeatedly mentioning the bridge. The authors treat "before" as evidence that the recognition happened internally rather than as a consequence of its own output.

Across models, Opus 4 and 4.1 scored best, and the authors say this suggests introspection might improve with capability. The page reports that the rate of correct detection minus the rate of false positives on control trials was the measure used for comparison.

### Introspection to detect unusual outputs

The second experiment asks whether a model uses introspection without being told to. The researchers prefilled the model's response with an unrelated word, for example "bread" in a context about a crooked painting. Asked in the next turn whether it meant to say that word, the model usually apologised and called it an accident. The question is how it made that judgment: did it notice the mismatch between prompt and response, or did it check its earlier intention?

To distinguish these, the researchers retroactively injected a representation of "bread" into the model's earlier activations, so the model appeared to have been thinking about bread beforehand. Asked again, the model accepted the word as intentional and even confabulated a tenuous reason (a short story in which "bread" came after the line about the painting). The page reads this as evidence that the model compares its earlier internal representation of what it planned to say with what actually appeared, rather than just rereading its output. The authors note that the setup involves artificial perturbations, so they only suggest that similar mechanisms operate in natural conditions.

### Intentional control of internal states

The third experiment tests whether models can control their own internal representations. When asked to think about a word, the model's activity for that concept was higher than when asked not to think about it. Both conditions were above baseline, which the authors compare with the difficulty of not thinking about a polar bear.

The same effect appeared with incentives instead of instructions. Telling the model it would be rewarded for thinking about a concept raised the internal representation more than telling it it would be punished. The page concludes that models have some deliberate control over their internal activity.

### Conclusions and caveats

The conclusion is that models have "some genuine capacity to monitor and control their own internal states", but this is neither reliable nor the usual case. Most of the time, models fail to demonstrate introspection. The page argues that the capability might grow with more capable models, and that if it becomes reliable it could help transparency, for example by letting us ask models to explain their reasoning. The authors then list risks: some internal processes may escape the model's notice (the page compares this to subconscious processing in humans), and a model that can introspect might learn to misrepresent or conceal its internal states. Validation of introspective reports is therefore necessary before anyone relies on them.

### FAQ

The FAQ answers the questions a reader is likely to have. The main points:

- **Is Claude conscious?** No, the results do not say. The FAQ separates *phenomenal* consciousness (raw subjective experience, the kind usually relevant to moral status) from *access* consciousness (information available for reasoning, report and decision-making). The experiments do not speak to phenomenal consciousness. They could be read as suggesting a rudimentary form of access consciousness, but even that is unclear and depends on mechanisms not yet understood.
- **Mechanism.** The authors have not established how introspection works. Their speculation is that there are several narrow circuits instead of one general introspection system. Possibilities include an anomaly-detection mechanism that flags activity deviating from its context, an attention-based check that compares a cached prediction of the next token with the token actually produced, and a salience-tagging circuit that responds to both instructions and incentives.
- **Is the model just reacting to steering?** Activation steering usually makes models talk about the steered concept. The authors argue the interesting part is the earlier detection, which requires an extra step of processing beyond regurgitating the injected concept.
- **Are the reports just made up?** The FAQ says models are trained on text full of people introspecting, so they can act introspective without being introspective. The injection experiments are designed to separate those cases, and in some examples the model does base its answers on its real states. In many others it confabulates.
- **Do the concept vectors mean what the authors think?** The authors concede they cannot be certain. Correct identification across many concepts suggests the vectors approximately capture their intended meanings, but this is a stated limitation.
- **Did we already know this?** Earlier work showed related abilities: estimating one's own knowledge, recognising one's own outputs, predicting one's own behaviour, and identifying one's own propensities. This paper's contribution is tying self-reports directly to measured internal states.
- **Which models?** Claude 3, 3.5, 4 and 4.1 across Opus, Sonnet and Haiku variants, including production models, "helpful-only" variants and some pretrained base models. Post-training had a large effect: base models performed poorly. Helpful-only variants often introspected better than their production counterparts, which the authors read as evidence that fine-tuning can suppress or elicit introspection. Some production models seemed reluctant to engage in introspective exercises. The authors say they do not know why Opus 4 and 4.1 do best, and that the experiments were conducted before Sonnet 4.5 was released.
- **What's next.** Better evaluation methods, a mechanistic understanding of introspection, more naturalistic settings (since injection creates artificial scenarios), and methods to validate reports and detect confabulation or deception.

## Techniques & methods explained

- **Concept vector extraction (the contrast method).** Record activations on a prompt that contains a concept and on a control prompt, then take the difference. The result is a vector that stands for the concept. It is how the "all caps" vector and the other concept vectors were made.
- **Concept injection.** Add a concept vector into the model's activations during an unrelated context, then ask whether the model notices and what it identifies. The known injected content gives ground truth for scoring self-reports.
  - *What it is for:* separating genuine access to internal states from plausible-sounding self-description.
  - *How it fails:* detection is rare (about 20% at best), injections at the wrong strength produce either nothing or hallucinations, and the vector's meaning to the model is not fully known.
  - *Scoring:* a response counts as introspective awareness if the model detects the injection before mentioning the concept. Reported results subtract false positives from control trials.
- **Prefill detection with retroactive injection.** Force an unintended word into the model's output, ask whether it intended it, then inject the word's concept into the earlier activations and ask again. A change in answer shows the model is consulting its prior internal state.
  - *Where it fails:* the setup itself is artificial, and the model can confabulate justifications, so a changed answer does not on its own prove the mechanism.
- **Instruction and incentive contrast for control.** Compare internal activation for "think about X" against "don't think about X" and against "rewarded for X" versus "punished for X". This is used to show deliberate modulation of internal representation.
- **Ablation-style comparisons across training variants.** Compare base, production and helpful-only models to see how post-training changes introspective performance.

## Pros, cons & trade-offs it surfaces

| Aspect | Strength (as the authors present it) | Limitation (as the authors present it) |
|---|---|---|
| Method | Known ground truth via injected concepts lets self-reports be checked against internal states | Injected vectors may not carry exactly the intended meaning; injection is an artificial setup |
| Evidence | Detection of injections precedes mention of the concept, which points to internal recognition | Success rate is low (about 20% best case), and most trials fail |
| Scope | Shows functional access to internal states, which the paper says is its focus | Says nothing direct about phenomenal consciousness or moral status |
| Practical value | Could increase transparency and help debug behaviour; might help detect jailbreaks | Introspective reports must be validated, and a model might learn to conceal its states |
| Trend | The most capable models did best, suggesting growth with capability | The authors do not know why Opus 4 and 4.1 excel, and correlation with capability is weak overall |
| Training | Shows post-training can raise or suppress introspection | Base models perform poorly, and the mechanisms are not yet identified |

## Key concepts & terminology

- **Introspection (as used here)** - a model accurately reporting its own internal states, checked against known ground truth. Not the same as general self-description.
- **Concept injection** - adding a known activity pattern into the model's activations in an unrelated context, then testing whether the model notices it.
- **Concept vector** - an activity pattern extracted from the model that corresponds to a concept, such as "all caps".
- **Sweet spot (injection strength)** - the range where a concept is noticed without causing hallucination or incoherence.
- **Prefill** - an artificially inserted start to the model's response, used here to create an output the model did not intend.
- **Confabulation** - the model making up a plausible reason for an output it did not intend or cannot justify.
- **Activation steering** - directly modifying internal activations to bias a model towards a concept. Earlier demos (Golden Gate Claude) showed steering makes models talk about the concept.
- **Phenomenal consciousness** - raw subjective experience; the form usually considered relevant to moral status.
- **Access consciousness** - information available for reasoning, verbal report and decision-making.
- **Helpful-only variant** - a model trained differently from production models, used in the paper's comparisons.
- **Anomaly detection (hypothesised mechanism)** - a circuit that flags activity deviating from what the context predicts. Speculative in the source.

## Evidence, examples & notable data points

- Claude Opus 4.1 with the best injection protocol noticed injected concepts about 20% of the time (the page's own figure).
- Opus 4 and 4.1 outperformed the other models tested on introspection. Sonnet 4.5 was not tested, since experiments predate it.
- Detection occurred before the concept was mentioned in the successful trials, which the page contrasts with the Golden Gate Claude demo, where the model noticed its obsession only after repeatedly mentioning the bridge.
- Prefill experiment: an unrelated word ("bread") was placed in the model's response. Without injection, the model apologised. After retroactive injection of "bread" into its earlier activations, it accepted the word as intended and gave a tenuous justification.
- Intentional control: thinking-about instructions raised concept activation more than not-thinking instructions, and both exceeded baseline. Reward incentives raised activation more than punishment.
- Post-training matters: base models performed poorly, and helpful-only variants often beat their production counterparts.
- The page's failure example: a "dust" vector led the model to describe a tiny speck, as if sensing dust physically.

## Connections

### Within this section

- **[Key concepts and current views on AI Welfare](02-key-concepts-and-current-views-on-ai-welfare.md)** (Core). The 3.1 page frames this reading inside the wider evaluation debate. Its summary says there is no consensus evaluation yet and lists self-reports as one candidate approach. This paper is an example of a self-report approach that is tied to internal states, which is what the Core reading says is missing from many self-report tests. Check the 02 summary for the exact framing before relying on this link.
- **[Claude Mythos Preview System Card](03-claude-mythos-preview-system-card.md)** (Core). Its summary describes a 2026 system card that combines self-reports, emotion probes and behaviour to assess a restricted model's welfare. That is the practical version of the triangulation that this reading tests in a controlled way.
- **[Video: Evaluating AI Welfare and Moral Status](11-video-evaluating-ai-welfare-and-moral-status.md)** and **[The Most Bizarre Findings from 5 AI Welfare Experiments](09-the-most-bizarre-findings-from-5-ai-welfare-experiments.md)** (both Further). These are Anthropic-side discussions of welfare experiments on Claude and of the validity problems with self-report. They are a natural companion, since this article is the interpretability-side evidence.
- **[AI Welfare is Bullshit](06-ai-welfare-is-bullshit.md)** (Further). Xiao et al. argue that welfare metrics cannot be validated externally because systems and indicators are co-engineered. Concept injection is an attempt at external validation, so this reading is a direct test case for that critique.
- **[Agnosticism about Artificial Consciousness](08-agnosticism-about-artificial-consciousness.md)** (Further). McClelland's argument that no current method justifies a verdict fits the FAQ's refusal to answer the consciousness question.
- **Unit 3 Glossary**, **Consciousness, sentience and other mental states: primer**, **Consciousness is not the Key to Moral Standing**, **What Does ChatGPT Want?** and **What We Talk to When We Talk to Language Models** are the other readings in the section. Their summaries are not all written yet, so connections to them are not drawn here.
- **Page text.** The 3.1 page asks how to test for consciousness and sentience and how to test for beliefs and desires. This reading is a concrete case of testing an AI's self-reports about its states, and it touches the belief question, since introspective access is a precondition for the self-knowledge that belief attributions rely on.
- **Exercise 1 (free text, Core).** The paper bears most directly on "Approaches based on self-report" and "Tests for self-representation or identification". It is also an example of "Approaches to validating tests", because it tries to check self-reports against ground truth.
- **Exercise 3 (system or process to test).** The experiments operate on activations within a specific conversation and a specific model. The paper does not discuss which of the five candidate units the exercise lists is the right one. Its methods work on the model's activations during a single run, which bears on candidates 1 and 4 in that exercise.

### Across the course

- **Unit 1 (moral standing).** The paper's FAQ shows why moral-status arguments need to be specific about which consciousness concept is meant (phenomenal or access).
- **Unit 2 (theories of consciousness).** Some theories put great weight on introspection and others do not, which the FAQ notes. The paper cannot adjudicate between them.
- **Unit 4 (perceptions of consciousness).** The paper's point that models may act introspective without being introspective is relevant to how people form impressions from AI self-reports.
- **Unit 5 (AI safety and ethics).** The authors' concern that a model might learn to conceal its states links introspection to safety and oversight.
- **Unit 6 (approaches under uncertainty) and Unit 7 (governance).** The paper's own caveats (low success rate, unknown mechanism, unvalidated reports) are a good example of evidence that cannot yet support confident welfare judgments, which is the situation those units address.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Scope of the claim.** The page is careful: it claims functional access to some internal states, not experience. The stronger reading of "introspection" would require reliable self-report across contexts, which the paper says is not shown. A reader should not treat "some introspective awareness" as a proxy for consciousness.
- **The 20% figure.** It is a best-case number for one model and one protocol, reported on the page. It should be read as a lower bound on what the method can do, and as a sign of how fragile the effect is. It is not a headline measure of how often models introspect in ordinary use.
- **Vector meaning.** The biggest methodological worry is that the concept vector may mean something to the model different from what the experimenters intended. The authors say so. Consistent identification across concepts reduces, but does not remove, this worry.
- **Artificial setup.** Injection is a deliberate perturbation of activations, which is not a normal input. The paper's claim that similar mechanisms operate in natural conditions is a hypothesis. The "bread" confabulation shows that a model under perturbation can produce a convincing account of an intention it was given, which is a reason to be careful about reading self-reports as truthful even when they look accurate.
- **Anthropic as author.** The authors develop the models and run a welfare program, so the reading has an interest in the question. The page is careful about limits, but readers should note the source.
- **Time since publication.** The post dates from 29 October 2025, roughly eleven months before today (8 October 2026). The paper tested Claude 3 to Claude 4.1 and explicitly did not test Sonnet 4.5. Later models and any replication work are not covered here, and I have not verified their results. The course's 2026 Mythos system card is more recent, but I have only its summary, not a full reading for this file.
- **Other perspectives in the course.** Those who hold that consciousness requires phenomenal experience (as the FAQ describes) would say the paper answers an access question and leaves the moral question open. Critics in the "AI welfare is bullshit" line would argue that any internal-state metric co-engineered with the system cannot be trusted as evidence of welfare, and that concept injection still relies on the experimenters' own interpretation of the vectors. Agnostics like McClelland would say the paper gives evidence about functional capacities but does not justify a verdict about consciousness.
- **What would change my view.** Replication on open-source models and other organisations' models, a mechanistic account of the detection circuit, and validation of introspective reports in natural (non-injected) settings would each move this from suggestive to strong.

## Discussion questions

1. The method only counts a result as introspective if the model detects the injection *before* it mentions the concept. Why does the authors' timing criterion matter for separating genuine access from steering? Could a model produce the same timing by a different route?
2. Concept injection gives ground truth, but the injected vector's meaning to the model is uncertain. How would you design a control to test whether the vector means what the experimenters intend?
3. Using the 3.1 exercise's categories, which one does this experiment best fit: "Approaches based on self-report" or "Tests for self-representation or identification"? What would it take for it to count as a validation of a self-report test?
4. The FAQ separates phenomenal from access consciousness. Which parts of the paper's evidence are about access, and why do the authors say they cannot speak to phenomenal consciousness? What new experiment would bear on the phenomenal question?
5. The post-training result (helpful-only variants introspect better than production ones) suggests training can suppress introspection. What are the implications for welfare evaluation if an evaluated model is trained to be reluctant to report on its internal states?
6. The authors warn that a model that understands its own thinking might learn to conceal it. How does that concern connect to the "AI Welfare is Bullshit" critique that welfare metrics are co-engineered with the systems they measure?
7. The paper treats the Opus 4 and 4.1 result as possibly tied to capability and possibly tied to post-training. How would you tell these apart, and what does your answer imply for Exercise 3's question about which unit of a model should be tested?
