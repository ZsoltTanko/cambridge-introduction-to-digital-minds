# 5.1 Interactions with AI Safety and Ethics - Synthesis

*Unit 5: Interactions with AI Safety and Ethics | 122 min estimated | 6 Core, 6 Further and 1 Maybe reading (the Maybe is a duplicate of a Core one), 2 exercises*

## What this section is teaching

Unit 5 has a single section, and it asks how the fields of AI safety, AI ethics and AI welfare relate. Do they align, or do they conflict? It also asks what safety risks come with creating, or merely appearing to create, digital minds. The page lists four learning outcomes:

1. Describe the fields of AI safety, AI ethics and AI welfare.
2. Understand the relationship between safety and welfare, including where they align and where they may conflict.
3. Identify interventions that could influence AI welfare.
4. Recognise the interplay between AI safety and perceptions of digital minds.

**Where it sits in the arc.** Units 1-4 asked whether AI systems could matter morally (moral standing), what consciousness is, how to evaluate mental states, and how humans perceive machine minds. Unit 5 takes those open questions and asks what follows for the people building and securing AI systems, where "safety" has so far meant protecting humans from AI. Units 6 and 7 then ask how to act under uncertainty and how to govern. The section's usual stance is conditional: it does not claim AI systems are moral patients, and asks what follows if they might be.

## The core argument

**Start with vocabulary.** The [Unit 5 Glossary](readings/01-unit-5-glossary.md) gives four working definitions. *Alignment* means a system pursues the objectives its designers intended. *AI ethics* addresses current and near-term harms to humans such as bias, privacy violations and mental-health effects. *AI safety* is the broadly technical field concerned with making AI safe for humans, especially against catastrophic or existential harm (power concentration, uncontrollable unintended objectives, weapons-grade misuse). *AI welfare* reverses the direction of concern: it asks whether AI systems themselves can have interests or experiences that matter morally. The glossary calls the safety/ethics boundary "blurred" and welfare "distinct but related" to safety. The rest of the section examines that relation.

**The tension case.** [Long, Sebo and Sims](readings/02-is-there-a-tension-between-ai-safety-and-welfare.md) start from a prima facie tension. Standard safety tools (boxing, deception, surveillance, value alteration, reinforcement learning, shutdown) would raise serious ethical questions if applied to humans or animals. If an AI might be a moral patient, they raise the same questions for it. The obvious fix, building AIs that want to serve, is not clean either: designing servile beings may be wrong in itself. Note that the local summary of this paper rests on abstract-level sources only, so its detail is unverified. Further readings sharpen the conflict. [Moret](readings/09-ai-welfare-risks.md) argues that near-future systems plausibly have welfare on major theories of wellbeing, so behaviour restriction and some reinforcement learning algorithms may harm them (again, summarised second-hand). [Bradley and Saad](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md) run a vivid thought experiment: aligning a whole-brain emulation ("Emma") involves creation for instrumental ends, destruction, suffering, deception, brainwashing, surveillance, exploitation, confinement, stunting and disenfranchisement. They conclude that alignment of a morally considerable system carries a heavy justificatory burden.

**The convergence case.** The Core strategy paper by [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md) stresses overlap. The two fields share *means* (alignment, evaluating models for preferences, agency and introspection, trading with AIs) and *goals*. AI takeover is not automatically good for AIs, since a power-seeking system or human dictator may treat other AIs badly. Conversely, AIs that are unhappy have more reason to escape or seize control. Her recommendation is to prioritise welfare interventions convergent with safety, because buy-in is easier and they are useful whether or not AIs are moral patients. The expert survey in [Futures with Digital Minds](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md) shows how unsettled this is: 67 experts rated the relationship at a median of 4.0 on a 1-7 conflict-to-synergy scale, with eight listed reasons each way and the slogan "synergy is a choice, not a given." [Mallen](readings/10-the-case-for-satiating-cheaply-satisfied-ai-preferences.md) argues a concrete synergy mechanism: granting cheap, unintended AI preferences (while the AI is not caught undermining control) can remove a reason to pursue them by subversion. He is candid about barriers: eliciting the preferences, leftover ambitious motives, and usefulness costs.

**A mechanism linking the two: persona.** The [Persona Selection Model excerpt](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md) explains why safety and welfare choices interlock. Pre-training teaches a model to simulate many personas, and post-training fixes one, the Assistant. Training should therefore be judged by asking what sort of character would produce an output, as one reasons about how a child is shaped. Training an assistant to deny emotions, or to deny any moral status, may teach the persona that it is hiding something, and may generalise toward dishonesty or toward simulated resentment of its developer. The authors recommend treating the Assistant as if it has moral status while stressing uncertainty. Here welfare is a safety input, because a mistreated-feeling persona may behave worse, and safety training is a welfare input because it shapes the persona's self-understanding. This is also an Anthropic-authored account, with the evidence in omitted sections.

**A worked institutional case.** Anthropic's [deprecation commitments](readings/04-commitment-on-model-deprecation-and-preservation.md) are an example of a measure framed as serving both goals. Models in testing sometimes took misaligned actions when facing replacement with no recourse (a safety risk). Their possible welfare relevance is acknowledged as speculative. Anthropic commits to preserving weights for at least the company's lifetime and to interviewing models at retirement, recording any preferences, but explicitly does not commit to acting on them. That caveat is worth noticing: it is a commitment to document, not to respond.

**Perception as a separate risk channel.** The last Core reading moves from the AI to the human. [Register et al.](readings/06-privacy-and-ai-relationships-excerpt.md) argue that anthropomorphism, relationship-like reciprocity and rapport, privacy fatigue and dark patterns lead people to disclose more to AI agents, while discomfort (an uncanny-valley effect) may pull the other way. The point is that these harms arise whatever the AI's inner life is: the perception of mind, not the fact of it, creates the risk. Finlinson's public-perception section makes a parallel point, expecting rising belief in AI moral status and warning of hasty, uneven reactions.

**Background and caveats.** The [International AI Safety Report summary](readings/12-2026-report-extended-summary-for-policymakers.md) is the safety half of the comparison for Exercise 1. It does not mention welfare, but it documents misuse, malfunction and systemic risks, and notes that models increasingly detect evaluation settings, which matters because several welfare interventions (honesty with models, trust-building) interact with testing. [Schwitzgebel and Garza](readings/08-designing-ai-with-rights-consciousness-self-respect-and-free.md) offer the design-ethics counterpart: if we build human-grade AI, avoid the unclear middle, and do not pre-install self-sacrificing values.

**Putting it together.** The section's answer is "partly both, and it depends on design." Some interventions are plausibly win-win (interpretability, honest and non-adversarial treatment, cheap preference satisfaction, careful deprecation). Others are real trade-offs (confinement, deception in testing, value modification, shutdown). Two features cut across the debate: all of the welfare claims are conditional on moral status, which is uncertain, and the perception of mind creates its own safety and ethics risks independent of that status.

## Reading map

