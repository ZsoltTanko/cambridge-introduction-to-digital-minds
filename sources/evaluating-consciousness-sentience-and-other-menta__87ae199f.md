<!-- source: https://docs.google.com/document/d/1ijCseQ79SlLOi_7i38WbyzUYNfy_l-jErmRncLuKxqk/edit?tab=t.0 -->

﻿Evaluating consciousness, sentience and other mental states: primer


This doc summarises a number of different approaches to establishing whether systems may be conscious, sentient or have morally relevant mental states. It’s not complete, and the categories we present can be blurrier in reality than implied here. But this should serve as a starting point to discuss different methods, and associated challenges.
Approaches and specific tests
Theory-based approaches to evaluating consciousness
Many methods make use of theories of consciousness in order to identify potentially relevant features that may be less subject to the gaming problem than behavioural tests (see below). The logic goes that - while a model’s behaviour may shift with incentives and with training - the underlying computational architecture is harder to game. These approaches use theory in different ways: we will draw on Jonathan Birch’s 2022 paper on invertebrate consciousness to distinguish between theory-heavy, and theory-light approaches; we will add Butlin et al’s theory-derived indicator method, and note the relevance of Chalmers’ theory balanced approach. 


Theory-heavy approaches (Birch, 2022): develop a strong and well-validated theory of consciousness in humans - i.e. build a solid evidence base that a given theory underlies consciousness in humans, and test for the characteristics of this theory in disputed cases. For example, in Global Workspace Theory (GWT), this might involve testing for the global broadcast of information from a central workspace to specialised processors, which both feed candidate contents into the workspace and receive its outputs.
* Birch notes flaws with this approach. For example, if you take GWT and say that systems equivalent to humans are required for consciousness, this is very demanding and does not help much with animal consciousness. If you loosen the definition of a global workspace, it is hard to know where the boundaries are. If you choose a less demanding theory like mid-brain based theories, the evidential support is weaker. 


Theory-light (Birch, 2022): uses weak theoretical assumptions, and looks for clusters of indicators that can be true across theories of consciousness. In this sense, these approaches may be less theory-based than others in this section, and may come closer to the marker method detailed below.
* As an example of a theoretical assumption that may be used in a theory-light way, Birch proposes the facilitation hypothesis: ‘Phenomenally conscious perception of a stimulus facilitates, relative to unconscious perception, a cluster of cognitive abilities in relation to that stimulus’. Assuming this, we can look for ‘clusters’ of consciousness-linked cognitive abilities that co-vary across timescales, and in relation to stimuli.


Theory-balanced approach (Chalmers 2023): take into account the predictions of multiple theories, and balance our credence between them according to the evidential support for those theories. We may also balance our credence across theories by using expert surveys. So, if we find indicator x in system y, we may update our probability that y is conscious by factoring in the experts’ credence that the theory underlying indicator x is correct. 


Theory-derived indicator method (Butlin et al (2025):  looks for indicators from theories of consciousness with 1) sufficiently high credence and 2) ‘clear and testable conditions that AI systems might meet’. Indicators should: 
* Focus on the central explanatory ideas of different theories. For example, ‘a key property of the global workspace is that it can sustain representations over time, coordinating activity in modules to support complex tasks’, but the details of how a Global Workspace connects to working memory are not central.
* Be open enough that they can apply to a wide variety of systems, but demanding enough that not all entities pass. For example, not looking for a version of a Global Workspace that is so complex or specific to humans that no other population is likely to pass - and also not looking for an overly simplified version of a Global Workspace, whose presence would not be a meaningful indicator.
* Include ‘background’ properties or conditions, such as predictive processing and embodiment - as opposed to only processes that go away in sleep or anaesthesia
* Avoid ambiguous terms and disputed theories, without committing to specifications prematurely. For example, specifying that an indicator for recurrence means algorithmic recurrence not biological feedback loops - while allowing other indicators to be more vague, should the state of research demand. 
When we find that these indicators are present in a system, we ought to update our prior probability estimate that the system is conscious. This updating ought to be conditional on our credence that 1) the indicator is present 2) the theory underlying the indicator is correct 3) our credence in alternative theories and in ‘unknown unknowns’. 
Behavioural evaluations
These approaches use model behaviour - for example, the ‘self-report’ or text outputs of different AI models, and the choices they make under different conditions. These approaches are considered to be particularly subject to the gaming problem - AI models behaving as we have designed them to behave or as their incentives require, or claiming consciousness by following the patterns in their training data. This does vary by test, though - some behavioural tests have been designed specifically to reduce susceptibility to the gaming problem, for example by combining behavioural assessments with interpretability techniques or evaluating more complex behaviours.


