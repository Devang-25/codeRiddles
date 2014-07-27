T = int(raw_input())
ans=[]
def delete(popularity):
    for i in xrange(len(popularity)-1):
        if popularity[i] <= popularity[i+1]:
            popularity.pop(i)
            return popularity
    return popularity[:-1]

if __name__=='__main__':
    for i in xrange(T):
        N,K = [int(i) for i in raw_input().split()]
        popularity = [int(i) for i in raw_input().split()]
        for i in xrange(K):
            popularity = delete(popularity)
        ans.append(popularity)
    for i in ans:
        #print ' '.join(map(str, i))
        print ' '.join([str(j) for j in i])
