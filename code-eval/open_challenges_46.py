import fileinput
import sys
import math

def gen_primes(limit):
    assert limit < 4294967295
    primeList = []
    primeList.append(2)
    for n in range(1, limit, 2):
        if getIfPrime(n):
            primeList.append(n)
    return ','.join(map(str, primeList)) 

def getIfPrime(n):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2:
        return True
    m = int(math.sqrt(n))
    for i in range(3, m + 1, 2):
        if n % i == 0:
            return False
    return True

# def gen_primes(limit):
#     assert limit < 4294967295
#     primes = range(2, limit)
#     for i in primes:
#         factors = range(i, limit, i)
# 	for f in factors[1:]:
# 		try:
# 	                primes.remove(f)
# 		except:
# 			continue
#     return primes


if __name__ == '__main__':
    # ANS = []
    for line in fileinput.input():
        print(gen_primes(int(line)))
    #     ANS.append(gen_primes(int(line)))
    # for j in ANS: print ','.join(map(str, j))
        # for k in xrange(len(j)-1):
        #     sys.stdout.write('%.0f,'%j[k])
        # sys.stdout.write('%.0f'%j[len(j)-1])
        # print
    # For Benchmarking..
    # import timeit
    # for i in xrange(2,20):
    #     print(timeit.timeit("gen_primes("+str(i)+")", 
    #         setup="from __main__ import gen_primes"))
