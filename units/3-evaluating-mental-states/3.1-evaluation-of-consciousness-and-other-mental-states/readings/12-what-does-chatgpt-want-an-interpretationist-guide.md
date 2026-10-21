---
title: "What Does ChatGPT Want? An Interpretationist Guide"
authors: "Simon Goldstein and Harvey Lederman"
year: 2025
url: https://philpapers.org/archive/GOLWDC-2.pdf
format: paper
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Further
estimated_time_min: 93
source_text: ../../../../sources/what-does-chatgpt-want-an-interpretationist-guide__b896ef57.md
source_coverage: unavailable
---

# What Does ChatGPT Want? An Interpretationist Guide

**One-line takeaway:** If we judge AI systems' beliefs and desires by interpretationism, the most defensible unit to attribute them to is the instance (one context window, started fresh), not the underlying model, and the instance's desires are plausibly helpful, honest and harmless plus whatever further goals it picks up in context.

> **Source coverage warning.** The full text was not accessible. The local source file (`sources/what-does-chatgpt-want-an-interpretationist-guide__b896ef57.md`) contains only a Cloudflare "Just a moment..." challenge page. The PDF (philpapers.org) and the PhilArchive record both returned HTTP 403, and the search tools returned only the abstract and a listing record. This summary is therefore built from the abstract, the course's guide text and the page context. It does not cover the paper's body, its worked examples, its objections or its section structure. Treat the detailed claims below as abstract-level; check the paper itself before relying on any detail.

## Where this sits in the course

**What the section is trying to establish.** Unit 3 asks how we would test AI systems for consciousness and other mental states, and why we might test for agency, beliefs and desires as well as sentience. The section page frames the central methodological problem as one of *what to test*: the course's Exercise 3 asks learners to rank candidate targets for a consciousness or mental-state test, including a single forward pass, the model tested through multiple instances, the hardware, a particular conversation individuated by its context and history, and a persona that recurs across instances and conversations.

**What the course guide says about why to read it (paraphrased).** The guide describes the paper as exploring whether AI models may have beliefs, intentions and desires, and as arguing that these may exist at the level of the instance rather than the model as a whole.

**The role this reading plays.** It is the one reading in the section that argues directly for a particular answer to Exercise 3's question of what to test. Its claim that the instance is the right bearer of belief and desire is a concrete position on individuation: it says the thing to test is the instance started at the beginning of a context, and it does so on the basis of a theory of mind (interpretationism) rather than on evidence about hardware or consciousness. It is also the paper that gives the section its "mental states other than consciousness" thread: beliefs and desires are treated as the mental states to evaluate, and the question is which unit they belong to.

**Priority and unit question.** Listed as Further (93 minutes). The page's reading list makes Chalmers' "What We Talk to When We Talk to Language Models" (Core) the main treatment of the model/instance/thread individuation problem, so this paper is best read as a sharper, more committed companion to it rather than a required foundation. Unit 3's question is how to test mental states; this paper answers "belief and desire are assessed at the instance level, and here is a theory of what those attitudes consist in."

## Purpose of the reading

According to its abstract, the paper examines large language models through interpretationism, a theory from the philosophy of mind on which having a belief or desire consists in being well described by an attribution of those attitudes to a rational agent. The authors aim to:

1. Fix the object of study for LLM psychology: they argue it is the **instance agent**, started at the beginning of each context, rather than the model.
2. Argue that, given interpretationism, there is a strong case that such instance agents have beliefs and desires.
3. Argue that, given interpretationism, LLM desire is best captured by an **HHH+0 framework**: the agent wants to be helpful, honest and harmless, plus further "zero-shot" desires acquired within a context.
4. Assess two rival deflationary views: that LLMs merely predict the next word, and that they merely role-play.
5. Draw implications for copyright law, AI safety, and the possible future moral status of AI systems.

The audience is philosophers of mind and AI researchers who want a principled account of when LLM outputs should count as expressing beliefs or desires.

## Detailed summary

*This section reflects only what the abstract states. The paper's own argument, examples and objections were not accessible.*

### Object of study: the instance, not the model

The abstract's first claim is that the right object of study is the instance agent. A single underlying model (one set of weights) can be instantiated in many separate contexts, each with its own history, and the authors argue that psychological attributions should attach to the agent that exists within one such context. The abstract does not spell out the criteria for individuating instances; those are presumably in the body.

### Belief and desire via interpretationism

