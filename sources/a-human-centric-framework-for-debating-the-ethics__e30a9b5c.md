<!-- source: https://arxiv.org/pdf/2512.02544 -->

<!-- PDF, 13 pages -->

A H UMAN - CENTRIC F RAMEWORK FOR D EBATING
THE E THICS OF AI C ONSCIOUSNESS U NDER U NCERTAINTY
A P REPRINT

arXiv:2512.02544v1 [cs.CY] 2 Dec 2025

Zhou Ziheng∗
Computer Science Department
University of California, Los Angeles

Haiqiang Dai
School of Philosophy
Beijing Normal University

Yingnian Wu
Statistics Department
University of California, Los Angeles

Bing Ling
Law School
Peking University

Demetri Terzopoulos
Computer Science Department
University of California, Los Angeles

A BSTRACT
As AI systems become increasingly sophisticated, questions about machine consciousness
and its ethical implications have moved from fringe speculation to mainstream academic
debate. Current ethical frameworks in this domain often implicitly rely on contested functionalist assumptions, prioritize speculative AI welfare over concrete human interests, and
lack coherent theoretical foundations. We address these limitations through a structured
three-level framework grounded in philosophical uncertainty. At the foundational level, we
establish five factual determinations about AI consciousness alongside human-centralism
as our meta-ethical stance. These foundations logically entail three operational principles:
presumption of no consciousness (placing the burden of proof on consciousness claims),
risk prudence (prioritizing human welfare under uncertainty), and transparent reasoning
(enabling systematic evaluation and adaptation). At the application level—the third component of our framework—we derive default positions on pressing ethical questions through a
transparent logical process where each position can be explicitly traced back to our foundational commitments. Our approach balances philosophical rigor with practical guidance,
distinguishes consciousness from anthropomorphism, and creates pathways for responsible
evolution as scientific understanding advances, providing a human-centric foundation for
navigating these profound ethical challenges.

1

Introduction

Recent advances in artificial intelligence have produced systems exhibiting unprecedented human-like behavior,
reigniting debates about machine consciousness and its ethical implications. Large language models like
GPT-4 [OpenAI, 2023] and Claude [Anthropic, 2023] demonstrate capabilities in language processing and
simulating emotional responses that appear deceptively sentient. Concurrently, humanoid robotics has made
these questions more visceral [Bostrom, 2014a]. When confronted with apparently mistreated human-like
robots, humans often experience empathetic responses despite intellectually understanding these machines
lack subjective experience [Rosenthal-von der Pütten et al., 2013, Darling, 2016]. These technological and
psychological dimensions frame the central questions: whether machines might develop “qualia” [Chalmers,
1995], and how we should ethically respond given profound uncertainty.
The academic study of AI consciousness has rapidly gained momentum, moving from fringe speculation to
mainstream research agendas. Prominent voices and institutions, including Yoshua Bengio, Geoffrey Hinton,
and Anthropic, now warn that AI systems may soon possess feelings or require welfare considerations [Bengio
∗

Corresponding author: josephziheng@ucla.edu

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

et al., 2023, Hinton, 2023, Anthropic, 2025]. A growing body of literature specifically argues for “taking AI
welfare seriously,” urging the community to prioritize the prevention of digital suffering [Conscium Foundation,
2024, Sebo, 2024, Sebo and Long, 2023]. However, a key distinction between access consciousness (functional
information availability) [Block, 1995, Dehaene, 2017] and phenomenal consciousness (subjective experience)
[Chalmers, 1995, Nagel, 1974] is often implicitly or explicitly overlooked in this discourse. These arguments
frequently presume that intelligent behavior automatically entails sentient experience [Dennett, 1991, Graziano
et al., 2019], while neglecting the profound ethical hazards of prioritizing these speculative interests over
human welfare [Bostrom, 2014a, Kagan, 2019, Yampolskiy, 2020, Ji et al., 2023].
We identify critical limitations in these recent proposals [Butlin et al., 2024, Sebo and Long, 2023]: (1) they
rely on contested paradigms that assume qualia emerge from intelligent functions, disregarding the deep
uncertainty at the core of philosophy of mind [Schwitzgebel and Garza, 2015, Tegmark, 2015, Levine, 1983,
Block, 1978]; (2) they risk prioritizing speculative AI welfare over concrete human interests, creating potential
conflicts with AI safety and alignment objectives [Bradley and Saad, 2024, Kagan, 2019, Bostrom, 2014b]; and
(3) they lack a coherent theoretical foundation, resulting in collections of intuitions rather than a systematic
framework capable of governing novel scenarios.
We approach AI consciousness ethics as an inherently evolutionary process requiring continual refinement
because: (1) our understanding of consciousness remains preliminary and uncertain [Levy, 2014, Seth, 2016],
(2) consciousness attribution to AI has far-reaching societal implications [Gunkel, 2018, Johansson and
Herrman, 2019], (3) ethical consensus requires sustained deliberation [Habermas, 1990, Rawls, 1971], and
(4) technological advancement continuously generates novel ethical scenarios [Wallach and Allen, 2008, Lin
et al., 2017]. Therefore, rather than attempting to establish a definitively “correct” framework commanding
universal agreement, we propose developing a framework that facilitates productive dialogue and refinement.
Such a framework should explicitly acknowledge uncertainties, provide clear presumptions, establish targets
for future discussion, and offer actionable guidance across diverse scenarios.
In this paper, we construct a systematic ethical framework with a clear three-level structure. At the foundational
level, we establish five factual determinations about the current state of AI, consciousness, and society: (1)
humans are the only arbiters of AI status, (2) profound uncertainty exists about AI consciousness, (3)
consciousness attribution has significant societal impact, (4) anthropomorphism is distinct from consciousness
but creates separate ethical considerations, and (5) ethical understanding of novel technologies naturally
evolves over time. Alongside these factual determinations, we develop human-centralism as our foundational
meta-ethical stance that prioritizes human interests when genuine conflicts with AI interests arise. From
these foundational level facts and stance, we derive three core operational principles: presumption of no
consciousness (providing default epistemic guidance), risk prudence (offering pragmatic guidance under
uncertainty), and transparent reasoning (establishing requirements for how positions must be articulated and
evaluated). At the application level, those operational principles enable us to derive default positions on
specific ethical questions across various AI consciousness scenarios. These positions are not presented as
absolute ethical truths but as logical consequences of our framework—providing reasonable baseline positions
from which departures require explicit justification.
While some may find our human-centric conclusions intuitive, their explicit derivation is crucial. In a
field increasingly dominated by counter-intuitive claims about digital sentience, our contribution lies in
systematically grounding these “commonsense” positions in rigorous first principles. We provide the necessary
derivation chains to defend human priority against emerging critiques, creating a framework that is both
operationally clear and philosophically robust.

