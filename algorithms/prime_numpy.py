#!/usr/bin/env python2
import math
import numpy
def prime6(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)

x = prime6(int(raw_input("Enter upper range: ")))
for i in x: print i
