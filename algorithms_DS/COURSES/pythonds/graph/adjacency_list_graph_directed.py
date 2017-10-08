#!/bin/env python3


# TODO:
# remove edges/vertices etc..
# is connected (dfs/bfs)
# find path

# The graph abstract data type (ADT) is defined as follows:

# - Graph() creates a new, empty graph.
# - addVertex(vert) adds an instance of Vertex to the graph.
# - addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
# - addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
# - getVertex(vertKey) finds the vertex in the graph named vertKey.
# - getVertices() returns the list of all vertices in the graph.
# - in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.

import csv
import sys
from pprint import pprint
from prettytable import PrettyTable

PT = PrettyTable()
PT.field_names = ["Vertex ID", "Inward count", "Outward count"]


class Vertex(object):
    
    def __init__(self, key):
        self._id = key
        self.connectedTo = {}
        self.props = {}
        self.inward_count = 0


    def __get_iter_obj(self):
        return [
            self._id,
            self.inward_count,
            len(self.getConnections())
        ]

    def getId(self):
        return self._id

    def setProperties(self, **kwargs):
        self.props.update(kwargs)

    def getProperties(self):
        return self.props
        
    def __str__(self, degree=None):        
        # return [
        #     str(self._id),
        #     str([x._id for x in self.connectedTo]),
        #     str(self.props)
        # ]

        # with degree %s and inward count %s
        # str(len(self.getConnections())),
        #   self.inward_count,
        # import pdb; pdb.set_trace()
        return "%s is connectedTo: %s has properties: %s" % \
            (
                str(self._id),
                str([self.connectedTo[x]['v_obj']._id for x in self.connectedTo]),
                str(self.props)
            )

    def __repr__(self):

        # return str([
        #     self._id,
        #     self.inward_count,
        #     len(self.getConnections())
        # ])
        
        #()            
        # return "Vertex(_id=%s, inward_count=%s, outward_count=%s" % \
        #     (
        #         self._id,
        #         self.inward_count,
        #         len(self.getConnections())
        #     )

        _op = "Vertex(_id={}, inward_count={}, outward_count={})"
        return _op.format(*self.__get_iter_obj())

        # return ''.join([_op.format(*self.__get_iter_obj())])
    

        
    def __iter__(self):
        return iter(self.__get_iter_obj())

    def __len__(self):
        return len(self.__get_iter_obj())
    
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
    Directed Graph
    '''
    def __init__(self):
        self.vertList = {}
        # { v1_id : v1_object }
        # v1_object : { connectedTo: { v2:w2, v3:w3}}
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
        if bool(a) and bool(b):
            self.numEdges += 1
            if a not in self.vertList:
                nv = self.addVertex(a)
            if b not in self.vertList:
                nv = self.addVertex(b)
            self.vertList[a].addNeighbour(b, self.vertList[b], cost)
            self.vertList[b].inward_count += 1
            
    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self, k):
        return k in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

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
    
if __name__=='__main__':
    G = Graph()

    try:
        f = open(sys.argv[1], 'r')
        reader = csv.reader(f, delimiter=',')
        
        # header format:
        #     id,connectedTo,edgeWeights,name,age,....
        # .....(add anything in csv data from 4th field onwards)
        headers = next(reader)
        
    except IndexError:
        quit("Didn't supply a graph data csv as arg[1], did ya?")
    except:
        raise

    for row in reader:
        G.addVertex(row[0])
        connections, weights = row[1].split(','), row[2].split(',')
        for edge in zip(connections, weights):
            G.addEdge(row[0], *edge)
        prop = dict(zip(headers[3:], row[3:]))
        G.addPropertyToVertex(row[0], **prop)

    # # trigger __repr__ of Vertex class
    # pprint(G.vertList)    
    for v in G:
        PT.add_row(v)
        print(v)

    print(PT)
    
    print("Max Degree: ", G.maxDegree())
    print("Average Degree: ", G.averageDegree())
    print("Number of self loops: ", G.numberofSelfLoops())
    print("Is connected?: ",)



    # https://stackoverflow.com/questions/28623558/how-to-override-a-python-classs-str-method-on-construction-with-argument

    # so when we have:
    # def __str__(self, degree):
    #   return "blabla", degree

    # so we could do:
    # print(vertex, degree=2)

    # would this help?
    # def __call__(self, cls):
    #     prop = self.prop
    #     def __str__(s):
    #         return getattr(s, prop)
    #     cls.__str__ = __str__
    #     return cls
