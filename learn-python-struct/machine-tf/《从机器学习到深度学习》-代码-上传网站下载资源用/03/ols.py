
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


reg = linear_model.LinearRegression()

        
x = np.linspace(0, 10, 30)
y = x*0.7-2 + np.random.normal(0, 1, len(x))

f_x = x.reshape(-1, 1)
reg.fit(f_x, y)
plt.plot(x, y, "k.")
plt.plot(x, reg.predict(f_x))

plt.show()


x = np.array([[0, 1], [3, -2], [2, 3]])
y = np.array([0.5, 0.3, 0.9])

reg = linear_model.LinearRegression()
reg.fit(x, y)

print("intercept_: ", reg.intercept_)
print("coef_: ", reg.coef_)

print(reg.predict([[1, 2], [-3, 2]]))
