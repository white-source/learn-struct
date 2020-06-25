import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#  1 获取数据
data = pd.read_csv('../../code/第3章 回归分析/3.4/Advertising.csv', index_col=0)
# 显示前五项
# data.head()
# print(data.head(),data.shape)
# x_vars 这三个是特征，
# sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', height=7, aspect=0.8, kind='reg')
# plt.show()

# 2 创建特征列表
feature_cols = ['TV', 'radio', 'newspaper']
# 3 使用列表选择原始Frame的子集
X = data[feature_cols]
y = data['sales']
# 4 构造 训练集 和 测试 集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# 75% train 25% test
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)
print(y.head())

linreg = LinearRegression()

model = linreg.fit(X_train, y_train)
print(model)
print(linreg.intercept_)
print(linreg.coef_)

resultFeatureCoef = zip(feature_cols, linreg.coef_)
print(list(resultFeatureCoef))

# 5 预测
y_pred = linreg.predict(X_test)
print(y_pred)
print(type(y_pred))

'''
6 评价测度   分类问题-》准确率  /回归问题 
 针对连续数值的   1 平均绝对误差 MAE 2 均方误差  MSE  3 均方根误差 RMSE
'''
# 计算Sales的预测 RMSE
print(type(y_pred), type(y_test))
print(len(y_pred), len(y_test))
print(y_pred.shape, y_test.shape)

from sklearn import metrics
import numpy as np

sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += (y_pred[i] - y_test.values[i]) ** 2
sum_error = np.sqrt(sum_mean / 50)
# 计算RMSE的大小
print("RMSE by hand:", sum_error)

# 7 绘制ROC曲线
import matplotlib.pyplot as plt
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label='predict')
plt.plot(range(len(y_pred)),y_test,'r',label='test')
plt.legend(loc='uppper right')
#显示途中的标签
#横坐标
plt.xlabel("the number of sales")
#纵坐标
plt.ylabel("the values of sales")
plt.show()