<!-- source: https://docs.google.com/document/d/1T_9iltxtGx5tN8QX8oRChfHT4UW6lCJMcNH5AqMiIX8/edit?tab=t.0#heading=h.cuighsf9mc3l -->

﻿Frameworks for decision-making under uncertainty

This is a quick overview of some frameworks that may be relevant to approaching questions concerning digital minds, especially questions with no easy or certain answers. We encourage you to use it as a starting point: consider what might be relevant, what we are missing, and how the below may - or may not - inform decision-making around digital minds.


The EU’s guidance on the precautionary principle
The precautionary principle is invoked in many different jurisdictions, to guide decisions when science cannot fully assess risks to human health and the environment. While proponents note its potential utility in preventing harm, critics note that it can be vague, lean on cognitive biases and unnecessarily hinder innovation and progress. 
The EU has set out some guidelines for its application, aiming to balance protection with freedom for individuals and industry. These guidelines - and their application - have critics as well as proponents, but may offer relevant lessons or read-across. The EU asks that any application of the precautionary principle consider five things (see Article 6 here):
* Proportionality. ‘Tailoring measures to the chosen level of protection’, for instance a total ban only where that is proportional to the risk.
* Non-discrimination. ‘Comparable situations should not be treated differently’ and ‘different situations should not be treated in the same way, unless there are objective grounds for doing so’.
* Consistency. Measures should match those taken in similar areas where the science is better understood.
* Costs and benefits. Compare the long-and short-term costs of acting or not acting, including economic analysis, how effective each option is, and public acceptability. ‘Protection of health takes precedence over economic considerations’.
* Review against new data. Assign responsibility for producing new evidence. Usually businesses must prove their products are safe, though this varies case by case. Review measures as data arrives and amend them if needed.


The Intergovernmental Panel on Climate Change’s guidance on communicating uncertainty (IPCC)
Fields that deal with high uncertainty rely on shared conventions to communicate it. The IPCC’s framework is widely used, though it isn’t applied uniformly (and - to avoid confusion - most of this course doesn’t use it either). Two ideas sit at its core, likelihood and confidence.
Likelihood. How probable an outcome is thought to be. Because people read words like ‘likely’ and ‘unlikely’ very differently, the IPCC ties each term to a fixed probability band.
Term
	Probability
	Virtually certain
	99–100%
	Very likely
	90–100%
	Likely
	66–100%
	About as likely as not
	33–66%
	Unlikely
	0–33%
	Very unlikely
	0–10%
	Exceptionally unlikely
	0–1%
	It also recommends flagging when one outcome is conditional on another, and factoring that into the assessment.
Confidence. How much we can trust a finding, or trust that a probability estimate is right. The IPCC grades this on a five-point scale, from ‘very low’ through ‘low’, ‘medium’, ‘high’, to ‘very high’, based on the quality of the evidence and how well it agrees.
 IPCC confidence matrix of evidence and agreement 

Expected value and utility
Expected value is a way of weighing possible outcomes under uncertainty. You take each possible outcome, multiply it by the chance it happens, and add the results up. The option with the highest total is the one to take. A lottery ticket that pays £100 on a one in a hundred chance has an expected value of £1, so a rational buyer pays no more than £1 for it.
Expected utility works the same way, but it weighs utility - a measure of how good or bad an outcome is - rather than a dollar amount. The swap is important because the things we care about most, such as a being's wellbeing or suffering, have no natural price. Utility aims to put them on a common scale, so they can still be weighed against each other. This is the language of utilitarian ethics, where the aim is the greatest good overall. Expected value is at home in finance, expected utility in utilitarian ethics.
The calculation is the same in both cases. For each outcome, multiply how likely it is by how much utility or value it carries, then add those up across all the outcomes, so: 

(chance of A × utility of A) + (chance of B × utility of B), and so on. 

