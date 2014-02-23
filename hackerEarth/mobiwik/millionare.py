if __name__ == '__main__': 
    T = int(raw_input())
    assert 1<=T<=1000
    ans = []
    for i in xrange(T):
        N = int(raw_input())
        assert 3<=N<=1000
        ans.append('%.6f'%float(float(N-1)/N))
    for i in ans: print i
