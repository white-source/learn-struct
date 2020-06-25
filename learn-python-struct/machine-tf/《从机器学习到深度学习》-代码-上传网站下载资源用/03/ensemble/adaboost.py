#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
iris = load_iris()

from sklearn.utils import shuffle
X, Y = shuffle(iris.data, iris.target)
from sklearn.naive_bayes import GaussianNB

regressor = AdaBoostClassifier(GaussianNB())
regressor.fit(X[:-20], Y[:-20])

print(regressor.score(X[-20:], Y[-20:]))


