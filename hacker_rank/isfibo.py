class IsFibo:
    def __init__(self, number):
        self.N = number
        self.a = [1,1]

    def final(self):
        while True:
            if self.N in self.a:
                return "IsFibo"
            elif self.a[-1] > self.N:
                return "IsNotFibo"
            else:
                self.a.append(self.a[-2] + self.a[-1])
            
if __name__ == '__main__': 
    t = int(raw_input())
    assert 1<=t<=10**5
    ans = []
    for i in xrange(t):
        n = int(raw_input())
        assert 1<=n<=10**10
        IF = IsFibo(n)
        ans.append(IF.final())
    for i in ans: print i

