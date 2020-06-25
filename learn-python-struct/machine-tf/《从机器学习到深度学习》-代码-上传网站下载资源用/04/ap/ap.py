import matplotlib.pyplot as plt

import numpy as np
import random
from sklearn.cluster import KMeans

X = np.array([[1, 2], [1, 4], [0.7, 0], [0.2, 5], [0, 4], [1.3, 0],
              [0.1, 2], [0, 4], [0.4, 0]])

from sklearn.cluster import AffinityPropagation

af= AffinityPropagation(preference=-5, ).fit(X)
print(af.labels_)

af2= AffinityPropagation(preference=-8, ).fit(X)
print(af2.labels_)
print(af2.n_iter_)
print(af2.cluster_centers_)

ax = plt.subplot(131)
ax.scatter(X[:,:1], X[:,1:])
ax.set_title('samples')

from itertools import cycle

cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

ax = plt.subplot(132)
    
    
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    ax.plot(X[class_members, 0], X[class_members, 1], col + '.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=8)
    for x in X[class_members]:
        ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

ax.set_title('preference: -5')



cluster_centers_indices = af2.cluster_centers_indices_
labels = af2.labels_

n_clusters_ = len(cluster_centers_indices)

ax = plt.subplot(133)

    
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    ax.plot(X[class_members, 0], X[class_members, 1], col + '.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=8)
    for x in X[class_members]:
        ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

ax.set_title('preference: -8')


plt.show()

