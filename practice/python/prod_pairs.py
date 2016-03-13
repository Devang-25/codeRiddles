from collections import defaultdict

N,K = [int(i) for i in raw_input().split()]
count = 0

tree = defaultdict(list)

for i in xrange(N-1):
    S,D = [int(j) for j in raw_input().split()]
    tree[S].append(D)


for k,v in tree.iteritems:
    if S*D <= K: count+=1

    print count
