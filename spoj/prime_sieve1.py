def primes_sieve1(m,limit):
    limitn = limit+1
    primes = dict()
    for i in range(m, limitn): primes[i] = True
    
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
p=[]
t=int(raw_input())
if(t<=10):
    for j in range(t):
        m,n=raw_input().split()
        if m>=1 and n >=m and n<=1000000000 and n-m<=100000:
            p.append(primes_sieve1(m,n)) 


        
