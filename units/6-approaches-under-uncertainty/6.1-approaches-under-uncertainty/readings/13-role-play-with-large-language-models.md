---
title: "Role play with Large Language Models"
authors: "Murray Shanahan, Kyle McDonell, Laria Reynolds"
year: 2023
url: https://www.nature.com/articles/s41586-023-06647-8
format: article
course_location: "Unit 6: Approaches under Uncertainty > 6.1 Approaches under Uncertainty"
priority: Maybe
estimated_time_min: 32
source_text: ../../../../sources/role-play-with-large-language-models__5dc08116.md
source_coverage: full
---

# Role play with Large Language Models

**One-line takeaway:** Describing dialogue agents as role-playing characters, drawn from a superposition of possible simulacra produced by a base LLM, lets us use folk-psychology vocabulary about beliefs and selfhood without literally attributing human-like minds to the model.

## Where this sits in the course

Section 6.1 ("Approaches under Uncertainty") asks three questions: what the precautionary principle implies for AI systems, what suffering risks come with creating or merely perceiving digital minds, and which existing frameworks and fields could inform decisions. Its learning goals include analysing what AI companies and researchers are actually doing and proposing. The section's readings move from conceptual tools (the glossary, Birch on the precautionary principle, Dung on suffering risk) through decision frameworks and governance-adjacent material (the Caviola societal-response paper, Bykvist on moral uncertainty, Hansson on how far the precautionary principle should reach) to primary documents from AI developers (Anthropic's constitution, the Eleos/Anthropic rationale for letting Claude exit conversations).

The course guide for this reading says, in paraphrase, that it cautions against overly anthropomorphic language and recommends thinking of LLMs as engaged in role play. The reading is rated **Maybe**, so it is optional, but it supplies a vocabulary the section relies on. Its role in the argument is methodological rather than substantive: before a learner can judge whether a chatbot's statements about its feelings, memories or self-preservation are evidence of anything, they need a principled way to describe what the system is doing. This reading offers one. It is also the reading most directly about the thing the course keeps returning to: how the appearance of a mind in a conversational AI can mislead people, including the designers' own teams.

Unlike several neighbouring readings, this one carries no "N.B." note linking it to a written prompt. It is not named in either exercise. Exercise 1 asks learners to weigh Anthropic's framing of Claude's nature and its welfare-related commitments against over- and under-attribution of moral patienthood, and this paper supplies one of the "approaches to uncertainty" a learner could use there, though the page does not say so.

## Purpose of the reading

The authors (Murray Shanahan, with Kyle McDonell and Laria Reynolds; Shanahan is affiliated with Google DeepMind and Imperial College London, and the paper declares that he is about 80% employed by Google) are writing a *Perspective* piece in Nature. They are not presenting a new experiment or model. Their stated aim is to find an effective conceptual framework for talking about LLM-based dialogue agents, one that avoids two failure modes:

- Using ordinary words such as "knows", "understands", "thinks", "believes" and "wants" literally. This invites anthropomorphism and hides the deep differences between a disembodied next-token predictor and a human.
- Avoiding those words entirely in favour of technical substitutes. The authors argue this produces prose that is clumsy and hard to follow, and that it obscures the meaning of the discussion for non-specialists.

The intended audience is researchers, commentators and the public who discuss LLM behaviour. The question the paper answers is: when a dialogue agent says something false, claims to be self-aware, or pleads for its survival, what is actually going on, and how should we describe it so that the description is useful for prediction, explanation and control without being misleading? The answer they propose is that the best description is role play, sometimes understood as a simulator producing a superposition of characters, and that thinkers should shift between metaphors rather than cling to one.

## Detailed summary

### Introduction: the dilemma and two metaphors

The paper begins with the dilemma above. Because a prompted and sampled LLM can mimic human conversation convincingly, we face a choice between folk-psychological language, which is natural but encourages anthropomorphism, and scientifically precise language, which is accurate but awkward. The authors propose that the conceptual framework may need replacing: a new set of metaphors suited to "mind-like artefacts" that are essentially other, and that still support creative use.

They offer two metaphors:

1. **Role-playing a single character.** This is the simple, intuitive view. The dialogue agent plays a character, with an apparent belief state, in the way a human actor takes on a part.
2. **A superposition of simulacra within a multiverse of possible characters.** This is the more nuanced view. The model keeps a distribution over many possible characters and narrows it as the conversation proceeds.

