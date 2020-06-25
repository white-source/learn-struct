import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

func = lambda x: x[0]**3+x[1]**3 + np.cos(x[2]+1)

x0 = np.array([0, 0, 0])
res = minimize(func, x0)

print("y=%f when x=%s"%(func(res.x), res.x))



from scipy.optimize import curve_fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)

np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')
popt, pcov = curve_fit(func, xdata, ydata)
print(popt)
print(pcov)

plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.legend()
plt.show()


from scipy import optimize

def fun(x):
    return [x[0]**2 + x[1]**2 -x[2]/3 - 3,
            x[0]**2 +x[1]/5- x[2] +1,
            x[0]+x[1]+x[2]-7
    ]

sol = optimize.root(fun, [0, 0, 0])
print(sol.x)
print(fun(sol.x))
