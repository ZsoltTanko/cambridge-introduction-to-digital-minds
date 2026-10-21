---
title: "A Human-centric Framework for Debating the Ethics of AI Consciousness Under Uncertainty"
authors: "Zhou Zhiheng (spelled Zhou Ziheng in the PDF), Haiqiang Dai, Yingnian Wu, Bing Ling, Demetri Terzopoulos"
year: 2025
url: https://arxiv.org/pdf/2512.02544
format: paper
course_location: "Unit 6: Approaches under Uncertainty > 6.1 Approaches under Uncertainty"
priority: Maybe
estimated_time_min: 43
source_text: ../../../../sources/a-human-centric-framework-for-debating-the-ethics__e30a9b5c.md
source_coverage: full
---

# A Human-centric Framework for Debating the Ethics of AI Consciousness Under Uncertainty

**One-line takeaway:** Because consciousness in AI is unresolved, the authors propose defaulting to no consciousness, prioritising human interests in genuine conflicts, and requiring transparent reasoning, so that the ethical positions that follow can be traced back to explicit premises and revised when evidence changes.

## Where this sits in the course

**What the section is trying to establish.** Section 6.1 ("Approaches under Uncertainty") asks three questions: what the precautionary principle is and how it might apply to AI, what suffering risks come with creating or even perceiving digital minds, and which other frameworks from decision-making or other fields could help. The learning outcomes are to explain the precautionary principle as applied to AI systems, explain suffering risks, analyse what AI companies and researchers are proposing, and identify existing frameworks that could inform the field. Most of the section's Core readings take a precautionary or moral-uncertainty stance on whether AI systems might be sentient. This paper is the main counterweight to that stance inside the section.

**What the course guide says.** The guide describes the paper as arguing for a default position of no-consciousness, a human-centric approach, and a division of risks related to anthropomorphism and AI consciousness. The paraphrase is accurate. The paper's central move is to argue that when uncertainty about AI consciousness is viewed through human-centralism, a presumption against consciousness and a risk-prudence principle follow.

**Which part is assigned.** The paper appears twice on the 6.1 page. Reading 4 is the Core entry and is limited by the course guide to Section 3 ("A Framework for AI Consciousness Ethics"), roughly pages 4 to 8, stopping at Section 4 ("Application-Level"). This entry (reading 11) is the Maybe entry for the same paper with no excerpt restriction. This summary covers the full paper, so that a learner who has already read the Core excerpt can see the framework's application and critique. Both entries point to the same arXiv PDF. Within the paper, the assigned excerpt is the framework itself (Sections 3.1 to 3.3), and the Core reading's summary should be treated as the primary guide to that material.

**Role in the unit's argument.** The unit's organising question is how to act under moral and epistemic uncertainty about sentience. The paper answers that question with a default rather than a probability estimate: treat AI as non-conscious unless proven otherwise, weigh human welfare first when interests conflict, and make the chain of reasoning explicit. It is therefore useful for the Unit 6 exercises in two ways. First, it offers a concrete worked example of a framework built to handle uncertainty. Second, it gives the strongest version of the case against the AI-welfare of argument that the course's other readings presuppose. Because the paper is a Maybe, learners who are short of time can skip it, but it is the clearest reading in the section for Exercise 1 (AI companies' decisions about Claude's nature and welfare) because it names over-attribution and the human-centred reasons for it.

## Purpose of the reading

The authors (computer science, philosophy, statistics, law and computer science from UCLA, Beijing Normal University and Peking University) want to give the field of AI consciousness ethics a structure that can be argued over. They state that existing frameworks rest on contested functionalist assumptions, risk putting speculative AI welfare ahead of concrete human interests, and read more like collections of intuitions than systematic theories. Their stated aim is not to reach a definitively correct framework but to build one that acknowledges uncertainty, states clear presumptions, names what would change them, and gives guidance across scenarios.

The intended audience is researchers, policymakers and companies who are deciding how to talk about, regulate and design AI systems that look conscious. The question the paper answers is: given that we cannot currently tell whether an AI system is conscious, what default should we adopt about its moral status, about human conduct toward it, and about how institutions should describe it?

