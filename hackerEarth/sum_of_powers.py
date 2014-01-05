from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
'''
def check_sop(ip_int):
    if 1<=ip_int<=1000000:
        pass
    else:
        quit()

    if ((max(range_check)< 123) and (min(range_check)>=97)):
        if (len(range_check)==26):
            return 'YES'
        else:
            return 'NO'
    else:
        quit()
'''
def check(n):
    for b in xrange(1,int(log(n)+1)):
        if b>=2:
            for a in xrange(1,n/2):
                if pow(a,b)==n:
                    print a,b
                    return a,b
        else:
            pass

try:
    T = int(raw_input())
    if 1<=N<=1000:        
        check = []
        for i in xrange(T):
            check.append(check_sop(int(raw_input())))
        for i in xrange(T):
            print check[i]
    else:
        quit()
except:
    quit()
