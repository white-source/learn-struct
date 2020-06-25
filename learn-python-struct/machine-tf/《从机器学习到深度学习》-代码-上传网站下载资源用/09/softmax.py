import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def normalize(x):
    return x / x.sum(axis=0)

x = np.array([0.2, 0.2, 0.9])

print(softmax(x))
print(normalize(x))
