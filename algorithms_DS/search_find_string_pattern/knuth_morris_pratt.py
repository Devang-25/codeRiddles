#!/bin/env python3

# KMP
# Best case -- O(m + n): Prefix table has M, Search() has N
# Worst case -- O(mn): Prefix table is jumped upto M times for N elements

# Usage: $ ./knuth_morris_pratt.py
# Enter text: abadfdfababaca
# Enter pattern: ababaca

# Examples:
# small pattern: ababaca
# 0 1 2 3 4 5 6
# a b a b a c a
# 0 0 1 2 3 0 1

# longer pattern: acacabacacabacacac
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# a c a c a b a c a c a  b  a  c  a  c  a  c
# 0 0 1 2 3 0 1 2 3 4 5  6  7  8  9  10 11 4

_dbg = False
# _dbg = True
_values=[0]

# Type 1
def pattern_rollback(pattern, i, j):
    if pattern[i] == pattern[j]:
        j+=1
        _values.append(j)
    else:
        if j > 0:
            j = _values[j-1]
            if _dbg:
                print(i,j)
            j = pattern_rollback(pattern, i, j)
        else:
            _values.append(j)
    return j

def prefix_table(pattern):
    # O (M)
    j = 0
    for i in range(1, len(pattern)):
        if _dbg:
            print(i,j)
        j = pattern_rollback(pattern, i, j)
    return _values

# Type 2
def prefix_table_2(pattern):
    # O (M)    
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j+=1
            i+=1
            _values.append(j)
        else:
            if j > 0:
                j = _values[j-1]
            else:
                _values.append(j)
                i+=1
                
    return _values

# Type 3
# plain recursion w/ base case?

def search_pattern(ip, pattern):
    # O(N)
    # T = bacbabababacaca
    # P = ababaca
    
    # _values = prefix_table(pattern)
    _values = prefix_table_2(pattern)

    print("DFA: %s" % _values)
    
    i = j = 0
    m = len(pattern) - 1
    
    while i <= len(ip)-1:
        if _dbg:
            print(i,j)
        if pattern[j] == ip[i]:
            if j == m:
                return i-m, True
            j+=1
            i+=1
        else:
            if j>0:
                j = _values[j-1]
                continue
            i+=1
            
    return -1, False


if __name__ == '__main__':
    ip = input("Enter text: ")
    pattern = input("Enter pattern: ")
    _at, status = search_pattern(ip, pattern)
    print("%s at index %s" % (status, _at))


###############################
# Enter text: bacbabababacaca
# Enter pattern: ababaca
# DFA: [0, 0, 1, 2, 3, 0, 1]
# True at index 6
##############################
# with _dbg = True

# Enter text: bacbabababacaca
# Enter pattern: ababaca
# 1 0
# 2 0
# 3 1
# 4 2
# 5 3
# 5 1
# 5 0
# 6 0
# DFA: [0, 0, 1, 2, 3, 0, 1]
# 0 0
# 1 0
# 2 1
# 2 0
# 3 0
# 4 0
# 5 1
# 6 2
# 7 3
# 8 4
# 9 5
# 9 3
# 10 4
# 11 5
# 12 6
# True at index 6
