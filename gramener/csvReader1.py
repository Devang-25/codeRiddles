import csv
import os
#import geonamescache
#gc = geonamescache.GeonamesCache()
a={}
val=[]
k=[]
#dt={'state':('year','number')}
#with open('Neo-Natal_Mortality_Rate.csv', 'rb') as myFile:
with open(raw_input('Enter .csv file name: '), 'r') as myFile:
#    reader = csv.reader(myFile, delimiter=',')
    for row in (list(csv.reader(myFile,delimiter=','))):
        print
#        print row[0] + '|' + row[1]
#+ '\t' + row[5] + ' \t' + row[6]+ ' \t' + row[7] + '\n'
#        a.append(row[1])
        a[row[1]]=row[2]

print
tempfile=open('data.txt','w+')
raw_input('Writing output in .js format to data.txt ...')
val=a.values()
k=a.keys()
tempfile.write("{\n\t")
for i in xrange(len(a)):
#    print k[i],val[i]    
    tempfile.write("'")
    tempfile.write(k[i])
    tempfile.write("'")
    tempfile.write(":")
    tempfile.write("\t")
    tempfile.write("")
    tempfile.write(val[i])
    tempfile.write("")
    if i<len(a)-1:
        tempfile.write(",")
    tempfile.write("\n\t")
tempfile.write("}\n")
tempfile.close()
#print "\n",a