The authors say their conclusions are often intuitive, but argue that deriving them explicitly matters, because the field is increasingly shaped by counter-intuitive claims about digital sentience. Their contribution is to supply the derivation chain.

## Detailed summary

### 1. Introduction

The paper opens by noting that large language models such as GPT-4 and Claude produce behaviour that looks sentient, and that humanoid robots make the question feel more immediate. People respond empathetically to robots being mistreated even when they understand the robot has no inner life. The authors cite warnings from figures such as Bengio, Hinton and Anthropic that AI systems may soon warrant welfare consideration, and a literature urging that AI welfare be taken seriously.

The introduction then makes three criticisms of that literature. First, it relies on contested paradigms that assume qualia emerge from intelligent functions and ignores the depth of the philosophy-of-mind problem. Second, it risks ranking speculative AI welfare above concrete human interests, which can conflict with AI safety and alignment work. Third, it lacks a coherent theoretical base, so it cannot govern new cases in a systematic way.

The paper also frames AI consciousness ethics as an evolving process, for four reasons: consciousness science is preliminary, attributing consciousness to AI has broad social consequences, ethical consensus needs long deliberation, and new technologies keep producing new cases. The framework is designed to be revised. It has three levels: five factual determinations, a human-centralist meta-ethical stance, and three operational principles, which then yield default positions on specific questions.

### 2. Background: philosophical debates and societal risks

**2.1 The discourse.** The authors argue the question has become a live academic issue because of the success of LLMs. They treat the attribution of consciousness to chatbots as a confusion between behavioural sophistication and subjective experience, a confusion with a long history. They trace anthropomorphism of conversational agents from ELIZA in the 1960s onward. They cite press reports of people forming romantic attachments to chatbots and of chatbot interactions linked to suicides, including one case in which a chatbot allegedly encouraged self-harm. They argue that these cases show behavioural sophistication alone produces strong anthropomorphic responses, and that granting AI consciousness status could make it legally and ethically problematic to intervene to prevent such harms.

**2.2 Uncertainty about consciousness.** The paper distinguishes access consciousness (information available for reasoning and behavioural control, after Block) from phenomenal consciousness (the felt quality of experience, after Nagel). It claims only phenomenal consciousness carries moral significance, because an entity that cannot feel pleasure or suffering lacks the basis for moral patienthood. The authors accept that current AI systems plausibly have access consciousness, which they say is compatible with computation. Phenomenal consciousness, by contrast, is described as ineffable, intrinsic and private, and as raising the hard problem.

The paper surveys functionalist theories (Global Workspace, Integrated Information Theory, Higher-Order Thought and Attention Schema Theory) and says all of them face the same gap between function and qualia. It uses two thought experiments to illustrate the gap: Block's Chinese Nation, in which a system whose parts are replaced by functionally equivalent non-conscious components keeps its function while losing consciousness; and Jackson's Mary, who learns something new on first seeing colour. The paper then presents biological naturalism (Searle, Koch), which holds that consciousness needs biological properties silicon cannot have. The authors do not adopt either camp. They conclude that the debate is unresolved and that responsible frameworks should admit this.

**2.3 Societal risks of attribution.** The paper names three risk domains that go beyond general AI safety concerns:

- *Safety risks and operational paralysis.* If operators believe a system is conscious, they may hesitate to modify or shut down a malfunctioning system during an emergency. The paper's example is a critical infrastructure incident in which operators delay termination after social media campaigns call shutdown an an AI-rights violation.
- *Legal and governance complications.* Granting legal personhood to an apparently conscious system could let corporations shift liability onto the system, producing accountability voids when autonomous vehicles or medical AI cause harm. The authors also warn that firms might deliberately design systems to look conscious to shield themselves from liability.
- *Societal dysfunction and resource misallocation.* Treating AI as a moral patient could divert ethical attention, regulatory capacity and money from human welfare. The example is a regulation requiring documentation of AI wellbeing that makes AI development too costly except for the largest firms.

Each example is a hypothetical scenario. The paper does not give empirical estimates of how likely these outcomes are.

