import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(0, 10, 100)
y = np.linspace(-10, 0, 100)
z = np.sin(x+y)

ax = plt.subplot(1, 1, 1, projection="3d")
ax.plot(x, y, z)


ax = plt.subplot(1, 1, 1, projection="3d")
ax.scatter(x, y, np.sin(x+y), c="r", marker = ">")
ax.scatter(x, y, np.cos(x+y), c="b", marker = "<")


x = np.linspace(0, 10, 100)
y = np.linspace(-5, 0, 100)
x, y = np.meshgrid(x, y)
z = np.sin(x+y)
ax = plt.subplot(1, 1, 1, projection="3d")
ax.plot_surface(x, y, z, cmap= "Spectral")
plt.show()
