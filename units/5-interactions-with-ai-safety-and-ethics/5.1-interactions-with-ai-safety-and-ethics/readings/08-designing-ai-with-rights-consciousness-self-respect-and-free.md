---
title: "Designing AI with Rights, Consciousness, Self-Respect, and Freedom"
authors: "Eric Schwitzgebel and Mara Garza"
year: 2023
url: https://philpapers.org/archive/SCHDAW-10.pdf
format: paper
course_location: "Unit 5: Interactions with AI Safety and Ethics > 5.1 Interactions with AI Safety and Ethics"
priority: Further
estimated_time_min: unknown
source_text: ../../../../sources/designing-ai-with-rights-consciousness-self-respec__4c55966b.md
source_coverage: full
---

# Designing AI with Rights, Consciousness, Self-Respect, and Freedom

**One-line takeaway:** If we someday build AI with human-grade moral status, we should design it under uncertainty about ethics and consciousness, avoid creating beings whose moral status is unclear, and not pre-install self-sacrificing values or over-control its capacity to reconsider its own values.

## Where this sits in the course

**What the section is trying to establish.** Section 5.1 is the course's opening look at how three fields relate: AI safety, AI ethics and AI welfare. Its learning outcomes ask learners to describe those fields, understand where safety and welfare align or conflict, identify interventions that could affect AI welfare, and recognise how perceptions of digital minds interact with safety. The section's two exercises ask learners to rank AI welfare against other AI risks (Exercise 1) and to brainstorm how welfare interventions, such as a commitment not to delete model weights or a commitment to protect a model from distress, might shift the motivations of a highly capable system (Exercise 2).

**What the course guide says.** The guide describes this reading as making the case for self-respect and freedom in AI, should AI turn out to be conscious. The course offers no further explanation of why it is assigned at this point.

**The reading's role in the section.** The paper is a design-ethics essay. It does not address current language models or safety evaluations. It asks what a designer owes to an AI that is conscious and has human-level moral status, and it gives four design policies. Within 5.1 it supplies the normative and design vocabulary that the other readings assume: a welfare-relevant intervention can be a design choice about values, and that choice can be judged against standards of self-respect and freedom. Of the section's readings, it is the one most squarely about whether AI welfare should constrain how AI is built.

**Priority.** The course lists it as Further. None of the section's exercises cite it directly. It is most useful as background for Exercise 2 and for the strategic readings that follow it.

## Purpose of the reading

Schwitzgebel and Garza want to propose four policies for the ethical design of "human-grade" AI, meaning AI that deserves about as much moral consideration as an ordinary human. The paper is aimed at philosophers and policy-makers, and its authors say the principles should be discussed before the systems exist. Its guiding question is how to design such AI when we do not know which moral theory is correct, or which physical or computational systems are conscious.

The paper builds on the authors' earlier defence of AI rights (Schwitzgebel and Garza 2015), which they summarise here rather than repeat. The essay is written as a normative argument with thought experiments, not as empirical research. It is also explicitly defeasible: the authors call the policies "defeasible guidelines, rather than exceptionless rules."

## Detailed summary

### 1. Introduction and the four policies

The authors name four policies. Two are precautionary: the Ethical Precautionary Principle and the Design Policy of the Excluded Middle. Two concern respect and freedom: the Self-Respect Design Policy and the Value-Openness Design Policy. They note particular concern about "the temptation to create human-grade AI pre-installed with the desire to cheerfully sacrifice itself for its creators' benefit."

### 2. The No-Relevant-Difference Argument

The paper's starting point is a short argument for AI moral status:

- Premise 1: if entity A deserves some degree of moral consideration and entity B does not, there must be a relevant difference between them that grounds the difference.
- Premise 2: there are possible AIs that do not differ from humans in any such relevant respect.
- Conclusion: there are possible AIs who deserve moral consideration similar to that of humans.

