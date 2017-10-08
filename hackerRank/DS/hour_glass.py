#!/bin/env python3

import sys


# format of hour glass
# # a b c
# #   d
# # e f g

arr = []
N = 6

_dbg = False
# _dbg = True

for arr_i in range(N):
    arr_temp = [int(i) for i in input().strip().split(' ')]
    for i in arr_temp:
        assert -9 <= i <= 9
    assert len(arr_temp) == 6
    arr.append(arr_temp)

assert len(arr) == 6
c = 0
_max = None

for i in range(N-2):
    for j in range(N-2):
        tmp = []
        tmp.append(arr[j][i:i+3])
        tmp.append([arr[j+1][i+1]])
        tmp.append(arr[j+2][i:i+3])
        # hour_glasses.append(tmp)
        total = sum([sum(l) for l in tmp])
        if _dbg:
            print(i, total, tmp)
        if _max is None:
            _max = total
        if total > _max:
            _max = total        
        c+=1

if _dbg:
    print("Total hour glasses: ", c)

print(_max)

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# -1 1 -1 0 0 0
# 0 -1 0 0 0 0
# -1 -1 -1 0 0 0
# 0 -9 2 -4 -4 0
# -7 0 0 -2 0 0
# 0 0 -1 -2 -4 0
