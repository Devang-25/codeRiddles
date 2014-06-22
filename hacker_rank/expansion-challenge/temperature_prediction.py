'''
Find missing temperature values
===============================
libraries enabled: numpy, scipy, sklearn, nltk
testcases/minima.txt
'''

import sys
from numpy import array #, hstack
from sklearn.preprocessing import Imputer
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.pipeline import Pipeline
# from sklearn.cross_validation import cross_val_score

class PredictTemp:    
    ''' 
    Apply AND operator on subsets with given conditions 
    '''

    def __init__(self, size, ip):
        self.N = size
        # self.data = array(ip, \
        #                   dtype=[(heads[0],'int'), \
        #                          (heads[1],'|S10'), \
        #                          (heads[2], 'float'), \
        #                          (heads[3], 'float')
        #                      ])
        self.data = array(ip)
        #print self.data[:,[2,3]]
        #print self.data
        
    def predict_already(self):
        return Imputer(self.data[:,[2,3]])
        
if __name__ == '__main__':
    N = int(raw_input())
    assert 1<=N<=1500
    raw_input()
    ans = []
    ip = []
    for i in xrange(N):
        temp = raw_input().split()        
        assert len(temp) == 4
        if 'Missing' in temp[2]:
            temp[2] = "NaN"
            assert -75<=float(temp[3])<=75
        elif 'Missing' in temp[3]:
            temp[3] = "NaN"
            assert -75<=float(temp[2])<=75
        else:
            assert -75<=float(temp[2])<=75 and -75<=float(temp[3])<=75    
        assert 1908<=int(temp[0])<=2013
        temp[0] = int(temp[0])
        ip.append(temp)
    PT = PredictTemp(N, ip)
    ans.append(PT.predict_already())
    for i in ans: print i
