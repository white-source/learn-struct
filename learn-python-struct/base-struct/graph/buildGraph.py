
# 顶点里放：与它直接相连的各个领接顶点
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight =0 ):
        self.connectedTo[nbr] = weight
        print(self)

    def getConnections(self):
        return  self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

# 图里的字典，只放各个顶点-》顶点先关的信息
class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):

        self.numVertices = self.numVertices + 1
        #新建一个顶点
        newVertex = Vertex(key)
        #{顶点id->{顶点id,{邻居顶点：权重，邻居顶点2：权重}}
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in  self.vertList:
            return  self.vertList[n]
        else:
            return None

    def getVertices(self):
        return  self.vertList.keys()

    def __contains__(self, item):
        return  item in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def addEdge(self,f,t,cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)


# test

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    #print(g.vertList)

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,2,1)
    g.addEdge(5,4,8)

    for v in g:
        for w in v.getConnections():
            print("(%s,%s)" % (v.getId(),w.getId()))














