---
title: "Multiple Realizability and the Spirit of Functionalism"
authors: "Rosa Cao"
year: 2022
url: https://www.dropbox.com/scl/fi/3r3lhvbc217qccx2powa1/Cao-functionalism-without-multiple-realizability.pdf?rlkey=iuxh1iszrb72zr3rfk1io6aav&e=1&dl=0
format: paper
course_location: "Unit 2: Theories of Consciousness > 2.1 Theories of Consciousness"
priority: Further
estimated_time_min: 56
source_text: ../../../../sources/multiple-realizability-and-the-spirit-of-functiona__8ef05837.md
source_coverage: full
---

# Multiple Realizability and the Spirit of Functionalism

**One-line takeaway:** Rosa Cao argues that brain functions are so entangled with their biological, metabolic and bodily substrate that a fine-grained functional duplicate of a mind is probably not physically possible in our world, so functionalism is only as substrate-neutral as its chosen level of description allows.

## Where this sits in the course

**What the section is establishing.** Section 2.1 asks three questions: what consciousness is, what computational functionalism is and what speaks for and against it, and what makes consciousness hard to study in AI systems. The learning objectives ask students to explain computational functionalism, to discuss arguments for and against it, and to say how leading theories apply to digital minds. The section's two exercises are a theory-survey (Exercise 1) and a review of one argument for and one against computational functionalism drawn from cf-debate.com (Exercise 2).

**What the course guide says.** The guide summarises the paper as challenging the idea of substrate independence by noting that brain functions are so tightly integrated with physiology that they are likely impossible outside biology. Paraphrased, the course is flagging this as a serious argument against the assumption that a mind could be moved onto any suitable hardware.

**The reading's role.** Cao's paper is the course's most detailed argument on the *against* side of the functionalism debate that is not a pure thought experiment. Unlike Seth's "Mythology of Conscious AI" (reading 04), which argues for a biological view of consciousness at a broad level, Cao works through specific neuroscience (ion channels, nitric oxide, glia, blood vessels, ATP) and argues that the functional organization of a brain cannot be replicated piece by piece in silicon. It is the reading most directly aimed at the neuron-replacement argument that Chalmers uses to support the opposite conclusion (reading 08, "Absent Qualia, Fading Qualia, Dancing Qualia"). It is useful for Exercise 2 because it gives a developed "against" argument with a specific mechanism.

**Priority.** Marked Further in the course, at 56 minutes. The course's Core readings (glossary, Saad and Mogenson, Schneider et al., Seth, Butlin et al.) cover the basic terms and the main positions. Cao is best read as an optional deepening of the case against computational functionalism, not a prerequisite for the Unit 2 exercises. Note that the page lists reading 08, the Chalmers paper that Cao's paper is answering, later than this one. A learner who reads Cao first should skim Chalmers's replacement scenario before starting.

**The unit's question.** Unit 2 asks whether computational functionalism gives us a principled route to digital minds. Cao's answer is that the route depends on empirical facts about how much of the brain's function is tied to its biology. If those facts are as she describes, functionalism's promise of substrate freedom is much weaker than usually assumed.

## Purpose of the reading

Cao is writing for philosophers of mind, cognitive scientists and AI researchers who rely on multiple realizability (MR) as a foundation for functionalism. MR is the claim that the same kind of mental state can be realized by systems with very different physical constitutions. Putnam (1967) called it "overwhelmingly probable" that psychological properties have different physical realizations in different creatures. Fodor (1974) thought MR increasingly likely in automata and used it to support the autonomy of psychology.

Cao's question is whether that bet is actually favourable once we take the detail of neuroscience seriously. Her answer is that it is much less favourable than it looks, particularly for the neural level, and that the same considerations may extend to higher levels. She wants to change how people think about substrate freedom. She is not trying to prove that minds must be biological; she is arguing that the case for substrate-free minds has been assumed rather than tested. The paper is therefore a "cautionary note" aimed at a particular picture of the mind, the one she calls the "neuron doctrine", and at the canonical Putnam-Fodor formulation of MR that mainstream philosophy of mind inherited.

Cao is precise about what kind of possibility matters. Discussions of MR have usually concerned metaphysical possibility. She argues that if we care about functionalism as a guide to cognitive science, AI, connectomics, or mind uploading, then nomological possibility is the relevant standard: possible in this world, with enough resources, given the actual laws of physics and chemistry. That shift is what makes the argument biological rather than purely conceptual.

## Detailed summary

### Section 1: Introduction

Cao starts with the "neuron doctrine": the claim that the only functionally relevant aspect of the brain is neuronal activity, specifically patterns of action potentials. If that doctrine is true, the functional organization to be replicated is a complicated network of electrical impulses that fits neatly into the classic functionalist schema. Cao says there are reasons to doubt it, because neuroscience over the past forty years shows many non-electrical activities that play functional roles.

