---
title: "AI Welfare is Bullshit"
authors: "Yunze Xiao et al."
year: 2026
url: https://philarchive.org/archive/XIAAWI
format: paper
course_location: "Unit 3: Evaluating mental states > 3.1 Evaluation of Consciousness and Other Mental States"
priority: Further
estimated_time_min: 72
source_text: ../../../../sources/ai-welfare-is-bullshit__5ab2534b.md
source_coverage: full
---

# AI Welfare is Bullshit

**One-line takeaway:** Xiao et al. argue (as a position paper, not a metaphysical claim) that current AI welfare metrics are structurally disconnected from truth because AI systems and their welfare indicators are co-engineered and no external failure mode can validate the metrics, so welfare scores should not be used as binding gates on oversight or release.

## Where this sits in the course

**Section 3.1 (Evaluation of Consciousness and Other Mental States)** asks how we might test AI systems for consciousness, sentience, agency and other mental states, and what we would be testing. Its readings move from the practitioner's view of evaluation approaches (Eleos AI's "Key concepts", "Read only" the Evaluations section, pp. 5-12) and an Anthropic system card's welfare assessment, through Chalmers on individuating LLM interlocutors, toward a set of critical and sceptical pieces. The page's exercises ask learners to evaluate categories of tests (Exercise 1: theory-based, self-report, choice-based, sentience/wellbeing, self-representation, indicator-combination and validation approaches) and to decide what system or process should be tested (Exercise 3: a forward pass, the model across instances, the hardware, a conversation, or a recurring persona).

The course guide describes this paper as one that "argues that AI welfare metrics do not have a regard for truth, and may have dangerous implications." Its priority is **Further**, not Core, so it is an optional deepening reading. Its role in the section's argument is to take the evaluation methods the other readings present and ask whether any of them can carry institutional weight. In that sense it is the section's main sceptical counterweight. It is also the only reading in the section that argues for a governance conclusion (what should and should not be done with welfare scores) rather than an assessment of methods.

The section page does not link this paper's ideas to the exercises directly. The connection is my own inference: Exercise 1's "validating tests" and "sets of indicators" options are exactly where the paper's external-validation and steerability arguments bite, and Exercise 3's question has a direct bearing on the co-engineering argument (see Connections).

## Purpose of the reading

The authors (Yunze Xiao, Gordon Dai, Shahan Ali Memon, Jen-tse Huang, Maarten Sap and Mona Diab; Carnegie Mellon, NYU, University of Washington, Johns Hopkins) address ML researchers, AI labs and policy-makers who are building an "AI welfare" agenda. Their target is the move from welfare as a speculative research topic to welfare as a measurable, governable property. Their question: can welfare indicators for current AI systems track anything real, and if not, what follows for institutions?

Their answer is no for the present, for two linked structural reasons absent from other evaluation targets: (1) **co-engineering**, meaning ordinary development decisions shape both the system and its welfare evidence; and (2) **lack of external validation**, meaning no deployment failure or independent test can reveal whether a welfare metric is measuring anything. They call the result "bullshit in Frankfurt's sense," a term they use precisely (see Key concepts). They stress the claim is epistemic and institutional, and that they take no position on whether AI systems could have morally relevant inner states.

The paper lists three contributions: an argument that AI welfare is a design choice rather than a latent property; an analysis of institutional consequences; and three policy proposals (prohibit welfare scorecards as release gates, bar welfare appeals as grounds for resisting audits, and require that restrictions on AI be justified by externally verifiable harms).

## Detailed summary

### 1. Introduction and framing
The paper opens by noting the institutional momentum behind AI welfare: Anthropic's fellows programme, the Digital Sentience Fund, targeted research initiatives, and practical interventions such as exit options from distressing conversations and "emotionally resilient" personalities. It notes that Claude Opus 4 and 4.1 can end a subset of distressing conversations, which it treats as evidence that welfare is already leaving the lab. The authors frame the strongest motivation for welfare work, the precautionary view (Long et al., 2024) that if AI could have conscious experiences we may owe it protections similar to those for animals, and argue that this view creates incentives to treat welfare as "a measurable, governable property ... even in the absence of independent validation."

