# Chapter 3.3.1: Introduction to Decision Making Under Uncertainty

So far in this chapter, AI has learned how to represent uncertain belief.

But intelligence is not only about belief.
It is also about **action**.

That means a harder question now appears:

> if outcomes are uncertain, how should an agent choose what to do?

This is where decision theory enters AI.

The problem is no longer only:

- What is likely true?

It becomes:

- Which action is best, given uncertainty?

That requires three things:

- probabilities
- preferences
- long-term consequences

So in this section, we move from uncertain belief to uncertain action.

The path is:

1. Utility
2. Expected utility
3. Markov Decision Processes (MDPs)
4. Policies and value functions
5. Bellman equations
6. Reinforcement learning before deep learning

This part matters because it reconnects statistics with the older AI idea of rational agents.

The agent is still trying to achieve goals.
But now it must do that in a world where outcomes are not guaranteed.

We begin with the idea of **utility**.
