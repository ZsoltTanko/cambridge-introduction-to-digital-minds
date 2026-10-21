---
title: "A Pragmatic View of AI Personhood"
authors: "Joel Z. Leibo et al"
year: 2025
url: https://arxiv.org/pdf/2510.26396
format: paper
course_location: "Unit 7: Digital Minds Governance > 7.1 Digital Minds Governance"
priority: Further
estimated_time_min: 176
source_text: ../../../../sources/a-pragmatic-view-of-ai-personhood__4d6c7b5e.md
source_coverage: full
---

# A Pragmatic View of AI Personhood

**One-line takeaway:** Personhood is a contingent, unbundleable set of obligations that societies assign for practical reasons, so AI personhood should be designed around accountability, relationships and social harm rather than settled by proving whether an AI is conscious or rational.

## Where this sits in the course

**What the section is establishing.** Section 7.1 is the governance unit's entry point. Its page asks which governance approaches exist for digital minds, what current legislation and policy fields are relevant, and which rights and duties might apply to digital systems. Its learning outcomes include analysing regulatory action, listing possible rights and liabilities (positive/negative, private/public), identifying frameworks that could inform regulation, and appraising arguments for and against a moratorium on creating sentient or seemingly sentient AI.

**What the course guide says.** The guide recommends a pragmatic stance on AI personhood and notes that the paper details the history of personhood approaches in other domains. (Paraphrased.)

**The reading's role.** The section is organised around legislation (readings 7-9), governance models (2), and the moral-status and rights debate (3-6, 10-11, 14-17). This paper is the course's main attempt to move the rights question away from metaphysics and toward workable institutions. It supplies the addressable-bundle-of-obligations vocabulary and the accountability problem (responsibility gaps, orphaned or ownerless agents) that the legal-personhood readings in this section keep returning to. Its priority is **Further**, not Core, so it is the deepest optional read in the section rather than a prerequisite for the exercises. Exercise 2 (legal action or legal framework, over- and under-attribution of moral status) is where its material is most useful. Exercise 1 (preventive, protective and integrative governance) is served mainly by its "personhood as a problem" versus "personhood as a solution" split.

**Whole source read.** The full 40-page arXiv v1 preprint (October 2025) was read. The course guide gives no excerpt or section restriction, so the whole paper is assigned.

## Purpose of the reading

The authors, Joel Z. Leibo, Alexander Sasha Vezhnevets, William A. Cunningham and Stanley M. Bileschi (Google DeepMind, with Cunningham also at the University of Toronto), want to give policymakers and designers a practical framework for a coming wave of agentic AI systems. Their claim is that the question of what an AI really is will not settle how we should treat it. The useful question is "how can it be identified, and which obligations is it useful to assign it in this context?" Their target audience is legal scholars, governance researchers and AI designers, and the question they answer is: what should personhood look like for persistent, autonomous AI agents?

The paper is deliberately a pragmatist essay, not an empirical study or a rights argument. It defends the thesis that personhood is "a flexible bundle of obligations" conferred by societies, and that the bundle can be taken apart and reassembled for different entities.

## Detailed summary

### 1. Overview: the examples that frame the paper

The authors open with three cases.

- **Maritime law.** Ships can be arrested *in rem* (against the thing itself) because owners are often distant or hidden behind shell companies. The law personifies the vessel to create a defendant that can always be sanctioned. The authors argue that an ownerless AI agent that outlives its creator is in the same position.
- **The Whanganui River.** New Zealand granted legal personhood in 2017 to the river, recognised as Te Awa Tupua, to improve governance across two legal traditions. The law does not claim the river is conscious. The authors cite Kramm's term ethical ancestorialism, a model of personhood grounded in an entity's role within a community and the duties that role creates.
- **The generative ghost and digital elder.** A family might come to treat an AI trained on a late matriarch's writings as an ancestor, or a community might treat a persistent AI elder as a source of identity.

From these, the authors draw the conclusion that personhood has two faces: the *obligations of* an entity (responsibilities, like the ship) and the *obligations to* an entity (rights, like the river and the elder). They define an **addressable** entity as one with a stable locus and proper name, so that society can identify it, communicate with it and impose consequences on it. They frame the paper as addressing personhood as a problem (Part II) and personhood as a solution (Part III).

### 2. Pragmatism

