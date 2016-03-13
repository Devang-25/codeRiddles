#!/usr/bin/env python3

def find_largest_palindrome(upper, lower):
    _tmp = {}
    flag = lower-1
    for i in range(upper, lower-1, -1):
        if flag <= i:            
            for j in range(i, flag, -1):
                x = str(i*j)
                if x == x[::-1]:
                    flag = j-1
                    _tmp[x] = (i,j)
                    break
        else:
            break
    return _tmp

# _tmp = find_largest_palindrome(99999,10000)
# final = [int(i) for i in _tmp.keys()]
# print(max(final), _tmp[str(max(final))])
# print(_tmp)
# print()

_tmp = find_largest_palindrome(9999,1000)
final = [int(i) for i in _tmp.keys()]
print(max(final), _tmp[str(max(final))])
print(_tmp)
print()

_tmp = find_largest_palindrome(999,100)
final = [int(i) for i in _tmp.keys()]
print(max(final), _tmp[str(max(final))])
print(_tmp)
print()

_tmp = find_largest_palindrome(99,10)
final = [int(i) for i in _tmp.keys()]
print(max(final), _tmp[str(max(final))])
print(_tmp)
print()
