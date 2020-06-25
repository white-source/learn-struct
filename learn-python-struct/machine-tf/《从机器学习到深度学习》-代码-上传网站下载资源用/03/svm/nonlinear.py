
import math
import numpy as np
from matplotlib import pyplot as plt


def filt_circle(X, Y, in_):
    x_new, y_new = [], []
    r=1.5
    for i in range(len(X)):
        length = math.sqrt(X[i]**2 + Y[i]**2)
        print(in_, length, r)
        if in_ and (length < r-0.3):
            x_new.append(X[i])
            y_new.append(Y[i])
        elif not in_ and (length > r):
            print(length)
            x_new.append(X[i])
            y_new.append(Y[i])
    return np.array(x_new), np.array(y_new)
            

np.random.seed(1)
X = np.random.normal(0, 1, 300)
Y = np.random.normal(0, 1, 300)
x, y = filt_circle(X, Y, True)

plt.scatter(x, y, s=40, marker="o", color="r")



p, q = filt_circle(X, Y, False)
plt.scatter(p, q, s=40, marker="s", facecolors='none', edgecolors='b')

plt.show()



from mpl_toolkits.mplot3d import Axes3D				#必须引入mpl_toolkits.mplot3d
ax = plt.subplot(1, 1, 1, projection='3d')	
ax.scatter(x, y, np.sqrt(x**2+y**2), marker="o", color="r")	
ax.scatter(p, q, np.sqrt(p**2+q**2), marker="s", facecolors='none', edgecolors='b')


plt.show()

ax = plt.subplot(1, 1, 1, projection='3d')	
ax.scatter(x, y, np.sqrt(x**2+y**2), marker="o", color="r")	
ax.scatter(p, q, np.sqrt(p**2+q**2), marker="s", facecolors='none', edgecolors='b')

x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)
x, y = np.meshgrid(x, y)
ax.plot_surface(x ,y, 
                np.ones((100, 100))*1.1, color="#FFFFFF")


plt.show()
