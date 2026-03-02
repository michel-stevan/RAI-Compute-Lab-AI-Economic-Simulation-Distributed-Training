import numpy as np

class EconomicSimulation:
    def __init__(self, num_agents=100):
        self.num_agents = num_agents
        self.wealth = np.random.normal(100, 20, num_agents)

    def step(self, inflation=0.02, shock=0):
        self.wealth *= (1 - inflation)

        if shock == 1:
            crash = np.random.uniform(0.7, 0.9, self.num_agents)
            self.wealth *= crash

        return self.wealth

    def gini(self):
        sorted_wealth = np.sort(self.wealth)
        n = self.num_agents
        cumulative = np.cumsum(sorted_wealth)
        return (n + 1 - 2 * np.sum(cumulative) / cumulative[-1]) / n
