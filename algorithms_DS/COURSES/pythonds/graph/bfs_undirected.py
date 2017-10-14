#!/bin/env python3

import sys
from pprint import pprint
from ladder_prob import *
from adjacency_list_graph_undirected import *

def bfs(s, g):
    level = {s: 0}
    parent = {s: None}
    frontier = [s]
    i = 1
    while frontier:
        _next = []
        for u in frontier:
            for v in g.adjacent(u):
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    _next.append(v)
        print(i, _next)                    
        i+=1
        frontier = _next


    return level, parent

def traverse():
    pass

### numerical v/s alhpabetical graphs

def words_graph(word='fool'):
    wordList = read_data()
    # word = wordList[0]
    G = buildGraph(wordList)
    l, p = bfs(word, G)
    return word, l, p

def digits_graph():
    # f = open(sys.argv[1], 'r')
    f = open('data/tinyG.txt', 'r')
    In = f.read().splitlines()
    f.close()
    G = Graph()
    [G.addEdge(*i.split()) for i in In]

    nodes = sorted(list(G.graph.keys()))
    print(nodes)
    print(G)
    print()
    l, p = bfs(nodes[1], G)
    return nodes[1], l, p
    

if __name__ == '__main__':
    s, level, parents = words_graph()
    # s, level, parents = digits_graph()

    print("\n\nResult for %s:\n" % s)
    pprint(level)
    # pprint(parents)
