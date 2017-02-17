#!/bin/env python3

# find all pairs (m,n) whose sum equals X, from a list of numbers (with duplicates)
# https://groups.google.com/forum/#!forum/dsa_sg

# In [62]: %timeit find_pairs([3,1,5,5,2,8,6,14],10)
# 100000 loops, best of 3: 8.07 µs per loop

# O(n) with added space complexity due to hash maps usage

from collections import Counter

def find_pairs(A, x):
    pairs = []
    A = [j for j in A if j<=x]
    V = Counter(A)
    # V = {k:v for k,v in Counter(A).items() if k<=x}
    # visited = []
    # import pdb; pdb.set_trace()
    for i in A:
        if V[i]==0:
            continue
        c = x-i
        if c in V:
            # visited.append(i)
            if c == i:
                if V[c] > 1:
                    pairs.append([c,i])
                    V[c] -= 2
            elif V[c] >= 1 and V[i] >= 1:
                pairs.append([c,i])
                V[c] -= 1
                V[i] -= 1
    return pairs
    # F = set(V.keys())-set(visited)
    # for i in F:
    #     V[i] = 0
    # Z = {k:v for k,v in V.items() if v==1}
    # if Z:
    #     find_pairs(Z,x)
    # else:
    #     return

assert find_pairs([3,1,5,5,2,8,6,14],10) == [[5, 5],[8,2]]
assert find_pairs([1,1,1,1,1],2) == [[1, 1], [1, 1]]
