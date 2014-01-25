def check(x):
    assert 2 <= x <= 10^18

def atoms(N,K,M):
    map(check, [N,K,M])
    assert N<=M    
    t = 0
    while N <= M:
        t+=1
        N *= K
    return t-1

if __name__ == '__main__':
    P = int(raw_input())
    assert 1 <= P <= 10**4 #test
    ans = []
    for i in xrange(P):
        ip = raw_input().split()
        assert len(ip)==3 #test
        ip = map(int, ip)
        ans.append(atoms(ip[0],ip[1],ip[2]))
    for i in ans: print i
