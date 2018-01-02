#!/usr/bin/python3

# https://stackoverflow.com/questions/2087469/sort-a-file-with-huge-volume-of-data-given-memory-constraint
# https://en.wikipedia.org/wiki/Merge_algorithm#K-way_merging

from glob import glob
from collections import Counter
from itertools import islice
from functools import reduce

# def parallel_merge(A,B,C=[]):
#     m = len(A) - 1
#     n = len(B) - 1
#     p = len(C)
    
#     if m < n:
#         A,B = B,A
#         m,n = n,m
        
#     if m <= 0:
#         return

#     r = (i + j) // 2
#     s = binary_search(A[r], B)
#     t = p + (r - i) + (s - k)

# https://stackoverflow.com/questions/29712445/what-is-the-use-of-buffering-in-pythons-built-in-open-function
# TODO: write a file size splitter function in python instead of using shell script 

def buffer_refresh(T=[], chunks=None):
    if not T:
        T = { k:v.readline() for (k,v) in chunks.items() }
    total = len(T)
    empty = 0
    for f in T:
        if not T[f]:
            T[f] = chunks[f].readline()
            if not T[f]:
                empty+=1
    if empty == total:
        return False
    
    return {k:v for (k,v) in T.items() if bool(v)}

def merge_chunks(final, chunks):
    # read files N lines at a time
    # N = 10
    # T = [islice(f, N) for f in chunks]
    # T = {f:f.readline() for f in chunks}
    age_col = lambda x: int(x[1].split(',')[1])
    T = []
    while True:
        T = buffer_refresh(T, chunks)
        # print(T)
        # T = [i.split(',')[1] for i in T]
        if not T:
            break
        age_asc = sorted(T.items(), key=age_col)
        # extract smallest
        smallest = age_asc[0][1]
        # update input buffer for replacement of that value 
        T[age_asc[0][0]] = ''
        final.write(smallest)


if __name__ == '__main__':
    # read 1M of data
    # f.readlines(1024**2)
    # T = [islice(f, N) for f in chunks]
    chunk_size = (1024**2)//2 # // 2 => 0.5MB => 512KB  
    # open all chunked files
    chunks = {f:open(f, 'r', chunk_size) for f in glob('data/age_chunked*')}
    final = open('data/age_sorted_large.txt', 'w')
    merge_chunks(final, chunks)
    # smallest = None
    # while True:
    #     T = [f.readlines(chunk_size) for f in chunks]
    #     if not reduce(lambda x,y: bool(x) & bool(y), T):
    #         break
    #     else:
    #         reduce(lambda x,y: parallel_merge(x,y))
            
    # close all open files
    final.close()
    [f.close() for f in chunks.values()]
