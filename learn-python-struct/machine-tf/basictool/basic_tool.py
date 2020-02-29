import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-5, 5, 20)
# y = x ** 2 + 1
# plt.xticks([-4, -3, -1])
# plt.yticks([2, 5, 10, 20], ["two", "five", "ten", "twenty"])
# plt.plot(x, y, "r--x", label="base")
# plt.plot(x + 2, y, "g-o", label="moved")
# plt.annotate('sample point', xy=(x[1], y[1]), xytext=(0, 24), arrowprops=dict(facecolor='black', shrink=0.05))
# plt.legend(loc='lower right')
# plt.title("Easy Matplot", fontdict={"fontsize": 20, }, loc="center")
# plt.xlabel("X values", fontdict={"fontsize": 12, })
# plt.ylabel("Y values", fontdict={"fontsize": 12, })
# plt.show()

"""
1 子视图 用来比较不同算法 或数据集 -》一次绘制多个子视图作为对比
"""

"""

ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)
x = np.linspace(0, 2, 100)
ax1.plot(x, x ** 0.5, label="y=power(x,0.5)")
ax1.plot(x, x ** 2, label="y=power(x,2)")
ax2.plot(x, 0.5 ** x, label="y=power(0.5,x)")
ax2.plot(x, 2 ** x, label="y=pwd(2,x)")
ax3.plot(x, np.log2(x), label="y=log2(x)")
ax3.plot(x, np.log10(x), label="y=log10(x)")

ax1.legend()
ax2.legend()
ax3.legend()

plt.show()
"""

"""
图像image绘制
"""
import scipy.constants as C
print(C.pi)




