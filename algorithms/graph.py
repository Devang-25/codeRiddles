#!/usr/bin/env python2
graph = {
    'A': ['B', 'C'],
    'B': ['E', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F','B'],
    'F': ['A']
    }

print "\n",graph,"\n"

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    if end in graph[start]:
        return path+[end]
    for node in graph[start]:
        #print path
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

final = []
start = raw_input("Enter starting node: \n").upper()
end = raw_input("Enter target node: \n").upper() 

try:
    for node in graph[start]:
        final.append(find_path(graph, node, end, [start]))
    print "shortetest path: ", min(final)
    print "longest path: ", max(final)
except:
    print None