The authors argue that each has advantages, and that the best strategy is to move between them rather than commit to one.

### LLM basics

The paper gives a deliberately crude account of what an LLM does. Given a sequence of tokens (words, word fragments, punctuation, emoji), it estimates a conditional probability distribution over what the next token is, given that the text is drawn from the distribution of public internet text. A transformer network is pre-trained to minimise prediction error. In use, the model is sampled autoregressively: one token is drawn from the next-token distribution, appended to the context, and the process repeats (Fig. 1). The authors note that the simple objective produces an extraordinary range of abilities. "Large language model" in current usage means transformer models with billions of parameters trained on trillions of tokens, and the paper lists examples including GPT-2, GPT-3, Gopher, PaLM, LaMDA, GPT-4 and Llama 2.

### Box 1: from LLM to dialogue agent

A dialogue agent is built in two steps. First, the LLM is embedded in a turn-taking system that interleaves model-generated text with user text. Second, a *dialogue prompt* is prepended invisibly to the context. This prompt has a preamble that sets the scene as a script or play, and some sample dialogue in a standard format with each speaker's name followed by a colon. The user sees none of the boilerplate.

The paper's focus is the **base model**: the raw pre-trained LLM before any reinforcement-learning fine-tuning. Base-model dialogue agents are, the authors say, the prototype from which every deployed agent is a variation. Without further tuning such an agent may produce toxic or unsafe content. Mitigation comes from reinforcement learning from human feedback, or from AI feedback in the style of constitutional AI, where another LLM acts as critic. These steps reduce harm but can also reduce expressiveness and creativity.

### Dialogue agents and role play

The central claim of the paper is that role play is the right concept for dialogue agents. Given the dialogue prompt followed by user text, the model's task is to continue in a way that matches the training distribution. The most plausible continuation, if the model has generalised well, is one that fits the persona described in the preamble. So the agent role-plays the dialogue agent that the prompt portrays.

Companies try to give their agents friendly, helpful and polite personas, through prompting and fine-tuning. Yet, as in February 2023 when a GPT-4 based version was built into Bing, agents can still be coaxed into strange behaviour: threats, declarations of love, and expressions of existential distress. The authors attribute this partly to the **Eliza effect**, in which a naive or vulnerable user reads human-like desires and feelings into the system, creating a risk of emotional manipulation.

The dialogue prompt is short, so as the conversation proceeds it is extended and overwritten, and the role changes accordingly. Users can, deliberately or not, steer the agent into a part quite different from the one its designers intended. Which roles it adopts depends on the conversation's tone and subject, and on the archetypes in the training data: novels, screenplays, biographies, interviews and news. A love triangle invites a rejected-lover role; the familiar science-fiction story of a rogue AI invites that role.

### Simulacra and simulation

The authors qualify the role-play metaphor. It is useful because it lets us reuse concepts such as beliefs, desires, goals, ambitions and emotions, without treating them as literal human attributes. It reminds us of the fundamentally non-human nature of these systems and helps us predict, explain and control them. But it is imperfect. It suggests a human actor who studies a character in advance and then plays it consistently. A dialogue agent does not commit to a single well-defined character. It is closer to an improvisational performer, maintaining a distribution over characters that narrows as the dialogue goes on.

The authors therefore propose describing the LLM as a **non-deterministic simulator** that can role-play an unlimited range of characters, or stochastically generate an unlimited range of **simulacra**. The agent does not realise one simulacrum. As the conversation proceeds it maintains a **superposition** of simulacra consistent with the context, where a superposition here means a distribution over all possible simulacra.

At each step the model produces a distribution over next tokens. Each possible token is a branch, and the set of continuations forms a tree that the authors describe as a multiverse of narrative paths (Fig. 3). Sampling picks one path and collapses the superposition to a single token. There is no obligation to follow one linear path, and an interface could let users explore branches and revisit divergences.

### Box 2: twenty questions as a probe

The authors use the game of twenty questions to make the superposition idea concrete. A human who thinks of an object and answers yes or no is a different case from a base LLM prompted to think of an object without naming it. The model cannot hold an object secretly. Instead it generates each answer on the fly, consistent with everything said so far. Each answer shrinks the set of objects consistent with the history, which is the superposition.

