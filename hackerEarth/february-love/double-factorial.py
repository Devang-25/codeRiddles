from math import factorial
#for handling long int
import sys 
sys.setrecursionlimit(10000)

class DoubleFactorial:
    ''' Check triangle inequality'''
    def __init__(self, N, M):
        self.N = N
        self.M = M
    
    def generate_double_fact(self):
        return divmod(factorial(factorial(self.N)), 10**self.M)

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        ans = []
        for i in xrange(T):
            # input values
            ip = map(int, raw_input().split())
            #check on input
            assert len(ip)==2
            # intiate class object
            DF = DoubleFactorial(ip[0], ip[1])
            # append result to an answers list, to be printed later
            ans.append(DF.generate_double_fact())
        for i in ans: print i
    except:
        raise
