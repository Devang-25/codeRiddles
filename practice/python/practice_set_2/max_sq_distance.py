#!/bin/env python3

from itertools import combinations

def solution(A, B, C, D):
    max = 0
    list_all = [A, B, C, D]
    def calc_sq_sum(x,y):
        return  sum([(xi-yi)**2 for xi, yi in zip(x, y)])
    for pair in combinations(list_all, 2):
        aset = list_all.copy()
        [aset.remove(i) for i in pair]
        # print(aset, pair)
        tmp_sum = calc_sq_sum(aset, pair)
        if tmp_sum > max:
            max = tmp_sum    
    return max

assert solution(1,1,2,3) == 5
assert solution(2,4,2,4) == 8
