#!/usr/bin/env python3

import operator

swapping_indices = [(1,4), (3,4)]

if __name__=="__main__":
    ip = input("Enter string: ")
    d = dict(enumerate(ip, 1))

    B = []
    while swapping_indices:
        b = swapping_indices[0]; v = set(b); x = [b]
        for i in swapping_indices[1:]:
            if set(b) & set(i):
                v.update(b+i)
                x.append(i)
        [swapping_indices.remove(j) for j in x]
        B.append(v)

    for v in B:
        x = sorted(operator.itemgetter(*v)(d),
                   reverse=True)
        for i,j in zip(v,x):
            d[i] = j
    
    print(''.join(d.values()))

