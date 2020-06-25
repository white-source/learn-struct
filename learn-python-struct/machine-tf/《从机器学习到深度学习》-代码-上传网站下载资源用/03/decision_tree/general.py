#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier(criterion="entropy")

X = [[20, 30000, 400],
     [37, 13000, 0],
     [50, 26000, 0],
     [28, 10000, 3000],
     [31, 19000, 1500000],
     [46, 7000, 6000]]

Y = [1, 0, 0, 0, 1, 0]

clf = clf.fit(X, Y)

test_X = [[40, 6000, 0]]
#print(clf.predict(test_X))
print(clf.decision_path(X))
print(clf.feature_importances_)
#print(clf.tree_)


import graphviz
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=[u"年龄", u"收入", u"存款"],  
                                class_names=[u"普通", u"VIP"],
                                filled=True, rotate=True)
#dot_data = tree.export_graphviz(clf, out_file=None, 
#                         feature_names=iris.feature_names,  
#                         class_names=iris.target_names)


graph = graphviz.Source(dot_data)
graph.render("mytree")

print(clf)
