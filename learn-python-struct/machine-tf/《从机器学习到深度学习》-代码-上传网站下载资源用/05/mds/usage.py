print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import MDS

iris = datasets.load_iris()
X = iris.data
y = iris.target

plt.subplot(121)
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X_pca[y==label, 0], X_pca[y==label,1], label=name, marker=m)
plt.legend()
plt.title("PCA")
print(pca.explained_variance_ratio_)

plt.subplot(122)
mds = MDS( n_components=2, metric=True)
X_mds = mds.fit_transform(X)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X_mds[y==label, 0], X_mds[y==label,1], label=name, marker=m)
plt.legend()
plt.title("MDS")

plt.show()

