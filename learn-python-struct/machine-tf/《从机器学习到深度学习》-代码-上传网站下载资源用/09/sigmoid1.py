import matplotlib.pyplot as plt  
import numpy as np

from scipy.misc import derivative

sigmoid = lambda x: 1 / (1 + np.exp(-x))

def draw_sigmoid(w, b):
    x = np.linspace((-b)/w-10,(-b)/w+10,100)
    z = x*w + b
    plt.plot(x,sigmoid(z),'b')
    plt.grid()
    plt.title('w=%d, b=%d'%(w, b))
plt.suptitle('$Sigmoid(x| w, b)=\sigma(wx+b)$')

plt.subplot(131)
draw_sigmoid(5, 1)
# plt.text(4,0.8,r'$\sigma(x)=\frac{1}{1+e^{-x}}$',fontsize=15)

plt.subplot(132)
draw_sigmoid(5, 10)


plt.subplot(133)
draw_sigmoid(5, 100)

plt.legend(loc='lower right')

plt.show()