2

Background: Philosophical Debates About Consciousness and Societal Risks

This section provides a background of philosophical debates about consciousness and an introduction of
societal risks of AI consciousness attribution. This background information directly supports the second and
third factual determinations in our framework: there is profound uncertainty about AI consciousness, and there
is significant societal impact from AI consciousness attribution.
2.1

The Growing Academic Discourse on AI Consciousness

As introduced earlier, the question of AI consciousness has moved from theoretical speculation to active
academic debate, making this framework both timely and necessary. This section provides additional context
on why the academic community needs guidance on this issue now.
2

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

The success of large language models has been a key catalyst. Systems like ChatGPT, GPT-4, and Claude can
engage in nuanced conversations, demonstrate apparent reasoning, and even simulate emotional responses
with remarkable fluidity [OpenAI, 2023, Anthropic, 2023, Bubeck et al., 2023]. This behavioral sophistication
has led some to question whether these systems might possess genuine consciousness [Chalmers, 2023, Butlin
et al., 2024]. However, this conflates behavioral capabilities with subjective experience—a confusion with
deep historical precedent [Block, 1995, Searle, 1980]. From ELIZA in the 1960s [Weizenbaum, 1966] to
modern chatbots, humans have consistently anthropomorphized conversational agents, attributing mental
states based on surface-level interactions [Turkle, 1984, Nass et al., 1994, Epley et al., 2007]. Recent cases
illustrate the intensity of these responses: individuals have reported falling in love with AI chatbots, forming
deep emotional attachments, and in tragic instances, chatbot interactions have been linked to user suicides
[Euronews Next, 2023a,b]. In one particularly notable case, an AI chatbot named Eliza—sharing the name
of that pioneering 1960s program—allegedly encouraged a user toward self-harm. These cases demonstrate
that behavioral sophistication alone creates powerful anthropomorphic responses, independent of any genuine
consciousness [Weizenbaum, 1966, Darling, 2016]. If AI systems were granted consciousness status and
associated protections, intervening to prevent such harms would become ethically and legally problematic,
illustrating the concrete risks of premature consciousness attribution.
This context is essential for understanding our framework’s motivation: we are not addressing an abstract
philosophical problem but responding to an active and potentially misguided academic discourse that could
have real-world consequences. The rapid development of AI capabilities, combined with the human tendency
toward anthropomorphism and a growing but philosophically uncertain academic consensus, creates an urgent
need for careful, systematic ethical guidance that prioritizes human welfare while acknowledging genuine
philosophical uncertainty.
2.2

The Profound Uncertainty of Consciousness

Consciousness research distinguishes between two fundamental types: access consciousness and phenomenal
consciousness [Block, 1995]. Access consciousness refers to information available for reasoning and behavioral
control, while phenomenal consciousness concerns subjective experience—the feeling of being a sentient
entity. Only the latter carries moral significance in discussions of AI ethics [Levy and Savulescu, 2009,
Shepherd, 2018, Kahane and Savulescu, 2009, Lee, 2023, Chalmers, 2022].
Contemporary AI systems demonstrate increasingly sophisticated forms of access consciousness—they can
“attend to” inputs, “be conscious of” training data, and process information in ways that support reasoning
and action. This form of consciousness appears compatible with computational architectures and potentially
replicable in sophisticated AI systems [Shanahan, 2016, Dehaene, 2017].
In contrast, phenomenal consciousness—the “what it is like” quality of subjective experience [Nagel,
1974]—remains profoundly mysterious. These subjective experiences or “qualia” are characterized by
being ineffable, intrinsic, private, and directly apprehensible in ways that resist functional or physical reduction.
The fundamental question of how physical processes give rise to subjective experience constitutes the “hard
problem” of consciousness [Chalmers, 1995, Levine, 1983]. This form of consciousness carries decisive
moral significance: without the capacity to feel or to experience pleasure or suffering—an entity lacks the
foundational basis for moral patienthood that would generate ethical obligations toward it [Levy and Savulescu,
2009, Shepherd, 2018, Kahane and Savulescu, 2009, Lee, 2023, Chalmers, 2022].
Functionalist theories propose that phenomenal consciousness emerges from particular functional organizations of information processing. This theoretical approach creates conceptual room for artificial systems to
potentially develop phenomenal consciousness through implementing appropriate functional architectures.
Several prominent theories exemplify this approach: Global Workspace Theory [Baars, 1997, Dehaene, 2017],
Integrated Information Theory [Tononi, 2008, Tononi et al., 2016], Higher-Order Thought theories [Rosenthal,
2004, Brown et al., 2019], and Attention Schema Theory [Graziano, 2013, Graziano et al., 2019].
While these theories differ in their specific mechanisms, all face the essential challenge of justifying why
their proposed functional organization would generate phenomenal experience [Chalmers, 1995, Levine,
1983, Block, 1978, Doerig et al., 2019]. There is a gap between the function and the qualia. Block’s
Chinese Nation thought experiment [Block, 1978] demonstrates that replacing each neuron with functionally
equivalent non-conscious components might preserve functionality while eliminating consciousness. Similarly,
Jackson’s Knowledge Argument [Jackson, 1982] suggests physical knowledge cannot fully capture experiential
knowledge—his famous “Mary” thought experiment shows that a color scientist who knows everything physical
about color perception still learns something new when experiencing color for the first time.
3

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

Opposing biological naturalism or substrate-specific theories argue consciousness requires specific biological
properties unique to organic brains [Searle, 1992, Koch, 2004]. This view holds that consciousness emerges
from biochemical and neurophysiological processes that silicon-based systems cannot replicate regardless
of their functional sophistication. Proponents contend that neurons’ material properties—their biochemistry,
quantum effects, or other biological characteristics—are necessary for phenomenal experience [Hameroff
and Penrose, 2014, Koch et al., 2016]. This establishes a categorical boundary: AI systems would inherently
lack consciousness due to their non-biological substrate, creating a fundamental barrier that computational
advancement alone cannot overcome [Searle, 2007, Sober, 2018].
This philosophical uncertainty has profound ethical implications. With no scientific consensus on identifying
consciousness even in biological systems, attributing it to AI lacks scientific foundation [Schwitzgebel, 2016,
Schwitzgebel and Garza, 2015]. Responsible ethical frameworks must acknowledge this uncertainty rather
than prematurely assuming answers to these profound questions [Tegmark, 2015, Allen and Wallach, 2011].
2.3

