def is_prime(n):
    import math
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
print is_prime(4)
