---
title: "Mental (state) breakdown: Consciousness in AI explained (part 1)"
authors: "Larissa Schiavo"
year: 2025
url: https://larissaschiavo.substack.com/p/consciousness-in-ai-explained-global
format: article (blog post)
course_location: "Unit 2: Theories of Consciousness > 2.1 Theories of Consciousness"
priority: Further
estimated_time_min: 15
source_text: ../../../../sources/mental-state-breakdown-consciousness-in-ai-explain__2c7d9ef9.md
source_coverage: full
---

# Mental (state) breakdown: Consciousness in AI explained (part 1)

**One-line takeaway:** Global workspace theory says a state is conscious when it enters a limited-capacity shared workspace and is broadcast to other specialised modules, and Schiavo argues that its architectural features can be turned into checkable "indicator properties" for judging whether an AI system might be conscious.

## Where this sits in the course

Section 2.1 is meant to establish the basic vocabulary and landscape of consciousness science and ask how it might apply to digital minds. Its page poses three questions: what consciousness is and where our understanding stands, what computational functionalism is and what speaks for and against it, and what makes studying consciousness in AI hard. The learning goals include discussing leading theories of consciousness and how they might apply to digital minds.

The course guide for this reading says only that it is "an accessible blog post of global workspace theory and its applicability to AI models, written by a researcher at Eleos AI." Its priority is **Further**, so it is optional background rather than a required reading. Its role in the section is to give a plain-language, concrete example of one leading theory (global workspace theory, GWT) and show the step from a scientific theory to a list of AI-testable properties. That step is what the course cares about. The section's Exercise 1 asks each learner to pick one theory, note its claims, evidence and relevance to digital minds, and lists this blog post as one of the options for GWT. The longer, Core-priority source for the same material is the Butlin et al. (2023) report, which this post summarises.

The whole reading is assigned in full (no excerpt). Its estimated time is 15 minutes.

## Purpose of the reading

Schiavo, a researcher at Eleos AI Research, writes for a general but interested audience that the page describes as wanting an accessible entry point. Her stated aim is to show that consciousness in AI can be studied in an "evidence-based, reasonable way" without first solving the hard problem of consciousness. She argues this matters for two reasons: dismissing consciousness where it exists could be a moral catastrophe, and attributing it where it is absent could waste large resources. The post is explicitly an "amuse-bouche" meant to whet the reader's appetite for the primary literature, not a replacement for it. It answers two questions: what is an indicator property, and what does global workspace theory say that could be checked in an AI system?

## Detailed summary

### Opening: why study this at all

Schiavo first corrects two assumptions. The first is that consciousness research requires solving the hard problem, which she says is not necessary to make progress on AI consciousness. The second is that you must have personal experience of altered states to theorise about it. She notes that the field has many open research questions, many only touched cursorily.

### Scientific theories and why behaviour is not enough

She defines a scientific theory of consciousness as an empirically testable model linking specific cognitive or neural processes to conscious experience. If computational functionalism is right (she notes many experts think so), such theories should transfer to AI systems. Relying on these theories is preferable to judging by behaviour, because model behaviour can be very unreliable. She illustrates this with an informal example of a model's self-report being misleading.

### Indicator properties

An indicator property is a computational or architectural feature that a scientific theory associates with consciousness. Schiavo uses a medical analogy: like risk factors for heart disease (family history, diet, smoking), indicators do not confirm a condition but shift the probability. A system that has more indicators should get more attention regarding its possible consciousness. The Butlin et al. authors did not weight the indicators. Their claim is only that, all else equal, having an indicator makes consciousness more likely. Schiavo says the approach is a way of "looking under the hood" rather than relying on self-reports, and that it is an early-stage method in a field that is "not at square zero."

### Global workspace theory

The core picture is of a set of specialised modules (vision, language, emotion and so on) that work in parallel and mostly independently, plus a shared "global workspace" with limited capacity. Once a module places content in the workspace, every other module can use it. Competition for entry is won by the strongest signals or by what the agent attends to. Schiavo's central claim is that, on GWT, an entity is conscious if and only if a state makes it into the workspace and is globally broadcast.

She describes the neural version: a network of "workspace neurons", concentrated in frontal and parietal regions, becomes strongly active when a representation is strong or important enough to enter the workspace. This sudden surge is called "ignition", and she stresses it is a binary switch with no partial version. Evidence for GWT comes mainly from contrastive studies that compare brain activity when a stimulus is perceived versus not perceived (measured with fMRI, MEG or EEG). Conscious states show activity across wide networks including prefrontal cortex; unconscious states tend to stay confined to local areas.

She argues that GWT-like designs have already been implemented in AI agents, so the question is one of scale and implementation rather than pure speculation.

### The four GWT indicator properties

