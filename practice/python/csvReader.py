import csv

x = ['543', '674', '345', '547', 'a']
y = ['a', '1:543', '2:674', '3:345', '4:547']
print x,y
raw_input()
reader = csv.reader(x, delimiter=',', quotechar='|')
for row in reader:
    print row[4] + ' 1:' + row[0] + ' 2:' + row[1] + ' 3:' + row[2] + ' 4:' + row[3]
