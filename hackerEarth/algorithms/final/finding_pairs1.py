def find_pair(N,A):
    c=N
    A_grp = [A.count(i) for i in set(A)]
    while 1 in A_grp:
        A_grp.remove(1)
    for i in A_grp:
        c += ((i-1)*i)/2
    return c
    
if __name__ == '__main__': 
    try:
        T = int(raw_input())
        final = []
        if 1 <= T <= 10:
            for i in xrange(T):
                N = int(raw_input())
                #if 1 <= N <= 10**6:
                A = raw_input().split()
                A = map(int, A)
                #if (-10**6 <= min(A)) and (max(A) <= 10^6):
                final.append(find_pair(N,A))
                #    else:
                #        quit()
                #else:
                #    quit()
            for i in final: print i
    except:
        quit()