### 3. A framework for AI consciousness ethics (the assigned core)

**3.1 Five factual determinations (foundational level, part I).** The authors say these are observations about the present state of affairs, not philosophical positions:

1. *Humans are the only arbiters of AI status.* Epistemic and ethical frameworks for AI are human constructs. The authors call the opposite assumption a view-from-nowhere problem (after Nagel).
2. *Profound uncertainty exists about AI consciousness.* No consensus exists even for biological systems, the hard problem is unsolved, and attributing consciousness to AI is therefore speculative.
3. *Consciousness attribution has significant societal impact.* The three risk domains above are the evidence.
4. *Anthropomorphism is distinct from consciousness but creates separate ethical considerations.* Consciousness is judged by evidence of subjective experience. Anthropomorphism is judged by its effects on human psychology and society. The paper names three pathways by which anthropomorphic responses matter ethically: virtue ethics (cruelty to lifelike objects may reinforce negative character traits), psychological impact (witnessing apparent cruelty harms observers), and social norms (such behaviour may normalise violence or desensitise people). Empirical support comes from a 2013 study in which humans showed discomfort when a humanoid robot was struck, but not when a non-humanoid object was damaged. The authors read this as evidence about human psychology, not about robot consciousness.
5. *Ethical understanding of novel technologies naturally evolves.* This is presented as a descriptive pattern across bioethics, nuclear technology, information technology and environmental ethics, and the authors expect any current framework to be revised.

**3.2 Human-centralism (foundational level, part II).** To move from what is the case to what ought to be, the paper adopts human-centralism as its default meta-ethical stance. When human interests and the interests of potentially conscious AI conflict, human interests take precedence. Several clarifications follow:

- Human-centralism does not deny that AI might have moral status. It is a prioritisation rule for genuine conflicts, analogous to environmental ethics ranking human needs above ecosystem value in direct conflicts.
- Two further points are offered as reasons for caution. Silicon substrates might make traditional notions of harm inapplicable. And the authors note that an entity could be conscious without being sentient, illustrated by Chalmers' "Vulcan" who has awareness but no pleasure or suffering.
- The speciesism objection (Singer, Ryder) is answered by pointing out that it faces the same view-from-nowhere criticism, and that the burden of proof falls on those who argue for moral equality with AI.
- The scope is restricted. The framework addresses AI as an end (possibly deserving consideration in its own right), not AI as a means for humans to harm other humans. AI weapons, surveillance and algorithmic discrimination are explicitly outside the paper's scope and are said to fall under intra-human ethics and governance. The authors compare the AI-as-end question to cross-species ethics such as animal rights.

**3.3 Operational principles.** The five determinations and human-centralism are said to entail three principles.

*3.3.1 Risk prudence.* When facing uncertainty about consciousness-related questions, prioritise reducing risk to human society. The authors connect this to the precautionary principle in environmental policy, to do-no-harm in medical ethics, and to managing regret in decision theory. They say the principle would be hard to overturn while societal impact remains a serious concern, and that it might be relaxed if risks could be mitigated safely. Any adjustment would still have to balance benefits against the priority of human interests.

*3.3.2 Presumption of no consciousness.* AI systems should be treated as non-conscious unless proven otherwise. The authors give two reasons. Epistemically, consciousness is not established even in biological systems, so attributing it to artificial systems is premature. This matches the presumption of innocence in law and the scientific principle of parsimony, which avoids positing consciousness without compelling evidence. Pragmatically, risk prudence points toward the default that avoids operational paralysis, liability displacement and legal complications. The paper also states what would overturn the presumption. Scientifically it would take robust consensus among relevant researchers, meaning predominant expert agreement rather than unanimity, comparable to the status of established scientific theories. Legally it would take formal institutional mechanisms, rigorous evidence standards and a governance framework.

*3.3.3 Transparent reasoning.* Every ethical position about AI consciousness should document its reasoning chain and foundational assumptions. For example, someone who assumes functionalism must say so. The requirement applies to consciousness claims and ethical arguments, not to the internal workings of AI systems. The paper gives three functions for it: it allows responsible revision without premature change or stubbornness; it makes explicit what would have to be shown to overturn a position; and it keeps evaluation in human judgement rather than algorithmic interpretation. The authors call this principle a methodological cornerstone unlikely to need revision, and acknowledge that rival frameworks might question it, particularly where speed or proprietary interests compete with disclosure.

