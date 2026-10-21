---
title: "Functionalism, Integrity and Digital Consciousness"
authors: "Derek Shiller"
year: 2024
url: https://philarchive.org/rec/SHIFIA-2
format: paper
course_location: "Unit 2: Theories of Consciousness > 2.1 Theories of Consciousness"
priority: Further
estimated_time_min: 43
source_text: ../../../../sources/functionalism-integrity-and-digital-consciousness__b1a7fa10.md
source_coverage: unavailable
---

# Functionalism, Integrity and Digital Consciousness

**One-line takeaway:** Even if consciousness depends only on abstract functional organization, a digital system must also implement that organization in the right way, and Shiller argues that current neural networks fail three proposed "integrity" constraints on proper implementation.

> **Source coverage warning.** The full text of this paper was not reachable. The local source file holds only the abstract (about 124 words, from a blog repost). The PhilPapers page returned HTTP 403, and the Springer article (DOI 10.1007/s11229-023-04473-z) redirected to a cookie-gated login page. The names and formulations of the three constraints, the worked examples and the author's replies to objections are therefore **not** covered below from the paper itself. What follows combines (a) the abstract, (b) a search-engine summary of the paper that could not be verified against the text, and (c) a 2023 EA Forum post by the same author that summarises closely related work. Items from (b) and (c) are labelled. Read the paper itself before relying on any detail of the constraints.

## Where this sits in the course

**What the section is trying to establish.** Section 2.1 is the course's conceptual core on consciousness. Its page asks three questions: what consciousness is and where our understanding stands; what computational functionalism is and what speaks for and against it; and what problems make consciousness hard to study, especially in AI. Its learning goals include explaining computational functionalism and its application to digital minds, and discussing arguments for and against it.

**What the course guide says about this reading.** The guide describes the paper as arguing that functionalism about consciousness requires implementation constraints which current neural networks fail to meet. Paraphrased: it is a paper about a specific gap in functionalism, not a general introduction to it.

**The role it plays.** Its priority is **Further**, so it is optional depth. The Core readings set up the basic debate: Saad and Mogenson on problems in studying consciousness, Schneider et al. on the myths around AI consciousness, Seth's critique of computational functionalism, and Butlin et al.'s indicator-property framework. This paper picks up one thread those readings raise but do not develop in detail: the step from "the right abstract organization" to "a physical system that actually has it". It is the course's most technical argument for why AI consciousness might be doubted on implementation grounds rather than on the claim that silicon is inherently incapable.

**Relation to the unit question.** The unit asks whether computational functionalism is true and what follows for digital minds. This paper grants a version of functionalism for the sake of argument and asks whether today's systems satisfy it. The exercises do not assign it. Exercise 2 asks learners to review one argument for and one against computational functionalism from cf-debate.com, and this paper is a natural candidate for the "against" side, though it is not on the course's list of suggestions.

## Purpose of the reading

**What the author is arguing.** Shiller argues that the prospect of consciousness in artificial systems is tied to whether functionalism is viable. Even if consciousness arises from abstract functional relations among a system's parts, it does not follow that every digital system implementing the right organization is conscious. Functionalism needs a theory of what counts as properly implementing an organization.

**For whom.** Philosophers of mind and cognitive science, and readers working on AI moral status who need to know which arguments depend on substrate and which on organization.

**The question it answers.** Which conditions must a physical system meet to count as implementing a functional organization in the sense that functionalism requires? And do current neural network models meet them?

## Detailed summary

*Structured from the abstract. Sub-headings follow the abstract's logic. Claims marked (secondhand) come from the search-engine summary and have not been checked against the paper.*

### 1. The problem: organization is not enough

The abstract opens by linking the question of AI consciousness to functionalism. The point is that a functionalist cannot simply say "run the right program and you get consciousness". The functionalist must say what it takes for a physical system to realise the program's organization. Otherwise the view is too permissive, because almost any physical system can be interpreted as implementing almost any computation. This is the implementation or triviality worry, which the rocks-and-walls cases dramatise (the same worry appears in the 2023 EA post by the author, and in Chalmers' 1996 paper "Does a Rock Implement Every Finite-State Automaton?", which appears in the search results but was not read here).

### 2. What existing constraints say

