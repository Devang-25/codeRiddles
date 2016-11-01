import csv

lines_limit = 10

f = open('train.csv','r')
a = csv.DictReader(f)
for line in a:
    if a.line_num < lines_limit:
        print(line)
    else:
        print("breaking off at line:%d"
              % lines_limit)
        break
    
# dont use pandas
# pd loads in memory with
# x = pandas.read_csv('train.csv')   
