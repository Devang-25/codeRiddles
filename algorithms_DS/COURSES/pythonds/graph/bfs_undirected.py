#!/bin/env python3

import sys
from pprint import pprint
from ladder_prob_undirected import *
from adj_list_undirected_graph import *

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

def traverse(s, t, parents):
    # reverse traverse from end to start
    # one of the shortest paths (in case 2 paths of same distance)
    chain = [t]
    try:
        while s != t:
            t = parents[t]
            chain.append(t)
    except KeyError:
        print("\ntraverse(start, end): Key Error!")
        quit("Invalid start/end nodes supplied")

    return ' => '.join(chain[::-1])

### numerical v/s alhpabetical graphs

def words_graph(word='fool'):
    wordList = read_data()
    # word = wordList[0]
    G = buildGraph(wordList)
    l, p = bfs(word, G)
    return word, l, p

def digits_graph():
    # f = open(sys.argv[1], 'r')
    f = open('data/undirected.txt', 'r')
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
    

def print_results(start, end, query, parents, level):
    print("\n\nResult: %s " % traverse(start, end, parents))
    print("Distance of '%s' from '%s' is %s" % (
        query,
        start,
        level[query]
    ))
    # pprint(level)
    # pprint(parents)
    

if __name__ == '__main__':

    try:
        if sys.argv[1] != '0':
            start = '0'
            end = '1'
            query = '4'
            start, level, parents = digits_graph()
        else:
            # Distance of 'sage' from 'fool' is 6
            # #sixdegreesofseparation :D
            # https://en.wikipedia.org/wiki/Six_degrees_of_separation
            start = 'fool'
            end = 'sage'
            query = end
            # query = 'male'
            start, level, parents = words_graph(word=start)

        print_results(start, end, query, parents, level)

    except IndexError:
        print("Usage: supply 0 for word based BFS; 1 for digits based")
        print("Example: ./bfs_undirected.py 1")

    except:
        raise
