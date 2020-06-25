from scipy import signal
import numpy as np

x = np.array([1.0, 2.5, 3.0, 2.0])
h = np.array([0.7, 1.3])

print(signal.convolve(x, h))


x = np.array([[1.0, 2.5, 3.0, 2.0], [2.0, -0.3, 9.1, 5.8], [3.7, 2.5, 2.0, 4.2]])
h = np.array([[0.7, 1.3, 1], [4.7, 5.0, 1]])

print(signal.convolve(x, h))
