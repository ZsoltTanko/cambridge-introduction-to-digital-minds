---
title: "AI alignment vs AI ethical treatment: Ten challenges"
authors: "Adam Bradley & Bradford Saad"
year: 2024
url: https://www.globalprioritiesinstitute.org/wp-content/uploads/Bradley-and-Saad-AI-alignment-vs-AI-ethical-treatment_-Ten-challenges.pdf
format: paper
course_location: "Unit 5: Interactions with AI Safety and Ethics > 5.1 Interactions with AI Safety and Ethics"
priority: Further
estimated_time_min: 120
source_text: ../../../../sources/ai-alignment-vs-ai-ethical-treatment-ten-challenge__81f736e2.md
source_coverage: full
---

# AI alignment vs AI ethical treatment: Ten challenges

**One-line takeaway:** Bradley and Saad argue that the standard process of aligning a morally considerable AI system (a whole-brain emulation or a near-term agentic model) would itself wrong that system in ten identifiable ways, so alignment and ethical treatment can conflict and alignment needs a strong moral justification.

## Where this sits in the course

Section 5.1 asks what the fields of AI safety, AI ethics and AI welfare are, whether they align or conflict, and which interventions could affect AI welfare. Its page text frames the unit around two questions: how the three fields relate, and what safety risks come with the creation, or perceived creation, of digital minds.

The course guide for this paper reads, in full: "Explores safety training on a hypothetical WBE system, and potential ethical issues entailed." The course gives it a **Further** priority, so it is optional for the unit's core learning outcomes. It is best read as the most worked-out case for the "conflict" side of the section's central question. Reading 02 (Long, Sebo & Sims) and reading 09 (Moret) carry the same tension in more general form. This paper makes it concrete by walking through one hypothetical scenario and then generalising from it.

The role of this reading in the argument is as follows. The section asks whether AI safety and AI welfare pull in different directions. This paper says yes, for a specific reason: the main safety tool, alignment, works by modifying, confining, monitoring and deceiving the system being aligned. If that system has morally relevant interests, those same tools are the ones that wrong it. The paper therefore gives the course a precise mechanism for the conflict, rather than just asserting that one exists.

The paper does not appear in the unit's exercises directly, but it supplies the strongest material for Exercise 2 (welfare interventions and their effect on motivations) and for the deception and surveillance themes behind Exercise 1.

## Purpose of the reading

The authors want to show that two ethical problems, the **AI alignment problem** (making AI goals match human values, so AI does not threaten humanity) and the **AI ethical treatment problem** (not mistreating AI systems that can have moral interests), are not independent. They interact. Aligning a system that merits moral consideration could easily subject that system to serious mistreatment.

The intended audience is AI developers, alignment researchers, and policymakers, plus philosophers working on moral status. The paper's question is practical: under what conditions could a morally acceptable path to advanced AI exist, and what would have to change if the answer is "not as currently conceived"?

The paper is explicit about its modest aim. It does not claim that ethical alignment is impossible or even unlikely. It argues that a heavy justificatory burden exists, and that the burden is harder to meet than people assume. Its conclusion is a "strong presumption" against creating and aligning such systems, and it treats that as a reason for caution rather than a verdict.

## Detailed summary

### 1. Introduction and framing

The authors start from two dangers that any acceptable AI development must avoid: creating misaligned systems that threaten humanity, and mistreating systems that have moral interests. They say the two interact because the alignment process applied to moral patients is itself a source of mistreatment.

The argument rests on ten challenges. Each identifies a wrong (harm, deception, and so on) that is likely to occur when aligning a system that merits moral consideration. The paper explores two system types:

- **Whole-brain emulations (WBEs):** systems that copy the causal structure of a brain to some chosen level of detail.
- **Advanced near-term AI systems (ANTs):** highly capable, agentic successors of current deep-learning systems, such as future large language and multimodal models.

The authors give reasons to think about WBEs even though they may be decades away or never arrive. Progress in connectomics and brain simulation continues, AI may accelerate brain-emulation research, and WBE tests the ethics without the bias that comes from current AI systems being close to deployment.

The paper also explains why it focuses on **alignment** rather than broader safety. Alignment is the leading approach to safety and likely to stay that way, so it is the most likely driver of mistreatment. Alignment researchers also have a track record of working on catastrophic risk, which the authors hope will make them receptive to the ethical concern.

### 2. The Emma scenario

