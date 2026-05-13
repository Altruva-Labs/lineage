# Chapter 4.3.3.1: Q-Learning in Reinforcement Learning

Q-Learning learns a value function for state-action pairs.

## 1. Core Idea

Updates Q-values based on rewards and future expected rewards.

## 2. How It Works

Q(s,a) ← Q(s,a) + alpha * (r + gamma * max_a' Q(s',a') - Q(s,a))

## 3. Strengths

- Model-free
- Learns optimal policy
- Handles stochastic environments

## 4. Limits

- Can be slow to converge
- Requires exploration
- High memory for large state spaces

## 5. What Comes Next

Policy Gradient optimizes policy directly.