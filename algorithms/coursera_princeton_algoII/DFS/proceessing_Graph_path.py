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
    

class Paths(object):
    def __init__(self, adj_mx, source):
        self.s = source
        self.G = adj_mx
        
    def hasPathTo(self, v):
        if self.pathTo(self.s, v):
            return True
        else:
            return False
        
    def pathTo(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.G.has_key(start):
            return None
        for node in self.G[start]:
            if node not in path:
                newpath = self.pathTo(node, end, path)
                if newpath: return newpath
        return None
    
if __name__=='__main__':
    f = open(sys.argv[1], 'rb')
    In = f.read().splitlines()
    f.close()
    G = Graph(In)
    s = sys.argv[2]
    print G.graph
    paths = Paths(G.graph, int(s))
    
    for v in xrange(0, G.V):
        if paths.hasPathTo(v):
            print v
