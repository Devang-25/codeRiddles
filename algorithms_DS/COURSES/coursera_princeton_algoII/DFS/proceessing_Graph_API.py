import sys
from collections import defaultdict

class Graph(object):
    def __init__(self, _graph):
        self.graph = defaultdict(list)
        self.V = int(_graph.pop(0))
        self.E = int(_graph.pop(0))
        [self.addEdge(*i.split()) for i in _graph]
        assert len(self.graph.keys()) == self.V
        assert len(_graph) == self.E
        
    def addEdge(self, v, w):
        v = int(v); w = int(w)
        self.graph[v].append(w)
        self.graph[w].append(v)

    def adj(self, v):
        return self.graph[v]

    def degree(self, v):
        return len(self.graph[v])

    def maxDegree(self):
        _max = 0
        for v in xrange(0, self.V):
            if self.degree(v) > _max:
                _max = self.degree(v)
        return _max
    
    def averageDegree(self):
        return (2.0 * self.E / self.V)

    def numberofSelfLoops(self):
        count = 0
        for v in xrange(0, self.V):
            for w in self.adj(v):
                if v == w:
                    count+=1
        return count/2

    
if __name__=='__main__':
    f = open(sys.argv[1], 'rb')
    In = f.read().splitlines()
    f.close()
    G = Graph(In)

    for v in xrange(0, G.V):
        print "Degree of %s is %s" % (v, G.degree(v))
    
    print "Max Degree: ", G.maxDegree()
    print "Average Degree: ", G.averageDegree()
    print "Number of self loops: ", G.numberofSelfLoops()
