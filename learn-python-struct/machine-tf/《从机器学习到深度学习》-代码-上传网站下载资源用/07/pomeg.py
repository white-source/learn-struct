from pomegranate import *
import numpy as np

# model = BayesianNetwork("Monty Hall Problem")
# a = NormalDistribution(1, 1)
# b = NormalDistribution(1, 1)

# a = BetaDistribution(1, 1)
# b = BetaDistribution(1, 1)
# model.add_states(a, b)
# model.bake()

X = [[1,0.1, 1], [2, 2.3, 2], [2, 1., 2], [3, 0.2, 3]]
model = BayesianNetwork.from_samples(X, algorithm='exact')
model.fit(X)
print(model)
