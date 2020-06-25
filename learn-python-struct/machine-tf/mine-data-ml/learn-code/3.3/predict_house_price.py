import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import traceback
from sklearn import datasets, linear_model
from sklearn.externals import joblib


# 读取数据函数
def get_data(file_name):
    data = pd.read_csv(file_name)  # 读取cvs文件
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        X_parameter.append([float(single_square_feet)])  # 这里面存的是一个一个的list
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# 将数据拟合到线性模型
def linear_model_main(X_parameter, Y_parameter, predict_value):
    try:
        # 1 创建线性回归对象
        regr = linear_model.LinearRegression()
        # 2 创建线性回归对象
        regr.fit(X_parameter, Y_parameter)
        joblib.dump(regr, "./lr.pkl")
        predict_outcome = regr.predict(predict_value)
        predictions = {}
        predictions['intercept'] = regr.intercept_
        predictions['coefficient'] = regr.coef_
        predictions['predicted_value'] = predict_outcome
        return predictions
    except Exception as e:
        traceback.print_exc()


X, Y = get_data('input_data.csv')
predictvalue = 700
print(np.array(predictvalue))
newPredictvalue = np.array(predictvalue).reshape(1, -1)
print(newPredictvalue)
# result = linear_model_main(X, Y, newPredictvalue)
lr = joblib.load("./lr.pkl")
result = lr.predict(newPredictvalue)
print(str(result))
# print("Intercept value", result['intercept'])
# print("coefficient ", result['coefficient'])
# print("Predicted value:", result['predicted_value'])


def show_linear_line(X_parameters, Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    # scatter可以用来查看展示样本数据在坐标系里
    plt.scatter(X_parameters, Y_parameters, color='blue')
    # 样本参数和预测的标签
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


show_linear_line(X, Y)


