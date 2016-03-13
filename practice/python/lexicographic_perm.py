import sys

MIN_INT = -sys.maxint - 1
def lexicographic_order_generation(A):
    A[0:0] = [MIN_INT]
    A.sort()
    n = len(A) - 1
    while True:
        print("".join([str(x) for x in A[1:]]))
        j = n - 1
        while A[j] >= A[j + 1]:
            j -= 1
        if j == 0:
            return
        l = n
        while A[j] >= A[l]:
            l -= 1
        A[j], A[l] = A[l], A[j]
        suffix = A[j+1:]
        suffix.reverse()
        A = A[:(j + 1)] + suffix

'''
A = [1, 2, 3]
lexicographic_order_generation(A)
A = list("AABAAC")
lexicographic_order_generation(A)
'''

lexicographic_order_generation(list(raw_input()))
