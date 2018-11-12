#!/usr/bin/env python
import functools

from time import time

def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            print("cache miss: %s -- %.9f" % (key, time()))
            cache[key] = func(*args, **kwargs)
        else:
            print("cache hit: %s -- %.9f" % (key, time()))
        return cache[key]
    return memoized_func

@memoize
def fibonacci(n):
    if n == 0:return 0
    if n == 1:return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(1))

print(fibonacci(0))
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(1))
print(fibonacci(0))

# OUTPUT
###################################################################
# fibonacci(5) -> fibonacci(4) + fibonacci(3)
#              -> [fibonacci(3) + fibonacci(2)] + fibonacci(2) + fibonacci(1)
#              -> [[fibonacci(2) + fibonacci(1)] + fibonacci(1) + fibonacci(0)] + [fibonacci(1) + fibonacci(0)] + fibonacci(0)

# cache hit: (1,){} -> 1,1 (appeared once)
# cache hit: (2,){} -> 2
# cache hit: (3,){} -> 3
# 5 -> 5th term is (1,1,2,3,5)
###################################################################

# fibonacci(7) -> fibonacci(6)                 +      fibonacci(5)
#              -> fibonacci(5) + fibonacci(4)  +      fibonacci(5)

# cache hit: (5,){}
# cache hit: (4,){}
# cache hit: (5,){}
# 13

###################################################################
# cache hit: (5,){}
# 5

###################################################################
# cache hit: (7,){}
# 13

###################################################################
