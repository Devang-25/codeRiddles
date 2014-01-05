def numDivisorSieve(a,b):
        divs = [1] * ((b-a) + 1)
        for i in xrange(a, b + 1):
            for j in xrange(1, b / i + 1):
                divs[i * j] += 1
        return divs

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
                final.append(divisorSieve(N,A))
                #    else:
                #        quit()
                #else:
                #    quit()
            for i in final: print i
    except:
        quit()