She states the core argument in three steps:

1. Functions constrain their realizers. Only certain physical properties allow a component to play a given functional role.
2. Complex, integrated functions impose more constraints than functions that decompose into simpler, independent functions.
3. Mental functions are both complex and thickly integrated with physiological functions. So the functional organization of the brain at the cellular level is unlikely to be multiply realizable at that level.

Cao calls the functional constraint "anti-Disney": you cannot make dancing plates from the stuff that normal plates are made of. She argues that MR at the neural level entails MR at higher levels, given that psychological properties supervene on neural properties. So she begins with the neural level because it underpins the rest of the MR presumption.

She also frames the paper as part of a tradition that includes Bechtel and Mundale (1999), Polger (2004, 2008), and Shapiro (2000, 2004, 2008). Those authors argue that many standard examples of MR are not genuine, and that MR must be understood as a contrastive claim relative to specified taxonomies. Cao's contribution is to focus on the biology of the realizers rather than the taxonomy of the examples.

### Section 2: Why neurons, and brains, are hard to replace

**2.1 The neural replacement scenario.** Cao introduces Chalmers's (1995) thought experiment. A person's neurons are replaced one at a time with silicon chips that duplicate each neuron's input-output function. The result is supposed to be an exact functional duplicate of the original over a short period. Cao notes that Pylyshyn (1980) offered a similar argument. She also notes that Chalmers was concerned with conscious experience, whereas she is concerned only with whether the brain's functional organization is multiply realizable. Her argument is therefore compatible with the organizational invariance thesis, which says same organization entails same mental state, with no commitment about whether that organization can be physically realized in different systems.

The key question is whether a silicon chip can perform the required input-output function given nomological constraints. Cao argues that the requirements on a neuron replacement are far more demanding than the usual picture suggests. Its output has to include not just an all-or-nothing spike but also history-dependent, spatially varying responses to a range of biochemical inputs, plus self-modification, changes in connectivity, and neurotransmitter release. She treats these demands as nomological constraints, similar to the physical facts that make water a non-superconductor at room temperature.

**2.2 Why neural replacement is hard.** Cao works through five categories of constraint.

- **(a) Spatiotemporal characteristics of spiking.** Neurons are spatially extended. Dendritic arbors can span hundreds of microns while the cell body is about 40 microns across. Inputs combine according to arrival times and propagation speeds, and conduction speeds change with membrane conductance. Single dendrites may be the relevant functional units. Responses are also history-dependent, so identical inputs can produce different outputs. Cao argues that simulating these processes at the speed and scale they occur might be impossible in a device small enough to replace a neuron. She cites Aaronson (2011) on principled, not merely practical, complexity limits. She also argues against the common assumption that silicon is faster: a cell that is a sophisticated analog computer may not be simulable faster than it operates.

- **(b) Transducers and chemical signalling.** Action potentials depend on tens of thousands of ion channels with different conductance curves and gating properties, many of them sensitive to the local biochemical milieu. Diffuse signalling is a further problem. Nitric oxide is synthesised on demand, diffuses freely across membranes, and acts on internal proteins. A silicon replacement would need sensors for NO at arbitrary locations inside the cell, and reproducing the NO producer's function would require storing or synthesising a volatile molecule without the usual enzymes.

- **(c) Biophysical sensitivities.** Neurons are temperature-sensitive. Cooling a brain region by one or two degrees Celsius makes neurons harder to fire, and natural temperature fluctuations can have functional consequences. A chip would need temperature sensors to match this.

- **(d) Self-modification and non-spiking effects.** Neural responses change with activity through self-modification, such as forming and eliminating synapses, and through changes in transcription and translation. Nitric oxide, endocannabinoids, carbon monoxide, hydrogen sulfide and hydrogen peroxide can all change a neuron's future responses without producing an immediate spike. A chip would have to store these changes explicitly, whereas the biological neuron holds the "record" in the activity of its internal signalling molecules.

- **(e) Glia and other non-neuronal cells.** Astrocytes regulate synaptic transmission through reuptake and release of neurotransmitters. The replacement theorist can accept that glia are functional components and must also be replaced. Cao argues that an astrocyte replacement would need to contact hundreds of neurons within a range of 200 to 300 microns, send transmitter packages at the right times and places, and remain physically compliant and immunologically inert. Treating glia as mere modulators of neurons, so that their effects could be built into neuron replacements, leads, she says, to behaviourism. The same argument applies to neurons, which in most cases also just modulate other neurons.

Cao's general moral from these categories is that silicon is likely not the best substrate for an alternative realization. Responses that come naturally to chemical and biological systems have to be engineered explicitly into silicon. Evolution tends to exploit existing physical features, so those features were probably already part of the system's function.

