#!/usr/bin/env python2

# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/analysis.html
"""
An Anagram Detection Example
============================
A good example problem for showing algorithms with different orders 
of magnitude is the classic anagram detection problem for strings. 
One string is an anagram of another if the second is simply a 
rearrangement of the first. For example, 'heart' and 'earth' are 
anagrams. The strings 'python' and 'typhon' are anagrams as well. 
For the sake of simplicity, we will assume that the two strings in 
question are of equal length and that they are made up of symbols 
from the set of 26 lowercase alphabetic characters. Our goal is to 
write a boolean function that will take two strings and return whether
they are anagrams.
"""

# approach 2
from collections import Counter

def check_anagram(a, b):
    """
    ignore spaces
    case sensitive
    """
    a1 = Counter(a.replace(' ', ''))
    a2 = Counter(b.replace(' ', ''))
    
    for k,v in a1.items():
        try:
            assert a2[k] == v
        except:
            return False
    return True
        
check_anagram('aim','mai') == True
check_anagram('Afdd ','Af d') == True

# approach 3
def anagramSolution1(s1,s2):
    '''
    Compare each element of s1 to s2
    If found, swap character with None in s2
    if not found, stillOK = False and loop breaks

    Works for all characters / Unicode / ASCII
    '''
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
            #print pos1, pos2

        # print(alist)
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1
    return stillOK

# approach 4
def anagramSolution2(s1,s2):
    '''
    sort s1 and s2 and compare each position.

    # approach 1
    assert sorted('dog') == sorted('god')
    '''
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

# approach 5
# NOT FEASIBLE!
# generate all chars permutations from s1 and see if s2 lies in it
# A brute force technique for solving a problem typically tries to 
# exhaust all possibilities. For the anagram detection problem, we 
# can simply generate a list of all possible strings using the 
# characters from s1 and then see if s2 occurs. However, there is 
# a difficulty with this approach. When generating all possible 
# strings from s1, there are n possible first characters, n-1 
# possible characters for the second position, n-2 for the third, 
# and so on. The total number of candidate strings is 
# n*(n-1)*(n-2)*...*3*2*1, which is n!. 

# approach 6
def anagramSolution4(s1,s2):
    """
    # works for a-z if made to
    Check difference in ord(character) with 'a'
    either make it work for 26 chars and check parity against 'a'
    then maintain a list for each string and add make counters 
    for each character that way

    (Pdb) c1
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    (Pdb) c2
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]

    Could also just use ASCII range to do this. (see next approach below)
    """
    
    
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1


    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


# print(anagramSolution1('abcd',input("enter anagram for abcd: ")))
# print(anagramSolution2('abcde',input("enter anagram for abcde: ")))
# print(anagramSolution4('apple',input("enter anagram for apple: ")))
assert anagramSolution1('abcd','cdab') == True
assert anagramSolution2('abcde','a bcde') == False
assert anagramSolution4('apple','alpep') == True
assert anagramSolution2('x0R a','0 Rax') == True


# approach 7
def check_anagram_ascii(s1, s2):
    char_set1 = [0 for _ in range(128)]
    char_set2 = char_set1.copy()
    for c in s1:
        char_set1[ord(c)]+=1
    for c in s2:
        char_set2[ord(c)]+=1

    for i in range(128):
        if char_set1[i] != char_set2[i]:
            return False

    return True
