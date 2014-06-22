"""
Choose a number, reverse its digits and add it to 
the original. If the sum is not a palindrome (which 
means, it is not the same number from left to right 
and right to left), repeat this procedure. 
"""

import fileinput

def reverseAdd(N, c):
    """ 
    find palindrome and apply the rule.
    """
    if str(N) == str(N)[::-1]:
        return c, N
    else:
        c+=1
        return reverseAdd(N + int(str(N)[::-1]), c)

if __name__ == '__main__':
    ANS = []
    for line in fileinput.input():
        ANS.append(reverseAdd(int(line), 0))
    for j in ANS:
        print j[0], j[1]
