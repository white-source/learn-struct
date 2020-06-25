from sklearn import svm
X = [[0, 0], [2, 2]]
y = [1, 2]
clf = svm.SVC(kernel="rbf")
clf.fit(X, y)

t = [[2, 1], [0, 1]]
print(clf.predict(t))

print(clf.decision_function(t))