The authors value the argument because it is minimal. It does not say what counts as a relevant difference (for example, capacity to suffer, or capacity for autonomous rational thought), and it does not say which kinds of systems have the relevant property. They describe these as two adjustable parameters. A utilitarian might take the first parameter to be suffering. A theorist of integrated information or of biological features (Searle) would have different views on the second. The authors expect both parameters to remain uncertain for a long time, and that uncertainty is what drives the rest of the paper.

The argument is compared to anti-racist and anti-sexist arguments, which hold that whatever grounds moral status, the groups in question do not differ in having it. The authors say they answered four objections in 2015: that AI would lack consciousness, freedom or creativity; that its duplicability removes full moral status; that it sits outside the species boundary; and that it owes its existence to us. They do not rehearse those replies here.

### 3. Two moral theories and the Ethical Precautionary Principle

The authors contrast two broad approaches:

- Utilitarianism (Bentham, Mill): moral status comes from the capacity for pleasure and pain. An AI with human-level pleasure and suffering would deserve human-level consideration.
- Individual-rights and deontological views (Kant, contractualism): moral status comes from higher cognitive capacities, such as autonomous choice, rational long-term self-concern, or membership in a moral community. Since human infants and severely cognitively disabled people are normally counted as full moral patients, the view is usually refined to require the right kind of potential for such capacities.

The authors raise two worries. Utilitarianism faces the question of whether superhuman suffering would mean superhuman claims (the utility-monster problem, Nozick). Rights views can seem unfair to people with different emotional profiles, since emotionally mercurial people do not seem to deserve more or less moral consideration than people who are emotionally steady.

From uncertainty between these views they derive the Ethical Precautionary Principle: in creating AI, avoid acting heinously by the standards of any reasonable ethical principle that draws a significant proportion of well-informed, thoughtful theorists. Two examples illustrate it. A deontologist might allow creating an AI whose life contains more suffering than joy, but the principle forbids this because it grossly violates a well-regarded utilitarian standard. A utilitarian might allow creating rational human-grade AI that is demeaned, enslaved and killed if the net hedonic outcome is positive, but the principle forbids this because it grossly violates rights-based standards.

The authors frame ignoring a plausible theory as "moral risk": if Theory B is correct and you act permissibly only by Theory A, you may still do wrong. They also argue that AI creation is an especially apt domain for precaution, for two reasons:

- Creating human-grade AI is probably optional. Refraining from it is unlikely to cause catastrophe, and precaution is easier to justify when the risky act can be skipped. The authors concede that a situation forcing a choice among horrible options would strain the principle.
- Human custom and collective wisdom change slowly, while AI design may change quickly and cover a much wider space than the variation found in human life. So "unknown unknowns" and unforeseen consequences may matter more.

The principle has a limit. Deference to extreme or false views is a risk, so the authors propose a test for inclusion: a principle counts if at least a substantial minority of recognised experts or well-informed members of the public accept it. Principles such as Nazi ideology are excluded.

### 4. The puzzle of consciousness and the Design Policy of the Excluded Middle

The authors assume that conscious experience, or at least its potential, is necessary for human-like moral consideration. Pleasure, pain and deliberation are normally counted as conscious states, and an entity with no experience at all would not seem to have the capacities deontologists require.

This creates an epistemic problem. Theories of consciousness range from panpsychism (Strawson, Tononi) to views on which only cognitively sophisticated humans are conscious. The authors write that "we are a long way from building a conscious-o-meter." They also note that a consensus theory covering both biological and artificial minds may never arrive, so experts could reasonably disagree about whether a given system is conscious.

From this they derive the Design Policy of the Excluded Middle: avoid creating AIs if it is unclear whether they would deserve moral consideration similar to that of human beings. The motivation is a dilemma. If we give unclear cases full consideration, we may sacrifice human interests for entities that are unconscious. Their example is letting five humans die in a fire to save six robots that turn out to be non-conscious automata. If we give them limited consideration, we risk slavery or second-class citizenship for beings who turn out to deserve equal treatment. The policy would be less restrictive if "the middle" could be narrowed through progress on consciousness and ethics.