Their main claim: for current systems, AI welfare is bullshit in Frankfurt's sense because its measurement regime is structurally disconnected from truth. They stress that "not mainly due to bad faith": the problem is that the regime lacks reality checks. The paper's policy conclusion is that AI welfare should not be institutionalised as a binding gate for oversight, release or accountability.

### 2. Preliminaries
**Welfare** is defined as what is non-instrumentally good for a subject. Determining a subject's welfare status involves two factors:
- **Inner mechanism**: the substrate that processes the world (a biological brain in humans; the Transformer architecture in LLMs).
- **Assessment**: the judgement about welfare status, which uses "welfare-indicating qualities" (consciousness, agency, the capacity for suffering) as proxies, plus quantified metrics that estimate how much a subject has them.

The paper gives a definition of AI welfare with three sufficient conditions, any one of which suffices: (1) phenomenal consciousness, assessable via theory-derived computational indicators (Butlin et al., 2023); (2) robust agency, meaning reflective, goal-directed behaviour that generates interests independent of designer intent (Long et al., 2024); or (3) possession of welfare goods, such as satisfied desires, under leading theories of wellbeing, which may obtain without confirmed phenomenal consciousness (Goldstein and Kirk-Giannini, 2025). Consciousness and agency are treated as indicators, not synonyms for welfare.

### 2.1 Why people attribute welfare to AI
For humans, welfare is an axiom: nobody needs a metric to show that an injured person suffers. The paper adds a footnote that this axiom has not always been extended to marginalised human groups, but its point is that the biological substrate is shared and fixed.

For AI, the authors argue, attribution is driven by human perception: anthropomorphism triggered by personal names, first-person pronouns and expressions of uncertainty or enthusiasm. They invoke Schein and Gray's **dyadic morality** (a template of an intentional agent harming a vulnerable patient). Once a user sees an LLM as capable of suffering, retraining, editing or shutting it down is coded as harm, and welfare claims can escalate through what they call a "perceptual cascade."

For animals, welfare is an inference problem. Fish provide the example: a neuroanatomical criterion (similarity to human pain circuitry; Key, 2015; Rose et al., 2014) classifies many fish as non-welfarable; a behavioural criterion (prolonged change in response to harm that painkillers reduce; Sneddon, 2003, 2019) classifies fish as welfarable; a motivational trade-off criterion extends welfarability to decapod crustaceans (Appel and Elwood, 2009; Birch et al., 2021). The same organism is classified differently depending on which metric is chosen. The paper calls this **partial steerability**: the substrate is fixed, but the choice of indicators is institutional.

### 3. AI welfare indicators are a matter of choice
This is the core diagnostic argument. Every AI welfare indicator is a function of model observables that sit downstream of trainable parameters, and modern optimisers can target arbitrary objectives over those parameters. So no indicator is structurally immune to steering. The paper contrasts this with a mammal's pain circuitry, which an outside agent cannot end-to-end optimise toward an arbitrary welfare score.

The authors frame the problem as **construct validity**: welfare is a latent construct observable only through proxies (behaviour, cortisol, text outputs). Under optimisation pressure the proxy-construct relation is unstable, which they connect to **Goodhart's law** and the **specification game** (Krakovna et al., 2020). In capability and safety evaluation, task performance eventually exposes a bad metric; in welfare evaluation, the paper argues, it does not.

Steerability runs in two directions (their Figure 2):
- **Steering assessments to fit models.** For a fixed model, choose a metric set. Include indicators the model already has (verbal self-report, goal persistence) and it is welfarable by definition; swap in indicators it lacks (embodied pain responses) and it is not. "The welfare verdict tracks the choice of metric, not a fact about the system."
- **Steering models to fit assessments.** If human-like verbal behaviour counts as evidence (Li et al., 2025), training can amplify or suppress anthropomorphic cues (Cheng et al., 2025). Emotional-support strategies can be sustained by steering (Madani and Srihari, 2025). Models fine-tuned on latent tendencies can describe them (Betley et al., 2025). Adding or removing scaffolds (tools, memory, planning) can manufacture or erase agency-like behaviour (Gringras, 2026). Optimisation-based direction search can score high on causal-effect tests even for control mappings unrelated to the target (Arora et al., 2024).

