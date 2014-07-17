"""
refer to lab@college/prolog/n_queens.pl 
for solutions to 8 queens.

This is one of the test cases mapped 
to check the visual interpretation.
"""

from numpy import array as ar

# declare empty array of 0's
c = ar([[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8,[0]*8])

P = [5, 2, 6, 1, 7, 4, 8, 3] # one of the 8 queens soln.

for i in xrange(8):
    # change 0->1 for depiction queen positions
    c[i][P[i]-1] = 1

print c