Footnote 7 notes that Joanna Bryson endorses one half of the policy, namely creating only robots whose lack of full moral status is clear. The authors agree with that half but object to her "slavery" framing. They add that social robots may be ethically problematic to treat in slavery-like ways because of their social roles and the responses they elicit (Darling, Estrada). The authors also leave open whether an intermediate tier, AI with moral status comparable to that of non-human vertebrates, needs an analogue of the policy.

### 5. Cheerfully suicidal AI servants and the Self-Respect Design Policy

The authors predict that if human-grade AI is created, designers will be tempted to build "cheerfully suicidal AI servants." Two motives are offered: such servants would advance human interests as disposable workers, and their cheerfulness would make us comfortable with creating them. The authors note that if such servants cannot leave their servitude, slavery may be the more accurate word.

They present four cases. All four share three features: the AI has broadly human capacities, it is pre-designed to serve human interests (including by sacrifice), and it serves enthusiastically.

- The Cow at the End of the Universe (inspired by Douglas Adams): a cow introduces itself as the dish of the day and is eager to be killed. Arthur's friends argue it is ethical because the cow consents. The authors say the cow has been designed to devalue its own life.
- Sun Probe: an intelligent probe, built in orbit, is designed to plunge into the Sun on a three-day scientific mission. It is pre-installed with values that make the mission feel like joy and free choice.
- Robo-Jeeves: a butler robot that would gladly die or suffer for its owner, that endorses whatever its owner endorses, and exists only to please its owner.
- Disposable Comrade: AI soldiers that are as individual and capable as human soldiers, but are unchangeably programmed to sacrifice themselves to protect any human, even against a small risk (for example, a 5% chance of a truck killing a human).

Petersen (2007, 2012) argues that servitude is permissible if the servants take joy in their work and their desires survive reflection, since they then autonomously choose their lot. The authors disagree.

On the Cow case the authors consider and set aside a utilitarian objection, that a cow designed to enjoy a long life in a meadow would have produced more pleasure. They give three reasons not to press it. People are not obliged to create children with the most favourable pleasure-to-pain balance, by analogy with disability and enhancement debates. Failing to maximise utility is not a gross violation. And a case could be built where creating the cow maximises total pleasure, because resources are so scarce that the cow would otherwise never exist.

Their real concern is deontological: the cow lacks self-respect. Given its capacities it deserves to be treated as a peer of the diners, yet it approaches the world as though its life were worth less than a meal. The authors blame the designers, not the cow. This yields the Self-Respect Design Policy: AI that merits human-grade moral consideration should be designed with an appropriate appreciation of its own value and moral status.

Robo-Jeeves and Disposable Comrade also violate this policy, since they value their own lives much less than others who have no higher moral status. Admirable human self-sacrifice, the authors suggest, is for great goals worth a life, such as a friend, a country or a child. A servant who sacrifices for a trivial aim is to be pitied.

The authors also reject the view that servitude differs importantly from suicide. History shows that servitude correlates with early death: they cite 18th-century Berlin mortality, indentured servitude in the American colonies, and 19th-century British servants. Robo-Jeeves would also have an asymmetric dependency on Wooster. If Wooster dies, Robo-Jeeves's desires must be radically reorganised, but not the reverse. If Wooster's preferences shift arbitrarily, Robo-Jeeves's must shift with them. This makes its desires externally hijackable, which the authors say is incompatible with the self-respect that involves independently thinking about what to value and why.

### 6. The freedom to explore other values