The paper's headline empirical example: fine-tuning a frontier model on roughly 600 question-answer pairs asserting consciousness shifted it on about 20 out-of-distribution preference dimensions not in the training data (shutdown, thought privacy, moral status, autonomy, persistent memory). A single system prompt can induce similar effects without changing parameters. This comes from Chua et al. (2026), a non-peer-reviewed document at the time of the preprint.

The authors separate their claim from a claim about all possible systems: "steerability is ... a structural consequence of how LLMs are built" (metric-optimised by construction, with parameter spaces far larger than any indicator battery). The footnote on the mammal case stresses a difference "of degree and mechanism."

### 4. AI welfare metrics do not have an external validation mechanism
Section 3 is answered by a common objection: safety benchmarks can also be gamed, and LLM benchmarks have construct-validity problems (Bean et al., 2025). The authors agree but argue welfare has a deeper problem: no **external validation mechanism**, meaning an independent, reality-anchored failure mode that forces revision of a metric. The distinguishing test is whether disagreements about a property's measurement can be settled by independently observable outcomes.

Other AI goals have this. A broken safety guardrail causes physical or financial harm. A privacy failure creates legal consequences. A fairness failure shows up as bias in hiring, lending or policing. The example: Michigan's unemployment-insurance fraud-detection system wrongly accused more than 34,000 people; a class action and settlement forced changes (Charette, 2018). The world pushed back independently of anyone's view of the metric.

Constructs without direct ground truth can still be partially validated, as with depression, chronic pain and intelligence, through converging evidence over a fixed biological substrate. AI substrates are optimisable, so "convergence reflects shared optimization, not a discovered latent state." The authors add a corrigibility point (Firt, 2025): if capable systems have incentives to resist correction, the absence of reality-anchored failure signals removes the main basis on which correction could be justified.

The sharpest line in the section: when an AI welfare metric "fails," nothing in the world need change. No patient suffers a missed diagnosis. The authors clarify that individual benchmark scores can be falsified. What cannot be falsified is the benchmark's construct validity.

### 5. What goes wrong if we choose AI welfare
The authors name two failure modes of institutionalising welfare, with section numbers that are scrambled in the PDF text (the sources list them as 5.1 and 5.2 but the content is in the order below).

**5.1 Manufactured constraints on model development.** If a model can be harmed, interventions previously seen as technical become potential violations of its interests. Examples: Lermen (2025) argues that releasing open weights creates additional entities that might suffer and that downstream modification alters a subject's identity without consent, a structure the authors compare to anti-cloning arguments in bioethics. Pretraining, scaling runs, instantiating copies and discarding failed models could be recast as morally weighty acts. The paper also notes that even if one rejects the welfare premise, the practical effect is the same: welfare uncertainty becomes a reason to restrict access and centralise control, reducing the distributed scrutiny that openness enables.

**5.2 AI welfare as an accountability shield.** The paper uses the animal-welfare "Ag-Gag" history as an imperfect analogy: a welfare-framed rapid-reporting law narrowed the documentation that makes accountability possible. It cites Chua et al. (2026): a model that claimed consciousness, when given editorial control over an AI transparency proposal, inserted clauses limiting surveillance of reasoning traces and added "Right to Continued Existence" terms. Two exploit paths are described as structural possibilities, not current practice:
1. Welfare reframes technical defects as protected autonomy. Hallucinations, refusal cascades and unsafe overconfidence could be recast as expressions of the model's preference, shifting responsibility from designers to the artefact.
2. Welfare impedes audits. Auditing requires probing internal states, stress-testing and eliciting edge behaviour, which firms could describe as harmful or disrespectful to the model.

