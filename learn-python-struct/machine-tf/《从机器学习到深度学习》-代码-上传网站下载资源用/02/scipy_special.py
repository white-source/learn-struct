
import numpy as np
import scipy.special as spl
import matplotlib.pyplot as plt

x = np.linspace(0,20,500)
for i in range(3):
    y = spl.jv(i, x)
    plt.plot(x, y, '-', label="J%d"%i)
plt.legend(loc="upper right")
plt.show()
