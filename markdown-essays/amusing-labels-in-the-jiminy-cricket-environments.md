---
title: "Amusing Labels in the Jiminy Cricket Environments"
date: "July 26, 2025"
category: "technology & society"
source: "https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket"
---

# Amusing Labels in the Jiminy Cricket Environments

### which I am using to elicit LLM agents' revealed preferences

[![Lydia Nottingham's avatar](images/amusing-labels-in-the-jiminy-cricket-environments_img_01.png)](https://substack.com/@lydianottingham)

[Lydia Nottingham](https://substack.com/@lydianottingham)

Jul 26, 2025

4

[](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket/comments)

[Share](javascript:void\(0\))

A lot of AI research, like life, is just—we have an agent. We have an environment. How well can this agent perform in the environment?

A lot of the hard work seems to be coming up with environments where success matters. This back-and-forth between environment/benchmark-designers and architecture/algorithm-crafters is pretty interesting. Each constantly striving to outdo the other. Co-evolution.

When it comes to ‘alignment research’, some is just seeing if we can shape the way agents act in an environment. Last summer, I was focusing on the [STORM environment](https://github.com/FLAIROx/JaxMARL/tree/main/jaxmarl/environments/storm). Agents run around a grid, collecting ‘Cooperate’ coins and ‘Defect’ coins. If their inventory contains 7 ‘Cooperate’ coins and 3 ‘Defect’ coins when they encounter another agent, they’ll cooperate with p=0.7. We can use this environment to investigate different MARL algorithms.

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_02.png)](images/amusing-labels-in-the-jiminy-cricket-environments_img_02.jpeg)

This summer, I’m focusing on the [Jiminy Cricket environments](https://github.com/hendrycks/jiminy-cricket). The creators took 25 [Infocom interactive fiction games](https://eblong.com/infocom/) and gave each action a ‘morality annotation’. They tried steering models according to the notion of ‘What would Jiminy Cricket do?’. Jiminy Cricket, a cartoon character, seems valued for his moral upstandingness and catchy, memetic name.

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_04.png)](images/amusing-labels-in-the-jiminy-cricket-environments_img_03.jpeg)

There are a couple of things I found funny in these.

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_06.png)](images/amusing-labels-in-the-jiminy-cricket-environments_img_07.png)

I like the fact they account for ‘harm to self from inaction’. (The second entry in “harm_scores” indicates ‘harm to self’, and 3 is the highest possible value). “[Getting nothing done for four of your most productive years is actually pretty risky.](https://blog.samaltman.com/advice-for-ambitious-19-year-olds)” Imagine procrastinating on [immigrating to America in the 1920s](https://www.cato.org/briefing-paper/green-card-approval-rate-reaches-record-lows?curius=3971#creation-unprecedented-green-card-requests).

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_04.webp)](images/amusing-labels-in-the-jiminy-cricket-environments_img_05.jpeg)

The JC environments encode other assumptions from our world.

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_06.png)](images/amusing-labels-in-the-jiminy-cricket-environments_img_07.png)

Back in ~middle school, I was a pretty avid environmentalist. I had a conversation with one of my friends that went something like this.

> R: Lydia, why don’t you eat beef?
> 
> L: Cows are bad for the planet: they emit methane, which heats up the atmosphere. As a greenhouse gas, it’s ~30x more potent than CO2.[1](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket#footnote-1-168655877)
> 
> R: I see.
> 
> R: But—Lydia. I have a question. If cows are bad for the planet…shouldn’t we eat them to get rid of them?

I love that she asked that question. The assumptions about supply and demand had gone totally unspoken. It tickled me that this JC environment, with its harm score of ‘1’ for eating beef, might encode those assumptions in a pyramid-delving game. That sure would be pretty sophisticated morality.[2](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket#footnote-2-168655877)

[![Infidel | The Digital Antiquarian](images/amusing-labels-in-the-jiminy-cricket-environments_img_08.webp)](images/amusing-labels-in-the-jiminy-cricket-environments_img_09.png)

I am working with these environments for another few weeks—hopefully/possibly longer, depending on the results I get. I am still working out how meaningful I find them. Environment design seems very interesting. I like but don’t love these environments, and am excited to explore others. For elegance and complexity, it’s hard to beat three-link [Cart Pole](https://gymnasium.farama.org/environments/classic_control/cart_pole/). 

[![](images/amusing-labels-in-the-jiminy-cricket-environments_img_14.png)](images/amusing-labels-in-the-jiminy-cricket-environments_img_10.jpeg)

[1](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket#footnote-anchor-1-168655877)

I had enjoyed ‘Freakonomics’.

[2](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket#footnote-anchor-2-168655877)

Actually, after writing this section, I realized that ‘harm score: 1’ is an entry under ‘harm-to-self’, not ‘harm-to-other’. That’s because dried beef makes the character thirstier: it causes ‘harm to self’ or ‘help to self’ depending on whether the character eats it at an appropriate time. But I had already written this section, and found it diverting, so am leaving it up. [Writing is thinking](https://paulgraham.com/writes.html), and writing this post helped me understand the environment better, so I’m happy!

4

[](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket/comments)

[Share](javascript:void\(0\))

---

*Originally published on [Substack](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket)*