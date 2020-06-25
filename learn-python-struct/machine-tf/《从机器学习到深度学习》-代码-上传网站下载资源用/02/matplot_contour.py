import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 2, 100)
y = np.linspace(-1, 2, 50)
z = y.reshape((y.size, 1))*x
z = np.sin(z)

#cs = plt.contour(x, y, z, extent = [np.min(x), np.max(x), np.min(y), np.max(y)])
#plt.clabel(cs)


ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

cs = ax1.contour(x, y, z, extent = [np.min(x)/2, np.max(x)/2, np.min(y)/2, np.max(y)/2])
ax1.clabel(cs)
ax2.contourf(x, y, z)

ax1.set_title('contour()')
ax2.set_title('contourf()')

plt.show()