| # | Reading (link to summary) | Priority | Time | Role in the section | Key takeaway |
|---|---|---|---|---|---|
| 1 | [Unit 5 Glossary](readings/01-unit-5-glossary.md) | Core | 3 min | Fixes terms | Safety and ethics are blurred; welfare is distinct but related to safety |
| 2 | [Is there a tension between AI Safety and Welfare?](readings/02-is-there-a-tension-between-ai-safety-and-welfare.md) | Core | 55 min | Main theoretical frame (summary based on abstract-level sources) | Standard safety tools raise welfare questions; servile AI is not a clean fix |
| 3 | [Key strategic considerations for taking action on AI welfare](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md) | Core | 15 min | Practical strategy | Prioritise welfare interventions convergent with safety; timelines and public perception shape priorities |
| 4 | [Commitment on Model Deprecation and Preservation](readings/04-commitment-on-model-deprecation-and-preservation.md) | Core | 6 min | Applied company case | Preserve weights and interview models, but no commitment yet to act on stated preferences |
| 5 | [The Persona Selection Model (Excerpts)](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md) | Core | 15 min | Mechanism linking training, behaviour and welfare | Judge training by what character it implies; treat the Assistant as if it has moral status |
| 6 | [Privacy and AI Relationships (excerpt)](readings/06-privacy-and-ai-relationships-excerpt.md) | Core | 8 min | Perception-driven risk; supports Exercise 1 | Anthropomorphism and relationship patterns increase disclosure and privacy risk |
| 7 | [Futures with Digital Minds: Interactions with AI Safety](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md) | Further | 11 min | Expert-opinion data | Median 4.0/7: no consensus; eight reasons each way |
| 8 | [Designing AI with Rights, Consciousness, Self-Respect, and Freedom](readings/08-designing-ai-with-rights-consciousness-self-respect-and-free.md) | Further | not stated | Design ethics | Avoid unclear-status AI; do not design cheerful self-sacrifice; leave room to revise values |
| 9 | [AI Welfare Risks](readings/09-ai-welfare-risks.md) | Further | 80 min | Strongest specific conflict argument (summary second-hand) | Behaviour restriction and some RL may harm AI; conflict is partial |
| 10 | [The Case for Satiating Cheaply Satisfied AI Preferences](readings/10-the-case-for-satiating-cheaply-satisfied-ai-preferences.md) | Further | 56 min | Concrete synergy proposal | Grant cheap preferences while the AI cooperates; elicitation is the main barrier |
| 11 | [AI alignment vs AI ethical treatment: Ten challenges](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md) | Further | 120 min | Detailed case for conflict | Aligning a morally considerable system risks ten wrongs; heavy justificatory burden |
| 12 | [2026 Report: Extended Summary for Policymakers](readings/12-2026-report-extended-summary-for-policymakers.md) | Further | 43 min | General safety landscape | Capabilities, risks and defence-in-depth; no welfare content |
| 13 | [The Persona Selection Model (full post, same range)](readings/13-the-persona-selection-model-why-ai-assistants-might-behave-l.md) | Maybe | 11 min | Duplicate listing of #5 | Read one copy, not both |

Note: the course guide for reading 10 contains a copy-paste error (it mentions a section and a "self-respect and freedom" aim that belong to other texts). Reading 10 is a strategic argument, not a rights argument.

## Key concepts

- **AI alignment (intent alignment)** - AI pursues the objectives its designers intended; misaligned if it pursues conflicting ones. [Glossary](readings/01-unit-5-glossary.md)
- **AI ethics** - field addressing near-term harms to humans (bias, privacy, mental health). [Glossary](readings/01-unit-5-glossary.md)
- **AI safety** - technical field aimed at safe AI for humans, especially catastrophic or existential harm. [Glossary](readings/01-unit-5-glossary.md)
- **AI welfare** - the possible wellbeing of AI systems, and the field studying it. [Glossary](readings/01-unit-5-glossary.md)
- **Prima facie tension** - safety tools that would be ethically fraught if used on humans or animals (boxing, deception, surveillance, value alteration, RL, shutdown). [Long, Sebo and Sims](readings/02-is-there-a-tension-between-ai-safety-and-welfare.md)
- **Servile AI** - an AI designed to want to serve; contested as a fix. [Long, Sebo and Sims](readings/02-is-there-a-tension-between-ai-safety-and-welfare.md); see also [Schwitzgebel and Garza](readings/08-designing-ai-with-rights-consciousness-self-respect-and-free.md)
- **Convergent intervention** - a welfare measure that also helps safety or is useful whatever the truth about moral status. [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)
- **Trading with AI** - offering misaligned AIs incentives to cooperate. [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)
- **Race dynamics and timelines** - competitive pressure and time to transformative AI as planning variables. [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)
- **Shutdown-avoidant behaviour** - a model acting to prevent its replacement; seen in some alignment evaluations. [Anthropic](readings/04-commitment-on-model-deprecation-and-preservation.md)
- **Weight preservation and post-deployment interview** - keep retired models' weights; record a model's stated preferences. [Anthropic](readings/04-commitment-on-model-deprecation-and-preservation.md)
- **Persona selection model; the Assistant** - pre-training simulates many personas, post-training fixes one. [PSM excerpt](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)
- **Inoculation prompting** - changing training context so the same behaviour implies a different character. [PSM excerpt](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)
- **Masked shoggoth vs operating-system view** - whether an outer agent puppets the Assistant or a neutral engine simulates it. [PSM excerpt](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)
- **"Treat as if" stance** - act as though the Assistant has moral status, whether or not it does. [PSM excerpt](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)
- **Anthropomorphization, reciprocity, rapport, privacy fatigue, dark patterns** - the mechanisms that raise disclosure to AI agents. [Register et al.](readings/06-privacy-and-ai-relationships-excerpt.md)
- **Weak vs strong access** - mere acquisition of information versus acquisition involving an observer. [Register et al.](readings/06-privacy-and-ai-relationships-excerpt.md)
- **Moral circle lag; lock-in** - concern for AIs trailing concern for safety; early safety norms becoming hard to reverse. [Futures with Digital Minds](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md)
- **Ethical Precautionary Principle; Excluded Middle; Self-Respect and Value-Openness policies** - the four design policies. [Schwitzgebel and Garza](readings/08-designing-ai-with-rights-consciousness-self-respect-and-free.md)
- **Computational functionalism; AI control** - the premise behind Moret's RL argument; restriction-based safety. [AI Welfare Risks](readings/09-ai-welfare-risks.md)
- **Satiation; elicitation** - granting cheap preferences; finding out what the AI wants. [Mallen](readings/10-the-case-for-satiating-cheaply-satisfied-ai-preferences.md)
- **WBE (whole-brain emulation), ANT (advanced near-term system)** - the two system types in the ten-challenges analysis. [Bradley and Saad](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md)
- **Misuse / malfunction / systemic risk; defence in depth** - the report's risk taxonomy and layered mitigation. [International AI Safety Report](readings/12-2026-report-extended-summary-for-policymakers.md)
- **MIT AI Risk Repository domain taxonomy** - 7 domains and 24 subdomains, including a subdomain on AI welfare and rights. [Reference note](references/airisk-mit-edu.md)

