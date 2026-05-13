"""Chapter 4.3.15: SARSA as a Reinforcement Learning Setup.

State-Action-Reward-State-Action (on-policy temporal difference learning).
"""

import random
from collections import defaultdict


class SARSASetup:
    """SARSA agent --- on-policy temporal difference learning."""

    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.Q = defaultdict(lambda: {})

    def train(self, env, episodes=100):
        """Train SARSA agent."""
        for episode in range(episodes):
            state = env.reset()
            action = self._epsilon_greedy(state)
            done = False
            
            while not done:
                next_state, reward, done = env.step(state, action)
                next_action = self._epsilon_greedy(next_state)
                
                # SARSA update (on-policy)
                current_q = self._get_q(state, action)
                next_q = self._get_q(next_state, next_action)
                new_q = current_q + self.learning_rate * (reward + self.discount_factor * next_q - current_q)
                
                self._set_q(state, action, new_q)
                
                state = next_state
                action = next_action

    def act(self, state):
        """Choose best action (greedy)."""
        if state not in self.Q or not self.Q[state]:
            return 0
        return max(self.Q[state].keys(), key=lambda a: self.Q[state][a])

    def _epsilon_greedy(self, state):
        """Epsilon-greedy action selection."""
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        return self.act(state)

    def _get_q(self, state, action):
        if state not in self.Q:
            self.Q[state] = {}
        return self.Q[state].get(action, 0.0)

    def _set_q(self, state, action, value):
        if state not in self.Q:
            self.Q[state] = {}
        self.Q[state][action] = value


class SimpleGridEnv:
    """Grid environment."""
    def reset(self):
        return (0, 0)
    
    def step(self, state, action):
        x, y = state
        if action == 0:
            x = max(0, x - 1)
        elif action == 1:
            x = min(4, x + 1)
        elif action == 2:
            y = max(0, y - 1)
        else:
            y = min(4, y + 1)
        
        next_state = (x, y)
        reward = 1 if next_state == (4, 4) else -0.01
        done = next_state == (4, 4)
        return next_state, reward, done


if __name__ == "__main__":
    env = SimpleGridEnv()
    agent = SARSASetup()
    agent.train(env)
    print("SARSA training complete!")
