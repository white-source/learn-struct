import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 0], [0, 100]]

x, y = np.random.multivariate_normal(mean, cov, 5000).T

np.random.seed(1)
X = (np.random.rand(20)+0.5)/2 

Y = X*0.4 + np.random.rand(20)/5 + 0.3

# X1 = (np.random.rand(20)+0.5)/2 +0.3
# Y1 = X*0.7 + np.random.rand(20)/5 + 0.2
# X = np.concatenate((X, X1))
# Y = np.concatenate((Y, Y1))

T = np.array(X/2+Y>0.7)
# T = np.random.choice(2, X.shape[0])
# T = np.concatenate((np.zeros(X.shape[0]//2), np.ones(X.shape[0]//2)))
T = T + np.zeros(X.shape[0])
T[14] = 1
plt.scatter(X[T==0], Y[T==0], s=20, color='r', marker='o')
plt.scatter(X[T==1], Y[T==1], s=20, color='b', marker='x')


plt.xlim((0.2, 0.8))
plt.ylim((0.2, 0.8))
print(X, Y)
plt.show()

# plt.subplot(121)
# plt.scatter(X[T==0], Y[T==0], s=20, color='r')
# plt.scatter(X[T==1], Y[T==1], s=20, color='b')


# for idx, x in enumerate(X):
#     plt.plot((x, 0), (Y[idx], Y[idx]), 'k--', linewidth=1)
#     plt.scatter((0,), (Y[idx],), color='k', s=40)

# plt.xlim((0, 1))
# plt.ylim((0, 1))

# plt.subplot(122)
# plt.scatter(X, Y, s=20)
# for idx, x in enumerate(X):
#     plt.plot((x, x), (Y[idx], 0), 'k--', linewidth=1)
#     plt.scatter((x,), (0,), color='k', s=40)
# plt.xlim((0, 1))
# plt.ylim((0, 1))
# plt.show()

plt.subplot(121)

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X.reshape(-1, 1), Y)
print(reg.coef_, reg.intercept_)
def f(x):
    return x*reg.coef_[0]+reg.intercept_

plt.scatter(X[T==0], Y[T==0], s=20, color='r', marker='o')
plt.scatter(X[T==1], Y[T==1], s=20, color='b', marker='x')
plt.plot((0.2, 0.8), (f(0.2), f(0.8)), 'k', linewidth=2)
for idx, x in enumerate(X):
    coef = -1/reg.coef_[0]
    cept = Y[idx]-coef*x
    c_x = (cept-reg.intercept_)/(reg.coef_[0]-coef)
    c_y = f(c_x)
    plt.plot((x, c_x), (Y[idx], c_y), 'k--', linewidth=1)
    plt.scatter((c_x,), (c_y,), color='k', s=20)

plt.xlim((0.2, 0.8))
plt.ylim((0.2, 0.8))
plt.title("PCA")

plt.subplot(122)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(solver="svd", n_components=2).fit(np.concatenate((X.reshape(-1, 1), Y.reshape(-1, 1)), axis=1), T)

from sklearn import linear_model
print(lda.coef_, lda.intercept_, T)

lda_coef = lda.coef_[0][1]/lda.coef_[0][0]
lda_intercept = lda.intercept_[0] /lda.coef_[0][0]
def f(x):
    return x*lda_coef + lda_intercept

plt.scatter(X[T==0], Y[T==0], s=20, color='r', marker='o')
plt.scatter(X[T==1], Y[T==1], s=20, color='b', marker='x')
plt.plot((0.41, 0.45), (f(0.41), f(0.45)), 'k', linewidth=2)
for idx, x in enumerate(X):
    coef = -1/lda_coef
    cept = Y[idx]-coef*x
    c_x = (cept-lda_intercept)/(lda_coef-coef)
    c_y = f(c_x)
    plt.plot((x, c_x), (Y[idx], c_y), T[idx]==0 and 'r--' or 'b--', linewidth=1)
    plt.scatter((c_x,), (c_y,), color=(T[idx]==0 and 'k' or 'k'), s=20)

plt.xlim((0.2, 0.8))
plt.ylim((0.2, 0.8))
plt.title("LDA")
plt.show()


