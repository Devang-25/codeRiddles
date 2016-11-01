#!/usr/bin/env python2

# https://www.interviewbit.com/problems/spiral-order-matrix-i/
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        rows = len(A)
        cols = len(A[0])
        B = rows - 1; T = 0; L = 0; R = cols - 1; dir = 0 
        # import pdb; pdb.set_trace()
        while T <= B and L <= R:
            if dir == 0:
                for i in xrange(L,R+1): 
                    print A[T][i],
                T+=1
            elif dir == 1:
                for i in xrange(T,B+1):
                    print A[i][R],
                R-=1
            elif dir == 2:
                for i in xrange(R,L-1,-1):
                    print A[B][i],
                B-=1
            elif dir == 3:
                for i in xrange(B,T-1,-1):
                    print A[i][L],
                L+=1
            dir = (dir + 1)%4
        ## Actual code to populate result
        return result

S = Solution()
A = ([1,2,3,4],
     [5,6,7,8],
     [9,10,11,12])
for i in A: print i
print
S.spiralOrder(A)
