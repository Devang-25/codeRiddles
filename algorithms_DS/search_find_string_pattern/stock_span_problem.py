#!/usr/bin/python3

# https://www.geeksforgeeks.org/the-stock-span-problem/

_dbg = True

def spanner(price, S={}):
    stack = [0]
    S[0] = 1
    if _dbg:
        print("price: %s -- stack: %s" % (price[0], stack))
        print("stack now: %s -- S[%s] => %s" % (stack, 0, S[0]))
    for i in range(1,len(price)):
        if _dbg:
            print('-'*10)
            print("price: %s -- stack: %s" % (price[i], stack))
        while bool(stack) and price[stack[-1]] <= price[i]:
            if _dbg:
                print("price[i] >= stack[-1]")
            stack.pop()
        S[i] = i + 1 if not bool(stack) else (i - stack[-1]) # i+1 coz 0 ix'ed
        # funda is: if stack is not empty, deduct all but 
        if _dbg:
            print("stack now: %s -- S[%s] => %s" % (stack, i, S[i]))
        stack.append(i)
    return S


if __name__ == '__main__':
    # prices = {60, 70, 75, 80, 85, 100}
    prices = [1000, 4, 5, 90, 120, 80]
    S = spanner(dict(enumerate(prices)))
    assert list(S.values()) == [1, 1, 2, 3, 4, 1]
    if _dbg:
        print("="*10)
        print("Prices: ", prices)
        # output should be 1 1 2 4 5 1
        print("Stock Span: ", list(S.values()))

    if not _dbg:
        # just test 1 more case
        prices = [10, 4, 5, 90, 120, 80]
        S = spanner(dict(enumerate(prices)))
        assert list(S.values()) == [1, 1, 2, 4, 5, 1]


####################################
# price: 1000 -- stack: [0]
# stack now: [0] -- S[0] => 1
# ----------
# price: 4 -- stack: [0]
# stack now: [0] -- S[1] => 1
# ----------
# price: 5 -- stack: [0, 1]
# price[i] >= stack[-1]
# stack now: [0] -- S[2] => 2
# ----------
# price: 90 -- stack: [0, 2]
# price[i] >= stack[-1]
# stack now: [0] -- S[3] => 3
# ----------
# price: 120 -- stack: [0, 3]
# price[i] >= stack[-1]
# stack now: [0] -- S[4] => 4
# ----------
# price: 80 -- stack: [0, 4]
# stack now: [0, 4] -- S[5] => 1
# ==========
# Prices:  [1000, 4, 5, 90, 120, 80]
# Stock Span:  [1, 1, 2, 3, 4, 1]
####################################