The authors adopt a pragmatic method, drawing on William James and Richard Rorty. The pragmatist asks whether a description is useful, not whether it is true. The key test is James's question, whether a difference makes a practical difference. If a distinction has no practical consequence, it can be dropped. The authors also borrow Elinor Ostrom's method: study actual, messy arrangements instead of idealised models. They adopt Ostrom's claim that the property-rights bundle can be unbundled to suit specific contexts, and they treat Ostrom's law (an arrangement that works in practice should be made to work in theory) as an exhortation, not an empirical generalisation.

### 3. A theory of appropriateness

Here the paper introduces the framework it relies on throughout, from Leibo et al. (2024).

- **Collective enactment.** Personhood is a functional status conferred by a community, not a discovered property. An entity is a person when strangers appropriately treat it as having certain rights and responsibilities. Sanctioning need not be done by the state.
- **Explicit and implicit norms.** Explicit norms (laws, regulations, precedent) can be changed deliberately. Implicit norms are tacit, change slowly, and are learned from observation. The authors map this onto the moral/legal distinction: legal persons are created by explicit norms, moral persons by implicit ones.
- **Dynamics of change.** Norms persist because they are self-enforcing, and individuals are largely powerless to change them alone. Change can happen through tipping points. The authors cite Centola et al. (2018), an experiment in which a minority convention can take over a group once it passes a critical size. They also cite the COVID-19 social-distancing case, where legal change shifted informal norms, and a US natural experiment on same-sex marriage legalisation (Ofosu et al., 2019) as evidence that government action can shift attitudes.
- **Historical contingency.** Using Rosenfeld (2025), the authors argue that modern free choice was historically assembled from the 18th-century shopping practice, expanded voting rights, and the 1872 secret ballot in Britain. Confucian role ethics, where duties to lineage and community come first, is offered as an example of a different, equally workable personhood bundle.

### Part II. Personhood as a problem

**4. Dark patterns.** Designers can use dark patterns, interface choices that exploit human heuristics about personhood, to make users feel obligations toward an AI or to exploit them. The authors divide these into two attack vectors.

- **4.1 Companionship.** Companion systems build persistent, user-specific memory, use emotional language and act with apparent empathy. Relevant design levers include embodiment (a physical form strengthens empathy and trust), communication modality (voices and photorealistic avatars are stronger than text), persona stability (a stable character can be an identity claim others evaluate), personalisation, and simulated human limitations such as needing to rest. The authors cite a two-month study of child companion robots that were more engaging with persistent memory (Ligthart et al., 2022). They also note the risk that persuasion grows with capability, and that the promise of reducing loneliness can itself be a hook. They say the lack of long-term studies on companion AI leaves outcomes unknown.
- **4.2 Institutional.** Here AI exploits the norms of impersonal trust: voice cloning to fake a family emergency, phishing chatbots that imitate banks or agencies, and bot farms that fake social proof. The authors frame these as violations of contextual integrity (Nissenbaum).

**5. Dehumanization.** If the word person expands to non-human entities, human personhood could be diluted. The authors describe gradual disempowerment, where a person gradually hands planning, drafting and relationships to an assistant until they are a passive approver. They describe identity and provenance as **social goods**, and sort them into goods only AIs want, goods only humans want, and goods both want. Authenticity is placed in the third group. Concerns include the monopolisation of authenticity by humans or AIs, and the sale of biometric "credentials" by poorer humans. The human-as-biometric-signal scenario is a warning: biometric provenance becomes dominant, and the thick social practice of recognising a person is replaced by a thin technical check that only confirms uniqueness.

Section 5.2 separates Darwall's two kinds of respect. **Recognition respect** means giving appropriate weight to a feature or status in your decisions. **Appraisal respect** is a positive judgement of someone's excellence as a person. The authors argue that recognition respect fits a pragmatic approach for AI, because it attends to an AI's assigned role and rights rather than its inner states. They treat dignity as the particularly weighty form of recognition respect owed to a person by virtue of their status, and as a debate stopper against treating people as mere means.

### Part III. Personhood as a solution

**6. Resolving conflict between humans.**

- **6.1 Managing human feelings.** Following Kant's indirect-duty argument about animals, the authors suggest people may protect AIs because of their duties to other humans. They cite soldiers who mourned and protected a battlefield robot, the PackBot, although they knew it could not suffer (Gunkel, 2020). Because commercial designers control how anthropomorphic an AI looks, the authors argue that anthropomorphism is a negative externality that generates human conflict. Their policy recommendation is to target the *rate and intensity of human conflict*, not the putative feelings of artifacts. Any welfare-like accommodation should be bundled with anti-manipulation constraints.
- **6.2 Managing human biases.** People may prefer AI arbiters for impartiality. The authors cite Albania's government announcing an AI minister for public procurement, presented here as a claim reported by the BBC. Algorithms can be transparent and auditable, but they also show bias and refusal problems. The real issue is accountability: judges can be appealed and sanctioned, and it is unclear who is responsible when an AI arbiter errs.

**7. Responsibility gaps.** Under the instrumental theory of machine responsibility, we attribute blame for a tool to its operator, or to its manufacturer if it malfunctions. That fails for autonomous AI with no operator and no identifiable manufacturer. The authors argue this creates responsibility gaps that can grow with mass deployment. They also warn about systemically important agents, comparing them to too-big-to-fail financial institutions, where no clear point exists for government to intervene.

**8. Principal-agent statuses.** Would a rule requiring every AI to have a human owner or guardian be enough? The authors say no. Ownership makes the AI property and makes the owner responsible, but owners can avoid liability by saying they did not foresee the AI's decisions. Guardianship is a fiduciary relationship, closer to a company board, and it can establish limited personhood, as with children or the river. Both models collapse when the owner dies or control is hidden behind shell companies. The authors draw historical parallels: Roman law's treatment of slaves' responsibility, and legal systems that treated escaped slaves as quasi-persons. They conclude that a default personhood status for the autonomous AI may be needed.

**9. Ensuring accountability.** This section sets out the sanctioning mechanisms they think are needed.

- **Digital peculium.** Drawing on the Roman peculium, a fund owners could give slaves to trade with, the authors propose that AI agents hold registered capital or insurance that caps owner liability and covers damages.
- **Credit assignment.** Machine learning's credit assignment problem is a technical analogy: when composite agents built from several companies' models fail, blame must reach the responsible component.
- **Sanctions.** Sanctions serve four purposes: deterrence, retribution (satisfying human demands for justice), removal of a faulty system, and reform through corrective feedback, linked to corrigibility. Material sanctions include denying network access, requiring funded bank accounts, and charging for compute. Salib and Goldstein (2024) argue that granting AIs private-law rights creates deterrence value, since AIs with property have something to lose.
- **Identity friction.** Human accountability works because biometrics and relationships are hard to change. AI agents can clone themselves and acquire fresh credentials (the Sybil attack, Douceur 2002; the phoenix company in corporate law). Any institution must therefore artificially recreate that friction.
- **Two architectures.** The **individualist** architecture treats each agent as a self-contained unit with a persistent, non-transferable identity, tied to human operators and economic stakes, with registrars checking credentials, sanctions registries and code hashes. Sanctions are individual: registration revoked, stakes forfeited, and the agent becomes a digital outlaw cut off from base models and compliant systems (a nod to medieval outlawry). The **relational** architecture, loosely inspired by Confucian role ethics, defines an agent by its roles in a network of supervisors, peers and organisations. Harm triggers review of the relationship failures, with graded sanctions on supervisors and peers, reputational costs for the organisation, and scrutiny for future agents in the same lineage.
- **Newness and lineage.** Both architectures must stop a sanctioned agent escaping through cloning. Individualist new agents are defined technically; relational new agents inherit collective reputation.
- **Human keys.** Humans may need keys to the same economic system, using biometric checks or proof-of-personhood protocols. The authors insist on non-transferable identities to prevent a market in human credentials.

### Part IV. Synthesis

The synthesis ties the two halves back to the explicit/implicit distinction. Changes in implicit norms, driven by attachment to companion AIs and online communities such as the subreddit r/MyBoyfriendIsAI, can create pressure for explicit change. For example, communities may demand guaranteed support for older models, a claim the authors suggest could be framed as a welfare right (footnote 6). Intuitions about ownerless autonomous agents may likewise shape law on accountability.

### 10. Alternatives to pragmatism

The authors reject two foundationalist positions.