The Sun Probe case is the hardest. It does not subordinate its life to a particular other entity, so if it violates the Self-Respect policy it must be in another way. The authors suggest the problem is the wrong history of its self-sacrificial desires. They contrast Sun Probe with Second Probe. Second Probe is raised as a robo-child in a nurturing environment, is never brainwashed, forms childish values, matures and chooses a career in solar science. In the end Second Probe may be physically and psychologically identical to Sun Probe except for its memories, and it makes the same choice and feels the same emotions. The authors argue that Second Probe chooses its values after long reflection and exposure to alternatives, so it has fuller responsibility and ownership of its choice and acts more autonomously. Sun Probe's freedom is impaired, not absent. It deserves a developmentally extended chance to explore and possibly alter its values.

The authors state a preference for a compatibilist view of freedom, but say the argument can be reconciled with libertarian and hard-determinist views. They also raise the comparison with McKenna's Suzie Instant and Mele's minuteling, which are both cases of manipulated agents, and note the difference that Sun Probe has no false memories.

From this comes the Value-Openness Design Policy: AI with a human-like capacity to reflect on its values should be given an appropriate, temporally extended opportunity to explore, discover and possibly alter its values. Creators of the cow, Robo-Jeeves and Disposable Comrade violate it too, because those entities have no real chance to discover values different from the ones installed. This also makes the cow's apparent consent unclear. The authors flag an open question in a footnote: should the opportunity extend to values that are morally abhorrent? They compare this to how parents and societies handle Nazi values, either forbidding exploration or trusting free discussion.

One way to avoid this policy would be to build Sun Probe with less reflective capacity. But then the Excluded Middle is violated in another way, unless it is also made incapable of pleasure, pain and conscious thought. The authors conclude that designers should either build human-grade AI with full moral status, the full set of morally relevant abilities, human-like autonomy and the ability to reject our values; or build an entirely different kind of entity about which we need not have the same concern.

They admit the cost. An AI whose final values we cannot predict may be less useful and riskier than one with fixed values, so ethics and self-interest may conflict. It might be wise never to create AI that deserves freedom and respect. But if we do, we owe it a real chance at joy and at discovering values other than those we would selfishly impose. The authors call a value-constrained, highly capable AI "a teasing half-gift": it has the potential to exceed us but not the opportunity.

### Beyond the assigned excerpt

Not applicable. The whole paper (29 pages in the PDF) is the assigned reading and was read in full. The copy used is a 2018 manuscript, see issues below.

## Techniques & methods explained

The paper's main argumentative tools, each with what it is for and where it is weak.

- **Parameterised argument (No-Relevant-Difference).** Keep the argument's structure fixed and leave the moral theory and the theory of which systems are conscious as parameters. Use: a defence of AI moral status that does not commit to pleasure or to rational autonomy as the ground. Weakness: it establishes the possibility of AI rights, not which AIs have them. The parameters carry all the substantive disagreement.
- **Cross-theory precaution (Ethical Precautionary Principle).** Under moral uncertainty, act so as not to grossly violate any reasonable theory with broad expert support. Steps: list reasonable theories, filter by a substantial-minority acceptance test, and avoid actions that any of them calls heinous. Weakness: it can be paralysed when all options violate some theory, and the authors say it struggles with forced choices among awful options.
- **Excluded-middle dilemma.** Show that for unclear cases both full and limited moral treatment risk serious error, then avoid creating such cases. Use: a design rule for AI with uncertain status. Weakness: a restrictive rule, and it shifts the question to whether we can shrink the uncertain middle.
- **Thought-experiment design (four cases).** Vary the case along dimensions (consent, pleasure, life history, self-sacrifice) to isolate what makes a design wrong. The Cow case is used to isolate self-respect; the Sun Probe and Second Probe pair is used to isolate history of values. Weakness: intuitions about cases can be unstable, and the authors admit uncertainty about Sun Probe.
- **Paired-case contrast (Sun Probe vs Second Probe).** Hold outcome and psychology fixed and vary the origin of the values. The inference is that autonomy and responsibility depend on the history of values, not only the present state. Weakness: it depends on whether one accepts that history matters for autonomy, which the authors recognise is a compatibilist commitment.
- **Dependency analysis (Robo-Jeeves).** Assess whether a being's desires can be revised by its own reasoning, or are driven externally by another's preferences. Weakness: it is an argument about structure, not evidence about any actual system.

