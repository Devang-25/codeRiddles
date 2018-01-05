#!/bin/env python3

# geeks for geeks


arr = [2, 5, 2, 8, 5, 6, 8, 8]

# SET 1
def sort_by_freq(arr):
    arr.sort() # step 1
    tmp = 0
    freq = [[0, 1]]
    
    for i in range(len(arr)-1): # step 2
        if arr[i] == arr[tmp]:
            freq[-1][1] += 1
        else:
            freq.append([i,1])
            tmp = i
    print(freq)

    tmp = freq[0][1]
    highest = []
    for l in freq:
        if l[1]>=

# SET 2 - use dict

# SET 3 - using hashmap / treemap
sort_by_freq(arr)
