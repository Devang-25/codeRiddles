#!/bin/env python3

def transform(X, N):
    """
    returns one of:
    - 4x + 1 
    - 5x + 1

    ..depending on value of N
    """
    return N*X + 1

def execute(A, B):
    list_1 = [A]
    # iter w/ 4
    while list_1[-1] < B:
        X = list_1[-1]
        T = transform(X, 4)
        if T < B:
            list_1.append(T)
        else:
            break
            
    list_2 = [A] 
    # iter w/ 5
    while list_2[-1] < B:
        X = list_2[-1]
        T = transform(X, 5)
        if T < B:
            list_2.append(T)
        else:
            break

    list_1.pop(0)
    list_2.pop(0)
    
    print(list_1)
    print(list_2)

memo = []
    
def getMaxSteps(n, T):
    if n == T: return 0
    if memo[-1] == 26: return n
    if memo[-1] > 26: return 0
    r = getMaxSteps(4*n + 1, T)
    # print(r)
    r = max(r, getMaxSteps(5*n + 1, T))
    # print(r)
    memo.appen(r)
    return r

if __name__ == '__main__':
    begin = int(input("#1: "))
    end = int(input("#2: "))
    execute(begin, end)
    memo.append(begin)
    # print(getMaxSteps(begin, end))
    print(memo)
