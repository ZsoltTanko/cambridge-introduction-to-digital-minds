---
title: "Frameworks for decision making under uncertainty"
authors: "Cambridge Digital Minds Course Team"
year: 2026
url: https://docs.google.com/document/d/1T_9iltxtGx5tN8QX8oRChfHT4UW6lCJMcNH5AqMiIX8/edit?tab=t.0#heading=h.cuighsf9mc3l
format: course-team primer
course_location: "Unit 6: Approaches under Uncertainty > 6.1 Approaches under Uncertainty"
priority: Core
estimated_time_min: 16
source_text: ../../../../sources/frameworks-for-decision-making-under-uncertainty__e03d7538.md
source_coverage: full
---

# Frameworks for decision making under uncertainty

**One-line takeaway:** The course's own toolkit for acting without certainty (the EU precautionary principle, IPCC likelihood and confidence language, expected utility, Bayesian updating, and three families of moral-uncertainty strategies) is offered as a starting point for digital minds questions, and each tool has limits that matter a great deal when the inputs are speculative.

## Where this sits in the course

**What the section is trying to establish.** Section 6.1 ("Approaches under Uncertainty") asks three questions: what the precautionary principle is and how it might apply to AI; what suffering risks come with creating, or perceiving, digital minds; and which other frameworks might apply. Its learning outcomes include being able to explain the precautionary principle, explain suffering risks, analyse current action and suggestions by AI companies and researchers, and identify existing frameworks and fields that could inform digital minds work. This reading covers the last outcome directly. The section's other core readings are mostly specific arguments (Birch on sentience, Dung on suffering risk, Zhou et al. on a consciousness ethics framework, the Claude constitution excerpt). This primer is the general-purpose toolbox those arguments can be checked against.

**What the course guide says.** The guide marks the reading as Core and as connected to a written prompt. Its one-line description is that it outlines frameworks for approaching uncertainty that have potential read-across to digital minds. The course does not ask you to adopt any of them. The reading itself says it is a starting point: you are invited to ask what is relevant, what is missing, and whether each framework does or does not help with digital minds decisions.

**The specific role it plays.** It is the only reading in the section that is a menu of methods rather than an argument for a position. Exercise 2 uses it directly. You pick one of five frameworks and spend 6 minutes on how it may or may not apply to digital minds, what it might clarify, and its advantages and disadvantages. The five options match the five headings in the primer: the EU precautionary principle, IPCC communication of uncertainty, Bayesian reasoning, expected value and utility, and approaches to moral uncertainty.

**Relation to the unit's question.** The unit asks how to act when neither the empirical facts (is there anything it is like to be this system?) nor the moral theory (what do we owe such a thing?) is settled. The primer covers both halves. Its sections on the precautionary principle, IPCC and Bayes address empirical uncertainty. Its sections on expected utility and moral uncertainty address normative uncertainty. Exercise 1 (Claude's constitution) also asks you to draw on "the approaches to uncertainty you've read about this week", which means this reading is the implicit reference point for that discussion.

**Assigned part.** The whole reading is assigned. There is no excerpt.

## Purpose of the reading

The primer's author is the course team, writing for learners who are new to decision theory, regulatory practice and moral philosophy. Its purpose is not to resolve how to decide under uncertainty about digital minds. It introduces a set of established methods from outside AI ethics and asks the reader to test them against the digital minds case.

The question it answers is roughly this: when there is no easy or certain answer, what structured ways of reasoning exist, where do they come from, and where do they break down? The primer answers by giving each method a short account, a few examples, and the main objections. It does not rank them against each other.

## Detailed summary

The primer has an opening framing paragraph followed by six sections. The walk-through below follows its order.

### Framing

The primer describes itself as a quick overview of frameworks that may be relevant to digital minds questions, especially those without easy or certain answers. It asks readers to treat it as a starting point and to think about what is missing.

### The EU's guidance on the precautionary principle

