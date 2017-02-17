#!/bin/env python3

# aaabbcd -> abcd
# https://groups.google.com/forum/#!forum/dsa_sg

# O(n)

def eliminate(x):
    x = list(x)
    tmp = ''
    # import pdb; pdb.set_trace()
    for i in range(0,len(x),2):
        if (tmp and tmp[-1]!=x[i]) or not tmp:
            tmp+=x[i]        
        if i+1 < len(x):
            if x[i]!=x[i+1]:
                tmp+=x[i+1]
    return tmp

assert eliminate('aaabbcd') == 'abcd'
assert eliminate('aaabbacd') == 'abacd'
assert eliminate('aaabbaacd') == 'abacd'
assert eliminate('aaaaaa') == 'a'

# def eliminate_binary(x,tmp=''):
#     t = len(x)
#     eliminate_binary(x[:t/2])
