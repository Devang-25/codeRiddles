'''
Find missing temperature values
===============================
libraries enabled for expansion challenge: numpy, scipy, sklearn, nltk, pandas
'''

import sys
import numpy as np
from sklearn.preprocessing import Imputer
import pandas as pd
from matplotlib.pylab import poly1d, polyfit
from matplotlib import pyplot as plt
from pandas.tools.plotting import andrews_curves
        
class PredictTemp:    
    ''' 
    Apply AND operator on subsets with given conditions 
    '''

    def __init__(self, size, df_orig):
        self.N = size
        self.df = df_orig
        #self.null_refined = pd.notnull(self.df[[2,3]])

    def plot_regression(self):
        # sample plot of points
        x = self.filtered.tmax
        y = self.filtered.tmin
        fit = polyfit(x,y,1)
        fit_fn = poly1d(fit)
        # takes in x and returns an estimate for y
        # fig 1
        plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
        plt.title("Temperature pattern regression plot")
        plt.xlabel("tmax")
        plt.ylabel("tmin")
        # fig 2
        plt.figure()
        andrews_curves(self.filtered[[2,3]], 'tmin')
        plt.title("Andrews curve plot for tmin")
        plt.show()
        # fig 3
        plt.figure()
        self.df[[2,3]].boxplot()
        # fig 4
        self.filtered.plot()
        plt.show()
        
    def predict_already(self):
        print "Mean values:\n%s" % (self.df.mean())
        self.filtered = self.df\
                        [np.isfinite(self.df.tmax)]\
                        [np.isfinite(self.df.tmin)]
        self.plot_regression()


if __name__ == '__main__':    
    with open('testcases/temperature.txt') as f:
        content = f.read().split('\n')
        while '' in content: 
            content.remove('') # remove all empty line entries
    N = content.pop(0) # number of input lines
    df = pd.DataFrame(columns=content.pop(0).split(), 
                      dtype=float) # input with headers
    for index, line in enumerate(content):
        temp = line.split() # for space separated entries
        assert len(temp) == 4 # check list length
        df.loc[index] = temp
    form = lambda df: df.str.replace('([a-zA-Z]+_\d)', 'NaN').astype(float)
    df = df[[0,1]].join(form(df.tmax)).join(form(df.tmin))
    PT = PredictTemp(N, df)
    PT.predict_already()