The precautionary principle is used across many jurisdictions to guide decisions when science cannot fully assess risks to human health or the environment. The primer presents the two standard positions. Supporters say it helps prevent harm. Critics say it is vague, can lean on cognitive biases, and can hinder innovation.

The EU has issued guidelines on applying the principle, aiming to balance protection against freedom for individuals and industry. The primer says these guidelines have both critics and supporters, and that their lessons may transfer. It lists five things any application should consider:

1. **Proportionality.** Measures should be tailored to the chosen level of protection. A total ban is only appropriate if it is proportionate to the risk.
2. **Non-discrimination.** Comparable situations should not be treated differently, and different situations should not be treated the same without objective grounds.
3. **Consistency.** Measures should match those taken in comparable areas where the science is better understood.
4. **Costs and benefits.** Compare the short- and long-term costs of acting and of not acting. This includes economic analysis, how effective each option is, and public acceptability. The primer quotes the guidance's statement that protecting health takes precedence over economic considerations.
5. **Review against new data.** Someone must be responsible for producing new evidence. Businesses usually have to show their products are safe, though this varies case by case. Measures should be reviewed as data arrives and amended where needed.

### The IPCC's guidance on communicating uncertainty

Fields that deal with high uncertainty need shared conventions for communicating it. The primer says the Intergovernmental Panel on Climate Change (IPCC) framework is widely used but not applied uniformly. It also notes that most of the course does not use the IPCC framework either, to avoid confusion. Two ideas sit at its core.

**Likelihood** is how probable an outcome is judged to be. Because people read words like "likely" very differently, the IPCC ties each term to a fixed probability band:

| Term | Probability |
|---|---|
| Virtually certain | 99–100% |
| Very likely | 90–100% |
| Likely | 66–100% |
| About as likely as not | 33–66% |
| Unlikely | 0–33% |
| Very unlikely | 0–10% |
| Exceptionally unlikely | 0–1% |

The framework also recommends flagging when one outcome is conditional on another, and factoring that dependence into the assessment.

**Confidence** is how far a finding or probability estimate can be trusted. It uses a five-point scale from very low, through low, medium and high, to very high. The grade depends on the quality of the evidence and how well the sources agree. The primer includes a matrix of evidence and agreement, which is an image in the original and is not recoverable from the text.

### Expected value and utility

Expected value weighs possible outcomes by probability. For each outcome you multiply its value by its chance, then sum. The option with the highest total is the one to take. The primer's example is a lottery ticket that pays £100 on a one-in-a-hundred chance. Its expected value is £1, so a rational buyer would pay no more than £1.

Expected utility uses the same logic but substitutes utility, a measure of how good or bad an outcome is, for money. The primer's reason for the switch is that wellbeing and suffering have no natural price, and utility is meant to place them on a common scale. The primer notes that this is the language of utilitarian ethics, in which the aim is the greatest overall good. Expected value is the tool of finance and expected utility the tool of utilitarian ethics. The formula is the same: Expected utility(A) equals the sum over outcomes of the probability of each outcome times its utility.

The primer gives three cautions:

- **The numbers must mean something.** Philosophers dispute whether "good" and "bad" can be placed on one scale, especially for subjective experiences. Some deontologists reject utility altogether, on the grounds that it treats a person as a means to a larger total rather than as an end in themselves.
- **The answer is only as good as the inputs.** Supporters use Bayesian methods and debiasing to improve the numbers and to decide which outcomes count. Critics warn that this can create a false sense of objectivity, especially for subjective or ethical matters.
- **Rare, extreme outcomes can dominate.** A tiny probability of an enormous outcome can swamp the sum. The primer points to Nick Bostrom's "Pascal's Mugging" as the illustration.

Cost-benefit analysis is a close relative. It weighs options by expected costs and benefits, usually in money, which suits policy and finance better than ethics.

### Bayesian reasoning

Bayesian reasoning is presented as a foundational method used across many scientific fields, and as a proposed model of how the brain itself processes information. Belief is treated as a probability that moves up or down with evidence, rather than as all or nothing.

