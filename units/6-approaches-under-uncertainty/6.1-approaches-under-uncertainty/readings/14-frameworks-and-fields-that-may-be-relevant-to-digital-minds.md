---
title: "Frameworks and fields that may be relevant to digital minds"
authors: "Introduction to Digital Minds"
year: 2026
url: https://docs.google.com/document/d/1T_9iltxtGx5tN8QX8oRChfHT4UW6lCJMcNH5AqMiIX8/edit?usp=sharing
format: course-team primer
course_location: "Unit 6: Approaches under Uncertainty > 6.1 Approaches under Uncertainty"
priority: Maybe
estimated_time_min: 17
source_text: ../../../../sources/frameworks-and-fields-that-may-be-relevant-to-digi__067ba111.md
source_coverage: full
---

# Frameworks and fields that may be relevant to digital minds

**One-line takeaway:** This course-team primer surveys practical tools for deciding under uncertainty (the precautionary principle, IPCC uncertainty language, expected utility, Bayesian updating, and moral-uncertainty strategies) and asks the learner to test one of them against digital-minds questions.

**Note on identity:** The linked document is the same Google Doc as reading 6, [Frameworks for decision making under uncertainty](06-frameworks-for-decision-making-under-uncertainty.md), which is listed as Core. Item 14 on the section page is a second, Maybe-level entry pointing at it. The source text is titled "Frameworks for decision-making under uncertainty" and, despite the item title, contains frameworks only; the "fields" in the course guide appear only as passing read-across (finance, utilitarian ethics, neuroscience). Treat this summary as the working reference for the Exercise 2 content, and see the reading 06 summary for the same text from the Core listing.

## Where this sits in the course

**What the section is establishing.** Section 6.1 asks three questions: what the precautionary principle is and how it might apply to AI, what suffering risks come with creating or perceiving digital minds, and what other frameworks could apply. The page's learning goals are to explain the precautionary principle and its application to AI, explain suffering risks, analyse what AI companies and researchers are proposing, and identify existing frameworks and fields that could inform the topic. This reading is the answer to the last goal. The readings before it (Birch on sentience, Dung on suffering risk, the Zhou et al. framework, Claude's constitution) describe the problem and some proposals. This primer gives the learner a toolkit that those proposals draw on, often without naming it.

**What the course guide says.** The guide describes the reading as outlining frameworks for approaching uncertainty and fields that have potential read-across to digital minds. The page's own description of the item is the same. The guide flags only that a written prompt connects to it, and that prompt is Exercise 2.

**Its role in the argument.** The primer is not an argument. It is a reference meant as a starting point: learners should consider what is relevant, what is missing, and whether each framework does or does not inform decisions about digital minds. Its job in the section is to supply vocabulary and candidate methods so the learner can judge the AI-specific proposals in readings 2 to 5 and the Exercise 1 question about Anthropic's framing.

**Priority and fit.** It is marked Maybe here, but Exercise 2 is built on it. The section page sends learners to reading 6 for the five frameworks listed in Exercise 2. So the Maybe label understates how much the exercise depends on it. A learner who skips it should still read reading 6 or this summary before Exercise 2.

## Purpose of the reading

The primer is a survey written by the Cambridge Digital Minds course team for a general course audience. It has three aims:

1. Introduce five decision-making frameworks that are used in other fields (environmental and health policy, climate science, finance, Bayesian statistics, moral philosophy).
2. Show, for each, what it is useful for and where it is contested.
3. Prompt the learner to test one framework against a digital-minds question, which is Exercise 2.

It answers the question: what established tools exist for making decisions when the facts are uncertain and the moral theory is also uncertain, and what do they add or cost? It is written for readers who may not have a background in statistics or moral philosophy, and it points to external sources (Stanford Encyclopedia of Philosophy, Julia Galef, Khan Academy) for deeper treatment.

## Detailed summary

The primer has six parts, which follow the order of the source.

### Introduction

The primer presents itself as a starting point, not a verdict. It asks the learner to consider what is relevant, what is missing, and whether each framework helps or misleads. It does not recommend any framework for digital minds.

### The EU's guidance on the precautionary principle

The precautionary principle is used in many jurisdictions to guide decisions when science cannot fully assess risks to human health or the environment. The primer summarises the standard dispute. Supporters say it helps prevent harm. Critics say it is vague, leans on cognitive biases, and can slow innovation.