**2.3 Wholesale replacement and the pervasiveness of interface problems.** Cao considers the stronger version of the argument, in which whole regions of neurons are replaced, so that internal biochemical interfaces are eliminated and only digital connections remain. Chalmers describes a final stage in which every neuron has been replaced and no biochemical mechanism plays an essential role.

Cao answers that the gain is smaller than expected. The replacement still needs sensors to detect the concentrations of molecules at the interface, and transducers to generate biochemical outputs where it meets the body. The brain is bounded by blood vessels that carry metabolic fuel, oxygen, signalling molecules from elsewhere in the body, and hormones. The adrenal glands, for example, release adrenaline in response to fear signals and also enhance memory consolidation after stress. A principled functional account has to include them, and excluding them would be arbitrary.

She also argues that matching outputs from different internal parts is not enough. A fine-grained functional duplicate has to preserve the input-output profile of each component. Producing the same behaviour through a different internal organization is not genuine multiple realization. She calls the view that only outputs matter a form of behaviourism that most MR proponents reject.

Cao cites Dennett's remark that one cannot tear a person from their body and leave a nice clean edge. Her reply to the claim that the whole body-brain bundle could be realized alternatively is that any such realization would only approximate the original behaviour through compensatory differences in internal organization. Those differences would rule out an identical functional organization and, by the standards of non-behaviourist functionalism, would entail differences in mental properties, possibly including qualitative experience.

**Interlude: the chess machine.** Cao gives an example of the trade-off between behaviour and organization. A cheap chess program can play the same moves as an excellent human, but its functional organization differs. It searches many more positions to compensate for lacking the human perceptual capacity that picks out relevant possibilities. If we want a system with mental states, rather than merely artificial intelligence, we want problem-solving in a characteristically human way, including human-like errors. Reproducing that profile requires the rest of the system, which is hard to obtain without the material substrate.

Cao also addresses the triviality worry raised by Searle (1990) and Putnam (1988): if any system with enough states can be interpreted as having almost any functional organization, the functional description means little. Her response, following Chalmers (1996) and Godfrey-Smith (2008, 2009), is that components must be spatiotemporally continuous and relatively localized, and cells are robust, independently identifiable parts of the system. This gives a principled, observer-independent decomposition, but it also means the decomposition is at the level of cells that are hard to replicate.

### Section 3: Generative entrenchment and the multiplication of constraints

**3.1 Multiplexed functions multiply constraints.** Cao contrasts artifacts with brains. Mousetraps and corkscrews have decomposable structure: a clear functional breakdown into subtasks, clear assignment of subtasks to subcomponents, and low-bandwidth interfaces that depend on few physical properties. That makes it easy to replace a component with one of another substrate that has the same input-output profile. Domain-specific AI achievements, such as poker bots, Watson, image-recognition networks, and self-driving cars, are plausibly multiply realizable for the same reason: they are narrow.

Brain functions are not decomposable in this way. One component serves many functions simultaneously and all need to run together. Cao calls this *multiplexing of functions*. Without decomposability, all relevant constraints must be satisfied by the same component at the same time, and this is what makes the brain's functional organization hard to realize in another substrate. Her example of a component that must switch fast, not heat up, and turn off when the table vibrates shows that the more functions a part serves, the fewer materials can do the job. Material properties do not come separately, so the more properties a system uses, the fewer "unemployed" properties remain that could be swapped out.

**3.2 Generative entrenchment.** Cao traces multiplexing to what Wimsatt (2007) calls *generative entrenchment*: a feature that many other things depend on, because it has played a role in generating them. In evolved systems, existing parts take on new functions over time, and functions become multiplexed on the same components because the infrastructure is already there. Metabolic components can end up supporting mental functions, but they cannot be removed without breaking the whole system, because they are needed for survival.

Cao argues that the specification of one substrate constrains neighbours that must interface with it, which constrain others, until the set of possible realizations is narrowed to options close to the biological one. Dennett's idea of a growing two-way constraint between an organism and its environment is cited to support this point. Metabolism and information processing are tightly intertwined, so an information-processing system anchored to a biological metabolism is anchored along with it.

**3.3 Examples of generative entrenchment in the brain.** Cao gives four examples.

- **Glia.** Glia come before neurons in development and support neural survival through metabolism. They also modulate neurons involved in memory. There is some evidence (Han et al., 2013) that glia play a larger cognitive role in humans than in simpler animals. A component that began as metabolic support becomes part of cognitive architecture.
- **Neural adaptation.** Adaptation begins as a metabolic feature: neurons become less excitable after firing because of resource depletion. In complex nervous systems, the system has exploited this to detect novelty, and further mechanisms, such as active top-down suppression, have been built on it. Repetition suppression in fMRI is a case of a side effect turned into a function.
- **ATP.** ATP is the energy currency of the cell, but it also drives calcium waves in astrocytes, breaks down to adenosine (which inhibits spiking and is a main determinant of sleep pressure in mammals), and contributes to cAMP signalling. GTP can supply energy but cannot replace ATP's extracellular signalling, because neurons have adenosine receptors rather than guanosine receptors. Cao argues that ATP's physical realization is therefore heavily constrained by the many roles it plays.
- **Shared neurochemicals.** Lactate, BDNF, growth factors, endocrine products and neurotransmitters such as dopamine all play several roles at once. Dopamine contributes to motor commands, reward prediction, and blood-flow regulation. In Parkinson's patients treated with L-DOPA, a significant fraction develop gambling disorders while motor symptoms improve, which Cao presents as evidence that fiddling with one function disturbs others.