The method has a simple structure. You start with a **prior**, your initial estimate of how likely a hypothesis is. For each new piece of evidence, you ask whether you would expect to see it more if the hypothesis were true than if it were false. Evidence equally likely either way tells you nothing. The size of the shift depends on the ratio of the two likelihoods, which the primer calls the **Bayes factor**. Evidence twice as likely under the hypothesis nudges your estimate. Evidence a hundred times as likely moves it sharply.

The primer illustrates this with medical diagnostic tests. A positive result does not establish disease. Two tests with very low false-negative rates can differ in their false-positive rates. The test with the lower false-positive rate should raise the probability of disease more. Even a good test can leave the probability low if the prior is low: when the disease is extremely rare, being disease-free can remain the more likely outcome.

The relationship is captured by Bayes' theorem, which the primer writes as the probability of the hypothesis given the evidence equals the probability of the evidence given the hypothesis, times the prior, divided by the overall probability of the evidence. In words, you update most when the evidence is tightly tied to the hypothesis, and least when the evidence would probably have appeared anyway. The primer points to Julia Galef's video for an introduction, the Stanford Encyclopedia of Philosophy for a rigorous treatment, and Khan Academy for worked calculations.

### Approaches to moral uncertainty

The section first separates two kinds of uncertainty. Empirical uncertainty is about the facts, and settling it or improving probability estimates is only half the problem. Moral (or normative) uncertainty concerns which moral implications to draw and which theory (for example, consequentialist or deontological) should be used to work them out. The primer groups the proposed responses into three strategies.

**Strategy 1: act on a single theory.**

- *My favourite theory.* Follow the theory you have most confidence in and set the others aside. Defenders say this keeps choices consistent without comparing theories. Critics say it ignores how much could be at stake under the discarded theories, since a slightly less plausible rival might rate a choice as seriously wrong where the favourite rates it as merely suboptimal.
- *Normative externalism.* A more radical position holds that moral uncertainty makes no difference, and you should act in line with whichever theory is in fact correct.

**Strategy 2: weigh the theories and combine them.**

- *Maximising expected choiceworthiness (MEC).* This applies expected-value logic to ethics. Each plausible theory is weighted by your confidence in it and by how strongly it favours an option, and you choose the option that does best overall. Philosophers dispute whether theories can be compared on a common scale, which MEC requires. The same tail problem as in expected utility arises: a theory you find unlikely can dominate if it treats stakes as catastrophic. The primer notes that what to do in such "fanatical" cases is itself contested.
- *The Moral Parliament.* Each theory holds seats in proportion to your confidence in it. The theories vote and bargain. One may concede on an issue it cares little about in order to win on something it regards as a serious violation. The primer says Rethink Priorities has built a tool that applies this, and again notes the dispute over whether theories are comparable enough to bargain.

**Strategy 3: when combining fails, use simpler rules.**

- *Acting on convergence.* Favour actions that many moral theories endorse. This avoids choosing between theories. It works best as a heuristic: several actions can each have broad support while one is still judged severely wrong by a theory you take seriously.
- *Maximin.* Choose the option whose worst-case moral outcome is least bad.
- *Dominance.* If one option is at least as choiceworthy as another under every theory you take seriously, and better under at least one, prefer it. This rule only sorts options that it can compare in this way, and is silent when neither option dominates.

**Intuitions as a check.** When an argument reaches a conclusion that seems clearly wrong, you may reject a premise rather than accept the conclusion. The same applies to the aggregation methods. If MEC or another rule gives a verdict that seems plainly wrong, that is a reason to distrust the rule.

**Reflective equilibrium.** The overall method is associated with John Rawls. It moves back and forth between principles and judgements about particular cases, revising each until they agree. No perspective has the final say. A principle can be dropped if it clashes with a firm conviction, and a particular judgement can be given up if it conflicts with principles you trust more. The primer argues that for questions as new as digital minds, where intuitions are untested and no single theory is trusted, this back-and-forth is often how defensible views first emerge.

