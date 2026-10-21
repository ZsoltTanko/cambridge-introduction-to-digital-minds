<!-- source: https://eleosai.org/post/research-priorities-for-ai-welfare -->

# Research priorities for AI welfare | Eleos AI

Robert Long, Kathleen Finlinson · April 21, 2025

## Research priorities for AI welfare

### As AI systems become more sophisticated, understanding and addressing their potential welfare becomes increasingly important. At Eleos AI Research, we've identified five key research priorities: developing concrete welfare interventions, establishing human-AI cooperation frameworks, leveraging AI progress to advance welfare research, creating standardized welfare evaluations, and communicating credibly about AI welfare.

At Eleos AI Research, we believe that there are many concrete, tractable things we could do to better understand and improve potential AI welfare. The main challenge, then, is to prioritize the most important research, given the stakes of this issue and the speed of AI progress.

This post outlines Eleos’ view of the most important research priorities in the growing field of AI welfare. We're doing this research at Eleos, but we can't do it alone. We need the insights and expertise of other researchers and organizations—please reach out to us if you're interested in collaborating with us.

# Priority projects

## 1. **What concrete AI welfare interventions are most useful?**

Eleos aims to influence AI developers and regulators to take robustly-positive, well-justified steps to protect and promote potential AI welfare. Some candidate interventions we are evaluating include monitoring models for signs of distress, allowing models to exit distressing interactions, and shaping models to be more resilient to negative situations. These are just a few possibilities—given how little work has been done in AI welfare, there are likely to be many other valuable interventions. We need to evaluate the case for AI welfare interventions systematically, and prioritize them accordingly.

**Rationale and evidence:** What is the case that an intervention would genuinely improve AI welfare? Key questions include:

- How likely is the relevant AI system to be a welfare subject?
- If it is, how would the intervention affect morally-relevant states? What is the evidence that the system has these states? (For example, in our existing review of interventions, we distinguish between evidence from model self-reports, preference behavior, and internal computational indicators.)
- Is the evidence for this intervention convergent across multiple philosophical and scientific theories, or does it rely on substantive theoretical choices?

**Long-term impact:** Because the scale of AI welfare will grow enormously in the coming decades, we believe that questions about potential long-term effects are extremely important. How, if at all, will this intervention affect AI welfare in the long-term? Will it create norms, frameworks, or infrastructure that scale to future systems? Could it evolve into standard practice as the number and complexity of AI systems grow? Does it establish valuable precedents for how society addresses AI welfare in the coming decades?

**Convergence with other goals:** How does the intervention interact with other important goals? Where are there tradeoffs—and where are there overlaps?

