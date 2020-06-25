import numpy as np
from scipy.stats import gamma

a= 2
print(gamma.rvs(a, size=5))

print(gamma.pdf(np.linspace(0, 9, 10), a=a))

print(gamma.stats(a, moments='mvsk'))



import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)


ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

ax1.plot(x, gamma.pdf(x, a=2))
ax2.plot(x, gamma.cdf(x, a=2))

ax1.set_title('PDF')
ax2.set_title('CDF')

plt.show()


from scipy.stats import gaussian_kde

x = np.array([0, 1, 1.5 , 2, 4, 6.5, 7, 7, 7.9, 8, 9, 10])

kde = gaussian_kde(x)
print(kde)
plt.plot(x, np.zeros(x.shape), 'b+', ms=20)

x_eval = np.linspace(0, 10, num=200)
plt.plot(x_eval, kde(x_eval), '-')

plt.show()

print(kde(x_eval))
