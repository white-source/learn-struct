import matplotlib.pyplot as plt  
import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))

def draw_sigmoid(s, s2, w11=1,  start=0, end=1):
    w = 500000
    w2 = w
    b = -s*w
    b2 = -s2*w2
    w21 = -w11
    center = ((-b)/w+(-b2)/w2)/2
    x = np.linspace(start,end,100)
    z = x*w + b
    z2 = x*w2 + b2
    plt.plot(x,sigmoid(z)*w11+sigmoid(z2)*w21,'b')
    plt.grid()
    # plt.title('a1(w=%d, b=%d)*w11(%0.1f)+ \na2(w=%d, b=%d)*w21(%0.1f)'%(w, b, w11, w2, b2, w21))

target = lambda x: 0.3*x**3+0.3*np.sin(13*x)+0.05*(np.cos(30*x))

x = np.linspace(0, 1, 100)
plt.plot(x, target(x), 'k')
plt.grid()
plt.show()

def average(target, start, end):
    x = np.linspace(start, end, 100)
    return np.sum(target(x))/100
    
def draw_sigmoids(count):
    unit = 1/count
    deviation_number =0
    deviation_amount = 0
    for i in range(count):          
        start = i*unit
        end = (i+1)* unit
        avg = average(target, start, end)
        draw_sigmoid(start, end, avg, i==0 and -0.001 or start*(1-min(0.01,(end-start)*0.1)), end*(1+min(0.01, (end-start)*0.1)))

        x = np.linspace(start, end, 100)
        deviation_amount += np.sum(np.abs(avg-target(x)))
        deviation_number += x.shape[0]

    plt.title("pairs=%d, deviation=%0.3f"%(count, deviation_amount/deviation_number))

    
plt.subplot(131)
draw_sigmoids(5)
plt.plot(x, target(x), 'k')

plt.subplot(132)
draw_sigmoids(20)
plt.plot(x, target(x), 'k')


plt.subplot(133)

draw_sigmoids(100)
plt.plot(x, target(x), 'k')

plt.legend(loc='lower right')
# plt.text(4,0.8,r'$\sigma(x)=\frac{1}{1+e^{-x}}$',fontsize=15)
plt.show()
