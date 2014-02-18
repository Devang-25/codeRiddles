import collections

class OccuranceCheck:
    ''' Check the digit occurances'''

    def __init__(self, cnt):
        self.digit = cnt[2]
        self.lower = cnt[0]
        self.upper = cnt[1]

    def calculate_occurances(self):
        # This performs the following: range(10,12) gives [ ['1','0'], ['1','1'] ]
        occurrances = map(lambda x: list(x), map(str, xrange(self.lower, self.upper+1)))
        # This performs the following: [ ['1','0'], ['1','1'] ] gives [1,0,1,1]
        occurrances = map(int, [item for sublist in occurrances for item in sublist])
        # calculates digit frequencies
        counter = collections.Counter(occurrances)
        # return the result
        return counter.get(self.digit)

if __name__ == '__main__': 
    try:
        T = int(raw_input())
        ans = []
        for i in xrange(T):
            # input values
            cnt = map(int, raw_input().split())
            #check on input
            assert len(cnt)==3
            # intiate class object
            OC = OccuranceCheck(cnt)
            # append result to an answers list, to be printed later
            ans.append(OC.calculate_occurances())
        for i in ans: print i
    except:
        raise
