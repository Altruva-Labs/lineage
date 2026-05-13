# Chapter 4.3.3.3: SARSA (State-Action-Reward-State-Action)

SARSA is an on-policy temporal difference learning algorithm for reinforcement learning.
It learns a value function for state-action pairs by updating based on the actual policy being followed.

## 1. Core Idea

SARSA updates the Q-value using the next state and the action taken in that state (hence the acronym: State-Action-Reward-State-Action).
It is on-policy, meaning it learns from actions taken by the current policy.

## 2. How It Works

- Initialize Q-values for all state-action pairs.
- For each episode:
  - Observe current state S.
  - Choose action A using the current policy (e.g., ε-greedy).
  - Take action A, observe reward R and next state S'.
  - Choose next action A' using the current policy.
  - Update Q(S, A) ← Q(S, A) + α [R + γ Q(S', A') - Q(S, A)].
- Repeat until convergence.

## 3. Strengths

- Simple to implement.
- Converges to optimal policy in tabular settings.
- On-policy nature ensures it learns from the behavior policy.

## 4. Limits

- Can be slow in large state spaces.
- Requires exploration (e.g., ε-greedy) to avoid suboptimal policies.
- Off-policy methods like Q-Learning may be more sample-efficient.

## 5. What Comes Next

SARSA is closely related to Q-Learning; the key difference is on-policy vs. off-policy updates.
