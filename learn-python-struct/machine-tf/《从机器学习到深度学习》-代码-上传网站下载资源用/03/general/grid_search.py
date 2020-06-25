#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

iris = datasets.load_iris()


tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]


clf = GridSearchCV(SVC(), tuned_parameters, cv=10,
                       scoring='accuracy')
clf.fit(iris.data, iris.target)
print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
durations = clf.cv_results_['mean_fit_time']
for mean, std, duration, params in zip(means, stds, durations, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r in %f seconds"
          % (mean, std * 2, params, duration))
print()

