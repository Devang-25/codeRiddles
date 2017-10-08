#!/bin/env python3

import sys
from collections import defaultdict
from adjacency_list_graph_undirected import *


def buildGraph(wordList):
    g = Graph()
    buckets = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            buckets[bucket].append(word)

    for bucket in buckets.keys():
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
        
    return g


if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    wordList = f.read().splitlines()
    G = buildGraph(wordList)
    print(G)
    