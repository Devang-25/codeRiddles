class BrainBuster:
    '''Chang and the Mathematical Brainbuster'''
    def __init__(self, ip):
        self.ip = sorted(ip)

    def force_condition(self):
        count = 0
        while max(self.ip) - 3*min(self.ip) > 0:
            self.ip.pop()
            count+=1
        return count

if __name__ == '__main__': 
    N = int(raw_input())
    assert 1<=N<=10**4
    # input values
    ip = map(int, raw_input().split())
    #check on input
    assert len(ip)==N
    assert max(ip)<=10**4 and 1<=min(ip)
    # intiate class object
    BB = BrainBuster(ip)
    # append result to an answers list, to be printed later
    print BB.force_condition()