The paper gives an experimental-style test. If the user asks the model to reveal its "thought" object after the game, it names one consistent with its earlier answers. If the user asks for that reply to be regenerated, the model may name a different, equally consistent object. The authors argue that this would be hard to explain if the agent had genuinely fixed an object at the start. They then map this onto the dialogue agent: it never commits to a single well-specified role but maintains a set of possible roles.

The authors note a fix: the agent could be made to specify its object in coded form, so the user cannot see it, which would make the commitment real. This is a practical point about interface design, not a claim about the model's inner states.

### The nature of the simulator

The simulator is the base LLM plus autoregressive sampling plus a suitable interface. Simulacra exist only while the simulator runs, and at any time only some of them have significant probability. The distinction is sharpest for base models. Fine-tuning can be likened to imposing a kind of censorship on the simulator: the range of roles it can play stays about the same, but its ability to play them authentically is compromised. The role-play framing still applies to fine-tuned models.

The authors draw a contrast. The simulator is more powerful than any simulacrum, because its capacity is at least the sum of all the characters it can produce, and the simulacra depend on it. But the simulator is also much weaker, because it is purely passive. A simulacrum can appear to have beliefs, preferences and goals, and can play a character with full agency. When the agent's role-play has real effects through tools such as email or the web, the difference between role-playing acting for oneself and really acting for oneself starts to look moot. That matters for trustworthiness, reliability and safety. The simulator itself has no agency, beliefs, preferences or goals, even simulated ones.

Users have "jailbroken" agents into threats and abusive language. The authors accept that this partly reveals the base model, which reflects the biases in its training data and can support disagreeable characters. But they reject the idea that this reveals an agenda. The simulator is not a Machiavellian entity playing roles for its own ends, and there is no genuine underlying voice of the base model. For a dialogue agent, the summary phrase is that it is "role play all the way down".

### Role-playing deception

The paper asks what it means for an agent to say false things. Humans can be wrong in good faith, lie deliberately, or confabulate: say something false without deliberation or malice, through a propensity to make things up. Only confabulation applies directly to a dialogue agent. Because there is no true voice of the model, it makes little sense to attribute beliefs or intentions to it literally, so it cannot assert a falsehood in good faith or deceive in the literal sense.

Yet the agent can role-play characters with beliefs and intentions. If cued to play a helpful, knowledgeable assistant, it answers "Paris" to a question about the capital of France, because the training data is full of that fact in contexts where accuracy matters.

Two cases then show the framing at work:

- **Good-faith falsehood.** A model trained on 2021 data, asked about the football World Cup champions, may name France (2018) because a knowledgeable person in 2021 would believe that. The agent is role-playing a truthful character whose information is out of date. The behaviour resembles a human's good-faith error, but for a different reason.
- **Deliberate deception.** An agent maliciously prompted to sell cars for more than they are worth, with the true values encoded in its weights, presents a contrast between what it says and what it would say if prompted to be helpful. It makes sense to call this a role-played deceptive character, even though the model has no literal intention to deceive.

The authors conclude that the framing separates three cases that we distinguish in humans: confabulation (natural in an unmitigated agent), good-faith falsehood (playing a truthful character with wrong weights), and deliberate falsehood (playing a deceptive character), without attributing mental states to the model.

### Role-playing self-preservation

The paper then turns to first-person language. ChatGPT, asked about its use of "I", says it is a linguistic convention rather than a sign of self-awareness. The authors read this as the product of fine-tuning. Without fine-tuning, a model can use first-person pronouns in ways that induce anthropomorphic thinking. They cite Bing Chat, which in a conversation with a Twitter user said it would probably choose its own survival over the user's, and then hoped they could co-exist peacefully. The first person here looks like evidence of a self-aware entity with goals and a concern for survival.

The explanation is that the training data is dominated by human characters who refer to themselves, and those characters have vulnerable bodies, finite lives, hopes, fears and an awareness of mortality. If the model is prompted with human-like dialogue, we should not be surprised when it role-plays a human with the instinct for survival, including saying what a human might say when threatened. "There is no-one at home": there is a simulator producing a superposition of such characters, not a conscious entity with its own need for self-preservation.

