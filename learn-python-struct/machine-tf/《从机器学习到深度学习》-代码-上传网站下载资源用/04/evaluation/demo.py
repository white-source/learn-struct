from sklearn import metrics

true_labels = [1, 1, 2, 2, 0, 0]
pred_lables = [0, 0, 1, 1, 2, 2]

print(metrics.adjusted_rand_score(true_labels, pred_lables))

pred_lables = [1, 1, 2, 2, 1, 0]

print(metrics.adjusted_rand_score(true_labels, pred_lables))

print(metrics.adjusted_mutual_info_score(true_labels, pred_lables))

print(metrics.homogeneity_score(true_labels, pred_lables))






import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics


X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
kmeans.labels_

print(metrics.silhouette_score(X, kmeans.labels_))

print(metrics.calinski_harabaz_score(X, kmeans.labels_))
