import matplotlib.pyplot as plt  
import numpy as np

from scipy.misc import derivative

sigmoid = lambda x: 1 / (1 + np.exp(-x))


plt.subplot(121)
x = np.linspace(-6,6)
plt.plot(x,sigmoid(x),'b')
plt.grid()
plt.title('sigmoid')
plt.ylim([0, 1])

plt.subplot(122)
x = np.linspace(-6, 6)
plt.plot(x,derivative(sigmoid, x, dx=1e-6),'b')
plt.grid()
plt.title('derivative of sigmoid')
plt.ylim([0, 1])

plt.legend(loc='lower right')

plt.show()
