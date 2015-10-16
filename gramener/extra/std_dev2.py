import csv
from collections import defaultdict
d = defaultdict(list)
m=[]
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))
def std_dev(val, mean):
    import math
    size = len(val)
    sum = 0.0
    for k in xrange(size):
        sum += (val[k] - mean)**2
    return math.sqrt(sum/size) 
for i in xrange(len(d)):
    m.append(sum(d.values()[i])*1.0/len(d.values()[i]))
for i in xrange(len(d)):
    print d.keys()[i],int(std_dev(d.values()[i],m[i]))