The abstract states that the existing proposals for constraints on implementation concern the **integrity** of the parts and states of the realizers of roles in a functional organization. In plain terms: the physical components that play each functional role should form a cohesive, stable unit, and the states they hold should be properly bound to the roles they play. Such constraints have been raised in the literature but are rarely worked out in detail, especially for artificial systems.

### 3. The three novel integrity constraints

The paper says it presents and motivates **three novel integrity constraints** on proper implementation. The abstract does not name them or state them. Secondhand summaries (not verified) describe them roughly as follows:

- **A direct link** between the material parts and the realizers of the functional roles, rather than a loose mapping that an outside interpreter imposes.
- **Internal causal powers.** The realizers should perform their roles because of their own physical causal powers, not because an observer assigns them the role.
- **Persistence over time.** The realizers should keep their identity across the computation. A component should not be reassigned to a different role or replaced by a different physical part from one step to the next.

Treat these as a reconstruction of the summary, not as the paper's wording. The paper's exact formulations matter for any careful assessment.

### 4. The verdict on current networks

The abstract concludes that current neural network models do not satisfy the three constraints. The author's earlier 2023 post gives the clearest reason for why (see the next section): in standard digital hardware, the memory cells that store a network's node values are allocated dynamically, so the physical locations may change on each run. That breaks any persistence requirement on realizers, even when the functional organization is the same as a brain's.

## Techniques & methods explained

**1. Separating organization from implementation.** The argument splits functionalism into two components: a theory of which organization is needed for consciousness, and a theory of what it is to implement that organization physically. Current debate often assumes the first and neglects the second. The paper's move is to show that the second has real content and can rule out systems the first would include.

**2. Integrity constraints as a filter.** The constraints are used as necessary conditions. A system that fails any one is not a candidate for consciousness on this view, even if its abstract organization is brain-like. The filter works by asking about the physical parts that play the roles, not about the behaviour or the algorithm.

**3. Thought experiments on implementation (from the 2023 post, secondhand for the paper).**
- *Brain transducer.* A machine takes a frozen brain, disassembles it, and builds a new brain in the state the original would reach next. Feeding outputs back as inputs produces a sequence of frozen brains. The author suggests this sequence may lack unified experience even if functionalism is true, and by analogy computers with dynamic memory may lack it too.
- *Mirror grid.* A system so complex that any structure can be read into it. If it were conscious, the author argues, nearly everything complex would be, which most functionalists would reject.

These cases work by intuition. Their force depends on whether readers share the intuitions, and the author concedes this in the EA comments.

**Where it fails.** The method depends on intuitions about cases far from ordinary experience. It also assumes that the right physical individuation of "realizers" is clear. If the relevant parts are hard to individuate in brains or in chips, the constraints will be hard to apply in either direction.

## Pros, cons & trade-offs it surfaces

| Aspect | The source's view (as far as it is accessible) | Critic's view (secondhand, Dung 2025) |
|---|---|---|
| Core claim | Functionalism needs integrity constraints; current networks fail them | Constraints are implausible |
| Support | Distinctive constraints motivated by intuitions about implementation | Constraints rest on conflating intuitions about computational implementation in general with intuitions about consciousness |
| Hardware | Current neural network hardware fails the constraints | The argument against current hardware is persuasive, but neuromorphic hardware might later satisfy the constraints |
| Implication | Digital consciousness is not settled by functional organization alone | Shiller's view is among the most detailed implementation-based accounts |

**Trade-off the paper implies.** A strength of implementation constraints is that they can yield concrete, architecture-level verdicts. A weakness is that such verdicts can be engineered around. If implementation matters, a designer might change hardware without changing the algorithm, which the author says gives a "welfare lever" in one direction or the other (EA post, claim 7). This makes the verdict depend on engineering choices, which some will see as a reason to doubt that consciousness is what the constraints track.

## Key concepts & terminology

- **Functionalism** - the view that mental states, including consciousness, are individuated by their functional roles rather than by their physical substrate.
- **Functional organization** - the pattern of causal relations among a system's parts, abstracted away from what the parts are made of.
- **Realizer** - the physical component or state that plays a functional role in a system.
- **Implementation** - the relation between a physical system and the abstract organization it realises.
- **Triviality (implementation) problem** - the worry that almost any physical system can be interpreted as implementing almost any computation, so implementation must be constrained.
- **Integrity constraint** - a condition on how the realizers of functional roles must be unified, bound to their roles and stable over time, for the implementation to count.
- **Persistence (continuity) of realizers** - the requirement that the physical parts keep their identity across the computation.
- **Dynamic memory allocation** - the hardware practice of assigning memory locations at runtime, so the physical cells storing a value can change between runs.
- **Neuromorphic hardware** - chips designed to mirror neural structure more closely, which might in principle satisfy the constraints.

