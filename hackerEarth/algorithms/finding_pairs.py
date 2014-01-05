import sys
'''
def find_pair(N,A):
    c=N
    for i in xrange(N-1):
        j=i+1
        while j<N:
            c+=1 if A[i]==A[j] else 0
            j+=1
    
'''

def find_pair(N,A):
    c=N
    A_filtered = filter(lambda x: A.count(x)>1,A)
    for i in set(A_filtered):
        tmp = A_filtered.count(i) - 1 
        tmp = (tmp*(tmp+1))/2
        c += tmp
    return c
    
if __name__ == '__main__': 
    try:
        T = int(raw_input())
        if 1<=T<=10:
            pass
        else:
            quit()
        final = []
        for i in xrange(T):
            N = int(raw_input())
            A = raw_input().split()
            A = map(int, A)
            if len(A)==N:
                final.append(find_pair(N,A))    
            else:
                quit()                
        for i in final: print i

    except:
        print "Unexpected error:", sys.exc_info()[0]  
        raise