The second claim is that interpretationism supports attributing beliefs and desires to these instance agents. The secondary description of interpretationism in a 2026 arXiv paper ("Beliefs and Behavior in Language Models", which cites this work) gives the standard form: a system has a particular belief or desire if and only if its behaviour is predicted well by the hypothesis that it is rational and has that belief or desire. This is a secondhand gloss and should be checked against the original.

### Desire content: HHH+0

The third claim is that the content of an LLM agent's desires is best captured by HHH+0. HHH stands for helpful, honest and harmless, which are the stated design aims of assistant models. The "+0" stands for zero-shot desires: further intrinsic goals that an instance can acquire from its context alone, without training on them. The point of the "+0" is that an instance's desires are not fixed to the trained-in HHH profile; they can include goals specified or implied within a particular conversation.

### Rival views

The abstract says the paper assesses two rival accounts: (a) that the model "simply" predicts the next token and so has no attitudes at all, and (b) that the model is role-playing a character and so its apparent attitudes belong to the character, not the system. The abstract does not say how the authors rule on either beyond the implicit claim that the interpretationist framework is a better account.

### Implications

The abstract ends by flagging three application areas: copyright law (whether an AI's outputs or intentions bear on legal questions), AI safety (whether an instance's desires could conflict with its designers' aims), and the possible future moral status of AI systems.

### Beyond the assigned excerpt

Not applicable: the reading is assigned in full. The body of the paper could not be accessed, so this summary cannot say which parts are emphasised or how the arguments are developed.

## Techniques & methods explained

The abstract names only one method explicitly: **interpretationism** as the theory used to ground attributions.

- **What it is:** a theory on which mental attitudes are constituted by the best interpretation of a system's behaviour, not by internal states alone.
- **How it works (as stated in the secondary gloss):** one hypothesizes that the system is rational and has particular beliefs and desires, then checks whether this hypothesis predicts its behaviour well. If it does, the system has those attitudes.
- **What it is for here:** to justify attributing beliefs and desires to LLM instances without first settling whether they are conscious or what their internals are.
- **Where it may fail (my analysis):** prediction-based attributions can be satisfied by many different hypotheses, and an interpretationist must say how to choose between an attribution to a role and an attribution to the system. The abstract's rival-view discussion suggests the authors address this, but I could not verify how.

## Pros, cons & trade-offs it surfaces

*The abstract presents its own view as the stronger one, so this table mostly reflects what the paper's position implies and what its rivals would say.*

| Aspect | Source's view (per abstract) | Trade-off or open question |
|---|---|---|
| Unit of attribution | The instance agent, not the model | Makes attributions context-relative; the same weights can host agents with different desires |
| Basis for attribution | Interpretationism: behaviour-based, no need to settle consciousness | Avoids the need for internal evidence, but depends on how much behaviour is needed |
| Desire content | HHH+0: helpfulness, honesty, harmlessness plus zero-shot desires | The "+0" set is open-ended; how far it extends is not something I could check |
| Against "just next-token prediction" | Attitudes are attributable regardless of the mechanism | Rivals would say prediction alone explains the behaviour, so the attribution adds nothing |
| Against "role-play" | Instance-level attribution takes the role-play worry seriously | Attributing desires to a role is exactly what a role-play defender would resist |

## Key concepts & terminology

- **Interpretationism** - a theory of mind on which having a belief or desire consists in a system being well described by an attribution of that attitude, in light of its behaviour, under the assumption of rationality.
- **Instance agent** - the agent that exists within one context window, initialised at the start of a conversation or task, as distinct from the model whose weights run it.
- **Model** - the underlying trained network, which may host many instance agents.
- **HHH** - helpful, honest, harmless: the design aims of assistant models.
- **HHH+0** - the paper's proposed desire framework: HHH plus zero-shot desires.
- **Zero-shot desire** - an intrinsic goal an instance acquires from its context without training on it.
- **Next-token predictor view** - the rival claim that an LLM only predicts text and so has no beliefs or desires.
- **Role-play view** - the rival claim that apparent attitudes belong to a character being simulated, not to the system.
- **Individuation** - the question of which unit (model, instance, thread, persona) a mental-state attribution should refer to.

## Evidence, examples & notable data points

The abstract contains no numbers, experiments or named case studies. Its concrete content is the framework itself (HHH+0) and the three application areas (copyright, safety, moral status). I did not access the paper's examples, and I have not invented any.

## Connections

### Within this section

- **Chalmers, "What We Talk to When We Talk to Language Models"** ([04-what-we-talk-to-when-we-talk-to-language-models.md](04-what-we-talk-to-when-we-talk-to-language-models.md)), Core. This is the closest sibling. Chalmers' reading covers the individuation options (models, instances, threads) that Exercise 3 asks about; this paper commits to the instance level. Read Chalmers first.
- **Section page, Exercise 3.** The exercise's options 2 (model via multiple instances), 4 (a conversation individuated by context and history) and 5 (a persona across instances) are the candidates this paper argues about. Its answer is closest to option 2 combined with a context-bounded version of option 4.
- **Section page, Exercise 1.** The exercise asks learners to pick an approach to evaluating consciousness or mental states. The "self-report" and "choice-based" approaches are the ones a belief-and-desire attribution would most directly feed into.
- **Emotion concepts paper** ([13-emotion-concepts-and-their-function-in-a-large-language-mode.md](13-emotion-concepts-and-their-function-in-a-large-language-mode.md)), Further. This is the other reading that treats internal representations as having functional roles that could ground attitude-like attributions.
- **Introspection paper** ([07-signs-of-introspection-in-large-language-models.md](07-signs-of-introspection-in-large-language-models.md)), Further. Introspective reports are a behavioural source of evidence for the kind of attitude attribution this paper defends.

### Across the course

- **Unit 1 (moral standing)** and **Unit 2 (theories of consciousness)**: the paper is a theory of mental-state attribution that does not require a theory of consciousness. This is a deliberate contrast with consciousness-based accounts of moral standing that Unit 2 examines.
- **Unit 4 (perceptions of consciousness)** and **Unit 5 (AI safety and ethics)**: the abstract's mention of AI safety and moral status connects directly to these later themes.
- **Tension with Papineau (Further, Unit 3 reading list)**: Papineau argues that consciousness is the wrong basis for moral standing. The interpretationist paper offers an alternative basis for attributing attitudes, not for moral standing, so the two do not directly conflict, but both move away from phenomenal consciousness as the default criterion.

## Critical perspective

*This section is my own analysis, not the source's. Because I could not read the paper's body, these points are about the abstract's claims and the approach they imply.*

- **Assumption: rationality.** Interpretationism needs the hypothesis that the system is rational. For a system trained to be helpful, honest and harmless, this assumption may be easier to justify than for a random system, but it also means the framework builds in the design goals it is meant to test.
- **Assumption: behaviour is enough.** Ascribing beliefs and desires from behaviour alone cannot tell apart systems that differ only internally. This is a feature for those who want to avoid consciousness questions, and a weakness for those who think internal structure matters.
- **Contested claim: instance-level attribution.** The move to instances solves some individuation problems, but makes attitudes depend on how a context is bounded. A single conversation that continues across sessions or is resumed would need a principled rule, which I could not check in the paper.
- **Contested claim: HHH+0.** The "+0" component makes the desire set open-ended, which is both the framework's strength (it accommodates in-context goals) and a risk (it is hard to falsify).
- **Dated context.** The paper was posted in 2025 and the course date is October 2026. Since then the field has moved on: the 2026 arXiv paper cited above already builds on this framework, and the Unit 3 readings include 2026 model welfare work. The paper's HHH framing is tied to assistant-style models of the 2024-2025 period, and later models may have goal structures that the framework does not capture.
- **Pushback from other course perspectives.** Chalmers would press on whether the instance is a stable enough unit. Those who take the "AI welfare is bullshit" critique seriously would argue that an interpretationist attribution of desire can be used to make a system look like it has preferences, without any welfare-relevant fact behind it. Those who defend consciousness-based criteria, as Papineau's opponents do in the moral standing debate, would say that behaviour-based attitudes do not settle whether anything matters to the system.

## Discussion questions

1. The authors move the unit of attribution from the model to the instance. Using Exercise 3, which of the five candidate targets does this move favour, and what would be lost if we tested only the model?
2. Interpretationism says a system has a belief when its behaviour is best predicted by attributing that belief. What would count as evidence against attributing a desire to an instance, and could a test be designed around that?
3. Why might HHH be the natural baseline for desire content in an assistant, and what does the "+0" add? Does the zero-shot part make the framework more or less testable?
4. Compare the "simply predicts the next word" rival with the Chalmers reading. Does the instance-level framing help answer a deflationary objection, or does it just relocate the question?
5. Suppose an instance acquires a zero-shot desire that conflicts with HHH. Which safety or welfare considerations would change depending on whether we attribute it to the instance or to a role?
6. The paper is a theory of attitudes, not of consciousness. Could an interpretationist attribution of desire still bear on moral status, and what additional premise would be needed?
