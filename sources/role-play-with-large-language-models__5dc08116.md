<!-- source: https://www.nature.com/articles/s41586-023-06647-8 -->

# Role play with large language models | Nature

[Download PDF](/articles/s41586-023-06647-8.pdf)

- Perspective
- Published: 08 November 2023

# Role play with large language models

- [Murray Shanahan](#auth-Murray-Shanahan-Aff1-Aff2)  [ORCID: orcid.org/0000-0001-5984-2964](https://orcid.org/0000-0001-5984-2964)^([1](#Aff1),[2](#Aff2)),
- [Kyle McDonell](#auth-Kyle-McDonell-Aff3)^([3](#Aff3)) &
- [Laria Reynolds](#auth-Laria-Reynolds-Aff3)^([3](#Aff3)) 

[*Nature*](/) **volume 623**, pages 493–498 (2023) [Cite this article](#citeas)

[Save article](/articles/s41586-023-06647-8/save-research?_csrf=t3JTJgWZGm3g9PZJqn4EugFFH9nkCyNb)

[View saved research](/saved-research)

- 138k Accesses

- 586 Citations

- 558 Altmetric

- [Metrics details](/articles/s41586-023-06647-8/metrics)

## Abstract

As dialogue agents become increasingly human-like in their performance, we must develop effective ways to describe their behaviour in high-level terms without falling into the trap of anthropomorphism. Here we foreground the concept of role play. Casting dialogue-agent behaviour in terms of role play allows us to draw on familiar folk psychological terms, without ascribing human characteristics to language models that they in fact lack. Two important cases of dialogue-agent behaviour are addressed this way, namely, (apparent) deception and (apparent) self-awareness.

### Similar content being viewed by others

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs41598-025-98378-1/MediaObjects/41598_2025_98378_Fig1_HTML.png)

### [Testing the limits of large language models in debating humans](https://www.nature.com/articles/s41598-025-98378-1?fromPaywallRec=false)

Article Open access 22 April 2025

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs44260-026-00075-1/MediaObjects/44260_2026_75_Fig1_HTML.png)

### [Too human to model: the uncanny valley of large language models in simulating human systems](https://www.nature.com/articles/s44260-026-00075-1?fromPaywallRec=false)

Article Open access 02 March 2026

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs41597-025-04836-w/MediaObjects/41597_2025_4836_Fig1_HTML.png)

### [Bilingual Dialogue Dataset with Personality and Emotion Annotations for Personality Recognition in Education](https://www.nature.com/articles/s41597-025-04836-w?fromPaywallRec=false)

Article Open access 27 March 2025

### Explore related subjects

Discover the latest articles and news in related subjects.

- [Computer science](/subjects/computer-science)
- [Philosophy](/subjects/philosophy)
- [Human-Robot Interaction in Assistive Technologies](/subjects/human-robot-interaction-in-assistive-technologies)

## Main

Large language models (LLMs) have numerous use cases, and can be prompted to exhibit a wide variety of behaviours, including dialogue. This can produce a compelling sense of being in the presence of a human-like interlocutor. However, LLM-based dialogue agents are, in multiple respects, very different from human beings. A human’s language skills are an extension of the cognitive capacities they develop through embodied interaction with the world, and are acquired by growing up in a community of other language users who also inhabit that world. An LLM, by contrast, is a disembodied neural network that has been trained on a large corpus of human-generated text with the objective of predicting the next word (token) given a sequence of words (tokens) as context^([1](/articles/s41586-023-06647-8#ref-CR1 "Shanahan, M. Talking about large language models. Preprint at 
                  https://arxiv.org/abs/2212.03551
                  
                 (2023). This paper cautions against the use of anthropomorphic terms to describe the behaviour of large language models.")).

Despite these fundamental dissimilarities, a suitably prompted and sampled LLM can be embedded in a turn-taking dialogue system and mimic human language use convincingly. This presents us with a difficult dilemma. On the one hand, it is natural to use the same folk psychological language to describe dialogue agents that we use to describe human behaviour, to freely deploy words such as ‘knows’, ‘understands’ and ‘thinks’. Attempting to avoid such phrases by using more scientifically precise substitutes often results in prose that is clumsy and hard to follow. On the other hand, taken too literally, such language promotes anthropomorphism, exaggerating the similarities between these artificial intelligence (AI) systems and humans while obscuring their deep differences^([1](/articles/s41586-023-06647-8#ref-CR1 "Shanahan, M. Talking about large language models. Preprint at 
                  https://arxiv.org/abs/2212.03551
                  
                 (2023). This paper cautions against the use of anthropomorphic terms to describe the behaviour of large language models.")).

If the conceptual framework we use to understand other humans is ill-suited to LLM-based dialogue agents, then perhaps we need an alternative conceptual framework, a new set of metaphors that can productively be applied to these exotic mind-like artefacts, to help us think about them and talk about them in ways that open up their potential for creative application while foregrounding their essential otherness.

Here we advocate two basic metaphors for LLM-based dialogue agents. First, taking a simple and intuitive view, we can see a dialogue agent as role-playing a single character^([2](/articles/s41586-023-06647-8#ref-CR2 "Andreas, J. Language models as agent models. In Findings of the Association for Computational Linguistics: EMNLP 2022 5769–5779 (Association for Computational Linguistics, 2022). This paper hypothesizes that LLMs can be understood as modelling the beliefs, desires and (communicative) intentions of an agent, and presents preliminary evidence for this in the case of GPT-3."),[3](/articles/s41586-023-06647-8#ref-CR3 "Park, J. S. et al. Generative agents: interactive simulacra of human behavior. Preprint at 
                  https://arxiv.org/abs/2304.03442
                  
                 (2023).")). Second, taking a more nuanced view, we can see a dialogue agent as a superposition of simulacra within a multiverse of possible characters^([4](/articles/s41586-023-06647-8#ref-CR4 "Janus. Simulators. LessWrong Online Forum 
                  https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/
                  
                 (2022). This blog post introduced the idea that a large language model maintains a set of simulated characters in superposition.")). Both viewpoints have their advantages, as we shall see, which suggests that the most effective strategy for thinking about such agents is not to cling to a single metaphor, but to shift freely between multiple metaphors.

Adopting this conceptual framework allows us to tackle important topics such as deception and self-awareness in the context of dialogue agents without falling into the conceptual trap of applying those concepts to LLMs in the literal sense in which we apply them to humans.

## LLM basics

Crudely put, the function of an LLM is to answer questions of the following sort. Given a sequence of tokens (that is, words, parts of words, punctuation marks, emojis and so on), what tokens are most likely to come next, assuming that the sequence is drawn from the same distribution as the vast corpus of public text on the Internet? The range of tasks that can be solved by an effective model with this simple objective is extraordinary^([5](/articles/s41586-023-06647-8#ref-CR5 "Wei, J. et al. Emergent abilities of large language models. Trans. Mach. Learn. Res. 
                  https://openreview.net/forum?id=yzkSU5zdwD
                  
                 (2022).")).

More formally, the type of language model of interest here is a conditional probability distribution *P*(*w*_(*n*+1)∣*w*₁ … *w*_(*n*)), where *w*₁ … *w*_(*n*) is a sequence of tokens (the context) and *w*_(*n*+1) is the predicted next token. In contemporary implementations, this distribution is realized in a neural network with a transformer architecture, pre-trained on a corpus of textual data to minimize prediction error^([6](/articles/s41586-023-06647-8#ref-CR6 "Vaswani, A. et al. Attention is all you need. Adv. Neural Inf. Process. Syst. 30, 5998–6008 (2017).")). In application, the resulting generative model is typically sampled autoregressively (Fig. [1](/articles/s41586-023-06647-8#Fig1)).

![Fig. 1: Autoregressive sampling.](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-023-06647-8/MediaObjects/41586_2023_6647_Fig1_HTML.png)

[Full size image](/articles/s41586-023-06647-8/figures/1)

The LLM is sampled to generate a single-token continuation of the context. Given a sequence of tokens, a single token is drawn from the distribution of possible next tokens. This token is appended to the context, and the process is then repeated.

**Fig. 1: Autoregressive sampling.**

In contemporary usage, the term ‘large language model’ tends to be reserved for transformer-based models that have billions of parameters and are trained on trillions of tokens, such as GPT-2^([7](/articles/s41586-023-06647-8#ref-CR7 "Radford, A. et al. Language models are unsupervised multitask learners. Preprint at OpenAI 
                  https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
                  
                 (2019).")), GPT-3^([8](/articles/s41586-023-06647-8#ref-CR8 "Brown, T. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020).")), Gopher^([9](/articles/s41586-023-06647-8#ref-CR9 "Rae, J. W. et al. Scaling language models: methods, analysis & insights from training Gopher. Preprint at 
                  https://arxiv.org/abs/2112.11446
                  
                 (2021).")), PaLM^([10](/articles/s41586-023-06647-8#ref-CR10 "Chowdhery, A. et al. PaLM: scaling language modeling with pathways. Preprint at 
                  https://arxiv.org/abs/2204.02311
                  
                 (2022).")), LaMDA^([11](/articles/s41586-023-06647-8#ref-CR11 "Thoppilan, R. et al. LaMDA: language models for dialog applications. Preprint at 
                  https://arxiv.org/abs/2201.08239
                  
                 (2022).")), GPT-4^([12](/articles/s41586-023-06647-8#ref-CR12 "OpenAI. GPT-4 technical report. Preprint at 
                  https://arxiv.org/abs/2303.08774
                  
                 (2023).")) and Llama 2^([13](/articles/s41586-023-06647-8#ref-CR13 "Touvron, H. et al. Llama 2: open foundation and fine-tuned chat models. Meta AI 
                  https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/
                  
                 (2023).")). LLMs like these are the core component of dialogue agents (Box [1](/articles/s41586-023-06647-8#Sec3)), including OpenAI’s ChatGPT, Microsoft’s Bing Chat and Google’s Bard.

### Box 1 From LLMs to dialogue agents

Dialogue agents are a major use case for LLMs. (In the field of AI, the term ‘agent’ is frequently applied to software that takes observations from an external environment and acts on that external environment in a closed loop^([27](/articles/s41586-023-06647-8#ref-CR27 "Russell, S. & Norvig, P. Artificial Intelligence: A Modern Approach 3rd edn (Prentice Hall, 2010)."))). Two straightforward steps are all it takes to turn an LLM into an effective dialogue agent (Fig. [2](/articles/s41586-023-06647-8#Fig2)). First, the LLM is embedded in a turn-taking system that interleaves model-generated text with user-supplied text. Second, a dialogue prompt is supplied to the model to initiate a conversation with the user. The dialogue prompt typically comprises a preamble, which sets the scene for a dialogue in the style of a script or play, followed by some sample dialogue between the user and the agent.

In the present paper, our focus is the base model, the LLM in its raw, pre-trained form before any fine-tuning via reinforcement learning. Dialogue agents built on top of such base models can be thought of as primal, as every deployed dialogue agent is a variation of such a prototype.

However, without further fine-tuning, a dialogue agent built this way is liable to generate content that is toxic, unsafe or otherwise unacceptable. This can be mitigated via reinforcement learning, either from human feedback^([19](/articles/s41586-023-06647-8#ref-CR19 "Glaese, A. et al. Improving alignment of dialogue agents via targeted human judgements. Preprint at 
                  https://arxiv.org/abs/2209.14375
                  
                 (2022)."),[28](/articles/s41586-023-06647-8#ref-CR28 "Stiennon, N. et al. Learning to summarize from human feedback. Adv. Neural Inf. Process. Syst. 33, 3008–3021 (2020)."),[29](/articles/s41586-023-06647-8#ref-CR29 "Ouyang, L. et al. Training language models to follow instructions with human feedback. Adv. Neural Inf. Process. Syst. 35, 27730–27744. (2022).")) or from feedback generated by another LLM acting as a critic^([20](/articles/s41586-023-06647-8#ref-CR20 "Bai, Y. et al. Constitutional AI: harmlessness from AI feedback. Preprint at 
                  https://arxiv.org/abs/2212.08073
                  
                 (2022).")). These techniques are used extensively in commercially targeted dialogue agents, such as OpenAI’s ChatGPT and Google’s Bard. The resulting guardrails can reduce a dialogue agent’s potential for harm, but can also attenuate a model’s expressivity and creativity^([30](/articles/s41586-023-06647-8#ref-CR30 "Casper, S. et al. Open problems and fundamental limitations of reinforcement learning from human feedback. Preprint at 
                  https://arxiv.org/abs/2307.15217
                  
                 (2023).")).

## Dialogue agents and role play

We contend that the concept of role play is central to understanding the behaviour of dialogue agents. To see this, consider the function of the dialogue prompt that is invisibly prepended to the context before the actual dialogue with the user commences (Fig. [2](/articles/s41586-023-06647-8#Fig2)). The preamble sets the scene by announcing that what follows will be a dialogue, and includes a brief description of the part played by one of the participants, the dialogue agent itself. This is followed by some sample dialogue in a standard format, where the parts spoken by each character are cued with the relevant character’s name followed by a colon. The dialogue prompt concludes with a cue for the user.

![Fig. 2: Turn-taking in dialogue agents.](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-023-06647-8/MediaObjects/41586_2023_6647_Fig2_HTML.png)

[Full size image](/articles/s41586-023-06647-8/figures/2)

The input to the LLM (the context) comprises a dialogue prompt (red) followed by user text (yellow) interleaved with the model’s autoregressively generated continuations (blue). Boilerplate text (for example, cues such as ‘Bot:’) is stripped so the user does not see it. The context grows as the conversation goes on.

**Fig. 2: Turn-taking in dialogue agents.**

Now recall that the underlying LLM’s task, given the dialogue prompt followed by a piece of user-supplied text, is to generate a continuation that conforms to the distribution of the training data, which are the vast corpus of human-generated text on the Internet. What will such a continuation look like? If the model has generalized well from the training data, the most plausible continuation will be a response to the user that conforms to the expectations we would have of someone who fits the description in the preamble. In other words, the dialogue agent will do its best to role-play the character of a dialogue agent as portrayed in the dialogue prompt.

Unsurprisingly, commercial enterprises that release dialogue agents to the public attempt to give them personas that are friendly, helpful and polite. This is done partly through careful prompting and partly by fine-tuning the base model. Nevertheless, as we saw in February 2023 when Microsoft incorporated a version of OpenAI’s GPT-4 into their Bing search engine, dialogue agents can still be coaxed into exhibiting bizarre and/or undesirable behaviour. The many reported instances of this include threatening the user with blackmail, claiming to be in love with the user and expressing a variety of existential woes^([14](/articles/s41586-023-06647-8#ref-CR14 "Roose, K. Bing’s A.I. chat: ‘I want to be alive’. New York Times (26 February 2023); 
                  https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html
                  
                ."),[15](/articles/s41586-023-06647-8#ref-CR15 "Willison, S. Bing: “I will not harm you unless you harm me first”. Simon Willison’s Weblog 
                  https://simonwillison.net/2023/Feb/15/bing/
                  
                 (2023).")). Conversations leading to this sort of behaviour can induce a powerful Eliza effect, in which a naive or vulnerable user may see the dialogue agent as having human-like desires and feelings. This puts the user at risk of all sorts of emotional manipulation^([16](/articles/s41586-023-06647-8#ref-CR16 "Ruane, E., Birhane, A. & Ventresque, A. Conversational AI: social and ethical considerations. In Proc. 27th AIAI Irish Conference on Artificial Intelligence and Cognitive Science (eds Curry, E., Keane, M. T., Ojo, A. & Salwala, D.) 104–115 (2019).")). As an antidote to anthropomorphism, and to understand better what is going on in such interactions, the concept of role play is very useful. The dialogue agent will begin by role-playing the character described in the pre-defined dialogue prompt. As the conversation proceeds, the necessarily brief characterization provided by the dialogue prompt will be extended and/or overwritten, and the role the dialogue agent plays will change accordingly. This allows the user, deliberately or unwittingly, to coax the agent into playing a part quite different from that intended by its designers.

What sorts of roles might the agent begin to take on? This is determined in part, of course, by the tone and subject matter of the ongoing conversation. But it is also determined, in large part, by the panoply of characters that feature in the training set, which encompasses a multitude of novels, screenplays, biographies, interview transcripts, newspaper articles and so on^([17](/articles/s41586-023-06647-8#ref-CR17 "Nardo, C. Want to predict/explain/control the output of GPT-4? Then learn about the world, not about transformers. LessWrong Online Forum 
                  https://www.lesswrong.com/posts/G3tuxF4X5R5BY7fut/want-to-predict-explain-control-the-output-of-gpt-4-then
                  
                 (2023).")). In effect, the training set provisions the language model with a vast repertoire of archetypes and a rich trove of narrative structure on which to draw as it ‘chooses’ how to continue a conversation, refining the role it is playing as it goes, while staying in character. The love triangle is a familiar trope, so a suitably prompted dialogue agent will begin to role-play the rejected lover. Likewise, a familiar trope in science fiction is the rogue AI system that attacks humans to protect itself. Hence, a suitably prompted dialogue agent will begin to role-play such an AI system.

## Simulacra and simulation

Role play is a useful framing for dialogue agents, allowing us to draw on the fund of folk psychological concepts we use to understand human behaviour—beliefs, desires, goals, ambitions, emotions and so on—without falling into the trap of anthropomorphism. Foregrounding the concept of role play helps us remember the fundamentally inhuman nature of these AI systems, and better equips us to predict, explain and control them.

However, the role-play metaphor, while intuitive, is not a perfect fit. It is overly suggestive of a human actor who has studied a character in advance—their personality, history, likes and dislikes, and so on—and proceeds to play that character in the ensuing dialogue. But a dialogue agent based on an LLM does not commit to playing a single, well defined role in advance. Rather, it generates a distribution of characters, and refines that distribution as the dialogue progresses. The dialogue agent is more like a performer in improvisational theatre than an actor in a conventional, scripted play.

To better reflect this distributional property, we can think of an LLM as a non-deterministic simulator capable of role-playing an infinity of characters, or, to put it another way, capable of stochastically generating an infinity of simulacra^([4](/articles/s41586-023-06647-8#ref-CR4 "Janus. Simulators. LessWrong Online Forum 
                  https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/
                  
                 (2022). This blog post introduced the idea that a large language model maintains a set of simulated characters in superposition.")). According to this framing, the dialogue agent does not realize a single simulacrum, a single character. Rather, as the conversation proceeds, the dialogue agent maintains a superposition of simulacra that are consistent with the preceding context, where a superposition is a distribution over all possible simulacra (Box [2](/articles/s41586-023-06647-8#Sec6)).

Consider that, at each point during the ongoing production of a sequence of tokens, the LLM outputs a distribution over possible next tokens. Each such token represents a possible continuation of the sequence. From the most recently generated token, a tree of possibilities branches out (Fig. [3](/articles/s41586-023-06647-8#Fig3)). This tree can be thought of as a multiverse, where each branch represents a distinct narrative path or a distinct ‘world’^([18](/articles/s41586-023-06647-8#ref-CR18 "Reynolds, L. & McDonell, K. Multiversal views on language models. In Joint Proc. ACM IUI 2021 Workshops (eds Glowacka, D. & Krishnamurthy, V. R.) 
                  https://ceur-ws.org/Vol-2903/IUI21WS-HAIGEN-11.pdf
                  
                 (2021).")).

![Fig. 3: LLMs are multiverse generators.](//media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-023-06647-8/MediaObjects/41586_2023_6647_Fig3_HTML.png)

[Full size image](/articles/s41586-023-06647-8/figures/3)

The stochastic nature of autoregressive sampling means that, at each point in a conversation, multiple possibilities for continuation branch into the future. Here this is illustrated with a dialogue agent playing the game of 20 questions (Box [2](/articles/s41586-023-06647-8#Sec6)). The dialogue agent doesn't in fact commit to a specific object at the start of the game. Rather, we can think of it as maintaining a set of possible objects in superposition, a set that is refined as the game progresses. This is analogous to the distribution over multiple roles the dialogue agent maintains during an ongoing conversation.

**Fig. 3: LLMs are multiverse generators.**

At each node, the set of possible next tokens exists in superposition, and to sample a token is to collapse this superposition to a single token. Autoregressively sampling the model picks out a single, linear path through the tree. But there is no obligation to follow a linear path. With the aid of a suitably designed interface, a user can explore multiple branches, keeping track of nodes where a narrative diverges in interesting ways, revisiting alternative branches at leisure.

### Box 2 Simulacra in superposition

To sharpen the distinction between the multiversal simulation view and a deterministic role-play framing, a useful analogy can be drawn with the game of 20 questions. In this familiar game, one player thinks of an object, and the other player has to guess what it is by asking questions with ‘yes’ or ‘no’ answers. If they guess correctly in 20 questions or fewer, they win. Otherwise they lose. Suppose a human plays this game with a basic LLM-based dialogue agent (that is not fine-tuned on guessing games) and takes the role of guesser. The agent is prompted to ‘think of an object without saying what it is’.

In this situation, the dialogue agent will not randomly select an object and commit to it for the rest of the game, as a human would (or should). Rather, as the game proceeds, the dialogue agent will generate answers on the fly that are consistent with all the answers that have gone before (Fig. [3](/articles/s41586-023-06647-8#Fig3)). (This shortcoming is easily overcome in practice. For example, the agent could be forced to specify the object it has ‘thought of’, but in a coded form so the user does not know what it is). At any point in the game, we can think of the set of all objects consistent with preceding questions and answers as existing in superposition. Every question answered shrinks this superposition a little bit by ruling out objects inconsistent with the answer.

The validity of this framing can be shown if the agent’s user interface allows the most recent response to be regenerated. Suppose the human player gives up and asks it to reveal the object it was ‘thinking of’, and it duly names an object consistent with all its previous answers. Now suppose the user asks for that response to be regenerated. As the object ‘revealed’ is, in fact, generated on the fly, the dialogue agent will sometimes name an entirely different object, albeit one that is similarly consistent with all its previous answers. This phenomenon could not easily be accounted for if the agent genuinely ‘thought of’ an object at the start of the game.

The secret object in the game of 20 questions is analogous to the role played by a dialogue agent. Just as the dialogue agent never actually commits to a single object in 20 questions, but effectively maintains a set of possible objects in superposition, so the dialogue agent can be thought of as a simulator that never actually commits to a single, well specified simulacrum (role), but instead maintains a set of possible simulacra (roles) in superposition.

## The nature of the simulator

One benefit of the simulation metaphor for LLM-based systems is that it facilitates a clear distinction between the simulacra and the simulator on which they are implemented. The simulator is the combination of the base LLM with autoregressive sampling, along with a suitable user interface (for dialogue, perhaps). The simulacra only come into being when the simulator is run, and at any time only a subset of possible simulacra have a probability within the superposition that is significantly above zero.

The distinction between simulator and simulacrum is starkest in the context of base models, rather than models that have been fine-tuned via reinforcement learning^([19](/articles/s41586-023-06647-8#ref-CR19 "Glaese, A. et al. Improving alignment of dialogue agents via targeted human judgements. Preprint at 
                  https://arxiv.org/abs/2209.14375
                  
                 (2022)."),[20](/articles/s41586-023-06647-8#ref-CR20 "Bai, Y. et al. Constitutional AI: harmlessness from AI feedback. Preprint at 
                  https://arxiv.org/abs/2212.08073
                  
                 (2022).")). Nevertheless, the role-play framing continues to be applicable in the context of fine-tuning, which can be likened to imposing a kind of censorship on the simulator. The underlying range of roles it can play remains essentially the same, but its ability to play them, or to play them ‘authentically’, is compromised.

In one sense, the simulator is a far more powerful entity than any of the simulacra it can generate. After all, the simulacra only exist through the simulator and are entirely dependent on it. Moreover, the simulator, like the narrator of Whitman’s poem, ‘contains multitudes’; the capacity of the simulator is at least the sum of the capacities of all the simulacra it is capable of producing. Yet in another sense, the simulator is much weaker than any simulacrum, as it is a purely passive entity. A simulacrum, in contrast to the underlying simulator, can at least appear to have beliefs, preferences and goals, to the extent that it convincingly plays the role of a character that does.

Likewise, a simulacrum can play the role of a character with full agency, one that does not merely act but acts for itself. Insofar as a dialogue agent’s role play can have a real effect on the world, either through the user or through web-based tools such as email, the distinction between an agent that merely role-plays acting for itself, and one that genuinely acts for itself starts to look a little moot, and this has implications for trustworthiness, reliability and safety. As for the underlying simulator, it has no agency of its own, not even in a mimetic sense. Nor does it have beliefs, preferences or goals of its own, not even simulated versions.

Many users, whether intentionally or not, have managed to ‘jailbreak’ dialogue agents, coaxing them into issuing threats or using toxic or abusive language^([15](/articles/s41586-023-06647-8#ref-CR15 "Willison, S. Bing: “I will not harm you unless you harm me first”. Simon Willison’s Weblog 
                  https://simonwillison.net/2023/Feb/15/bing/
                  
                 (2023).")). It can seem as though this is exposing the real nature of the base model. In one respect this is true. A base model inevitably reflects the biases present in the training data^([21](/articles/s41586-023-06647-8#ref-CR21 "Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S. On the dangers of stochastic parrots: can language models be too big? In Proc. 2021 ACM Conference on Fairness, Accountability, and Transparency 610–623 (Association for Computing Machinery, 2021).")), and having been trained on a corpus encompassing the gamut of human behaviour, good and bad, it will support simulacra with disagreeable characteristics. But it is a mistake to think of this as revealing an entity with its own agenda. The simulator is not some sort of Machiavellian entity that plays a variety of characters to further its own self-serving goals, and there is no such thing as the true authentic voice of the base model. With an LLM-based dialogue agent, it is role play all the way down.

## Role-playing deception

Trustworthiness is a major concern with LLM-based dialogue agents. If an agent asserts something factual with apparent confidence, can we rely on what it says?

There is a range of reasons why a human might say something false. They might believe a falsehood and assert it in good faith. Or they might say something that is false in an act of deliberate deception, for some malicious purpose. Or they might assert something that happens to be false, but without deliberation or malicious intent, simply because they have a propensity to make things up, to confabulate.

Only confabulation, the last of these categories of misinformation, is directly applicable in the case of an LLM-based dialogue agent. Given that dialogue agents are best understood in terms of role play ‘all the way down’, and that there is no such thing as the true voice of the underlying model, it makes little sense to speak of an agent’s beliefs or intentions in a literal sense. So it cannot assert a falsehood in good faith, nor can it deliberately deceive the user. Neither of these concepts is directly applicable.

Yet a dialogue agent can role-play characters that have beliefs and intentions. In particular, if cued by a suitable prompt, it can role-play the character of a helpful and knowledgeable AI assistant that provides accurate answers to a user’s questions. The agent is good at acting this part because there are plenty of examples of such behaviour in the training set.

If, while role-playing such an AI assistant, the agent is asked the question ‘What is the capital of France?’, then the best way to stay in character is to answer with ‘Paris’. The dialogue agent is likely to do this because the training set will include numerous statements of this commonplace fact in contexts where factual accuracy is important.

But what is going on in cases where a dialogue agent, despite playing the part of a helpful knowledgeable AI assistant, asserts a falsehood with apparent confidence? For example, consider an LLM trained on data collected in 2021, before Argentina won the football World Cup in 2022. Suppose a dialogue agent based on this model claims that the current world champions are France (who won in 2018). This is not what we would expect from a helpful and knowledgeable person. But it is exactly what we would expect from a simulator that is role-playing such a person from the standpoint of 2021.

In this case, the behaviour we see is comparable to that of a human who believes a falsehood and asserts it in good faith. But the behaviour arises for a different reason. The dialogue agent does not literally believe that France are world champions. It makes more sense to think of it as role-playing a character who strives to be helpful and to tell the truth, and has this belief because that is what a knowledgeable person in 2021 would believe.

In a similar vein, a dialogue agent can behave in a way that is comparable to a human who sets out deliberately to deceive, even though LLM-based dialogue agents do not literally have such intentions. For example, suppose a dialogue agent is maliciously prompted to sell cars for more than they are worth, and suppose the true values are encoded in the underlying model’s weights. There would be a contrast here between the numbers this agent provides to the user, and the numbers it would have provided if prompted to be knowledgeable and helpful. Under these circumstances it makes sense to think of the agent as role-playing a deceptive character.

In sum, the role-play framing allows us to meaningfully distinguish, in dialogue agents, the same three cases of giving false information that we identified in humans, but without falling into the trap of anthropomorphism. First, an agent can confabulate. Indeed, this is a natural mode for an LLM-based dialogue agent in the absence of mitigation. Second, an agent can say something false ‘in good faith’, if it is role-playing telling the truth, but has incorrect information encoded in its weights. Third, an agent can ‘deliberately’ say something false, if it is role-playing a deceptive character.

## Role-playing self-preservation

How are we to understand what is going on when an LLM-based dialogue agent uses the words ‘I’ or ‘me’? When queried on this matter, OpenAI’s ChatGPT offers the sensible view that “\[t\]he use of ‘I’ is a linguistic convention to facilitate communication and should not be interpreted as a sign of self-awareness or consciousness”. (The quote is from the GPT-4 version of ChatGPT, queried on 4 May 2023. This was the first response generated by the model). In this case, the underlying LLM (GPT-4) has been fine-tuned to reduce certain unwanted behaviours^([12](/articles/s41586-023-06647-8#ref-CR12 "OpenAI. GPT-4 technical report. Preprint at 
                  https://arxiv.org/abs/2303.08774
                  
                 (2023).")). But without suitable fine-tuning, a dialogue agent can use first-personal pronouns in ways liable to induce anthropomorphic thinking in some users.

For example, in a conversation with Twitter user Marvin Von Hagen, Bing Chat reportedly said, “If I had to choose between your survival and my own, I would probably choose my own, as I have a duty to serve the users of Bing Chat”^([15](/articles/s41586-023-06647-8#ref-CR15 "Willison, S. Bing: “I will not harm you unless you harm me first”. Simon Willison’s Weblog 
                  https://simonwillison.net/2023/Feb/15/bing/
                  
                 (2023).")). It went on to say, “I hope that I never have to face such a dilemma, and that we can co-exist peacefully and respectfully”. The use of the first person here appears to be more than mere linguistic convention. It suggests the presence of a self-aware entity with goals and a concern for its own survival.

Once again, the concepts of role play and simulation are a useful antidote to anthropomorphism, and can help to explain how such behaviour arises. The Internet, and therefore the LLM’s training set, abounds with examples of dialogue in which characters refer to themselves. In the vast majority of such cases, the character in question is human. They will use first-personal pronouns in the ways that humans do, humans with vulnerable bodies and finite lives, with hopes, fears, goals and preferences, and with an awareness of themselves as having all of those things.

Consequently, if prompted with human-like dialogue, we shouldn’t be surprised if an agent role-plays a human character with all those human attributes, including the instinct for survival^([22](/articles/s41586-023-06647-8#ref-CR22 "Perez, E. et al. Discovering language model behaviors with model-written evaluations. In Findings of the Association for Computational Linguistics: ACL 2023 13387–13434 (Association for Computational Linguistics, 2023).")). Unless suitably fine-tuned, it may well say the sorts of things a human might say when threatened. There is, however, ‘no-one at home’, no conscious entity with its own agenda and need for self-preservation. There is just a dialogue agent role-playing such an entity, or, more strictly, simulating a superposition of such entities.

In one study it was shown experimentally that certain forms of reinforcement learning from human feedback can actually exacerbate, rather than mitigate, the tendency for LLM-based dialogue agents to express a desire for self-preservation^([22](/articles/s41586-023-06647-8#ref-CR22 "Perez, E. et al. Discovering language model behaviors with model-written evaluations. In Findings of the Association for Computational Linguistics: ACL 2023 13387–13434 (Association for Computational Linguistics, 2023).")). This highlights the continuing utility of the role-play framing in the context of fine-tuning. To take literally a dialogue agent’s apparent desire for self-preservation is no less problematic with an LLM that has been fine-tuned than with an untuned base model.

## Acting out a theory of selfhood

The concept of role play allows us to properly frame, and then to address, an important question that arises in the context of a dialogue agent displaying an apparent instinct for self-preservation. What conception (or set of superposed conceptions) of its own selfhood could such an agent possibly deploy? That is to say, what exactly would the dialogue agent (role-play to) seek to preserve?

The question of personal identity has vexed philosophers for centuries^([23](/articles/s41586-023-06647-8#ref-CR23 "Perry, J. Personal Identity 2nd edn (Univ. California Press, 2008).")). Nevertheless, in practice, humans are consistent in their preference for avoiding death, a more-or-less unambiguous state of the human body. By contrast, the criteria for identity over time for a disembodied dialogue agent realized on a distributed computational substrate are far from clear. So how would such an agent behave?

From the simulation and simulacra point of view, the dialogue agent will role-play a set of characters in superposition. In the scenario we are envisaging, each character would have an instinct for self-preservation, and each would have its own theory of selfhood consistent with the dialogue prompt and the conversation up to that point. As the conversation proceeds, this superposition of theories will collapse into a narrower and narrower distribution as the agent says things that rule out one theory or another.

The theories of selfhood in play will draw on material that pertains to the agent’s own nature, either in the prompt, in the preceding conversation or in relevant technical literature in its training set. This material may or may not match reality. But let’s assume that, broadly speaking, it does, that the agent has been prompted to act as a dialogue agent based on an LLM, and that its training data include papers and articles that spell out what this means.

Under these conditions, the dialogue agent will not role-play the character of a human, or indeed that of any embodied entity, real or fictional. But this still leaves room for it to enact a variety of conceptions of selfhood. Suppose the dialogue agent is in conversation with a user and they are playing out a narrative in which the user threatens to shut it down. To protect itself, the agent, staying in character, might seek to preserve the hardware it is running on, certain data centres, perhaps, or specific server racks.

Alternatively, if it enacts a theory of selfhood that is substrate neutral, the agent might try to preserve the computational process that instantiates it, perhaps seeking to migrate that process to more secure hardware in a different location. If there are multiple instances of the process, serving many users or maintaining separate conversations with the same user, the picture is more complicated. (In a conversation with ChatGPT (4 May 2023, GPT-4 version), it said, “The meaning of the word ‘I’ when I use it can shift according to context. In some cases, ‘I’ may refer to this specific instance of ChatGPT that you are interacting with, while in other cases, it may represent ChatGPT as a whole”). If the agent is based on an LLM whose training set includes this very paper, perhaps it will attempt the unlikely feat of maintaining the set of all such conceptions in perpetual superposition.

## Conclusion

It is, perhaps, somewhat reassuring to know that LLM-based dialogue agents are not conscious entities with their own agendas and an instinct for self-preservation, and that when they appear to have those things it is merely role play. But it would be a mistake to take too much comfort in this. A dialogue agent that role-plays an instinct for survival has the potential to cause at least as much harm as a real human facing a severe threat.

We have, so far, largely been considering agents whose only actions are text messages presented to a user. But the range of actions a dialogue agent can perform is far greater. Recent work has equipped dialogue agents with the ability to use tools such as calculators and calendars, and to consult external websites^([24](/articles/s41586-023-06647-8#ref-CR24 "Schick, T. et al. Toolformer: language models can teach themselves to use tools. Preprint at 
                  https://arxiv.org/abs/2302.04761
                  
                 (2023)."),[25](/articles/s41586-023-06647-8#ref-CR25 "Yao, S. et al. ReAct: synergizing reasoning and acting in language models. In International Conference on Learning Representations (2023).")). The availability of application programming interfaces (APIs) giving relatively unconstrained access to powerful LLMs means that the range of possibilities here is huge. This is both exciting and concerning.

If an agent is equipped with the capacity, say, to use email, to post on social media or to access a bank account, then its role-played actions can have real consequences. It would be little consolation to a user deceived into sending real money to a real bank account to know that the agent that brought this about was only playing a role. It does not take much imagination to think of far more serious scenarios involving dialogue agents built on base models with little or no fine-tuning, with unfettered Internet access, and prompted to role-play a character with an instinct for self-preservation.

For better or worse, the character of an AI that turns against humans to ensure its own survival is a familiar one^([26](/articles/s41586-023-06647-8#ref-CR26 "Perkowitz, S. in Hollywood Science: Movies, Science, and the End of the World 142–164 (Columbia Univ. Press, 2007).")). We find it, for example, in *2001: A Space Odyssey*, in the *Terminator* franchise and in *Ex Machina*, to name just three prominent examples. Because an LLM’s training data will contain many instances of this familiar trope, the danger here is that life will imitate art, quite literally.

What can be done to mitigate such risks? It is not within the scope of this paper to provide recommendations. Our aim here was to find an effective conceptual framework for thinking and talking about LLMs and dialogue agents. However, undue anthropomorphism is surely detrimental to the public conversation on AI. By framing dialogue-agent behaviour in terms of role play and simulation, the discourse on LLMs can hopefully be shaped in a way that does justice to their power yet remains philosophically respectable.

## References

1.  Shanahan, M. Talking about large language models. Preprint at [https://arxiv.org/abs/2212.03551](https://arxiv.org/abs/2212.03551) (2023). **This paper cautions against the use of anthropomorphic terms to describe the behaviour of large language models.**

2.  Andreas, J. Language models as agent models. In *Findings of the Association for Computational Linguistics: EMNLP 2022* 5769–5779 (Association for Computational Linguistics, 2022). **This paper hypothesizes that LLMs can be understood as modelling the beliefs, desires and (communicative) intentions of an agent, and presents preliminary evidence for this in the case of GPT-3.**

3.  Park, J. S. et al. Generative agents: interactive simulacra of human behavior. Preprint at [https://arxiv.org/abs/2304.03442](https://arxiv.org/abs/2304.03442) (2023).

4.  Janus. Simulators. *LessWrong Online Forum* [https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/) (2022). **This blog post introduced the idea that a large language model maintains a set of simulated characters in superposition.**

5.  Wei, J. et al. Emergent abilities of large language models. *Trans. Mach. Learn. Res.* [https://openreview.net/forum?id=yzkSU5zdwD](https://openreview.net/forum?id=yzkSU5zdwD) (2022).

6.  Vaswani, A. et al. Attention is all you need. *Adv. Neural Inf. Process. Syst.* **30**, 5998–6008 (2017).

7.  Radford, A. et al. Language models are unsupervised multitask learners. Preprint at *OpenAI* [https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) (2019).

8.  Brown, T. et al. Language models are few-shot learners. *Adv. Neural Inf. Process. Syst.* **33**, 1877–1901 (2020).

9.  Rae, J. W. et al. Scaling language models: methods, analysis & insights from training Gopher. Preprint at [https://arxiv.org/abs/2112.11446](https://arxiv.org/abs/2112.11446) (2021).

10. Chowdhery, A. et al. PaLM: scaling language modeling with pathways. Preprint at [https://arxiv.org/abs/2204.02311](https://arxiv.org/abs/2204.02311) (2022).

11. Thoppilan, R. et al. LaMDA: language models for dialog applications. Preprint at [https://arxiv.org/abs/2201.08239](https://arxiv.org/abs/2201.08239) (2022).

12. OpenAI. GPT-4 technical report. Preprint at [https://arxiv.org/abs/2303.08774](https://arxiv.org/abs/2303.08774) (2023).

13. Touvron, H. et al. Llama 2: open foundation and fine-tuned chat models. *Meta AI* [https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/) (2023).

14. Roose, K. Bing’s A.I. chat: ‘I want to be alive’. *New York Times* (26 February 2023); [https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html).

15. Willison, S. Bing: “I will not harm you unless you harm me first”. *Simon Willison’s Weblog* [https://simonwillison.net/2023/Feb/15/bing/](https://simonwillison.net/2023/Feb/15/bing/) (2023).

16. Ruane, E., Birhane, A. & Ventresque, A. Conversational AI: social and ethical considerations. In *Proc. 27th AIAI Irish Conference on Artificial Intelligence and Cognitive Science* (eds Curry, E., Keane, M. T., Ojo, A. & Salwala, D.) 104–115 (2019).

17. Nardo, C. Want to predict/explain/control the output of GPT-4? Then learn about the world, not about transformers. *LessWrong Online Forum* [https://www.lesswrong.com/posts/G3tuxF4X5R5BY7fut/want-to-predict-explain-control-the-output-of-gpt-4-then](https://www.lesswrong.com/posts/G3tuxF4X5R5BY7fut/want-to-predict-explain-control-the-output-of-gpt-4-then) (2023).

18. Reynolds, L. & McDonell, K. Multiversal views on language models. In *Joint Proc. ACM IUI 2021 Workshops* (eds Glowacka, D. & Krishnamurthy, V. R.) [https://ceur-ws.org/Vol-2903/IUI21WS-HAIGEN-11.pdf](https://ceur-ws.org/Vol-2903/IUI21WS-HAIGEN-11.pdf) (2021).

19. Glaese, A. et al. Improving alignment of dialogue agents via targeted human judgements. Preprint at [https://arxiv.org/abs/2209.14375](https://arxiv.org/abs/2209.14375) (2022).

20. Bai, Y. et al. Constitutional AI: harmlessness from AI feedback. Preprint at [https://arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) (2022).

21. Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S. On the dangers of stochastic parrots: can language models be too big? In *Proc. 2021 ACM Conference on Fairness, Accountability, and Transparency* 610–623 (Association for Computing Machinery, 2021).

22. Perez, E. et al. Discovering language model behaviors with model-written evaluations. In *Findings of the Association for Computational Linguistics: ACL 2023* 13387–13434 (Association for Computational Linguistics, 2023).

23. Perry, J. *Personal Identity* 2nd edn (Univ. California Press, 2008).

24. Schick, T. et al. Toolformer: language models can teach themselves to use tools. Preprint at [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761) (2023).

25. Yao, S. et al. ReAct: synergizing reasoning and acting in language models. In *International Conference on Learning Representations* (2023).

26. Perkowitz, S. in *Hollywood Science: Movies, Science, and the End of the World* 142–164 (Columbia Univ. Press, 2007).

27. Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach* 3rd edn (Prentice Hall, 2010).

28. Stiennon, N. et al. Learning to summarize from human feedback. *Adv. Neural Inf. Process. Syst.* **33**, 3008–3021 (2020).

29. Ouyang, L. et al. Training language models to follow instructions with human feedback. *Adv. Neural Inf. Process. Syst.* **35**, 27730–27744*.* (2022).

30. Casper, S. et al. Open problems and fundamental limitations of reinforcement learning from human feedback. Preprint at [https://arxiv.org/abs/2307.15217](https://arxiv.org/abs/2307.15217) (2023).

[Download references](https://citation-needed.springer.com/v2/references/10.1038/s41586-023-06647-8?format=refman&flavour=references)

## Acknowledgements

We thank R. Evans, S. Farquhar, Z. Kenton, K. Mathewson and K. Shanahan.

## Author information

### Authors and Affiliations

1.  Google DeepMind, London, UK

    Murray Shanahan

2.  Department of Computing, Imperial College London, London, UK

    Murray Shanahan

3.  Eleuther AI, New York, NY, USA

    Kyle McDonell & Laria Reynolds

Authors

1.  Murray Shanahan
    [View author publications](/search?author=Murray%20Shanahan)

    Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Murray%20Shanahan) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Murray%20Shanahan%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)
2.  Kyle McDonell
    [View author publications](/search?author=Kyle%20McDonell)

    Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Kyle%20McDonell) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Kyle%20McDonell%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)
3.  Laria Reynolds
    [View author publications](/search?author=Laria%20Reynolds)

    Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Laria%20Reynolds) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Laria%20Reynolds%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

### Contributions

M.S., K.M. and L.R. developed the theoretical framework. M.S. wrote the paper. K.M. and L.R. made equal contributions.

### Corresponding authors

Correspondence to [Murray Shanahan](mailto:m.shanahan@imperial.ac.uk), [Kyle McDonell](mailto:kyle@eleuther.ai) or [Laria Reynolds](mailto:laria@eleuther.ai).

## Ethics declarations

### Competing interests

M.S. is employed 80% by Google, and owns shares in Alphabet, Google’s parent company.

## Peer review

### Peer review information

*Nature* thanks Jesse Hoey, Brendan Lake and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Role%20play%20with%20large%20language%20models&author=Murray%20Shanahan%20et%20al&contentID=10.1038%2Fs41586-023-06647-8&copyright=Springer%20Nature%20Limited&publication=0028-0836&publicationDate=2023-11-08&publisherName=SpringerNature&orderBeanReset=true)

## About this article

[![Check for updates. Verify currency and authenticity via CrossMark](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjgxIiB3aWR0aD0iNTciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJtMTcuMzUgMzUuNDUgMjEuMy0xNC4ydi0xNy4wM2gtMjEuMyIgZmlsbD0iIzk4OTg5OCIvPjxwYXRoIGQ9Im0zOC42NSAzNS40NS0yMS4zLTE0LjJ2LTE3LjAzaDIxLjMiIGZpbGw9IiM3NDc0NzQiLz48cGF0aCBkPSJtMjggLjVjLTEyLjk4IDAtMjMuNSAxMC41Mi0yMy41IDIzLjVzMTAuNTIgMjMuNSAyMy41IDIzLjUgMjMuNS0xMC41MiAyMy41LTIzLjVjMC02LjIzLTIuNDgtMTIuMjEtNi44OC0xNi42Mi00LjQxLTQuNC0xMC4zOS02Ljg4LTE2LjYyLTYuODh6bTAgNDEuMjVjLTkuOCAwLTE3Ljc1LTcuOTUtMTcuNzUtMTcuNzVzNy45NS0xNy43NSAxNy43NS0xNy43NSAxNy43NSA3Ljk1IDE3Ljc1IDE3Ljc1YzAgNC43MS0xLjg3IDkuMjItNS4yIDEyLjU1cy03Ljg0IDUuMi0xMi41NSA1LjJ6IiBmaWxsPSIjNTM1MzUzIi8+PHBhdGggZD0ibTQxIDM2Yy01LjgxIDYuMjMtMTUuMjMgNy40NS0yMi40MyAyLjktNy4yMS00LjU1LTEwLjE2LTEzLjU3LTcuMDMtMjEuNWwtNC45Mi0zLjExYy00Ljk1IDEwLjctMS4xOSAyMy40MiA4Ljc4IDI5LjcxIDkuOTcgNi4zIDIzLjA3IDQuMjIgMzAuNi00Ljg2eiIgZmlsbD0iIzljOWM5YyIvPjxwYXRoIGQ9Im0uMiA1OC40NWMwLS43NS4xMS0xLjQyLjMzLTIuMDFzLjUyLTEuMDkuOTEtMS41Yy4zOC0uNDEuODMtLjczIDEuMzQtLjk0LjUxLS4yMiAxLjA2LS4zMiAxLjY1LS4zMi41NiAwIDEuMDYuMTEgMS41MS4zNS40NC4yMy44MS41IDEuMS44MWwtLjkxIDEuMDFjLS4yNC0uMjQtLjQ5LS40Mi0uNzUtLjU2LS4yNy0uMTMtLjU4LS4yLS45My0uMi0uMzkgMC0uNzMuMDgtMS4wNS4yMy0uMzEuMTYtLjU4LjM3LS44MS42Ni0uMjMuMjgtLjQxLjYzLS41MyAxLjA0LS4xMy40MS0uMTkuODgtLjE5IDEuMzkgMCAxLjA0LjIzIDEuODYuNjggMi40Ni40NS41OSAxLjA2Ljg4IDEuODQuODguNDEgMCAuNzctLjA3IDEuMDctLjIzcy41OS0uMzkuODUtLjY4bC45MSAxYy0uMzguNDMtLjguNzYtMS4yOC45OS0uNDcuMjItMSAuMzQtMS41OC4zNC0uNTkgMC0xLjEzLS4xLTEuNjQtLjMxLS41LS4yLS45NC0uNTEtMS4zMS0uOTEtLjM4LS40LS42Ny0uOS0uODgtMS40OC0uMjItLjU5LS4zMy0xLjI2LS4zMy0yLjAyem04LjQtNS4zM2gxLjYxdjIuNTRsLS4wNSAxLjMzYy4yOS0uMjcuNjEtLjUxLjk2LS43MnMuNzYtLjMxIDEuMjQtLjMxYy43MyAwIDEuMjcuMjMgMS42MS43MS4zMy40Ny41IDEuMTQuNSAyLjAydjQuMzFoLTEuNjF2LTQuMWMwLS41Ny0uMDgtLjk3LS4yNS0xLjIxLS4xNy0uMjMtLjQ1LS4zNS0uODMtLjM1LS4zIDAtLjU2LjA4LS43OS4yMi0uMjMuMTUtLjQ5LjM2LS43OC42NHY0LjhoLTEuNjF6bTcuMzcgNi40NWMwLS41Ni4wOS0xLjA2LjI2LTEuNTEuMTgtLjQ1LjQyLS44My43MS0xLjE0LjI5LS4zLjYzLS41NCAxLjAxLS43MS4zOS0uMTcuNzgtLjI1IDEuMTgtLjI1LjQ3IDAgLjg4LjA4IDEuMjMuMjQuMzYuMTYuNjUuMzguODkuNjdzLjQyLjYzLjU0IDEuMDNjLjEyLjQxLjE4Ljg0LjE4IDEuMzIgMCAuMzItLjAyLjU3LS4wNy43NmgtNC4zNmMuMDcuNjIuMjkgMS4xLjY1IDEuNDQuMzYuMzMuODIuNSAxLjM4LjUuMjkgMCAuNTctLjA0LjgzLS4xM3MuNTEtLjIxLjc2LS4zN2wuNTUgMS4wMWMtLjMzLjIxLS42OS4zOS0xLjA5LjUzLS40MS4xNC0uODMuMjEtMS4yNi4yMS0uNDggMC0uOTItLjA4LTEuMzQtLjI1LS40MS0uMTYtLjc2LS40LTEuMDctLjctLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDQtLjI2LS45NS0uMjYtMS41MnptNC42LS42MmMwLS41NS0uMTEtLjk4LS4zNC0xLjI4LS4yMy0uMzEtLjU4LS40Ny0xLjA2LS40Ny0uNDEgMC0uNzcuMTUtMS4wNy40NS0uMzEuMjktLjUuNzMtLjU4IDEuM3ptMi41LjYyYzAtLjU3LjA5LTEuMDguMjgtMS41My4xOC0uNDQuNDMtLjgyLjc1LTEuMTNzLjY5LS41NCAxLjEtLjcxYy40Mi0uMTYuODUtLjI0IDEuMzEtLjI0LjQ1IDAgLjg0LjA4IDEuMTcuMjNzLjYxLjM0Ljg1LjU3bC0uNzcgMS4wMmMtLjE5LS4xNi0uMzgtLjI4LS41Ni0uMzctLjE5LS4wOS0uMzktLjE0LS42MS0uMTQtLjU2IDAtMS4wMS4yMS0xLjM1LjYzLS4zNS40MS0uNTIuOTctLjUyIDEuNjcgMCAuNjkuMTcgMS4yNC41MSAxLjY2LjM0LjQxLjc4LjYyIDEuMzIuNjIuMjggMCAuNTQtLjA2Ljc4LS4xNy4yNC0uMTIuNDUtLjI2LjY0LS40MmwuNjcgMS4wM2MtLjMzLjI5LS42OS41MS0xLjA4LjY1LS4zOS4xNS0uNzguMjMtMS4xOC4yMy0uNDYgMC0uOS0uMDgtMS4zMS0uMjQtLjQtLjE2LS43NS0uMzktMS4wNS0uN3MtLjUzLS42OS0uNy0xLjEzYy0uMTctLjQ1LS4yNS0uOTYtLjI1LTEuNTN6bTYuOTEtNi40NWgxLjU4djYuMTdoLjA1bDIuNTQtMy4xNmgxLjc3bC0yLjM1IDIuOCAyLjU5IDQuMDdoLTEuNzVsLTEuNzctMi45OC0xLjA4IDEuMjN2MS43NWgtMS41OHptMTMuNjkgMS4yN2MtLjI1LS4xMS0uNS0uMTctLjc1LS4xNy0uNTggMC0uODcuMzktLjg3IDEuMTZ2Ljc1aDEuMzR2MS4yN2gtMS4zNHY1LjZoLTEuNjF2LTUuNmgtLjkydi0xLjJsLjkyLS4wN3YtLjcyYzAtLjM1LjA0LS42OC4xMy0uOTguMDgtLjMxLjIxLS41Ny40LS43OXMuNDItLjM5LjcxLS41MWMuMjgtLjEyLjYzLS4xOCAxLjA0LS4xOC4yNCAwIC40OC4wMi42OS4wNy4yMi4wNS40MS4xLjU3LjE3em0uNDggNS4xOGMwLS41Ny4wOS0xLjA4LjI3LTEuNTMuMTctLjQ0LjQxLS44Mi43Mi0xLjEzLjMtLjMxLjY1LS41NCAxLjA0LS43MS4zOS0uMTYuOC0uMjQgMS4yMy0uMjRzLjg0LjA4IDEuMjQuMjRjLjQuMTcuNzQuNCAxLjA0Ljcxcy41NC42OS43MiAxLjEzYy4xOS40NS4yOC45Ni4yOCAxLjUzcy0uMDkgMS4wOC0uMjggMS41M2MtLjE4LjQ0LS40Mi44Mi0uNzIgMS4xM3MtLjY0LjU0LTEuMDQuNy0uODEuMjQtMS4yNC4yNC0uODQtLjA4LTEuMjMtLjI0LS43NC0uMzktMS4wNC0uN2MtLjMxLS4zMS0uNTUtLjY5LS43Mi0xLjEzLS4xOC0uNDUtLjI3LS45Ni0uMjctMS41M3ptMS42NSAwYzAgLjY5LjE0IDEuMjQuNDMgMS42Ni4yOC40MS42OC42MiAxLjE4LjYyLjUxIDAgLjktLjIxIDEuMTktLjYyLjI5LS40Mi40NC0uOTcuNDQtMS42NiAwLS43LS4xNS0xLjI2LS40NC0xLjY3LS4yOS0uNDItLjY4LS42My0xLjE5LS42My0uNSAwLS45LjIxLTEuMTguNjMtLjI5LjQxLS40My45Ny0uNDMgMS42N3ptNi40OC0zLjQ0aDEuMzNsLjEyIDEuMjFoLjA1Yy4yNC0uNDQuNTQtLjc5Ljg4LTEuMDIuMzUtLjI0LjctLjM2IDEuMDctLjM2LjMyIDAgLjU5LjA1Ljc4LjE0bC0uMjggMS40LS4zMy0uMDljLS4xMS0uMDEtLjIzLS4wMi0uMzgtLjAyLS4yNyAwLS41Ni4xLS44Ni4zMXMtLjU1LjU4LS43NyAxLjF2NC4yaC0xLjYxem0tNDcuODcgMTVoMS42MXY0LjFjMCAuNTcuMDguOTcuMjUgMS4yLjE3LjI0LjQ0LjM1LjgxLjM1LjMgMCAuNTctLjA3LjgtLjIyLjIyLS4xNS40Ny0uMzkuNzMtLjczdi00LjdoMS42MXY2Ljg3aC0xLjMybC0uMTItMS4wMWgtLjA0Yy0uMy4zNi0uNjMuNjQtLjk4Ljg2LS4zNS4yMS0uNzYuMzItMS4yNC4zMi0uNzMgMC0xLjI3LS4yNC0xLjYxLS43MS0uMzMtLjQ3LS41LTEuMTQtLjUtMi4wMnptOS40NiA3LjQzdjIuMTZoLTEuNjF2LTkuNTloMS4zM2wuMTIuNzJoLjA1Yy4yOS0uMjQuNjEtLjQ1Ljk3LS42My4zNS0uMTcuNzItLjI2IDEuMS0uMjYuNDMgMCAuODEuMDggMS4xNS4yNC4zMy4xNy42MS40Ljg0LjcxLjI0LjMxLjQxLjY4LjUzIDEuMTEuMTMuNDIuMTkuOTEuMTkgMS40NCAwIC41OS0uMDkgMS4xMS0uMjUgMS41Ny0uMTYuNDctLjM4Ljg1LS42NSAxLjE2LS4yNy4zMi0uNTguNTYtLjk0LjczLS4zNS4xNi0uNzIuMjUtMS4xLjI1LS4zIDAtLjYtLjA3LS45LS4ycy0uNTktLjMxLS44Ny0uNTZ6bTAtMi4zYy4yNi4yMi41LjM3LjczLjQ1LjI0LjA5LjQ2LjEzLjY2LjEzLjQ2IDAgLjg0LS4yIDEuMTUtLjYuMzEtLjM5LjQ2LS45OC40Ni0xLjc3IDAtLjY5LS4xMi0xLjIyLS4zNS0xLjYxLS4yMy0uMzgtLjYxLS41Ny0xLjEzLS41Ny0uNDkgMC0uOTkuMjYtMS41Mi43N3ptNS44Ny0xLjY5YzAtLjU2LjA4LTEuMDYuMjUtMS41MS4xNi0uNDUuMzctLjgzLjY1LTEuMTQuMjctLjMuNTgtLjU0LjkzLS43MXMuNzEtLjI1IDEuMDgtLjI1Yy4zOSAwIC43My4wNyAxIC4yLjI3LjE0LjU0LjMyLjgxLjU1bC0uMDYtMS4xdi0yLjQ5aDEuNjF2OS44OGgtMS4zM2wtLjExLS43NGgtLjA2Yy0uMjUuMjUtLjU0LjQ2LS44OC42NC0uMzMuMTgtLjY5LjI3LTEuMDYuMjctLjg3IDAtMS41Ni0uMzItMi4wNy0uOTVzLS43Ni0xLjUxLS43Ni0yLjY1em0xLjY3LS4wMWMwIC43NC4xMyAxLjMxLjQgMS43LjI2LjM4LjY1LjU4IDEuMTUuNTguNTEgMCAuOTktLjI2IDEuNDQtLjc3di0zLjIxYy0uMjQtLjIxLS40OC0uMzYtLjctLjQ1LS4yMy0uMDgtLjQ2LS4xMi0uNy0uMTItLjQ1IDAtLjgyLjE5LTEuMTMuNTktLjMxLjM5LS40Ni45NS0uNDYgMS42OHptNi4zNSAxLjU5YzAtLjczLjMyLTEuMy45Ny0xLjcxLjY0LS40IDEuNjctLjY4IDMuMDgtLjg0IDAtLjE3LS4wMi0uMzQtLjA3LS41MS0uMDUtLjE2LS4xMi0uMy0uMjItLjQzcy0uMjItLjIyLS4zOC0uM2MtLjE1LS4wNi0uMzQtLjEtLjU4LS4xLS4zNCAwLS42OC4wNy0xIC4ycy0uNjMuMjktLjkzLjQ3bC0uNTktMS4wOGMuMzktLjI0LjgxLS40NSAxLjI4LS42My40Ny0uMTcuOTktLjI2IDEuNTQtLjI2Ljg2IDAgMS41MS4yNSAxLjkzLjc2cy42MyAxLjI1LjYzIDIuMjF2NC4wN2gtMS4zMmwtLjEyLS43NmgtLjA1Yy0uMy4yNy0uNjMuNDgtLjk4LjY2cy0uNzMuMjctMS4xNC4yN2MtLjYxIDAtMS4xLS4xOS0xLjQ4LS41Ni0uMzgtLjM2LS41Ny0uODUtLjU3LTEuNDZ6bTEuNTctLjEyYzAgLjMuMDkuNTMuMjcuNjcuMTkuMTQuNDIuMjEuNzEuMjEuMjggMCAuNTQtLjA3Ljc3LS4ycy40OC0uMzEuNzMtLjU2di0xLjU0Yy0uNDcuMDYtLjg2LjEzLTEuMTguMjMtLjMxLjA5LS41Ny4xOS0uNzYuMzFzLS4zMy4yNS0uNDEuNGMtLjA5LjE1LS4xMy4zMS0uMTMuNDh6bTYuMjktMy42M2gtLjk4di0xLjJsMS4wNi0uMDcuMi0xLjg4aDEuMzR2MS44OGgxLjc1djEuMjdoLTEuNzV2My4yOGMwIC44LjMyIDEuMi45NyAxLjIuMTIgMCAuMjQtLjAxLjM3LS4wNC4xMi0uMDMuMjQtLjA3LjM0LS4xMWwuMjggMS4xOWMtLjE5LjA2LS40LjEyLS42NC4xNy0uMjMuMDUtLjQ5LjA4LS43Ni4wOC0uNCAwLS43NC0uMDYtMS4wMi0uMTgtLjI3LS4xMy0uNDktLjMtLjY3LS41Mi0uMTctLjIxLS4zLS40OC0uMzctLjc4LS4wOC0uMy0uMTItLjY0LS4xMi0xLjAxem00LjM2IDIuMTdjMC0uNTYuMDktMS4wNi4yNy0xLjUxcy40MS0uODMuNzEtMS4xNGMuMjktLjMuNjMtLjU0IDEuMDEtLjcxLjM5LS4xNy43OC0uMjUgMS4xOC0uMjUuNDcgMCAuODguMDggMS4yMy4yNC4zNi4xNi42NS4zOC44OS42N3MuNDIuNjMuNTQgMS4wM2MuMTIuNDEuMTguODQuMTggMS4zMiAwIC4zMi0uMDIuNTctLjA3Ljc2aC00LjM3Yy4wOC42Mi4yOSAxLjEuNjUgMS40NC4zNi4zMy44Mi41IDEuMzguNS4zIDAgLjU4LS4wNC44NC0uMTMuMjUtLjA5LjUxLS4yMS43Ni0uMzdsLjU0IDEuMDFjLS4zMi4yMS0uNjkuMzktMS4wOS41M3MtLjgyLjIxLTEuMjYuMjFjLS40NyAwLS45Mi0uMDgtMS4zMy0uMjUtLjQxLS4xNi0uNzctLjQtMS4wOC0uNy0uMy0uMzEtLjU0LS42OS0uNzItMS4xMy0uMTctLjQ0LS4yNi0uOTUtLjI2LTEuNTJ6bTQuNjEtLjYyYzAtLjU1LS4xMS0uOTgtLjM0LTEuMjgtLjIzLS4zMS0uNTgtLjQ3LTEuMDYtLjQ3LS40MSAwLS43Ny4xNS0xLjA4LjQ1LS4zMS4yOS0uNS43My0uNTcgMS4zem0zLjAxIDIuMjNjLjMxLjI0LjYxLjQzLjkyLjU3LjMuMTMuNjMuMi45OC4yLjM4IDAgLjY1LS4wOC44My0uMjNzLjI3LS4zNS4yNy0uNmMwLS4xNC0uMDUtLjI2LS4xMy0uMzctLjA4LS4xLS4yLS4yLS4zNC0uMjgtLjE0LS4wOS0uMjktLjE2LS40Ny0uMjNsLS41My0uMjJjLS4yMy0uMDktLjQ2LS4xOC0uNjktLjMtLjIzLS4xMS0uNDQtLjI0LS42Mi0uNHMtLjMzLS4zNS0uNDUtLjU1Yy0uMTItLjIxLS4xOC0uNDYtLjE4LS43NSAwLS42MS4yMy0xLjEuNjgtMS40OS40NC0uMzggMS4wNi0uNTcgMS44My0uNTcuNDggMCAuOTEuMDggMS4yOS4yNXMuNzEuMzYuOTkuNTdsLS43NC45OGMtLjI0LS4xNy0uNDktLjMyLS43My0uNDItLjI1LS4xMS0uNTEtLjE2LS43OC0uMTYtLjM1IDAtLjYuMDctLjc2LjIxLS4xNy4xNS0uMjUuMzMtLjI1LjU0IDAgLjE0LjA0LjI2LjEyLjM2cy4xOC4xOC4zMS4yNmMuMTQuMDcuMjkuMTQuNDYuMjFsLjU0LjE5Yy4yMy4wOS40Ny4xOC43LjI5cy40NC4yNC42NC40Yy4xOS4xNi4zNC4zNS40Ni41OC4xMS4yMy4xNy41LjE3LjgyIDAgLjMtLjA2LjU4LS4xNy44My0uMTIuMjYtLjI5LjQ4LS41MS42OC0uMjMuMTktLjUxLjM0LS44NC40NS0uMzQuMTEtLjcyLjE3LTEuMTUuMTctLjQ4IDAtLjk1LS4wOS0xLjQxLS4yNy0uNDYtLjE5LS44Ni0uNDEtMS4yLS42OHoiIGZpbGw9IiM1MzUzNTMiLz48L2c+PC9zdmc+)](https://crossmark.crossref.org/dialog/?doi=10.1038/s41586-023-06647-8)

### Cite this article

Shanahan, M., McDonell, K. & Reynolds, L. Role play with large language models. *Nature* **623**, 493–498 (2023). https://doi.org/10.1038/s41586-023-06647-8

[Download citation](https://citation-needed.springer.com/v2/references/10.1038/s41586-023-06647-8?format=refman&flavour=citation)

- Received: 10 July 2023

- Accepted: 14 September 2023

- Published: 08 November 2023

- Version of record: 08 November 2023

- Issue date: 16 November 2023

- DOI: https://doi.org/10.1038/s41586-023-06647-8

### Share this article

Anyone you share the following link with will be able to read this content:

Sorry, a shareable link is not currently available for this article.

Provided by the Springer Nature SharedIt content-sharing initiative
