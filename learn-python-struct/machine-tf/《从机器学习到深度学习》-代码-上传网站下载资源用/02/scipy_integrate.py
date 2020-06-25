# -*- coding:utf-8 -*-


import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y = lambda x: x**2+3


plt.grid(zorder=5)
plt.plot(x, y(x), label="y=x**2+3")
plt.fill_between(x[30: 90], y(x[30: 90]),  hatch="/", label="quad(y, -2, 4)")
plt.legend(loc="upper center")
plt.show()
print(integrate.quad(y, -2, 4))


Y = lambda x: x**2+3

x = np.linspace(-2,4,10)
y = Y(x)
print(integrate.trapz(y, x))

x = np.linspace(-2,4,50)
y = Y(x)
print(integrate.trapz(y, x))

x = np.linspace(-2,4,100)
y = Y(x)
print(integrate.trapz(y, x))
