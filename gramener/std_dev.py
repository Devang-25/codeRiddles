import csv,math
from collections import defaultdict
d = defaultdict(list)
rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
for i in xrange(len(rows)):
    d[rows[i].values()[2]].append(int(rows[i].values()[0]))
    
def SD(values, mean):
#    print "inside SD now....."
#    print "values= ",values,"mean= ", mean
    
    size = len(values)
    sum = 0.0
    for n in range(0, size):
        sum += ((values[n] - mean)**2)
#    print "outside SD...."
#    print
    return math.sqrt((1.0/(size-1))*(sum))
m=[]
for i in xrange(len(d)):
    x=d.values()[i]
#    print "d.values()[i] = ",d.values()[i]
    m.append(sum(x)/len(x)) #mean calculation
#    print "mean= ",m

#print m[0]+m[1]+m[2]
for i in xrange(len(d)):
    print d.keys()[i],int(SD(d.values()[i],m[i]))
#    print d.keys()[i]+","+str(numpy.median(d.values()[i]))
