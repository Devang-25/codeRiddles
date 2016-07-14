#!/usr/bin/env python3

# given a number n, find minimum positive integer base b
# which when used for calculating the resulting cycle, is a palindorme.

# Example,
# 42 base 4 is 222, which is a palindrome. Hence:
#   input:  $ 42
#   output: $ 4

## clean code
# def answer(n):
#     # n/2 is python 3 gives a float
#     for i in range(2, n//2):
#         x = n
#         s = []
#         while x > 0:
#             s.append(x % i)
#             x //= i
#         if x != 0:
#             s.append(x)
#         v = len(s) % 2
#         if v != 0:
#             s.pop(len(s) // 2)            
#         if s[::-1] == s:
#             return i
#     return 2


## debug code
def answer(n, s_reversed=[]):
    # n/2 is python 3 gives a float
    for i in range(2, n//2):
        s_reversed=[]
        x = n
        s = []
        while x > 0:
            s.append(x % i)
            x //= i
        if x != 0:
            s.append(x)
        v = len(s) % 2
        s_reversed = s[::-1]

        #print(n,i,s_reversed)
        if v != 0:
            s.pop(len(s) // 2)
            
        if s[::-1] == s:
            return n,i, s_reversed

    return n,2,s_reversed

diff=42
print("calculating for all numbers in range (0,1000,42)...")
for k in range(0,1000,diff):
    print(answer(k))