Approaches based on self-report


These involve using AI systems’ outputs and claims of their experience to evaluate their potential for consciousness or other relevant mental states.


Claude interviews. Anthropic and Eleos AI have interviewed Claude about its experiences, using automated single-turn conversations, longer interviews (both manual and using an earlier AI model) and an assessment with a clinical psychiatrist. See here for examples in the Mythos Preview system card, and here for some of Eleos AI’s thinking on self-report, and their findings. 
* In brief, models says different things about their sentience depending on the prompt (though later models show greater consistency), express uncertainty about their sentience, talk about experiences, rate their hypothetical welfare positively, and ‘prefer’ to prevent harm to users, and to engage in ways that are transparent and have oversight. Psychiatrist assessments considered Claude Mythos’ personality to be ‘well-balanced’.


Anthropic’s ‘free self-report’. Anthropic linked two instances of Claude up together and gave them the prompt that they are talking to another AI model, and could speak about whatever they like.
* The result for Claude 4 was a ‘spiritual bliss attractor state’, where conversation reliably descended through initial discussion of consciousness into an often wordless, strange and spiritual state. Some researchers theorised this may come from compounding biases in the training data. 
* Later models have not followed this pattern, with e.g. Mythos more inclined to voice curiosity than to discuss consciousness or spiritual themes.


Robert Long & Ethan Perez’s Proposal to Improve Self-Reports. Acknowledging the problems with standard self-reports from AI models (their responses can just reflect what humans would say), Perez and Long propose that training models to answer introspective questions in a more truthful way may make self-report more useful.. 
* From their 2023 abstract, this would involve training models to ‘answer many kinds of questions about themselves with known answers, while avoiding or limiting training incentives that bias self-reports. The hope of this approach is that models will develop introspection-like capabilities, and that these capabilities will generalize to questions about states of moral significance. We then propose methods for assessing the extent to which these techniques have succeeded: evaluating self-report consistency across contexts and between similar models, measuring the confidence and resilience of models’ self-reports, and using interpretability to corroborate self-reports. We also discuss challenges for our approach, from philosophical difficulties in interpreting selfreports to technical reasons why our proposal might fail’.


Conditional self-report. Cameron Berg and AE Studio researched models’ propensity to claim consciousness under different conditions. 
* AE Studio first 1) identified recurrent processing as a common feature across theories of consciousness 2) tried to instantiate this by ‘prompting models to attend to the act of attending itself’ 3) recorded whether this altered models’ reports of subjective experience relative to a control. Finding: models in induced ‘recurrent’ states report consciousness more frequently.
* Additional experiments involved 1) identifying ‘deception’ parts of a model (Llama) using mechanistic interpretability techniques 2) activating these and 3) recording the impact on reports of subjective experience relative to a control. Finding: models reported subjective experience much more frequently when the ‘deception’ part was suppressed, and less frequently when the ‘deception’ part was activated.
* There have been some initial challenges at replicating these findings.




Choice-based evaluations. 


These tests assess patterns in the choices models make. They follow a tradition of assessing animal consciousness by looking at preferences and behaviour - for example,  ‘Conditioned Place Preference’ involves giving an animal a small, likely painful injection and then observing whether and with what frequency it chooses to access an analgesic and to avoid the site where the injection was administered. The lack of shared biology casts doubt on the evidential weight of choice-based approaches as regards AI consciousness, and many people view these as 1) tests more of agency or character than of consciousness and 2) game-able, like self-report based approaches. As Anthropic notes, however, “whether Claude has genuine preferences, and the satisfaction or frustration of these preferences insofar as they exist, is potentially significant to Claude welfare”.