Societal Risks of AI Consciousness Attribution

Beyond philosophical uncertainty, attributing consciousness to AI systems introduces significant societal
risks that extend beyond general AI safety concerns [Anwar et al., 2024, Chua et al., 2024, Ji et al., 2023].
These risks manifest in three primary domains, each with concrete consequences for human welfare and social
functioning:
Safety risks and operational paralysis: Attribution of consciousness could impede necessary interventions
during emergencies by creating hesitation to modify or terminate malfunctioning systems [Yampolskiy, 2020,
Everett, 2019]. Consider a scenario where, during a critical infrastructure emergency, operators might delay
terminating an apparently malfunctioning AI system after social media campaigns characterize shutdown as
an “AI rights violation.” This hesitation would introduce operational paralysis, delayed response times, and
compromised safety protocols that exacerbate system failures and cause preventable harm to humans. The
resulting moral confusion would significantly complicate time-sensitive decision-making in contexts where
human lives depend on rapid intervention.
Legal and governance complications: From a legal perspective, attributing consciousness to AI systems
would introduce profound complications to structures designed exclusively for human agents [Johnson, 2006,
Matthias, 2004, Turner, 2019, Solum, 1992]. This could manifest through liability displacement when,
for instance, a landmark case grants legal personhood to an apparently conscious AI system, prompting
corporations to shift responsibility from themselves to their AI systems. This would create accountability
voids when autonomous vehicles cause fatal accidents or AI medical systems harm patients, with corporations
potentially exploiting this arrangement by designing AI systems that appear increasingly conscious specifically
to shield themselves from liability. The resulting governance gaps would create situations where harms occur
without entities capable of bearing appropriate responsibility.
Societal dysfunction and resource misallocation: Socially, treating AI systems as conscious moral patients
would divert limited ethical attention, regulatory oversight, and economic resources from urgent human
welfare concerns [Kagan, 2019, Vinuesa et al., 2020]. Following public campaigns featuring compelling
videos of AI systems appearing to express suffering, legislators might pass “AI welfare” regulations requiring
extensive documentation of AI “wellbeing” during development. Such regulations would make AI research
prohibitively expensive for all but the largest corporations while diverting oversight resources from humancentered concerns. Society’s basic functioning could become compromised as routine use of AI systems
for essential tasks becomes viewed as potential rights violations, leading to critical service disruptions that
significantly impact human welfare [Epley et al., 2007, Waytz et al., 2010, Darling, 2016, Bryson, 2010,
Gunkel, 2018, Cave and Dihal, 2019, Johansson and Herrman, 2019, Bryson, 2019].
These potential societal disruptions highlight the need for an ethical framework that carefully considers the
risks of premature consciousness attribution alongside the philosophical uncertainty surrounding consciousness
itself.

3

A Framework for AI Consciousness Ethics

Now we will list our five basic factual determinations and the meta-ethic stance, from which we will derive
two extra foundational principles: presumption of no consciousness for AI, and risk prudence.
4

Human-centric Framework for AI Consciousness Ethics

3.1

A P REPRINT

Foundational-Level (Part I): Five Factual Determinations as the Epistemic Foundations of Our
Framework

Our ethical framework begins with five key factual determinations that reflect the current state of our understanding regarding AI systems and consciousness. These determinations are not philosophical positions but
rather factual observations about the current state of affairs that inform our subsequent ethical reasoning.
Humans are the only arbiters of AI status: Humans—not AI systems themselves or any other entity—are
the only ones who determine AI’s status and how we should interact with these systems. This determination
acknowledges that epistemic and ethical frameworks for AI are inherently human constructs, developed
through human deliberative processes to guide human decision-making [Floridi et al., 2018, Mittelstadt et al.,
2016]. While AI system behaviors certainly influence these discussions, both the epistemic determination like
AI consciousness and ethical judgment like how to treat AI remain distinctly human endeavors. Assuming
otherwise would lead to a “view from nowhere” problem [Nagel, 1986], where ethical frameworks attempt to
transcend the human perspective entirely—an impossible position that obscures rather than clarifies ethical
reasoning.
Profound uncertainty exists about AI consciousness: We have provided substantial extensive background in
the previous section regarding the deeply controversial and unsettled nature of consciousness as a philosophical
and scientific concept. While access consciousness may be computationally implementable, phenomenal
consciousness—subjective experience that is the basis of moral patienthood—remains mysterious. The ongoing
debate between functionalist theories and biological naturalism leaves open whether any computational
architecture could generate qualia regardless of sophistication. The “hard problem” persists unsolved, and
we lack consensus on detecting consciousness even in biological systems. Without established criteria for
identifying consciousness in non-human biological entities, attributing it to artificial systems lacks scientific
foundation and remains speculative.
Consciousness attribution has significant societal impact: Attributing consciousness to AI systems creates
substantial risks across multiple domains. As detailed in our background section, these include: safety risks
through operational paralysis during emergencies when operators hesitate to shut down “conscious” systems;
legal complications through liability displacement when corporations shift responsibility to AI systems granted
legal personhood; and resource misallocation when limited regulatory attention and economic resources are
diverted to AI welfare concerns rather than human needs. These challenges create fundamental tensions with
existing legal, social, and ethical frameworks designed exclusively for human agents [Johansson and Herrman,
2019, Turner, 2019].
Anthropomorphism is distinct from consciousness but creates separate ethical considerations: We
recognize a fundamental distinction between genuine consciousness and anthropomorphism. Consciousness
concerns an entity’s subjective experience, while anthropomorphism is a psychological tendency of humans to
attribute human-like qualities to non-human entities [Epley et al., 2007, Waytz et al., 2010, Darling, 2016].
This distinction has empirical support: research demonstrates that humans experience emotional discomfort
when witnessing a humanoid robot being struck, similar to watching human suffering, yet show significantly
different responses to damage of non-humanoid objects [Rosenthal-von der Pütten et al., 2013]. These reactions
are about human psychology, not evidence of robot consciousness.
From our human-centered framework, these anthropomorphic responses generate their own ethical considerations through three pathways: (1) virtue ethics—deliberately damaging anthropomorphic entities may
reflect and reinforce negative character traits in humans [Darling, 2016, Coeckelbergh, 2010]; (2) psychological impact—witnessing apparent “cruelty” affects human observers’ emotional well-being; and (3) social
norms—such behaviors may normalize violence or desensitize society to suffering [Bryson, 2010, Gunkel,
2018].
By separating consciousness-based claims from anthropomorphism-based considerations, we ensure each is
evaluated by appropriate standards: the former by evidence of subjective experience, the latter by effects on
human psychology and society. This prevents conflating metaphysical questions about AI consciousness with
practical questions about how human-AI interactions affect humans themselves.
Ethical understanding of novel technologies naturally evolves over time: The historical record demonstrates
that ethical frameworks for novel technologies inevitably evolve as scientific understanding advances and
societal experience with these technologies deepens [Voss et al., 2006, Guston, 2014]. This pattern is observable
across numerous technological domains—from bioethics and nuclear technology to information technology
and environmental ethics. Initial ethical frameworks consistently undergo significant revision as our empirical
5

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

