# Chapter 4.3.3.5: Proximal Policy Optimization (PPO)

PPO is a popular policy gradient method that improves stability and sample efficiency in reinforcement learning.
It is widely used in modern RL applications, including robotics and game playing.

## 1. Core Idea

PPO directly optimizes the policy by estimating gradients of the expected reward.
It uses a clipped surrogate objective to prevent large policy updates that could destabilize learning.

## 2. How It Works

- Collect trajectories using the current policy.
- Compute advantages (e.g., using Generalized Advantage Estimation).
- Optimize the policy using a clipped objective: minimize the clipped version of the ratio of new to old policy probabilities.
- Update the value function (often a critic network) to predict returns.
- Repeat with multiple epochs on the same data for better sample efficiency.

## 3. Strengths

- Stable and easy to implement.
- Works well on continuous action spaces.
- Achieves state-of-the-art performance in many environments.

## 4. Limits

- Can be computationally intensive for very large action spaces.
- Requires careful tuning of clipping parameters.
- May not be as sample-efficient as off-policy methods in some cases.

## 5. What Comes Next

PPO represents a mature point in policy gradient methods.
Further advancements include multi-agent RL and integration with other learning paradigms.
