import csv
with open('test.csv', 'rb') as myFile:
    reader = csv.reader(myFile, delimiter=',', quotechar='|')
    for row in reader:
            print row[4] + ' 1:' + row[0] + ' 2:' + row[1] + ' 3:' + row[2] + ' 4:' + row[3]