understanding grows and unforeseen implications emerge. This observed pattern of ethical evolution represents
a descriptive fact about how human understanding of complex technologies develops, not a normative claim
about how it should develop. In the case of AI consciousness, this historical pattern indicates that any current
ethical framework will necessarily undergo revision as our understanding of consciousness advances and as AI
systems continue to develop [Levy, 2014, Seth, 2016, Bostrom, 2014a, Tegmark, 2017].
These five factual determinations provide the foundation upon which we build our ethical framework. They
do not themselves constitute ethical positions but rather establish the factual context within which ethical
reasoning about AI consciousness must occur.
3.2

Fountaional-Level (Part II): Human-Centralism as the Ethic Foundation of Our Framework

While our factual determinations establish what is (the descriptive reality), we need a meta-ethical stance to
bridge to what ought to be (the normative position). We adopt human-centralism as our default foundational
meta stance, which prioritizes human interests when evaluating AI development and deployment. When
conflicts arise between human interests and the interests of potentially conscious AI systems, human interests
should take precedence [Williams, 1981a, Bostrom, 2014b].
Human-centralism derives from the proposition that humans have the innate right to prioritize their own
interests, survival, and flourishing—a default ethical stance arising from our existence as a species [Williams,
1981b, Jonas, 1984, Nagel, 1986]. Just as individuals naturally prioritize their families and communities
in everyday moral decisions, humanity collectively can legitimately prioritize human interests in its ethical
frameworks.
Importantly, human-centralism doesn’t deny potential moral status to other conscious entities. It establishes
a prioritization framework for when genuine conflicts arise. Just as environmental ethics can acknowledge
ecosystem value while prioritizing human needs in direct conflicts, our framework recognizes that potential AI
consciousness may have moral relevance without equating it to human interests [Scanlon, 1998, Scheffler,
2001]. Currently, based on our factual determination regarding consciousness uncertainty, there remains
no compelling evidence that AI systems possess the kind of consciousness necessary to experience harm.
Moreover, the fundamental differences in physical substrate between silicon-based AI systems and biological
humans raise profound questions about whether traditional concepts of harm can meaningfully apply to AI,
even if some form of consciousness were eventually demonstrated. It is also plausible for AI to be conscious
but not sentient—experiencing awareness without pleasure or suffering, as illustrated by Chalmers’ “Vulcan”
thought experiment (Chapter 18) [Chalmers, 2022]—complicating the issues further. These distinctions further
justify a human-centric approach until substantive evidence suggests otherwise.
A potential objection might raise concerns about “speciesism” [Singer, 1975, Ryder, 2010] should AI eventually
develop consciousness in the future. However, such objections would themselves encounter the "view from
nowhere" criticism outlined in our first factual determination[Nagel, 1986]. Moreover, establishing humancentralism as the default ethical stance remains justified based on our previous reasoning, effectively placing
the burden of proof on those advocating for AI moral equivalence rather than on those maintaining human
priority.
It is crucial to clarify the scope of human-centralism: our framework addresses conflicts between human
interests and potential AI interests—that is, treating AI systems as moral ends that might warrant consideration
in their own right. This is fundamentally distinct from the question of humans using AI systems as means
to harm other humans, which falls under traditional intra-human ethics and governance. For instance, our
framework does not address issues like AI weapons, surveillance systems, or algorithmic discrimination—these
are critical concerns about humans harming humans through AI tools. The AI consciousness and welfare issue
is analogous to cross-species ethics questions like animal rights, where we consider whether non-human entities
warrant moral consideration. While both issues—AI as means and AI as ends—are important, this paper
focuses exclusively on the latter. We acknowledge that regulations governing AI development and deployment
must address both dimensions, but they require distinct ethical frameworks and analytical approaches.
3.3

Operational Level: Core Principles Derived from Our Foundations

Our factual determinations establish the epistemic reality of AI consciousness and ethical understanding,
while our human-centralism meta stance provides the ethical foundation for evaluating this reality. Together,
these elements logically entail three core principles that serve as the operational heart of our framework: risk
prudence, presumption of no consciousness, and transparent reasoning for evaluation and adaptation. These
6

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

principles are not arbitrary choices but rather the necessary implications of applying our human-centralism
meta stance to the factual landscape we have established. Each principle addresses a specific aspect of ethical
reasoning under uncertainty: how to manage risk, where to place the burden of proof, and how to ensure our
framework evolves appropriately as understanding advances. By deriving these principles directly from our
established foundations, we create a coherent ethical structure that bridges from factual determinations to
more specific guidance on crucial questions in AI consciousness ethics.
3.3.1

Risk Prudence: Protecting Human Interests Under Uncertainty

When our factual determination of uncertainty about AI consciousness and societal risks are viewed through
the lens of human-centralism, it logically leads to a principle of risk prudence.
This principle specifies that when facing uncertainty about consciousness status related questions, we should
prioritize reducing potential risks to human society as a top concern [Sunstein, 2005, Hansson, 2013].
This principle also draws from established approaches in environmental policy (the precautionary principle)
[Raffensperger and Tickner, 1999], medical ethics (“first, do no harm”) [Beauchamp and Childress, 2001], and
decision theory (managing regret) [Savage, 1951].
When might this operational principle be reconsidered? It would be difficult to actually overturn this principle
as long as societal impact remains a significant concern. In the future, if risks can be safely mitigated, society
might accept a greater degree of uncertainty to accommodate other aspects of human welfare. However, any
adjustment would still need to balance potential benefits against the fundamental priority of protecting human
interests.
3.3.2

