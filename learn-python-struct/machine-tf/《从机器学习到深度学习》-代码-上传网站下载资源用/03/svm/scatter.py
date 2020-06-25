from sklearn import svm

X = [[-2,], [-1,], [0], [1], [2, ], [3, ]]
y = [0, 0, 0, 0, 1, 2,]
clf = svm.SVC(C=100)
clf.fit(X, y)

print(clf.predict([[1, ]]))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

random.seed(0)
def filt(x, y, small):
    return x, y
    new_x = []
    new_y = []
    for i in range(len(x)):
        sum_ = x[i] + y[i]
        if small and sum_ < 11:
            if sum_> 10:
                if random.randint(0, 9) >1:
                    continue
            new_x.append(x[i])
            new_y.append(y[i])
        elif not small and sum_ > 16:
            if sum_< 17:
                if random.randint(0, 9) >1:
                    continue
            new_x.append(x[i])
            new_y.append(y[i])
            
    return new_x, new_y
                
            
np.random.seed(0)
x = np.random.normal(3, 2.8, 200)
y = np.random.normal(3, 1.8, 200)
x, y = filt(x, y, True)
plt.scatter(x, y, s=40, marker="o", color="r")


x = np.random.normal(14, 2.8, 200)
y = np.random.normal(14, 1.8, 200)
x, y = filt(x, y, False)
plt.scatter(x, y, s=40, marker="s", facecolors='none', edgecolors='b')


plt.show()