**3.4 Why can't multiplexed functions be unbundled and separately realized?** The natural reply is to assign each role of ATP to a separate component, add components that keep the roles coupled, and then black-box the whole ensemble as a single "ATP-role" component. Cao answers that this works only for small numbers of components and functions. When many components have functions that cross-cut the boundaries of the black boxes, duplicating their interactions requires a combinatorial explosion of further components to discipline those interactions in the way the original substrate does. Space, timing and robustness requirements make this harder still.

Cao then argues that the lack of modularity is not confined to the cellular level. Nitric oxide does not have one role that could be boxed off. Large brain regions such as the visual system have roles in circadian coordination as well as perception, and capacities such as contour detection involve retina, V1, and higher-level priors in ways that cannot be isolated. The mapping from psychological capacities to neuroanatomical parts is not one-to-one. Cao calls this a "causal thicket" (Wimsatt, 2007).

### Section 4: Can we loosen the constraints on multiple realization?

Cao considers an objection: if the relevant behavioural profile is fine-grained enough to distinguish any physical duplicate from the original, nothing could be multiply realized. She accepts that fine-grained neural duplication is too demanding, and says this was a convenient starting point rather than the real requirement. What is needed is functional duplication at the level of detail needed to preserve the relevant psychological properties, and nothing more.

Standard functionalism assumes an intermediate level of abstraction, between biology and behaviour, called "the functional level." Cao notes that we have no theoretical guarantee that such a level exists. If it does, the burden is on the functionalist to show it, with patterns that are independently measurable by neuroscientific tools rather than inferred from behaviour. Different psychological phenomena might need different abstractions, and there may be no single functional level.

She considers two ways to loosen the requirement.

1. **Coarsen the behavioural profile.** Perhaps an android need not speak in monotone to count as human, if broad behaviour is human-like. But coarsening can go too far: at some level, a notebook and biological memory count as playing the same role, and that level no longer supports psychologically interesting distinctions. The right level has to explain and not merely re-describe psychological phenomena.
2. **Coarsen the functional organization.** Describe the functional roles of groups of neurons using population-level statistics, which neuroscience increasingly does. Cao argues that this runs into the same problem. In a biological brain, population regularities survive individual variability through redundancy and fine adaptive adjustments. A chip that copies the average behaviour of a neuron, but not its instance-by-instance adjustments, removes exactly the compensation that keeps the population stable. Cao compares this to riding a bicycle: a rider who holds the handlebars perfectly still on average is still making continuous corrections, and a mannequin would fall over. Simulated networks with few units show epileptic-like behaviour when small changes are introduced, so replacement networks may be fragile copies of one input-output relation.

She considers a fix in which replacements also compensate for neighbours' activity. Synaptic scaling, which homeostatically adjusts a neuron's input sensitivity, is a plausible mechanism, but it depends on protein synthesis and intracellular transport, so replicating it requires much of the biochemistry the replacement was supposed to avoid. Population-level generalizations also hold only within a vast set of ceteris paribus conditions, many of which fail when biochemistry is removed.

Cao then answers an objection from the animal kingdom. Many animals realize similar mental profiles with very different body plans, which looks like multiple realization. She says no: at the cellular level, animal brains are very similar to ours. Putnam's octopus, for example, has peripheral touch receptors that use chemical neurotransmitters, sensory areas distinct from motor areas, and endogenous opioids acting on receptors genetically similar to ours. Apparent differences are often underlain by similarity. Her argument does not show that other biological systems could not implement the same function. The difference that matters is between biological realizations, with their evolved capacities for adaptation, and non-biological substrates. Footnote 40 adds a caution that experiments on neurons in dissociated cultures or slices can misrepresent in vivo function.

Cao's conclusion from this section is that the functionalist must separate the parts of the causal structure that matter from those that do not. Because of generative entrenchment, the separation looks unlikely at the cellular and molecular level, and the metabolic and permissive functions of the brain are intertwined with its cognitive functions.

### Section 5: Implications for functionalism

Cao describes an earlier conception of functionalism, due to Putnam, in which functional organization is the machine-table of the whole system. On that conception, functions do not depend on a particular individuation of parts, and materialism becomes "a light cloak" over an unconstrained theory of mental states. Machine functionalism has mostly been abandoned, but many philosophers still take the spirit of functionalism to be freedom from material constraints and from biological detail.