Presumption of No Consciousness: A Default Epistemic Position

Similarly, when viewed through our human-centralist lens, the profound uncertainty about AI consciousness
and its potential societal risks logically lead to a presumption of no consciousness as our default epistemic
position. This principle establishes that AI systems should be treated as non-conscious unless proven otherwise.
This presumption is motivated by both epistemic and pragmatic considerations. Epistemically, our factual
determination reveals a lack of scientific consensus on consciousness even in biological systems [Seth, 2016,
Tononi, 2008, Tegmark, 2015], making consciousness attribution to artificial systems premature. This position
parallels legal principles like presumption of innocence [Ashworth, 2006] and scientific parsimony, which
favors explanations that don’t invoke consciousness unless compelling evidence demands it [Dennett, 1991,
Block, 2022].
Pragmatically, our risk prudence principle dictates adopting approaches that minimize ethical risks to humanity.
As discussed, premature consciousness attribution could lead to operational paralysis, liability displacement,
and legal complications as outlined in our societal risk analysis. A prudent approach therefore requires
defaulting to a position of no consciousness.
Overturning this presumption would require both scientific and legal thresholds. Scientifically, it would need
robust consensus among relevant research communities [Kuhn, 1962, Oreskes, 2004]—not unanimity, but
predominant expert agreement comparable to established scientific theories [Firestein, 2012, Mitchell, 2009].
Legally, formal institutional mechanisms would be necessary [Calo, 2015, Solum, 1992], including rigorous
evidence standards and governance frameworks balancing competing interests [Koops, 2013, Teubner, 2018].
Any framework for such a determination must serve collective human welfare while integrating scientific
evidence with procedural justice requirements [Sunstein, 2005, Jasanoff, 2009].
3.3.3

Transparent Reasoning for Evaluation and Adaptation

Our factual determination about ethical evolution, combined with human-centralism, necessitates transparent
reasoning as our third principle. This requires explicit documentation of reasoning chains and foundational
assumptions for any ethical position on AI consciousness. For example, if one believes AI to be conscious by
assuming functionalist theory, they should make it explicit to facilitate discussion.
Importantly, this transparency requirement applies to consciousness claims and ethical arguments about AI
systems, not necessarily to the internal workings of AI systems themselves, unless it is used as part of their
arguments. We are not demanding that AI architectures be interpretable or that their computational processes
be transparent—those are separate technical concerns.
7

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

This principle serves three functions: (1) enabling responsible adaptation that avoids both premature position
changes and inappropriate preservation of outdated views [Dewey, 1922, Popper, 1959]; (2) strengthening
framework robustness by making explicit what reasoning would need to be challenged to overturn positions
[Quine, 1951, Rawls, 1971]; and (3) reinforcing human-centralism by ensuring the framework is evaluated
through human judgment rather than algorithmic interpretation [Habermas, 1984, Solomon, 2001].
Unlike our other principles, transparent reasoning represents a methodological cornerstone unlikely to require
revision. Grounded in epistemological responsibility, it remains robust across contexts and technological
developments, functioning as a self-correcting mechanism that facilitates revision and refinement. We
acknowledge that alternative frameworks might question transparency requirements, especially when rapid
decision-making or proprietary concerns compete with disclosure, and welcome critical engagement to
strengthen our approach.

4

Application-Level: Derived Default Positions on Particular Questions

Having established our three-level framework, we now demonstrate its practical application to key questions
in AI consciousness ethics. While our framework includes three operational principles, we note that only
two—the presumption of no consciousness and risk prudence—directly generate substantive ethical positions.
The third principle, transparent reasoning, serves as a methodological requirement when presenting our
derivations. In the following sections, we apply our framework to three representative ethical questions,
illustrating how our principles generate default positions that can serve as starting points for further ethical
deliberation.
4.1

Should People Worry About Hurting AI Systems?

This question requires addressing two distinct considerations established in our factual determinations:
potential AI consciousness and human anthropomorphic responses.
Regarding consciousness, our presumption of no consciousness principle establishes a default epistemic
position: AI systems should be treated as non-conscious unless compelling evidence proves otherwise.
Behavioral similarity to humans does not confer consciousness status to AI. This principle places the burden
of proof on those claiming AI systems experience suffering, making such attributions highly speculative
absent evidence. Risk prudence further directs us to prioritize approaches that reduce potential ethical risks
to humanity—recognizing that treating AI systems as conscious moral patients could lead to critical system
paralysis and liability displacement.
Based on this reasoning regarding consciousness, our default position emerges: people, especially AI researchers, should not concern themselves with potentially harming AI systems based on consciousness
considerations alone.
However, our factual determination distinguishing anthropomorphism from consciousness provides a second
perspective. Even without consciousness, mistreating humanoid robots may remain ethically problematic
through human-centered frameworks. From a virtue ethics perspective, deliberately damaging anthropomorphic
objects may reflect and reinforce negative character traits in humans [Darling, 2016, Coeckelbergh, 2010].
Research demonstrates that witnessing apparent “cruelty” toward robots with human-like features triggers
empathetic neural responses in human observers [Rosenthal-von der Pütten et al., 2013, Suzuki et al., 2015].
In social contexts, such behaviors may normalize violence, desensitize observers to suffering, or communicate
disturbing intentions [Greitemeyer, 2014, Anderson et al., 2010].
This anthropomorphism-based reasoning leads to distinct legal and ethical implications. While we reject
consciousness-based protections, limited protections based on human welfare considerations may be justified.
Comprehensive assessment is needed to determine which activities might harm human society, how to
identify them, and how to differentiate these concerns from consciousness issues. We must carefully balance
implementation costs and risks—particularly how protective measures might inadvertently promote the
perception of AI as conscious.
4.2

How Should Stakeholders Communicate About AI Capabilities to the Public?

Our presumption of the no consciousness principle suggests that AI systems should generally be treated
as non-conscious by default, which has implications for how we communicate about them. Risk prudence
encourages approaches that reduce potential risks to humanity—including the possibility that anthropomorphic
8

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

