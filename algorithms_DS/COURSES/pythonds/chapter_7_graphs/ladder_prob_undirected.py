#!/bin/env python3

import sys
from collections import defaultdict
from adj_list_undirected_graph import *


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

    #print(buckets.keys())
    return g

def read_data():
    # f = open(sys.argv[1], 'r')
    f = open('data/wordlists_small.txt', 'r')
    wordList = f.read().splitlines()
    return wordList
         

if __name__ == '__main__':
    wordList = read_data()
    G = buildGraph(wordList)
    print(G)