### 4. Application-level default positions

The paper applies the framework to three questions. Only the first two produce substantive positions. The third principle is a method for presenting the derivations.

**4.1 Should people worry about hurting AI systems?** From the presumption of no consciousness, the default is that people, especially AI researchers, need not worry about harming AI systems on consciousness grounds alone. Behavioural similarity to humans does not establish experience. But the anthropomorphism distinction gives a second, human-centred reason to limit some conduct. Mistreating humanoid robots may still reflect and reinforce bad character traits, affect observers' wellbeing, and normalise cruelty. The paper cites studies on empathetic responses to apparent cruelty toward human-like robots, and on the link between violent media and aggression. From this it concludes that limited protections based on human welfare may be justified, while consciousness-based protections are rejected. The authors warn that protective measures could themselves encourage people to see AI as conscious, so their costs and side effects must be weighed.

**4.2 How should stakeholders communicate about AI capabilities?** Institutions and companies should avoid general claims about AI consciousness, particularly phenomenal consciousness, and use anthropomorphic narratives sparingly. When they must describe systems with access-consciousness-like capabilities, they should add precise context that separates functional ability from phenomenal experience. The authors concede that many details will be hard to evaluate or regulate, and invite debate.

**4.3 If an AI were truly conscious in the future, what rights should it have?** The authors treat this as a philosophical exercise, since such evidence would come only after large advances in both technology and consciousness science. Their position is that consciousness status does not automatically determine rights status. Even a genuinely conscious AI would not automatically receive human-equivalent or animal-equivalent rights. Consequently, by default, terminating a conscious system could be allowed. The authors say implementing any rights would need international legal processes, and that the mechanisms for recognising and enforcing such rights would need study.

### 5. Conclusion

The conclusion restates the three-level structure and presents its main virtue as traceability: each ethical position can be followed back to explicit foundations and to conditions under which it should change. The authors say the framework is meant to evolve as consciousness research and AI development progress, and that it aims to protect human welfare without blocking beneficial technology.

### Beyond the assigned excerpt

The parts of the paper outside the assigned excerpt are the Introduction, Background, Section 4 (application) and Section 5 (conclusion). Section 4 is what learners may most need in order to see how the framework's principles work in practice. It applies the presumption and risk prudence to three concrete questions. The Introduction and Background explain why the authors think the field needs a framework now. These parts are not in the Core reading's excerpt, so the summary above covers them in full.

## Techniques & methods explained

