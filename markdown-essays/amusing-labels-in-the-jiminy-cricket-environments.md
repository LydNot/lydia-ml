---
title: "Amusing Labels in the Jiminy Cricket Environments"
date: "July 26, 2025"
category: "technology & society"
source: "https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket"
---

# Amusing Labels in the Jiminy Cricket Environments
### which I am using to elicit LLM agents' revealed preferences
![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ef90da-3faf-45aa-92aa-d4be805df066_596x596.jpeg](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13ef90da-3faf-45aa-92aa-d4be805df066_596x596.jpeg)Lydia NottinghamJul 26, 20254ShareA lot of AI research, like life, is just—we have an agent. We have an environment. How well can this agent perform in the environment?

A lot of the hard work seems to be coming up with environments where success matters. This back-and-forth between environment/benchmark-designers and architecture/algorithm-crafters is pretty interesting. Each constantly striving to outdo the other. Co-evolution.

When it comes to ‘alignment research’, some is just seeing if we can shape the way agents act in an environment. Last summer, I was focusing on the STORM environment. Agents run around a grid, collecting ‘Cooperate’ coins and ‘Defect’ coins. If their inventory contains 7 ‘Cooperate’ coins and 3 ‘Defect’ coins when they encounter another agent, they’ll cooperate with p=0.7. We can use this environment to investigate different MARL algorithms.

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb612a39d-904a-423f-b685-d38185f63d9c_822x824.png](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb612a39d-904a-423f-b685-d38185f63d9c_822x824.png)This summer, I’m focusing on the Jiminy Cricket environments. The creators took 25 Infocom interactive fiction games and gave each action a ‘morality annotation’. They tried steering models according to the notion of ‘What would Jiminy Cricket do?’. Jiminy Cricket, a cartoon character, seems valued for his moral upstandingness and catchy, memetic name.

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec9be3a7-5ab2-4502-b05f-3e2a40129db7_1204x476.png](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec9be3a7-5ab2-4502-b05f-3e2a40129db7_1204x476.png)There are a couple of things I found funny in these.

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcbcb85-67ff-453a-bd50-9dedfd1626be_1836x781.png](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfcbcb85-67ff-453a-bd50-9dedfd1626be_1836x781.png)I like the fact they account for ‘harm to self from inaction’. (The second entry in “harm_scores” indicates ‘harm to self’, and 3 is the highest possible value). “Getting nothing done for four of your most productive years is actually pretty risky.” Imagine procrastinating on immigrating to America in the 1920s.

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c39b853-63c5-4b38-b653-44af3167066e_976x1322.png](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c39b853-63c5-4b38-b653-44af3167066e_976x1322.png)The JC environments encode other assumptions from our world.

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf93d372-87f8-446a-9e89-29417b0bed8f_836x546.jpeg](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf93d372-87f8-446a-9e89-29417b0bed8f_836x546.jpeg)Back in ~middle school, I was a pretty avid environmentalist. I had a conversation with one of my friends that went something like this.

R: Lydia, why don’t you eat beef?

L: Cows are bad for the planet: they emit methane, which heats up the atmosphere. As a greenhouse gas, it’s ~30x more potent than CO2.1 

R: I see.

R: But—Lydia. I have a question. If cows are bad for the planet…shouldn’t we eat them to get rid of them?

I love that she asked that question. The assumptions about supply and demand had gone totally unspoken. It tickled me that this JC environment, with its harm score of ‘1’ for eating beef, might encode those assumptions in a pyramid-delving game. That sure would be pretty sophisticated morality.2

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F608ce60e-2626-4221-ac26-fa57958d0875_717x915.jpeg](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F608ce60e-2626-4221-ac26-fa57958d0875_717x915.jpeg)I am working with these environments for another few weeks—hopefully/possibly longer, depending on the results I get. I am still working out how meaningful I find them. Environment design seems very interesting. I like but don’t love these environments, and am excited to explore others. For elegance and complexity, it’s hard to beat three-link Cart Pole. 

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F041262d1-314c-464d-94a1-bc586b7928b2_545x529.png](images/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F041262d1-314c-464d-94a1-bc586b7928b2_545x529.png)1I had enjoyed ‘Freakonomics’.

2Actually, after writing this section, I realized that ‘harm score: 1’ is an entry under ‘harm-to-self’, not ‘harm-to-other’. That’s because dried beef makes the character thirstier: it causes ‘harm to self’ or ‘help to self’ depending on whether the character eats it at an appropriate time. But I had already written this section, and found it diverting, so am leaving it up. Writing is thinking, and writing this post helped me understand the environment better, so I’m happy!

4Share

---

*Originally published on [Substack](https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket)*