#!/bin/env python3

# https://www.interviewbit.com/problems/smallest-sequence-with-given-primes/
# their solution

from heapq import heappush, heappop


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        if D == 0: return []
        
        p1,p2,p3 = A,B,C
        k = D
        
        primes_pq = []
        min_primes = []
        max_primes = []
        
        uniq = set()
        
        for x in [p1,p2,p3]: heappush(primes_pq, x)
        
        while len(primes_pq) != 0:
            num = heappop(primes_pq)
            
            if len(max_primes) >= k and max_primes[0] < num: continue
        
            if num in uniq: continue

            heappush(min_primes, num)
            heappush(max_primes, -num)
            
            uniq.add(num)
            
            for x in [p1,p2,p3]: heappush(primes_pq, num * x)

        final = [heappop(min_primes) for _ in range(k)]
        print("Total generated: %s v/s k=%s for input %s" \
              % (len(final), D, [p1,p2,p3]))            
        return final

arr = [2,3,5]
S = Solution()
assert S.solve(*arr,3) == [2,3,4]
print('='*60)
assert S.solve(*arr,5) == [2,3,4,5,6]
print('='*60)
assert S.solve(2,2,2,0) == []
print('='*60)
assert S.solve(3,11,7,50) == [3, 7, 9, 11, 21, 27, 33, 49, 63, 77, 81, 99, 121, 147, 189, 231, 243, 297, 343, 363, 441, 539, 567, 693, 729, 847, 891, 1029, 1089, 1323, 1331, 1617, 1701, 2079, 2187, 2401, 2541, 2673, 3087, 3267, 3773, 3969, 3993, 4851, 5103, 5929, 6237, 6561, 7203, 7623]
print('='*60)
