---
title: "Field Notes from EAG NYC"
date: "October 14, 2025"
category: "writing"
source: "https://lydianottingham.substack.com/p/field-notes-from-eag-nyc"
---

# Field Notes from EAG NYC

[AI / ML](https://lydianottingham.substack.com/s/posts-about-ai/?utm_source=substack&utm_medium=menu)

# Field Notes from EAG NYC

### which way, scientist AI?

[![Lydia Nottingham's avatar](https://substackcdn.com/image/fetch/$s_!vtly!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00b9f6ba-3b98-4eab-af7a-8b677e3d2c62_1126x1126.jpeg)](https://substack.com/@lydianottingham)

[Lydia Nottingham](https://substack.com/@lydianottingham)

Oct 14, 2025

7

[](https://lydianottingham.substack.com/p/field-notes-from-eag-nyc/comments)

[Share](javascript:void\(0\))

### The Brittleness Problem

I don’t think I can work on LM behavior much longer. It’s too brittle, fickle, sensitive to hyperparameter perturbations—outputs stochastic in a way even [Scherrer et al.](https://arxiv.org/abs/2307.14324) can’t resolve. A grad student resonates; that’s why he’s working on [knowledge graphs](https://arxiv.org/abs/2307.07697) now.

### Which Way, Scientist AI?

The [Scientist AI](https://arxiv.org/abs/2502.15657) people don’t seem to have ready answers to “how will Scientist AI expand its database / propose experiments & get them approved?” I perceive two defensible positions here:

  1. We can still get almost all the value we’d get from agentic / autonomous AI (scientific breakthroughs, poverty alleviation…) with non-agentic / scientist / oracle AI.

  2. We’re going to be leaving a lot of potential value on the table [by refusing agentic / autonomous systems], but we have no choice but to make this sacrifice.




They don’t make clear which position they’re defending.

I of course want to see more people defend 1. But if 2 is our only option—if ‘Scientist AI’ is as far as we can go[1](https://lydianottingham.substack.com/p/field-notes-from-eag-nyc#footnote-1-176117030)—then I’m interested in how we can set standards that prepare us for Scientist AI, so it can do its darn best with a semi-static / slow-moving database. [Rory](https://www.rory.bio/) says AlphaFold only worked because all protein-folding researchers used [Protein Data Bank](https://www.rcsb.org/) in the 1980-90s, yielding abundant standardized training data. **What standards can scientific conferences set today to help non-agentic AI readers?**

Some ‘Scientist AI’ co-authors I spoke to hadn’t read “[Why Tool AIs Want To Be Agent AIs](https://gwern.net/tool-ai)”, which informs a lot of my intuitions here.

[![](https://substackcdn.com/image/fetch/$s_!BSPQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5426cb4-01fa-4c6a-8327-b77317259920_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!BSPQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5426cb4-01fa-4c6a-8327-b77317259920_1024x1024.png)which way, Scientist AI?

### Activation Fatigue

When I discuss activation engineering woes, Linh recommends approaches I wish I had time & headspace to chase down—I need to get into an environment where I can properly try solving the problems I’m working on. Notably, I really need to read up on [Latent Adversarial Training](https://arxiv.org/abs/2407.15549).

Steering vectors are [not](https://arxiv.org/abs/2505.03189) currently deployable in frontier systems.

### LM Behavior

I’ve been interested in ‘stated vs. revealed preferences in LMs’ for a while now. [Abdur](https://abdur-raheem.com/) is so quick he runs a follow-up experiment on SvR right after we chat: a model tries to circumvent its max_tokens limit while claiming the limit’s chill. Quite sympathetic behavior. This is a comparatively simple / clean setup vs. [Petri](https://www.anthropic.com/research/petri-open-source-auditing) and [ControlArena](https://control-arena.aisi.org.uk/), other possible testbeds.

[Adam](https://thatadammorris.com/) has a neat [approach](https://arxiv.org/abs/2505.17120) to measuring model behavior and the effects of pro-[introspection](https://arxiv.org/abs/2410.13787) interventions. If you personally specify the model’s preferences, you have a cleaner baseline vs. working with ‘native’ preferences. Something I should keep in mind on SvR project.

The [CaML](https://www.compassionml.com/) people are engaging in “data poisoning for good”—controlling LMs with synthetic pro-compassion data given free to model developers and/or spread around the internet. In some ways, it’s such [noble](https://x.com/boops_u/status/1976656590569881811), honorable work. But it also connotes ‘fighting within a broken paradigm’. The world where this is counterfactual is not the one I want to live in.

I’m starting to think the best empirical LM behavior / ‘revealed preference’ analysis will take place over AI labs’ model logs, [AEI-style](https://www.anthropic.com/economic-index), though we can operate over datasets like [LMSYS-Chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) in the meantime. 

According to [Audre](https://www.povertyactionlab.org/person/lorvo)y, J–Pal’s evals (on how AI helps coffee farmers etc.) will inform us about philanthropy-counterfactual AI use. For example, they’ve got preliminary results suggesting chat assistants boost entrepreneurs who were already doing well, but may be unhelpful to struggling business owners who defer and dig holes they can’t get out of.

### Alignment Roundup

An ex-FHI / [CIWG](https://causalincentives.com/) researcher explains struggles doing research that’s both good and easy to fund. “Just write a paper every ~3 months.” Good advice.

AE Studio is one heck of a company—using software consultancy to fund their [alignment research](https://ai-alignment.ae.studio/). [Self-other overlap](https://www.lesswrong.com/posts/hzt9gHpNwA2oHtwKX/self-other-overlap-a-neglected-approach-to-ai-alignment), [energy-based transformers](https://arxiv.org/abs/2507.02092).

[Poseidon Research](https://poseidonresearch.org/) exists! Cryptography, steganography, LM monitoring. It’s now possible to do AIS research in Manhattan at the [NYC Impact Hub](https://www.nycimpacthub.org/).

Robotics interpretability is a growing field, with work in progress at [PAIR Lab](https://www.pair.toronto.edu/) (Yixiong) and Imperial (Ida) (VLAMs like 7B OpenVLA). 

The whole field of making AI science (e.g. jailbreaking) [principled](https://arxiv.org/abs/2501.11183) seems fun.

[Martin](https://www.linkedin.com/in/martinleitgab/) would need $20-30k to scale his literature-synthesis, intervention-extracting work from the [Alignment Research Dataset](https://huggingface.co/datasets/StampyAI/alignment-research-dataset) ($800) to all of ArXiv.

Tyler G’s study list is relatable: control theory, stochastic processes, categorical systems theory, dynamical systems theory, network theory, game theory, decision theory, multiagent modeling, and formal verification. [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) addresses agency, unlike Scientist AI. In general, I appreciate papers that address safe design, like [Overview of 11 Proposals](https://arxiv.org/abs/2012.07532).

Bandwidth generally high with long-time rationalists like [Justin](https://www.lesswrong.com/users/justinshovelain), and yes, ‘stealth advisor’ is a thing you can be.

Will’s [post](https://willmacaskill.substack.com/p/effective-altruism-in-the-age-of) encouraging EAs to ‘make AI go well’ seems like a helpful summary of the recent zeitgeist around me. Notably, [ETAI](https://digitaleconomy.stanford.edu/etai-course/) had this flavor. 

### Podcasting Tips

I hear all about podcast design from [Angela](https://angelatan.ca/)! For context, I’m thinking of starting a podcast in Oxford, mapping the work of PIs and grad students in AI, neurotech, matsci, etc. onto [Gap Map](https://www.gap-map.org/). Apparently [Oxford Public Philosophy](https://www.oxfordpublicphilosophy.com/) are a strong local podcast.

Angela’s advice for interviewing guests is this:

  * Watch their other episodes to see what they’ve spoken about before—get them off-script

  * Ask about a moment where they’ve experienced a paradigm shift / went into work believing one thing, then something changed

  * Prepare 10-20 questions, including ideas for what you’ll do if things don’t go to plan

  * Give them an idea before the episode starts of what you’re planning to do, where you’re planning to go with the episode, and what you’re hoping you, they, & the audience get out of it




### **Misc. current musings:**

  * How meaningful are LM outputs produced under the coercion of [structured decoding](https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction) / strict token limits?

  * After all the [spiking neurons](https://igi-web.tugraz.at/PDF/85a.pdf) / [predictive coding](https://arxiv.org/abs/2202.09467) / … ‘neuromorphic AI’ work, are there any lessons we can apply from AI back to neuro (e.g. [representation engineering](https://arxiv.org/abs/2310.01405) ⇒ neuromodulation)?

  * Perhaps there should be a tiny research / forecasting hackathon dedicated to “what are [SSI](https://ssi.inc/) doing, and how can the safety community best respond [to their likely strategy / this flavor of development]?”

    * Can we track what they’re doing through their hardware orders?

  * The map & the territory…the [strings](https://github.com/centerforaisafety/emergent-values/blob/main/utility_analysis/shared_options/options_hierarchical.json) & the world-states. 

  * Reasoning mode / CoT gives a janky, goodharty increase in power + coherence, not a robust one. & the [history](https://lydianottingham.substack.com/p/9030-ml-reading-group-retrospective) of ML shows janky workarounds get subsumed by elegant, clean, simple replacements…

  * ‘Comparative advantage for skeptics’, anyone?




### **Things I want to read pretty soon:**

  * [GFlowNets](https://arxiv.org/abs/2111.09266)

  * FHI on [infohazards](https://nickbostrom.com/information-hazards.pdf), [infinite ethics](https://nickbostrom.com/ethics/infinite), & [everything else](https://www.futureofhumanityinstitute.org/)

    * We now have an FHI-inspired working group in SF/Berkeley! Lmk if interested :)

  * As always, everything under ‘[Read Later!](https://curius.app/lydia-nottingham/read-later)’ But I’m going to introduce two new tags: one ‘skimmed, deprioritized’ and the other ‘read it, made updates, wrote about them, cleared cache’. It will be good.




Read some [Flatland](https://ned.ipac.caltech.edu/level5/Abbott/paper.pdf) on the plane.

‘Choose-your-own-adventure’ is the right mindset for EAG! I can’t wait for next year :)

_With huge appreciation to Iggy, who kindly hosted me after briefly meeting at[Memoria](https://www.memoria.day/), & as ever, to the EAG Team!_

[1](https://lydianottingham.substack.com/p/field-notes-from-eag-nyc#footnote-anchor-1-176117030)

notwithstanding the cat already being out of the bag wrt agentic systems

7

[](https://lydianottingham.substack.com/p/field-notes-from-eag-nyc/comments)

[Share](javascript:void\(0\))


---

*Originally published on [Substack](https://lydianottingham.substack.com/p/field-notes-from-eag-nyc)*
