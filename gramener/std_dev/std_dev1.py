import csv,math
from collections import defaultdict
d = defaultdict(list)
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))
def std_dev(val, mean):
    size = len(val)
#    print size, val
    sum = 0.0
    for k in xrange(size):
        sum += (val[k] - mean)**2
    return math.sqrt(sum/size)
m=[]
for i in xrange(len(d)):
    m.append(sum(d.values()[i])*1.0/len(d.values()[i])) #mean calculation
#print m
for i in xrange(len(d)):
    print d.keys()[i],int(std_dev(d.values()[i],m[i]))

'''
val=[2,4,4,4,5,5,7,9]
mean=5
print std_dev(val,mean)
'''