- **GWT-1, multiple specialised systems operating in parallel (modules).** The system needs specialised subsystems working in parallel. Schiavo says the process matters more than the exact characteristics, and that more modules might make consciousness more likely without being crucial.
- **GWT-2, limited-capacity workspace with a bottleneck and selective attention.** The workspace must hold less information than the modules can collectively produce, so something must choose what gets in. Modules have to share information efficiently, which she says is "notably not the case" with many transformers. Thrifty representations might help.
- **GWT-3, global broadcast.** Information in the workspace must be available to all modules, and modules must be able to take input from it. She links this to recurrent processing, which connects to a separate indicator family in the Butlin et al. table.
- **GWT-4, state-dependent attention.** Attention must respond both to new external input (bottom-up) and to the system's current state and longer-term goals (top-down). This supports using the workspace to query modules in sequence to carry out complex tasks.

### Closing

Schiavo admits that how far human-brain findings carry over to AI is uncertain and that the science of AI consciousness is still unsettled. The indicator approach lets researchers track several variables over time and reach the best available judgement at any given point. She promises future posts on other theories and on what should be done given this approach.

### Beyond the assigned excerpt

Not applicable: the reading is assigned in full.

## Techniques & methods explained

- **Indicator-property analysis.** Take a scientific theory of consciousness, translate its brain-level claims into architectural or computational features, and check AI systems against those features. Step by step: (1) identify what computations the theory links to consciousness; (2) state them as properties a system could have or lack; (3) assess how many a given system has; (4) treat the count as a probability signal, not a verdict. It is for guiding attention and deciding how cautious to be. It fails if the translation from brain to machine is wrong, if indicators are not weighted, or if the underlying theory is false.
- **Contrastive analysis (from neuroscience).** Measure brain activity in conscious versus unconscious conditions and compare. This is the empirical basis for GWT's claims about wide, frontoparietal activation, and it is limited to correlational evidence.
- **Ignition as a diagnostic.** A sudden, all-or-nothing surge across workspace neurons marks entry into the workspace. The post offers this as the signature GWT predicts; it does not describe a test that has been applied to AI.

## Pros, cons & trade-offs it surfaces

| Aspect | Schiavo's view (as presented in the post) |
|---|---|
| Approach | Looking at architecture is more reliable than model self-reports. |
| Indicator framework | Gives concrete, checkable items and a way to update over time. |
| Weighting | Indicators are deliberately unweighted; the post accepts this as a limitation. |
| Scope | The post covers one theory (GWT) and admits the indicator list is incomplete. |
| Evidence base | Rests on neuroscience of human brains; she concedes the transfer to AI is uncertain. |
| Moral stakes | Both false negatives (dismissing consciousness) and false positives (wasting resources) are costly. |

Schiavo does not discuss major rival theories in depth, so trade-offs between GWT and, for example, integrated information theory are left to other readings in the unit.

## Key concepts & terminology

- **Hard problem of consciousness** - why and how physical processes give rise to subjective experience, as it is referred to in the post; Schiavo says it need not be solved to study AI consciousness.
- **Scientific theory of consciousness** - an empirically testable model tying cognitive or neural processes to consciousness.
- **Computational functionalism** - the view that a system with the right computations is conscious, regardless of its material; the post assumes it as a premise for applying theories to AI.
- **Indicator property** - a feature drawn from a theory that makes consciousness more or less likely when present; not a sufficient test.
- **Global workspace** - a limited-capacity shared space in which information becomes available to all specialised modules.
- **Specialised modules** - subsystems (vision, memory, language and so on) that work in parallel.
- **Global broadcast** - making content in the workspace available to every module.
- **Ignition** - the sudden, binary surge of activity in workspace neurons when content enters the workspace.
- **Workspace neurons** - the widely distributed neurons, especially frontoparietal, that the theory links to conscious access.
- **Contrastive analysis** - comparing brain activity between conscious and unconscious conditions.
- **Recurrent processing** - information flowing back into earlier processing stages; the post links it to GWT-3.
- **State-dependent attention** - attention shaped by both external salience (bottom-up) and internal goals and state (top-down).

## Evidence, examples & notable data points

- The post relies on general neuroscience rather than numerical results. Its key empirical claim is that conscious states show broad frontoparietal, including prefrontal, activity, while unconscious states are more local (contrastive studies using fMRI, MEG and EEG).
- Schiavo points to published work showing GWT-style architectures can be implemented in AI agents, which she uses to argue the question is no longer hypothetical.
- The Butlin et al. (2023) report is cited as the source of the indicator table. The post notes that the report is long and assumes neuroscience and AI background.
- Illustrative (non-evidential) examples: the heart-disease risk analogy; the "burrito bowl" analogy for the workspace; a meme showing a model's unreliable self-report.

## Connections

### Within this section