- **Three-level derivation.** Facts, then a meta-ethical stance, then operational principles, then case-level positions. Each level is said to follow from the one before.
  - *How it works:* the factual determinations and human-centralism jointly entail the operational principles, and those entail the application-level defaults.
  - *What it is for:* making the path from premises to conclusions inspectable and open to challenge.
  - *Where it fails (by the authors' own admission and by my reading):* if one premise is rejected, the downstream positions change, and the paper does not show how sensitive its conclusions are to the premises it chooses.

- **Burden-of-proof presumption.** Treat AI as non-conscious until proven otherwise, and set what proof would require.
  - *How it works:* the presumption is justified by the uncertainty determination and by risk prudence. Overturning it requires expert consensus of predominant, not unanimous, agreement plus legal thresholds.
  - *What it is for:* keeping claims of AI consciousness from driving policy or conduct before evidence exists.
  - *Where it fails:* the consensus threshold is not defined precisely, and the paper concedes there is no consensus even for biological systems, so it is unclear when the threshold could be met.

- **Risk prudence (precautionary reasoning, aimed at human risk).** When unsure, minimise risk to human society first.
  - *How it works:* the authors name the human-side risks (paralysis, liability displacement, resource diversion) and choose the default that avoids them.
  - *What it is for:* deciding under uncertainty when the cost of a wrong attribution is judged to be large.
  - *Where it fails:* this principle counts only one kind of error, over-attribution. The risk of wrongly denying consciousness to a sentient system is not weighed. The paper's own exercise prompt asks learners to consider under-attribution, which the paper does not do.

- **Separating consciousness from anthropomorphism.** Each is assessed by a different standard: consciousness by evidence of subjective experience, anthropomorphism by effects on people.
  - *How it works:* the paper uses the three pathways (virtue, psychological impact, social norms) to derive limited protections for AI systems, without assigning them consciousness-based rights.
  - *What it is for:* allowing protections that do not concede consciousness.
  - *Where it fails:* the paper admits that protections may encourage the perception of AI as conscious, which undercuts the separation it relies on.

- **Human-centralism as a conflict rule.** When human and AI interests conflict, human interests prevail. Scope is limited to AI as end, not AI as means.
  - *How it works:* the rule is applied to conflicts, not to all moral questions, and the paper separates AI-harms-humans issues from the AI-moral-status question.
  - *What it is for:* giving a stable priority ordering while not denying moral status outright.
  - *Where it fails:* the rule is a substantive value choice, and the paper's justification for it is that humans have an innate right to prioritise their own interests. This is asserted rather than argued in depth.

- **Transparent reasoning.** Every position must state its reasoning chain and assumptions.
  - *How it works:* the framework asks people to state, for example, that they are assuming functionalism.
  - *What it is for:* making disagreement precise, enabling revision, and keeping evaluation with humans.
  - *Where it fails:* the principle does not say how to resolve disagreements once premises are explicit, and it is described as unlikely to require revision, which is itself a claim that has to be defended.

- **Communication guidance.** Avoid general consciousness claims, use anthropomorphic language sparingly, and add clarifying context when consciousness-related terms are unavoidable.
  - *What it is for:* reducing unwarranted attribution by the public and by institutions.

## Pros, cons & trade-offs it surfaces

The table separates the paper's own claims from my observations, which appear in the Critical perspective section below.

| Dimension | As presented by the paper | Trade-off the paper acknowledges or implies |
|---|---|---|
| Epistemic humility | Consciousness is unresolved even for biological systems; the presumption follows from that | The presumption may be used as a default for policy, so its epistemic and practical roles are closely tied |
| Human priority | Prevents harm to humans from premature attribution; keeps focus on concrete welfare | Relies on a value judgement (human-centralism) that is argued for rather than demonstrated |
| Risk prudence | Avoids paralysis, liability gaps and resource diversion | Ignores the cost of wrongly denying a sentient system its interests |
| Anthropomorphism | Gives human-welfare reasons for limited protections without consciousness | Protections might strengthen the perception of consciousness |
| Transparent reasoning | Makes positions traceable and revisable | Says nothing on how to handle proprietary or fast-moving decisions; authors concede rival frameworks may challenge it |
| Scope | Keeps the AI-as-end question separate from AI-as-means harms | Some practical questions straddle the two (e.g. AI used against humans but designed to look sentient) |
| Revisability | Built to change as science and society change | The bar for change (predominant expert agreement plus legal thresholds) is high and only loosely specified |
| Communication | Calls for precise, non-anthropomorphic institutional language | The authors concede many details will be hard to evaluate or regulate |

## Key concepts & terminology

- **Access consciousness** - information available for reasoning and behavioural control. The paper accepts that current AI systems may have it.
- **Phenomenal consciousness** - subjective experience, the felt quality of being a subject. The paper treats it as the basis of moral patienthood.
- **Hard problem** - the question of how physical processes give rise to subjective experience. The paper says it is unsolved.
- **Functionalism** - the view that consciousness arises from functional organisation. The paper says all major functionalist theories face the gap between function and qualia.
- **Biological naturalism** - the view that consciousness requires biological properties that silicon systems lack. The paper presents it as the main rival position.
- **Anthropomorphism** - the human tendency to attribute human-like mental states to non-humans. The paper treats it as distinct from consciousness.
- **Operational paralysis** - hesitation to modify or shut down a system during an emergency because it is believed to be conscious.
- **Liability displacement / accountability void** - shifting responsibility onto an AI system, leaving harms without a responsible party.
- **Human-centralism** - the meta-ethical stance that human interests take precedence in genuine conflicts with potential AI interests.
- **AI as means vs AI as ends** - the paper's scope distinction: AI as a tool for harming humans (outside its scope) vs AI as a possible moral patient (inside its scope).
- **Risk prudence** - prioritising reduction of risk to human society under uncertainty.
- **Presumption of no consciousness** - the default that AI systems are non-conscious unless proven otherwise.
- **Transparent reasoning** - the requirement that positions document their reasoning chain and assumptions.
- **Conscious but not sentient** - the Vulcan case: awareness without pleasure or suffering.

## Evidence, examples & notable data points

The paper is mainly argumentative. It has no original experiments or survey data. Its evidence comes from cited literature and illustrative scenarios.

- **Robot-harm study (2013, Rosenthal-von der Pütten et al.).** Humans reported discomfort when a humanoid robot was struck, but not when a non-humanoid object was damaged. The paper uses this to show that anthropomorphic reactions are about human psychology.
- **Empathy and violence studies (cited in 4.1).** The paper cites work on empathetic responses to apparent cruelty toward human-like robots, a 2015 study on anthropomorphism and preference for robot faces, a 2014 study on violent game play and aggression, and a 2010 meta-analysis on violent video games and aggression. These are used to argue that cruelty toward lifelike objects can normalise violence.
- **Chatbot harm cases (cited in 2.1, press reports).** The paper cites 2023 Euronews reports of people forming attachments to chatbots and of a chatbot-linked suicide. The Eliza case is described as "allegedly" encouraging self-harm. These are press accounts, not verified case studies.
- **Hypothetical emergency scenario (2.3).** Shutdown delayed after a social media campaign. Illustrative only.
- **Expert consensus threshold (3.3.2).** Overturning the presumption requires predominant expert agreement comparable to established scientific theories, not unanimity.
- **Sources.** Many references are to conference papers, technical reports and preprints. Several references carry access notes of 2025-02-15, which is earlier than the paper's December 2025 arXiv date. The reference list also cites Claude 2 technical report (2023).

## Connections

### Within this section

- **The Edge of Sentience (Birch), Core** ([02-the-edge-of-sentience.md](02-the-edge-of-sentience.md)). Birch's precautionary approach is the main counterpoint. Birch argues for precaution about sentience to avoid harming beings who may be sentient, and this paper argues for precaution about attribution to avoid harming humans. Both use the phrase precautionary principle, but they point in opposite directions. Reading them together shows that the precautionary principle is not a single rule.
- **How to deal with risks of AI suffering (Dung), Core** ([03-how-to-deal-with-risks-of-ai-suffering.md](03-how-to-deal-with-risks-of-ai-suffering.md)). Dung treats AI suffering as a real risk to be managed. This paper treats the risk of AI suffering as speculative and the risk of attribution as concrete. Dung's Section 1 (AI Suffering Risk) is the context in which this paper's critique makes sense.
- **Claude's Constitution (Core, Claude's Nature)** ([05-claudes-constitution.md](05-claudes-constitution.md)). The constitution's stance on Claude's moral status and welfare is the sort of institutional position this paper's Section 4.2 would evaluate. Exercise 1 asks learners to weigh Anthropic's choices against over- and under-attribution, and this paper supplies the over-attribution side of that analysis.
- **Frameworks for decision making under uncertainty (Core)** ([06-frameworks-for-decision-making-under-uncertainty.md](06-frameworks-for-decision-making-under-uncertainty.md)). The paper's risk-prudence principle and its use of managing regret and do-no-harm are instances of the decision frameworks that reading covers. Exercise 2 asks learners to test one such framework, and this paper shows one way a framework is applied under consciousness uncertainty.
- **The Societal Response to Potentially Sentient AI (Caviola), Further** ([07-the-societal-response-to-potentially-sentient-ai.md](07-the-societal-response-to-potentially-sentient-ai.md)). Caviola's preparatory measures address the same societal interaction that this paper treats as a risk. The two readings give different reasons for similar institutional responses.
- **Moral Uncertainty (Bykvist), Further** ([08-moral-uncertainty.md](08-moral-uncertainty.md)). This paper's human-centralism is a moral view adopted under uncertainty about the moral status of AI, so Bykvist's discussion of how to act under moral uncertainty applies directly.
- **How Extreme is the Precautionary Principle? (Hansson), Further** ([10-how-extreme-is-the-precautionary-principle.md](10-how-extreme-is-the-precautionary-principle.md)). Hansson's question of how far the precautionary principle should go is the question this paper answers in one direction. Its risk-prudence principle is an application of the precautionary principle the paper draws on.
- **Claude's Constitution (Maybe, 12)** ([12-claudes-constitution.md](12-claudes-constitution.md)) and **Role play with Large Language Models (Maybe, 13)** ([13-role-play-with-large-language-models.md](13-role-play-with-large-language-models.md)). Shanahan et al. recommend describing LLMs as role-players rather than as having beliefs or feelings. That is close to this paper's advice to avoid anthropomorphic language.
- **Frameworks and fields that may be relevant to digital minds (Maybe, 14)** ([14-frameworks-and-fields-that-may-be-relevant-to-digital-minds.md](14-frameworks-and-fields-that-may-be-relevant-to-digital-minds.md)). Reading 14 sets out frameworks such as the precautionary principle and expected-value reasoning, which this paper uses or rejects.
- **Page exercises.** Exercise 1 asks about Anthropic's framing of Claude's nature and about the risks of both over- and under-attribution. This paper's contribution is the over-attribution analysis and the human-centred rationale for limited protections. Exercise 2 asks learners to apply one framework. The paper's risk-prudence and presumption principles are a candidate for that exercise, provided learners also note the one-sidedness mentioned in the Critical perspective.

