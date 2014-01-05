import collections

# Skeleton for exception handling 
"""
import sys

try:
    # for system arguments: input supply alongwith compilation
    print sys.argv[1:]
    
    # sample statements
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]  # >>sys.exc_info()<< gives whole exception
    raise #system call to raise the exception out loud
"""

class TheShuttles:
    '''Return the minimum possible number of rabbits in this town.'''
    
    def __init__(self, cnt, baseCost, seatCost):
        if cnt and baseCost and seatCost:
            self.cnt = cnt
            self.seatCost = seatCost
            self.baseCost = baseCost

    def getLeastCost(self):
        counter=collections.Counter(self.cnt)
        counter.values()
        counter.keys()
        counter.items()
        money_needed = [self.cnt,self.baseCost,self.seatCost]
        return money_needed, counter

if __name__ == '__main__': 
    try:
        # input comma-separated elements into array
        cnt = raw_input().split(',')
        cnt[-1] = cnt[-1].rstrip('}')
        cnt[0] = cnt[0].lstrip('{')
        # checks and converts list of strings into integers 
        cnt = map(int, cnt)
        baseCost = int(raw_input())
        seatCost = int(raw_input())    
    except:
        quit('Constraint: Only integer / no space input allowed')

    if 1<=len(cnt)<=50:
        pass
    else:
        quit("Employee_count don't satisfy the constraint..")            
        
    if ((max(cnt, key=int) and baseCost and seatCost) < 101) and (0 < (min(cnt, key=int) and baseCost and seatCost)):
        pass
    else:
        quit('Constraint: Check range -> [1,100]')
        
    Sh = TheShuttles(cnt, baseCost, seatCost)
    result = Sh.getLeastCost()
    print type(result), result