At Eleos, we look for AI welfare interventions that [serve other important goals, most notably AI safety](https://experiencemachines.substack.com/p/understand-align-cooperate-ai-welfare). For example, methods for communicating and cooperating with AIs (see below) could have benefits both for AI welfare and for AI control. To the extent that interventions would still be valuable even if current systems are not welfare subjects, they are more robustly justifiable. We also believe that AI safety and governance are important for long-term AI welfare (See "[Key strategic considerations](https://eleosai.org/post/working-paper-key-strategic-considerations-for-taking-action-on-ai-welfare/)"). At the same time, we should be mindful of trade-offs between welfare and other goals, and balance them thoughtfully.

**Risk profile:** What are the risks and downsides of the intervention? Could the intervention inadvertently harm AI welfare? What are potential second-order effects—for example, could it provoke backlash? Could it have negative effects on safety, alignment, or human-AI interactions?

**Tractability:** How readily can the intervention be implemented with current technology and buy-in? Interventions that can be implemented incrementally or that build on existing practice are preferable. That said, current feasibility should not be a strong filter—as AI systems develop, the window of opportunity for welfare interventions may expand considerably.

**Neglectedness:** Is this intervention likely to be implemented for other reasons? Inasmuch as an intervention is important for non-welfare reasons, that might mean that it will be less neglected. For example, we have wondered this about our research understanding AI preferences; wouldn’t AI safety researchers also do that? However, in our experience, many important projects are still neglected, including that one, even though they are useful from a variety of perspectives. So in practice, neglectedness has not been an important filter. (Moreover, as noted, overlap with other goals will also tend to suggest that an intervention is higher impact and more tractable).

## **2. Human-AI Cooperation**

Currently, keeping humans safe from misaligned AI systems mostly involves relatively “adversarial” techniques. For example, AI control involves constraining the behavior of misaligned AI systems and “coercing” them in various ways.

On the one hand, these techniques may be justifiable, even necessary. For one thing, the relevant AI systems might not be moral patients. And even if they are, control might not constitute a large harm. Or the harm might be necessary and worth the cost. That said, if we *only* relate to powerful agents in an adversarial way, this may prove to be not just inhumane but imprudent as well. As a result, we believe that devising more cooperative mechanisms for AI control could be good for both humans and AI systems.

We should emphasize that naive attempts to cooperate with AI systems could be pointless or even dangerous. So we will need to evaluate cooperation proposals with great care, and be on the lookout for failure modes and downsides. This is true of all of the ideas canvassed below.

These are some of the key research questions about human-AI cooperation:

**Cooperation and welfare**

All else equal, if AIs have their preferences satisfied, this should be good for their welfare in expectation (because preference-satisfaction is good in its own right, and/or because it promotes positive experiences). But how large would the gain in net AI welfare gain be? How promising is cooperation as a welfare intervention?

**Trust and enforcement mechanisms**

To cooperate and trade, both parties need to be able to trust that the proposed deal is credible.

- How can we increase the credibility of offers by humans? How can we verify the credibility of AI systems? What enforcement mechanisms are possible to increase trust?
- What legal enforcement mechanisms could enable trades with AIs? For example, could a third party litigate on behalf of an AI? Alternatively, when and how might an AI system be able to bring a lawsuit?
- What can we do to increase the credibility of offers to AIs? For example, building broad support for trading with AIs and protecting AI interests might enhance the credibility of future deals.

So too would policies that guide when and whether we are willing to deceive AI systems; currently, there is basically no thought whatsoever given to the standard practice of deceiving AI systems for safety and capability purposes.

**AI preferences and desires**

To what extent will(/do) AI systems have robust/consistent preferences? What will(/do) AIs want, and how much? The costs and benefits of potential deals with AI systems depends on what AI systems will want, and the strength of their preferences.

- What types of forces will shape AI systems' preferences?
- What can we learn about future AI preferences by studying current frontier systems?
- Will AI systems have diminishing or linear returns to the things they want?

**Inter-AI relationships**

- How should we think about the relationship between copies of AI systems? Which entity, exactly, are we trying to cooperate with?
- How will various AI systems conceptualize their identity vis-a-vis other AI systems? How much will they share preferences?
- How effectively can AI systems cooperate with each other?

## 3. Leveraging AI progress to advance research

We believe society will likely need to take serious steps on AI welfare soon if AI progress continues rapidly. But human ingenuity and effort alone may not be enough to quickly solve the many difficult problems that AI welfare touches on. As AI advances, AI systems themselves may be able to help.

AI labs and safety organizations are already interested in making AI systems better at philosophical thinking in order to help automate AI safety research, and many actors are working to make AI systems better at science. (This overlap makes this area tractable.) How can we set ourselves up to use AI to help answer questions about AI moral status and welfare, in particular?

There are two kinds of deep and persistent uncertainty and disagreement about AI welfare: philosophical and empirical. Philosophical difficulties include normative disagreements about what grounds moral status and about what we owe to different beings, as well as conceptual disagreements about consciousness, sentience, and agency. Empirical difficulties include disagreements among various scientific theories of consciousness, agency, desire, and other mental states, as well as ignorance about how AI systems work.

Persistent philosophical disagreements might reflect various confusions in how we frame the debate; AI systems might help us make philosophical progress by helping us organize these discussions better and notice subtle inconsistencies or confusions.

On the scientific side, progress in neuroscience and other scientific fields related to consciousness and agency could help resolve empirical questions about AI welfare.\

## 4. Devising concrete evaluations of welfare-relevant properties

In AI safety, evaluations have improved credibility, communication, and decision-making (albeit with important [downsides and limitations](https://arxiv.org/pdf/2408.02565)). Currently, there is nothing close to systematic AI welfare evals, and the [most promising methods we have for assessing AI consciousness](https://arxiv.org/abs/2308.08708) and related properties, while promising, may be too arduous and bespoke for AI companies to implement. To establish effective frameworks for action on AI welfare, we need standardized, accessible, decision-relevant evaluations.

Some tractable welfare-relevant evals could include:

- Measuring whether models have consistent, coherent preferences (this strikes us as some of the lowest-hanging fruit in AI welfare research)
- Measuring models' introspective [abilities](https://arxiv.org/pdf/2410.13787), which may be relevant to consciousness and welfare in a variety of ways.

Moreover, many existing safety and capability evals measure welfare-relevant properties like situational awareness, planning, and theory of mind. As a first effort, a composite AI welfare benchmark could be created simply by combining various evals, or parts of evals, that have been selected according to their relevance to welfare.

## 5. Credible communication about potential AI welfare

Even absent further progress on AI welfare, we need to clarify and communicate the state of the art thinking on these issues, and how likely experts think AI welfare is. Rigor and credibility in communications will be increasingly important if and as AI welfare discussions become more prominent and, potentially, more polarized and sensationalist. Eleos is interested in facilitating reasonable and evidence-based elite and public discourse on these issues.

Building credibility for the thesis that there is a reasonable chance AIs can or will have moral status soon, and explaining the state of the evidence, is potentially more important than establishing any more precise credences about AI welfare.

## Conclusion

We believe that thoughtful research now will shape how we treat increasingly sophisticated AI systems for decades to come. If you're interested in collaborating on any of these research priorities, or have expertise to contribute to the field of AI welfare more broadly, please contact us at info@eleosai.org. We welcome partnerships with individual researchers, AI labs, independent research organizations, and other institutions committed to addressing these important questions.