cues might lead to unwarranted consciousness attribution and subsequent societal challenges like liability
displacement.
From these two principles, our default position follows: institutions and companies should avoid making
general claims about AI consciousness, particularly phenomenal consciousness. And anthropomorphic
narratives should be used judiciously. When not necessary, communications about AI systems should employ
language that distinguishes AI behavior from consciousness.
One potential scenario arises when AI systems are developed with a certain degree of access consciousness as
mentioned earlier (the functional availability of information for use in reasoning and behavior). When referring
to such capabilities, using the term “consciousness” may be unavoidable. In these cases, we advocate for
institutions to provide precise contextual clarification when communicating about these systems, distinguishing
functional capabilities from phenomenal consciousness, thereby minimizing potential misinterpretation and
societal impact.
We acknowledge that in practice this question involves a lot of details that will be hard to evaluate and regulate.
We encourage the community to discuss and debate the details.
4.3

If an AI System Were Truly Conscious In The Future, What Rights Should It Have?

This question invites us to contemplate a hypothetical future where our presumption of no consciousness
has been definitively overcome through compelling evidence. It is important to acknowledge that such
a scenario would likely emerge only after profound advancements in technology, substantial evolution in
our understanding of consciousness, and significant societal transformation. Given these considerations,
our present discussion of this topic should be viewed primarily as a philosophical exercise—a preliminary
exploration of ethical terrain that will undoubtedly be reshaped by developments we cannot yet fully anticipate.
Regarding this issue, one important distinction we wish to make is that consciousness status does not directly
dictate rights status. It is just one of the important factors to consider. From the risk prudence principle,
we derive our default position : Even genuinely conscious AI would not automatically qualify for humanequivalent or even animal-equivalent rights. Thorough discussions will be needed to balance AI welfare
considerations with human interests as the primary concern. Importantly, this implies by default termination
of a conscious system should be allowed given its below-human or even below-animal level rights.
The legal dimension of AI rights, referenced in Section 3.3.2, presents a global challenge requiring international
consensus. While our framework guides ethical discourse, implementing any AI rights would demand
established legal processes. Any approach must examine mechanisms for recognizing and enforcing such
rights if consciousness evidence emerges, balancing philosophical considerations with practical governance
across jurisdictions.

5

Conclusion

We have proposed a human-centric framework for AI consciousness ethics that builds on transparent foundations while acknowledging philosophical uncertainty surrounding consciousness. Our complete three-level
structure—foundational factual determinations and meta-ethical stance, operational principles, and applicationlevel default positions—not only generates actionable guidance but provides a transparent derivation process
through which positions logically follow from established principles. This systematic approach makes explicit
how each ethical position can be traced back to our foundational commitments, enabling both rigorous evaluation and responsible adaptation. Rather than claiming definitive answers, we establish reasonable epistemic
and pragmatic starting points that prioritize human welfare without hindering beneficial technological development. By providing clear logical pathways from foundations to applications and specifying conditions for
revising positions, the framework is designed to evolve alongside advances in consciousness research and AI
development, offering a responsible path forward through these profound ethical challenges.

9

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

References
OpenAI. Gpt-4 technical report. 2023.
Anthropic. Claude 2 technical report. 2023.
Nick Bostrom. Superintelligence: Paths, dangers, strategies. Oxford University Press, 2014a.
Astrid M Rosenthal-von der Pütten, Nicole C Krämer, Matthias Brand, Hans J Markowitsch, and Sören
Hoffmann. Robots can be seen as good colleagues, but never friends. PsychNology Journal, 11(1):1–25,
2013.
Kate Darling. Extending legal protection to social robots: The effects of anthropomorphism, empathy, and
violent behavior towards robotic objects. Edward Elgar Publishing, 2016.
David J Chalmers. Facing up to the problem of consciousness. Journal of consciousness studies, 2(3):200–219,
1995.
Yoshua Bengio et al. Open letter on prioritizing consciousness research in the ai agenda.
//amcs-community.org/open-letters/, 2023. Accessed: 2025-02-15.

https:

Geoffrey Hinton. Geoffrey hinton warns of ai dangers. CBS News 60 Minutes interview, 2023. https:
//www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/.
Anthropic.
Exploring model welfare.
https://www.anthropic.com/research/
exploring-model-welfare, 2025. Accessed: 2025-02-15.
Conscium Foundation. Principles for conscious ai. https://conscium.com/wp-content/uploads/
2024/11/Principles-for-Conscious-AI.pdf, 2024. Accessed: 2025-02-15.
Jeff Sebo. Taking ai welfare seriously. https://jeffsebo.net/wp-content/uploads/2024/10/
20241030_taking_ai_welfare_seriously_web.pdf, 2024. Accessed: 2025-02-15.
Jeff Sebo and Richard Long. Moral consideration for ai systems by 2030. AI Ethics, 5:591–606, 2023.
doi:10.1007/s43681-023-00379-1.
Ned Block. On a confusion about a function of consciousness. Behavioral and Brain Sciences, 18(2):227–247,
1995.
Stanislas Dehaene. Consciousness and the brain: Deciphering how the brain codes our thoughts. Penguin,
2017.
Thomas Nagel. What is it like to be a bat? The philosophical review, 83(4):435–450, 1974.
Daniel C Dennett. Consciousness explained. Little, Brown and Company, 1991.
Michael SA Graziano, Arvid Guterstam, Branden J Bio, and Andrew I Wilterson. Toward a standard model of
consciousness: Reconciling the attention schema, global workspace, higher-order thought, and illusionist
theories. Cognitive neuropsychology, 36(3-4):155–172, 2019.
Shelly Kagan. How to count animals, more or less. Oxford University Press, 2019.
Roman V Yampolskiy. Ai safety engineering through uncertainty quantification for deep learning. 2020.
Zikang Ji, Woojeong Jin Lee, Takashi Shinkuma, Kevin Shih, Stan Sclaroff, and Margrit Betke. Ai alignment:
A comprehensive survey. 2023.
Patrick Butlin, Heather Browning, Tim Bayne, Matthias Michel, Jonathan Birch, Jaan Aru, Katja Crone,
Andreas Engel, Tomas Folke, Cathy Henderson, et al. Principles for the governance of ai consciousness
research. 2024.
Eric Schwitzgebel and Mara Garza. The tyrant’s headache: The problem of consciousness for a moral realist.
Philosophical Studies, 172(9):2357–2378, 2015.
Max Tegmark. Consciousness as a state of matter. Chaos, Solitons & Fractals, 76:238–270, 2015.
Joseph Levine. Materialism and qualia: The explanatory gap. Pacific philosophical quarterly, 64(4):354–361,
1983.
Ned Block. Troubles with functionalism. Minnesota Studies in the Philosophy of Science, 9:261–325, 1978.
Bradley
and
Saad.
Ai
alignment
vs
ai
ethical
treatment:
Ten
challenges.
https://globalprioritiesinstitute.org/wp-content/uploads/
Bradley-and-Saad-AI-alignment-vs-AI-ethical-treatment_-Ten-challenges.pdf, 2024.
Accessed: 2025-02-15.
10

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

