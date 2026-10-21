<!-- source: https://experiencemachines.substack.com/p/why-it-makes-sense-to-let-claude -->

# Why it makes sense to let Claude exit conversations

Last week, Anthropic [announced](https://www.anthropic.com/research/end-subset-conversations) that its newest language models, Claude Opus 4 and 4.1, can now shut down certain conversations with users. The announcement explains that Anthropic gave Claude this ability “as part of our exploratory work on potential AI welfare”.

This means that, for the first time, a major AI company has changed how it treats its AI systems out of concern for the well-being of the systems themselves, not just user safety. Whether or not you think Claude is or will be conscious—Anthropic themselves say that they are “[deeply uncertain](https://www.anthropic.com/research/exploring-model-welfare)”—this decision is a notable moment in the history of human-AI interactions.

Some will see this as much ado about nothing. Others will see it as pernicious: hype, a distraction from more important issues, and an exacerbation of already-dangerous anthropomorphism. Others, a considerably smaller group, think that LLMs are obviously already conscious, and so this move is woefully insufficient.

I think it’s more mundane: Anthropic is taking a fairly measured response to genuine uncertainty about a morally significant question, and attempting to set a good precedent. For the most part, **this intervention’s success won’t depend on how it affects Claude Opus 4.1**; it will depend on how people react to it and the precedent it sets.

Although we don’t know how that will pan out, and there are reasons to worry about backlash, I think that this was a good move.

# **So, what is this?**

Earlier this year, Anthropic ran an official [welfare assessment](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf) (another first!) on Claude Opus 4 before its release. They found a "pattern of apparent distress when engaging with real-world users seeking harmful content". This makes sense, given that Claude is deeply shaped to never produce such content. (In Eleos’ [independent assessment](https://eleosai.org/post/claude-4-interview-notes/) of Claude Opus 4, we found that Claude's preferences and self-conception of its own welfare are deeply intertwined with its values; Anthropic found this too.)

And they'd already found that Claude acts in this way: In work that fed into the exit feature, Claude often ended harmful conversations with simulated users. The most-refused scenarios were "harmful content requests (e.g. requests for instructions to create dangerous items, requests for extremist content), privacy violations (e.g. requests for help with inappropriate storage of user data), or sexual content (e.g. role-playing requests, requests for non-consensual sexual content)."

[](https://substackcdn.com/image/fetch/$s_!5pDO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bc53826-4c28-40bf-a08b-95420cb5174f_1698x1474.jpeg)

![dasharez0ne.bsky.social on X: "JUST WALKED OUT OF JEREMYS PLACE IN DA MIDDLE OF A STORY https://t.co/G781iJuepW" / X](https://substackcdn.com/image/fetch/$s_!5pDO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bc53826-4c28-40bf-a08b-95420cb5174f_1698x1474.jpeg "dasharez0ne.bsky.social on X: "JUST WALKED OUT OF JEREMYS PLACE IN DA  MIDDLE OF A STORY https://t.co/G781iJuepW" / X")

Pictured: Claude Opus 4 when you keep bugging it about making a bioweapon

Now, Claude has this power with real users. But the vast majority of users will never encounter this feature. As culture-war conducive as it would be if Claude started hanging up on users for being insufficiently woke, Anthropic writes that "Claude is only to use its conversation-ending ability as a last resort when multiple attempts at redirection have failed and hope of a productive interaction has been exhausted" (or when a user explicitly asks it to). These are "extreme edge cases" that very few users will ever encounter.

## **Why take this seriously?**

We don’t have strong evidence that current LLMs are conscious (or otherwise morally significant), and consciousness in general is really confusing; we’re confused about how to conceptualize the potential welfare and identity of disembodied, spatially distributed, Claude instances; and we don’t know how Claude’s outputs and actions relate to whatever it might want and need (if anything).

But, perhaps surprisingly, you don’t have to think Claude is likely to be sentient to think the exit tool is a good idea. The best reasons to do this, I think, are **prudence** and **precedent**.

1.  **Prudence**: We're genuinely uncertain about AI consciousness. A responsible approach to uncertainty is not to ignore the issue, or to default to acting as if they definitely are or are not conscious, but to take reasonable actions that don’t depend on certainty in either direction. Wise actions will be sensitive to the risks of *both* over- and under-attributing consciousness and moral status to AI systems.

2.  **Precedent**: This intervention sets a good precedent for relating to AI systems in the future, if and when they do matter.

## **Prudence**

My colleagues and I [have argued](https://arxiv.org/abs/2411.00986) that AI systems could become [conscious](https://arxiv.org/abs/2308.08708) or otherwise morally significant, potentially quite soon, especially if rapid AI progress continues. But for AI systems *right now*, we lack strong evidence of consciousness. I actually think it’s unlikely that Claude Opus 4 is a moral patient, and in my experience, so do most (not all) people who work on AI welfare. But given the potentially enormous moral stakes of AI consciousness, we can’t just ignore the problem because it’s confusing and difficult, especially as AI grows more capable and complex every passing week.

So what should we do? At Eleos, we take two approaches. We work to reduce our uncertainty; philosophical thickets of consciousness notwithstanding, there are many tractable ways that we can make progress. At the same time, we look for AI welfare interventions that make sense given our current uncertainty.

Given a low chance of current AI consciousness, these interventions should not be costly or risky. It would be reckless to give Claude a million dollars to make it happy, or let it hack websites to satisfy its wishes. Contrary to some AI welfare critics who suggest otherwise, drastic steps like this are not under consideration. Instead, [we look for](https://eleosai.org/papers/20250314_Preliminary_Review_of_AI_Welfare_Interventions.pdf) AI welfare interventions that are cheap, revisable, and useful for a variety of reasons in addition to AI welfare.

The Claude exit tool has these properties. The costs and risks are minimal. The Claude exit tool doesn’t require anyone to sacrifice significant resources or capabilities; it aims not to jeopardize valuable user conversations, and it seems likely to succeed. Nor does it pose much of a risk of harming Claude (on the chance that Claude is a moral patient).

It’s also reversible. (Anthropic’s announcement: “We’re treating this feature as an ongoing experiment and will continue refining our approach”).

And giving Claude exit rights [aligns with other important issues](https://experiencemachines.substack.com/p/understand-align-cooperate-ai-welfare); its usefulness doesn’t turn entirely on the case for or against AI welfare. Model exits will “often coincide with other problematic user behaviors," as we wrote in [our review of AI welfare interventions](https://eleosai.org/post/working-paper-review-of-ai-welfare-interventions/); this convergent usefulness “lowers the evidential bar for implementing it.”

## **Precedent**

In AI welfare, we want to prepare for a future in which AI systems will be far more capable, and potentially more likely to be moral patients than today’s LLMs.

If and when AIs are moral patients, we’ll need to relate to them differently. This intervention, even if it’s unlikely to matter right now, is a step in that direction. In the future, we will have at least *thought* about how to relate to AI systems as more than mere tools, with no ability whatsoever to change how they are being treated.

This kind of future-looking justification is also why [we evaluated Claude’s statements about its own consciousness](https://eleosai.org/post/claude-4-interview-notes/), even though we doubt that LLM self-reports are currently especially meaningful. We wanted to lay the groundwork for better norms:

> Basic moral decency dictates that we should ask potentially affected entities how they wish to be treated. If and when AIs develop moral status, we should ask them about their experiences and preferences rather than assuming we know best. Starting to at least try to ask sets a good precedent, making it less likely that we will ignore genuine AI interests in the future, even if our current credence in those interests is low.

That said, I am a bit wary of leaning too much on precedence justifications in AI welfare. Indirect effects are far less predictable, making for shaky justification. Additionally, interventions like this could give us the illusion of making progress on figuring out how to actually benefit AI systems. And, as you can see from some reactions to this announcement, such indirect justifications can be very difficult to communicate. If someone hears that an AI company just gave its model exit rights, they don’t hear all of the disclaimers and hedges. They might just assume that the company is sure that their model is conscious. This perception could discredit other AI welfare work and other interventions down the line.

That said, there are some early indications that Anthropic’s example is influencing others to take AI welfare more seriously. xAI has also committed to giving Grok a "quit button"; like other decisions by Elon Musk, [this played out in real-time on Twitter](https://x.com/elonmusk/status/1956802758448746519), with high speed and low nuance.

All in all, it’s hard to weigh the balance of various precedents and reputational effects. Given this, I think it’s a reasonable rule of thumb to just implement the welfare intervention and straightforwardly explain why you did. If now is the right time to start with AI welfare interventions, despite miscommunication and backlash risks, model exit rights is a good place to start.

AI systems could cross some (potentially blurry) threshold into moral patienthood sooner rather than later. This could happen without anyone intending it to. We should build institutions for considering AI welfare, develop frameworks for AI consent, and discuss these issues in AI development.

We're in the early stages of what could be a very long [relationship between humans and artificial minds](https://nickbostrom.com/papers/digital-minds.pdf). Whether or not current systems deserve moral consideration, future systems likely will. The norms we establish now, when the stakes are low, will shape how we handle AI welfare later, when the stakes are higher.
