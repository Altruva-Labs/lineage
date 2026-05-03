# Chapter 3.3.7: Reinforcement Learning Before Neural Networks

At this point, all the pieces are in place:

- uncertainty
- rewards
- policies
- values
- Bellman-style recursion

Now a new question appears:

> what if the agent does not know the full model in advance?

That question leads to **reinforcement learning**.

Before deep neural networks entered the story, reinforcement learning already existed as a serious idea.

The main goal was:

> learn good behavior from experience

## 1. Temporal-Difference Learning

Temporal-Difference, or **TD learning**, updates value estimates from sampled experience.

The rough intuition is:

- estimate the value now
- observe one step of experience
- adjust the estimate toward a better target

It learns by bootstrapping:

using a current estimate to improve itself.

## 2. Q-Learning

**Q-learning** focuses on action values directly.

Instead of learning only how good a state is, it learns:

- how good each action is in each state

That is powerful because once the agent has good `Q(s, a)` estimates, it can choose the action with the highest value.

## 3. Why This Was Important

This was a major shift.

Earlier systems often needed:

- hand-written rules
- hand-built probabilities
- explicit transition models

Reinforcement learning showed that an agent could improve behavior by interacting with the environment and updating estimates from experience.

That is a big step toward modern learning-based AI.

## 4. But This Was Still Not the Final Form

Early reinforcement learning methods worked best in smaller or more structured settings.

They still struggled when:

- state spaces became huge
- observations became raw and unstructured
- function approximation became necessary

That limitation points forward again.

Statistics gave AI uncertainty.
Reinforcement learning gave AI experience-based improvement.
But large-scale pattern learning still needed a stronger framework.

That next step is:

**Machine Learning**.
