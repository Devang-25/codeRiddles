def prime_factors(n):
    "Returns all the prime factors of a positive integer"
    factors = []
    d = 2
    while (n > 1):
        while (n%d==0):
            n/=d
            if d not in factors:
                factors.append(d)
        d = d + 1
    return factors[-1]
print prime_factors(600851475143) # The largest (last) element in the prime factor array
