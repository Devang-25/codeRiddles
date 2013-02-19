import csv,os
import itertools
#from collections import OrderedDict
#a={}
#with open('salaries.csv', 'r') as myFile:

reader = csv.DictReader(open('salaries.csv','rb')) 
rows = sorted(reader, key=lambda d: d['Salary'])

#for Salary in reader:
#    if Salary[1]=='Lawyers':
#        a[Salary[0]]=Salary[2]

#groups = itertools.groupby(rows, lambda d: d['Salary'])
    
#items = a.items()
#items.reverse()

print
for i in xrange(len(rows)):
    print rows[i],"\n" 
