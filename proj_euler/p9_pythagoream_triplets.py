#!/bin/env python

# real	0m0.102s
# user	0m0.096s
# sys	0m0.006s

# for a in range(1, 1000):
#     for b in range(a, 1000):
#         c = 1000 - a - b
#         if c*c == a*a + b*b:
#             print(a,b,c)
#             print(a*a, b*b, c*c)
#             print(a*b*c)
#             break


#########################################
# real	0m0.041s
# user	0m0.035s
# sys	0m0.006s

for a in range(1, 500):
    for b in range(a, 500):
        c = 1000 - a - b
        if c*c == a*a + b*b:
            print(a,b,c)
            print(a*a, b*b, c*c)
            print(a*b*c)
            break

#########################################
# A third way is to filter by rules. Consult wikipedia
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

# below is a failed attempt. Need to optimize. And check whether it would
# be a primitive or a derivative.

# primite pythagorean triplets:
# Exactly one of a, b is odd; c is odd.[11]
# Exactly one of a, b is divisible by 3.
# Exactly one of a, b is divisible by 4
# Exactly one of a, b, c is divisible by 5
# The largest number that always divides abc is 60
# c is of the form 4n + 1.
# The area (K = ab/2) is a congruent number[14] divisible by 6.
# At most one of a, b, c is a square.
####################################################################

# a_sets = []
# b_sets = []
# c_sets = []

# for i in range(1,32):
#    if (i%4==0 or i%3==0):
#        a_sets.append(i)
       
#    if (i%3==0 and i%2==1):
#        b_sets.append(i)
    
#    if i%2==1 and i>1:
#        c_sets.append(i)


# print(a_sets)
# print(b_sets)
# print(c_sets)

# print(set(a_sets) ^ set(b_sets) ^ set(c_sets))
# possible_pairs = []
