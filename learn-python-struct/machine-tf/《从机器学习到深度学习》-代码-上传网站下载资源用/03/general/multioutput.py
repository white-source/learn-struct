#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

X = [[0, 1, 3], [9, 2, 5], [5, 1, 9], [6, 6, 1]]
Y = [[0, 0], [1, 0], [1, 0], [1, 1]]

clf =  MultiOutputClassifier(RandomForestClassifier())
clf.fit(X, Y)

print(clf.predict([[6, 1, 3]]))

