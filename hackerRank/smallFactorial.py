import sys 
t=int(raw_input())
if 1<=t<=100:
    k=[]
    e=[]
    for i in xrange(t):
        a=1
        n=int(raw_input())
        if 1<=n<=100:
            k.append(n)
            while k[i]>0:
                a=a*k[i]
                k[i]=k[i]-1
            e.append(a)
        else:
            sys.exit(0)
    for i in xrange(t):
        print e[i]
