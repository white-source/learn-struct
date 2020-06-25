import matplotlib.pyplot as plt

import numpy as np
import random
from sklearn.cluster import KMeans

random.seed(0)

x, y = [], []
np.random.seed(0)


x = np.concatenate((x, np.random.normal(-1, 1, 15)))
y = np.concatenate((y, np.random.normal(0, 1, 15)))

x = np.concatenate((x, np.random.normal(2, 1, 15)))
y = np.concatenate((y, np.random.normal(5, 1, 15)))

x = np.concatenate((x, np.random.normal(4, 1, 15)))
y = np.concatenate((y, np.random.normal(0, 1, 15)))

#x = np.concatenate((x, np.random.normal(0, 1, 5)))
#y = np.concatenate((y, np.random.normal(3, 1, 5)))

#x, y = filt(x, y, False)
plt.scatter(x, y, s=10, facecolors='k', edgecolors='k')
plt.show()


from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs

# #############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5,
                            random_state=0)

# #############################################################################
# Compute Affinity Propagation
X = np.stack((x, y), axis=-1)

max_iters = [15, 14, 10, 8]

for idx, max_iter in enumerate(max_iters):
    af = AffinityPropagation(preference=-50, damping=0.7, max_iter=max_iter).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_

    n_clusters_ = len(cluster_centers_indices)


    from itertools import cycle
    ax = plt.subplot(220+idx+1)
    

    #for idx, row in enumerate(af.affinity_matrix_):
    #    for idy, cell in enumerate(row):
    #        print(idx, idy, cell)
    #        if cell > -5:
    #            plt.plot([X[idx][0], X[idy][0]], [X[idx][1], X[idy][1]]) 
    #print(af.cluster_centers_indices_ , af.affinity_matrix_, af.n_iter_ )

    
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        ax.plot(X[class_members, 0], X[class_members, 1], col + '.')
        ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=8)
        for x in X[class_members]:
            ax.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    ax.set_title('AP iters: %d' % max_iter)
plt.show()


