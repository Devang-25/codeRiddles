from collections import Counter
a=[]
i=int(raw_input('No. of test cases? : '))
if(1<=i<=100):
    for k in xrange(i):
        a.append(raw_input("Enter test case %s: "% (k+1)))
        c=Counter(a[k].strip())
        print c

