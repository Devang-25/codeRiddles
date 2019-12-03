"""
NOTE: 
Safely evaluate an expression node or a string 
containing a Python expression. The string or node provided 
may only consist of the following Python literal structures: 
strings, numbers, tuples, lists, dicts, booleans, and None.
"""

import ast #converts string of list into python list type

def flatten(L):
    '''
    Flattening a list '''
    if L==[]:
        return []
    elif isinstance(L[0],list):
        return flatten(L[0])+flatten(L[1:])
    else:
        return L[:1]+flatten(L[1:])

L = raw_input("Enter a list (or list[lists] or list[lists[lists]])..: ")

try:
    L = ast.literal_eval(L) #string -> list
    print "Sum of flattened list: %d"%(sum(flatten(L)))
except:
    raise

# https://learning.oreilly.com/scenarios/python-cookbook-data/9781492061465/

# recursive with *astrix (multi-value args format)
# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head

# >>> items = [1, 10, 7, 4, 5, 9]
# >>> head, *tail = items
# >>> head
# 1
# >>> tail
# [10, 7, 4, 5, 9]