Cao argues that standard functionalism, understood in terms of the causal roles of a complex system's constituents, is an "iron cage." If she is right that fine-grained replacement is nomologically impossible, the only functionally isomorphic systems, even individuated coarsely, are made of biologically similar stuff. The burden of proof falls on the functionalist, who must show that a silicon neuron can do what a biological one does. Cao notes that this makes Block's Blockhead and Aunt Hilary cases easy to dismiss from a functionalist standpoint, because their machinery could not realize the required functional organization given the constraints of matter.

She accepts that this implication cannot be what anti-chauvinists had in mind when they replaced the identity theory with functionalism. She argues that a chauvinist functionalism has much to recommend it. Bechtel and Mundale (1999) say that a functional criteria approach can apply to both psychological and brain states, even if MR is abandoned.

Cao then distinguishes three projects.

- **Analytic functionalism** (Lewis, Armstrong, and perhaps Clark, 2008) aims at conceptual analysis of mental-state talk. It is not threatened by the implausibility of MR, though at the personal level it says little about subpersonal causal roles, and it is a schema more than a finished theory.
- **High-church computationalism** (Dennett, 1986), which relies on the promise that minds can be studied without attention to bodies and brains, depends on the truth of the MR bet. Losing the bet means functionalists must learn the biological details.
- **A scientific functionalism** looks for a sweet spot of abstraction, above the details that do not matter for a phenomenon but with enough structure to be more informative than behaviourism. Whether such a level exists may differ across domains. Cao is more optimistic about neural prostheses and brain-computer interfaces for narrow tasks, where many holistic constraints are lifted. She is more sceptical about uploading a whole cognitive economy to a virtual environment while preserving its relevant capacities.

Her closing position is that taking functionalism seriously pulls in two directions. One is a methodological behaviourism that specifies capacities top-down and asks what computational architectures could realize them. The other is a biologically focused identity theory that attends to messy biological detail. If the constraints are strong enough, these might meet in the middle. She also says that to understand general features of possible cognitive architectures, we can look at whatever physical architectures work, and that successes in AI come from exploiting substrates different from our own, not from copying our fine-grained functional architecture.

### Beyond the assigned excerpt

The whole paper is assigned, so there is no excerpt to set aside. The references are a long list that draws on neuroscience reviews (for example Bullock et al., 2005 on the neuron doctrine; Wimsatt, 2007 on generative entrenchment; Polger and Shapiro, 2016 on the MR book), and on computational neuroscience work that Cao cites as partial successes for task-specific models (Yamins and DiCarlo, 2016; Kell et al., 2018; Schrimpf et al., 2021).

## Techniques & methods explained

The paper's main argumentative moves are the following.

- **Nomological rather than metaphysical standard.** Cao asks whether duplication is possible in our world, given the laws and enough resources, not whether it is conceivable. This turns thought experiments into empirical claims that can be checked against neuroscience.
- **Input-output function specification for a replacement.** A replacement is judged by the full functional profile of the part it replaces: spiking, history-dependence, self-modification, diffuse signalling, glial interaction and vascular interface. Failing to specify any of these weakens the replacement.
- **Argument from integration.** If a function decomposes into independent subfunctions, each can be replaced by an alternative substrate. If it is multiplexed, a single substrate must satisfy all its constraints at once. The argument predicts where replacement becomes hard, namely at components with many roles.
- **Generative entrenchment.** Evolution co-opts existing infrastructure, so parts with many dependencies cannot be replaced without breaking the whole system. Used to explain why biological functions become tangled over time.
- **Compensatory differences.** Cao considers how an alternative substrate could match behaviour by changing its internal organization. She argues this removes the claim to identical functional organization, so it is not genuine MR.
- **Coarse-graining the functional level.** She tests whether a coarser description (behavioural or population-level) would make replacement feasible. Her answer is that coarse descriptions either lose psychological detail or inherit the same robustness and adaptation problems.
- **Black-boxing and its combinatorial limits.** Groupings of components can be treated as single functional units only if their interactions can be disciplined cheaply. Cao argues that for densely interacting brain components this fails.

## Pros, cons & trade-offs it surfaces

| Aspect | Strength or cost (as the paper presents it) |
|---|---|
| Empirical grounding | Uses specific neuroscience (ion channels, NO, glia, blood flow, ATP) to test a claim usually handled by intuition |
| Clarity of target | Targets the canonical Putnam-Fodor formulation of MR, not all formulations; acknowledges alternative characterizations (Piccinini and Maley, 2014) |
| Nomological framing | Shifts the debate from what is conceivable to what is physically achievable, which matters for connectomics and uploading |
| Chauvinism | Gives a principled version of biological chauvinism, but Cao concedes it cuts against what anti-chauvinists wanted from functionalism |
| Coarse-graining | Shows that loosening the requirement is necessary, but has no settled answer for where to draw the level |
| Scope | Argues about the brain's functional organization for mental states in organisms, not about all possible minds |
| Limitations as Cao states them | Leaves open whether a tractable functional level exists; says the question is "empirically open" |

