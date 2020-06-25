# -*- coding: utf-8 -*-
from numpy import *
import pandas as pd
from pandas import DataFrame
filename='./data.txt' #文件目录
#df = DataFrame(pd.read_csv('/Users/apple27/Documents/logi.csv'))
def loadDataSet():   #读取数据（这里只有两个特征）
    df=pd.read_csv(filename)
    print(df)
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  #前面的1，表示方程的常量。比如两个特征X1,X2，共需要三个参数，W1+W2*X1+W3*X2
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

loadDataSet()
def sigmoid(inX):  #sigmoid函数
    return 1.0/(1+exp(-inX))

def stocGradAscent1(dataMat, labelMat): #改进版随机梯度上升，在每次迭代中随机选择样本来更新权重，并且随迭代次数增加，权重变化越小。
    dataMatrix=mat(dataMat)
    classLabels=labelMat
    m,n=shape(dataMatrix)
    weights=ones((n,1))
    maxCycles=500
    for j in range(maxCycles): #迭代
        dataIndex=[i for i in range(m)]
        for i in range(m): #随机遍历每一行
            alpha=4/(1+j+i)+0.0001  #随迭代次数增加，权重变化越小。
            randIndex=int(random.uniform(0,len(dataIndex)))  #随机抽样
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-h
            weights=weights+alpha*error*dataMatrix[randIndex].transpose()
            del(dataIndex[randIndex]) #去除已经抽取的样本
    return weights

def plotBestFit(weights):  #画出最终分类的图
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
    plt.savefig('logExample.png', format='png')
def main():
    datamat,labelmat=loadDataSet()
    weights=stocGradAscent1(datamat, labelmat).getA()
    plotBestFit(weights)

if __name__=='__main__':
    main()


from numpy import *
import matplotlib.pyplot as plt


def sigmoid(X):
    return 1.0 / (1 + exp(-X))


class logRegressClassifier(object):

    def __init__(self):
        self.dataMat = list()
        self.labelMat = list()
        self.weights = list()

    def loadDataSet(self, filename):
        fr = open(filename)
        for line in fr.readlines():
            lineArr = line.strip().split()
            dataLine = [1.0]
            for i in lineArr:
                dataLine.append(float(i))
            label = dataLine.pop()  # pop the last column referring to  label
            self.dataMat.append(dataLine)
            self.labelMat.append(int(label))
        self.dataMat = mat(self.dataMat)
        self.labelMat = mat(self.labelMat).transpose()

    def train(self):
        self.weights = self.stocGradAscent1()

    def batchGradAscent(self):
        m, n = shape(self.dataMat)
        alpha = 0.001
        maxCycles = 500
        weights = ones((n, 1))
        for k in range(maxCycles):  # heavy on matrix operations
            h = sigmoid(self.dataMat * weights)  # matrix mult
            error = (self.labelMat - h)  # vector subtraction
            weights += alpha * self.dataMat.transpose() * error  # matrix mult
        return weights

    def stocGradAscent1(self):
        m, n = shape(self.dataMat)
        alpha = 0.01
        weights = ones((n, 1))  # initialize to all ones
        for i in range(m):
            h = sigmoid(sum(self.dataMat[i] * weights))
            error = self.labelMat[i] - h
            weights += (alpha * error * self.dataMat[i]).transpose()
        return weights

    def stocGradAscent2(self):
        numIter = 2
        m, n = shape(self.dataMat)
        weights = ones((n, 1))  # initialize to all ones
        for j in range(numIter):
            dataIndex = range(m)
            for i in range(m):
                alpha = 4 / (1.0 + j + i) + 0.0001  # apha decreases with iteration, does not
                randIndex = int(random.uniform(0, len(dataIndex)))  # go to 0 because of the constant
                h = sigmoid(sum(self.dataMat[randIndex] * weights))
                error = self.labelMat[randIndex] - h
                weights += (alpha * error * self.dataMat[randIndex]).transpose()
                del (dataIndex[randIndex])
        return weights

    def classify(self, X):
        prob = sigmoid(sum(X * self.weights))
        if prob > 0.5:
            return 1.0
        else:
            return 0.0

if __name__ == '__main__':
    lr = logRegressClassifier()