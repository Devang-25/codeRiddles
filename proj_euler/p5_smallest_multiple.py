#!/usr/bin/env python3

from collections import defaultdict, Counter
from functools import reduce

def prime_factors(n):
    "Returns all factors of a positive integer"
    factors = []
    d = 2
    while (n > 1):
        while (n%d==0):
            n/=d
            factors.append(d)
        d = d + 1
    return factors

def generate_smallest_multiple(m, n):
    _tmp = defaultdict(int)
    for i in range(m,n+1):
        factored_dict = Counter(prime_factors(i))
        for factor in factored_dict:
            if _tmp[factor] < factored_dict[factor]:
                _tmp[factor] = factored_dict[factor]
                
    z = lambda x,y: x**y
    smallest_multiple = [z(i,j) for i,j in _tmp.items()]
    smallest_multiple = reduce(lambda x,y: x*y,
                               smallest_multiple)
    return smallest_multiple

print(10, generate_smallest_multiple(1,10))
print(20, generate_smallest_multiple(1,20))
