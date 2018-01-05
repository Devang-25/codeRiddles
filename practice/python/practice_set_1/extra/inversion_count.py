#!/bin/env python3

# https://www.geeksforgeeks.org/counting-inversions/

def count_inversions(arr):
    count = 0
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                # print(arr[i], arr[j])
                count += 1
    return count

arr = [2,4,1,3,5]
print(arr)
print(count_inversions(arr))

arr = [1, 20, 6, 4, 5, 11, 34, 5, 3]
print(arr)
print(count_inversions(arr))
