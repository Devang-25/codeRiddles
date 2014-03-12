#!/usr/bin/python
"""
Amazon Problem: Shortest Sub-Segment.
"""

import sys

class ShortestSubSeg:
    ''' Find common Factors, return smallest 
    and also smallest fibonacci divisor '''
    
    def __init__(self, current):
        self.number = current

    def foo(self):
        '''
        ...
        '''
        # bar
        factors = [[i, self.number/i] \
                   for i in xrange(1, int(self.number**0.5) + 1) \
                   if self.number % i == 0]
        # bar
        return set(reduce(list.__add__, factors))

# main
if __name__ == '__main__': 
    try:
        # Test input
        T = long(raw_input())
        assert 1 <= T <= 5        
        FINAL = []
        for case in xrange(T):
            K = int(raw_input())
            assert 2 <= K <= 1000000
            SS = ShortestSubSeg(K)
            FINAL.append(SS.get_smallest())
        
        for r in FINAL:
            print r[0], r[1]
    
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        sys.exit(1)
