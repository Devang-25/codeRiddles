#!/bin/env python3

from adjacency_list_graph_directed import *

G = Graph()        
try:
    f = open(sys.argv[1], 'r')
    reader = csv.reader(f, delimiter=',')
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

for v in G:
    print(v)
# pprint(G.vertList)

visited = dict.fromkeys(G.getVertices())

def pathTo(start, end, traversed=[]):
    print(traversed)
    traversed.append(start)
    if not bool(start):
        return False, traversed
        
    if end == start:
        return True, traversed

    if visited[start] != None:
        return False, traversed

    visited[start] = 1
    start = G.getVertex(start)
    for adj in start.connectedTo.keys():
        status, traversed = pathTo(adj, end, traversed=traversed)
        if status:
            return True, traversed
        else:
            if traversed:
                traversed.pop(-1)

    return False, traversed
            
if __name__ == '__main__':    
    start = input("Enter start node: ")
    end = input("Enter destination node: ")
    traversed = []

    print("Checking path start to end, using DFS..")
    values = pathTo(start, end, traversed=traversed)
    print("Path found: {} \nTraversed route: {}".format(*values))
