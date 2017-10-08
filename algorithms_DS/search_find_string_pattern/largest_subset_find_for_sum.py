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
                     input("Enter list of integers (csv): ").split(',')])
total_sum = int(input("Enter total sum value to compare against: "))

def find_largest(ip_list, T, c):
    relevant = []
    _tmp = itertools.combinations(ip_list, c)

    for subset in _tmp:
        if sum(subset) <= T:
            relevant.append(subset)
        else:
            continue

    if not relevant:
        if len(ip_list) == 1:
            if sum(ip_list) <= T:
                return ip_list
            else:
                return
        elif not ip_list:
            return
        else:
            relevant.append(find_largest(ip_list, T, c-1))
            
    d = 0
    S = None
    for subset in relevant:
        if sum(subset) >= d:
            S = subset
            d = sum(subset)

    return S

answer = find_largest(user_input, total_sum, len(user_input))

print("Largest subset with sum <= total value is: %s" % str(answer))
print("Sum of this largest set (value accrued at the end of the day): %s" % sum(answer))
