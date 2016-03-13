#!/usr/bin/env python3

def find_largest_palindrome(upper, lower):
    _tmp = {}
    for i in range(upper, lower,-1):
        flag = lower
        if flag <= i:            
            for j in range(i, flag, -1):
                x = str(i*j)
                if x == x[::-1]:
                    flag = j
                    _tmp[x] = (i,j)
                    break
        else:
            break
    return _tmp

_tmp = find_largest_palindrome(999,99)
final = [int(i) for i in _tmp.keys()]
print(max(final), _tmp[str(max(final))])

_tmp = find_largest_palindrome(99,9)
final = [int(i) for i in _tmp.keys()]
print(max(final), _tmp[str(max(final))])