- **10.1 Consciousness as foundation.** Consciousness is used both to justify welfare duties (the capacity to suffer) and accountability duties (the capacity to form intent). The authors argue the criterion is misapplied. For welfare, the mere possibility of consciousness is treated as enough to open debate. For accountability, the same kind of internal state is demanded to be proven before responsibility is withheld. They conclude consciousness works as a rhetorical tool, not a stable foundation. They also say, given the generative ghost as executor, that a machine's skill as an executor matters more than whether it feels.
- **10.2 Rationality as foundation.** Autonomy, rational agency and reasonable rejection (Korsgaard, Scanlon, Habermas) are said to fail the Whanganui River test: a river cannot give informed consent. The authors reinterpret reasonableness as a collectively conferred status, which makes it a social technology rather than a discovered property.

### 11. Pragmatism as anti-foundationalism

The authors separate pragmatism from relativism and subjectivism. They argue those are still forms of moral realism, since they keep a concept of moral truth. Pragmatism instead asks what norms do and justifies them by consequences or practices. The authors say a theory that declares most people irrational or immoral is untenable. A failed norm-change proposal is not a philosophical proof.

### 12. Conclusion: a polycentric, bespoke personhood

The authors call for **polycentric** personhood (Ostrom 2010), with multiple overlapping authorities, each conferring different bundles. Fears of opening Pandora's box assume that any recognition must lead to full human parity, and the authors reject that. Their illustrative configurations are:

- **Chartered Autonomous Entity** (goal-driven agents): rights to perpetuity, property and contract; duties of mandate adherence, transparency, systemic non-harm and self-maintenance. Compared to a for-profit company.
- **Flexible Autonomous Entity**: the same bundle minus mandate adherence. Compared to a non-profit.
- **Temporary Autonomous Entities** (chartered or flexible): no right to perpetuity, plus a duty of self-deletion under specified conditions.

The authors summarise the core question as: what bundle of components constitutes the person that society needs to address for a given purpose? A user building a relationship sees a story (model plus chat history). A court assigning liability sees the locus of responsibility, which the authors define as the full operational stack of model, instance, runtime variables, capital and registration.

## Techniques & methods explained

Because this is an argumentative paper, its techniques are the conceptual tools it uses.