Written compactly, that is Expected utility (A) = Σ P(outcome) × U(outcome).
Three things are worth keeping in mind when using it.
* The numbers have to mean something. Philosophers dispute whether 'good' and 'bad' can sit on a single scale at all, especially for subjective experiences. Some, such as deontologists, reject utility outright, arguing it treats a person as a means to a larger total rather than as an end in themselves.
* The answer is only as good as the inputs. Supporters use Bayesian methods and debiasing to reach better numbers, and to select which outcomes are weighed in the process. Critics warn that this can give a false air of objectivity, particularly when applied to subjective or ethical matters. 
* Rare, extreme outcomes can swamp the sum. A tiny probability of an enormous outcome can dominate the result. This causes problems as Nick Bostrom sets out in 'Pascal's Mugging'.
For a fuller philosophical treatment, see the Stanford Encyclopedia of Philosophy entry.
Cost-benefit analysis is a close cousin of this approach. It weighs options by their expected costs and benefits. Often, this method uses money as the common unit, which can make it more at home in policy and finance than in ethics.
Bayesian reasoning
Bayesian reasoning is a foundational method for reasoning under uncertainty, used across many fields of scientific study, and proposed as a model of how the brain itself processes information. Rather than treating belief as all or nothing, it treats belief as a probability that slides up or down in response to evidence.
At its simplest, it is a structured way of changing your mind when new evidence arrives. You start with a prior, your initial estimate of how likely something is to be true. Then, for each new piece of evidence, you ask whether you would expect to see it more if the hypothesis were true than if it were false.  If a piece of evidence is equally likely either way, it tells you nothing and your estimate stays put. How far your estimate moves depends on how lopsided the comparison is. Evidence twice as likely if the hypothesis is true as if it is false nudges your estimate, while evidence a hundred times as likely moves it sharply. This ratio between the two likelihoods is sometimes called the Bayes factor.
Consider diagnostic tests in medicine. A person tests positive for a disease - do they really have the disease? A Bayesian would consider how good the test is - that is, its false positive rate (how many disease-free people wrongly test positive for the disease) and its false negative rate (how many people with the disease wrongly test negative for it). Let’s imagine two tests - we’ll assume that each has a very low false negative rate. Test 1 has a very high false positive rate (many people testing positive when they do not in fact have the disease). Test 2 has a very low false positive rate. A positive result from Test 2 should increase the probability we place on the person having the disease by more than Test 1 - as Test 1 has a greater likelihood of giving a positive test result to people who do not have the disease. The prior probability matters a lot in both cases - if the disease is extremely rare, being disease-free can be the more likely outcome, even if a person receives a positive result from a good test. 
The relationship is captured by Bayes' theorem.
P(H | E) = [ P(E | H) × P(H) ] / P(E)
In words, how likely the hypothesis is given the evidence equals how likely the evidence would be if the hypothesis were true, multiplied by your prior (or how likely you thought the hypothesis was before) and then divided by how likely the evidence was overall. We update based on how expected the evidence is if the hypothesis is true, relative to how expected it is overall - so evidence tightly tied to the hypothesis moves the estimate further than evidence that would probably have appeared anyway.
For an introduction, see Julia Galef's video. For a philosophical treatment, see the Stanford Encyclopedia of Philosophy. For an accessible approach to the calculations, see Khan Academy.
Approaches to moral uncertainty

Settling the empirical facts - or increasing our confidence in our probability estimates - is only half the problem. We can also be unsure of the right moral implications to draw or which moral theory (e.g. consequentialist or deontological approaches) we ought to use to figure this out. This is moral, or normative, uncertainty. Philosophers have suggested different ways of handling it, which fall into three broad strategies.
Act on a single theory
The simplest response is not to weigh theories against each other at all.
* My favourite theory. Follow the single moral theory you have most confidence in and set the rest aside. Its defenders argue this keeps your choices consistent without forcing comparisons between theories. Critics object that it ignores how much can be at stake under the theories you set aside, since a theory you find only slightly less plausible might condemn as a grave wrong the very option your favourite theory only mildly prefers.
* Externalism. A more radical view, normative externalism, holds that moral uncertainty should make no difference at all, and that you ought simply to act in accordance with whichever theory is in fact correct. 
Weigh the theories and combine them
A second family treats your confidence in each theory as a weight and pools their verdicts.
* Maximising expected choiceworthiness (MEC). This applies the logic of expected value to ethics. You take every theory you find plausible, weight each by your confidence in it and by how strongly it favours an option, and pick what does best across all of them at once. However, philosophers dispute whether theories can be compared on a common scale as MEC requires.  In addition, this calculation can suffer from a similar problem to expected utility: you might find a theory very unlikely, but this theory may dominate the result if it treats the stakes as catastrophic. What should be done in these fanatical cases is itself contested.
* The Moral Parliament. Imagine each theory holding seats in proportion to your confidence in it. The theories vote and can bargain, one conceding on an issue it cares little about to prevail on something it counts a serious violation. Rethink Priorities has built a tool which applies this. Again, though, philosophers dispute whether the theories are comparable enough to vote and bargain against one another.
When combining the theories won't work
As above, there are difficulties with comparing different theories on a common scale. Where the combining methods stall, simpler rules can step in.
* Acting on convergence. As a rule of thumb, favour actions that many moral theories endorse, which sidesteps the need to choose between them. It works best as a heuristic rather than a strict rule, since several actions can each command broad agreement while one of them is still judged horrendous by a theory you take seriously.
* Maximin. Pick the option whose worst-case moral outcome is least bad.
* Dominance. If one option is at least as choiceworthy as another under every theory you take seriously, and better under at least one, prefer it. The rule only sorts options it can compare this way, and stays silent when neither dominates the other.
Intuitions as a check
When an argument leads somewhere that seems clearly wrong, you may treat that as reason to reject one of its premises rather than accept the conclusion. Intuitions can be a check on the methods above too. If MEC or another aggregation rule delivers a verdict that seems plainly wrong, that may be reason to distrust it.

The method behind this process of deliberation is reflective equilibrium, associated with John Rawls, which works back and forth between your principles and your judgements about particular cases, revising each until they agree. Here, no perspective has a final say, so a principle can be dropped when it clashes with a firm conviction, and a particular judgement given up when it conflicts with principles you trust more. For questions as new as digital minds, where intuitions are untested and no single theory commands confidence, this back-and-forth is often how defensible views first get developed.

________________




These materials are released under a Creative Commons BY-NC-ND licence with the following Terms of Use: Cambridge Digital Minds (CDM) is the sole authoritative provider of this course; these materials do not confer any credential or certification unless completed through CDM; reproducing the CDM name/logo in a way that implies organisational affiliation is not permitted.