# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV    # 0.17 grid_search
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
if __name__ == "__main__":
    N = 50
    np.random.seed(0)
    x = np.sort(np.random.uniform(0, 6, N), axis=0)
    print('训练数据集(x,y)：')
    print ('x =\n', x)
    y = 2*np.sin(x) + 0.1*np.random.randn(N)
    x = x.reshape(-1, 1)
    print ('y =\n', y)
    model = svm.SVR(kernel='rbf')
    c_can = np.linspace(105,107,10)
    print('c_can=',c_can)
    gamma_can = np.linspace(0.4, 0.5, 10)
    print('gamma_can=',gamma_can)
    svr_rbf = GridSearchCV(model, param_grid={'C': c_can, 'gamma': gamma_can}, cv=5)
    svr_rbf.fit(x, y)
    print ('最优参数：\n', svr_rbf.best_params_)
    print('测试数据集(x_test,y_test)：')
    x_test = np.linspace(x.min(), 1.5*x.max(), 50)
    print('x_test=\n',x_test)
    np.random.seed(0)
    y_test = 2*np.sin(x_test) + 0.1*np.random.randn(N)
    print('y_test=\n',y_test)
    x_test=x_test.reshape(-1,1)
    y_rbf = svr_rbf.predict(x_test)
    print('高斯核的预测值:')
    print('y_rbf=\n',y_rbf)
    sp = svr_rbf.best_estimator_.support_
    plt.figure(figsize=(9, 8),facecolor='w')
    plt.scatter(x[sp], y[sp], s=200, c='r', marker='*', label='Support Vectors')
    plt.plot(x_test, y_rbf, 'r-', linewidth=2, label='RBF Kernel')
    plt.plot(x, y, 'ks', markersize=5, label='train data')
    plt.plot(x_test, y_test, 'mo', markersize=5, label='test data')
    plt.legend(loc='lower left')
    plt.title('SVR', fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    print("选取最优参数的高斯核函数支持向量机的平均绝对误差为:", mean_absolute_error(y_test,y_rbf))
    print("选取最优参数的高斯核函数支持向量机的均方误差为:", mean_squared_error(y_test,y_rbf))