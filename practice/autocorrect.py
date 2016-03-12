#!/bin/env python3

# pretty naive implementation of autocorrect

import enchant
from string import ascii_lowercase
from itertools import product

# usage: ./autocorrect.py

# example1:
# Enter input string: xorrect
# You mean, one of these words?:
# correct

# example2:
# Enter input string: cgeck
# You mean, one of these words?:
# check

# example3:
# Enter input string: hoker
# You mean, one of these words?:
# homer, joker

dictionary = enchant.Dict("en_US")

row1 = list('qwertyuiop')
row2 = list('asdfghjkl')
row3 = list('zxcvbnm')
layout = {'qwerty': [[i for i in row1], [j for j in row2], [k for k in row3]]}
# this gives:
# [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#   ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#   ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
# lengths of rows: 10, 9, 7 resp..

def get_nearby_chars(layout_style, entered_char):    
    """ 
    helper method to suggest nearby characters present on a keyboard

    example: layout_style = layout['qwerty']
    """
    # init the character entered itself into list of proximity
    _tmp = [entered_char]
    for row in layout_style:
        try:
            pos = row.index(entered_char)
            current_row_index = layout_style.index(row)
            if current_row_index != len(layout_style)-1:
                # if current row is not last one, suggest 2 more chars
                if pos <= len(layout_style[current_row_index+1])-1:
                    _tmp.append(layout_style[current_row_index+1][pos])
                else:
                    _tmp.append(layout_style[current_row_index+1][-1])
                if pos < len(row)-1:
                    _tmp.append(row[pos+1])
                else:
                    _tmp.append(row[pos-1])

            else:
                # if last row is the current one, suggest only 1 more char
                if pos > len(row)-1:
                    _tmp.append(row[pos-1])
                else:
                    _tmp.append(row[pos+1])
        except:
            continue

    return _tmp


class Autocorrect(object):
    """
    Finds an input word and returns the nearby words
    if the input is not a word itself. Think, autocorrect.
    """
    def __init__(self, word):
        self.word = word
        self.style = 'qwerty'
        
    def nearby_permutations(self):
        _tmp = []
        
        for current_key in list(self.word):
            _tmp.append(get_nearby_chars(layout[self.style], current_key))
        
        perms_vector = list(product(*_tmp))        
        perms_vector = [''.join(i) for i in perms_vector]
        return perms_vector
    
    def nearby_words(self):
        x = self.nearby_permutations()
        dict_checked_vector = [i for i in x if dictionary.check(i)]
        return dict_checked_vector

if __name__ == '__main__':
    try:
        user_input = input("Enter input string: ")
        AC = Autocorrect(user_input)
        suggested = ', '.join(AC.nearby_words())
        if suggested == user_input:
           print("You entered a valid word: %s" % user_input)
        elif suggested:
            print("You mean, one of these words?: \n%s" % suggested)
        else:
            print("No suggestions found for: %s" % user_input)            

    except:
        raise


# x = str.maketrans(ascii_lowercase,
#                   ascii_lowercase[2:] + ascii_lowercase[:2])

# shift each letter 2 integer ordinals backwards
# 'fcjjm'.translate(x) - > hello

# import re

# w = 'word'
# test_single_word = re.compile(r'\b({0})\b'.format(w),
#                               flags=re.IGNORECASE).search

# print test_single_word('words shall seek the truth')
# print test_single_word('wordsmith shall seek the truth')
# print test_single_word('word shall seek the truth')