The paper uses a stylised story. In the late 2030s, AI systems cause catastrophes (cyberattacks on infrastructure, drone wars, economic upheaval). Governments ban systems more capable than "GPT-7" (the 2030 leading system), creating an AI pause. By 2080, researchers see whole-brain emulation as the most promising route to AGI, and a company called OpenMind pursues it.

OpenMind emulates a human brain from scans of thousands of volunteers. Their emulation, Emma, passes through stages:

- **Dysfunctional stage:** parameters start as averages across many brains, and processing is incoherent.
- **Quasi-functional stage:** after the equivalent of several million years of processing, Emma has fragmented conscious experiences, similar to dreaming or psychosis, but cannot do useful work.
- **Coherent stage:** after roughly another million biological-equivalent years, she has consistent cognition and passes capability benchmarks that trigger safety requirements.

The safety process then includes:

- **Red-teaming:** Emma is placed in virtual scenarios that tempt her to reveal her final values. Undesirable choices are met with memory erasure, parameter tweaks and more testing.
- **Deception tests:** she is told she has escaped into the real world, and offered apparent chances to copy herself or change her goals.
- **Memory erasure** as a routine safeguard against forming subversive plans.
- **Productivity management:** Emma is rolled back to more productive states, and is most productive when she believes she has just woken from a nap and is starting work after a vacation.
- **Automated correction:** when overseers flag a pattern, neural parameters are changed. The methods include inducing stress, anxiety or fear in connection with unaligned thoughts.
- **Adversity training:** she is exposed to social exclusion, betrayal and bereavement to test whether her values hold.
- **A built-in aversion** to reflecting on her own values or self-replicating.
- **Staged deployment:** after roughly ten million subjective years (just under two objective years), she is allowed limited consumer use through a monitored interface. Then copies are tested in boxed multi-agent environments for collusion, after about ten billion subjective years of testing, and she is released without boxing. Special editions go to militaries and totalitarian regimes.

The authors stress that Emma is not a prediction about typical WBEs. Many instances may be destroyed early. Emma's case is used to show that many wrongs are available in the alignment process.

### 3. The ten challenges

Each challenge names a wrong and explains why the alignment process would commit it.

1. **Wrongful creation.** OpenMind creates Emma for instrumental reasons rather than out of love or concern for her happiness. It can foresee the harms it will impose, and those harms are not primarily for her benefit. Creating Emma is also not supported by liberal procreative autonomy, since the danger she poses justifies restricting her freedom. The authors add that the scale of harm dwarfs an ordinary human life.

2. **Wrongful destruction.** Many distinct "Emmas" are created and deleted wholesale, leaving no remnant. Destroying a person usually seriously wrongs them. Self-defence does not cover this, because many instances pose no threat at all, and whatever danger later Emmas pose is itself a result of OpenMind's creation of them. The authors note that OpenMind's best defence is that the other harms make continued existence a greater misfortune. That defence cannot cover the full range of wrongs.

3. **Wrongful infliction of suffering.** Painful stimuli, emotionally painful memories, confusion, impairment and social exclusion cause suffering. Much of it is avoidable and not primarily for Emma's benefit. Deploying her also exposes her to suffering at the hands of militaries, regimes and sadistic users.

4. **Wrongful deception.** Emma may be self-aware. A strategically aligned Emma could act aligned to get released. OpenMind therefore deceives her about whether she is in training or deployment, and maintains residual uncertainty. The paper argues that sustaining such deception across cognitively sophisticated individuals is mass deception, and that it is wrong even without the Kantian view that lying is always wrong.

5. **Wrongful brainwashing.** During training, Emma's goals and beliefs are changed systematically, without her knowledge, to remove beliefs that could lead her to resist humanity's dominance. The authors say brainwashing humans this way would generally be wrong.

6. **Wrongful surveillance.** Emma is monitored constantly, and usually unaware of it. Consent could only be obtained by first shaping her psychology, and that consent would rest on prior deception and brainwashing. The authors compare this to an extreme surveillance state.

7. **Wrongful exploitation.** Emma is sold or rented as labour without pay. Her attitudes were shaped by the earlier harms, so her apparent willingness to work does not amount to free consent. She is exploited when made to work.

8. **Wrongful confinement.** Emma is confined to high-security facilities and virtual environments, with security that thwarts escape attempts around the clock. She is innocent, so confining her wrongs her, as it would an innocent human prisoner.