### Closing material

The text ends with a Creative Commons licence notice and a statement that Cambridge Digital Minds is the sole authoritative provider of the course, which does not confer credentials unless completed through it. There is no further argument.

## Techniques & methods explained

- **EU precautionary-principle checklist.** Test any precautionary measure against five questions: proportionality, non-discrimination, consistency with better-understood cases, costs and benefits of acting and not acting, and review against new data. *Use:* structuring a policy decision. *Where it fails:* the primer notes critics think the principle is vague and can be biased. Summarizer's observation: the checklist does not say how to weigh its own five criteria against each other.

- **IPCC likelihood banding.** Map each probability judgement onto a fixed term (for example, "likely" means 66–100%). Flag conditional outcomes. *Use:* making probability words comparable across readers. *Where it fails:* the primer says the framework is not applied uniformly. Summarizer's observation: the fixed bands are coarse.

- **IPCC confidence grading.** Rate trust on a five-point scale based on the quality and agreement of evidence. *Use:* separating "how probable" from "how sure we are". *Where it fails:* the grade depends on judgements of evidence quality. Summarizer's observation: those judgements are themselves uncertain in new fields.

- **Expected value and expected utility.** Multiply each outcome's probability by its value (or utility) and sum. *Use:* comparing options with different risks. *Where it fails:* requires commensurable values, depends on inputs, and can be dominated by tiny probabilities of huge outcomes (Pascal's Mugging).

- **Bayesian updating.** Start from a prior; for each piece of evidence, compute the likelihood ratio (Bayes factor); revise the estimate with Bayes' theorem. *Use:* changing beliefs in proportion to evidence, as in diagnostic testing. *Where it fails:* outcomes depend on the prior; the primer notes this matters most when the base rate is extreme.

- **Maximising expected choiceworthiness (MEC).** Apply expected-value logic across ethical theories, weighted by confidence. *Use:* combining theories in a single calculation. *Where it fails:* requires theories to be comparable on one scale; fanatical cases where a low-credence theory with catastrophic stakes dominates.

- **Moral Parliament.** Give theories seats by confidence and let them vote and bargain. *Use:* a procedural alternative to a single scale. *Where it fails:* same comparability dispute as MEC.

- **Convergence, maximin and dominance.** Simpler rules used when combining theories stalls: favour actions many theories endorse, pick the least-bad worst case, or choose options that dominate across theories. *Use:* decisions where comparison is hard. *Where it fails:* convergence is only a heuristic; dominance is silent when neither option dominates. The primer describes maximin only as choosing the least-bad worst case and does not discuss its weaknesses.

- **Intuition-checking and reflective equilibrium.** Revise principles and case judgements against each other until they cohere. *Use:* developing defensible views where theory is untested. *Where it fails:* it depends on which intuitions are kept. Summarizer's observation: no fixed standard decides which to revise.

## Pros, cons & trade-offs it surfaces

The primer presents trade-offs as the course team's summary of positions in the literature, not as its own verdict.

