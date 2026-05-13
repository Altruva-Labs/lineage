"""Chapter 4.3.17: Proximal Policy Optimization as a Reinforcement Learning Setup."""

import random
import math


class SimplePolicy:
    """Simple neural network policy."""

    def __init__(self, state_dim, action_dim, learning_rate=0.001):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        
        # Policy network weights
        self.W1 = [[random.gauss(0, 0.1) for _ in range(state_dim)] for _ in range(32)]
        self.b1 = [0.0] * 32
        
        self.W2 = [[random.gauss(0, 0.1) for _ in range(32)] for _ in range(action_dim)]
        self.b2 = [0.0] * action_dim
        
        # Value network weights
        self.V_W1 = [[random.gauss(0, 0.1) for _ in range(state_dim)] for _ in range(32)]
        self.V_b1 = [0.0] * 32
        
        self.V_W2 = [[random.gauss(0, 0.1)] for _ in range(32)]
        self.V_b2 = 0.0

    def softmax(self, x):
        """Softmax activation."""
        max_x = max(x)
        exp_x = [math.exp(xi - max_x) for xi in x]
        sum_exp = sum(exp_x)
        return [e / sum_exp for e in exp_x]

    def forward_policy(self, state):
        """Forward pass for policy."""
        h = [self.b1[i] + sum(self.W1[i][j] * state[j] for j in range(len(state)))
             for i in range(len(self.b1))]
        h = [max(0, hi) for hi in h]  # ReLU
        
        logits = [self.b2[i] + sum(self.W2[i][j] * h[j] for j in range(len(h)))
                  for i in range(self.action_dim)]
        return self.softmax(logits)

    def forward_value(self, state):
        """Forward pass for value."""
        h = [self.V_b1[i] + sum(self.V_W1[i][j] * state[j] for j in range(len(state)))
             for i in range(len(self.V_b1))]
        h = [max(0, hi) for hi in h]  # ReLU
        
        value = self.V_b2 + sum(self.V_W2[i][0] * h[i] for i in range(len(h)))
        return value

    def update(self, state, action, advantage, old_prob, epsilon=0.2):
        """PPO update with clipped objective."""
        probs = self.forward_policy(state)
        new_prob = probs[action]
        
        ratio = new_prob / (old_prob + 1e-8)
        clipped_ratio = max(1 - epsilon, min(ratio, 1 + epsilon))
        
        loss = -min(ratio * advantage, clipped_ratio * advantage)
        
        # Simplified update
        grad = loss / (abs(loss) + 1e-8)
        for i in range(self.action_dim):
            self.b2[i] -= self.learning_rate * grad


class PPOSetup:
    """Proximal Policy Optimization agent."""

    def __init__(self, state_dim, action_dim):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.policy = SimplePolicy(state_dim, action_dim)
        self.gamma = 0.99
        self.gae_lambda = 0.95

    def collect_trajectories(self, env, steps=100):
        """Collect experience trajectories."""
        trajectories = []
        state = env.reset()
        
        for _ in range(steps):
            probs = self.policy.forward_policy(state)
            action = self.sample_action(probs)
            prob = probs[action]
            
            next_state, reward, done = env.step(state, action)
            
            value = self.policy.forward_value(state)
            next_value = self.policy.forward_value(next_state)
            
            advantage = reward + self.gamma * next_value - value
            
            trajectories.append((state, action, reward, advantage, prob))
            
            state = next_state if not done else env.reset()
        
        return trajectories

    def sample_action(self, probs):
        """Sample action from policy."""
        r = random.random()
        cumsum = 0
        for a, p in enumerate(probs):
            cumsum += p
            if r < cumsum:
                return a
        return len(probs) - 1

    def train(self, env, episodes=20, steps_per_episode=50):
        """Train PPO."""
        for episode in range(episodes):
            trajectories = self.collect_trajectories(env, steps_per_episode)
            
            for state, action, reward, advantage, old_prob in trajectories:
                self.policy.update(state, action, advantage, old_prob)
            
            avg_reward = sum(t[2] for t in trajectories) / len(trajectories)
            print(f"Episode {episode}, Avg Reward: {avg_reward:.3f}")


if __name__ == "__main__":
    class SimpleEnv:
        def reset(self):
            return [random.gauss(0, 1) for _ in range(4)]
        
        def step(self, state, action):
            reward = state[action % 4] if action else -state[0]
            return state, reward, random.random() < 0.1
    
    env = SimpleEnv()
    agent = PPOSetup(state_dim=4, action_dim=2)
    agent.train(env)
    print("PPO training complete!")
