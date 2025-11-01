---
title: "Announcing Manival"
date: "June 18, 2025"
category: "artificial intelligence"
source: "https://manifund.substack.com/p/announcing-manival"
preview_image: "https://substackcdn.com/image/fetch/$s_!-A0s!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc171ea3e-515e-473d-8490-ac0e1dea13ee_2819x1644.png"
---

_Status: Something we’ve hacked on for a couple of weeks; looking to get feedback and iterate!_

Last time, I wrote about some [considerations](https://manifund.substack.com/p/givewell-for-ai-safety-lessons-learned) for AI safety grant evaluation, but didn’t actually ship a cost-effectiveness model. Since then, Austin, Nishad, and I have:

  * Developed [Manival](https://manivaluator.org/), an LLM-powered grant evaluator

  * Demoed it to an audience at [Manifest](https://manifest.is/)

  * Written and applied [our own grantmaking criteria](https://docs.google.com/spreadsheets/d/1t4GkdnurnDAb8N_tO5Kl6RuEY83Nll7hA0FscezqGFU/edit?usp=sharing)—we’ll see if Manival can replicate our taste 




[![](images/announcing-manival_img_01.png)](https://substackcdn.com/image/fetch/$s_!-A0s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc171ea3e-515e-473d-8490-ac0e1dea13ee_2819x1644.png)

### How Manival works

This is effectively a form of structured ‘Deep Research’.

First, we specify the fields that matter to us when evaluating a grant. These might include ‘domain expertise of project leads’ or ‘strength of project’s theory of change’. We have RAG-based ‘data fetchers’ (Perplexity Sonar) scour the internet and return a score, with reasoning, for each of these fields. We then feed these into an LLM synthesizer (Claude Opus), which provides an overall evaluation.

This is a pretty janky LLM wrapper compensating for the lack of Deep Research API. We’re aware of various RAG and Deep Research alternatives, and expect our evaluations to improve as we plug better models in.

[![](images/announcing-manival_img_02.png)](https://substackcdn.com/image/fetch/$s_!cApP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd376df32-91e9-4252-8e7d-19c315ccece1_870x1478.png)

### Customizing the criteria

Different people have different ideas of what should go into a grant evaluation config. Austin cares deeply about how great a team is; I’d like mine to consider counterfactual uses of a team’s time.

With Manival, you can apply any grant evaluation criteria of your choosing (go to Configs → AI Generate). Here’s one we made just for fun:

[![](images/announcing-manival_img_03.png)](https://substackcdn.com/image/fetch/$s_!MgNi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1bf45dd9-52a5-4e80-b612-09c55fafc796_1374x831.png)

[![](images/announcing-manival_img_04.png)](https://substackcdn.com/image/fetch/$s_!jiZz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d6a5f52-0e43-4657-baae-210509b02ec5_1871x1507.png)

### What’s next for Manival?

Manival has lots of potential uses. Here are some main ones:

  1. **Estimating marginal cost-effectiveness:** We could write a config that estimates how much of a difference marginal $ <x> would make.

  2. **Predicting impact market cap:** Right now, our configs evaluate projects on a scale from 0 to 10. In the real world, project size varies: some established projects seek 6-7 figures like a ‘Series A’; others seek 4-5 figures in ‘seed’ / ‘pre-seed’ funding. Can we use Scott Alexander’s [impact valuations](https://forum.effectivealtruism.org/posts/E7pkeDruknpSa7j3i/results-of-an-informal-survey-on-ai-grantmaking) to estimate a project’s ‘impact market cap’?

  3. **Improving project proposals:** Grant applicants can run their project proposal through Manival to understand what might need clarifying.

  4. **Project comparison:** We can use Manival to rank a category on Manifund, funnelling its most underrated projects to the top of your feed.

  5. **Recommendations:** We can use Manival to recommend new projects to grantmakers based on projects they’ve already supported.

  6. **Solving the ‘adverse selection’ / ‘funging’ problems:** Grantmakers can estimate how likely a project might be to get funding elsewhere, or better understand why it hasn’t been funded when that’s the case.




It might be valuable to simulate how other grantmakers you respect might evaluate a project when deciding whether to make a grant. For example, here’s a simulation of Joe Carlsmith’s thinking:

[![](images/announcing-manival_img_05.png)](https://substackcdn.com/image/fetch/$s_!ysc_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda5b104f-536d-4d13-aa87-39fef28dd6be_2799x1088.png)

These ‘simulated scores’ might differ from how a grantmaker actually thinks. Accordingly, we plan to develop configs that are maximally faithful to [our own thinking](https://docs.google.com/spreadsheets/d/1t4GkdnurnDAb8N_tO5Kl6RuEY83Nll7hA0FscezqGFU/edit?usp=sharing) over the next week.

For now, I expect a lot of Manival’s value to come from ‘flagging potentially great projects to look into’, rather than being something people defer to.

We’re excited for you to try Manival, and eager to know what you think, especially if you’re a donor, grantmaker, or someone else who cares a lot about evaluating grant proposals. [Schedule a call](https://calendly.com/manival/) with us to chat this through, or let us know in the comments!


---

*Originally published on [The Fox Says](https://manifund.substack.com/p/announcing-manival)*
