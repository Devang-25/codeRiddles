import csv,numpy
from collections import defaultdict
d = defaultdict(list)
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))
#for i in xrange(len(d)):
#    d.items()[i][1].sort()
for i in xrange(len(d)):
    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
