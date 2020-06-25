import numpy as np


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


centers = [(0.5, 0.5)]
def in_circle(point, center):
    return ((point[0]-center[0])**2+(point[1]-center[1])**2)**0.5<=0.5

fig = plt.figure()

for idx, num_total in enumerate((100, 1000, 10000)):
    ax = fig.add_subplot(131+idx)
    X = np.random.random(num_total)
    Y = np.random.random(num_total)

    rect = Rectangle(
        (0.0, 0.0),   # (x,y)
        1.,          # width
        1.,          # height
        edgecolor='b',
        facecolor='none'
    )
    circle1 = plt.Circle(centers[0], 0.5,edgecolor='r', facecolor='none')

    ax.add_patch(rect)
    ax.add_patch(circle1)


    Z = [in_circle((X[idx], Y[idx]), centers[0])  for idx, x in enumerate(X)]
    plt.scatter(X[Z], Y[Z], marker='+')
    plt.scatter(X[np.logical_not( Z)], Y[np.logical_not(Z)], marker='x')

    num_in = np.sum(Z)
    pi = 4.0*num_in/num_total
    plt.title("in: %s, total: %s --> pi: %s"%(num_in, num_total, pi))
plt.show()
