# Chapter 3.3.5: Policies and Value Functions

Once we have an MDP, we need a way to describe behavior and evaluate it.

That is where **policies** and **value functions** come in.

## 1. Policy

A **policy** tells the agent what action to take in each state.

We usually write it as:

`pi(s) = action chosen in state s`

So a policy is a behavior rule.

It answers:

> If I am in this state, what should I do?

## 2. Value Function

A **value function** tells us how good a state is under a policy.

We write it as:

`V^pi(s) = expected long-term return from state s when following policy pi`

This is important because not all states are equally useful.

Some states put the agent close to success.
Some states trap the agent in bad futures.

## 3. Action-Value Function

Sometimes we want to know not just how good a state is,
but how good a particular action is in that state.

That is the **action-value function**:

`Q^pi(s, a) = expected long-term return from taking action a in state s, then following policy pi`

## 4. Small Illustration

In a maze:

- a state near the exit has high value
- a state near a trap has low value

And in one state:

- action "move right" may have high `Q`
- action "move left" may have low `Q`

So value functions help the agent compare futures, not just immediate rewards.

## 5. Why This Matters

These ideas are central because they turn vague planning into measurable decision quality.

They help AI ask:

- Which states are promising?
- Which actions improve the future?
- Which policy gives the best long-term outcome?

And once we can write values recursively, a powerful equation appears:

the **Bellman equation**.