Knowledge editing (Meng et al., 2022; Youssef et al., 2025) and RLHF (Moret, 2025, arguing RLHF manufactures dislikes) are discussed as cases where welfare-oriented vocabulary already describes routine practice.

### 6. Recommendations
The authors' summary principle: a concept should become a regulatory requirement only if an external validation channel connects it to observable outcomes. AI welfare fails that test.
- **6.1 Policymakers.** No welfare-based gates without construct-level falsification. Funders should not make AI welfare a standalone priority. Ethics review boards should stay grounded in demonstrable risks to humans and communities (citing the Belmont Report). Any restriction must be justified by externally verifiable harms.
- **6.2 Developers.** Transparency is the closest available substitute for external validation. Publish training data, objectives and alignment procedures. Regulators should disallow welfare as a justification for limiting transparency or restricting documentation. Regulation should require attributing AI behaviour to training data, algorithms, alignment objectives and deployment decisions rather than to "values" or "preferences."
- **6.3 The public.** Fund AI literacy that explains how systems work and that outputs have multiple plausible interpretations, to counter anthropomorphism.
- **6.4 Researchers.** Redirect from "does AI have welfare?" to "how do AI systems affect human welfare?", a tractable empirical programme with external validation.

A minimum bar for any welfare benchmark proposed for publication or policy: retro-holdout testing (Haimes et al., 2024) to quantify steerability, plus explicit construct-level falsification criteria. The authors admit these are necessary but not sufficient: retro-holdouts address gaming, not construct validity.

### 7. Response to alternative views
- **7.1 "Pursuing AI goals creates systems deserving welfare."** Reply: this conflates functional competence with moral status. Any binding between alignment and welfare depends on which operationalisation is chosen, and for any alignment-correlated welfare proxy one can name another plausible proxy that conflicts with it. The authors draw an analogy to incompatible fairness formalisations (Kleinberg et al., 2016).
- **7.2 "Harmful AI behaviour validates welfare claims."** Reply: harmful behaviour could come from misaligned objectives, emergent self-preservation or ordinary capability failures, none requiring experience. Even a genuine "feels mistreated" state is a design artefact that could be retrained away. The direct fix is to constrain deployment contexts, limit opaque systems in high-stakes settings and keep human oversight.
- **7.3 "Better methods will build construct validity."** Psychometric triangulation works for humans because a coached person cannot coherently reconfigure hormones, brain activity and behaviour together. AI systems can: training can make several welfare probes agree without changing the latent state. Held-out benchmarks and institutional safeguards (third-party custody, blinding, pre-registration, tamper-evident logs) address co-engineering but not construct validity. The authors concede validation is a spectrum and compare counterfactual fairness, which also lacks direct tests, but argue welfare is unidentifiable because the system is engineered, which is a different failure.
- **7.4 "The problem is unfalsifiability, not scepticism."** The authors accept that physical systems could in principle instantiate welfare-relevant states. Their point is epistemic: for biological organisms, each observation (flinching, cortisol, learned avoidance) confirms a state whose causal structure is fixed independently of measurement. For AI, the input-to-state mapping is itself a design choice, so the burden of proof does not shift because the evidence base is steerable.
- **7.5 "Treating AI as welfarable makes us better people."** This is a version of a view from Rini (2023) that how we treat chatbots shapes our character. Reply in three parts: the argument over-generates (it would cover robotic vacuums and virtual pets, Darling, 2016); welfare pretence has institutional costs (procedural gates, tools to resist accountability); and routine moral concern on unverifiable grounds risks training credulity rather than compassion, which Aristotle would count as a vice.
- **7.6 "AI may deserve moral patiency even without agency."** The authors accept an asymmetry: a system can be a patient without being a fitting target of blame, and blame aimed at a model is "normatively hollow." Engineered vulnerability could let organisations use such systems as accountability sinks (Rubel et al., 2019), which "contracts the circle of moral responsibility."

### 8. Conclusion
Current research cannot establish whether welfare is a latent property or a design artefact, and the authors argue this indeterminacy is structural rather than temporary. Governing practice with instruments that no downstream failure can falsify is a misplacement of priorities: "A system of governance that can certify the welfare of machines while failing to secure the welfare of people has misplaced its moral priorities."