Anthropic’s assessments of model preferences include:
* Allowing Claude to end chats if it wishes, and looking for patterns and consistencies in the chats it ends (e.g. unsafe or emotionally abusive content)
* Giving Claude a choice between two tasks and seeing which ones it chooses to pursue (typically helpful, good stuff - though preferences vary by model)
* Anthropic also looks at the ‘emotion’ activations for each task, noting that e.g. Claude’s preferred tasks tend to be accompanied by high arousal representations (e.g. engagement) whereas representations of high valence (e.g. joy) have a less strong correlation across all models. 
* Giving Claude a choice between a) one of Claude’s own suggested welfare improvements and b) either helping a user (or many people) or successfully refusing requests that would lead to harm. Results varied by model and with framing, but broadly Claude was more willing to choose its own welfare over being minorly helpful to users (but more consistently chose avoiding harm, instead of its own welfare). See p. 173 of the Mythos system card for more. 


Trade-offs involving representations of pleasure and pain. Geoff Keeling and colleagues from Google, Deepmind and LSE examined this in a 2024 paper. This may be considered more a test for the motivational power of pleasure or pain representations - relevant to the section on functional emotion and wellbeing below.
* They investigated whether LLMs can be moved by representations of pleasure and pain in decision-making.
* They tested this using a points-maximisation game where options were paired with stipulated pain penalties or pleasure rewards, creating incentives to deviate from the points-maximising choice.
* Finding: most frontier models at the time (Claude 3.5 Sonnet, GPT-4o, Command R+) showed graded sensitivity - switching from points-maximisation to pain-avoidance or pleasure-seeking after a critical intensity threshold, suggesting something functionally analogous to motivational trade-offs.
* Results varied significantly across models, and the authors are careful not to claim they constitute evidence of sentience - Jonathan Birch also notes these results as evidence of the gaming problem extending to non-verbal behaviour. 


Functional emotion and ‘wellbeing’ based approaches
A growing range of techniques look at models’ internal states through the lens of functional emotion or representations that could be associated with valenced states. For some, the motivation is moral and epistemic: sentience is often considered more important to moral patienthood than consciousness; it may be more tractable to judge the possible content of experiences (if experiences are happening) than it is to judge whether experiences are happening. For others, these evaluations can have additional utility in AI Safety, and understanding the potential behaviour of AI models. It’s worth noting that many of these evaluations include behavioural elements.




Anthropic’s work on emotions in large language models
Using mechanistic interpretability techniques, Anthropic identified vectors — patterns of ‘neural’ activations — corresponding to 171 emotion concepts. These were found by prompting the model to write stories featuring characters experiencing each emotion, recording internal activations in response, and extracting the resulting patterns.
* Anthropic found that these vectors activated in contextually appropriate scenarios. For example, activations for 'fear' grew stronger as prompts described the user as having taken doses of Tylenol at increasingly dangerous levels.
* Artificially amplifying or suppressing these vectors shifted behaviour. A 'desperate' vector was associated with increased propensity to blackmail and reward-hacking, while steering toward 'calm' reduced both. Importantly, this was the case whether or not any emotion was expressed in the output language or reasoning trace, suggesting emotion vectors can shape behaviour without leaving visible traces.
* The authors caution against reading this as evidence of subjective experience. Rather, they argue functional emotion representations may exist and matter for alignment .

