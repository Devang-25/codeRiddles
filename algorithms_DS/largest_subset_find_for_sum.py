#!/usr/bin/env python3

###################################################################
# ..takes a list as input and returns the largest subset
# with a sum of value equal to T (taken as another user input)

# Usage: ./largest_subset_find_for_sum.py
# 
# Enter list of integers: 4,6,1,8
# Enter total sum value to compare against: 15
# Largest subset with sum <= total value is: (1, 6, 8)
#
###################################################################

import itertools

user_input = sorted([int(j) for j in \
                     input("Enter list of integers: ").split(',')])
total_sum = int(input("Enter total sum value to compare against: "))

def find_largest(ip_list, T):
    relevant = []
    for i in range(len(ip_list),0,-1):
        _tmp = itertools.permutations(ip_list, i)
        for subset in _tmp:
            if sum(subset) > T:
                find_largest(ip_list[:i-1], T)
            else:
                relevant.append(subset)
    d = 0
    S = None
    for subset in relevant:
        if sum(subset) > d:
            S = subset
            d = sum(subset)
    return S

print("Largest subset with sum <= total value is: %s" %
      str(find_largest(user_input, total_sum)))
