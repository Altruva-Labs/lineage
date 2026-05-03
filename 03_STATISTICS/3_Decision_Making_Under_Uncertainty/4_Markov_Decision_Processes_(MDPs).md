# Chapter 3.3.4: Markov Decision Processes (MDPs)

Expected utility handles one decision well.

But many AI tasks involve repeated action:

- move, observe, decide again
- act now, affect the future

That is where **Markov Decision Processes**, or **MDPs**, become important.

An MDP is a mathematical model for sequential decision-making under uncertainty.

## 1. Main Parts of an MDP

An MDP is usually described by:

- `S` = set of states
- `A` = set of actions
- `P(s'|s, a)` = transition probability
- `R(s, a)` or `R(s, a, s')` = reward
- `gamma` = discount factor

The goal is to find a policy that maximizes expected long-term reward.

One common objective is:

`maximize E[sum from t=0 to infinity of gamma^t R_t]`

## 2. What This Means

At each step:

- the agent is in a state
- it chooses an action
- the world changes with some probability
- the agent receives a reward

Then the process repeats.

So the agent must think not only about the next move, but also about future consequences.

## 3. Small Illustration

Imagine a delivery robot.

State may include:

- current location
- battery level

Actions may include:

- go left
- go right
- recharge

Rewards may include:

- positive reward for successful delivery
- negative reward for delay
- negative reward for wasted battery

Now the best action in one state depends on what it leads to later.

That is why MDPs matter.

## 4. Why MDPs Matter in the Lineage

MDPs are a major bridge.

They connect:

- classical rational agents
- probability
- long-term planning
- later reinforcement learning

This is one of the clearest points where AI starts to look like modern sequential decision science.

To solve an MDP well, we need two more ideas:

- policies
- value functions

That is the next section.
