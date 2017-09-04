from itertools import combinations
from operator import and_
import sys

# testcases/minima.txt
class FindMinima:

    ''' 
    Apply AND operator on subsets with given conditions 
    '''

    def __init__(self, size, ip):
        self.N = size
        self.parent = ip
        self.subsets = []
        self.results = []

    def produce_subsets(self):
        [self.subsets.extend(list(combinations(self.parent, x))) \
         for x in xrange(2, self.N + 1)]
        #print self.subsets
        [self.results.append(reduce(and_, subset)) \
         for subset in self.subsets]
        return min(self.results)

   # def produce_subsets(self):
   #      a = 10
   #      for x in xrange(2,self.N+1):
   #          c = set(itertools.combinations(self.parent, x))
   #          for i in xrange(len(c)):
   #              a = min(a, reduce(operator.and_, c.pop()))
   #      return a


if __name__ == '__main__':
    T = int(raw_input())
    ans = []
    total = 0
    for i in xrange(T):
        size = int(raw_input())
        ip = map(int, raw_input().split())
        assert size == len(
            ip) and 2 <= size <= 10 ** 5 and 1 <= min(ip) and max(ip) <= 10 ** 18
        total += size
        assert 2 <= total <= 100000
        FM = FindMinima(size, ip)
        ans.append(FM.produce_subsets())
    for i in ans:
        print i
