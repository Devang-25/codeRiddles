#!/usr/bin/env python3

# Usage:
# $ ./lexicographically_largest.py
#   Enter string: abdc
#   Example of swappable indices input (2 pairs): 1,4-3,4
#   Enter swappable indices in pairs: 1,4-3,4
#   Answer: dbca

import operator

if __name__=="__main__":
    ip = input("Enter string: ")

    print("Example of swappable indices input (2 pairs): 1,4-3,4")
    swp_ip = input("Enter swappable indices in pairs: ")
    swapping_indices = [[int(j) for j in i.split(',')]
                        for i in swp_ip.split('-')]
    
    d = dict(enumerate(ip, 1))

    # B contains all loops of connected vertices, if
    # say each position in string is a vertex. Connected
    # vertices are swappable. (Permutations)
    B = []
    while swapping_indices:
        b = swapping_indices[0]; v = set(b); x = [b]
        for i in swapping_indices[1:]:
            if set(b) & set(i):
                v.update(b+i)
                x.append(i)
        [swapping_indices.remove(j) for j in x]
        B.append(v)

    # for each group of connected loops, swap and
    # reverse sort letters, to get largest one on leftmost
    # position in string. Update new positions at the end.
    for v in B:
        x = sorted(operator.itemgetter(*v)(d),
                   reverse=True)
        for i,j in zip(v,x):
            d[i] = j
    
    print("Answer: %s" % ''.join(d.values()))