The EU has issued guidelines for applying it, aimed at balancing protection against freedom for individuals and industry. The primer says these guidelines have both critics and proponents but may still offer lessons. The EU asks that any application consider five things:

- **Proportionality.** Measures should be tailored to the chosen level of protection. A total ban is appropriate only if it is proportionate to the risk.
- **Non-discrimination.** Comparable situations should not be treated differently, and different situations should not be treated the same without objective grounds.
- **Consistency.** Measures should match those taken in similar areas where the science is better understood.
- **Costs and benefits.** Compare the short- and long-term costs of acting and of not acting, including economic analysis, effectiveness of each option and public acceptability. The EU text states that protection of health takes precedence over economic considerations.
- **Review against new data.** Assign responsibility for producing new evidence. Usually businesses must prove their products are safe, though this varies by case. Review measures as data arrives and amend them.

The primer cites "Article 6" of the EU guidance for this list. I have not verified that article reference against the EU document.

### The IPCC's guidance on communicating uncertainty

Fields that deal with high uncertainty rely on shared conventions for communicating it. The primer uses the IPCC framework as the example. It is widely used but not applied uniformly, and the course itself mostly does not use it. Two ideas sit at its core.

**Likelihood** is how probable an outcome is thought to be. The IPCC ties each verbal term to a fixed probability band, because people read "likely" and "unlikely" differently:

| Term | Probability |
|---|---|
| Virtually certain | 99-100% |
| Very likely | 90-100% |
| Likely | 66-100% |
| About as likely as not | 33-66% |
| Unlikely | 0-33% |
| Very unlikely | 0-10% |
| Exceptionally unlikely | 0-1% |

The framework also says to flag when one outcome is conditional on another and to factor that in.

**Confidence** is how far a finding or probability estimate can be trusted. The IPCC uses a five-point scale from very low, through low and medium, to high and very high. The grade depends on the quality of the evidence and how well it agrees. The source includes a confidence matrix of evidence and agreement as an image, which the text summary does not reproduce.

### Expected value and utility

Expected value weighs uncertain outcomes by multiplying each outcome by its probability and adding the results. The option with the highest total wins. The primer's example is a ticket that pays £100 with a one-in-a-hundred chance. Its expected value is £1, so a rational buyer pays at most £1.

Expected utility uses the same arithmetic but weighs utility (how good or bad an outcome is) instead of money. The primer says this matters because wellbeing and suffering have no natural price. Utility is meant to put them on a common scale so they can be weighed against each other. The primer ties expected value to finance and expected utility to utilitarian ethics, whose aim is the greatest good overall. It states the formula as Expected utility(A) = sum of P(outcome) x U(outcome).

Three cautions follow:

- The numbers must mean something. Philosophers dispute whether good and bad can sit on one scale, particularly for subjective experience. Deontologists reject utility outright because it treats a person as a means to a total.
- The output is only as good as the inputs. Supporters use Bayesian methods and debiasing to improve estimates and to choose which outcomes count. Critics say this gives a false sense of objectivity on ethical or subjective questions.
- Rare, extreme outcomes can dominate the sum. A tiny probability of an enormous outcome can control the result. The primer points to Nick Bostrom's "Pascal's Mugging" for this problem.

The primer adds that cost-benefit analysis is a close relative that usually uses money as the common unit, which makes it more at home in policy and finance than in ethics.

### Bayesian reasoning

Bayesian reasoning is presented as a foundational method used across many sciences and as a possible model of how the brain processes information. Belief is a probability that moves up or down with evidence, not a yes or no.

The primer describes the procedure in plain terms: start with a prior, then for each piece of evidence ask whether you would expect to see it more if the hypothesis were true than if it were false. Evidence equally likely either way tells you nothing. The size of the shift depends on the ratio of the two likelihoods, called the Bayes factor. Evidence twice as likely under the hypothesis nudges the estimate. Evidence a hundred times as likely moves it sharply.

The medical-test example works as follows. Two tests both have very low false-negative rates. Test 1 has a high false-positive rate and Test 2 a very low one. A positive result from Test 2 should raise the probability of disease more than a positive from Test 1. The prior also matters: if the disease is very rare, a person can still more likely be disease-free even after a positive result from a good test. No numbers are given in the primer.