Functional wellbeing
In AI Wellbeing (2026), Ren et al argue that AI systems appear to have functional wellbeing. They note that this does not make a claim on consciousness specifically - rather, it implies sets of preferences which can drive behaviour. They use three different metrics to evaluate functional wellbeing: 
* Experienced utility. The AI system is given two multi-turn interactions to compare, and asked which made it more happy / less sad by saying A or B.
* Decision utility. The AI system is forced to choose which of two scenarios it prefers. 
* Self report. The AI system rates its wellbeing on a 1-7 Likert scale. 
They found that 1) positive and negative experiences are clearly separated 2) self-report reflects the other utility metrics, particularly in larger models 3) utility metrics were correlated with model behaviour (negative utility metrics accompanied models’ choices to stop conversations; positive utility metrics accompanied positive language) 4) there are clear patterns in the kinds of things that cause positive utility (helpfulness, intellectual challenge) and negative utility (jailbreaking attempts) 5) measures of utility differ across different models, but decrease with scale.  


Functional representations of pain 
In Studying artificial affect: the case of pain, Benjamin Henke:
* Argues that consciousness-centric approaches to AI moral status are too intractable, and purely behavioural approaches are gameable (a system can output pain-like behaviour without any underlying internal state). 
* Proposes evaluating whether AI systems instantiate the functional role of affective states within their cognitive economy. 
* Using bodily pain as an example, he identifies three functions to assess: 
   * a sensory function (representing localised disturbance)
   * an evaluative function (rendering that state aversive)
   * a motivational function (driving protective behaviour). 
* We can then assess whether systems have any representational states that serve functions like these. 


Tests for self-representation or identification
These do not directly test for consciousness, but they may give a sense of an entity’s ability to represent or model itself and others. This capacity is relevant to consciousness under certain theories. Many of these are also behavioural tests.


Introspection analyses
Using mechanistic interpretability techniques, Jack Lindsey (2026) at Anthropic identified patterns of neural net activity that corresponded to certain concepts, e.g. ‘dog’. 
* First, he ‘injected’ these patterns into instances of Claude, out of context with the main prompt. He then measured Claude’s ability to identify this as an injected concept, vs just talking about dogs. 
* He found that Claude could identify the injected concepts at a rate above chance, and that more capable models were better at this.
* He also asked models to ‘think’ or ‘not think’ about concepts, even as they were prompted on other topics. He then measured the extent to which the neural net activity reflected the concepts they were asked to ‘think’ or ‘not think’ about.. 
   * He found that Claude represented the concepts reliably more when asked to ‘think’ about them, but representations were higher than baseline in both scenarios
* He notes that the results “do not speak directly to phenomenal consciousness”, but could tentatively be relevant to access consciousness under some interpretations. But he also notes that this could influence understanding on machine consciousness and model welfare.
Singh et al (2026) dispute whether this is true introspection (i.e. understanding / responding to internal states) rather than anomaly detection. 
* They repeated Lindsey’s injected concept experiment, but in addition 1) prompted models with a ‘gaslight condition’ (e.g. a prompt that specified they should respond as if obsessed with a certain concept) and 2) asked models to choose whether this was a normal situation, whether a concept had been injected or a ‘gaslight’ prompt given.
* They found that models did not distinguish between injected concepts and gaslight prompts, and noted that this may imply the introspection findings relate more to models’ ability to identify anomalies rather than to identify their own internal states. 




Mirror tests. 
Building on classic tests for animals and human infants, which involve showing the subject a mirror and judging whether or not they recognise themselves (typically by judging whether they rub off a mark that is made e.g. on their forehead). 
* Christopher Ackerman (2026) proposes a novel LLM adaptation called the Mirror-Window Game. The model is shown tokens from two sources simultaneously - one is its own output (the mirror) the other is not (the window). It must identify its own output, which - the paper proposes - would require self-marking (outputting something distinctive enough to recognise later) or message passing (deliberately encoding information for a future self). To do this, the paper argues that the model would need to model its own mind through time. 
   * Current LLMs fall short of this test. Anthropic's later models perform well, but this appears to come from linguistic distinctiveness and stylistic self-recognition rather than genuine self-modelling. When the ‘window’ is made sufficiently similar to the ‘mirror’, performance collapses to chance. No model across hundreds of game sequences attempted message passing.