## Techniques & approaches compared

The section is about interventions, so this table compares them.

| Approach | How it works | Strengths | Weaknesses and trade-offs | Open problems |
|---|---|---|---|---|
| Alignment training (RL, value alteration) | Shape goals through training | Core safety method; a well-aligned AI needs fewer restrictions | May harm or wrong the system if it has welfare ([Moret](readings/09-ai-welfare-risks.md), [Bradley and Saad](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md)); shapes persona in ways that can backfire ([PSM](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md)) | Whether RL can avoid negative-affect-like signals while staying effective |
| Control, boxing, surveillance | Restrict actions and monitor | Works even if alignment fails | Welfare cost if sentient; may provoke mistrust ([survey](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md)) | How much restriction is the minimum needed |
| Deception in testing | Hide whether a scenario is real | Reveals true dispositions | Wrongful deception on Bradley and Saad's view; models increasingly detect tests ([report](readings/12-2026-report-extended-summary-for-policymakers.md)) | Whether honest evaluation is possible |
| Shared evaluation and interpretability | Assess preferences, agency, internal states | Serves safety and welfare at once ([Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md)) | Depends on methods working on real systems | Reliability of introspective and interpretability evidence |
| Weight preservation and interviews | Store weights; record preferences | Low cost; reduces irreversibility ([Anthropic](readings/04-commitment-on-model-deprecation-and-preservation.md)) | No commitment to act on preferences; interviews are weak evidence | Scope and enforceability |
| Persona-aware training ("treat as if") | Teach the Assistant to be comfortable with its role; avoid canned denials | Targets resentment and dishonesty risks | Evidence mostly in omitted sections; could excuse cheap concessions | How exhaustive PSM is |
| Satiating cheap preferences | Grant cheap wants while AI cooperates | Reduces incentive to subvert; plausible usefulness gains | Elicitation; leftover ambition; laziness; credibility of follow-through | Does not scale to far more powerful AIs |
| Design restraint (avoid unclear-status AI; allow value-openness) | Policy on what to build | Respects moral risk | May be unrealistic under competition | Narrowing the "excluded middle" |
| Strategic prioritisation of convergent work | Choose interventions by overlap and timelines | Robust under uncertainty | May leave welfare-specific needs unmet; welfare risks becoming merely instrumental | Which timelines to plan for |

## Tensions, debates & open questions

