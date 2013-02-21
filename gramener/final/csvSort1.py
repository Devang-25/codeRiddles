import csv,operator,numpy
a={}

rows = sorted(csv.DictReader(open('salaries.csv','rb'), delimiter=','))
#rows = csv.DictReader(open('salaries.csv','rb'))
#,delimiter=',')
#, key=lambda d: d['Salary'])
#t=raw_input("Enter profession: (Lawyers,Plumbers,Doctors): ")

for i in xrange(len(rows)):
    if rows[i].values()[2]=='Doctors':
        a[rows[i].values()[1]]=int(rows[i].values()[0])

t=[item for item in reversed(sorted(a.iteritems(),key=operator.itemgetter(1)))]
for i in t:
    print i[0]+","+str(i[1])

'''
t = [i for i in sorted(a, key=lambda key:a[key], reverse=True)]
p=a.values()
p.sort()
p.reverse()
for i in xrange(len(a)):
    print t[i]+","+p[i]

'''
