from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt


n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
                                      noise=.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

X, Y = noisy_moons
#X, Y = no_structure
print(Y)


plt.scatter(X[:, :1][Y==1], X[:, 1:][Y==1])
plt.show()
