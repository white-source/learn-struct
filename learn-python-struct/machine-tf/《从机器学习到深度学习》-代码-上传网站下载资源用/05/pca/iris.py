print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause


import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn import datasets

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
y = iris.target
plt.subplot(121)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X[y==label, 0], X[y==label,1], label=name, marker=m)
plt.legend()
plt.title("data shape:%s"%(X.shape,))

plt.subplot(122)
pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X[y==label, 0], X[y==label,1], label=name, marker=m)

plt.legend()
plt.title("data shape:%s"%(X.shape,))

plt.show()