Cao's view on trade-offs: the choice between a fine-grained functional duplicate (very hard) and a coarse one (may not preserve psychologically important distinctions) is the central one. She also notes that narrow tasks and neural network models are more amenable to alternative realization, because they do not carry the full set of holistic constraints.

## Key concepts & terminology

- **Multiple realizability (MR)** - the thesis that the same kind of mental state can be produced by systems with very different physical constitutions.
- **Nomological possibility** - what is physically possible in our world given its laws, with enough resources. Cao's standard for the argument.
- **Metaphysical possibility** - what is conceivable or consistent. Cao sets it aside as the less relevant standard for functionalism as a research guide.
- **Neuron doctrine** - the claim that the only functionally relevant aspect of the brain is neuronal activity, especially action potentials.
- **Neural replacement scenario** - Chalmers's thought experiment in which neurons are replaced one by one by functionally identical silicon chips.
- **Organizational invariance** - the thesis that the same functional organization yields the same mental state. Cao's argument is compatible with it.
- **Functional duplicate** - a system that matches the original's functional organization at the relevant level of detail, not just its behaviour.
- **Generative entrenchment** - Wimsatt's term for features that many other features come to depend on, because they played a role in generating them.
- **Multiplexing of functions** - one component serving several functions at once, which makes its constraints harder to satisfy in an alternative substrate.
- **Decomposability** - the property of a function that can be divided into subfunctions realized by separate components, which makes replacement easier.
- **Causal thicket** - Wimsatt's term for a region of causal structure where levels and perspectives break down so that no clear scale is picked out.
- **Compensatory differences** - internal changes that let an alternative substrate approximate the original's behaviour, which Cao argues rule out identical functional organization.
- **Population coding** - the view that neural functional roles are best described by the statistics of groups of neurons.
- **Synaptic scaling** - homeostatic regulation of a neuron's sensitivity to input, which Cao uses as an example of biochemistry that is hard to replicate.
- **Biological chauvinism** - the view, which Cao partly accepts, that only biologically similar systems can realize the relevant functional organization.
- **Analytic functionalism** - the project of giving conceptual analyses of mental-state terms through their causal roles. Cao argues it survives the failure of MR.
- **Methodological behaviourism** - a top-down approach that specifies capacities first and then asks which computational architectures could realize them.
- **Triviality arguments** - Searle's and Putnam's worry that any sufficiently complex system can be given almost any functional description.

## Evidence, examples & notable data points

- **Dendritic reach.** Dendritic arbors can span hundreds of microns, while the cell body is about 40 microns across (Cao, Section 2.2a).
- **Ion channels.** A neuron membrane has tens of thousands of ion channels, each with its own conductance curves (Section 2.2b).
- **Astrocyte territory.** An astrocyte's range of 200 to 300 microns can contact hundreds of neurons, which Cao uses to illustrate the difficulty of an astrocyte replacement (Section 2.2e).
- **Temperature.** Cooling a brain region by 1 to 2 degrees Celsius makes neurons harder to fire (Section 2.2c).
- **Simulation cost.** Simulating a single protein-protein interaction for less than a millisecond is computationally expensive, which Cao uses to argue that some simulations could be nomologically impossible in the time available (footnote 11).
- **Wiring.** Marr (1982) noted that connections in the brain outnumber nerve cells by a factor of about 10^4, and that wiring is cheap in biology but restricted in conventional technology. Cao notes that wiring length still matters in biology (footnote 16).
- **Parkinson's and L-DOPA.** A significant fraction of Parkinson's patients given L-DOPA develop gambling disorders while their motor symptoms are relieved (Section 3.3, citing Pirritano et al., 2014 and Schultz et al., 1997).
- **Glia.** Some evidence (Han et al., 2013) suggests glia play a more substantive cognitive role in humans than in simpler organisms.
- **Adenosine and sleep.** Adenosine, produced by breakdown of extracellular ATP, is described as a main determinant of sleep pressure in mammals (Section 3.3).
- **Chess.** A cheap chess machine can match a strong human's moves while searching far more positions, illustrating how behaviour can match with different organization.
- **Octopus.** Putnam's octopus has pain-related features (peripheral touch receptors with chemical neurotransmitters, opioid receptors similar to ours) that Cao cites to argue against a clean case of multiple realization in animals (Section 4).
- **Dennett's quote.** Cao quotes Dennett's point that one cannot tear a person from their body and leave a clean edge. This is her main image for why the periphery cannot be cut off.

