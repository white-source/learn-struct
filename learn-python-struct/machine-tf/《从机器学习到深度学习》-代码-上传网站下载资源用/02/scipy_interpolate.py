import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x, y, s=0)

xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0)

print(xnew)
print(ynew)









import scipy.constants as C

x = np.linspace(0, C.pi*2, num=10, endpoint=True)
y = np.sin(x)

interp_line = interpolate.interp1d(x, y)
interp_cubic = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(0, C.pi*2, num=33, endpoint=True)
ynew_line = interp_line(xnew)
ynew_cubic = interp_cubic(xnew)
plt.plot(x, y, 'o', xnew, ynew_line, '-', xnew, ynew_cubic, '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
