#!/usr/bin/python
# -*- coding: utf-8 -*-


from sklearn.datasets import load_iris
iris = load_iris()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.8,
    random_state=0
)


from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
clf = AdaBoostClassifier()
scores = cross_val_score(clf, iris.data, iris.target, cv=3)
print(scores)
print("total accuracy:", scores.mean())


from sklearn.model_selection import LeaveOneOut
X = [['a'], ['b'], ['c'], ['d']]
Y = ['A', 'B', 'C', 'D']
loo = LeaveOneOut()
for idx_train, idx_test in loo.split(X):
    print("%s %s" % (idx_train, idx_test))

cross_val_score(clf, [], [], scoring='wrong_choice')