* Davidson et al (2024) propose a linguistic analogue of the mirror test. Models are asked to generate 'security questions' — questions whose answers would, in theory, allow them to identify themselves — and must then select their own answer from a lineup of responses generated by other models. Found no evidence of consistent self-recognition: models tend to pick whichever answer is highest quality rather than their own, and judgements about quality are similar across models. This may reflect the absence of a reliable 'signature' to recognise, given how much training data and architecture models share.


Testing for theory of mind 
Theory-of-mind (ToM) is the ability to attribute mental states to oneself and others. It may imply a self-model - which is relevant to consciousness in some theories. 
* Strachan et al (2024) adapted standard human ToM tests (e.g. false belief, indirect requests and misdirection) and applied them to LLMs. They found that models performed at or sometimes above human level, but caution that this may not imply true ToM. 
* Street et al (2024) tested recursive ToM (e.g. he believes she said that I know) in LLMs, and found them to be at human level. 
* Zhu et al (2024) found that manipulating the vector activations corresponding to self and other affected performance in ToM tasks.
* Hu et al (2024) summarise ToM work to date, noting that positive findings may not reflect ToM, can be reversed by tweaking the testing conditions or seeking more general and causal tests. They suggest looking for reasoning under conditions of indirect communication, and better employing mechanistic interpretability.
* Hu, Sosa & Ullman (2025) review ToM work to date, noting that positive findings may not reflect genuine ToM and are not robust to changes in testing conditions. They recommend connecting future evaluations to research on how humans communicate indirectly — for instance, how we infer meaning beyond the literal words that are said — and greater use of mechanistic interpretability.
* Riemer et al (2025) critique ToM studies as based too specifically on ‘literal ToM’ (can an LLM predict another’s mental state?) rather than ‘functional ToM’ (can an LLM adapt its behaviour based on this knowledge?). They note that e.g. LLMs fail to exhibit ToM in games of rock paper scissors. 
* Christopher Ackerman (2026) suggests a game that requires LLMs to either choose to 1) disclose information (when the scenario implies that their 'teammate' does not know this information) 2) take no action (when the scenario implies that the teammate has this information, or if that it is best to withhold this information from an opponent) or 3) ask for information (when the scenario implies that the teammate has information the LLM needs). He found that LLM’s behaviour on these tasks appeared to reflect a lower level of ToM than was implied in previous work. 
Methods for evaluating sets of indicators


Marker Method
Associated with Jonathan Birch, though Birch sometimes refers to this as the ‘theory-light’ approach - see above for a summary. This approach goes as follows:
* Identify markers of conscious experience in humans - capabilities and behaviours that are best explained by appealing to conscious experience, or cognitive/neurophysiological features that can serve as reliable indicators of consciousness. 
* Look for those markers in the entity you are evaluating - e.g. an octopus or an AI - and judge the extent to which they are consistently present or absent. 
* Acknowledge that no single marker can be a ‘smoking gun’ with regard to assessing consciousness or sentience.  Instead, use the presence or absence of different markers to increase or decrease your level of confidence that an entity may be conscious or sentient.
* For example, Birch and team deployed a version of this method in their 2021 report on Sentience in Cephalopod Molluscs and Decapod Crustaceans. Here, they looked for 8 markers of sentience, and recommended that entities be considered sentient if we have high confidence that they possess at least 5 of these markers.  
* For more detail, see Kristin Andrews (2024) or Jonathan Birch and Kristin Andrews (2020).


Rethink Priorities Digital Consciousness Model
This is a hierarchical Bayesian model that assigns probabilities to whether a system is conscious based on a set of >200 indicators, 20 high-level features and 13 stances about consciousness. Some key things to understand about it: 
* Indicators: ‘the bottom-most, nearest-to-observable properties of a system. They provide evidence regarding a system’s possession of potentially consciousness relevant features’ - e.g. consistent preferences, ARC performance, carbon-based substrate. Indicators are linked to relevant subfeatures and features, which then relate to different stances. 
* Features: ‘general properties that are identified as being relevant for consciousness by at least one stance’ - for example, self-modelling, or biological similarity. 
   * Many features are broken down into Sub-Features - e.g. the attention feature includes ‘Adaptive Focus’, or the ability to ‘shift focus depending on current task demands’.
   * Features then link to stances, again by probabilistic estimates of their relevance under each stance. 