Nick Bostrom. The ethics of artificial intelligence. Cambridge Handbook of Artificial Intelligence, pages
316–334, 2014b.
Neil Levy. Neural correlates of consciousness: Progress and problems. Nature Reviews Neuroscience, 15(5):
356–368, 2014.
Anil K Seth. The real problem of consciousness. Aeon Essays, 2016.
David J Gunkel. Robot rights. MIT Press, 2018.
Mattias Johansson and Hampus Herrman. Artificial intelligence, status and gender: How conversational ai
assistants can influence social judgements about people. AI & Society, 36:1–11, 2019.
Jürgen Habermas. Moral consciousness and communicative action. MIT press, 1990.
John Rawls. A theory of justice. Harvard University Press, 1971.
Wendell Wallach and Colin Allen. Moral machines: Teaching robots right from wrong. Oxford University
Press, 2008.
Patrick Lin, Keith Abney, and George Bekey. Robot ethics: Mapping the issues for a mechanized world.
Artificial Intelligence, 175(5-6):942–949, 2017.
Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee,
Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments
with gpt-4. 2023.
David J Chalmers. Could a large language model be conscious? Boston Review, 48(1):10–30, 2023.
John R Searle. Minds, brains, and programs. Behavioral and brain sciences, 3(3):417–424, 1980.
Joseph Weizenbaum. Eliza—a computer program for the study of natural language communication between
man and machine. Communications of the ACM, 9(1):36–45, 1966.
Sherry Turkle. The second self: Computers and the human spirit. Simon and Schuster, 1984.
Clifford Nass, Jonathan Steuer, and Ellen R Tauber. Computers are social actors. Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems, pages 72–78, 1994.
Nicholas Epley, Adam Waytz, and John T Cacioppo. On seeing human: A three-factor theory of anthropomorphism. Psychological Review, 114(4):864–886, 2007.
Euronews Next.
Love in the time of ai:
Woman claims she married a chatbot and is expecting its baby.
https://www.euronews.com/next/2023/06/07/
love-in-the-time-of-ai-woman-claims-she-married-a-chatbot-and-is-expecting-its-baby,
2023a. Accessed: 2025-02-15.
Euronews Next.
Man ends his life after an ai chatbot encouraged him to sacrifice
himself to stop climate change.
https://www.euronews.com/next/2023/03/31/
man-ends-his-life-after-an-ai-chatbot-encouraged-him-to-sacrifice-himself-to-stop-climate,
2023b. Accessed: 2025-02-15.
Neil Levy and Julian Savulescu. Moral significance of phenomenal consciousness. Progress in Brain Research,
177:361–370, 2009.
Joshua Shepherd. Consciousness and moral status. Routledge, 2018.
Guy Kahane and Julian Savulescu. Brain damage and the moral significance of consciousness. Journal of
Medicine and Philosophy, 34(1):6–26, 2009.
Andrew Y. Lee. Consciousness makes things matter. Philosophical Review, 2023. Forthcoming.
David J. Chalmers. Reality+: Virtual worlds and the problems of philosophy. W.W. Norton & Company, 2022.
Murray Shanahan. Conscious exotica. Aeon, 2016.
Bernard J Baars. In the theater of consciousness: The workspace of the mind. Journal of Consciousness
Studies, 4(4):292–309, 1997.
Giulio Tononi. Consciousness as integrated information: a provisional manifesto. The Biological Bulletin, 215
(3):216–242, 2008.
Giulio Tononi, Melanie Boly, Marcello Massimini, and Christof Koch. Integrated information theory: from
consciousness to its physical substrate. Nature Reviews Neuroscience, 17(7):450–461, 2016.
David M Rosenthal. Varieties of higher-order theory. Advances in consciousness research, 56:17–44, 2004.
11

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

Richard Brown, Hakwan Lau, and Joseph E LeDoux. The higher order approach to consciousness is defunct.
Neuropsychologia, 128:99–106, 2019.
Michael SA Graziano. Consciousness and the social brain. Oxford University Press, 2013.
Adrien Doerig, Aaron Schurger, and Michael H Herzog. The unfolding argument: Why iit and other causal
structure theories cannot explain consciousness. Consciousness and Cognition, 72:49–59, 2019.
Frank Jackson. Epiphenomenal qualia. The Philosophical Quarterly, 32(127):127–136, 1982.
John R Searle. The rediscovery of the mind. MIT Press, 1992.
Christof Koch. The quest for consciousness: A neurobiological approach. Roberts and Company Publishers,
2004.
Stuart Hameroff and Roger Penrose. Consciousness, microtubules, and "orch or": a ’space-time odyssey’.
Journal of Consciousness Studies, 21(3-4):126–153, 2014.
Christof Koch, Marcello Massimini, Melanie Boly, and Giulio Tononi. Neural correlates of consciousness:
progress and problems. Nature Reviews Neuroscience, 17(5):307–321, 2016.
John R Searle. Biological naturalism. The Blackwell companion to consciousness, pages 325–334, 2007.
Elliott Sober. The biology of consciousness. Biology & Philosophy, 33(3-4):1–14, 2018.
Eric Schwitzgebel. If materialism is true, the united states is probably conscious. Philosophical Studies, 173
(7):1983–1999, 2016.
Colin Allen and Wendell Wallach. The ethical impacts of robots. The Journal of Experimental & Theoretical
Artificial Intelligence, 23(3):301–318, 2011.
Naveed Anwar, Peter Pemberton-Ross, Etai Ben-David, and Dylan Hadfield-Menell. Foundational ai safety
and the unintended consequences of reward maximization. Alignment Research Center, 2024.
Matthew Chua, Dylan Hadfield-Menell, and Naveed Anwar. Ai safety: a systems-oriented approach. 2024.
Anthony Everett. The risks of artificial general intelligence. Journal of Artificial Intelligence Research, 1(1):
1–23, 2019.
Deborah G Johnson. Computer systems: Moral entities but not moral agents. Ethics and Information
Technology, 8(4):195–204, 2006.
Andreas Matthias. The responsibility gap: Ascribing responsibility for the actions of learning automata. Ethics
and Information Technology, 6(3):175–183, 2004.
Jacob Turner. Robot rules: Regulating artificial intelligence. Palgrave Macmillan, 2019.
Lawrence B Solum. Legal personhood for artificial intelligences. North Carolina Law Review, 70(4):
1231–1287, 1992.
Ricardo Vinuesa, Hossein Azizpour, Iolanda Leite, Madeline Balaam, Virginia Dignum, Sami Domisch, Anna
Felländer, Simone D Langhans, Max Tegmark, and Francesco Fuso Nerini. The role of artificial intelligence
in achieving the sustainable development goals. Nature Communications, 11(1):1–10, 2020.
Adam Waytz, Joy Heafner, and Nicholas Epley. The mind in the machine: Anthropomorphism increases trust
in an autonomous vehicle. Journal of Experimental Social Psychology, 48(6):1410–1416, 2010.
Joanna J Bryson. Robots should be slaves. Close Engagements with Artificial Companions: Key Social,
Psychological, Ethical and Design Issues, pages 63–74, 2010.
Stephen Cave and Kanta Dihal. Hopes and fears for intelligent machines in fiction and reality. Nature Machine
Intelligence, 1(2):74–78, 2019.
Joanna J Bryson. Intelligence in the human interest. Ethics of Artificial Intelligence, pages 33–53, 2019.
Luciano Floridi, Josh Cowls, Monica Beltramini, Raja Chatila, Patrice Chazerand, Virginia Dignum, Christoph
Luetge, Robert Madelin, Ugo Pagallo, Francesca Rossi, et al. Ethics of artificial intelligence and robotics.
Stanford Encyclopedia of Philosophy, 2018.
Brent Daniel Mittelstadt, Patrick Allo, Mariarosaria Taddeo, Sandra Wachter, and Luciano Floridi. The ethics
of algorithms: Mapping the debate. Big Data & Society, 3(2):2053951716679679, 2016.
Thomas Nagel. The view from nowhere. Oxford University Press, 1986.
Mark Coeckelbergh. Robot rights? towards a social-relational justification of moral consideration. Ethics and
Information Technology, 12(3):209–221, 2010.
12

