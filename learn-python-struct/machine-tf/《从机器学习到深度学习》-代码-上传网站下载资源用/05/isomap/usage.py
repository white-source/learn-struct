print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap


iris = datasets.load_iris()
X = iris.data
y = iris.target

plt.subplot(221)
X_pca = PCA( n_components=2).fit_transform(X)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X_pca[y==label, 0], X_pca[y==label,1], label=name, marker=m)
plt.legend()
plt.title("PCA")

for idx, neighbor in enumerate([2, 20, 100]):
    plt.subplot(222 + idx)
    isomap = Isomap( n_components=2, n_neighbors=neighbor)
    X_isomap = isomap.fit_transform(X)

    for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
        plt.scatter(X_isomap[y==label, 0], X_isomap[y==label,1], label=name, marker=m)
    plt.legend()
    plt.title("Isomap (n_neighbors=%d)"%neighbor)

plt.show()

