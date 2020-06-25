
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def make_data(nDim):
    x0 = np.linspace(1, np.pi, 50)

    y = np.sin(x0) + np.random.normal(0,0.15,len(x0))

    # x = np.vstack([[x0,], [x0 + np.random.normal(0,0.0015,len(x0)) for i in range(1, nDim)]])
    x = np.vstack([[x0,], [i**x0 for i in range(2, nDim+1)]])
    return x.transpose(), y


x, y = make_data(12)
def linear_regression():
    dims = [1,  3, 6, 12]
    
    for idx, i in enumerate(dims):
        plt.subplot(2, len(dims)/2, idx+1)
        reg = linear_model.LinearRegression()

        sub_x = x[:, 0: i]
        reg.fit (sub_x, y)
        plt.plot(x[:,0], reg.predict(sub_x))
        plt.plot(x[:,0], y, ".")
        plt.title("dim=%s"%i)

        print("dim %d :"%i)
        print("intercept_: %s"% (reg.intercept_,))
        print("coef_: %s"% (reg.coef_,))
    plt.show()

linear_regression()
    
    
def ridge_regression():
    alphas = [1e-15, 1e-12,1e-5 ,1,]
    
    for idx, i in enumerate(alphas):
        plt.subplot(2, len(alphas)/2, idx+1)
        reg = linear_model.Ridge(alpha=i)

        sub_x = x[:, 0: 12]
        reg.fit (sub_x, y)
        plt.plot(x[:,0], reg.predict(sub_x))
        plt.plot(x[:,0], y, ".")
        plt.title("dim=12, alpha=%e"%i)

        print("alpha %e :"%i)
        print("intercept_: %s"% (reg.intercept_,))
        print("coef_: %s"% (reg.coef_,))
    plt.show()

ridge_regression()


def lasso_regression():
    alphas = [1e-10, 1e-3, 1e-1 ,1]
    
    for idx, i in enumerate(alphas):
        plt.subplot(2, len(alphas)/2, idx+1)
        reg = linear_model.Lasso(alpha=i)
        sub_x = x[:, 0: 12]
        reg.fit (sub_x, y)
        plt.plot(x[:,0], reg.predict(sub_x))
        plt.plot(x[:,0], y, ".")
        plt.title("dim=12, alpha=%e"%i)

        print("alpha %e :"%i)
        print("intercept_: %s"% (reg.intercept_,))
        print("coef_: %s"% (reg.coef_,))
    plt.show()

lasso_regression()
