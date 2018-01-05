#!/usr/bin/python3

# Complete the function below.
import operator
from collections import defaultdict

def best_hotels():
    hotels = defaultdict(list)
    for i in range(int(input())):
        a,b = [int(i) for i in input().split()]
        hotels[a].append(b)
    print(hotels)
    hotels = {k:sum(v)/len(v) for (k,v) in hotels.items()}
    hotels = sorted(hotels.items(), key=operator.itemgetter(1), reverse=True)
    [print(i[0]) for i in hotels]

best_hotels()

'''
Input:

4
2000 10
1000 9
1000 8
2000 2

Output:
1000
2000
'''

