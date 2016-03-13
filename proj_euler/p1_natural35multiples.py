#!/usr/bin/env python2
g = (lambda x: x%3==0 or x%5==0)
t=0
for i in xrange(1,1000):
    if(g(i)):
        t+=i
    # print i,t

print t