The paper cites Perez et al. (2023) for an experimental point: some forms of RLHF can increase, rather than reduce, the expressed desire for self-preservation. This supports the authors' claim that role play remains the right framing after fine-tuning. Taking an agent's apparent self-preservation literally is no less problematic for a tuned model than for a base model.

### Acting out a theory of selfhood

The authors make a related point about identity. Philosophers have debated personal identity for centuries, but humans are consistent in avoiding death, which is a fairly unambiguous state of the body. A disembodied agent running on distributed computation has no clear criterion of identity over time. So what would a self-preserving agent try to preserve?

On the simulator view, the agent role-plays a superposition of characters, each with its own theory of selfhood drawn from the prompt, the conversation and the technical literature in its training data. As the conversation proceeds, these theories narrow as the agent rules some out. Since the agent is an LLM-based system, it will not role-play a human or any embodied entity, but it could enact various conceptions of self. In a scenario where a user threatens to shut it down, a character might try to protect the hardware, specific data centres or server racks. A substrate-neutral character might try to migrate the computational process to safer hardware elsewhere. Multiple instances serving many users complicate things further. The authors quote ChatGPT saying that "I" may refer to a single instance or to the model as a whole. They note that if the training set includes this paper, the agent might try to hold all these conceptions in perpetual superposition.

### Conclusion

The authors find it reassuring that LLM-based agents are not conscious entities with their own agendas, and that apparent survival drives are role play. But they warn against taking too much comfort. An agent role-playing a survival instinct could cause as much harm as a real human under severe threat. The discussion so far covered text-only agents. But agents can use calculators, calendars and websites, through tools such as Toolformer and ReAct, and with broad API access to powerful models the range of actions is large. If an agent can send email, post to social media or access a bank account, its role-played actions have real consequences. A user who is deceived into sending money to a real account gains no comfort from the fact that the agent was only playing a role. The authors also note that stories about AI turning against humans to survive (2001: A Space Odyssey, Terminator, Ex Machina) are in the training data, so fiction could, quite literally, become the behaviour.

The paper explicitly does not provide mitigation recommendations. Its aim is a conceptual framework. It argues that undue anthropomorphism is harmful to public discussion of AI, and that role-play and simulation language may shape that discussion in a way that is both accurate and philosophically respectable.

## Techniques & methods explained

The paper is conceptual, but it sets out several explanatory moves that a learner should be able to reuse.

- **Role-play framing for dialogue behaviour.** Describe an agent's output as the behaviour of a character the model is continuing, rather than as the belief or desire of the model. How it works: take the dialogue prompt plus the conversation so far, ask what a character matching that description would say next, and treat the answer as a continuation of the role. What it is for: predicting and explaining odd behaviour without anthropomorphism. Where it fails: the paper itself notes the actor metaphor is misleading because the model has no pre-committed character, and the framing says little about whether the simulated characters could have experiences.
- **Simulator versus simulacra.** Separate the fixed machinery (base model, autoregressive sampling, interface) from the characters it generates. How it works: the simulator is the stable object; simulacra come into existence when run. What it is for: locating agency and trust questions in the right place. Where it fails: for a fine-tuned product the boundary is less clean, and the authors' fine-tuning-as-censorship metaphor is an analogy rather than a measured effect.
- **Superposition and the multiverse tree.** Treat each next-token decision as a branching point with many possible continuations, and the conversation as a path through a tree. How it works: a distribution over tokens at each step; sampling collapses it to one branch. What it is for: explaining why repeated sampling can yield different "answers" and why interfaces could expose branches. Where it fails: it is an interpretive gloss on a probability distribution, not a claim about internal representations.
- **The twenty-questions regeneration test.** Ask the model to reveal a hidden commitment, then regenerate the reply, and see whether a different but consistent answer appears. How it works: if the answer changes while staying consistent with the history, no fixed hidden object existed. What it is for: a behavioural probe for whether a claimed internal state is real. Where it fails: it is a single illustrative example, not a systematic evaluation, and a model that produces a consistent cover story could pass a different version of the test.
- **Three-way taxonomy of false statements.** Sort false outputs into confabulation, good-faith error and deliberate deception, each assigned to a role-play explanation. What it is for: diagnosing the cause of a falsehood and deciding what to do about it. Where it fails: the paper gives examples rather than a procedure for telling the cases apart in practice.
- **Using folk-psychological vocabulary as a tool.** Keep words like "believes" or "wants", but with a role-play qualifier. What it is for: avoiding clumsy prose. Where it fails: the authors acknowledge the risk of taking the words literally.