## Evidence, examples & notable data points

This is a philosophy paper. It has no experiments or statistics that the course-accessible sources report.

- **Abstract (verified):** the paper presents three novel integrity constraints, and says current neural network models do not satisfy them.
- **Dynamic memory (2023 EA post, by the author):** the cells storing a network's node values may change with each invocation, which is the example used against persistence.
- **Brain transducer and mirror grid (2023 EA post, by the author):** described above as intuition pumps.
- **Encryption example (secondhand, unverified):** if a brain's data were encrypted but still updated in the same way, would the system remain conscious? The summary says the material-complexity constraint suggests not.
- **Dung 2025 (secondhand):** the constraints are described as the most detailed implementationalist account, and are found implausible.

## Connections

### Within this section

- **[Unit 2 Glossary](01-unit-2-glossary.md)** (Core): the terms used here (functionalism, realizer, implementation) are defined there. Read it first.
- **[Digital Minds I](02-digital-minds-i-issues-in-the-philosophy-of-mind-and-cogniti.md)** (Core): introduces the problems in studying consciousness; this paper is a deeper dive into one of them, the implementation problem.
- **[Is AI Conscious?](03-is-ai-conscious-a-primer-on-the-myths-and-confusion-driving.md)** (Core): the primer's discussion of theories and of non-physicalist options is the wider frame. The primer's point that AI consciousness claims depend on the theory adopted is the setting for this paper's claim that the implementation question matters.
- **[The Mythology of Conscious AI](04-the-mythology-of-conscious-ai-consciousness-and-computation.md)** (Core): Seth argues against computational functionalism from a biological view. Shiller accepts functionalism for argument's sake and finds a narrower route to skepticism. The two readings are allies on the conclusion but not on the premises.
- **[Consciousness in AI (Butlin et al.)](05-consciousness-in-artificial-intelligence-insights-from-the-s.md)** (Core): the indicator properties are functional and architectural. Shiller's constraints ask whether such indicators, when realised in real hardware, are realised properly.
- **[Multiple Realizability and the Spirit of Functionalism](06-multiple-realizability-and-the-spirit-of-functionalism.md)** (Further): Cao challenges substrate independence through the integration of brain function with physiology. Both papers attack the easy version of functionalism, but Cao does so from biology and Shiller from implementation.
- **[Could a Large Language Model be Conscious?](07-could-a-large-language-model-be-conscious.md)** (Further): Chalmers considers LLMs with a more open mind than Shiller's verdict on current networks would suggest. A useful comparison for the exercise on the debate.
- **[Absent Qualia, Fading Qualia, Dancing Qualia](08-absent-qualia-fading-qualia-dancing-qualia.md)** (Further): Chalmers' gradual replacement argument supports organizational invariance. Shiller's constraints are one way to resist its conclusion without denying functionalism outright, by insisting that the replacement must preserve integrity.
- **[Phenomenal Consciousness, Defined](09-phenomenal-consciousness-defined-and-defended-as-innocently.md)** (Further): Schwitzgebel's definition gives the target that functionalist theories are meant to explain.
- **[Theories of Consciousness (Seth and Bayne)](10-theories-of-consciousness.md)** (Further): the review of IIT, GWT and others. Shiller's constraints would apply differently to each theory's architectural claims.
- **[Mental (state) breakdown: Consciousness in AI explained](12-mental-state-breakdown-consciousness-in-ai-explained-part-1.md)** (Further): Schiavo's accessible account of global workspace theory. A good way to see what an architectural theory claims before asking whether the implementation meets the constraints.
- **[Landscape of Consciousness](13-landscape-of-consciousness-website.md)** (Further): places functionalist and non-physicalist positions on one map.

**Section page.** Exercise 1 asks learners to pick one theory and assess its application to digital minds. A learner choosing global workspace theory or recurrent processing could use this paper's constraints as a test of whether the chosen architecture is realised properly in hardware. Exercise 2 asks for one argument for and one against computational functionalism. This paper is a candidate for the "against" side, but it is not assigned.

### Across the course

