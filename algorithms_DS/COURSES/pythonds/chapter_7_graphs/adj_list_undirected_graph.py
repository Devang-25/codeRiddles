#!/bin/env python3

import sys
from collections import defaultdict


class Vertex(object):
    def __init__(self, key):
        self._id = key
        self.connectedTo = {}
        self.props = {}
        self.color = 'white'

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color
    
    def getId(self):
        return self._id

    def setProperties(self, **kwargs):
        self.props.update(kwargs)

    def getProperties(self):
        return self.props
        
    def __repr__(self):
        return "Vertex %s" % self._id
    
    def __str__(self, degree=None):        
        return "%s with degree %s is connectedTo: %s has properties: %s" % \
            (
                str(self._id),
                len(self.connectedTo),
                str([self.connectedTo[x]['v_obj']._id for x in self.connectedTo]),
                str(self.props)
            )        

    def __len__(self):
        return len(self.getConnections())

    def addNeighbour(self, k, nbr, weight=0):
        self.connectedTo[k] = {
            'v_obj': nbr,
            'weight': weight
        }
    
    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, v):
        return self.connectedTo[v]



class Graph(object):
    '''
    Type 1 implementation of Undirected Graph:
    2 classes to maintain vertex and graph objects
    '''
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self, k):
        if k in self.vertList:
            return self.getVertex(k)
        
        self.numVertices += 1
        newVertex = Vertex(k)
        self.vertList[k] = newVertex
        return newVertex

    def addPropertyToVertex(self, k, **kwargs):
        if k not in self.vertList:
            nv = self.addVertex(k)
        else:
            nv = self.getVertex(k)
        nv.setProperties(**kwargs)
        # test if this works:
        # self.vertList[k] = nv   
        
    def getVertex(self, k):
        return self.vertList[k]

    def addEdge(self, a, b, cost=0):
        # returns 1 if edge already exists 
        # import pdb; pdb.set_trace()
        if a not in self:
            nv = self.addVertex(a)
            self.numVertices += 1
        if b not in self:
            nv = self.addVertex(b)
            self.numVertices += 1

        if a not in self.vertList[b].getConnections():
            self.vertList[a].addNeighbour(b, self.vertList[b], cost)
            self.vertList[b].addNeighbour(a, self.vertList[a], cost)
            self.numEdges += 2

        
    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self, k):
        return k in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def __repr__(self):
        _op = "Graph(Vertices=%s, Edges=%s)" % (self.numVertices, self.numEdges)
        for v in self.getVertices():
            current_vertex = self.getVertex(v)
            _op += "\n %s" % (current_vertex)
        return _op
    
    def degree(self, k):
        return len(self.vertList[k].getConnections())

    def maxDegree(self):
        _max = 0
        for v in self.vertList.keys():
            if self.degree(v) > _max:
                _max = self.degree(v)
        return _max
    
    def averageDegree(self):
        return (2.0 * self.numEdges / self.numVertices)

    def numberofSelfLoops(self):
        count = 0
        for v in self.vertList:
            for w in self.vertList[v].getConnections():
                if v == w:
                    count+=1
        return count

    def isConnected(self):
        return
    
    def is_rRegular(self):
        # https://en.wikipedia.org/wiki/Regular_graph
        return
    

# class Graph(object):
#     '''
#     Type 2 implementation of Undirected non-weighted Graph: 
#     single class using list of vertices for edges
#     '''
    
#     def __init__(self):
#         # super(Vertex, self).__init__()
#         self.graph = defaultdict(list)
#         self.E = 0
#         self.V = 0
#         self.color = None
#         # self.edges = []
        
#     def __repr__(self):
#         _op = "Graph(Vertices=%s, Edges=%s)" % (self.V, self.E)
#         if self.V:
#             for v in self.graph:
#                 _op += "\n %s => %s" % (v, self.graph[v])
#         # if self.E:
#         #     for i,j in self.edges:
#         #        _op += "\n(%s -- %s)" % (i,j)
#         return _op

#     def addVertex(self, v):
#         if v not in self.graph:
#             self.V += 1
#             self.graph[v]
#             return 0
#         return -1

#     def removeVertex(self, v):
#         if v not in self.graph:
#             return "Not found in Graph!"
#         self.V -= 1
#         self.graph.pop(v)
#         for k in self.graph:
#             if v in self.graph[k]:
#                 self.graph[k].remove(v)
#                 self.E -= 1
#         return 0
    
#     def addEdge(self, v, w):
#         if w not in self.graph:
#             self.graph[w]
#             self.V+=1            
#         if v not in self.graph:
#             self.graph[v]
#             self.V+=1
#         if v not in self.graph[w]:
#             self.graph[v].append(w)
#             self.graph[w].append(v)        
#             self.E += 2
#             # self.edges.append((v,w))
#         return 0
    
#     def removeEdge(self, v, w):
#         if v not in self.graph or w not in self.graph:
#             return "One of the vertices not found in Graph!"
#         if v not in self.graph[w]:
#             return "Edge doesn't exist!"
#         self.graph[v].remove(w)
#         self.graph[w].remove(v)        
#         self.E -= 1
#         return 0
#         # if (v,w) in self.edges:
#         #     self.edges.remove((v,w))
#         # if (w,v) in self.edges:
#         #     self.edges.remove((w,v))
            
#     def adjacent(self, v):
#         return self.graph[v]
    
#     def degree(self, v):
#         return len(self.graph[v])
    
#     def maxDegree(self):
#         _max = 0
#         for v in self.graph:
#             if self.degree(v) > _max:
#                 _max = self.degree(v)
#         return _max
    
#     def averageDegree(self):
#         return (2.0 * self.E / self.V)

#     def numberofSelfLoops(self):
#         count = 0
#         for v in self.graph:
#             for w in self.adjacent(v):
#                 if v == w:
#                     count+=1
#         return count/2

    
if __name__=='__main__':
    f = open(sys.argv[1], 'r')
    In = f.read().splitlines()
    f.close()
    G = Graph()
    [G.addEdge(*i.split()) for i in In]

    for v in G: print(v)        
    
    print("Max Degree: ", G.maxDegree())
    print("Average Degree: ", G.averageDegree())
    print("Number of self loops: ", G.numberofSelfLoops())
