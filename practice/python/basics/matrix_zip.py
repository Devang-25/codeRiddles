mat = [
    [1, 2, 3, 0],
    [5, 6, 7, 8],
    [9, 0, 11, 12],
    [13, 0, 15, 16],
    [112, 0, 51, 96]
]

s = [[str(e) for e in row] for row in matrix]

print(s)

print([max(map(len, col)) for col in s])
print([max(map(len, col)) for col in zip(*s)])

# In [116]: [max(map(len, col)) for col in s]
# Out[116]: [1, 2, 2, 2, 2]

# In [117]: [max(map(len, col)) for col in zip(*s)]
# Out[117]: [2, 2, 2, 2, 2]

# why ?
