final = []
T = int(raw_input())
for i in xrange(T):
    N,K = [int(x) for x in raw_input().split()]
    prefs = []
    for j in xrange(N):
        ip = raw_input()
        prefs.append(int(ip.lstrip('0')))

    s = str(sum(prefs))
    occs = s.count(str(N))
    final.append(N-occs)
    
for i in xrange(len(final)):
    print final[i]