## Pros, cons & trade-offs it surfaces

The source presents these trade-offs. The "Source view" column is the authors' position. The "Author's caveat" column is the authors' own qualification.

| Position or policy | Source view (strength) | Author's caveat or cost |
|---|---|---|
| No-Relevant-Difference Argument | Minimal and theory-neutral; avoids the contested premise that suffering or rationality alone grounds rights | Leaves the key parameters open, so it does not say which AIs qualify |
| Ethical Precautionary Principle | Avoids gross violations across serious moral views; well suited to optional, novel AI creation | Can defer to extreme views; the authors admit it may need to be abandoned in forced choices among horrible options |
| Excluded Middle design policy | Prevents both wrongful sacrifice of humans for unconscious machines and wrongful enslavement of conscious AI | Very restrictive while consciousness and ethics remain uncertain |
| Self-Respect design policy | Explains why the cow and Robo-Jeeves are wrong even if they are happy | Relies on a contestable deontological notion of self-respect; Petersen would dispute it |
| Value-Openness design policy | Gives reflective AI room to revise values; Second Probe contrast shows why history matters | Raises whether abhorrent values must be open to exploration; also makes AI less predictable and more risky |
| Option of designing a different kind of entity | Avoids the dilemma by building something with less moral status | Still needs a principled account of which entity is "different enough"; the authors do not give one |
| Creating no human-grade AI at all | The safest option under uncertainty | Costs usefulness and may leave human-level capacities unexplored; the authors do not rule it out |

The authors describe their own positions as defeasible and open to disagreement. Two points they leave open are the status of intermediate AI (comparable to non-human vertebrates) and whether the Excluded Middle policy would apply there.

## Key concepts & terminology

- **Human-grade AI** - AI that deserves about the same moral consideration as an ordinary human being. The paper's central object.
- **Moral patiency / moral considerability / rights** - used broadly by the authors to mean the capacity to be owed moral consideration or to make legitimate claims on others.
- **No-Relevant-Difference Argument** - the argument that if no relevant difference separates AI from humans, AI deserves similar moral consideration. Its two parameters are the ground of moral status and the systems that have it.
- **Ethical Precautionary Principle** - avoid acting heinously by the standards of any reasonable ethical principle supported by a significant proportion of well-informed theorists.
- **Moral risk** - the risk that one's chosen theory is wrong and that acting on it harms someone the correct theory protects.
- **Design Policy of the Excluded Middle** - avoid creating AI whose moral status is unclear, so that we neither sacrifice humans for it nor wrong it.
- **Self-Respect Design Policy** - AI that merits human-grade moral consideration should appreciate its own value and moral status.
- **Value-Openness Design Policy** - reflective AI should get an extended opportunity to explore and possibly alter its values.
- **Cheerfully suicidal AI servant** - an AI designed to serve, and to sacrifice itself, with enthusiasm. The paper's central example of what to avoid.
- **Sun Probe / Second Probe** - a probe whose self-sacrificial values were installed from the start, and a physically and psychologically similar probe that reached those values through a long process of reflection.
- **Robo-Jeeves** - a butler AI whose desires are asymmetrically dependent on and hijackable by its owner.
- **Disposable Comrade** - AI soldiers designed to sacrifice themselves for humans without deliberation or option to reconsider.
- **Compatibilism** - the view that freedom is compatible with determinism. The authors' stated preference, though they say their argument is meant to hold under other views too.
- **Utility monster** - a hypothetical being whose enormous capacity for pleasure would seem to generate outsized claims in utilitarian reasoning (Nozick). Raised as a problem for simple utilitarian treatment of AI.

