import decimal 

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self
    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

class CookieClicker:
    ''' Check the bot moves'''
    def __init__(self, C, F, X, time_class):
        self.C = C
        self.F = F
        self.X = X
        self.cookies = 0.0
        self.rate = 2.0
        self.time = 0.0

    def run_strategy(self):
        while self.cookies < self.X:
            with Timer() as t:
                if self.cookies >= self.C:
                    self.rate += self.F
                    self.cookies -= self.C
            self.time += t
            self.cookies += self.time * self.rate
                
        return self.time
                    
if __name__ == '__main__': 
    t = int(raw_input())
    assert 1<=t<=100
    ans = []
    d = decimal.Decimal
    for i in xrange(t):
        # input values
        condition = raw_input().split()
        #check condition
        assert len(condition)==3
        #check on decimal digits count: [1,5] x 3
        temp = d(condition[0]).as_tuple().exponent + \
               d(condition[1]).as_tuple().exponent + \
               d(condition[2]).as_tuple().exponent
        assert 3 <= abs(temp)<= 15
        # convert list elements: str to float
        condition = map(float, condition)
        # check on range
        assert 1.0 <= condition[0] <= 500.0
        assert 1.0 <= condition[1] <= 4.0
        assert 1.0 <= condition[2] <= 2000.0

        # pass the tested attributes
        CC = CookieClicker(condition[0], condition[1], condition[2])
        ans.append(CC.run_strategy())
    for i,e in enumerate(ans): print "Case #%d: %.7f" % (i+1, e)
