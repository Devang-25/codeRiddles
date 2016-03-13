#!/usr/bin/env python2
flag=1
p=a=2
tmp=0
while 1:
    for i in xrange(1,a):
        if(a %i==0 and i!=1):
            break
        elif i==a-1:
            p=a
        else:
            continue
    
    if(tmp!=p):
        print p
        tmp=p
    a+=1
    flag+=1
    if flag%3000==0:
        break
