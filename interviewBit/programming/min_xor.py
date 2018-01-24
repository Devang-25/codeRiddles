#!/bin/env python3

# https://www.interviewbit.com/problems/min-xor-value/

from itertools import combinations


def findMinXor(A):
    # not an optimal solution as we're working with an unsorted array
    # The first step is to sort the array.
    # The answer will be the minimal value of X[i] XOR X[i+1] for every i.
    # details near the end of this script
    min_pair = [None,None,None]
    # res = []
    for i, j in combinations(A, 2):
        tmp = i ^ j
        # res.append([tmp,i,j])
        if min_pair[0] is None:
            min_pair = [tmp, i, j]
            continue
        if tmp < min_pair[0]:
            # print(tmp, i, j)
            # print(min_pair)
            min_pair = [tmp, i, j]
            # print(min_pair)
            # print()
            
    _op = "{} ({} XOR {})"
    return _op.format(*min_pair)#, res


assert findMinXor([0,4,7,9]) == '3 (4 XOR 7)'

A = [ 121088, 1164860, 558464, 638080, 758588, 858240, 612224, 1112064, 684860, 728704, 1021500, 329472, 1098812, 513024, 838784, 832256, 171196, 1210752, 227260, 951228, 1071164, 397244, 1095424, 1077760, 1164800, 461056, 965436, 774144, 160384, 806272, 880000, 1041280, 732604, 622208, 245760, 17980, 1085756, 647740, 891708, 196608, 190268, 878012, 800572, 179712, 1274300, 686720, 560700, 247612, 692924, 1010492, 733440, 191232, 364032, 1056188, 638908, 540476, 575744, 1001728, 1164800, 196156, 308736, 1164860, 94336, 1272380, 511036, 1273984, 442428, 610748, 985728, 309180, 1137340, 83132, 677308, 332860, 52096, 653184, 809148, 1196348, 641920, 1021056, 1041468, 111548, 833468, 151740, 10880, 108288, 103740, 1056512, 428800, 684288, 630972, 1188352, 1050240, 913664, 1000764, 273920, 1251968, 952576, 848956, 1251004, 617788, 301372 ]

# multiple possibilities with 0 as XOR result, but as per our logic, we'd get:
assert findMinXor(A) == '0 (1164860 XOR 1164860)'


# Suggested approach:
# The first step is to sort the array. The answer will be the minimal value of X[i] XOR X[i+1] for every i.

# Proof: 
# Let’s suppose that the answer is not X[i] XOR X[i+1], but A XOR B and there exists C in the array such as A <= C <= B.

# Next is the proof that either A XOR C or C XOR B are smaller than A XOR B.

# Let A[i] = 0/1 be the i-th bit in the binary representation of A 
# Let B[i] = 0/1 be the i-th bit in the binary representation of B 
# Let C[i] = 0/1 be the i-th bit in the binary representation of C

# This is with the assumption that all of A, B and C are padded with 0 on the left until they all have the same length

# Example: A=169, B=187, C=185

# A=101010012 
# B=101110112 
# C=101110012

# Let i be the leftmost (biggest) index such that A[i] differs from B[i]. There are 2 cases now: 
# 1) C[i] = A[i] = 0, 
# then (A XOR C)[i] = 0 and (A XOR B)[i] = 1 
# This implies (A XOR C) < (A XOR B) 
# 2) C[i] = B[i] = 1, 
# then (B XOR C)[i] = 0 and (A XOR B)[i] = 1 
# This implies (B XOR C) < (A XOR B)

# Time complexity: O(N * logN) to sort the array and O(N) to find the smallest XOR 
# Space complexity: O(N)
