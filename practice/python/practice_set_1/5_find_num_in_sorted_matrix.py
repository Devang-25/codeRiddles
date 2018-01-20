#!/bin/env python3

# 1. Find a number in sorted matrix
# Given a matrix of numbers that is sorted both row and column-wise and another number, write a function that returns True or False depending whether is present in the matrix or not.

# 10 20 30 40
# 12 22 32 43
# 21 24 41 51
# 23 31 42 52

# num = 22 Ans- True
# num = 52 Ans - True
# num = 100 Ans- False
# num = 43 Ans- True
# num =  27 Ans - False

mat = '''
10 20 30 40
12 22 32 43
21 24 41 51
23 31 42 52
'''
print(mat)

mat = mat.splitlines()[1:]
# mat = ['10 20 30 40', '12 22 32 43', '21 24 41 51', '23 31 42 52']
mat = [arr.split() for arr in mat]
mat = [[int(i) for i in arr] for arr in mat]
# mat => [[10, 20, 30, 40], [12, 22, 32, 43], [21, 24, 41, 51], [23, 31, 42, 52]]

def bin_search(mat, l, r, x):
    """
    Approach is to compare number with diagonal values (like binary search, but modified)
    # optimize this by finding out where to start from. Example If we wanna find 41
    # we need to probably start from 43 (it might not lie on the diagonal)
    """
    print(l, r)
    if r > l:
        mid_i = l[0] + (r[0] - l[0])//2
        mid_j = l[1] + (r[1] - l[1])//2
        mid = mat[mid_i][mid_j]
        print("current mid: %s"%mid)
        if mid == x:
            return True
        elif mid > x:
            print("searching left\n")
            # return bin_search(mat, l, mid-1, x)
            return bin_search(mat, l, [mid_i-1, mid_j-1], x)
        else:
            print("searching right\n")
            # return bin_search(mat, mid+1, r, x)
            return bin_search(mat, [mid_i+1, mid_j+1], r, x)
    elif l == r:
        pass
    else:        
        return -1
    
x = 21
print("..searching for %s\n" % x)
# assume square matrix
assert bin_search(mat, [0,0], [len(mat)]*2, x) == True
# it fails currently, but I'm still working on my modified binary search for matrix

# approach 2:
