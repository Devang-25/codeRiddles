"""
Sample Input:

4
2 1
3 4
5 5
1 1
"""

from fractions import gcd


def decide(a,b):
    if a>b:
        return "Arjit"
    elif b>a:
        return "Chandu Don"
    elif a==b:
        return "Draw"

def play(a,b):
    if gcd(a,b)>1:
        if b%2 == 0:
            return b/2
        else:
            return b-1
    else:
        return b-1

if __name__ == '__main__':
    ans = []
    T = int(raw_input())
    for i in xrange(T):
        a,b = [int(i) for i in raw_input().split()]
        if a>1 and b>1:
            c = 0
            while a>1 and b>1:
                if c==0:
                    b = play(a,b)
                    c+=1
                else:
                    a = play(b,a)
                    c-=1
            ans.append(decide(a,b))
        else:
            ans.append(decide(a,b))

    for i in ans: print i
