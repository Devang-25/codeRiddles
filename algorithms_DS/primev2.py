#!/usr/bin/env python2
#def isprime(startnumber):

def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        print int(startnumber**0.5)+1,"\n"
        print divisor
        if startnumber/divisor==int(startnumber/divisor):
            return False
        else:
            return True
print isprime(int(raw_input()))
