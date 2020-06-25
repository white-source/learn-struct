from sklearn import datasets
iris = datasets.load_iris()

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

gnb.fit(iris.data, iris.target)

print(gnb.class_prior_)

print(gnb.class_count_)

print(gnb.theta_)

print(gnb.sigma_)




from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB(binarize=1)
X = [[0.3, 0.2], [1.3, 1.2], [1.1, 1.2]]
Y = [0, 1, 1]

clf.fit(X, Y)
print(clf.predict([[0.99, 0.99]]))


