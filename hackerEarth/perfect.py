'''
n = 1
while True:
    factors = [1]
    [factors.append(i) for i in range(2,n+1) if n%i == 0]
    if sum(factors) == 2*n: print n
    n += 1
'''

#l = [x for x in xrange(1,10001) if sum(y for y in xrange(1,x) if x%y==0)==x]

def perf(n):
    sum = 0
    for i in xrange(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print perf(int(raw_input()))