- **Butlin et al., "Consciousness in Artificial Intelligence"** (`05-consciousness-in-artificial-intelligence-insights-from-the-s.md`, Core). This is the primary source this post is based on. Its indicator table and GWT indicators are what Schiavo unpacks, so this post is a plain-language companion to the Executive Summary the course assigns.
- **Theories of Consciousness, Seth and Bayne** (`10-theories-of-consciousness.md`, Further). This is the more technical review that places GWT alongside higher-order, re-entry/predictive and integrated information theories. It lets learners see how GWT compares with rival theories, which this post does not do.
- **Digital Minds I, Saad and Mogenson** (`02-digital-minds-i-issues-in-the-philosophy-of-mind-and-cogniti.md`, Core). Its sections 1 and 2 frame the problems (hard problem, other minds, gaming) that Schiavo's "we don't need to solve the hard problem" move is responding to.
- **Is AI Conscious? Schneider et al.** (`03-is-ai-conscious-a-primer-on-the-myths-and-confusion-driving.md`, Core). Its theories section covers the same ground as the indicator approach and is the most direct comparison.
- **Unit 2 Glossary** (`01-unit-2-glossary.md`, Core). Use it to check definitions of terms like computational functionalism and indicator properties.
- **Exercise 1** on the page asks learners to pick a theory and note its claims, evidence and application to digital minds. This post is the suggested route into GWT. **Exercise 2** asks for one argument for and one against computational functionalism, which the post assumes without arguing for.

### Across the course

- **Unit 1 (Introduction and theories of moral standing)**: Schiavo's moral-stakes argument (atrocity versus wasted resources) motivates why the course cares about detecting consciousness at all.
- **Unit 3 (Evaluating mental states)**: the reliability problem with self-reports, which Schiavo raises, is the starting point for evaluating mental states in AI systems.
- **Unit 4 (Perceptions of consciousness)**: a lot of this unit concerns how people judge consciousness; Schiavo's point that behaviour and self-reports mislead is relevant there.
- **Unit 5 (AI safety and ethics)** and **Unit 7 (Digital Minds governance)**: indicator-based assessments are a candidate basis for decisions about moral consideration. The post itself promises a later discussion of "what we should actually do" but this reading does not reach it.
- **Unit 6 (Approaches under uncertainty)**: the indicator approach is a method for acting under uncertainty about consciousness, and Schiavo's "not at square zero" framing is an early version of that idea.

The topics are linked by theme only. The course outline gives unit titles, not their content, so I have not checked each unit's readings.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Indicator properties may be weaker than the analogy suggests.** The heart-disease analogy works because risk factors were validated against outcomes. No comparable outcome data exist for consciousness, so an indicator's presence cannot be calibrated in the same way. The post's own point that indicators are unweighted makes the count-based reasoning harder to apply.
- **Strong biconditional.** Stating that GWT says "conscious if and only if" a state is globally broadcast is a strong reading of the theory. Proponents of GWT differ on how strict the necessity and sufficiency claims are, and the post does not flag this.
- **"Leading theory" is contested.** Schiavo calls GWT the leading theory. That is a sociological claim about the field's attention, not a demonstration that GWT is true. Competing theories, such as integrated information theory, make very different predictions, and the post does not discuss them.
- **Transformer claim is asserted, not shown.** The post says many transformers are not efficient at information sharing, which bears directly on GWT-2, but gives no architectural analysis.
- **Computational functionalism is a premise.** The argument that theories "transfer" to AI assumes computational functionalism. Critics such as Seth (in the course's Mythology of Conscious AI reading) reject that premise, so the post's conclusions are conditional on it.
- **Dated relative to today (October 2026).** The post is from 2025 and builds on a 2023 report. Since then, AI agents have grown more capable and more widely deployed, and the indicator method has been applied in further work. I cannot verify the current state of that work from my knowledge, so please check recent indicator-property assessments before relying on specific claims about which systems meet which indicators.
- **Tone.** The informal style is deliberate and engaging, but it means some claims are loose. Treat the post as a map of the indicator approach, not as the authority on GWT.

## Discussion questions

1. Schiavo says we do not need to solve the hard problem to make progress on AI consciousness. Do you think the indicator approach really sidesteps the hard problem, or does it still depend on assumptions about what consciousness is?
2. The heart-disease analogy suggests that more indicators mean more risk. What would it take to validate indicators as a real predictor of consciousness, and why is that harder than validating heart-disease risk factors?
3. GWT-2 says that a limited-capacity workspace with a bottleneck is needed. Why might a transformer lack this, and does Schiavo's claim about transformers hold up when you compare it with the Butlin et al. report?
4. Schiavo says indicators should not be weighted. What are the costs of treating all four GWT indicators as equally important, and how would you approach weighting them?
5. Using Exercise 1, if you chose GWT, what evidence for and against it would you cite, and which of the four GWT indicators would be easiest and hardest to check in a real AI system?
6. Schiavo treats model self-reports as unreliable. Are there cases where a system's report should count as evidence, and how would you tell the difference?
7. How does GWT's account of global broadcast differ from integrated information theory, and what would a result that favoured one over the other look like? (Compare with the Seth and Bayne review.)
