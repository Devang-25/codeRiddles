#!/bin/env python3

# Let (x,y) be the coordinate of a student’s house on a 2-D plane.
# There are 2N students and we want to pair them into N groups.
# Let d_i be the distance between the houses of 2 students in group i.
# Form N groups such that [i=1 to N] sum(d_i) is minimized.

# Constraints: N ≤ 8; 0 ≤ x, y ≤ 1000.


def read_data(fpath='case_10911_UVaOJ.txt'):
    f = open(fpath,'r')
    In = f.read().splitlines()
    f.close()
    In = [[int(j) for j in i.split()] for i in In]
    return In

def check_constraints(In):
    for x,y in In:
        assert 0 <= x <= 1000
        assert 0 <= y <= 1000

    N = len(In)/2
    assert (N <= 8) and (N%2==0)

    return N

def pair_groups(data, N):
    pass


if __name__ == "__main__":
    data = read_data()
    N = check_constraints(data)
    
    pairs = pair_groups(data, N)
    for i in range(len(pairs)):
        print("Pair #%s --> (%s,%s) with distance: %s" % \
              (i, pairs))
