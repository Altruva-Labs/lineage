"""Chapter 4.3.14: Policy Gradient as a Reinforcement Learning Setup."""

import random
import math


class PolicyGradientSetup:
    """Policy gradient agent using REINFORCE algorithm."""

    def __init__(self, state_dim, action_dim, learning_rate=0.01):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        
        # Policy weights
        self.weights = [[random.gauss(0, 0.1) for _ in range(state_dim)]
                       for _ in range(action_dim)]
        self.bias = [0.0] * action_dim

    def train(self, env, episodes=50):
        """Train using REINFORCE."""
        for episode in range(episodes):
            trajectory = []
            state = env.reset()
            done = False
            
            while not done:
                action_probs = self._compute_action_probs(state)
                action = self._sample_action(action_probs)
                next_state, reward, done = env.step(state, action)
                
                trajectory.append((state, action, reward))
                state = next_state
            
            # Compute returns
            returns = []
            cumulative = 0
            for state, action, reward in reversed(trajectory):
                cumulative = reward + 0.99 * cumulative
                returns.insert(0, cumulative)
            
            # Update policy
            for t, (state, action, _) in enumerate(trajectory):
                self._update_policy(state, action, returns[t])

    def act(self, state):
        """Choose action greedily."""
        probs = self._compute_action_probs(state)
        return max(range(len(probs)), key=lambda a: probs[a])

    def _compute_action_probs(self, state):
        """Compute action probabilities."""
        logits = [self.bias[a] + sum(self.weights[a][i] * state[i] 
                                    for i in range(len(state)))
                 for a in range(self.action_dim)]
        
        # Softmax
        max_logit = max(logits)
        exp_logits = [math.exp(l - max_logit) for l in logits]
        sum_exp = sum(exp_logits)
        return [e / sum_exp for e in exp_logits]

    def _sample_action(self, probs):
        """Sample action from probability distribution."""
        r = random.random()
        cumsum = 0
        for a, p in enumerate(probs):
            cumsum += p
            if r < cumsum:
                return a
        return len(probs) - 1

    def _update_policy(self, state, action, return_val):
        """Update policy using gradient."""
        probs = self._compute_action_probs(state)
        
        for a in range(self.action_dim):
            advantage = return_val if a == action else 0
            
            for i in range(len(state)):
                gradient = (1 if a == action else 0) - probs[a]
                self.weights[a][i] += self.learning_rate * gradient * state[i] * return_val
            
            self.bias[a] += self.learning_rate * gradient * return_val


if __name__ == "__main__":
    # Simple environment simulator
    class SimpleEnv:
        def reset(self):
            return [random.gauss(0, 1) for _ in range(4)]
        
        def step(self, state, action):
            reward = state[0] if action == 0 else -state[0]
            return state, reward, random.random() < 0.2
    
    env = SimpleEnv()
    agent = PolicyGradientSetup(state_dim=4, action_dim=2)
    agent.train(env, episodes=20)
    print("Policy Gradient training complete!")