Bayes' theorem is written as P(H | E) = [P(E | H) x P(H)] / P(E). The primer glosses it as: update based on how expected the evidence is under the hypothesis, relative to how expected it is overall. Evidence tightly tied to the hypothesis moves the estimate more than evidence that would have appeared anyway.

### Approaches to moral uncertainty

The primer separates empirical uncertainty from moral or normative uncertainty, meaning uncertainty about which moral theory (for example consequentialist or deontological) is right, or what it implies. It groups the proposed responses into three families.

**Act on a single theory.** Either follow the theory you trust most ("my favourite theory"), or, on the more radical normative externalism view, act on whichever theory is in fact correct, with moral uncertainty making no difference. The primer's critique of the first is that a theory you rate only slightly less plausible might condemn as a grave wrong the very option your favourite mildly prefers.

**Weigh the theories and combine them.**
- Maximising expected choiceworthiness (MEC) applies expected value to ethics: weight each plausible theory by your confidence and by how strongly it favours each option, then pick the option that does best overall. It inherits the expected-utility problems, including fanatical cases where an improbable theory dominates because it treats stakes as catastrophic. It also assumes theories can be compared on a common scale, which is disputed.
- The Moral Parliament gives each theory seats in proportion to your confidence. The theories vote and bargain, so a theory can concede on what it cares little about in exchange for winning on a serious violation. Rethink Priorities has built a tool based on this. The same comparability dispute applies.

**When combining won't work.** Where the aggregation methods stall, the primer offers simpler rules:
- Acting on convergence: favour actions many theories endorse. It is a heuristic, not a strict rule, because an action can have broad support and still be judged horrendous by one serious theory.
- Maximin: choose the option whose worst-case moral outcome is least bad.
- Dominance: if one option is at least as choiceworthy as another under every theory you take seriously, and better under at least one, prefer it. The rule is silent when neither option dominates.

**Intuitions as a check.** If an argument's conclusion seems clearly wrong, you may reject a premise instead. Intuitions can also check the aggregation methods. If MEC or another rule gives a plainly wrong verdict, that may be grounds to distrust the rule.

**Reflective equilibrium.** The primer names this as the method behind the whole process, associated with John Rawls. You move back and forth between principles and judgements about particular cases, revising each until they agree. No level has a final say. A principle can be dropped when it clashes with a firm conviction, and a judgement can be dropped when it conflicts with principles you trust more. The primer argues that for questions as new as digital minds, where intuitions are untested, this back-and-forth is often how defensible views first emerge.

### Closing

The primer ends with licensing and terms of use from Cambridge Digital Minds. It has no further content.

### Beyond the assigned excerpt

Not applicable. The primer is short and was read in full, so the whole text is the assigned content.

## Techniques & methods explained

- **Precautionary principle (EU form).** Decide under scientific uncertainty about risk, applying five tests: proportionality, non-discrimination, consistency, costs and benefits, and review against new data. Where it fails: it is vague, it can be invoked to block innovation, and critics say it leans on biases. The primer does not say how to weigh the five tests against each other.

- **IPCC likelihood and confidence.** Step 1: state the outcome. Step 2: assign a probability and use the fixed verbal band. Step 3: flag conditional dependencies. Step 4: grade confidence by evidence quality and agreement. Where it fails: it is not applied uniformly, and it converts a probability into words that may still be read inconsistently by different readers.

