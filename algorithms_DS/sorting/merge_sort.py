#!/usr/bin/env python2

# def merge_improper_method(a, i = 0, j = 0, l = []):
#     print "splitting input into 2 arrays for sake of merge sort"
#     l1 = sorted(a[:len(a)/2])
#     l2 = sorted(a[len(a)/2:])
#     print "l1 = %s \nl2 = %s" % (l1, l2)
#     for k in xrange(len(a)):
#         print "l: %s" % l
#         # check for list out of range
#         if  i == len(l1):
#             l.extend(l2[j:]); return l
#         elif  j == len(l2):
#             l.extend(l1[i:]); return l
#         # compare
#         if l1[i] < l2[j]:
#             l.append(l1[i])
#             i+=1
#         elif l2[j] < l1[i]:
#             l.append(l2[j])
#             j+=1
#         elif l1[i]==l2[j]:
#             l.append(l1[i])
#             l.append(l2[j])
#             i+= 1; j+= 1
#     # return final list
#     return l

def merge_sort(L):
    s = len(L)
    print("splitting %s" % L)
    if s > 1:
        left_arr = L[:s//2]
        right_arr = L[s//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                L[k] = left_arr[i]
                i+=1
            else:
                L[k] = right_arr[j]
                j+=1
            k+=1
        while i < len(left_arr):
            L[k] = left_arr[i]
            i+=1; k+=1
        while j < len(right_arr):
            L[k] = right_arr[j]
            j+=1; k+=1        
            
    print("merging %s" % L)
    return L
    
X = raw_input("Enter space separated list of integers: ").split()
print "\nanswer: %s" % merge_sort(map(int, X))
