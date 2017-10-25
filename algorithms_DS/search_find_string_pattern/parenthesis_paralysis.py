#!/bin/env python

# https://www.interviewcake.com/question/python/matching-parens
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0
    position = opening_paren_index + 1

    while position <= len(sentence) - 1:
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

        position += 1

    raise Exception("No closing parenthesis :(")


assert get_closing_paren('sdsd(sdsd)',4) == 9

import re

def get_closing_paren(pattern, ix):
    l_start = [i.start() for i in re.finditer('\(', pattern)]
    l_close = [i.start() for i in re.finditer('\)', pattern)]
    assert len(l_close) == len(l_start)
    
    return l_close[-(l_start.index(ix)+1)]

pat = 'sdsd(sd(sd)sdsd)'
assert get_closing_paren(pat,4) == 15
assert get_closing_paren(pat,7) == 10
