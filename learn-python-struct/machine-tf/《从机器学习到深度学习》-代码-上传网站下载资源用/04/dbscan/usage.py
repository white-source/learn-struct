from sklearn import datasets
from sklearn.cluster import DBSCAN
import numpy as np


blobs1 = datasets.make_blobs(n_samples=10, random_state=8, n_features=2, centers=[[0, 0]] ,cluster_std=[[0.1]])
blobs2 = datasets.make_blobs(n_samples=10, random_state=8, n_features=2, centers=[[1, 1]] ,cluster_std=[[0.1]])

X = np.concatenate((blobs1[0], blobs2[0]))

dbscan = DBSCAN(eps=0.2, min_samples=5).fit(X)
print(dbscan.labels_)
print(dbscan.components_)
