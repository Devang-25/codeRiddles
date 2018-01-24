from itertools import combinations

def findMinXor(A):
    min_pair = [None,None,None]
    for i, j in combinations(A, 2):
        tmp = i ^ j
        if not min_pair[0]:
            min_pair = [tmp, i, j]
            continue
        if tmp < min_pair[0]:
            min_pair = [tmp, i, j]

    # use .format for printing a list
    _op = "{} ({} XOR {})"
    return _op.format(*min_pair)

print(findMinXor([0,4,7,9]))
