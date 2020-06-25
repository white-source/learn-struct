import numpy as np

from sklearn import datasets
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X_train,X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.4, random_state=0)

n_classes = len(np.unique(y_train))

gmm = GaussianMixture(n_components=3, covariance_type="diag",
                      max_iter=20, random_state=0)
gmm.fit(X_train)

print(gmm.n_iter_)

print(gmm.weights_)
print(gmm.means_)
print(gmm.covariances_)

print(gmm.predict(X_test[:1]))
print(gmm.predict_proba(X_test[:1]))