## Connections

### Within this section

- **Reading 05, Butlin et al., "Consciousness in Artificial Intelligence"** ([../readings/05-consciousness-in-artificial-intelligence-insights-from-the-s.md](05-consciousness-in-artificial-intelligence-insights-from-the-s.md)). Butlin et al. derive indicator properties from scientific theories and apply them to AI architectures. Cao's argument bears on which indicator properties could be satisfied on a non-biological substrate. Her view suggests that properties tied to specific biochemistry may be hard to satisfy in silicon, while computational properties may be easier.
- **Reading 04, Seth, "The Mythology of Conscious AI"** ([04-the-mythology-of-conscious-ai-consciousness-and-computation.md](04-the-mythology-of-conscious-ai-consciousness-and-computation.md)). Seth argues against computational functionalism and for a biological view. Cao gives the detailed neuroscience behind a similar conclusion. Both are "against" readings, and a reader can compare Seth's broader case with Cao's specific one.
- **Reading 08, Chalmers, "Absent Qualia, Fading Qualia, Dancing Qualia"** ([08-absent-qualia-fading-qualia-dancing-qualia.md](08-absent-qualia-fading-qualia-dancing-qualia.md)). This is the paper whose replacement scenario Cao is answering. Chalmers argues that gradual replacement preserves experience. Cao argues that the replacement is not nomologically possible at the required level of detail. Read together, they are a direct debate.
- **Reading 07, Chalmers, "Could a Large Language Model be Conscious?"** ([07-could-a-large-language-model-be-conscious.md](07-could-a-large-language-model-be-conscious.md)). Chalmers's LLM paper takes the substrate question for granted in a different way. Cao's argument concerns human brains, so its bearing on LLMs is indirect.
- **Reading 11, Shiller, "Functionalism, Integrity and Digital Consciousness"** ([11-functionalism-integrity-and-digital-consciousness.md](11-functionalism-integrity-and-digital-consciousness.md)). Shiller argues that functionalism requires implementation constraints that current neural networks do not meet. This is a related but distinct argument from implementation, and is a natural companion to Cao's.
- **Reading 10, Seth and Bayne, "Theories of Consciousness"** ([10-theories-of-consciousness.md](10-theories-of-consciousness.md)) and reading 12, Schiavo ([12-mental-state-breakdown-consciousness-in-ai-explained-part-1.md](12-mental-state-breakdown-consciousness-in-ai-explained-part-1.md)). Seth and Bayne survey theories that Cao's argument may affect differently. Schiavo's global workspace account is the one Exercise 1 suggests learners start with.
- **Unit 2 Glossary** ([01-unit-2-glossary.md](01-unit-2-glossary.md)). Use it to check terms such as functionalism, substrate independence and multiple realizability.
- **Section page text.** The page asks learners to explain computational functionalism and discuss arguments for and against it. Cao is the best candidate for the "against" argument in Exercise 2 if the learner wants a developed case rather than a short blog post. The page's exercises do not name her paper, so this is an interpretive link.

### Across the course

- **Unit 1: Introduction and Theories of Moral Standing.** Moral-standing theories often ask which features matter for moral patienthood. Cao's argument matters for whether digital systems could have the features those theories name, since if those features depend on biology, a digital system might lack them.
- **Unit 3: Evaluation of Consciousness and Other Mental States.** Evaluating mental states in AI requires some view on what counts as the same mental state across substrates. Cao's distinction between coarse and fine functional levels is directly relevant to that evaluation.
- **Unit 4: Perceptions of Consciousness.** Section 4.1 assigns Seth's "Conscious Artificial Intelligence and Biological Naturalism" (a different Seth paper from reading 04 in this section). That paper's biological-naturalism position overlaps in its conclusions with Cao's. The link is listed in this section's Exercise 1 as a biological-naturalism option, so learners who pick it will meet a second biology-first argument.
- **Unit 5: Interactions with AI Safety and Ethics.** Cao's point that a functional duplicate might be impossible or approximate bears on whether AI moral status can be inferred from behaviour. Her warning against behaviourism is relevant to behaviour-based welfare tests.
- **Unit 6: Approaches under Uncertainty.** Cao's argument is an empirical bet against substrate-neutrality. Unit 6 asks how to act under uncertainty about such claims, and Cao's work shows how an empirical premise can shift credence in functionalism without settling it.
- **Unit 7: Digital Minds Governance.** Governance proposals that rely on functionalist criteria for AI moral status depend on the substrate question Cao addresses. If her argument holds, governance may need separate criteria for biological and non-biological minds.
- **Unit 8: Reflections and Next Steps.** Learners can use Cao's paper as a reference point for how to test assumptions in digital-minds claims.

**Tensions.** Cao argues against substrate-neutrality at the level of fine-grained neural duplication, while Chalmers (reading 08) argues for organizational invariance. Cao concedes that invariance is compatible with her view, so the two can coexist. Their disagreement is about whether a silicon system can instantiate the organization in the first place.

