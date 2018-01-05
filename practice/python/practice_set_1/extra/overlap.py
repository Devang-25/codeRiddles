#!/usr/bin/python3

# Complete the function below.
import operator

def merge_overlapping_intervals():
    arr = []
    stack = []
    for i in range(int(input())):
        arr.append([int(i) for i in input().split()])
    arr = sorted(arr, key=operator.itemgetter(0))
    stack.append(arr[0])
    # dump = []
    for cur in arr[1:]:
        if cur[0] <= stack[-1][1]:
            # dump.append(cur[0])
            stack[-1][1] = cur[1]
        else:
            stack.append(cur)
    # [print(i) for i in dump]
    print(len(stack))
    for cur in stack:
        print(' '.join([str(i) for i in cur]))
    #print(stack)
    

merge_overlapping_intervals()

'''
Input:
4
0 1
2 4
4 5
6 7

Output:
3
0 1
2 5
6 7

'''
