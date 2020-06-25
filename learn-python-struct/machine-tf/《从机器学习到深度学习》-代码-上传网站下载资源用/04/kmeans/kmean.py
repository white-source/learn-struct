
import matplotlib.pyplot as plt

import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)

print(kmeans.predict([[0, 0], [4, 4]]))

print(kmeans.cluster_centers_)
print(kmeans.inertia_)


print(kmeans.transform([[4, 2], [4, 4]]))


print(kmeans.score([[2, 2], [5, 3]]))
