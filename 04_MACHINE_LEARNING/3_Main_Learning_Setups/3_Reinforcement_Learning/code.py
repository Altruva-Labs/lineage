"""From-scratch tabular Q-learning demo."""

from random import Random


class LineWorld:
    def __init__(self, length=5):
        self.length = length
        self.start_state = 0
        self.goal_state = length - 1
        self.state = self.start_state

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action):
        if action == 0:
            self.state = max(0, self.state - 1)
        else:
            self.state = min(self.goal_state, self.state + 1)

        reward = 1.0 if self.state == self.goal_state else -0.01
        done = self.state == self.goal_state
        return self.state, reward, done

    def available_actions(self):
        return [0, 1]


class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate=0.2, gamma=0.95, epsilon=0.2, seed=0):
        self.q_table = [[0.0 for _ in range(n_actions)] for _ in range(n_states)]
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.random = Random(seed)

    def choose_action(self, state):
        if self.random.random() < self.epsilon:
            return self.random.choice([0, 1])
        return self.greedy_action(state)

    def greedy_action(self, state):
        values = self.q_table[state]
        return max(range(len(values)), key=lambda action: values[action])

    def update(self, state, action, reward, next_state, done):
        best_next = 0.0 if done else max(self.q_table[next_state])
        target = reward + self.gamma * best_next
        current = self.q_table[state][action]
        self.q_table[state][action] = current + self.learning_rate * (target - current)


def run_reinforcement_demo(episodes=200):
    env = LineWorld(length=5)
    agent = QLearningAgent(n_states=5, n_actions=2)

    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state

    print("Q-learning in a simple line world\n")
    print("Q-table:")
    for state, values in enumerate(agent.q_table):
        print(state, [round(value, 3) for value in values])

    print("\nGreedy policy:")
    policy = []
    for state in range(env.length - 1):
        action = agent.greedy_action(state)
        policy.append("right" if action == 1 else "left")
    print(policy)


if __name__ == "__main__":
    run_reinforcement_demo()