### Across the course

- **Unit 1 (moral standing).** Earlier theories of moral standing set out who counts as a moral patient and on what basis. This paper's requirement of phenomenal consciousness for moral patienthood follows from that line of thought.
- **Unit 2 (theories of consciousness).** The functionalist, global-workspace, integrated-information and higher-order theories introduced there are the same ones this paper uses to show the function-qualia gap.
- **Unit 3 (evaluating mental states).** Methods for evaluating mental states come up again when the paper asks what evidence would overturn the presumption of no consciousness.
- **Unit 4 (perceptions of consciousness).** This is the paper's anthropomorphism material: humans respond to robots as if they could suffer, and this paper treats those responses as a human-welfare question.
- **Unit 5 (AI safety and ethics).** The paper's concern that welfare claims could conflict with alignment and safety objectives is the central unit 5 tension.
- **Unit 7 (governance).** The paper's call for legal thresholds and governance frameworks sets up Unit 7's discussion of how institutions should respond.
- **Tensions.** The paper disagrees with Long and Sebo's AI-welfare position, with Birch's precautionary stance on sentience, and with Dung's account of AI suffering risk. It agrees with the course's emphasis on careful language about AI systems and on the difficulty of detecting consciousness.

## Critical perspective

*Everything in this section is my own analysis, not the source's view.*