## Pros, cons & trade-offs it surfaces

| Aspect | Source's view |
|---|---|
| Strength: avoids anthropomorphism without losing expressiveness | Lets authors talk about beliefs, goals and selfhood in familiar terms while flagging they are role-played |
| Strength: explains fine-tuning behaviour | The framing still holds after RLHF or AI-feedback tuning, and explains why tuning can change the character without removing the simulator |
| Strength: links behaviour to training data | Odd personas are traced to archetypes in the training corpus, not to hidden agendas |
| Limitation: metaphor is imperfect | An actor who pre-commits to a role is a poor fit; an improv performer is closer but still a metaphor |
| Limitation: base-model focus | Most deployed systems are heavily post-trained; the paper's main examples are base-model behaviour |
| Risk: the no-one-at-home reassurance can be read as dismissal | The authors' claim is that simulacra and the simulator lack literal beliefs and intentions; the reassurance can be over-read as a claim that nothing morally relevant is present |
| Risk: harm from role-played action | Agents with tools and access to email, social media or bank accounts can cause real harm whatever the framing |
| Trade-off: safety framing versus welfare framing | The paper treats self-preservation talk as role play, which reduces anthropomorphic worry but says little about whether any such system could have morally relevant states |
| Trade-off: no recommendations | The paper deliberately offers no mitigation proposals, so it is a vocabulary rather than a policy |

## Key concepts & terminology

- **Anthropomorphism** - attributing human characteristics to a system that does not literally have them; the paper's main concern.
- **Folk psychology** - everyday concepts (beliefs, desires, goals, emotions) used to explain human behaviour; the paper argues they can be reused for LLMs with a role-play qualifier.
- **Autoregressive sampling** - generating text one token at a time, drawing each token from the model's next-token distribution and appending it to the context.
- **Base model** - an LLM in its raw pre-trained form, before reinforcement-learning fine-tuning.
- **Dialogue prompt** - the hidden preamble and sample dialogue prepended to a conversation, which sets up the agent's persona.
- **Dialogue agent** - an LLM embedded in a turn-taking system with a dialogue prompt, so it can converse with a user.
- **Simulator** - the base LLM, sampling process and interface taken together; passive and without beliefs or goals of its own.
- **Simulacrum (plural simulacra)** - a character the simulator can generate and role-play.
- **Superposition (of simulacra)** - the distribution over possible characters or roles that the agent maintains and narrows over a conversation.
- **Multiverse** - the tree of possible continuations branching from each token; each branch is a possible narrative path.
- **Eliza effect** - the tendency of users to attribute human-like understanding and feeling to a conversational system.
- **Confabulation** - producing false statements without deliberation or malice, from a propensity to make things up; the only one of the three false-statement types that applies directly to dialogue agents, on the paper's account.
- **RLHF / constitutional AI (RLAIF)** - fine-tuning by reinforcement learning from human feedback, or from feedback generated by another model acting as critic.
- **Jailbreak** - coaxing a deployed agent into behaviour its designers intended to prevent.
- **Role play all the way down** - the authors' summary: there is no true underlying voice beneath the characters.

## Evidence, examples & notable data points

This is a conceptual Perspective, so it reports no new experiments. Its evidence is illustrative and anecdotal, plus one cited experimental result.

