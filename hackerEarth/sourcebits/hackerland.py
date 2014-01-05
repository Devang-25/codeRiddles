#import collections
import math
        
class HackerLand:
    """ Least coin split, not prime """
    def isprime(self, n):
        n = abs(n)
        if n < 2:
            return False
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return True

    def getLeastCoins(self, coin):
        #sub = []
        count = 0
        cache = coin
        if coin==3:
            return 3
        #myland = HackerLand()
        #print self.isprime(coin) 
        while(self.isprime(coin)==True and coin >= 1):
            coin -= 1
            count += 1
            #print cache, coin, count
        
        #if self.isprime(coin):
        #    pass
        #elif self.isprime
        if count == 0:
            return 1 #coin is non-prime
        elif count == cache:
            return 0
        else:
            return 2 #solved: coin, count

if __name__ == '__main__': 
    try:
        T = int(raw_input())
    except:
        #quit('Constraint: Only integer / no space input allowed')
        quit()

    if 1<=T<=100:
        pass
    else:
        quit("don't satisfy the Test case constraint..")            

    r = []
    hl = HackerLand()    
    for i in xrange(T):
        ip = int(raw_input())
        if 1<=ip<=100000:
            r.append(hl.getLeastCoins(ip))
        else:
            #quit('\namount constraint check\n')
            quit()
    #print r
    for i in r:
        print i
