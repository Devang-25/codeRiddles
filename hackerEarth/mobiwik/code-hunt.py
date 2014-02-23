class CodeHunt:
    '''Find the prized door'''
    def __init__(self, ip, array_size):
        self.ip = ip
        self.array_size = array_size
    
    def euclid_GCD(self, m, n):
        """
        Euclid's algorithm to find GCD (m,n)
        # 1000000 loops, best of 3: 518 ns per loop
        """
        while n % m != 0:
            r = n % m
            n = m
            m = r
        return m

    def find_correct_door(self):
        self.door_number = 0
        for i in xrange(self.array_size-1):
            for j in xrange(i+1, self.array_size):
                if self.euclid_GCD(self.ip[i], self.ip[j]) == self.ip[j]:
                    temp = self.euclid_GCD(2**self.ip[i]-1, 2**self.ip[j]-1)
                    if temp == 2**self.ip[j]-1:
                        self.door_number += 1;
                    else:
                        self.door_number -= temp
        return self.door_number

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        assert 1<=T<=20
        ans = []
        for i in xrange(T):
            # input values
            array_size = int(raw_input())
            ip = map(int, raw_input().split())
            #check on input
            assert len(ip)==array_size
            # intiate class object
            CH = CodeHunt(ip, array_size)
            # append result to an answers list, to be printed later
            ans.append(CH.find_correct_door())
        for i in ans: print i
    except:
        raise
