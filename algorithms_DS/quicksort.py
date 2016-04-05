#!/usr/bin/env python3

import random

def quick_sort(A, size):
    if size < 2:
        return A
    pivot_ix = random.choice(range(size - 1))
    L = 0; U = size - 1
    while L < U:
        #import pdb; pdb.set_trace()
        while A[L] < A[pivot_ix]:
            L+=1
        while A[U] > A[pivot_ix]:
            U-=1
        A[L], A[U] = A[U], A[L]
    quick_sort(A, L)
    quick_sort(A[L:], size - L - 1)
    return A

X = input("enter space separated input integer  array: ")
X = [int(i) for i in X.split()]
print(quick_sort(X, len(X)))
