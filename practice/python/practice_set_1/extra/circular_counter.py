#!/bin/env python3

# https://github.com/keon/algorithms/blob/master/array/circular_counter.py
# START = 1
# END = 101
# SKIP = 2

# modified question:
# 100 people standing in a circle, in an order 1 to 100.
# No. 1 has a sword. He kills the next person (i.e., No. 2)
# and gives the sword to the next (i.e., No. 3)
# All people do the same until only 1 survives. Who'll survive in the end?
START = 1
END = 101
SKIP = 1
# boils down to skip 1 circularly until all but 1 are skipped
# 1 kills 2, hands the sword to 3 -->
# 3 kills 4, hands the sword to 5 -->
# 5 kills 6, ....

# the following iteration sequences form:
# (people in this list removed elements from previous iterations)
# [1, 3, 5, 7, 9, 11, .... ] ## eliminated [2,4,6, ... ]
# [1, 5, 9, 13, 17, 2 .... ] ## eliminated [3,7,13, ...]
# ... and so on.

a = list(range(START, END))
ix = 0
skip = ix + SKIP
len_a = len(a)

while len_a>0:
    ix = (skip+ix)%len_a
    if len_a == 1:
        print(a)
    # print(a.pop(ix))
    a.pop(ix)
    print(a)
    len_a -= 1