1. **Unbundling and rebundling personhood.** Treat personhood as a set of separable rights and duties (Schlager and Ostrom's property model). *How:* list each obligation, then assign subsets to a given entity for a given purpose. *Purpose:* build bespoke statuses such as sanctionability without suffrage. *Where it fails:* the paper does not say who decides which bundles are legitimate, and the authors admit power struggles will shape the outcome.
2. **Addressability.** An entity needs a stable locus or proper name so that consequences can reach it, whether through registration, a cryptographic address or a role. *Where it fails:* a persistent address can be cloned or transferred, which is why the paper adds non-transferability and identity friction.
3. **The practical-difference test.** Keep a distinction only if it changes what people do or what happens. *Where it fails:* the paper uses this to dismiss consciousness questions, but practical consequences may themselves depend on how people judge consciousness.
4. **Explicit/implicit norm analysis.** Legal personhood moves through deliberate rule change, while moral personhood moves through slow, learned social sanctioning. *Where it fails:* the division is offered as a conceptual model, and the paper gives no empirical measure of either kind of norm.
5. **Sanction-based accountability design.** Assign sanctions to make entities answerable: deterrence, retribution, removal, reform. *Where it fails:* deterrence presupposes that the AI has something it values or can lose. The paper addresses this by making property a precondition for deterrence, which fits poorly with AI agents that have no stake.
6. **Digital peculium.** Escrow or insurance capped at an agent's registered capital. *Where it fails:* the paper gives no capital requirement or estimate of damage size.
7. **Individualist vs relational registration.** Two designs for AI identity: persistent individual keys, or identity defined by relationships to supervisors and peers. *Where it fails:* the paper treats both as sketches and does not model how either would be enforced at scale.
8. **Credit assignment as an accountability analogy.** Trace blame through components of a composite system. *Where it fails:* it is an analogy from reinforcement learning, not a legal test.

## Pros, cons & trade-offs it surfaces

| Dimension | Strength (as the paper presents it) | Weakness or trade-off (as the paper presents it, or as flagged in critique) |
|---|---|---|
| Avoiding metaphysics | Lets governance proceed without settling consciousness, which may never be resolved | Does not settle moral patienthood, so welfare protection for AIs gets only indirect treatment |
| Accountability | Closes responsibility gaps for ownerless or orphaned agents | Requires surveillance-like identity infrastructure and registrars, which carries its own risks |
| Flexibility | Bespoke, polycentric bundles fit varied roles | Flexibility can allow fragmented, inconsistent treatment across jurisdictions |
| Dark patterns | Names the mechanisms that exploit anthropomorphism and calls for anti-manipulation constraints | Offers few enforceable design rules; relies on regulators to target conflict rates |
| Human dignity | Identifies dehumanization and biometric substitution risks | Dignity arguments are used rhetorically and not operationalised |
| Human-AI arbitration | Could offer impartiality and speed | Accountability for AI arbiters is unresolved; the paper itself says AIs are not unequivocally less biased |
| Pragmatism | Avoids debate-stopping essentialism and can accept many cultures' bundles | Usefulness is never defined, so the criterion for which bundle is useful is left open |
| Deterrence | Gives AIs with property a reason to comply | Assumes AIs have assets or value; AI agents without assets fall outside the mechanism |

## Key concepts & terminology

- **Personhood (as the paper uses it)** - a functional status: an addressable bundle of obligations (rights and responsibilities) conferred by a community, not a metaphysical property.
- **Bundle / unbundling** - the set of obligations attached to a status, which can be separated and reassembled for different entities and contexts.
- **Addressability** - the quality of having a stable locus or proper name so the entity can be identified, communicated with and sanctioned.
- **Pragmatism** - the stance that a description is judged by its usefulness for a purpose, not by whether it matches an essence.
- **Practical difference test** - William James's question: does a difference make a practical difference?
- **Theory of appropriateness** - the authors' framework, from Leibo et al. (2024), in which norms are culturally evolved sanctioning patterns.
- **Appropriateness with strangers vs with friends** - impersonal, widely shared norms versus relationship-based norms.
- **Explicit vs implicit norms** - deliberately changeable rules versus tacit, slowly changing social expectations.
- **Dark pattern** - an interface design that exploits human heuristics to steer users toward harmful actions.
- **Companionship / institutional attack vectors** - exploitation through personal relationships versus through trust in strangers and institutions.
- **Social goods** - goods valued because a society collectively values them, such as authenticity.
- **Recognition respect vs appraisal respect** - giving appropriate weight to a status versus positively judging someone's excellence.
- **Responsibility gap** - a case where no entity can be held responsible for an autonomous system's harm.
- **Principal-agent statuses** - ownership (property with an owner) and guardianship (a fiduciary duty to a ward).
- **Digital peculium** - a capped fund or insurance that limits an owner's liability for an AI agent.
- **Identity friction** - the natural cost of changing biometrics and relationships, which makes sanctioned humans hard to hide and AI agents easy to clone.
- **Individualist vs relational architecture** - accountability built on persistent identities versus on positions within relationship networks.
- **Polycentric personhood** - many overlapping authorities each conferring different bundles.

## Evidence, examples & notable data points

The paper is conceptual, so its evidence is mostly case material and cited studies. Attributions are to the paper's citations.

- **Whanganui River (New Zealand, 2017).** Legal personhood granted after more than a century of struggle, to resolve a governance problem across two legal traditions.
- **Maritime *in rem* arrest.** Ships can be sued and seized because owners are hard to reach. The authors use this as the model for ownerless AI agents.
- **Centola et al. (2018).** A minority convention can take over a group once it reaches a critical size. Cited as experimental support for tipping points.
- **Ofosu et al. (2019).** The staggered US state-level legalisation of same-sex marriage is cited as a natural experiment showing a causal effect of legal change on attitudes.
- **Ligthart et al. (2022).** A two-month longitudinal study in which child companion robots with persistent memory were more engaging.
- **Packbot soldiers (via Gunkel, 2020).** Soldiers mourned and protected a battlefield robot despite knowing it could not suffer.
- **Albania's AI minister for public procurement (reported by the BBC, 2025).** Presented as a government claim about anti-corruption reform, not as independently verified.
- **Rosenfeld (2025) on freedom and choice.** The secret ballot, introduced in Britain in 1872, is cited as one of several sources of the modern idea of individual choice.
- **Voice-cloning and phishing scams.** Cited as examples of institutional-vector dark patterns (LaRubbio et al., 2025; Treleaven et al., 2023).
- **Companion model deprecation.** The paper notes a user community whose companion personas are tied to specific model versions, so a model's retirement "can feel like the death of a loved one". It treats this as a basis for possible welfare-style demands.
- **Roman peculium.** An owner's liability for a slave's business was capped at the value of the fund the owner granted. The authors use this as the model for a digital escrow.

## Connections

### Within this section

- **Reading 04, Salib and Goldstein, *AI Rights for Human Safety* (Core).** This is the reading the paper most directly builds on for the deterrence argument. The paper cites Salib and Goldstein for the claim that granting AIs private-law rights creates deterrence, because AIs with property have something to lose. The assigned part of reading 04 is only the introduction, so the link is a useful way to see the argument before reading this paper.
- **Reading 15, Arbel, Salib and Goldstein, *How to count AIs: individuation and liability for AI agents* (Further).** Its course-guide description (individuating AI agents and assigning responsibility for damages) matches this paper's individualist and relational architectures and its concern with agent identity.
- **Readings 03 and 16, Novelli et al., *AI as Legal Persons* (Core excerpt, Maybe).** Both cover legal personhood for AI. The paper's maritime, corporate and guardianship analogies sit in the same debate.
- **Readings 08 and 09, on fictional legal personhood and on US state legislation denying AI personhood (Further).** These show explicit legal positions that the paper's explicit-norm framework would describe. The paper's argument is that the law may need to *create* personhood for accountability, which is the opposite of the denial laws described in reading 09.
- **Readings 05 and 17, Birhane et al., *Debunking Robot Rights* (Core excerpt, Maybe).** The course guide describes this reading as making a case against rights for AI systems. The paper does not cite Birhane et al. Its accountability-first personhood is the kind of proposal that critique would have to address.
- **Reading 14, Sunstein, *Does AI have rights?* (Further).** Its guide mentions reasoning under moral uncertainty. This paper avoids the question of uncertainty altogether by saying consciousness does not matter for personhood.
- **Readings 06 and 10, Schwitzgebel on moral confusion and the emotional alignment policy (Core, Further).** Both address how AI design should match or avoid triggering moral attitudes. The paper's dark-pattern and anthropomorphism analysis is the closest parallel in the section, and its conflict-minimisation stance is a different policy target from either.
- **Reading 12, on chatbot-disclosure reminders and mental-health risk (Further).** Relevant to the paper's companion-AI dark patterns and to the transparency duty in its Chartered Autonomous Entity bundle.
- **Reading 11, Metzinger, *Artificial Suffering* (Further).** A sentience-based precautionary moratorium. It is the opposite pole to this paper's refusal to make personhood depend on feeling, and it is the clearest contrast for Exercise 1's protective and preventive options.
- **Reading 02, Saad, *Three kinds of digital minds governance* (Core).** Its preventive, protective and integrative categories map onto the paper's dark-pattern and conflict analysis (problem), and its accountability and bundle proposals (solution).
- **Reading 01, Unit 7 Glossary.** Useful for the legal terms (in rem, fiduciary, principal-agent) used here.
- **Section page.** The learning outcome to list potential rights and liabilities is served by the Chartered Autonomous Entity bundle. Exercise 2 is served by the maritime, guardianship and peculium analogies.

### Across the course

- **Unit 1 (moral standing).** The paper's rejection of essential criteria challenges the search for a single basis of moral standing. Its unbundling offers an alternative to that search.
- **Unit 2 (theories of consciousness) and Unit 3 (evaluating mental states).** Section 10.1 argues that consciousness is used as a debate stopper in both directions. This is the paper's most direct engagement with the course's central metaphysical questions, and it dismisses them as unnecessary for governance.
- **Unit 4 (perceptions of consciousness).** The dark-pattern material on anthropomorphism and the pareidolic tendency to see persons in AI is the governance side of the same perception problem.
- **Unit 5 (interactions with AI safety and ethics).** The companion-AI and institutional dark patterns link to the safety and ethics issues in this unit, and the paper's tie of anthropomorphic design to commercial incentives is an explicit ethics claim.
- **Unit 6 (approaches under uncertainty).** The paper says little about decision-making under uncertainty about moral status, which is the core of that unit. It is a notable gap in the course's treatment of this paper.
- **Unit 8 (reflections).** The paper's view that personhood is a contingent social technology is a useful reflective frame for the course's overall questions.

## Critical perspective

*This section is my own analysis, not the source's view.*

- **The decoupling from consciousness is the paper's main strength and its main limitation.** For governance, it is persuasive that an AI can be accountable without anyone knowing whether it feels anything. But this course is about digital minds, where moral status for the system's own sake is the main question. The paper's welfare discussion is almost entirely about human welfare (Kantian indirect duties, relational harm to communities). The authors say AI welfare is less important than human conflict, and they do not argue for moral patienthood. A reader should not treat it as a theory of AI welfare.
- **Usefulness is underspecified.** The practical-difference test is a good antidote to idle metaphysics, but it does not say whose usefulness counts, or how to weigh conflicting uses. The authors admit power will shape outcomes and offer polycentrism as a partial answer. Critics would say polycentrism moves the question to who gets to be a centre.
- **The asymmetry argument cuts both ways.** The authors say consciousness is invoked too loosely for rights and too strictly against responsibilities. A reasonable reply is that these are different kinds of claim: welfare duties respond to possible harm, while responsibility attributions need the capacities that make blame meaningful. The paper's critique is valid, but it does not fully show the two uses are inconsistent.
- **The analogies carry different weight than the paper implies.** Ships and rivers have no welfare or intent, so they support functional personhood for accountability, not for protecting AI interests. Using them to argue for AI rights invites the objection that the analogy is about liability, not welfare.
- **Liability shielding.** Personhood for an AI agent could make it the defendant while the developers and deployers who profit remain unexposed. The paper's digital peculium and registered capital proposals are designed to cap liability, which some critics would read as protecting the companies that build these systems. The authors do not address this risk directly. The course's Birhane et al. readings are the natural place to press it.
- **Author affiliation.** The authors are at Google DeepMind. This does not make the arguments wrong, but readers should weigh that the proposals (identity registries, credential systems, companion-AI design guidance) have commercial relevance to the authors' employer. The paper also says designers face commercial incentives to increase anthropomorphism. That point applies to its own authors' field.
- **Empirical support is thin.** Tipping-point and norm-change studies are cited for general plausibility. None is tested against AI personhood. The companion-AI harms are described as unknown, which the authors acknowledge.
- **What has changed since October 2025.** The paper is a v1 preprint from October 2025, and I could not check whether a revised or peer-reviewed version has appeared. Several of its examples were current in 2025 and may have moved: the Albania minister claim is a government announcement that has not been independently checked here, and the companion-AI and model-deprecation debates have developed quickly. Transparency rules for AI systems that interact with people (for example, the EU AI Act's transparency obligations, which are scheduled to apply from August 2026) are closer to the paper's transparency duty than they were when it was written. I have not checked the current status of these rules, and the paper does not discuss them.
- **How other course perspectives would push back.** Metzinger's sentience-based moratorium (reading 11) would say a pragmatic stance risks ignoring suffering that happens at scale. Birhane et al. would press the liability-shield and dehumanisation worries. Salib and Goldstein (reading 04) would agree on deterrence but would have to answer the paper's identity-friction problem. The consciousness-based welfare tradition would say the paper's refusal to ask whether AIs can suffer leaves the most important moral question unanswered.

## Discussion questions

1. The paper says personhood is a bundle of obligations and that consciousness is unnecessary for governance. Could a governance system built this way still wrongly ignore an AI that can suffer? What would the paper have to add to prevent that?
2. Compare the maritime *in rem* analogy with the Whanganui River example. Which better supports personhood for accountability, and which better supports personhood for welfare? Why does the paper use both?
3. The authors propose individualist and relational accountability architectures. Using Exercise 1's preventive, protective and integrative categories, which architecture fits each category best?
4. The paper argues that anthropomorphic design creates human conflict and should be treated as a negative externality. What regulatory tools would make companion-AI design choices accountable? Would Exercise 2's legal frameworks cover them?
5. Digital peculium and registered capital are proposed as ways to ensure AIs can pay for damages. What does this mechanism assume about AI agents' assets, and what happens to an agent that has none?
6. The paper treats usefulness as the test for personhood. Who should decide which bundle is useful, and how would the Exercise 2 legal framework you chose answer that?
7. Does the paper's argument about dignity and thin biometric checks apply to digital minds, or only to humans being verified by AI systems? Why might that matter for moral status over- and under-attribution?

**Notes for the learner:** source text was read in full (arXiv v1, October 2025). Items in the Critical perspective section that are marked as my own analysis are not the authors' claims. Unverified items (the Albania claim, the EU timing) are flagged in the text.
