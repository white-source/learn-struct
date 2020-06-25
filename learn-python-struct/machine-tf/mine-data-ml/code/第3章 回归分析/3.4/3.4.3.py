# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# read csv file directly from a URL and save the results
data = pd.read_csv('./Advertising.csv', index_col=0)

#创建特征列表
feature_cols = ['TV', 'radio', 'newspaper']

# use the list to select a subset of the original DataFrame
X = data[feature_cols]

#使用列表选择原始DataFrame的子集
X = data[['TV', 'radio', 'newspaper']]

# 输出前五项数据
print(X.head())
print(type(X))
print(X.shape)

#从DataFrame中选择一个Series
y = data['sales']
y = data.sales

# 输出前五项数据
print(y.head())

print(type(y))
print(y.shape)

#构建训练集和测试集，分别保存在X_train，y_train，Xtest，y_test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

linreg = LinearRegression()
linreg.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print (linreg.intercept_)
print (linreg.coef_)

# 将特征名称与系数对应
zip(feature_cols, linreg.coef_)

y_pred = linreg.predict(X_test)

print (np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()



















