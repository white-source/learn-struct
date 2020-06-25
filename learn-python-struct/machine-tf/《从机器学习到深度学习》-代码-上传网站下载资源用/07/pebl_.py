from pebl import data
from pebl.learner import greedy
print "ksd"
dataset = data.fromfile("pebl-tutorial-data1.txt")
dataset.discretize()
print "88"
learner = greedy.GreedyLearner(dataset)
print "88", dataset
ex1result = learner.run()
print "88"
ex1result.tohtml("example1-result")
