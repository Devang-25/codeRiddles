#!/usr/bin/env python3

import operator

swapping_indices = [(1,4), (3,4)]

if __name__=="__main__":
    ip = input("Enter string: ")
    d = dict(enumerate(ip, 1))
    v = set(); [v.update(i) for i in swapping_indices]
    x = sorted(operator.itemgetter(*v)(d),
           reverse=True)
    for i,j in zip(v,x):
        d[i] = j
    
    print(''.join(d.values()))

