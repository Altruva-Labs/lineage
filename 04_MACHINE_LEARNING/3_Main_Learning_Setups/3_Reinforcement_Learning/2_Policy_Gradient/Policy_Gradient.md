# Chapter 4.3.3.2: Policy Gradient in Reinforcement Learning

Policy Gradient directly optimizes the policy using gradient ascent.

## 1. Core Idea

Uses gradient of expected reward to improve policy parameters.

## 2. How It Works

Samples trajectories, computes gradient of log-probability weighted by returns.

## 3. Strengths

- Handles continuous actions
- Can learn stochastic policies
- End-to-end optimization

## 4. Limits

- High variance gradients
- Requires many samples
- Can get stuck in local optima

## 5. What Comes Next

The limitations of classical ML lead to neural networks.