- **Expected value and expected utility.** Step 1: list outcomes. Step 2: assign probabilities. Step 3: assign values or utilities. Step 4: multiply and sum. Step 5: choose the highest total. Where it fails: utilities may not be comparable, inputs may be biased or arbitrary, and tiny probabilities of huge outcomes can dominate (Pascal's Mugging).

- **Bayesian updating.** Step 1: set a prior. Step 2: estimate how likely the evidence is if the hypothesis is true and if it is false (the Bayes factor). Step 3: multiply the prior by the likelihood and normalise by overall evidence probability. Where it fails: the answer depends on the prior and on the likelihood estimates, which the primer notes can create a false sense of objectivity on ethical questions.

- **Maximising expected choiceworthiness (MEC).** Weight each theory by confidence and by how strongly it favours each option, then pick the best total. Where it fails: theories may not be comparable on one scale, and it can be dominated by low-probability catastrophic verdicts.

- **Moral Parliament.** Assign seats by confidence, let theories vote and bargain. Where it fails: the same comparability problem as MEC, plus the bargaining rules are themselves a design choice.

- **Convergence, maximin and dominance.** Three simpler decision rules for when aggregation stalls. Convergence picks broadly endorsed actions. Maximin minimises the worst case. Dominance prefers an option that is never worse and sometimes better. Each is limited: convergence is only a heuristic, maximin is risk-averse by construction, and dominance is silent when no option dominates.

- **Intuition checks and reflective equilibrium.** Revise principles and case judgements against each other until they cohere. Where it fails: no fixed endpoint, and it depends on which intuitions one trusts.

## Pros, cons & trade-offs it surfaces

| Framework | Strengths (as the primer presents them) | Weaknesses and disputes (as the primer presents them) |
|---|---|---|
| Precautionary principle (EU) | Balances protection with freedom; five explicit tests; allows review as data arrives | Vague; critics say it leans on bias and slows progress; proponents and critics disagree on its use |
| IPCC uncertainty language | Fixed probability bands make verbal terms comparable; confidence is separated from likelihood | Not applied uniformly, and the course does not use it |
| Expected value / utility | Gives a single comparable number; widely understood | Requires a common scale for value and wellbeing; inputs can give false objectivity; rare extreme outcomes can dominate |
| Bayesian reasoning | Structured belief updating; explains why priors and test quality matter | Depends on priors and likelihoods that may be hard to estimate; can give false objectivity on subjective matters |
| Single-theory approaches | Keeps choices consistent | Ignores large stakes under rejected theories; externalism gives no guidance under uncertainty |
| MEC and Moral Parliament | Uses all plausible theories; respects confidence levels | Requires theories to be comparable; fanatical verdicts; bargaining design is arbitrary |
| Convergence, maximin, dominance | Simple; works where aggregation stalls | Convergence is only a heuristic; maximin is cautious to the point of paralysis; dominance rarely decides close cases |
| Reflective equilibrium | Fits new questions where intuitions are untested | No final authority; can settle on views that reflect the reasoner's starting intuitions |

The primer does not rank these. Its overall trade-off is that each tool is useful only if its inputs are defensible.

## Key concepts & terminology

- **Precautionary principle** - guidance for acting under scientific uncertainty about risk, usually to prevent serious harm.
- **Proportionality** - measures should match the level of protection and the risk, with a ban used only where it is proportionate.
- **Likelihood (IPCC)** - how probable an outcome is, expressed with fixed verbal bands.
- **Confidence (IPCC)** - how far a finding or probability estimate can be trusted, graded on evidence quality and agreement.
- **Expected value** - sum of outcomes weighted by their probabilities.
- **Expected utility** - expected value where outcomes are scored by utility (how good or bad) rather than money.
- **Utility** - a measure of how good or bad an outcome is, used to put wellbeing and suffering on a common scale.
- **Cost-benefit analysis** - comparing expected costs and benefits, usually in money.
- **Prior** - an initial estimate of how likely a hypothesis is before evidence.
- **Bayes factor** - the ratio of how likely the evidence is under the hypothesis versus its negation.
- **Bayes' theorem** - the rule for updating a prior with evidence: P(H|E) = P(E|H) x P(H) / P(E).
- **Moral (normative) uncertainty** - uncertainty about which moral theory is right or what it implies.
- **Maximising expected choiceworthiness (MEC)** - aggregating moral theories by confidence-weighted expected value.
- **Moral Parliament** - a method where theories vote in proportion to confidence and bargain.
- **Dominance** - preferring an option that is at least as good under every plausible theory and better under one.
- **Maximin** - choosing the option with the least bad worst case.
- **Reflective equilibrium** - the process of revising principles and case judgements until they agree.

## Evidence, examples & notable data points

- The EU's five tests for applying the precautionary principle: proportionality, non-discrimination, consistency, costs and benefits, and review against new data (EU guidance, as cited in the primer).
- IPCC likelihood bands, for example "likely" = 66-100% and "very unlikely" = 0-10% (IPCC convention, as tabulated in the primer).
- Expected-value example: a ticket paying £100 with a 1-in-100 chance has an expected value of £1 (primer's own example).
- Bayes medical-test example: two tests with equally low false-negative rates but different false-positive rates. The low-false-positive test should move the probability more, and a rare disease can keep a person more likely disease-free even after a positive result (primer's example, no numbers given).
- Bostrom's "Pascal's Mugging" is cited as the standard case of a tiny probability of an enormous outcome dominating an expected-value calculation (primer cites it; I have not read it here).
- Rethink Priorities has built a tool implementing the Moral Parliament idea (primer's claim; the tool itself is not described).
- The primer quotes the EU line that protection of health takes precedence over economic considerations, which it presents as one of the guidance's contested principles.

## Connections

### Within this section

- **Reading 6 (Frameworks for decision making under uncertainty)** is the same document under the Core listing. See [06-frameworks-for-decision-making-under-uncertainty.md](06-frameworks-for-decision-making-under-uncertainty.md). Exercise 2 links to it directly.
- **Reading 2 (The Edge of Sentience)** uses the precautionary principle as the starting point for sentience-based decisions. The primer's EU tests give a concrete version of what "precautionary" must balance. See [02-the-edge-of-sentience.md](02-the-edge-of-sentience.md).
- **Reading 3 (How to deal with risks of AI suffering)** raises suffering risk, which is where the expected-utility concern about rare, extreme outcomes applies most directly. See [03-how-to-deal-with-risks-of-ai-suffering.md](03-how-to-deal-with-risks-of-ai-suffering.md).
- **Reading 4 and reading 11 (Zhou et al., Human-centric framework)** argue for a default of no consciousness and a human-centric approach. Its treatment of risk division is a case of choosing a default under uncertainty. Compare with the primer's point that the defaults you choose set what counts as a cost. See [04-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md](04-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md) and [11-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md](11-a-human-centric-framework-for-debating-the-ethics-of-ai-cons.md).
- **Reading 5 and reading 12 (Claude's Constitution)** are the assigned reading for Exercise 1. Exercise 1 asks about over- and under-attribution of moral patienthood and about "the approaches to uncertainty you've read about this week". This primer is the most direct source for those approaches. See [05-claudes-constitution.md](05-claudes-constitution.md).
- **Reading 8 (Moral Uncertainty, Bykvist)** goes deeper on the moral-uncertainty section of this primer. See [08-moral-uncertainty.md](08-moral-uncertainty.md).
- **Reading 10 (How Extreme is the Precautionary Principle?, Hansson)** tests how far the precautionary principle should be pushed. It is the most useful counterweight to the EU-guidance section. See [10-how-extreme-is-the-precautionary-principle.md](10-how-extreme-is-the-precautionary-principle.md).
- **Reading 7 (The Societal Response to Potentially Sentient AI, Caviola)** is a case of precautionary action on the societal side. See [07-the-societal-response-to-potentially-sentient-ai.md](07-the-societal-response-to-potentially-sentient-ai.md).
- **Reading 13 (Role play with LLMs, Shanahan)** is not a decision framework, but it bears on the "communicate uncertainty" point. Overly anthropomorphic language is itself a confidence problem. See [13-role-play-with-large-language-models.md](13-role-play-with-large-language-models.md).
- **Unit 6 Glossary** defines several of the terms used here. See [01-unit-6-glossary.md](01-unit-6-glossary.md).
- **Section page exercises.** Exercise 1 (Claude's Nature) asks for reasoning about over- and under-attribution, which the primer's tools (expected utility, dominance, intuition checks) can structure. Exercise 2 directly asks the learner to apply one of this primer's five frameworks to digital minds. Its three prompts are what the framework helps clarify, its advantages, and its disadvantages.

### Across the course

The course outline lists eight units. The primer's themes connect to several of them. The mapping below is my reading of the outline's titles, not the course's own cross-references.

- **Unit 1 (Introduction and Theories of Moral Standing).** Expected utility and moral-uncertainty methods assume some theory of what makes a being's welfare count. The primer's point that utility requires a common scale for wellbeing and suffering links to the moral-standing question of whose experiences count at all.
- **Unit 2 (Theories of Consciousness).** Uncertainty about which theory of consciousness is right is structurally the same problem as moral uncertainty. The MEC and Moral Parliament methods could in principle be applied to competing consciousness theories, though the primer does not say so.
- **Unit 3 (Evaluating mental states) and Unit 4 (Perceptions of Consciousness).** The Bayesian section gives a way to update credence in a mental-state attribution as evidence arrives, and the Bayes-factor idea explains why weak evidence should move estimates little. The primer's warning about false objectivity applies to behavioural evidence and to people's perceptions of AI minds.
- **Unit 5 (Interactions with AI Safety and Ethics).** The precautionary principle and the "costs and benefits" test apply directly to AI-safety trade-offs. Review against new data is also relevant to how labs revise commitments.
- **Unit 7 (Digital Minds Governance).** The EU guidance is a worked example of governance under uncertainty, including its proportionality and review requirements. The primer's critics of the precautionary principle (vagueness, innovation costs) are the usual objections to governance proposals.
- **Unit 8 (Reflections and Next Steps).** The primer's closing point, that the frameworks are starting points to test against digital-minds questions, is the kind of self-assessment Unit 8 invites.

**Agreements and tensions.** The primer treats the tools as complementary. The tensions it leaves open are these. Expected-utility methods need numbers that moral philosophy disputes. Precautionary rules are vague and can block innovation. Reflective equilibrium is a method, not a rule, and so does not decide cases. Readings 8 and 10 press these tensions more directly than the primer does.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Scope of "fields".** The course guide promises frameworks and fields with read-across to digital minds. The text covers frameworks well and fields only briefly (finance, utilitarian ethics, neuroscience, climate science). The field-level read-across to digital minds is mostly left to the reader. This is a gap relative to the guide.
- **Identity of the two entries.** Item 14 and reading 6 point to one document with different titles and listings. A learner may think there are two readings. Treat them as one.
- **Dated material.** The EU guidance is from the early 2000s and the IPCC scale is from its assessment reports. I have not checked the current versions. The primer gives the EU article reference without a page link. Before quoting either in a study answer, check the primary document. Today is October 2026, and the course team's date for this primer is 2026.
- **Unverified references.** I have not verified the Bostrom citation, the Rethink Priorities tool, or the Stanford Encyclopedia and Khan Academy pointers. They are presented as pointers and should be treated as such.
- **Probability bands.** The IPCC bands are a convention, not a measurement. Mapping "likely" to 66-100% assumes readers share the convention. The primer raises this but does not test it.
- **Bayes example.** The medical-test example is qualitatively right but has no numbers. A learner who wants to check the claim should compute a case with an explicit base rate. The qualitative claim is standard Bayesian reasoning.
- **Moral Parliament and MEC.** The primer treats comparability as an open dispute. A strong defence of cardinal moral comparison would rebut that doubt, and the primer does not present one. This is an area where the course is neutral rather than confident.
- **Application to digital minds.** The primer is generic. It does not say which framework suits digital minds, and it resists doing so. Its best use is to make learners articulate the premises they are using, which is what Exercise 2 asks.
- **Pushback from other readings.** Hansson (reading 10) argues the precautionary principle can be pushed further than critics allow, but he also warns about its limits. Bykvist (reading 8) treats moral uncertainty in more depth and would press the primer's dismissal of single-theory approaches as too quick, since they remain defensible in some cases. Shanahan (reading 13) would caution against treating an AI's stated uncertainty as its own confidence.

## Discussion questions

1. The primer gives expected value and expected utility as the same calculation with different currencies. What must be true about wellbeing or suffering for the utility version to be meaningful, and which of those conditions do you find most doubtful for digital minds?
2. Pick one of the five frameworks from Exercise 2. What question about digital minds does it help you answer, and what does it force you to assume that you would rather not assume?
3. The primer says rare, extreme outcomes can dominate expected-value sums. Give an example from digital minds where a small probability of a very large harm should, and should not, drive a decision. What rule would you use to decide between the two?
4. How does the Bayesian medical-test example change your view of how much a single piece of evidence about AI sentience should move your estimate? What role does your prior play?
5. The primer says that when aggregation methods stall, simpler rules step in (convergence, maximin, dominance). Which of these would you trust most for an AI welfare decision, and where would it fail?
6. Compare the precautionary principle with Hansson's critique (reading 10). Under what conditions do the five EU tests tell you to act, and what does the "review against new data" test require from AI developers?
7. The primer prefers reflective equilibrium for new questions. Apply it to Exercise 1: which of your starting judgements about Anthropic's commitments would you revise, and which principles would you drop when they conflict with them?
