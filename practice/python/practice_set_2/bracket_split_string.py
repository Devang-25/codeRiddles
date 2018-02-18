#!/bin/env python3

# split string of brackets such that left split has same opening bracket count as the number of closing brackets in right split.
# return total length of string, in case no balance found.

from collections import Counter

def solution(S):
    # S_encoded = [0 if i == '(' else 1 for i in S]
    i = len(S)//2
    while 0 <= i < len(S):
        S_left = Counter(S[:i])
        S_right = Counter(S[i:])
        if S_left['('] > S_right[')']:
            i-=1
        elif S_left['('] < S_right[')']:
            i+=1
        elif S_left['('] == S_right[')']:
            break
    return i

assert solution('(())))(') == 4
assert solution('(())') == 2
assert solution('))') == 2
