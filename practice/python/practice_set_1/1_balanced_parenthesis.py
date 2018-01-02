#!/usr/bin/python3

# Create function that will determine if the parenthesis are balanced
# in a given string 

def isBalanced(text):
    # type 1: use stacks and filter all brackets to see if
    # if anything left in stack in the end. if so, unbalanced

    # type 2: reduce all non parenthesis characters to null and
    # check rest of the string with type 1 algo

    # type 3: modify default str.maketrans ?
    # devise a method to translate the string to one that
    # has it's counter part bracket removed.
    # use ord()/chr() ?

    # type 4: modify KMP?
    # - others in domain: string searching / median of medians 

    # can't use yield / generators. As we need to process in place and time

    # type 5: using hashmaps for brackets and indices?
    
    p_open = '{[('
    p_close = '}])'
    
    S = []
    for i in text:
        if i in p_close:
            if S[-1] != p_open[p_close.index(i)]:
                return False
            else:
                S.pop(-1)
        elif i in p_open:
            S.append(i)
        else:
            continue

    if S:
        return False
    else:
        return True

assert isBalanced("a(bcd)d") == True
assert isBalanced("(kjds(hfkj)sdhf") == False
assert isBalanced("(sfdsf)(fsfsf") == False
assert isBalanced("{[]}()") == True
assert isBalanced("{[}]") == False # should be fully enclosed loops, no intersections


# from nose.tools import assert_equal
# from nose.tools import assert_dict_equal
# assert_dict_equal({5:1, 2: { 4:5}}, {2: { 4:6}, 5:1})

# import re
# parenthesis = '{}[]()<>'

################################################################
# # all possible parentheses combo for given length
# # courtesy: https://stackoverflow.com/a/20554991/1332401

# def paren(left, right=None):
#     if right is None:
#         right = left  # allows calls with one argument

#     if left == right == 0: # base case
#         yield ""

#     else:
#         if left > 0:
#             for p in paren(left-1, right): # first recursion
#                 yield "("+p

#         if right > left:
#             for p in paren(left, right-1): # second recursion
#                 yield ")"+p

# list(paren(4))

################################################################
