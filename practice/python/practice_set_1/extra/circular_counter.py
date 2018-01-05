#!/bin/env python3

# https://github.com/keon/algorithms/blob/master/array/circular_counter.py

a = ['1','2','3','4','5','6','7','8','9']
ix = 0
skip = ix + 2
len_a = len(a)

while len_a>0:
    ix = (skip+ix)%len_a
    print(a.pop(ix))
    print(a)
    len_a -= 1