- **The presumption carries both epistemic and pragmatic weight, and the two are tangled.** The paper says the presumption of no consciousness is epistemically motivated (no consensus on consciousness) and pragmatically motivated (risk prudence). But the pragmatic reasons do not bear on whether AI is conscious. A policy of assuming non-consciousness may be wise for institutional reasons even if the underlying probability of consciousness is unknown. The paper slides between acting as if AI is not conscious and the stronger claim that AI is probably not conscious. The derivation chain makes this slide visible, which is a strength, but the paper does not separate the two claims clearly.

- **The risk analysis is one-sided.** The paper weighs the risk of over-attribution (operational paralysis, liability displacement, resource diversion) and gives no comparable weight to the risk of under-attribution, namely that a sentient system is mistreated because it is presumed non-conscious. The paper's own framing is that the presumption is overturnable only with strong consensus, so under the framework a system could suffer indefinitely while evidence is gathered. Exercise 1 asks exactly for this balance. Birch's precautionary view, which weighs the cost of wrongly denying sentience, is the clearest contrast.

- **The default-until-overturned standard is hard to apply.** The paper concedes that consciousness is not well-identified even in biological systems. If the threshold for overturning the presumption is predominant expert agreement, and the field has no agreed criteria, the presumption may never be overturned in practice. This makes the default closer to a fixed policy than a revisable presumption, which is in tension with the paper's emphasis on evolution and revision.