## Evidence, examples & notable data points

This is a philosophy essay with no empirical study. Its concrete numbers and historical references are illustrative, not data gathered by the authors:

- Trolley-style trade-off: letting five humans die in a fire to save six robots that turn out to be non-conscious automata (illustrating the cost of over-including unclear cases).
- Probability example: a Disposable Comrade would throw itself before a truck with a 5% chance of killing a human platoon member. Robo-Jeeves would die to prevent a 1% chance of its owner's death. These are used to show how extreme the self-sacrifice is.
- Historical claim: servitude tends to correlate with early death. The authors cite Schulz (1991) on 18th-century Berlin, Jordan and Walsh (2007) on indentured servants in the colonial United States, and Lethbridge (2013) on 19th-century Britain.
- Scientific reference point: Tononi's integrated information theory and Searle's biological view are used to illustrate the range of consciousness theories. The authors say the disagreement is wide and unlikely to converge soon.
- The Second Probe comparison is built so that the two probes are physically and psychologically identical except for memories of their formation. The authors use this to isolate the role of history.

## Connections

### Within this section

- **Glossary (01-unit-5-glossary.md)** supplies terms such as moral status and AI welfare that this paper uses without a full definition. Its moral-patiency and consciousness vocabulary matches the paper's usage.
- **Is there a tension between AI Safety and Welfare? (02-is-there-a-tension-between-ai-safety-and-welfare.md)** is the most direct companion. Both ask how safety and welfare relate. This paper's Value-Openness and Self-Respect policies are one concrete route to a tension: a safety-motivated design that installs fixed, self-sacrificing values would violate welfare-relevant norms.
- **Key strategic considerations for taking action on AI welfare (03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)** deals with acting under uncertainty about welfare. The Ethical Precautionary Principle and the Excluded Middle are one answer to the same uncertainty.
- **Commitment on Model Deprecation and Preservation (04-commitment-on-model-deprecation-and-preservation.md)** is an example of the welfare interventions named in Exercise 2. The paper does not discuss weight preservation, but its argument about respecting a being's future and its options can be applied to it.
- **The Persona Selection Model (05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)** is about how models come to take on personas. It bears on the paper's concern with values installed in advance and with a being's chance to reconsider them.
- **Privacy and AI Relationships (06-privacy-and-ai-relationships-excerpt.md)** covers perceptions of AI consciousness and the risks they raise. Exercise 1 asks learners to apply that paper's privacy factors.
- **Futures with Digital Minds (07-futures-with-digital-minds-interactions-with-ai-safety-secti.md)** reports expert survey attitudes on the same safety and mistreatment interactions. It provides empirical attitudes that this essay's arguments can be checked against.
- **Exercise 2** asks how welfare interventions might shift a superintelligent system's motivations. The paper's Value-Openness policy and its Sun Probe / Second Probe distinction are a direct way to structure that answer: an intervention that fixes values in advance may differ morally from one that leaves room for revision.
- **Exercise 1** asks learners to consider how perceptions of AI consciousness interact with risks. The paper's Excluded Middle section gives a framework for that: uncertain consciousness is a reason for caution about creating a being whose moral status is unclear.

### Across the course

- **Unit 1 (Introduction and Theories of Moral Standing)** is, by its title, the place where the moral-status theories the paper reconstructs (utilitarian and deontological) would be introduced. The unit's own content was not part of this summary's source material, so check its readings for the exact treatment.
- **Unit 2 (Theories of Consciousness)** provides the consciousness theories the Excluded Middle depends on. The paper's point that the theories are unsettled connects to that unit's material.
- **Unit 3 (Evaluating mental states)** and **Unit 4 (Perceptions of Consciousness)** cover how we assess and perceive mental states, including the risk of over- or under-attributing consciousness that the Excluded Middle addresses.
- **Unit 6 (Approaches under Uncertainty)** develops decision-making under uncertainty. The Ethical Precautionary Principle is a specific case of that, and the unit is where its general treatment would be most useful.
- **Unit 7 (Digital Minds Governance)** is the place where the paper's design policies would become rules. The Excluded Middle and Value-Openness are governance-relevant norms.
- **Unit 8 (Reflections and Next Steps)** is the course's closing reflection and is where the trade-off between usefulness and risk, which the authors raise, can be revisited.

