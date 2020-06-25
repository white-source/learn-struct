# -*- coding: utf-8 -*-

# 引入数据集

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier      #导入决策树DTC包
import matplotlib.pyplot as plt

iris = load_iris()
iris_feature = iris.data #特征数据
iris_target = iris.target #分类数据

print (iris.data)          #输出数据集
#print (iris.target)        #输出真实标签
#print (len(iris.target) )
#print (iris.data.shape )   #150个样本 每个样本4个特征


clf = DecisionTreeClassifier()      # 所以参数均置为默认状态
clf.fit(iris.data, iris.target)     # 使用训练集训练模型


# 获取花卉两列数据集
X = iris.data
L1 = [x[0] for x in X]
#print(L1)
L2 = [x[1] for x in X]
#print (L2)

	#绘图
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.scatter(X[100:, 0], X[100:, 1], color='green', marker='s', label='Virginica')
plt.title("DTC")
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xticks(())
plt.yticks(())
plt.legend(loc=2)
plt.show()

import pandas
#导入数据集iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names) #读取csv数据
print(dataset.describe())
#直方图 histograms
dataset.hist()
plt.show()


# viz code 可视化 制作一个简单易读的PDF
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     special_characters=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
print(len(graph))  # 1
print(graph)  # [<pydot.Dot object at 0x000001F7BD1A9630>]
print(graph[0])  # <pydot.Dot object at 0x000001F7BD1A9630>
# graph.write_pdf("iris.pdf")
graph[0].write_pdf("iris.pdf")