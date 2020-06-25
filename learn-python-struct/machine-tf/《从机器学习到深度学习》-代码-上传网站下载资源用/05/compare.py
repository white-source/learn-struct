
from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter

from sklearn import manifold, datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

Axes3D

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(15, 8))
plt.suptitle("Dimension Reduction with %i points, %i neighbors"
             % (1000, n_neighbors), fontsize=14)


ax = fig.add_subplot(251, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)

methods = ['standard', 'ltsa', 'hessian', 'modified']
labels = ['LLE', 'LTSA', 'Hessian LLE', 'Modified LLE']

for i, method in enumerate(methods):
    if i>2:
        continue
    t0 = time()
    Y = manifold.LocallyLinearEmbedding(n_neighbors, n_components,
                                        eigen_solver='auto',
                                        method=method).fit_transform(X)
    t1 = time()
    print("%s: %.2g sec" % (methods[i], t1 - t0))

    ax = fig.add_subplot(252 + i)
    plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.title("%s (%.2g sec)" % (labels[i], t1 - t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis('tight')

    
estimators = [(manifold.Isomap(n_neighbors, n_components), "Isomap"), 
              (manifold.MDS(n_components, max_iter=100, n_init=1), "MDS"),
              (manifold.SpectralEmbedding(n_components=n_components,
                                          n_neighbors=n_neighbors), "Laplace Eigenmaps"),
              (manifold.TSNE(n_components=n_components, init='pca', random_state=0), "t-SNE"),
              (PCA(n_components), "PCA"),
              (LDA(n_components=n_components), "LDA"),
              ]

for idx, (estimator_obj, estimator_name) in enumerate(estimators):
    # estimator_obj, estimator_name = estimator[0], estimator[1]
    t0 = time()
    if estimator_name=="LDA":
        Y = estimator_obj.fit_transform(X, (color).astype(int))
    else:
        Y = estimator_obj.fit_transform(X)
    t1 = time()
    print("%s: %.2g sec" % (estimator_name, t1 - t0))
    ax = fig.add_subplot(2, 5, 5+idx)
    plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.title("%s (%.2g sec)" % (estimator_name, t1 - t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis('tight')
    
plt.show()
