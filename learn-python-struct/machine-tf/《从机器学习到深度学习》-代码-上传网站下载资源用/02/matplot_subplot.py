import numpy as np
import matplotlib.pyplot as plt

#建立子视图
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

x = np.linspace(0, 2, 100)

#绘制数据点线图
ax1.plot(x, x**0.5, label="y=power(x, 0.5)")
ax1.plot(x, x**2, label="y=power(x, 2)")
ax2.plot(x, 0.5**x, label="y=power(0.5, x)")
ax2.plot(x, 2**x, label="y=power(2, x)")
ax3.plot(x, np.log2(x), label="y=log2(x)")
ax3.plot(x, np.log10(x), label="y=log10(x)")

#不设置loc参数，自动选择图例位置
ax1.legend()     
ax2.legend()
ax3.legend()

plt.show()
