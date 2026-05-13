"""Chapter 4.3.16: Deep Q-Networks as a Reinforcement Learning Setup."""

import random
import math


class SimpleNeuralNetwork:
    """Simple neural network for function approximation."""

    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate=0.01):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.learning_rate = learning_rate
        
        # Weights
        self.W1 = [[random.gauss(0, 0.1) for _ in range(input_dim)] for _ in range(hidden_dim)]
        self.b1 = [0.0] * hidden_dim
        
        self.W2 = [[random.gauss(0, 0.1) for _ in range(hidden_dim)] for _ in range(output_dim)]
        self.b2 = [0.0] * output_dim

    def forward(self, x):
        """Forward pass."""
        # Hidden layer
        h = [self.b1[i] + sum(self.W1[i][j] * x[j] for j in range(len(x)))
             for i in range(self.hidden_dim)]
        h = [max(0, hi) for hi in h]  # ReLU
        
        # Output layer
        q = [self.b2[i] + sum(self.W2[i][j] * h[j] for j in range(len(h)))
             for i in range(self.output_dim)]
        
        return q, h

    def update(self, x, target_q):
        """Update weights using gradient descent."""
        q, h = self.forward(x)
        
        # Simplified gradient update
        for i in range(self.output_dim):
            error = q[i] - target_q[i]
            
            # Output layer gradients
            self.b2[i] -= self.learning_rate * error
            for j in range(self.hidden_dim):
                self.W2[i][j] -= self.learning_rate * error * h[j]


class DQNSetup:
    """Deep Q-Network agent."""

    def __init__(self, state_dim, action_dim, learning_rate=0.01):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.q_network = SimpleNeuralNetwork(state_dim, 64, action_dim, learning_rate)
        self.epsilon = 0.1

    def train(self, env, episodes=50):
        """Train DQN."""
        for episode in range(episodes):
            state = env.reset()
            done = False
            
            while not done:
                # Epsilon-greedy
                if random.random() < self.epsilon:
                    action = random.randint(0, self.action_dim - 1)
                else:
                    q_vals, _ = self.q_network.forward(state)
                    action = max(range(len(q_vals)), key=lambda a: q_vals[a])
                
                next_state, reward, done = env.step(state, action)
                
                # Compute target
                next_q_vals, _ = self.q_network.forward(next_state)
                max_next_q = max(next_q_vals) if next_q_vals else 0
                target_q = [reward + 0.99 * max_next_q if a == action else 0
                           for a in range(self.action_dim)]
                
                # Update network
                self.q_network.update(state, target_q)
                
                state = next_state

    def act(self, state):
        """Choose best action."""
        q_vals, _ = self.q_network.forward(state)
        return max(range(len(q_vals)), key=lambda a: q_vals[a])


if __name__ == "__main__":
    class SimpleEnv:
        def reset(self):
            return [random.gauss(0, 1) for _ in range(4)]
        
        def step(self, state, action):
            reward = state[0] if action else -state[0]
            return state, reward, random.random() < 0.2
    
    env = SimpleEnv()
    agent = DQNSetup(state_dim=4, action_dim=2)
    agent.train(env)
    print("DQN training complete!")
