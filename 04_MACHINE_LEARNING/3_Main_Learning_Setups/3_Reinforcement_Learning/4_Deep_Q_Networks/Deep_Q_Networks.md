# Chapter 4.3.3.4: Deep Q Networks (DQN)

Deep Q Networks combine Q-Learning with deep neural networks to handle high-dimensional state spaces.
This breakthrough enabled reinforcement learning to scale to complex environments like video games.

## 1. Core Idea

Instead of a tabular Q-table, DQN uses a neural network to approximate the Q-function.
It learns to predict Q-values for state-action pairs from raw inputs like pixels.

## 2. How It Works

- Use a deep neural network as the Q-function approximator.
- Employ experience replay: store transitions (S, A, R, S') in a buffer and sample mini-batches for training.
- Use a target network (copy of the main network) to stabilize learning.
- Update the network to minimize the loss: [R + γ max_a' Q_target(S', a') - Q(S, A)]^2.
- Incorporate ε-greedy exploration.

## 3. Strengths

- Handles continuous or high-dimensional states (e.g., images).
- Achieved superhuman performance in games like Atari.
- Experience replay improves sample efficiency.

## 4. Limits

- Can be unstable without techniques like target networks and replay.
- Requires careful hyperparameter tuning.
- Struggles with continuous action spaces (needs extensions like DDPG).

## 5. What Comes Next

DQN paved the way for more advanced deep RL methods, including policy-based approaches like PPO.
