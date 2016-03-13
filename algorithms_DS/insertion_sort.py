#!/usr/bin/env python3

def swap(x,y):
    return y,x

def insert_sort(a=[]):
    for i in range(1, len(a)):
        j = i
        while j>0 and a[j] < a[j-1]:
            print("before: i-%s j-%s a-%s" % (i, j, a))
            a[j], a[j-1] = swap(a[j], a[j-1])
            print("after : i-%s j-%s a-%s" % (i, j, a))
            j -= 1
    return a

def insert_sort_string(a=[]):
    a = list(a)
    for i in range(1, len(a)):
        j = i
        while j>0 and a[j] < a[j-1]:
            a[j], a[j-1] = swap(a[j], a[j-1])
            j -= 1
        print(''.join(a))
    return a

a = input("enter either int array (comma delimited) or a word as it is: ")
if ',' not in a:
    # process a string    
    print(insert_sort_string(a))
else:
    print(insert_sort([int(i) for i in a.split(',')]))
