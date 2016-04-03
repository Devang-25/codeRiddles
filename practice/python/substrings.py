#!/usr/bin/env python3

import itertools

ip = input()

def generate_substrings(ip):
    ip_len = len(ip)
    return set([ip[i:j+1] for i in range(ip_len) for j in range(i,ip_len)])

def generate_substrings_2(ip):
    s = set()
    for i in range(1,len(ip)+1):
        s.update([''.join(x) for x in list(itertools.combinations(ip, i))])
    return s


x = generate_substrings(ip)
print("in order: \n", len(x), x)
x = generate_substrings_2(ip)
print("without order: \n", len(x), x)
