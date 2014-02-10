#Skeleton for using collections
"""
import collections

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
"""

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
    quit("\n\n\tCould not convert data to an integer.\n")
except KeyboardInterrupt:
    quit("\n\n\tYou aborted the program!\n")
except:
    print "Unexpected error:", sys.exc_info()[0]  # >>sys.exc_info()<< gives whole exception
    raise #system call to raise the exception out loud
"""

# actual frame sample
class BotCheck:
    ''' Check the bot moves'''
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def testFinal(self):
        # for A
        a_pos_init = [i for i, x in enumerate(list(self.initial)) if x == 'A']
        a_pos_final = [i for i, x in enumerate(list(self.final)) if x == 'A']
        # for B
        b_pos_init = [i for i, x in enumerate(list(self.initial)) if x == 'B']
        b_pos_final = [i for i, x in enumerate(list(self.final)) if x == 'B']
        #check on whether A moves left and doesn't jump B
        for i in xrange(len(a_pos_init)):
            if a_pos_init[i] >= a_pos_final[i] and \
               a_pos_final[i] not in range(b_pos_init[0],b_pos_init[-1]+1):
                flag_A = True
            else:
                flag_A = False
        #check on whether B moves right and doesn't jump A
        for i in xrange(len(b_pos_init)):
            if b_pos_init[i] <= b_pos_final[i] and \
               b_pos_final[i] not in range(a_pos_init[0],a_pos_init[-1]+1):
                flag_B = True
            else:
                flag_B = False
        # return results
        if flag_A and flag_B:
            return 'Yes'
        else:
            return 'No'

if __name__ == '__main__': 
    # input comma-separated elements into array
    '''
    cnt = raw_input().split(',')
    cnt[-1] = cnt[-1].rstrip('}')
    cnt[0] = cnt[0].lstrip('{') '''
    # checks and converts list of strings into integers 
    '''
    cnt = map(int, cnt)
    baseCost = int(raw_input())
    seatCost = int(raw_input()) '''

    # actual sample code
    try:
        t = int(raw_input())
        assert 1<=t<=1000
        ans = []
        for i in xrange(t):
            # input values
            bots = raw_input().split()
            #check on bots count
            assert len(bots)==2
            #check on strings
            assert len(bots[0])==len(bots[1])
            # check on bot names A/B
            b1,b2 = set(''.join(bots[0].split('#'))), set(''.join(bots[1].split('#')))
            z = lambda x: ord(x)==65 or ord(x)==66
            assert z(b1.pop()) and z(b1.pop()) and z(b2.pop()) and z(b2.pop())
            # pass the tested attributes
            Bc = BotCheck(bots[0], bots[1])
            ans.append(Bc.testFinal())
        for i in ans: print i
    except:
        quit()
