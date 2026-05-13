"""Chapter 4.3.13: Q-Learning as a Reinforcement Learning Setup.

Q-Learning learns action values in a Markov Decision Process.
"""

import random
from collections import defaultdict


class QLearningSetup:
    """Q-Learning agent for reinforcement learning."""

    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        """
        Args:
            learning_rate: Learning rate (alpha)
            discount_factor: Future reward discounting (gamma)
            epsilon: Exploration rate for epsilon-greedy
        """
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.Q = defaultdict(lambda: {})  # Q-table: Q[state][action]

    def train(self, env, episodes=100):
        """Train Q-learning agent."""
        for episode in range(episodes):
            state = env.reset()
            done = False
            
            while not done:
                # Epsilon-greedy action selection
                if random.random() < self.epsilon:
                    action = env.sample_action()
                else:
                    action = self._best_action(state)
                
                # Take action
                next_state, reward, done = env.step(state, action)
                
                # Q-learning update
                current_q = self._get_q(state, action)
                max_next_q = max([self._get_q(next_state, a) for a in env.actions()], default=0)
                new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
                
                self._set_q(state, action, new_q)
                state = next_state

    def act(self, state):
        """Choose best action (greedy)."""
        return self._best_action(state)

    def _best_action(self, state):
        """Get best action for state."""
        if state not in self.Q or not self.Q[state]:
            return 0
        return max(self.Q[state].keys(), key=lambda a: self.Q[state][a])

    def _get_q(self, state, action):
        """Get Q-value."""
        if state not in self.Q:
            self.Q[state] = {}
        return self.Q[state].get(action, 0.0)

    def _set_q(self, state, action, value):
        """Set Q-value."""
        if state not in self.Q:
            self.Q[state] = {}
        self.Q[state][action] = value


class GridWorldEnv:
    """Simple grid world environment."""

    def __init__(self, size=5, goal=(4, 4)):
        self.size = size
        self.goal = goal
        self.agent_pos = (0, 0)

    def reset(self):
        self.agent_pos = (0, 0)
        return self.agent_pos

    def step(self, state, action):
        """Take action and return next_state, reward, done."""
        x, y = state
        
        # Move
        if action == 0:  # Up
            x = max(0, x - 1)
        elif action == 1:  # Down
            x = min(self.size - 1, x + 1)
        elif action == 2:  # Left
            y = max(0, y - 1)
        elif action == 3:  # Right
            y = min(self.size - 1, y + 1)
        
        next_state = (x, y)
        done = next_state == self.goal
        reward = 1 if done else -0.01
        
        return next_state, reward, done

    def sample_action(self):
        return random.randint(0, 3)

    def actions(self):
        return [0, 1, 2, 3]


if __name__ == "__main__":
    env = GridWorldEnv()
    agent = QLearningSetup(learning_rate=0.1, discount_factor=0.99, epsilon=0.1)
    
    agent.train(env, episodes=100)
    
    # Test
    state = env.reset()
    for _ in range(10):
        action = agent.act(state)
        state, reward, done = env.step(state, action)
        if done:
            print("Goal reached!")
            break
