#!/usr/bin/env python3

import numpy as np
from collections import Counter

def create_histogram(x, n):
    return np.histogram(x, bins=n, range=None,
                        normed=False, weights=None)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]                    

def bucketize(x, interval):
    b = []
    c = interval
    while c <= max(x):
        b.append([i for i in x if i <= c])
        x = Counter(x) - Counter(b[-1])
        if not x:
            break
        c+=interval
    return b


x =  [0.01, 1.0, 5.0, 10.0, 25.0, 50.0, 75.0, 100.0, 200.0, 300.0, 400.0]

print("histogram:\n", create_histogram(x, 5))
print("chunks with equal bin size:\n", list(chunks(x, 5)))
print("chunks with equal interval size:\n", bucketize(x, 15))


##############
# FYI
##################

# def ff():
#     for i in v.elements(): i*3

# In [86]: %timeit ff()
# 100000 loops, best of 3: 7.05 µs per loop
#############################################
# def gg():
#     for i in v.keys(): i*3            

# In [87]: %timeit gg()
# 100000 loops, best of 3: 2.54 µs per loop
#############################################

# def hh():
#     for i in v: i*3

# In [100]: %timeit hh()
# 100000 loops, best of 3: 2.42 µs per loop

#######
# also, just so you know:
# http://blog.labix.org/2008/06/27/watch-out-for-listdictkeys-in-python-3
