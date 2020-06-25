print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

iris = datasets.load_iris()
X = iris.data
y = iris.target
# plt.subplot(131)

# for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
#     plt.scatter(X[y==label, 0], X[y==label,1], label=name, marker=m)
# plt.legend()
# plt.title("data shape:%s"%(X.shape,))

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
lda = LDA( n_components=2).fit(X, y)
X_lda = lda.transform(X)

for name, label, m in [('Setosa', 0, "<"), ('Versicolour', 1, "o"), ('Virginica', 2, ">")]:
    plt.scatter(X_lda[y==label, 0], X_lda[y==label,1], label=name, marker=m)
plt.legend()
plt.title("LDA")
print(pca.explained_variance_ratio_)
print(lda.explained_variance_ratio_)
plt.show()

