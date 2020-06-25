import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.utils import shuffle

X = [[0, 0], [2, 1], [5, 4]]
y = [0, 2, 2]

clf = SGDClassifier(penalty="l2", max_iter=10000)
clf.fit(X, y)

print(clf.predict([[4, 3]]))


print(clf.coef_)
print(clf.intercept_)


from sklearn.linear_model import SGDRegressor

reg = SGDRegressor( penalty="l2", max_iter=10000)
reg.fit(X, y)

print(reg.predict([[4, 3]]))
print(reg.coef_)
print(reg.intercept_)


print("-------")
from random import randint
reg2 = SGDRegressor(loss="squared_loss", penalty="none", tol=1e-15)

X=np.linspace(0, 1, 50)
y = X*2 #+ np.random.normal(0, 0.15, len(X))

X=X.reshape(-1, 1)
print(X.shape, X[0:1], y[0:1])
reg2.partial_fit(X[0:1], y[0:1])
for i in range(10000):
    # idx = randint(0, len(y)-1)
    # reg2.partial_fit(X[idx:idx+1], y[idx: idx+1], np.ones(1)*0.02)
    i = randint(0, 9)
    reg2.partial_fit(X[5*i: 5*(i+1)], y[5*i: 5*(i+1)])


print(reg2.coef_)
print(reg2.intercept_)

print(reg2.predict([[0.6]]))


