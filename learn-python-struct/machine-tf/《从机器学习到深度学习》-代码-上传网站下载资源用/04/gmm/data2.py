from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

n_samples = 800
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,
                                      noise=.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.1)
blobs = datasets.make_blobs(n_samples=n_samples//3, random_state=8, n_features=2, centers=[[2.8, 0.9]] ,cluster_std=[[0.13]])
no_structure = (np.random.rand(150, 2)+[-0.2, -0.3])*[7, 2], None


s_curve = datasets.make_s_curve(n_samples=n_samples//2)
s_curve_t = [s_curve[0] + [0, 2.7, 0], s_curve[1]]
s_curve_t = [s_curve_t[0] *[1, 1, 0.2], s_curve[1]]
print(s_curve[0][:,:2])
X, Y = noisy_moons
#X, Y = no_structure
X = np.concatenate((X, blobs[0]))
Y = np.concatenate((Y, blobs[1]))
X = np.concatenate((X, s_curve_t[0][:,1:]))
Y = np.concatenate((Y, s_curve[1]))
X = np.concatenate((X, no_structure[0]))

print(X, Y)
#plt.scatter(X[:, :1], X[:, 1:])

dbscan = DBSCAN(eps=0.2, min_samples=100).fit(X)
labels = db.labels_

unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k =-1:
        plt.scatter((X[:, :1][labels==k], X[:, 1:][labels==k]), color='k')
    else:
        plt.scatter((X[:, :1][labels==k], X[:, 1:][labels==k]), color=col)

plt.show()
