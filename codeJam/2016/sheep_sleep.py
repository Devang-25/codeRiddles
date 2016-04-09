#!/usr/bin/env python3

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
    T = int(input())
    assert 1 <= T <= 100
    A = []
    for m in range(T):
        N = int(input())
        assert 0 <= N <= 200
        if check_insomnia(N):
            A.append("INSOMNIA")
        else:
            A.append(sleep_counter(N))
    for m,n in zip(range(1,T+1),A):
        print("Case #%d: %s" % (m,n))