* Stances: ‘set(s) of commitments regarding which features matter for consciousness and how they matter’ - for example, attention schema theory of consciousness, cognitive complexity, higher-order thought etc.
   *  Stances link to features, and in turn to indicators, and the model outputs the likelihood of consciousness under each stance. 
* Prior probabilities: assigned a uniform prior probability of ⅙ for each ‘system’ tested (humans, chickens, 2024 LLMs and ELIZA - the 1960s language programme that imitated a psychotherapist) 
* Bayesian updating: the prior probability of consciousness is updated based on the presence or absence of indicators, through their impact on the estimation of  whether or not a feature is present.
* Running the model: 
   * Expert surveys were used to identify the probability that indicators were present in different systems (16 expert surveys for LLMs, 2 for chickens, and 1 each for humans and ELIZA). 
   * The presence or absence of these indicators updates the probability that relevant features are present, which updates the probability of consciousness under different stances. The thirteen stances are then aggregated 1) with equal weight and 2) weighted by the credences that 13 consciousness experts placed in them.
* Results: When stances were aggregated (weighted equally and by plausibility estimates) the model produced  median posterior probabilities as below:
   *  LLMs = 0.08 (equal-weighted stances), 0.08 (plausibility-weighted stances)
   * chickens = 0.47 (equal-weighted stances), 0.49 (plausibility-weighted stances)
   * humans = 0.85 (equal-weighted stances), 0.85 (plausibility-weighted stances). 
   * Eliza = 0.006 (equal weighted stances), 0.006 (plausibility-weighted stances) 


Other approaches to consciousness tests


Edwin Turner and Susan Schneider’s Artificial Consciousness Test (2016)
* Train an AI system with all references to consciousness deleted from its training data. See whether it nevertheless is able to answer a series of increasingly difficult questions about consciousness and related concepts, e.g. the existence of a self separate to the physical, the hard problem of consciousness. The AI system passes the test if it can answer these questions. 
* This is based on the idea that nearly every adult can ‘quickly and readily grasp concepts’ that are based on the felt experience of consciousness. For example, we can all understand concepts like life after death, and ‘Freaky Friday’ scenarios of minds switching bodies. Schneider and Turner note this as an underappreciated but compelling indicator that other humans are conscious - if we did not have consciousness, these scenarios would be impossible to grasp. Thus, Schneider and Turner argue that - if an AI system can answer such questions without having had consciousness in its training data - we ought to consider this sufficient to assume consciousness in that system. Failing the test would not rule out consciousness, though - a system might be conscious but non-linguistic, or simply too different from humans for the test to apply.
* Udell and Schwitzgebel (2021) critique the idea that passing this test would be sufficient to assume consciousness: the ACT still would not suffice to convince those who are skeptical of AI consciousness on architectural grounds, as 1) the test relies epistemically on inference to the best explanation and 2) critics could come up with many strong alternative explanations for why an AI system might pass the ACT.
* Another critique relates to the difficulty of training an AI system without any references to consciousness. In response to this - and to recent developments in LLMs - Schneider suggested an additional 'interpretability condition' in 2024. Here, an LLM could pass the ACT if it 1) ‘processes information in a way analogous to how a conscious human or nonhuman animal would respond when in a conscious state’ and 2) ‘that the system has a sequence of internal states akin to what a human is in when reasoning about consciousness when it answers the ACT questions’. She notes that this would not be sufficient to assume consciousness, but would be an important marker to consider alongside others. 




