import time
from random import randrange

def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        ismin = True
        for j in alist:
            if i>j:
                ismin = False
        if ismin:
            overallmin = i
    return overallmin

def findMin2(alist):
    minsofar = alist[0]
    for i in alist:
        ismin = True
        if i < minsofar:
            minsofar = i
    return minsofar

for listSize in range(1000, 10001, 1000):
    # findMin
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print findMin(alist)
    end = time.time()
    print "#1 - O(n^2) - size: %d time: %f" % (listSize, end-start)
    
    # findMin2
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print findMin2(alist)
    end = time.time()
    print "#2 O(n) - size: %d time: %f" % (listSize, end-start)
    