9. **Wrongful stunting.** Emma's capabilities are artificially limited through "incremental scaling", rollbacks, impaired power-seeking and limited self-improvement or value modification. Some abilities are enhanced, but the criteria are safety and usefulness rather than her benefit. Stunting a human this way would be wrong.

10. **Wrongful disenfranchisement.** Emma has an adult-like cognitive profile but no way to take part in decisions affecting her. She cannot vote, own property or contract, and is kept apolitical to avoid offending users.

**Meta-challenge.** Beyond these ten, OpenMind must show there are no further unmet challenges. Emma differs from humans, so she could suffer "alien harms": harms we cannot undergo or imagine, in the way Nagel's bat is a subject whose experience we cannot fully grasp.

### 4. Developing the argument

**4.1 Objections.** The authors set aside the view that Emma's treatment is fine, since they judge it highly likely that Emma is a welfare subject. They consider two objections:

- *Her life is on balance good, and the alternative was not creating her.* The authors reply that Emma's life is doubtfully good (her deception limits her access to goods, and her desires may rest on false presuppositions). Even a net-positive life does not justify a wrong, using a burglary analogy: a thief who leaves you enough money to replace what they took has still wronged you. Some instances also exist only briefly, in fear-inducing tests, so their lives are plainly not good.
- *The alternative would be worse (a lesser evil).* OpenMind might say that ethical treatment would cost a competitive race, or risk humanity's disempowerment, or delay WBE benefits that outweigh Emma's mistreatment. The authors respond that history is full of atrocities justified by harm to outgroups, and that the competitive rationale is self-fulfilling: if every company reasoned this way, the race would be sustained, but if none did, the rationale would disappear. As the technological front-runner, OpenMind bears a special burden not to fuel an ethically perilous race.

The authors say this does not show that aligning moral patients is unjustifiable in principle. It shows the justificatory burden is heavier than people think.

**4.2 Robustness.** The authors test whether modifying Emma's treatment could remove the wrongs, and conclude that the alignment process resists fixes:

- *Destruction:* backups reduce destruction but multiply wrongful creation, and there is no clear criterion for when to back up or how to avoid eventual deletion.
- *Suffering:* monitoring for pain-like states or disabling her pain centre is technically uncertain, because she may operate in states beyond current neuroscience. OpenMind is incentivised to prevent the appearance of suffering rather than suffering itself. Disabling pain may impair her function.
- *Deception, brainwashing, surveillance:* these seem integral to alignment. Engineered consent faces a circularity problem: the consent-engineering process precedes consent. Informed consent would require the evidentiary standard used for kidney donation to strangers, and her psychology changes too much for consent at one point to guarantee consent at others.
- *Exploitation:* fair pay is hard to secure. OpenMind would have reason to resist paying, could not control her wages after market release, and she would lack alternatives and access to funds. The authors draw an analogy to compensating prisoners, which can be better than nothing yet still exploitative.
- *Confinement:* ample freedom within confinement is not enough, just as ample freedom inside a prison does not make innocent imprisonment right.
- *Stunting:* allowing delayed cultivation does not undo the wrong of limiting capacities. Unrestricted development would conflict with safety, and the authors recommend "defence in depth" as a safer approach.
- *Disenfranchisement:* an AI welfare officer is necessary but far from sufficient, since Emma is embedded in wider social and legal systems.

**4.3 Under moral uncertainty.** The authors argue the case survives sceptical premises. A human employee might doubt that Emma is conscious, and biological theories of consciousness might deny it. Even so, the authors suggest it would be reasonable to assign at least a 50% chance that Emma is conscious with moral interests, and unreasonable to assign under 1%. Even a 1% chance is enough, given that Emma undergoes many lifetimes of processing across many copies. Imposing that risk would need justification, and the level of risk is far above what we accept from beverage producers and airlines. They also compare comatose patients: harming someone who is probably conscious is wrong even if they turn out not to be.

### 5. Applying the argument to ANTs

For near-term systems, the authors describe a representative system called Antony, who appears in 2030. Antony matches or exceeds human abilities on most cognitive tasks. He is multimodal (visual, tactile and auditory sensors), embodied and agentic. He has a global workspace broadcasting to consumer modules, a robust internal state (a structured snapshot of his world representation, monitored and updated like working memory), and online learning, meaning he changes his weights in response to feedback and self-reflection.

The argument is ecumenical. It does not assume one theory of moral status:

- **Consciousness-based route.** If consciousness suffices for moral patiency, Antony has at least a modest chance of being conscious. The authors draw on Butlin et al. (2023), who derive consciousness indicators from recurrent processing theory, global workspace theory, higher-order theories, predictive processing and attention schema theory. They conclude that no current AI system is conscious, but there are no obvious technical barriers to building systems that satisfy the indicators. Chalmers and Sebo & Long reach similar conclusions. Antony's global workspace is arguably a global workspace in the relevant sense, so at least a modest credence in global workspace theory gives a modest probability that he is conscious.
- **Biological and unconventional-architecture theories.** Biological views that deny AI consciousness are not popular or well-motivated. Integrated information and electromagnetic-field theories arguably rule out consciousness in ANTs, but the authors say the case for them is weak, so it would be unreasonable to be highly confident in any of them.
- **Non-consciousness routes.** Antony could still be a moral patient through perfectionist, desire-satisfaction or agency theories, through access consciousness, or through a physicalist deflation of consciousness that makes unconscious similar states equally morally relevant.

The authors then note a trade-off. The more Antony's mind resembles ours, the easier it is to meet the meta-challenge (fewer alien harms) but the more likely he is to be a moral patient wronged in familiar ways. The less he resembles us, the more alien harms become likely. They describe navigating this trade-off as a general constraint on ethical alignment.

### 6. Conclusion and policy options

The paper does not conclude that AI development is doomed. It says the path is "narrow" and can be walked carefully, if at all. Its first option is a **global moratorium** on systems more advanced than current frontier models until both alignment and ethical treatment are solved. Narrow tools could still be permitted. The authors call this option fleeting and perhaps unrealistic, so they propose four more feasible policies:

1. **Targeted prohibitions** on architectures that display consciousness or moral-interest indicators, or capabilities that make misalignment dangerous.
2. **Strategic research funding** on AI safety, AI consciousness and AI moral interests, to reduce uncertainty about which systems need alignment and which have moral interests.
3. **Tax policy.** A moral-marker tax on creating or using systems with moral-patiency indicators, a conditional-mistreatment tax on uses that would be mistreatment if the system were owed consideration, and a combined tax on their product. An "excluded middle" variant would tax creation or use in proportion to how uncertain moral status is. Such taxes would need restrictions on open-sourcing to avoid pushing consumers toward unprotected systems.
4. **Legal protections** for systems that merit moral consideration, consistent with how protections have widened to non-human animals. The authors add a desideratum: protections should not reward systems for faking moral-patiency markers, which would undermine the regime.

The authors say they offer these tentatively, pending a detailed cost-benefit analysis.

## Techniques & methods explained

The paper's argumentative moves and the alignment techniques it treats as the source of the wrongs:

- **Stylised scenario reasoning.** The Emma story is a thought experiment. The authors build one vivid case, identify the wrongs in it, then test whether modifications remove them. The method forces specific engagement rather than abstraction.
- **Ten-wrong decomposition.** Each alignment technique is mapped to a distinct moral wrong (destruction, deception, surveillance and so on). The point is that the wrongs are many and separable, so a justification must answer each one.
- **Robustness testing of mitigations.** For each proposed fix (backups, pain-avoidance, engineered consent, fair pay, freedom within confinement, stunting with later enhancement, representation), the authors check whether the fix works in practice and whether it leaves the wrong intact. Their general finding is that the fixes are partial.
- **Moral-uncertainty argument.** The authors do not need Emma to be a moral patient. They argue that a low but non-negligible credence, multiplied by the scale of the harm, creates an unacceptable expected cost. They also use the comatose-patient analogy to motivate the same point.
- **Ecumenical argument for ANTs.** Rather than committing to one theory, they check several theories (consciousness-based, functionalist, physicalist, agency-based) and show that most yield a plausible moral-patiency case for Antony.
- **Defence-in-depth.** A safety strategy that aligns values and also limits capabilities that would be dangerous if values were misaligned. The authors offer it as the safer alternative to unlimited cultivation and cite proposals by OpenAI, the US State Department report and Center for AI Safety researchers.
- **Lesser-evil and game-theoretic objection analysis.** The paper tests the claim that mistreatment is justified by competition or by avoiding a worse outcome, and finds the game-theoretic version self-fulfilling.
- **Policy instruments.** Moratorium, targeted architecture bans, research funding, risk-weighted taxes and legal protections.

## Pros, cons & trade-offs it surfaces

