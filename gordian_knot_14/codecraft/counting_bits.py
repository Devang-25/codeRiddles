##########
"""
Given N, if we write all numbers from 1 to N (both inclusive) in binary,
what is the count of 1s I have written.

For example, if N=3,
I will write down:
1
10
11
Therefore, a total of 4 ones.
"""
#########

def count_bits(N):
    assert 1 <= N <= 1000
    l = ''
    for i in xrange(1,N+1):
        l += bin(i).lstrip('0b')
    return l.count('1')

if __name__ == '__main__': 
    T = int(raw_input())
    assert 1 <= T <= 1000
    ans = []
    try:
        for i in xrange(T): ans.append(count_bits(int(raw_input())))
    except:
        quit()
    for i in xrange(T): print ans[i]

# another version: 
"""
    z = lambda x: bin(x).lstrip('0b')
    return ''.join( map(z, xrange(1,N+1)) ).count('1')
"""
