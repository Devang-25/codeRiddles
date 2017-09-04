#!/usr/bin/env python2
import json

try:
    file = open('lookup_factorials.json','r')
    lookup_dict = json.load(file)
    file.close()
except: 
    print 'file or json object not found'
    lookup_dict = {}

class fact_memoized:
    ''' use of memoization for a faster approach to factorials '''
    
    def __init__(self,lookup_dict):
        self.lookup_dict = lookup_dict

    def factorial(self, n):
        if n in [0,1,2]:
            return n
        else:
            return n * self.factorial(n-1)

if __name__ == '__main__':    
    n = int(raw_input('enter factorial input: '))
    if str(n) in lookup_dict.keys():
        print "dictionary looked up..", lookup_dict[str(n)]
        quit()
    #else carry on with factorial 
    fm = fact_memoized(lookup_dict)
    result = fm.factorial(n)
    lookup_dict[str(n)] = result #store new result
    print 'Result: ', result
    # write new dictionary to file
    file = open('lookup_factorials.json','w')
    file.write(json.dumps(lookup_dict))
    file.close()
