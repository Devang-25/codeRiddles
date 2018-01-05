#!/usr/bin/python3

# Complete the function below for lexicographically arranged letters of input

import itertools

def find_all_possible_teams():
    arr = list(input())
    assert len(arr) < 26
    final = []
    for i in range(1, len(arr)+1):
        tmp = list(itertools.combinations(arr, i))
        final.extend([''.join(i) for i in tmp])
    [print(i) for i in final]

find_all_possible_teams()


'''
Input:
abc

Output:
a
b
c
ab
ac
bc
abc
'''
