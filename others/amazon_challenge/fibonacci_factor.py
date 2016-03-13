#!/usr/bin/python
"""
Amazon Problem: Fibonacci Factor. 
"""

import sys

class FibonacciFactor:
    ''' Find common Factors, return smallest 
    and also smallest fibonacci divisor '''
    
    def __init__(self, current):
        self.number = current
        #self.fibonacci_list = []

    def generate_factors(self):    
        '''
        Return all factors of a number.
        '''
        # generator object containing redundant factors
        factors = [[i, self.number/i] \
                   for i in xrange(1, int(self.number**0.5) + 1) \
                   if self.number % i == 0]
        # refine and return
        return set(reduce(list.__add__, factors))
        
    """
    def generate_fibonacci(self):
        ''' 
        To generate all fibonacci's less than 
        given number K (less than K).
        '''
        num1, num2 = 0, 1
        while num1 < self.number + 1:
            self.fibonacci_list.append(num1)
            num1, num2 = num2, (num1 + num2)
        self.fibonacci_list = self.fibonacci_list[3:] # eliminate 0,1,1
    """

    def get_smallest(self):
        ''' 
        solves for F and D.
        '''
        factors_list = sorted(list(self.generate_factors()))
        factors_list.remove(1)
        first = long(1)
        second = long(1)        

        # Use the commented code below, in case
        # you need fibonacci numbers <= K
        """
        self.generate_fibonacci()

        for fibonacci in self.fibonacci_list:
            for factor in factors_list:
                if divmod(fibonacci, factor)[1] == 0:
                    return [fibonacci, factor]
                else:
                    pass
        """
        while True:
            first, second = second, (first + second)
            for factor in factors_list:
                if divmod(second, factor)[1] == 0:
                    return [second, factor]
                else:
                    pass
        return [0, 0]
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
            FF = FibonacciFactor(K)
            FINAL.append(FF.get_smallest())
        
        for r in FINAL:
            print r[0], r[1]
    
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        sys.exit(1)