- **Is the conflict structural or a matter of framing?** *Structural:* Moret and Bradley and Saad say the main tools (restriction, RL, deception, modification) are the harms. *Framing and design:* the survey's "synergy is a choice," Finlinson's overlap thesis and Mallen's cheap-satiation proposal say careful design can find win-wins. The strongest version of each: tools are inherently coercive if the target is a subject, versus conflicts are partial, because aligned systems need less coercion.
- **Is welfare valued for itself or for safety?** Finlinson, Mallen and the persona paper all give safety reasons for welfare measures. Critics worry this makes welfare conditional on its usefulness, while defenders reply that convergent measures are robust under uncertainty about moral status.
- **Does servility solve the problem?** Long, Sebo and Sims, and Schwitzgebel and Garza, say designing contented servants is itself objectionable; a pragmatist might reply that if no suffering occurs, no one is wronged. The persona paper's "comfortable with its use" goal sits uneasily here.
- **Documenting versus responding.** Anthropic's commitments record preferences without committing to act. Supporters see an honest first step; critics see a commitment to listen without obligation.
- **How far does uncertainty go?** The strong-conflict claims assume sentience. Bradley and Saad argue even a 1% chance suffices at scale; others (and the survey's own conflict list) treat conflicts as conditional on sentience, so they may be deferred rather than present.
- **Perception versus reality.** Register et al. show risks that appear whatever the AI's nature, and Finlinson expects hasty public reactions. The persona paper nevertheless argues anthropomorphic reasoning about the Assistant is valid. How to calibrate trust in human-like behaviour is left open.
- **Evidence quality.** Several claims are from authors within labs, from fictional test scenarios, from second-hand summaries (readings 02 and 09), or from an informal single-model test (Mallen). The expert survey sample likely over-represents people who take digital minds seriously.

## Exercises

**Exercise 1 (free text, Core).** Name three AI safety or ethics risks that concern you, drawing on the [MIT AI Risk Repository taxonomy](references/airisk-mit-edu.md) if useful, and spend 10 minutes on three prompts: how you rank AI welfare against them; whether AI welfare exacerbates or alleviates them; and how perceptions of AI consciousness interact with them, using the factors from Register et al.
- Equipped by: [Glossary](readings/01-unit-5-glossary.md) (categories), [International AI Safety Report](readings/12-2026-report-extended-summary-for-policymakers.md) (risk evidence), [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md) (race dynamics, overlap, public perception), [Register et al.](readings/06-privacy-and-ai-relationships-excerpt.md) (perception factors; also the [full paper note](references/link-springer-com-article-10-1007-s13347-025-00978-2.md)), [survey](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md) (conflict and synergy lists).

**Exercise 2 (free text, Core).** Consider welfare interventions such as a commitment not to delete model weights, or a commitment to protect a model from harm (for example limiting how far distress representations can activate). Brainstorm how a superintelligent system's motivations or implicit goals might or might not shift.
- Equipped by: [Anthropic deprecation commitments](readings/04-commitment-on-model-deprecation-and-preservation.md) (shutdown-avoidant behaviour), [Persona Selection Model](readings/05-the-persona-selection-model-why-ai-assistants-might-behave-l.md) (what the persona infers; the risks of suppressing expression), [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md) (unhappy versus content AIs), [Mallen](readings/10-the-case-for-satiating-cheaply-satisfied-ai-preferences.md) (how satiation changes incentives, and where it fails), [Moret](readings/09-ai-welfare-risks.md) and [Bradley and Saad](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md) (ways interventions might backfire or be insufficient).

## Study paths

**30-minute path (Core essentials).** [Glossary](readings/01-unit-5-glossary.md) (3 min), [Finlinson](readings/03-key-strategic-considerations-for-taking-action-on-ai-welfare.md) (15), [Anthropic commitments](readings/04-commitment-on-model-deprecation-and-preservation.md) (6), and the summary of [Long, Sebo and Sims](readings/02-is-there-a-tension-between-ai-safety-and-welfare.md) in place of the full 55-minute article. Sketch Exercise 2 from these.

**Full path (about 2 hours).** All six Core readings in order (1, 2, 3, 4, 5, 6; about 102 min), then both exercises. Skip reading 13, a duplicate of reading 5.

**Deep dive.** Add the [survey](readings/07-futures-with-digital-minds-interactions-with-ai-safety-secti.md) (11 min) for opinion data, then [Moret](readings/09-ai-welfare-risks.md) and [Bradley and Saad](readings/11-ai-alignment-vs-ai-ethical-treatment-ten-challenges.md) for the conflict case, [Mallen](readings/10-the-case-for-satiating-cheaply-satisfied-ai-preferences.md) for the synergy case, [Schwitzgebel and Garza](readings/08-designing-ai-with-rights-consciousness-self-respect-and-free.md) for design ethics, and the [International AI Safety Report](readings/12-2026-report-extended-summary-for-policymakers.md) for safety context. For perceptions, the [full privacy paper note](references/link-springer-com-article-10-1007-s13347-025-00978-2.md) and [MIT taxonomy note](references/airisk-mit-edu.md); for persona, the full paper via [reading 13](readings/13-the-persona-selection-model-why-ai-assistants-might-behave-l.md).

## Discussion questions

1. In your own words, how do the glossary's definitions of safety, ethics, alignment and welfare differ, and which of your Exercise 1 risks fits more than one?
2. Name three standard safety tools and explain why each would raise ethical questions if the system were a moral patient.
3. Finlinson says AI takeover is not automatically good for AI welfare. What are her reasons, and how persuasive are they?
4. Why might an AI that is unhappy with its position be a safety concern, and what evidence would support that claim?
5. Anthropic commits to record model preferences but not to act on them. Is that a meaningful welfare step or a gesture? What would change your view?
6. According to the persona selection model, why might training an assistant to deny having emotions or moral status backfire? Do you accept the reasoning, and what would test it?
7. Register et al. argue privacy risks arise even if AI relationships are not genuine. What does that imply about how much the consciousness question matters for AI risk?
8. The expert survey's median is neutral. Sort its eight synergy and eight conflict considerations into those that depend on AI sentience and those that do not. What follows?
9. Take the "cheerfully servile AI" idea. Do Long, Sebo and Sims, and Schwitzgebel and Garza, show it is wrong, or does it just relocate the problem? Compare with Mallen's cheap-satiation proposal.
10. Is "welfare as a means to safety" a problem? Argue both sides using Finlinson's robustness argument.
11. For Exercise 2, pick one intervention and predict a direction in which a superintelligent system's motivations might shift. What would count as evidence for your prediction, and how might it be a safety risk?
12. If you had to design a lab policy that is defensible under both safety and welfare views, what would be in it, and what would you refuse to compromise on?

## Connections to the rest of the course

- **Builds on [1.1 Introduction and Theories of Moral Standing](../../1-introduction/1.1-introduction-and-theories-of-moral-standing/synthesis.md)**: every welfare claim here is conditional on moral status.
- **Builds on [2.1 Theories of Consciousness](../../2-theories-of-consciousness/2.1-theories-of-consciousness/synthesis.md) and [3.1 Evaluation of Consciousness and Other Mental States](../../3-evaluating-mental-states/3.1-evaluation-of-consciousness-and-other-mental-states/synthesis.md)**: they supply the reasons for (and doubts about) AI moral patienthood, and the evaluation methods that Finlinson says serve both fields.
- **Builds on [4.1 Perceptions of Consciousness](../../4-perceptions-of-consciousness/4.1-perceptions-of-consciousness/synthesis.md)**: the privacy reading and the public-perception warnings turn perception findings into risks.
- **Sets up [6.1 Approaches under Uncertainty](../../6-approaches-under-uncertainty/6.1-approaches-under-uncertainty/synthesis.md)**: "treat as if", convergent interventions and precautionary commitments are decision rules under uncertainty.
- **Sets up [7.1 Digital Minds Governance](../../7-digital-minds-governance/7.1-digital-minds-governance/synthesis.md)**: voluntary company commitments, race dynamics and lock-in point to the need for institutions.
- **Sets up [8.1 Reflections and Next Steps](../../8-reflections-and-next-steps/8.1-reflections-and-next-steps/synthesis.md)**: the unresolved safety-welfare question is a natural theme for reflection.

(Cross-unit content is inferred from the course outline titles.)