## Critical perspective

*This section is my own analysis, not the source's view.*

**Assumptions.** Cao's central premise is that the relevant functional level for mental states is at or near the neural level, or at least that a fine-grained enough level is needed to preserve mental properties. She acknowledges that her argument for this depends on the level of description and asks whether a higher level exists. If a much coarser level captures the psychology, her main conclusion weakens. She is open about this, but the paper's rhetoric pushes toward the fine level.

**Limitations.** The argument is about nomological feasibility in our world. It does not show that digital minds are impossible in principle. Cao explicitly says that other biological systems might implement the same function, and that narrow AI can succeed without copying brains. So the argument is best read as a claim about whole-brain uploading and neural replacement, not about every AI system. Readers should be careful not to extend it to LLMs or other architectures that never try to replicate neurons.

**Contested claims.** Several of Cao's steps are contestable.

- The claim that silicon will need to reproduce the whole biochemistry of a neuron to reproduce its function is an empirical bet. Neuromorphic and machine learning approaches try to replicate function at different levels, and Cao's counterexamples are mostly about the difficulty of matching a specific organism, not about whether matching is possible in principle.
- The argument from generative entrenchment is persuasive as a narrative of evolution, but it does not show that the entrenched functions cannot be decomposed by future science. Cao's claim that decomposition "seems unlikely" is a judgment, not a proof.
- The octopus example is used to argue that animal minds share the relevant realizers, but it is an argument from similarity at the cellular level, which Cao herself concedes is not proof.
- Cao's critics, including Aizawa and Gillett (2009) and Aizawa (2013), argue that compensatory differences are a legitimate route to multiple realization. Fang (2018) argues that MR is genuine in biology. Cao engages these positions briefly and treats them as a contrast rather than a refutation.

**What has changed since 2022.** The paper is four years old at the time of writing (October 2026). Its examples come mostly from neuroscience and AI work published before 2022. The debate has moved toward large language models, which Cao's paper does not discuss. Cao's claim that successful AI exploits different substrates now reads as a more significant statement than it did in 2022, because the most capable systems do not try to reproduce neurons at all. I have not checked the post-2022 literature on neuromorphic hardware or brain emulation in detail, so I cannot say how much of her specific list of constraints remains unaddressed. That is something a learner should verify.

**How the course's other perspectives would push back.** Chalmers (reading 08) would reply that the replacement scenario needs only that each chip match the local input-output function, and that Cao's complexities can be built in given enough resources, which is a nomological rather than a metaphysical question. Shiller (reading 11) would likely agree that implementation constraints matter but would ask what specific constraints functionalism actually needs. Seth (reading 04) would be broadly sympathetic but might argue that Cao's functional-level framing still concedes too much to computational functionalism. Butlin et al. (reading 05) would ask whether the indicator properties they propose can be assessed without settling the substrate question.

**Why the argument matters for digital minds.** If Cao is right, arguments that move a human mind onto a computer through neural replacement are hard to sustain. If she is wrong or if coarser functional levels suffice, the argument does not block digital minds, but it does place a demand on proponents of substrate-independence to say what level of description they mean.

## Discussion questions

1. Cao says the relevant standard is nomological rather than metaphysical possibility. What would change in the debate if we accepted metaphysical possibility as the standard? Which claims in the course would be strengthened or weakened?
2. Take the neural replacement scenario (Chalmers, reading 08). Which of Cao's five categories of constraint (spiking, transducers, biophysics, self-modification, glia) do you think is the strongest objection, and why? Would the answer change if a sufficiently powerful simulator were available?
3. Cao distinguishes multiplexed functions from decomposable ones using the mousetrap and the chess machine. Do you agree that the brain's functions are multiplexed in the relevant sense? What would evidence against multiplexing look like?
4. Cao proposes two ways to loosen the constraints: coarsening the behavioural profile and coarsening the functional organization. Which seems more defensible to you as a level of description for psychological properties? Use the notebook-memory example to test your answer.
5. Cao accepts that her argument points toward "biological chauvinism" and argues it is a feature, not a bug. How should a researcher working on digital minds respond? Would Exercise 2's cf-debate.com arguments be stronger if they included Cao's position?
6. Compare Cao with Seth (reading 04). Both argue against computational functionalism from a biological starting point. Where does Cao's argument rely on specific neuroscience that Seth does not use, and where does Seth's broader argument fill a gap in Cao's?
7. Cao says successes in AI come from exploiting substrates different from our own. Does that point support or undermine the case for AI consciousness? Connect your answer to the course's Unit 5 on AI ethics.
8. Cao's paper was written before large language models became the central focus of the consciousness debate. Which of her claims would you expect to be most affected by that shift, and which would remain relevant?
