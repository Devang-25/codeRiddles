#!/usr/bin/env python2

# hack of sieve of eratosthenes
# not good for large numbers.

def get_primes_in_range(lower_limit, limit, old_primes_list):
    limitn = limit+1
    primes = dict()
    for i in range(lower_limit, limitn): primes[i] = True
    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False

    if lower_limit == 2:
        return [i for i in primes if primes[i]==True]
    
    for i in primes:
        if primes[i]:
            prime_factors = [p for p in old_primes_list if i%p == 0]
            for pf in prime_factors:
                factors = range(i, limitn, pf)
                factors = [f for f in factors if primes[f] == True]
                for f in factors:
                    primes[f] = False
                
    return [i for i in primes if primes[i]==True]

def generate_primes_upto(count):
    try:        
        _tmp = []
        start = 2
        upper_limit = count
        flag = False
        _set = False
        while not flag:
            _tmp.extend(get_primes_in_range(start, upper_limit, _tmp))
            if len(_tmp) < count:
                start = upper_limit + upper_limit%2
                upper_limit += (count - len(_tmp))*(count//len(_tmp))
            else:
                flag = True
        print(list(_tmp))
        return list(_tmp)[count-1], len(_tmp)
    except BaseException as e:
        print(e)

# test_cases = [6,10,10001]
test_cases = [6,10,180]
# test_cases = [1000000]
for n in test_cases:
    x, l = generate_primes_upto(n)
    print("%sth: -> %s | len of list-> %s" %
          (n, x, l))