| Framework | Strengths (as presented) | Weaknesses or trade-offs (as presented) |
|---|---|---|
| EU precautionary principle | Has a structured guideline; aims to balance protection and freedom; lessons may transfer | Critics say vague, prone to bias, can hinder innovation; guidelines contested |
| IPCC communication | Shared vocabulary; separates likelihood from confidence | Not applied uniformly; (summarizer's note) fixed bands are coarse |
| Expected value and utility | Puts outcomes on one scale; widely used in finance and utilitarian ethics | Disputed comparability of good and bad; garbage-in, garbage-out; tail-risk domination |
| Bayesian reasoning | Principled way to update on evidence; used across science | Prior-dependent; supporters vs critics on objectivity |
| Single-theory approaches | Consistency; avoids cross-theory comparison | Ignores stakes under discarded theories (favourite theory); (summarizer's note) externalism gives little guidance under uncertainty |
| MEC and Moral Parliament | Uses all plausible theories; accounts for confidence | Theories may not be comparable; fanatical cases contested |
| Convergence, maximin, dominance | Simple; avoids comparing theories | Convergence is only a heuristic; dominance is silent when neither option dominates |
| Reflective equilibrium | Respects both principles and intuitions; suits new questions | Depends on which judgements are held fixed |

## Key concepts & terminology

- **Precautionary principle** - acting to prevent harm when science cannot fully assess risk; here, the EU's five-part application guidance.
- **Likelihood (IPCC)** - how probable an outcome is, mapped to fixed probability bands for standard terms such as "likely".
- **Confidence (IPCC)** - how far a finding can be trusted, graded from very low to very high based on evidence quality and agreement.
- **Expected value** - the sum of outcomes weighted by their probabilities; the basis of the lottery example.
- **Expected utility** - expected value using utility (a measure of how good or bad an outcome is) instead of money.
- **Cost-benefit analysis** - weighing options by expected costs and benefits, usually in monetary terms.
- **Prior** - an initial estimate of a hypothesis's probability before new evidence.
- **Bayes factor** - the ratio of how likely evidence is if a hypothesis is true versus false; it sets how far evidence shifts belief.
- **Bayes' theorem** - the rule for updating the probability of a hypothesis given evidence.
- **Empirical vs moral (normative) uncertainty** - uncertainty about facts versus uncertainty about which moral implications and theories to use.
- **Normative externalism** - the view that you should act on whichever moral theory is in fact correct, regardless of your uncertainty.
- **Maximising expected choiceworthiness (MEC)** - applying expected-value logic across moral theories, weighted by confidence.
- **Moral Parliament** - a method in which moral theories hold seats in proportion to confidence and bargain over choices.
- **Dominance** - choosing an option that is at least as good under every theory considered and strictly better under one.
- **Reflective equilibrium** - the process of revising principles and particular judgements until they cohere.

## Evidence, examples & notable data points

The primer contains no empirical study or experiment. Its evidence is illustrative and historical.

- **EU guidance.** Five application criteria. The primer quotes the guidance's statement that protection of health takes precedence over economic considerations.
- **IPCC bands.** Seven terms from "virtually certain" (99–100%) to "exceptionally unlikely" (0–1%). Confidence graded on five levels.
- **Lottery example.** A £100 prize at a one-in-a-hundred chance has an expected value of £1.
- **Diagnostic tests.** Two tests with very low false-negative rates but different false-positive rates. The primer gives no numbers. It shows that the test with the lower false-positive rate moves the probability more, and that a rare disease can keep the probability low even after a positive result.
- **Bayes factor example.** Evidence twice as likely under a hypothesis nudges belief; evidence a hundred times as likely moves it sharply. This is an arithmetic illustration, not a result.
- **Pascal's Mugging.** Cited to Nick Bostrom as the case where a tiny probability of an enormous outcome dominates expected value.
- **Rethink Priorities.** Cited as having built a tool that applies the Moral Parliament method.

## Connections

### Within this section

- **Unit 6 Glossary** ([01-unit-6-glossary.md](01-unit-6-glossary.md)) - Core. The glossary has the definitions for this week; the primer's terms (precautionary principle, expected utility, moral uncertainty) should be cross-checked against it.
- **The Edge of Sentience** ([02-the-edge-of-sentience.md](02-the-edge-of-sentience.md)) - Core. Birch applies the precautionary principle to sentience and proposes decision frameworks under moral and epistemic uncertainty. The primer's EU section is the general version. Birch's proposals are a specific application.
- **How to deal with risks of AI suffering** ([03-how-to-deal-with-risks-of-ai-suffering.md](03-how-to-deal-with-risks-of-ai-suffering.md)) - Core. Dung's suffering-risk analysis is the risk side of the section's second question. The primer supplies the tools for weighing that risk.
- **A Human-centric Framework for Debating the Ethics of AI Consciousness Under Uncertainty** ([04-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md](04-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md)) - Core. Zhou et al. propose a default of no-consciousness under uncertainty. That default is a prior, and the primer's Bayesian and moral-uncertainty sections show how such a default would be updated or challenged.
- **Claude's Constitution** ([05-claudes-constitution.md](05-claudes-constitution.md)) - Core. The "Claude's Nature" section is the assigned text for Exercise 1, which asks you to weigh over- and under-attribution of moral patienthood using the approaches in this reading.
- **The Societal Response to Potentially Sentient AI** ([07-the-societal-response-to-potentially-sentient-ai.md](07-the-societal-response-to-potentially-sentient-ai.md)) - Further. Caviola's preparatory measures are policy-level decisions under the kind of uncertainty the primer's cost-benefit and EU sections address.
- **Moral Uncertainty** ([08-moral-uncertainty.md](08-moral-uncertainty.md)) - Further. Bykvist is the fuller treatment of the moral-uncertainty strategies sketched in this primer. Read it if you pick the moral-uncertainty option in Exercise 2.
- **Why it makes sense to let Claude exit conversations** ([09-why-it-makes-sense-to-let-claude-exit-conversations.md](09-why-it-makes-sense-to-let-claude-exit-conversations.md)) - Further. An example of a low-cost precautionary measure, which the EU proportionality and cost-benefit criteria can be used to evaluate.
- **How Extreme is the Precautionary Principle?** ([10-how-extreme-is-the-precautionary-principle.md](10-how-extreme-is-the-precautionary-principle.md)) - Further. Hansson asks how far the principle should be pushed. This is the critical question the primer raises only as "critics note".
- **A Human-centric Framework ...** ([11-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md](11-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md)) - Maybe. Same paper as reading 04, fuller read.
- **Claude's Constitution** ([12-claudes-constitution.md](12-claudes-constitution.md)) - Maybe. Same text as reading 05.
- **Role play with Large Language Models** ([13-role-play-with-large-language-models.md](13-role-play-with-large-language-models.md)) - Maybe. Shanahan et al. argue for role-play framing of LLMs, which bears on how evidence about AI behaviour should be interpreted before Bayesian updating.
- **Frameworks and fields that may be relevant to digital minds** ([14-frameworks-and-fields-that-may-be-relevant-to-digital-minds.md](14-frameworks-and-fields-that-may-be-relevant-to-digital-minds.md)) - Maybe. The same team's companion piece, which extends this primer to fields beyond the five covered here.

The section page's exercises depend on this reading. Exercise 1 (Claude's Nature) asks for "the approaches to uncertainty you've read about this week", and Exercise 2 directly asks you to apply one of the five frameworks here. The learning outcome to "identify existing frameworks and fields" is met by this reading.

### Across the course

- **Unit 1 (Introduction and Theories of Moral Standing).** The moral-uncertainty section of this primer assumes you know what consequentialist and deontological theories say. The moral-standing theories in Unit 1 give the candidates that a Moral Parliament or MEC would weigh.
- **Unit 2 (Theories of Consciousness).** Uncertainty about which theory of consciousness is correct is a case of the empirical or normative uncertainty the primer describes. Expected-utility and Bayesian methods are the natural way to combine such theories' verdicts, with the same comparability problems.
- **Unit 3 (Evaluating mental states) and Unit 4 (Perceptions of consciousness).** The primer's cautions about biased inputs and debiasing connect to the course's discussion of how people misjudge minds. The Shanahan reading and the anthropomorphism material in Unit 4 raise the same concern about inputs.
- **Unit 5 (Interactions with AI Safety and Ethics).** Expected-value and tail-risk arguments are common in AI safety. The Pascal's Mugging warning applies directly when comparing speculative AI risks with digital minds welfare.
- **Unit 7 (Digital Minds Governance).** The EU precautionary principle, with its proportionality and review criteria, is a template for governance. Cost-benefit analysis is the policy tool that most governance proposals will use.
- **Unit 8 (Reflections and Next Steps).** Reflective equilibrium is the method a learner is likely to use to form their own view at the end of the course.

**Agreements and tensions.** The main tension is between methods that aggregate (expected utility, MEC, cost-benefit) and methods that refuse to aggregate (single-theory, maximin, dominance, convergence). Birch and Zhou et al. both lean on decision frameworks, while Dung's concern about the limits of scientific approaches to AI suffering risk suggests that frameworks for uncertainty may need inputs that science cannot yet provide.

## Critical perspective

*This section is my own analysis, not the source's view.*

- **Transfer from other domains is assumed, not shown.** The EU, IPCC and finance-derived tools were built for climate, health and markets, where probabilities can sometimes be estimated from data. Digital minds questions often lack a reference class, so the probability inputs the primer warns about may be unavailable rather than merely unreliable. The primer flags the problem but does not address whether these tools can run without the inputs.
- **Priors will carry the weight.** In Bayesian and expected-value approaches, the answer depends heavily on the prior probability that a system is conscious or morally considerable. Zhou et al.'s default of no-consciousness is itself a prior, and the primer's own examples show that a low base rate can dominate a positive result. Readers should ask whose prior is being used.
- **Pascal's Mugging applies to digital minds.** If a very small probability of very large suffering is taken seriously, expected-value reasoning could recommend extreme actions. The primer raises the problem and stops short of a resolution. Hansson's paper (reading 10) takes up how far the precautionary principle should go.
- **Comparability is an open problem.** MEC and the Moral Parliament both need theories measured on a common scale or at least comparable enough to bargain. The primer reports this as contested. From outside the course, this is one of the best-known unresolved issues in normative uncertainty research, and I am not aware of a consensus solution.
- **Conservatism of reflective equilibrium.** Reflective equilibrium uses intuitions as a check. For digital minds, intuitions about mind and moral status may be shaped by human-centric bias and by how systems like Claude have been presented. Readers who take anthropomorphism seriously (see reading 13) may see the method as one that could lock in the very biases it is supposed to test. The primer does not address this.
- **Likely pushback from the course's other perspectives.** Dung and Birch would push for precaution, asking why the burden of proof should sit with the claim that a system is not a patient. Zhou et al. would push for a human-centric default and caution against over-attribution. The primer's Bayesian and moral-uncertainty sections are neutral between these, which is useful but means it cannot settle the dispute.
- **Facts that may have changed.** The IPCC framework is the same likelihood scale used in its earlier assessment reports; to my knowledge the calibrated terms have been retained in later assessments, but I have not verified the current wording. The primer is dated 2026 and there is nothing in it I can check for staleness against October 2026 beyond the framework descriptions, which I have no reason to think have changed.

## Discussion questions

1. The EU's five criteria include proportionality and review against new data. Which of these would be easiest to apply to a decision about whether to give a digital system protections, and which would be hardest? Why?
2. The IPCC separates likelihood from confidence. For a claim such as "this system has some morally relevant experience", what would a low-confidence but high-likelihood judgement look like, and does separating the two help or hinder the decision?
3. Expected utility is said to put suffering on a common scale with other goods. Is that scale achievable for the kinds of experience that might matter in digital minds? What would you need to believe for the calculation to be meaningful?
4. Pick one tiny-probability, huge-stakes scenario about digital minds. What does expected-value reasoning recommend? Is that recommendation a reason to reject expected value, or a reason to reject the scenario's inputs?
5. Compare "act on a single theory" with the Moral Parliament. Which would you use if you had to make a decision next week about a digital minds issue, and what would you lose by choosing it?
6. Reflective equilibrium revises principles against intuitions. Which intuition about digital minds do you hold most firmly, and would you give it up if it clashed with a principle you trust more? What would make you do so?
7. Exercise 2 asks you to pick one framework and assess advantages and disadvantages. Which of the five frameworks do you think is most useful for digital minds, and which is most likely to mislead? Give one concrete case for each.