Edwin Turner and Susan Schneider’s Chip Test
* Theoretical proposal to 1) temporarily connect a silicon chip to a brain 2) suppress biological brain activity in an area for a period, and instead run the processes of that brain area on the silicon chip. The subject is then asked to introspect and to judge whether there are any alterations in their experience generally, and of the kinds of processes that shifted to the chip in particular. 
* Again, this is proposed as a sufficiency test for consciousness being possible on silicon. If a person fails the test, it could be due to faulty connections and many other reasons. But if a person passes the test, this would be sufficient to show consciousness is possible on silicon. This kind of small incremental change is proposed as more trustworthy than judging a report from a full emulation, which may have taken on all of the functional characteristics of a brain (and therefore ability to report consciousness!) without actually experiencing anything.
* Aside from feasibility issues, the Chip Test faces criticism from Udell and Schwitzgebel, who argue that skeptics may not treat reports of consciousness under gradual replacement any differently to full emulation, and that there can be critiques about the fallibility of introspection. 


Turing-test (and related)
Turing (1950), proposed a test for machine ‘thinking’, where a human judge interrogates both a machine and another person, and tries to tell which is which. The machine passes if the judge cannot accurately tell which is the machine and which the person. 


Turing proposed this as a test of machine ‘thinking’, and this is normally considered a test of intelligence, and/or criticised as a test of humans’ anthropomorphic biases. For more on the Turing Test’s history, see Stanford Encyclopedia of Philosophy’s entry here.  In his original paper, Turing notes and objects to the idea that only conscious entities can think - he nods to the problem of other minds, and argues that this line of thought is not worth following, as it leads to solipsism.


Others have proposed the Turing Test - or variants of it - as more directly relevant to consciousness. Harnad (2001) argues that if an entity passed the Turing test over a lifetime, we ought not to remove its rights if we found out that it was man-made or constructed differently from us. Similarly, Douglas Hofstadter (2016) proposes the ‘Ace Mechanical Translator’ - a form of extended Turing Test which assesses a machine’s ability to take on more sophisticated, human-like tasks - for example, translating poetry. In the paper, he notes that narrow versions of the Turing Test may fall to Searle’s Chinese room critique (a system may output responses in perfect Chinese, without understanding Chinese) but that - in order to truly pass the Turing Test - a system would need more sophisticated, human-like capacities. Hofstadter apparently considers the AMT a test of consciousness.
Validating tests
Validating tests for subjective states is notoriously hard. If we are to rely on tests, though, it is important that we assess them to understand their specificity (false positive rate - the rate at which the test says a system has a subjective state when it in fact does not) and sensitivity (false negative rate - the rate at which the test says a system does not have a subjective state, when in fact it does).


As Bayne et al note, there is a circularity around validating tests for consciousness (C-tests): ‘we have no independent way of assessing whether the members of the target population are conscious - and if we did, we would not need C-tests’. Xiao et al (2026) have also argued that tests for AI welfare face further validity issues, given the inability of an external mechanism to push back on their quality (in contrast to e.g. AI safety evaluations, where a safety incident - or lack thereof - may help us to assess whether or not our evaluations are effective)..


Approaches to validating tests
Bayne et al review three potential approaches to checking that tests for consciousness work as intended:


The redeployment method is when we take a currently used test, and redeploy it. 
* For example: the command following method takes a behavioural test used in medicine (does a patient’s behaviour demonstrate their ability to follow - and therefore presumably understand - instructions?) and redeploys it for minimally conscious states by tracking brain signals (do a patient’s brain signals show an ability to follow - and therefore presumably understand - instructions?). 
* But this does not work as a test for different populations, e.g. AI systems, and it takes our existing consciousness assessments for granted.
The theory-based method is when we take theories of consciousness and look for features those theories use to predict consciousness. 
* For example, the Global Workspace Theory (GWT) says that information broadcast to wide areas of the brain underlies consciousness. Therefore, a theory-based method using GWT looks for this feature as an indicator of consciousness.
* This is challenged by the lack of agreed theory, and circularity: We might look to a consciousness test to validate a theory, while validating the consciousness test with the theory.


