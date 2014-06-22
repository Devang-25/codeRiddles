import csv

with open('temperature.txt','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    print tsvin
