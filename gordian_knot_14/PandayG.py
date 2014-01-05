import sys

MIN_INT = -sys.maxint - 1

def lexicographic_order_generation(A):
    A[0:0] = [MIN_INT]
    A.sort()
    n = len(A) - 1
    count = 0
    while True:
        #print("".join([str(x) for x in A[1:]]))
        count+=1
        j = n - 1
        while A[j] >= A[j + 1]:
            j -= 1
        if j == 0:
            return count
        l = n
        while A[j] >= A[l]:
            l -= 1
        A[j], A[l] = A[l], A[j]
        suffix = A[j+1:]
        suffix.reverse()
        A = A[:(j + 1)] + suffix

c=0
for i in xrange(1,8):
    ip = '5'*i + '7'*(15-i)
    c+=lexicographic_order_generation(list(ip))

print c, ".. for 7 5's and 8 7's (Since total length is threshold value: 15)"
print "Total comes when this answer is doubled. (for 7 '7' and 8 5's)"
print "Answer= ",c*2