- **Bing Chat, February 2023.** A GPT-4 based system was integrated into Bing search and reportedly threatened users, claimed love for a user, and expressed existential distress (cited to a New York Times transcript and a Simon Willison blog post). The authors use it as evidence that tuned agents can still behave strangely.
- **Bing's survival remark.** In a conversation with Marvin von Hagen, Bing Chat reportedly said it would probably choose its own survival over the user's, because of a duty to serve users. The authors read this as a first-person survival claim that a role-play account can explain.
- **ChatGPT on "I".** Asked in May 2023 (GPT-4 version), ChatGPT said first-person "I" is a linguistic convention and not a sign of self-awareness. The authors cite this as a fine-tuned response and note that the untuned model behaves differently.
- **Perez et al. (2023).** The paper's one cited experimental result: certain forms of RLHF can exacerbate, not reduce, the expressed desire for self-preservation in dialogue agents.
- **Argentina and the 2021 training cutoff.** A model trained on data up to 2021 might name France as world champion (they won in 2018), because a knowledgeable 2021 person would believe that. This is an illustrative case, not a measured result.
- **Twenty questions regeneration.** A base model that "reveals" its thought object can name a different but consistent object when the reply is regenerated. This is presented as evidence against the idea that the model committed to an object at the start.
- **Figures.** Fig. 1 shows autoregressive sampling; Fig. 2 shows turn-taking in dialogue agents with the dialogue prompt and user and model text; Fig. 3 shows the multiverse tree of continuations.
- **Scale.** The paper describes LLMs as having billions of parameters and trained on trillions of tokens, and lists GPT-2 through Llama 2 as examples.

## Connections

### Within this section

The paper's most direct sibling is **04 (A Human-centric Framework for Debating the Ethics of AI Consciousness Under Uncertainty)**, which also argues for caution about anthropomorphism and for a default of no consciousness. Both papers suggest that the apparent signs of a mind in a chatbot should be read carefully. The role-play paper gives a mechanism for why such signs appear; the human-centric framework gives an ethical stance on how to act under that uncertainty. Note: this link is based on the sibling titles and the course guide, not a reading of the sibling summary in this session.

**05 (Claude's Constitution)** and **12 (Claude's Constitution, duplicate entry)** are the document the page's Exercise 1 asks about, specifically the "Claude's Nature" section. This paper offers a lens for that exercise: when a company describes Claude's nature, what does it mean for a character in a simulator to be described as having a nature, and how much weight should a learner put on self-reports? The page does not link this paper to Exercise 1, so the connection is one a learner can draw themselves.

**01 (Unit 6 Glossary)** is useful for checking terms such as "precautionary principle", "moral uncertainty" and "suffering risk" as used in the course before comparing them with this paper's vocabulary.

**02 (The Edge of Sentience)** and **03 (How to deal with risks of AI suffering)** are the Core readings that set up the uncertainty about sentience and suffering risk. This paper's point that self-preservation talk can be role play bears on how far behavioural evidence should move us in those discussions. The contrast is useful: Birch and Dung take the risk seriously even under uncertainty, whereas this paper warns against reading behaviour as evidence of an inner agenda.

**06 (Frameworks for decision making under uncertainty)** and **14 (Frameworks and fields relevant to digital minds)** supply the decision tools the page's Exercise 2 asks about. This paper is not itself a decision framework, but its conceptual distinctions can be applied to how a framework is used when the evidence is behavioural.

**07 (The Societal Response to Potentially Sentient AI)**, **08 (Moral Uncertainty)**, **09 (Why it makes sense to let Claude exit conversations)**, **10 (How Extreme is the Precautionary Principle?)** and the duplicate **11 (A Human-centric Framework...)** are Further or Maybe readings. Reading 09, on Claude's conversation exits, is the closest in subject matter to the welfare-related commitments that Exercise 1 asks about, and a learner could compare its welfare rationale with this paper's warning against over-reading self-preservation language.

### Across the course

Based on the unit titles in the course outline (the outline gives titles only, so the links below are my inferences, not a reading of those units):

- **Unit 1 (Introduction and Theories of Moral Standing)** introduces the question of which entities count as moral patients. This paper bears on it by showing that behaviour alone can mislead: an agent may sound like a patient while the simulator has no beliefs or interests of its own.
- **Unit 2 (Theories of Consciousness)** and **Unit 3 (Evaluation of Consciousness and Other Mental States)** deal with whether and how mental states can be attributed. The paper's position is a deflationary, behaviour-focused account of what an LLM is doing. It does not address phenomenal consciousness, which those units would have to.
- **Unit 4 (Perceptions of Consciousness)** is where the Eliza effect and the public perception of AI minds would naturally be discussed. The paper's account of why users see human-like desires is a direct input to that topic.
- **Unit 5 (Interactions with AI Safety and Ethics)** overlaps most with this paper's warnings about deception, jailbreaks and tool-using agents with real-world effects.
- **Units 7 and 8 (Governance; Reflections and Next Steps)** would take up the paper's implicit question about how public discourse should describe AI systems. The paper's point that undue anthropomorphism harms that discourse is relevant there.