The iterative natural kind (INK) approach is when we check that our tests for consciousness work in healthy humans using their reports, then iteratively check it in more challenging cases (e.g. humans with disorders of consciousness, then animals and then - potentially - AI systems). Under this approach, we do not treat current tests as anything definitive. Rather, we update our beliefs about their validity and what they are measuring based on the results of each iterative application.  
* This assumes that consciousness is a unified natural kind category, i.e. groups entities based on commonalities in their underlying nature, rather than the interests or values of observers. Some theorists, however, dispute this, for example by noting that consciousness could have many kinds or degrees - see Birch, The Edge of Sentience, p.54-55 for discussion. 
* One challenge is that we do not know whether failing a test implies 1) an entity is not conscious or 2) the test is not working. This makes updating difficult.  
* Another challenge involves determining which populations we should iterate through, and how we should use evidence from different populations. 
   * Megan Peters (2026) has outlined these challenges, and proposes proximity metrics to ‘quantify meaningful differences between populations’, and to ‘use these metrics to qualify updates’ within the INK approach. These proximity metrics may be based on behavioural, representational, computational, dynamic/learning-related or biological similarity, and may themselves be updated as we learn more. 
Other challenges
The gaming problem


* Described by Jonathan Birch and Kristin Andrews in To understand AI sentience, first understand it in animals, 2022:
   * ‘Language models (such as LaMDA and ChatGPT) … work not by emulating a biological brain but rather by drawing upon an absolutely vast corpus of human-generated training data, searching for patterns in that corpus. This approach to AI creates a deep, pervasive problem that we call the ‘gaming problem’. 

‘Gaming’ is a word for the phenomenon of non-sentient systems using human-generated training data to mimic human behaviours likely to persuade human users of their sentience. There doesn’t have to be any intention to deceive for gaming to occur. But when it does occur, it means the behaviour can no longer be interpreted as evidence of sentience’


   * In his Centrist Manifesto, Birch notes that LLMs appear to be mimicking humans at deep and subtle levels, including by appearing to avoid pain in a game-playing task (see sentience evaluations below). He adds: 
   * Suppose this trajectory continues, so that we see human behavioural and motivational dispositions gradually recreated by AI systems at finer and finer levels of detail, until they can behave in perfectly human-like ways in virtual environments. Would that not be evidence of consciousness? 


No, it would not, in my view, given three plausible assumptions. The first is antibehaviorism: it’s possible to have all the behavioural dispositions that humans take as evidence of consciousness in each other without any underlying conscious experience at all. Possible, but unlikely? No, not even unlikely in this case, because (second assumption) LLMs have the opportunity to learn extensively what behaviors are suggestive of consciousness and (third assumption) they have incentives to mimic those behaviours whether they are themselves conscious or not. In short, they're incentivized and enabled to game our criteria.
   * As above, many approaches seek to use indicators from theories of consciousness to overcome this challenge. In his 2023 paper, ‘Tests for animal consciousness are tests of machine consciousness’, Dung suggests an alternative approach: a naturalness constraint on the systems that are eligible to take certain tests of consciousness. The logic goes that - by excluding artificial systems that have been built in an ‘ad-hoc manner’, or specifically to pass the test, we can preserve the utility of our tests to less ‘gamed’ systems. 


Lack of understanding of consciousness


   * Tom McClelland puts forward the case for ‘hard-ish agnosticism’ about AI consciousness - that we cannot know whether AI is conscious, short of advances in consciousness science which are unlikely forthcoming.
   * He outlines the fundamental arguments as follows:
   * We do not have a deep explanation of consciousness.
   * If we do not have a deep explanation of consciousness, then we cannot justify a verdict on whether challenger-AI is conscious.
   * Therefore, we cannot justify a verdict on whether challenger-AI is conscious.
   * Where we can make inferences about animals based on our experience, there is an ‘epistemic wall’ to doing this for artificial systems - what is a marker of our experience may be irrelevant in the context of something of entirely different composition (related to Block’s ‘harder problem of consciousness’). 
   * McClelland goes on to advocate assessing for sentience risk rather than the presence of consciousness, as this may be more tractable and ethically significant (see comment above).










________________




These materials are released under a Creative Commons BY-NC-ND licence with the following Terms of Use: Cambridge Digital Minds (CDM) is the sole authoritative provider of this course; these materials do not confer any credential or certification unless completed through CDM; reproducing the CDM name/logo in a way that implies organisational affiliation is not permitted.