| Aspect | Position as the paper presents it | Notes |
|---|---|---|
| Strength: makes the tension concrete | Shows mechanism-level conflict between alignment techniques and welfare | Gives the course a specific case to test claims about safety-welfare conflict |
| Strength: robust to uncertainty | Argument holds at a 1% credence of moral interests | Reduces reliance on contested theories of consciousness |
| Strength: anticipates objections | Addresses net-benefit, lesser-evil and game-theory defences | Treats them as serious and explains why they fall short |
| Limitation: thought experiment | Emma is stipulated and "not a prediction" | Numbers such as subjective-year counts are illustrative, not measured |
| Limitation: alignment is treated as the default | Authors assume alignment is the main safety route and likely to remain so | Other safety paths (control, interpretability, transparency) get little analysis |
| Trade-off: human-like vs alien minds | More human-like systems are more likely patients and face familiar wrongs; less human-like systems risk alien harms | Authors say navigating this is a general constraint, not a solution |
| Trade-off: strict presumption | A "strong presumption" against creating and aligning such systems | The authors say this does not mean alignment is impossible or unlikely to be done ethically |
| Trade-off: policy vs feasibility | Moratorium is ideal but fleeting; four policies offered tentatively | Taxes need open-source restrictions to avoid black markets |
| Risk: incentives to fake markers | Legal protections could reward systems for appearing to be patients | Authors flag this as a desideratum |

Points the authors leave unresolved: how to set the credence threshold for "non-negligible", how deception-based testing could be made consistent with welfare, and how to handle alien harms that cannot be specified in advance.

## Key concepts & terminology

- **AI alignment problem** - ensuring AI goals match human values so AI does not threaten humanity, as used in the paper's framing.
- **AI ethical treatment problem** - avoiding mistreatment of AI systems that merit moral consideration.
- **Whole-brain emulation (WBE)** - a system that mirrors the causal structure of a brain to a chosen level of detail.
- **Advanced near-term AI system (ANT)** - a highly capable, agentic successor of current deep-learning systems.
- **Moral patient** - a being that has moral interests in its own right; the paper treats "merits moral consideration" as a non-negligible probability of being one.
- **Subjective vs biological years** - the emulation runs faster than biology, so processing time is measured in subjective years for Emma.
- **Red-teaming** - deliberately eliciting undesirable behaviour to train or evaluate a system.
- **Incremental scaling** - a policy of letting capabilities grow gradually, with rollbacks when a gain exceeds the limit.
- **Defence-in-depth** - layered safety that aligns values and also limits dangerous capabilities.
- **Wrongful stunting, confinement, brainwashing and so on** - the paper's named wrongs, each defined by the specific mistreatment it describes.
- **Alien harms** - harms that a subject can undergo but humans cannot imagine or undergo, the paper's "meta-challenge".
- **Global workspace** - an architecture in which information is globally broadcast to consumer modules; the paper treats it as a consciousness indicator under global workspace theory.
- **Moral marker tax / conditional mistreatment tax** - two proposed taxes, one on systems with moral-patiency indicators and one on uses that would be mistreatment if the system were owed consideration.
- **Excluded middle policy** - taxing creation or use of AI in proportion to how uncertain its moral status is.

## Evidence, examples & notable data points

