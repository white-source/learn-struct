import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 0], [0, 100]]

x, y = np.random.multivariate_normal(mean, cov, 5000).T

np.random.seed(1)
X = (np.random.rand(20)+0.5)/2

Y = X*0.4 + np.random.rand(20)/5 + 0.3

plt.scatter(X, Y, s=20)

plt.xlim((0, 1))
plt.ylim((0, 1))
print(X, Y)
plt.show()

plt.subplot(121)
plt.scatter(X, Y, s=20)


for idx, x in enumerate(X):
    plt.plot((x, 0), (Y[idx], Y[idx]), 'k--', linewidth=1)
    plt.scatter((0,), (Y[idx],), color='k', s=40)

plt.xlim((0, 1))
plt.ylim((0, 1))

plt.subplot(122)
plt.scatter(X, Y, s=20)
for idx, x in enumerate(X):
    plt.plot((x, x), (Y[idx], 0), 'k--', linewidth=1)
    plt.scatter((x,), (0,), color='k', s=40)
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.show()

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X.reshape(-1, 1), Y)
print(reg.coef_, reg.intercept_)
def f(x):
    return x*reg.coef_[0]+reg.intercept_

plt.scatter(X, Y, s=20)
plt.plot((0.2, 0.8), (f(0.2), f(0.8)), 'k', linewidth=2)
for idx, x in enumerate(X):
    coef = -1/reg.coef_[0]
    cept = Y[idx]-coef*x
    c_x = (cept-reg.intercept_)/(reg.coef_[0]-coef)
    c_y = f(c_x)
    plt.plot((x, c_x), (Y[idx], c_y), 'k--', linewidth=1)
    plt.scatter((c_x,), (c_y,), color='k', s=40)

plt.xlim((0, 1))
plt.ylim((0, 1))
plt.show()


from sklearn.decomposition import PCA
pca = PCA(n_components=1).fit(np.concatenate((X.reshape(-1, 1), Y.reshape(-1, 1)), axis=1))
print(pca.components_)
print(pca.explained_variance_, pca.singular_values_)
