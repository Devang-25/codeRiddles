#!/usr/bin/python3

# http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html
# https://brilliant.org/wiki/median-finding-algorithm/
# http://austinrochford.com/posts/2013-10-28-median-of-medians.html

import random
from time import time


_dbg = True
# run custom sort, not python's sort
_custom_sort = True
_benchmark = True
SIZE_LIMIT = 500


def median_of_medians(ulist, i, local_debug=False):
    # swap low <-> high for kth largest element. Reverses the order.
    # or this could also be achieved by changing the input like this:
    # - i'th largest => len(A) - i - 1 (this finds Nth smallest which is also i'th largest)
    # conversely, for largest, call median_of_medians(A, len(A)-1)
    chunked_lists = [ulist[j:j+5] for j in range(0, len(ulist), 5)]
    # each sorted() is O(n) on small sized lists.
    # Total = x * N where x is # of sublists of length 5 each
    medians = [sorted(sublist)[len(sublist)//2] for sublist in chunked_lists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = median_of_medians(medians, len(medians)//2)

    low = [j for j in ulist if j < pivot] # for largest, this is high[] now
    high = [j for j in ulist if j > pivot]

    if local_debug:
        print(chunked_lists)
        print("\t MEDIANS: ", medians)
        print("\t PIVOT: ", pivot)
        print("\t LOW: ", low)
        print("\t HIGH: ", high, end="\n\n")
    
    k = len(low)
    # make appropriate changes here for kth largest, if required
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else:
        # pivot = k
        # k == i
        return pivot    

def benchmark(unsorted_list, custom=False):
    start = time()
    k = SIZE_LIMIT // 4 #find 12th smallest
    print("\nBenchmark results for list of size %s" % SIZE_LIMIT)
    print("..for ix positon %s [kth smallest element]:" % k)
    
    for i in range(10000):
        ismallest = median_of_medians(unsorted_list, k)
    end = time()
    print("MoM time: %s", end - start)
    
    start = time()
    for i in range(10000):
        ismallest = sorted(unsorted_list)[k]
    end = time()
    print("sorted() time: %s", end - start)

    
if __name__ == '__main__':
    # def chunks(l, n):
    #     """Yield successive n-sized chunks from l."""
    #     for i in range(0, len(l), n):
    #         yield l[i:i+n]

    # # divide list into subsets of ~5
    # chunked_list = list(chunks(ulist, 5))

    # i represents the ith smallest element
    unsorted_list = [28, 6, 1, 11, 17, 26, 2,  25, 24, 0, 19, 27, 9, 5, 10, 8]
    i = 5
    answer = 8

    if _custom_sort:
        ismallest = median_of_medians(unsorted_list, i, local_debug=_dbg)
    else:
        ismallest = sorted(unsorted_list)[i]

    assert ismallest == answer

    if _dbg:
        print("UNSORTED: ", unsorted_list, end="\n\n")
        print("ACTUAL SORTED LIST: ", sorted(unsorted_list))
        print("i = %d; ith smallest element: %s" % \
              (i, ismallest))
    
    if _benchmark:
        # unsorted_list = random.sample(range(random.randint(SIZE_LIMIT//2,SIZE_LIMIT)),
        #                               (random.randint(0,SIZE_LIMIT//2)))
        sample_range = range(random.randint(SIZE_LIMIT, SIZE_LIMIT + 1000))
        unsorted_list = random.sample(sample_range, SIZE_LIMIT)
        benchmark(unsorted_list)        
