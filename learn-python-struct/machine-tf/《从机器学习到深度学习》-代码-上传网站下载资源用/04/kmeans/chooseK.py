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


ks = [i+1 for i in range(7)]
cs = []
for k in ks:
    kmeans = KMeans(n_clusters=k).fit(np.stack((x, y), axis=-1))
    cs.append(kmeans.inertia_)

plt.plot(ks, cs)
plt.show()




colors = ["r", "g", "b"]
markers = ["o", "<", ">"]
init_centers = np.array([[2, 1], [0, 1], [1, 0]])
kmeans = KMeans(n_clusters=3, random_state=1, max_iter=10 ,n_init=1, init=init_centers).fit(np.stack((x, y), axis=-1))
kmeans.labels_

for xp, yp, c, m in zip(x, y, [colors[i] for i in kmeans.labels_], [markers[i] for i in kmeans.labels_]):
    plt.scatter(xp, yp, s=30, color=c, marker=m)

centers = kmeans.cluster_centers_
print(centers[:, :1].flatten(), centers[:, 1:].flatten())
print(kmeans.inertia_)
for cp, c, m in zip(centers, colors, markers):
    plt.scatter(cp[0], cp[1], color = c, s=500, marker=m)#(5, 1))

plt.show()