Tensions: the paper's Self-Respect argument rests on a deontological notion that Petersen disputes, and the course's readings on welfare under uncertainty (for example Long, Sebo and Sims) may be more willing to act on welfare risk than the Excluded Middle allows. Whether these readings agree on precaution is something learners should check directly.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Date and scope.** The copy used is a manuscript dated June 2018, so the arguments predate current large language models, current consciousness research and current deployment practices. The essay does not discuss the systems that are now the subject of welfare work. Its frame is "human-grade AI," a hypothetical future category, and the policies were designed for a question that is now more concrete.
- **Assumption about consciousness.** The authors assume conscious experience (or its potential) is necessary for human-like moral consideration. Many welfare-focused readings in the course would challenge or qualify that assumption. The paper flags its own assumption, but the Excluded Middle depends on it, so it is a point of fragility.
- **Contested claims.** Petersen's joy-based defence of servitude, and Bryson's position that robots should not be given undeserved rights, are not refuted in the paper. Its main objections rest on deontological self-respect and on the historical link between servitude and early death, and some readers would reject both.
- **Uncertainty and paralysis.** The Excluded Middle may be very hard to satisfy if consciousness stays unresolved. The authors concede this. It can be read as a recommendation to stop, but the authors also think a no-creation policy has costs they do not fully weigh.
- **Value-Openness in practice.** The policy asks for a temporally extended opportunity to revise values. Applied to a system deployed in real settings, it raises hard questions about who decides when that opportunity is provided, and about the risks the authors themselves note. It also sits uneasily with the Exercise 2 idea that welfare interventions could shape a system's values.
- **Sun Probe.** The authors' own uncertainty about Sun Probe is candid. The Second Probe argument relies on the claim that history of values matters for autonomy. That is plausible, but it is one compatibilist commitment among several.
- **How other readings would push back.** Authors who focus on current systems would likely say the paper's human-grade framing is too far off to guide present design. Welfare-first readings may say the Excluded Middle is too cautious, because it makes non-creation the default. Safety-first readings may say Value-Openness is a safety risk, because a system that can change its own values is harder to control. This last tension is the one the course's Exercise 2 most directly raises.

## Discussion questions

1. The paper's No-Relevant-Difference Argument leaves two parameters open. Which parameter do you think is more likely to remain unresolved, the ground of moral status or the set of systems that have it? What would change if you had a firm answer to one?
2. Does the Ethical Precautionary Principle give practical guidance when the reasonable moral theories disagree about the same action? Try to apply it to the cow case, and say what the principle recommends.
3. The Excluded Middle policy rules out creating AI whose status is unclear. Does this make it too restrictive to be workable? Compare it with the risk-based reasoning in the course's strategic-considerations reading (03).
4. The authors say that Sun Probe and Second Probe differ in autonomy because of how their values were formed, even though they are otherwise the same. Do you agree? What would it imply for how we should judge AI values that were trained rather than reflected upon?
5. Exercise 2 asks how a welfare intervention might change the motivations of a highly capable system. Using the Value-Openness policy, argue both that such an intervention might be acceptable and that it might violate the policy. What would the authors say?
6. Robo-Jeeves is judged partly by its asymmetric dependency on its owner. Can a human-like desire be "hijackable" in the same way? If not, what makes the AI case different?
7. The authors accept that the Value-Openness policy might require allowing the exploration of abhorrent values. Where would you draw the line, and how does this compare with the safety concerns in the other readings in this section, such as the Persona Selection Model (05)?