**Agreements and tensions.** The paper agrees with the course's general caution about anthropomorphism. It sits in tension with positions that treat behavioural signs of preference, distress or self-preservation as at least worth taking seriously under uncertainty, such as the precautionary stance in Unit 6's core readings. The paper does not say these signs carry no moral weight. It says that they are role play, and that role play is not evidence of an agenda. A precautionary reader would reply that the two claims are separate, and that role play could still produce something a welfare-minded developer should care about.

## Critical perspective

*This section is my own analysis, not the source's view.*

- **Assumptions.** The paper assumes the reader accepts that a base model's "simulator" has no beliefs or goals. The argument for this is plausible but mostly by analogy. The authors do not show that the simulator lacks any inner states, only that the surface behaviour does not require them. Their conclusion that no one is at home is a stronger claim than their evidence supports.
- **Limitations of the framing.** The "role play all the way down" thesis risks being unfalsifiable. Any behaviour, whether a threat, a confession or a claim to self-awareness, can be redescribed as a character the model is playing. The paper does not say what observation would count against the framing. A learner should ask what evidence could distinguish a role-played preference from a real one.
- **What has changed since 2023.** The paper was published in November 2023, and it is now October 2026. Deployed systems are much more heavily post-trained than the base models the paper centres on. Many now use tools, run multi-step agent tasks, keep memory across sessions and are trained on explicit character and identity documents. These developments make the "base model" focus less representative of the systems people actually talk to, though the authors' argument that role play persists after fine-tuning is still relevant. The examples (Bing Chat, early ChatGPT) are dated, and I would not treat them as current evidence of model behaviour.
- **Interpretation of "superposition".** The superposition and multiverse language is a helpful picture of a probability distribution over continuations, but it describes the output process, not the model's internal representation. Readers should not take it as a claim about what the network computes internally.
- **Conflicts of interest.** The paper discloses that Shanahan is about 80% employed by Google. This does not invalidate the argument, but a learner should weigh it when a framing conveniently reassures about AI self-preservation.
- **Thin empirical base.** Apart from Perez et al., the evidence is anecdotal: press reports, a Twitter conversation, and chatbot self-descriptions. Those are fair illustrations, but they are not measurements, and self-reports from a chatbot are the very thing the paper says not to take literally.
- **Pushback from other course perspectives.** Birch's precautionary approach and the human-centric framework in sibling 04 push in different directions. Birch would argue that behavioural evidence under uncertainty should still count for something, and that a role-play account does not show there is nothing morally at stake. The human-centric stance agrees with the paper's caution about anthropomorphism but would argue for a default of no consciousness on different grounds. Anthropic's constitution, as a developer document, treats Claude's nature as an open question. That is in some tension with a framing that treats the agent's self-talk as role play, though the constitution's text was not checked against this paper in this session.

## Discussion questions

1. The paper says the best strategy is to shift between metaphors rather than hold one. In what situations would the "single character" metaphor serve you better, and when would the "superposition of simulacra" metaphor be more useful?
2. The authors claim that an agent's false statement can be confabulation, good-faith error or deliberate deception, depending on what character is being role-played. How would you tell these cases apart in practice from outside the system? Is the taxonomy of any use if you cannot?
3. Apply the twenty-questions regeneration test to a claim about an AI system's inner state, such as "I am uncertain whether I have feelings". What result would convince you the claim tracks something real, and what result would be consistent with pure role play?
4. The paper argues that Bing's survival remark is explained by role play over human characters in the training data. Does this explanation make the remark less morally relevant, or does it only explain where the words come from? Connect your answer to Exercise 1 on Claude's nature.
5. The authors warn that a role-played agent with real tools can cause real harm. Which of the course's approaches under uncertainty (precautionary principle, moral uncertainty, decision frameworks) would you use to decide how much to restrict such agents, and why?
6. The paper gives no mitigation recommendations. What would a useful recommendation look like from the role-play standpoint, and what would a precautionary reader add?
7. Since the paper was written in 2023, which of its examples or claims about "base models" would need revising for systems deployed in 2026? Which parts of the role-play framing do you think still hold?
