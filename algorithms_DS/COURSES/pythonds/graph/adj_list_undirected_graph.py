#!/bin/env python3

import sys
from collections import defaultdict
    
class Graph(object):
    '''
    Undirected non-weighted Graph
    '''
    
    def __init__(self):
        # super(Vertex, self).__init__()
        self.graph = defaultdict(list)
        self.E = 0
        self.V = 0
        # self.edges = []
        
    def __repr__(self):
        _op = "Graph(Vertices=%s, Edges=%s)" % (self.V, self.E)
        if self.V:
            for v in self.graph:
                _op += "\n %s => %s" % (v, self.graph[v])
        # if self.E:
        #     for i,j in self.edges:
        #        _op += "\n(%s -- %s)" % (i,j)
        return _op

    def addVertex(self, v):
        if v not in self.graph:
            self.V += 1
            self.graph[v]
            return 0
        return -1

    def removeVertex(self, v):
        if v not in self.graph:
            return "Not found in Graph!"
        self.V -= 1
        self.graph.pop(v)
        for k in self.graph:
            if v in self.graph[k]:
                self.graph[k].remove(v)
                self.E -= 1
        return 0
    
    def addEdge(self, v, w):
        if w not in self.graph:
            self.graph[w]
            self.V+=1            
        if v not in self.graph:
            self.graph[v]
            self.V+=1
        if v not in self.graph[w]:
            self.graph[v].append(w)
            self.graph[w].append(v)        
            self.E += 1
            # self.edges.append((v,w))
        return 0
    
    def removeEdge(self, v, w):
        if v not in self.graph or w not in self.graph:
            return "One of the vertices not found in Graph!"
        if v not in self.graph[w]:
            return "Edge doesn't exist!"
        self.graph[v].remove(w)
        self.graph[w].remove(v)        
        self.E -= 1
        return 0
        # if (v,w) in self.edges:
        #     self.edges.remove((v,w))
        # if (w,v) in self.edges:
        #     self.edges.remove((w,v))
            
    def adjacent(self, v):
        return self.graph[v]
    
    def degree(self, v):
        return len(self.graph[v])
    
    def maxDegree(self):
        _max = 0
        for v in self.graph:
            if self.degree(v) > _max:
                _max = self.degree(v)
        return _max
    
    def averageDegree(self):
        return (2.0 * self.E / self.V)

    def numberofSelfLoops(self):
        count = 0
        for v in self.graph:
            for w in self.adjacent(v):
                if v == w:
                    count+=1
        return count/2

    
if __name__=='__main__':
    f = open(sys.argv[1], 'rb')
    In = f.read().splitlines()
    f.close()
    G = Graph()
    # G.V = int(In.pop(0))
    # G.E = int(In.pop(0))
    [G.addEdge(*i.split()) for i in In]
    # assert len(G.graph.keys()) == G.V
    # assert len(In) == G.E

    print(G)
    for v in G.graph:
        #     for w in G.adjacent(v):
        #         print "%s->%s" % (v, w)        
        print("Degree of %s is %s -- %s" % (v, G.degree(v), G.graph[v]))
    
    print("Max Degree: ", G.maxDegree())
    print("Average Degree: ", G.averageDegree())
    print("Number of self loops: ", G.numberofSelfLoops())
