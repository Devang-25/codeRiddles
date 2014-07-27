"""
Sample Input:

7
1 3 2 3 4 5 5
5
1 1 1
1 2 2
1 4 3
1 5 4
1 7 5
"""

N = int(raw_input())
A = [int(i) for i in raw_input().split()]
assert len(A) == N

# def xor(l,r,X):
#     temp = A[l-1:r]
#     res = {}
#     for j in set(temp):
#         res[(j^X)] = j
#     Z = res[min(res)]
#     return (Z, temp.count(Z))

def xor(l,r,X):
    temp = A[l-1:r]
    LEAST = temp[0]^X
    Z = temp[0]
    for j in set(temp):
        CURR = j^X
        if CURR < LEAST: LEAST = CURR; Z = j
    return (Z, temp.count(Z))

if __name__=='__main__':
    Q = int(raw_input())
    ans = []
    for i in xrange(Q):
        l,r,X = [int(i) for i in raw_input().split()]
        ans.append(xor(l,r,X))
    for i in ans: print '%d %d'%(i[0],i[1])