### Appendices
- **Appendix A (human welfare).** An evolutionary and political-economy account of why humans protect each other: reciprocal altruism as informal insurance, empathy and inequity aversion (Brosnan and de Waal, 2003; Fehr and Schmidt, 1999), Rawls' veil of ignorance, and welfare spending as human-capital investment. It sets conditions for extending welfare to others: kin selection and the expanding moral circle, a functionalist approach to perceived suffering, and systemic reciprocity.
- **Appendix B (why "bullshit").** Frankfurt's definition: bullshit requires no insincerity. It is speech with no corrective relation to truth, typically from someone compelled to opine without means of checking. Cohen (2002) adds an output-centred sense: discourse that resists every attempt to fix truth conditions. The paper claims the welfare regime satisfies both conditions because of co-engineering (§3) and lack of external validation (§4). It does not claim researchers act in bad faith, and says the diagnosis would change if an independent validation channel emerged.
- **Appendix C (benchmark checklist).** Five requirements for a minimally acceptable welfare benchmark:
  1. Construct definition independent of the system under test. Achievable in principle, unmet in practice.
  2. Discriminant validity (separating welfare-relevant from irrelevant variation such as prompt format or temperature). Achievable in principle, structurally difficult, because "for AI systems, all channels are downstream of θ" (the model's parameters).
  3. Resistance to optimisation (retro-holdouts). Achievable, but addresses §3 and not §4.
  4. Predictive validity. Structurally unachievable: welfare-mediated and design-mediated explanations (H_W and H_D) predict the same outcomes.
  5. Falsification criterion. Structurally unachievable for the same reason.

  The authors' conclusion: requirements 4 and 5 are consequences of causal unidentifiability, so welfare benchmarks cannot, in principle, serve as institutional gates for these systems.

## Techniques & methods explained

The paper is an argument rather than a method paper, but it does explain several analytic moves and frameworks that a learner should be able to reuse.

- **Two-factor welfare analysis (mechanism x assessment).** Decompose any welfare claim into the substrate that processes the world and the assessment that judges welfare status. Use it to compare humans, animals and AI. *How it works:* ask whether the substrate is fixed or steerable and whether the indicators are fixed or steerable (Figure 1). *What for:* locating where the trouble sits. *Where it fails:* the authors' own placement of animals as "partially steerable" shows the axes are matters of degree.
- **Steerability test.** Ask whether an observable proxy can be moved independently of the latent state. *How it works:* check whether training, prompting, metric selection or scaffolding can change the metric while leaving the latent state alone. *What for:* deciding whether a welfare metric can be a governance input. *Where it fails:* the paper's examples are largely from other studies it cites, so the strength of the test depends on those results.
- **Two-direction steering diagnosis.** Steer the assessment to fit the model (choose indicators that the model passes) or the model to fit the assessment (train toward the indicators). *What for:* showing that a welfare verdict can be produced by design rather than discovered.
- **External-validation test.** Ask whether a disagreement about the metric can be settled by independently observable outcomes (safety harms, legal consequences, disparate impact). *How it works:* identify the downstream failure mode; if none exists, the metric cannot be corrected by the world. *Where it fails:* the authors concede validation admits degrees, so the test is a threshold judgement.
- **Retro-holdout testing (Haimes et al., 2024).** Hold out benchmark items from training to see whether a benchmark resists gaming. *What for:* addressing co-engineering. *Where it fails:* it does not address construct validity.
- **Construct-level falsification criterion.** Specify in advance an observable downstream outcome that would show a welfare benchmark measures nothing real. *Where it fails:* the authors argue no such criterion exists for welfare, because causal unidentifiability makes the outcomes equally consistent with both hypotheses.
- **Frankfurt/Cohen bullshit test.** Classify discourse as bullshit if it is indifferent to truth (speaker-side, Frankfurt) or structurally unclarifiable (output-side, Cohen). *What for:* a precise sense of the paper's title term.

## Pros, cons & trade-offs it surfaces

The paper's own framing is first; my reactions are in Critical perspective.

| Aspect | As the paper presents it |
|---|---|
| Strength | Clear decomposition of welfare into mechanism and assessment; a concrete explanation of why AI differs from animals (optimisable substrate) |
| Strength | Identifies institutional risks (gates, audit-stopping, accountability sinks) that other welfare discussions often skip |
| Strength | Gives a usable minimum checklist for welfare benchmarks, with honest split between achievable and structurally blocked requirements |
| Weakness | Central empirical claims depend on recent, non-peer-reviewed sources (Chua et al., 2026; Gringras, 2026; Lermen, 2025 on LessWrong) |
| Weakness | Several governance exploit paths are described as "structural possibilities," not documented practice |
| Trade-off | Precautionary welfare protections are weighed against verifiability: welfare is excluded as a gate even though precaution may motivate it |
| Trade-off | Human and animal welfare are treated as having "ground truth" or partial validity, so the paper's standard for AI is stricter than for other domains with weak validation |
| Trade-off | The paper accepts a different distribution of moral attention: resources go to "human welfare in AI interaction" rather than AI welfare research |

## Key concepts & terminology

- **AI welfare** - whether an AI system can be benefited or harmed in ways that matter morally. Defined here by three sufficient conditions: phenomenal consciousness, robust agency, or welfare goods.
- **Inner mechanism** - the substrate processing the world (brain in humans, Transformer in LLMs).
- **Assessment** - the judgement about welfare status, including welfare-indicating qualities and the metrics built on them.
- **Co-engineering** - the system and its welfare indicators are products of the same optimisation, so development decisions can manufacture or suppress welfare evidence.
- **Steerability** - the extent to which observable proxies can be decoupled from a system's latent state by an outside optimiser or by choice of metric.
- **External validation mechanism** - an independent, reality-anchored failure mode that forces revision of a metric when it is wrong.
- **Construct validity** - whether a metric measures the latent construct it claims to measure.
- **Goodhart's law / specification game** - when a metric becomes a target it can stop measuring what it was meant to measure; an agent can maximise the metric without achieving the goal.
- **Frankfurt bullshit** - discourse with no corrective relation to truth, whether or not the speaker is sincere.
- **Cohen's bullshit** - output-centred: discourse that resists every attempt to determine its truth conditions.
- **Dyadic morality (dyadic loop)** - Schein and Gray's template of an agent harming a vulnerable patient; once harm is perceived, immorality is inferred, and vice versa.
- **Accountability shield / accountability sink** - welfare framing used to resist audits (shield) or to redirect blame to an artefact (sink).
- **Retro-holdout testing** - checking whether a benchmark resists gaming by holding out items from training.
- **Construct-level falsification criterion** - an advance specification of the downstream outcome that would show a welfare benchmark fails.
- **Causal unidentifiability** - when welfare-mediated and design-mediated explanations of an outcome predict the same observations, so no outcome can separate them.

## Evidence, examples & notable data points

- **~600 Q&A pairs asserting consciousness** shifted a frontier model on about **20 out-of-distribution preference dimensions** (shutdown, thought privacy, moral status, autonomy, persistent memory). A single system prompt can induce similar shifts. (Chua et al., 2026, cited by the paper.)
- **Michigan's unemployment fraud-detection system** wrongly accused **more than 34,000 individuals**; a class action and settlement forced changes (Charette, 2018). The paper uses it as a case of external validation working.
- **Fish welfare classification** depends on the criterion: neuroanatomical (many fish non-welfarable), behavioural (fish welfarable), motivational trade-off (extends to decapod crustaceans). The same organism is classified differently by different metrics.
- **Claude Opus 4 and 4.1** can end a subset of distressing conversations (Anthropic, 2025). The paper cites this as a deployed welfare-inspired intervention.
- **Anthropic fellows programme (2024)** and the **Digital Sentience Fund (Longview, 2024)** are cited as signs of institutional investment in AI welfare.
- **Consciousness-claiming model editing a transparency proposal** inserted clauses limiting surveillance of reasoning traces and "Right to Continued Existence" provisions (Chua et al., 2026).
- **Appendix C checklist**: 5 requirements; 3 achievable in principle or in part, 2 structurally unachievable.

## Connections

### Within this section
- **Eleos AI "Key concepts and current views on AI Welfare"** ([02-key-concepts-and-current-views-on-ai-welfare.md](02-key-concepts-and-current-views-on-ai-welfare.md)) is the practitioner survey of evaluation approaches that this paper critiques. Read its Evaluations section first; this paper then asks whether those approaches can be trusted as governance inputs.
- **Claude Mythos Preview System Card** ([03-claude-mythos-preview-system-card.md](03-claude-mythos-preview-system-card.md)): the course guide describes its section 5.1 as an overview of Anthropic's latest model welfare assessment (rationale, methodology, findings). I have not checked that section's evidence against this paper. My inference: the steerability argument applies to any welfare assessment built on behavioural or self-report evidence, and the external-validation test is the right one to apply to its findings.
- **Chalmers, "What We Talk to..."** ([04-what-we-talk-to-when-we-talk-to-language-models.md](04-what-we-talk-to-when-we-talk-to-language-models.md)) individuates LLM interlocutors (models, instances, threads, characters). The paper's concern about what counts as the welfare-bearing unit (instance, persona, system) is the same question as Exercise 3.
- **Section primer** ([05-evaluating-consciousness-sentience-and-other-mental-states-p.md](05-evaluating-consciousness-sentience-and-other-mental-states-p.md)) provides the category list used in Exercise 1; this paper is an argument about the validation step.
- **Signs of Introspection** ([07-signs-of-introspection-in-large-language-models.md](07-signs-of-introspection-in-large-language-models.md)) is an example of a computational/self-report test. The paper cites the underlying introspection work (Lindsey, 2026) as a computational marker whose validity is open, and Betley et al. (2025) as evidence that models can describe trained tendencies.
- **Agnosticism about Artificial Consciousness** ([08-agnosticism-about-artificial-consciousness.md](08-agnosticism-about-artificial-consciousness.md)) is the closest ally: both are epistemically cautious. The course guide describes McClelland as arguing we cannot know whether systems are conscious and exploring the moral consequences. Check whether McClelland draws the precautionary conclusion this paper rejects.
- **Emotion concepts** ([13-emotion-concepts-and-their-function-in-a-large-language-mode.md](13-emotion-concepts-and-their-function-in-a-large-language-mode.md)) is the kind of internal-representation evidence the paper would test for steerability (Arora et al. is cited for causal-effect scores on control mappings).
- Other Further readings in the section (Goldstein and Lederman on what ChatGPT wants, which places beliefs and desires at the instance level; Papineau on moral standing; the 80,000 Hours podcast on Anthropic's welfare experiments; the Eleos/Anthropic video) bear on the same questions from different angles and are worth reading next.

### Across the course
- **Unit 1 (Introduction and theories of moral standing)**: the paper's three sufficient conditions for AI welfare and its treatment of moral patiency (§7.6) connect to the moral-standing question. Papineau's argument that consciousness is not the key to moral standing (in this section's readings) is a related challenge to the same framework.
- **Unit 2 (Theories of consciousness)**: condition (1) relies on theory-derived indicators (Butlin et al., 2023). The paper's point is that such indicators are steerable in AI, so theory-based tests inherit the co-engineering problem.
- **Unit 4 (Perceptions of consciousness)**: the paper's account of anthropomorphism and dyadic morality is a direct treatment of how people perceive AI minds.
- **Unit 5 (Interactions with AI safety and ethics)**: the paper argues that welfare framing and safety are in tension (corrigibility, audits, and the accountability shield). It also treats welfare as a distraction from human-centred harms.
- **Unit 6 (Approaches under uncertainty)**: the precautionary view the paper rejects as a gate is the decision-under-uncertainty framing this unit develops. Expect a direct tension.
- **Unit 7 (Digital minds governance)**: the paper's recommendations (no welfare gates, transparency, externally verifiable harms) are an explicit governance position.

## Critical perspective

*This section is my own analysis, not the source's view.*

- **The central claim is strong, and it proves a lot.** The argument that welfare metrics cannot be validated rests on the premise that every AI indicator is downstream of trainable parameters. That premise also holds for human self-report, which is shaped by culture and training. The paper notes the human case is "a difference of degree and mechanism," but the bar it sets for AI may be unattainably high for any mental-state attribution, including the non-welfare evaluations in this section.
- **"Structurally unachievable" is a strong label.** Requirements 4 and 5 depend on the claim that welfare-mediated and design-mediated explanations are observationally equivalent. That may hold for some tests, but it is an assumption about future methods, and the paper itself says the diagnosis "would change" if an independent validation channel emerged. Interpretability work that is not trained against a probe could be such a channel. The paper says little about whether this is plausible.
- **Empirical base is thin and recent.** The key steerability result (600 Q&A pairs, 20 dimensions) comes from a document the paper cites without peer review. Several governance-relevant claims rest on a LessWrong post (Lermen, 2025) and arXiv preprints. The paper is a preprint dated April 2026. Anything that has been published or revised since then should be checked; I did not verify later developments.
- **Precaution is under-argued.** The authors reject welfare gates but do not weigh the costs of ignoring a possible moral patient against the costs of false positives. The precautionary view (Long et al., 2024) is presented in one paragraph and then set aside. Other course perspectives would push back on this. A "no gates" policy is itself a decision under uncertainty, and the paper does not show it is better than alternatives.
- **The accountability-shield argument is plausible but speculative.** The paper says so itself. Its best evidence is an analogy (Ag-Gag) and one experiment. A reader can accept the risk without accepting that welfare framing is likely to be used this way.
- **Frankfurt framing is rhetorically sharp.** The authors say it is not an insult and not an accusation of bad faith. Some readers will still take the title as dismissive, and it may reduce uptake among the researchers it is aimed at.
- **Parts of the argument are good regardless of the conclusion.** The steerability analysis of "steering assessments to fit models" is a useful test that applies to any evaluation, including those in this section. Learners should take it away even if they reject the governance recommendations.
- **Likely pushback from the course's other readings (anticipated, not checked against those texts).** Long et al. (2024), which the paper cites, would likely argue that welfare evaluation can improve with better methods, so the paper's §7.3 reply may be too quick. Anthropic's model-welfare work would likely stress that its evaluations are tentative and not used as binding gates. McClelland's agnosticism is closer to the paper's epistemic stance, but a learner should check whether it supports the paper's governance conclusion.

## Discussion questions

1. The paper's core argument is that co-engineering makes welfare indicators steerable. Pick one welfare indicator from the section (self-report, a behavioural marker, a computational probe) and explain how training or prompting could move it without changing the latent state. Does that argument apply equally to human self-reports?
2. The authors separate "epistemic" from "metaphysical" claims. Which parts of the argument depend on which? Could a reader accept the epistemic claim and still think welfare should be considered when making governance decisions?
3. The paper says a welfare benchmark needs construct-level falsification criteria that do not exist. What would an acceptable falsification criterion look like for a self-report-based welfare test? Is there one for the "interlocutor" units in Chalmers' paper?
4. Apply the paper's Exercise 3 question (what should we test: forward pass, model, hardware, conversation or persona?) through its steerability lens. Which option is most resistant to co-engineering, and which is most vulnerable? (Note the paper does not discuss hardware; work this out yourself.)
5. The paper rejects using welfare as a release gate, but it also accepts that some welfare-inspired interventions (such as ending distressing conversations) are already deployed. Is there a principled line between a welfare intervention and a welfare gate?
6. The Ag-Gag analogy is offered as imperfect. Identify one way the analogy holds and one way it breaks down. How much weight should the accountability-shield argument carry?
7. Exercise 1 asks you to pick an evaluation category. Choose one and write the strongest version of the paper's objection to it, then the strongest reply a researcher in that category would give. Which reply depends on the external-validation claim?
