import matplotlib.pyplot as plt  
import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))

def draw_sigmoid(w, b, w2, b2, w11=1, w21=1):
    center = ((-b)/w+(-b2)/w2)/2
    x = np.linspace(center-10,center+10,100)
    z = x*w + b
    z2 = x*w2 + b2
    plt.plot(x,sigmoid(z)*w11+sigmoid(z2)*w21,'b')
    plt.grid()
    plt.title('a1(w=%d, b=%d)*w11(%0.1f)+ \na2(w=%d, b=%d)*w21(%0.1f)'%(w, b, w11, w2, b2, w21))


plt.subplot(131)
draw_sigmoid(5, 1, 5, 30, 0.3, 0.7)
# plt.text(4,0.8,r'$\sigma(x)=\frac{1}{1+e^{-x}}$',fontsize=15)

plt.subplot(132)
draw_sigmoid(500, -5000, -500, 1000)


plt.subplot(133)
draw_sigmoid(500, -1000, 500, -2000, 0.7, -0.7)

plt.legend(loc='lower right')

plt.show()
