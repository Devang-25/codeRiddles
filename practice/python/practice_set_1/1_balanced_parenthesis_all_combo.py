# import re
# parenthesis = '{}[]()<>'

################################################################
# # all possible parentheses combo for given length
# # courtesy: https://stackoverflow.com/a/20554991/1332401

def paren(left, right=None):
    if right is None:
        right = left  # allows calls with one argument

    if left == right == 0: # base case
        yield ""

    else:
        if left > 0:
            for p in paren(left-1, right): # first recursion
                yield "("+p

        if right > left:
            for p in paren(left, right-1): # second recursion
                yield ")"+p

for comb in paren(3):
    print(comb)

################################################################