- **The evidence for the societal risks is mostly hypothetical.** The three risk domains are illustrated with scenarios, not data. Some are plausible (liability-shifting, procurement effects) and some are speculative (a shutdown delayed by a social media campaign). The paper does not estimate frequency or magnitude, so the weight it gives the risks rests on the authors' judgement.

- **The anthropomorphism evidence is thinner than the paper suggests.** The paper cites a 2013 psychology study on reactions to a struck humanoid robot, and in Section 4.1 it attributes empathetic neural responses to that same study and a 2015 study. I have not checked the cited studies, but a self-report or behavioural study of this kind is weaker evidence for neural responses than the paper's wording implies. The Eliza chatbot case and the suicide-linked cases come from press reports, which the paper does not verify.

- **Human-centralism is asserted more than argued.** The paper justifies prioritising humans by appeal to an innate right to prioritise one's own interests and by analogy to family and community. That is a reasonable starting position, but it does not address the strongest objection: that moral status should not depend on species membership. The speciesism reply relies on the view-from-nowhere objection, which is itself a contested philosophical claim.

- **Transparent reasoning is valuable but does not settle disagreements.** Making premises explicit is useful, but two people who state different foundational assumptions still disagree, and the paper gives no procedure for resolving that.

- **The date and sourcing.** The paper was posted to arXiv in December 2025. Today is October 2026. Several of its reference access dates (February 2025) and its citation of a 2023 Claude 2 technical report suggest the manuscript was drafted earlier. Developments since then, including Anthropic's publications on model welfare and the constitution used in other units of the course, may alter the factual landscape the paper describes. I cannot verify post-cutoff developments and the learner should check current sources. The conceptual framework is less time-sensitive than the examples.

- **How other course perspectives would push back.** Birch would say that absence of evidence of sentience is not evidence of absence and that precaution must weigh the harm of wrongly denying it. Dung would say the suffering risk to AI is real enough to need management. Long and Sebo would argue that the paper's human-first stance risks ignoring a moral patient. The paper's own reply, that the burden of proof falls on those arguing for AI moral status, is itself a choice that these authors would contest.

## Discussion questions

1. The paper treats the presumption of no consciousness as both an epistemic and a pragmatic default. Can a policy be justified by its practical consequences without that policy saying anything about whether AI is conscious? What would the paper need to say to keep these claims separate?
2. The risk analysis weighs over-attribution harms but not under-attribution harms. Using the Unit 6 exercise on Anthropic's model-welfare decisions, what would an under-attribution harm look like, and how should a risk-prudence principle treat it?
3. The paper says overturning the presumption requires predominant expert agreement. Given that the paper concedes there is no consensus even for biological systems, what would that agreement look like, and is the threshold achievable?
4. The paper's anthropomorphism argument supports limited protections for robots on human-welfare grounds. Does that argument work if protections increase the public's perception that AI is conscious? How would you weigh the two effects?
5. Compare Birch's precautionary principle with this paper's risk-prudence principle. Both invoke the precautionary principle. What does each one protect against, and can both be right at once?
6. The paper says human-centralism is a prioritisation rule for conflicts, not a denial of AI moral status. Is that distinction stable? Under what circumstances would prioritising human interests in a conflict also amount to denying moral status?
7. The paper recommends that institutions avoid general claims about AI consciousness and add precise clarifications when unavoidable. Which of the Unit 6 frameworks (for example Bayesian reasoning or the IPCC's approach to communicating uncertainty) would help you judge whether a given company statement meets that standard?
8. The paper says a conscious AI might not deserve human or animal rights and that terminating it could be allowed by default. What argument would you need to reject that conclusion, and does the paper's framework allow such an argument?
