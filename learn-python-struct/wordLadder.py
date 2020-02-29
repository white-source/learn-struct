# 为词梯构建 单词关系图
#词梯问题是个什么样的问题？条件是什么，结果是什么，思路是什么
1
# 通过字典实现
# 1.1 字典的键 -》 桶上的标签 （_OPE,P_PE,_PO_E,POP_）
# 1.2 字典的值 -》 对应的单词列表{_OPE,[POPE,ROPE,NOPE,HOPE,LOPE,MOPE,COPE]}
# 2.1 为每个单词创建顶点
# 2.2 然后在字典对应的同一个键的单词之间创建边

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # 创建词桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 为同一个桶中的单词添加 顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId)
        x = x.getPred()
    print(x.getId)

traverse(g.getVertex('sage'))



