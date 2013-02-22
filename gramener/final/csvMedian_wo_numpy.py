import csv
from collections import defaultdict
d = defaultdict(list)
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))

for i in xrange(len(d)):
    d.items()[i][1].sort()
    x=d.items()[i][1]
    if len(x)%2==0:
        t=len(x)/2
        m= (x[t-1]+x[t])/2
    else:
        m= x[len(x)/2]
    print d.keys()[i],m

#Here, when i used numpy, it showed no module named numpy, so i did manual
#math otherwise after building dictionary with collections.defaultdict, i would rather:
#for i in xrange(len(d)):
#    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