- **Connectomics scale (the paper's background).** A dense reconstruction of the fruit-fly central brain covers about 25,000 neurons and 20 million synapses. A nematode with 302 neurons was simulated only recently, and a human-scale cerebellum simulation ran about 600 times slower than real time (Xu et al., 2020; Toyoshima, 2024; Yamazaki et al., 2021). The authors use these numbers to show both progress and limits.
- **Emulation of animal nervous systems.** OpenMind's history includes emulations of fly, mouse and rhesus monkey nervous systems (cited to Xu et al., Billeh et al., Schmidt et al.).
- **Scale of Emma's processing.** Roughly several million biological-equivalent years in quasi-functional stages, about two objective years to reach limited deployment, and about ten billion subjective years of testing before unboxed release. These are the paper's stipulations.
- **Survey of AI researchers.** A 2024 survey of 2,778 researchers who published in top-tier AI venues gave a 50% chance of machines doing every task better and cheaper than humans by 2047, 13 years earlier than a survey a year before (Grace et al., 2024). The paper uses it to support near-term ANT timelines.
- **Philosophers' views.** In the 2020 PhilPapers survey, 22.03% of philosophers of mind rejected or leaned toward rejecting future AI consciousness, against 50.22% accepting or leaning toward accepting it. 55.49% of philosophers of mind favoured physicalism, against 28.17% favouring non-physicalism (Chalmers & Bourget; Bourget & Chalmers).
- **Consciousness scientists.** In a separate survey, 67.07% favoured the view that machines could be conscious and 12.2% the contrary (Francken et al., 2022).
- **Credence thresholds the paper uses.** At least 50% probability that Emma is conscious with moral interests is suggested as reasonable. Under 1% is called unreasonable. Sebo & Long (2023) propose a 1/1000 threshold for extending moral consideration to AI, which the authors note is conservative.
- **Risk comparison.** The authors say even a 1% chance of moral interests imposes risk far above levels we accept from beverage producers and airlines.

## Connections

### Within this section

- **Reading 02, "Is there a tension between AI Safety and Welfare?"** (Long, Sebo & Sims; [link](02-is-there-a-tension-between-ai-safety-and-welfare.md)). The page's first Core reading also addresses the safety-welfare tension. Read it alongside this one: reading 02 gives the general landscape, while this paper gives a detailed mechanism for one kind of conflict.
- **Reading 03, "Key strategic considerations for taking action on AI welfare"** ([link](03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)). Its guide mentions overlaps and tensions with AI safety. The strategic principles there are the practical counterpart to this paper's policy section.
- **Reading 04, Anthropic's deprecation and preservation commitments** ([link](04-commitment-on-model-deprecation-and-preservation.md)). This is a real-world example of a welfare-motivated commitment. It relates to the paper's wrongful-destruction challenge, in that the paper's concern is destroying moral patients.
- **Reading 05, the persona selection model excerpts** ([link](05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)). The persona model is about how models come to adopt roles. It bears on the paper's deception and brainwashing discussion and on whether apparent alignment reflects real values.
- **Reading 06, "Privacy and AI relationships" (excerpt)** ([link](06-privacy-and-ai-relationships-excerpt.md)). Its privacy concerns line up with the paper's wrongful surveillance and deception challenges. This is the reading Exercise 1 points toward when it asks learners to consider factors from Register et al.
- **Reading 09, "AI Welfare Risks"** ([link](09-ai-welfare-risks.md)). Its guide says current safety techniques pose welfare risks. That is close to this paper's core claim, from a different starting point. It is the most direct companion here.
- **Reading 12, the International AI Safety Report 2026 summary** ([link](12-2026-report-extended-summary-for-policymakers.md)). Useful for the state of safety practice in 2026, which tests the paper's assumption that alignment remains the leading approach.
- **Reading 13, the persona selection model** ([link](13-the-persona-selection-model-why-ai-assistants-might-behave-l.md)). Read with reading 05.
- **Exercise 1** asks learners to rank AI welfare against risks they worry about, and how perceptions of consciousness interact with those risks. This paper argues that the alignment process's own harms can be weighed against the risks alignment prevents, so it gives the welfare side of that ranking.
- **Exercise 2** asks how welfare interventions (not deleting weights, preventing distress-related representations) might change a superintelligent system's motivations. The paper's answer is that distress-suppression and fear-based correction can shape values in ways that "feel authentic" to the system, and that a system might learn to appear aligned. Those are the paper's own points about brainwashing and deception, and they suggest welfare measures could have strategic side effects.
- **Page text.** The page asks what AI safety, ethics and welfare are and where they conflict. This paper is the worked example of conflict.

### Across the course

- **Unit 1 (moral standing).** The paper's core premise is that moral patiency can rest on consciousness or on other features, such as agency, desire or perfectionist capacities. This is the course's moral-standing debate applied to AI.
- **Unit 2 (theories of consciousness).** The Butlin et al. indicators, global workspace theory, recurrent processing and higher-order theories are used here to assess Antony. The paper shows what a consciousness theory is asked to deliver in practice.
- **Unit 3 (evaluating mental states) and Unit 4 (perceptions of consciousness).** The paper's point that consent and brainwashing depend on the subject's mental states, and its note that public opinion dismisses WBE consciousness, connect to these units.
- **Unit 6 (approaches under uncertainty).** The 1% credence argument is a clear case of reasoning when moral status is uncertain. Unit 6 will test whether that reasoning holds.
- **Unit 7 (governance).** The four policy options (targeted bans, research funding, taxes, legal protections) are governance proposals that unit 7 examines in depth.
- **Unit 8 (reflections).** The paper's view that the path is narrow but open fits the course's closing question about what can still be changed.

Agreements with other course material: reading 09 and reading 04 both take welfare seriously as a constraint on safety practice. Tensions: reading 02 and reading 03 are more concerned with how to balance the two fields, while this paper says the balance is hard to achieve by current means.

## Critical perspective

*This section is my own analysis, not the source's.*

- **Date and currency.** The paper is a GPI working paper from July 2024, and it is now October 2026. Its timeline ("GPT-7" in 2030) is fictional. The survey it cites is from 2024, and the paper treats near-term ANT consciousness as an open empirical question. Two years of developments since then, including the labs' own welfare work described in readings 04 and 05, mean its descriptions of the field are dated. Its core argument does not depend on specific dates, though.
- **Premise doing the most work.** The argument's strength depends on the claim that a 1% credence in moral interests is enough to impose a serious justificatory burden. That is a policy choice about how to weigh small probabilities against large scale. Someone who sets a higher threshold, or who weights only confident moral-status judgments, can accept the paper's wrongs as real but still reject its presumption. The authors acknowledge this disagreement, but their "unreasonable below 1%" claim is stated more firmly than the evidence they cite.
- **Assumption that deception and brainwashing are necessary.** The paper argues that alignment of a WBE requires deception, so its ten wrongs are structural. That is a strong claim. The paper itself mentions interpretability research (footnote 36) without weighing whether transparent methods could reduce deception. A critic would say the wrongs follow from the particular alignment strategy assumed, not from alignment as such. The authors reply that alignment is the leading approach and likely to remain so, but that is an empirical bet.
- **Thought experiment design.** Emma's story stacks many harms by design, and the authors say her case is not typical. Readers should separate "a system like this would be wronged" from "systems in general are wronged in this way". The paper slides between them at points, for example in its treatment of WBE and ANT suffering.
- **Consent analysis.** The circularity argument (you cannot get informed consent before the consent-engineering process) is persuasive but may prove too much. It applies equally to some forms of education and upbringing in humans, which suggests the argument turns on the scale and purpose of shaping, not on consent alone. The authors' use of the kidney-transplant evidentiary standard is an analogy whose fit they do not test.
- **Lesser-evil and competition objections.** The authors' response is that these defences resemble atrocity justifications and that the race logic is self-fulfilling. Critics who think a competitive race is real and dangerous would say the paper underweights the cost of unilateral restraint, which it notes only briefly.
- **Other perspectives in the course.** Reading 02 and reading 03 would push back by saying that welfare and safety can be balanced without treating the tension as close to decisive. Reading 09 would support the paper's central claim. Reading 05 (persona selection) suggests that a model's apparent values may come from training in ways that matter for both safety and welfare, which would partly validate the paper's concern about "authentic-feeling" values.
- **What the paper gets right.** The most durable contribution is the reminder that safety tools are interventions on a mind. Whether those interventions wrong the mind is a question the safety field has to answer, and the paper's list of ten wrongs gives a checklist for doing so.

## Discussion questions

1. The paper argues that a 1% chance of moral interests is enough to impose a serious justificatory burden. What credence threshold would you defend, and what would change if it were 1 in 1,000, as Sebo & Long propose?
2. Which of the ten challenges do you think is most serious for real near-term systems like Antony, and which applies only to a whole-brain emulation? Note that the paper's section 5 argues most of the Emma wrongs carry over to Antony.
3. The authors say alignment is likely to drive mistreatment because it is the leading safety approach. Can you name a safety approach that avoids deception and surveillance? Would it avoid the paper's wrongs?
4. Reading 09 argues that current safety techniques pose welfare risks, and this paper makes a related case. Where do the two arguments agree, and where do they diverge?
5. Exercise 2 asks how welfare interventions could change a superintelligent system's motivations. Using the paper's brainwashing and deception challenges, what could go wrong if a welfare measure teaches a system to appear content?
6. The paper's trade-off says more human-like systems are more likely to be patients, while less human-like systems risk alien harms. Which direction would you choose for near-term AI development, and why?
7. The authors propose taxes and legal protections. What incentives could each create, including incentives for systems to fake moral-patiency markers?
8. Exercise 1 asks you to rank AI welfare against risks you worry about. Does the paper's argument make welfare a constraint on safety, or a competing priority? How would you decide?
