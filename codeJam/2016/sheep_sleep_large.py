#!/usr/bin/env python3

# usage:
# $ ./sheep_sleep_large.py [input file]  > large_sheep_output
# check output of large_sheep_output

import sys

ALL = set('0123456789')

def check_insomnia(N):
    if N == 0: return True
    
def sleep_counter(N):
    c = 0
    s = set()
    while True:
        if s == ALL:
            break
        c+=1
        s.update(str(N*c))

    return N*c
    
if __name__ == '__main__':    
    f = open(sys.argv[1],'r')
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline().rstrip("\n"))
        assert 1 <= T <= 100
        A = []
        # for line in f:
        #     print(line.rstrip("\n"))
        for m in range(T):
            N = int(f.readline().rstrip("\n"))
            assert 0 <= N <= 10**6
            if check_insomnia(N):
                A.append("INSOMNIA")
            else:
                A.append(sleep_counter(N))
    for m,n in zip(range(1,T+1),A):
        print("Case #%d: %s" % (m,n))
