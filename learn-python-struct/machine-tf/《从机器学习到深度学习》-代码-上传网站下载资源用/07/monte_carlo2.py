import numpy as np


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


centers = [(0.5, 0.5), (0.7, 0.55), (0.6, 1.2), (1.3, 0.9)]
def in_circle(point, center):
    return ((point[0]-center[0])**2+(point[1]-center[1])**2)**0.5<=0.5

fig = plt.figure()

for idx, num_total in enumerate((100, 1000, 10000)):
    ax = fig.add_subplot(131+idx)
    X = np.random.random(num_total)*2
    Y = np.random.random(num_total)*2

    rect = Rectangle(
        (0.0, 0.0),   # (x,y)
        2.,          # width
        2.,          # height
        edgecolor='b',
        facecolor='none'
    )
    ax.add_patch(rect)

    for center in centers:
        circle = plt.Circle(center, 0.5,edgecolor='r', facecolor='none')
        ax.add_patch(circle)


    Z = []
    for idx, x in enumerate(X):
        in_ = False
        for center in centers:
            if in_circle((X[idx], Y[idx]), center):
                in_ = True
        Z.append(in_)
    plt.scatter(X[Z], Y[Z], marker='+')
    plt.scatter(X[np.logical_not( Z)], Y[np.logical_not(Z)], marker='x')

    num_in = np.sum(Z)
    space = 4.0*num_in/num_total
    plt.title("space: %s"%( space, ))
plt.show()
