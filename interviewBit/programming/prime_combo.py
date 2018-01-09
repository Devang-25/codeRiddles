#!/bin/env python3

# https://www.interviewbit.com/problems/smallest-sequence-with-given-primes/

# Given three prime number(p1, p2, p3) and an integer k. Find the first(smallest) k integers which have only p1, p2, p3 or a combination of them as their prime factors.

# for p1
# initial = [p1, p2, p3]
# index = [0,0,0]
# final = [min(initial)] == [p1]
# for i in range(k):
#   M = min(initial)
#   x = initial.index(M)
#   initial[x] = final[index[x]] * p1


class Solution(object):
    '''
    Solution.solve(*args)

    @args: contains for items in a list as follows:
    [p1, p2, p3, k]

    p* are distinct primes 
    k is total elements to be returned in a list
    '''
    _dbg = False # print iteration debug info
    _soft_dbg = True # print metadata about run
    
    def print_debug_info(self, *args, new=False, final=False):
        if self._dbg:
            print(*args)
        if new and self._dbg:
            print('-'*10)
        if final and self._soft_dbg:
            print("Total generated: %s v/s k=%s for input %s" \
                  % (args[0], args[1], args[2]))
            print('='*60)
            
    def solve(self, *args):
        k = args[-1]
        p1,p2,p3 = args[:-1]
        initial = list(args[:-1])
        maps = dict(zip(range(3), initial))
        final = []
        ix_final = [0] * len(initial)
        if not final and k!=0:
            final = [min(initial)]
            self.print_debug_info(initial, ix_final, final, new=True)
        
        for i in range(k):
            M = min(initial)                
            if final[-1] != M:
                final.append(M)
            self.print_debug_info(i, M)

            while True:
                try:
                    p = initial.index(M)
                    initial[p] = final[ix_final[p]] * maps[p]
                    ix_final[p] += 1
                except ValueError:
                    break
            self.print_debug_info(initial, ix_final, final, new=True)
            
        self.print_debug_info(len(final), k, args[:-1], final=True)
        
        return final

# if M == initial[0]:
#     initial[0] = final[ix_final[0]] * p1
#     ix_final[0] += 1
# if M == initial[1]:
#     initial[1] = final[ix_final[1]] * p2
#     ix_final[1] += 1
# if M == initial[2]:
#     initial[2] = final[ix_final[2]] * p3
#     ix_final[2] += 1

arr = [2,3,5]
S = Solution()
assert S.solve(*arr,3) == [2,3,4]
assert S.solve(*arr,5) == [2,3,4,5,6]

assert S.solve(2,2,2,0) == []
assert(S.solve(3,11,7,50)) == [3, 7, 9, 11, 21, 27, 33, 49, 63, 77, 81, 99, 121, 147, 189, 231, 243, 297, 343, 363, 441, 539, 567, 693, 729, 847, 891, 1029, 1089, 1323, 1331, 1617, 1701, 2079, 2187, 2401, 2541, 2673, 3087, 3267, 3773, 3969, 3993, 4851, 5103, 5929, 6237, 6561, 7203, 7623]

# OUTPUT
# Total generated: 3 v/s k=3 for input (2, 3, 5)
# ============================================================
# Total generated: 5 v/s k=5 for input (2, 3, 5)
# ============================================================
# Total generated: 0 v/s k=0 for input (2, 2, 2)
# ============================================================
# Total generated: 50 v/s k=50 for input (3, 11, 7)
# ============================================================


#########################################################
# from itertools import combinations as gen_comb

# class Solution(object):
    # def __init__(self):
    #     pass
    
    # def generate_next(self, *args):
    #     return [x[0]*x[1] for x in gen_comb(args, 2)]
    
    # def solve(self, *args):
    #     # print(args)
    #     k = args[-1]
    #     self.combo = args[:-1]
    #     if k == 3:
    #         return list(args[:-1])
    #     elif k < 3:
    #         return "arg length less than supplied prime combo"
    #     else:
    #         combo.extend([i**2 for i in args[:-1]])
    #         combo.extend()
    #         for i in range(k-3):