- **Unit 1 (Introduction and Theories of Moral Standing):** the question of which theory of consciousness grounds moral status. If implementation matters, moral status may depend on engineering choices, which bears on the moral-standing theories covered in unit 1.
- **Unit 3 (Evaluating mental states):** the problem of attributing mental states to systems. Implementation constraints are one way to decide which attributions are warranted.
- **Unit 4 (Perceptions of consciousness):** the course assigns Seth's *Conscious Artificial Intelligence and Biological Naturalism* in section 4.1 (linked from the Exercise 1 list on the 2.1 page). That paper rejects computational functionalism on biological grounds. This paper takes a different route to skepticism, through implementation rather than biology. The two can be compared in the same session.
- **Unit 5 (AI safety and ethics):** if implementation matters, design decisions that look like safety or efficiency choices could also change whether a system is conscious.
- **Unit 6 (Approaches under uncertainty):** the implementation argument lowers the probability of consciousness in current systems without ruling it out for future hardware. That is a clear case of reasoning under theory uncertainty.
- **Unit 7 (Digital minds governance):** the "welfare lever" point (secondhand, from the EA post) raises governance questions about regulating hardware and architecture for welfare reasons.
- **Unit 8 (Reflections and next steps):** the open question of whether consciousness tracks organization, implementation or biology.

**Tension to hold on to.** Chalmers and Shiller both use thought experiments about gradual change. Chalmers reads them as showing that organization is what matters. Shiller reads the same kind of case as showing that implementation can make a difference. The course's Unit 2 exercises invite learners to adjudicate that tension.

## Critical perspective

*This section is my own analysis, not the source's view. It is based on the abstract and the secondhand material above, and flags where the claims are unverified.*

- **Date.** The paper appeared in 2024 and the course page was fetched on 2026-10-08. Since then, the author has published related work on implementation and digital consciousness (per the search results: a 2025 Erkenntnis paper "Bomb Threats for Functionalists" and a 2025 Synthese paper on interwoven computation in GPU clusters). Neuromorphic and other non-standard hardware has also developed. The claim that "current neural networks fail the constraints" is about the hardware of 2024 and may need revisiting for newer systems, though the dynamic-memory point may still hold for most deployed systems.
- **Assumptions.** The argument assumes that the parts and states of a system can be individuated in a principled way. For brains and chips this is not obvious, and the constraints are only as clear as the individuation.
- **Contested claims.** The constraints are motivated by intuitions in unusual cases (the brain transducer, the mirror grid). Those intuitions are the weakest link. Dung (2025, secondhand) argues they conflate general and consciousness-specific intuitions about implementation.
- **Design-dependence.** If the verdict depends on whether a system uses dynamic memory, a designer could in principle change the verdict without changing the system's behaviour. Some will find that a reductio of the constraints as a theory of consciousness; others will accept it as a surprising but coherent consequence.
- **Other perspectives in the course.** Chalmers' gradual-replacement argument would push back by asking why swapping integrity-preserving parts should matter if the organization is preserved. Seth would welcome the skepticism but reject the premise that organization is the right level of description. Butlin et al. would likely treat the constraints as an extra check on their indicator approach rather than a reason to abandon it.

## Discussion questions

1. The abstract says functionalism "needs" implementation constraints. What would go wrong if you accepted functionalism without any such constraint? Which of the rocks-and-walls cases motivates the constraint most strongly?
2. Pick one of the three integrity constraints (ideally the one you can best reconstruct from the paper itself). Does it seem necessary for consciousness? Would a brain satisfy it at every moment?
3. Shiller's verdict depends on hardware details such as dynamic memory allocation. Is it a strength that the view yields concrete engineering predictions, or a weakness that consciousness would then seem to depend on engineering choices?
4. Compare Shiller's implementation route to Seth's biological route. Can both lead to skepticism about current AI while disagreeing about what consciousness requires?
5. Use the Exercise 2 format. Write one argument for and one against computational functionalism, then say where this paper's constraints fit. Does the paper make the "against" case stronger, or does it just move the dispute to implementation?
6. Chalmers' gradual-replacement argument and Shiller's continuity constraint make opposite predictions about a brain whose neurons are replaced one at a time. Which prediction do your intuitions support, and what would change your mind?
7. Given that Shiller's verdict may change as hardware changes, how should a researcher in unit 6 (approaches under uncertainty) weigh this argument against the indicator-property approach in Butlin et al.?
