from sklearn import linear_model
import numpy as np

"""
第一个模型（最小二乘法训练 ）
"""
x = np.array([[0, 1], [3, -2], [2, 3]])  # 训练样本特征
y = np.array([0.5, 0.3, 0.9])  # 训练样本目标值

reg = linear_model.LinearRegression() #最小二乘法回归对象
reg.fit(x, y) #训练拟合

print("intercept_:",reg.intercept_) #读取截距
print("coef_:",reg.coef_)#读取回归参数

predict_result = reg.predict([[1,2],[-3,2]])
print(predict_result) #预测

"""
第二个模型 
"""


