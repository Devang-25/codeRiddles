'''
Find missing temperature values
===============================
libraries enabled: numpy, scipy, sklearn, nltk

copy-paste text from ./testcases/temperature.txt
'''

import sys
import numpy as np
from sklearn.preprocessing import Imputer
import pandas as pd
#from pandas import DataFrame
from matplotlib.pylab import poly1d, polyfit
from matplotlib import pyplot as plt

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.pipeline import Pipeline
# from sklearn.cross_validation import cross_val_score

class PredictTemp:    
    ''' 
    Apply AND operator on subsets with given conditions 
    '''

    def __init__(self, size, ip):
        self.N = size
        # # self.data = np.array(ip, \
        # #                   dtype=[(heads[0],'int'), \
        # #                          (heads[1],'|S10'), \
        # #                          (heads[2], 'float'), \
        # #                          (heads[3], 'float')
        # #                      ])
        # self.data = np.array(ip)
        # self.data_std = np.isnan(self.data[:,[2,3]].astype(np.float,
        #                                                    copy=False))
        self.df = pd.DataFrame(ip, 
                               columns=['year','month','tmax','tmin'], 
                               dtype=float)
        self.null_refined = pd.notnull(self.df[[2,3]])

    def plot_regression(self):
        # sample plot of points
        x = self.NaN_filtered['tmax']
        y = self.NaN_filtered['tmin']
        fit = polyfit(x,y,1)
        fit_fn = poly1d(fit)
        # takes in x and returns an estimate for y
        plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
        plt.title("Temperature pattern regression plot")
        plt.xlabel("tmax")
        plt.ylabel("tmin")
        plt.show()        
        
    def predict_already(self):
        # tmax_true = self.df['tmax'][np.isfinite(self.df['tmax'])
        self.NaN_filtered = self.df[self.null_refined['tmax']]\
                       [self.null_refined['tmin']]

        self.plot_regression()
        return Imputer(self.NaN_filtered[[2,3]])
        
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
            temp[2] = np.NAN
            assert -75<=float(temp[3])<=75
        elif 'Missing' in temp[3]:
            temp[3] = np.NAN
            assert -75<=float(temp[2])<=75
        else:
            assert -75<=float(temp[2])<=75 and -75<=float(temp[3])<=75    
        assert 1908<=int(temp[0])<=2013
        temp[0] = int(temp[0])
        ip.append(temp)
    PT = PredictTemp(N, ip)
    ans.append(PT.predict_already())
    for i in ans: print i

## Optionally, take multiple line inputs with this 
## (but it only ends depending on sentinel)
# sentinel = '' # ends when this string is seen
# for line in iter(raw_input, sentinel):
#     pass # do things here