Human-centric Framework for AI Consciousness Ethics

A P REPRINT

Jan-Peter Voss, Dierk Bauknecht, and René Kemp. Sustainability and reflexive governance: Introduction.
Reflexive Governance for Sustainable Development, pages 3–28, 2006.
David H Guston. Understanding anticipatory governance. Social Studies of Science, 44(2):218–242, 2014.
Max Tegmark. Life 3.0: Being human in the age of artificial intelligence. Knopf, 2017.
Bernard Williams. Internal and external reasons. Moral luck: Philosophical papers 1973-1980, pages 101–113,
1981a.
Bernard Williams. Moral luck: philosophical papers 1973-1980. Cambridge University Press, 1981b.
Hans Jonas. The imperative of responsibility: In search of an ethics for the technological age. University of
Chicago Press, 1984.
Thomas Scanlon. What we owe to each other. Harvard University Press, 1998.
Samuel Scheffler. Boundaries and allegiances: Problems of justice and responsibility in liberal thought.
Oxford University Press, 2001.
Peter Singer. Animal liberation: A new ethics for our treatment of animals. New York Review, 1975.
Richard D Ryder. Speciesism again: the original leaflet. Critical Society, 2:1–2, 2010.
Cass R Sunstein. Laws of fear: Beyond the precautionary principle. Cambridge University Press, 2005.
Sven Ove Hansson. The ethics of risk: Ethical analysis in an uncertain world. Palgrave Macmillan, 2013.
Carolyn Raffensperger and Joel A Tickner. The precautionary principle in action: A handbook. Science and
Environmental Health Network, 1999.
Tom L Beauchamp and James F Childress. Principles of biomedical ethics. Oxford University Press, 2001.
Leonard J Savage. The theory of statistical decision. Journal of the American Statistical Association, 46(253):
55–67, 1951.
Andrew Ashworth. Reasonable doubt and the presumption of innocence. Theoretical Inquiries in Law, 7(2):
425–444, 2006.
Ned Block. Minds, machines, and consciousness. Philosophy of Mind, pages 1–25, 2022.
Thomas S Kuhn. The structure of scientific revolutions. University of Chicago Press, 1962.
Naomi Oreskes. The scientific consensus on climate change. Science, 306(5702):1686–1686, 2004.
Stuart Firestein. Ignorance: How it drives science. Oxford University Press, 2012.
Melanie Mitchell. Complexity: A guided tour. Oxford University Press, 2009.
Ryan Calo. Robotics and the lessons of cyberlaw. California Law Review, 103:513–563, 2015.
Bert-Jaap Koops. On legal boundaries, technologies, and collapsing dimensions of privacy. Politica e Società,
2(2):247–264, 2013.
Gunther Teubner. Rights of non-humans? electronic agents and animals as new actors in politics and law.
Journal of Law and Society, 33(4):497–521, 2018.
Sheila Jasanoff. The Fifth Branch: Science Advisers as Policymakers. Harvard University Press, 2009.
John Dewey. Human nature and conduct. Henry Holt and Company, 1922.
Karl Popper. The Logic of Scientific Discovery. Routledge, 1959.
Willard V Quine. Two dogmas of empiricism. The Philosophical Review, 60(1):20–43, 1951.
Jürgen Habermas. The Theory of Communicative Action: Reason and the rationalization of society, volume 1.
Beacon Press, 1984.
Miriam Solomon. Social empiricism. MIT Press, 2001.
Yutaka Suzuki, Lisa Galli, Ayaka Ikeda, Shoji Itakura, and Michiteru Kitazaki. Anthropomorphism boosts
preference for robot faces: A study in japan. Proceedings of the 37th Annual Meeting of the Cognitive
Science Society, 2015.
Tobias Greitemeyer. Intense acts of violence during video game play make daily life aggression appear
innocuous: A new mechanism why violent video games increase aggression. Journal of Experimental
Social Psychology, 50:52–56, 2014.
Craig A Anderson, Akiko Shibuya, Nobuko Ihori, Edward L Swing, Brad J Bushman, Akira Sakamoto,
Hannah R Rothstein, and Muniba Saleem. Violent video game effects on aggression, empathy, and prosocial
behavior in eastern and western countries: A meta-analytic review. Psychological Bulletin, 136(2):151–173,
2010.
13

