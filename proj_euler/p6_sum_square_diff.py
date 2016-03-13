#!/usr/bin/env python3

from functools import reduce

def generate_squared_diff(n):
    _tmp = range(n+1)
    z = lambda x,y: x+y
    square_of_sum = sum(_tmp)**2
    sum_of_square = reduce(z, [i**2 for i in _tmp]) 
    return abs(square_of_sum - sum_of_square)

print(10, generate_squared_diff(10))
print(100, generate_squared_diff(100))
