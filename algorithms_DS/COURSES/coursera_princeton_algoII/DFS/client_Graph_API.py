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
    
    
if __name__=='__main__':
    f = open(sys.argv[1], 'rb')
    In = f.read().splitlines()
    f.close()
    #import pdb; pdb.set_trace()
    G = Graph(In)
    for v in xrange(0, G.V):
        for w in G.adj(v):
            print "%s->%s" % (v, w)
