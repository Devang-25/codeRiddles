#!/bin/env python3

# http://www.pythonchallenge.com/pc/def/equality.html

import re
from collections import Counter

_values = [0]

# Enable Knuth Morris Pratt algorithm
_kmp = False

def prefix_table(pattern):
    # O (M)    
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j+=1
            i+=1
            _values.append(j)
        else:
            if j > 0:
                j = _values[j-1]
            else:
                _values.append(j)
                i+=1
                
    return _values

def search_pattern(ip, pattern, _dbg=False):
    # O(N)
    # T = bacbabababacaca
    # P = ababaca
    
    _values = prefix_table(pattern)

    print("DFA: %s" % _values)
    
    i = j = 0
    m = len(pattern) - 1
    
    while i <= len(ip)-1:
        if _dbg:
            print(i,j)
        if pattern[j] == ip[i]:
            if j == m:
                return i-m, True
            j+=1
            i+=1
        else:
            if j>0:
                j = _values[j-1]
                continue
            i+=1
            
    return -1, False

def hot_encode(x):
    if x in range(97,124):
        # a-z -- 97-123
        return '0'
    elif x in range(65,92):
        # A-Z -- 65-91
        return '1'


def preprocess(data):
    
    ## pattern = re.compile(r'[A-Z]{3,3}[a-z][A-Z]{3,3}')
    # In [12]: pattern.match('xQXgalSKJ')

    # In [13]: pattern.match('XQXgSKJ')
    # Out[13]: <_sre.SRE_Match object; span=(0, 7), match='XQXgSKJ'>

    z = lambda x: ord(x)                          

    data_ord_new = [z(i) for i in data]    
    # In [52]: len([z(i) for i in data.replace('\n','')])
    # Out[52]: 100000

    # data_ord = [[z(i) for i in line] for line in data.splitlines()]
    # data_ord_new = []                                   
    # while data_ord: data_ord_new.extend(data_ord.pop())     
    
    # # In [40]: sum([len(line) for line in data.splitlines()])
    # # Out[40]: 100000

    # # In [41]: len(data_ord_new)
    # # Out[41]: 100000

    data_encoded = ''.join([hot_encode(k) for k in data_ord_new])
    
    with open('encoded.txt', 'w') as f:
        f.write(data_encoded)

    return data_encoded
    
if __name__ == '__main__':    

    data = open('text.txt').read()
    data = data.replace('\n','')
    data_encoded = preprocess(data)
    
    if _kmp:
        
        # One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
        pattern = r'011101110'
        # In [3]: ''.join(map(chr, range(97,123)))
        # Out[3]: 'abcdefghijklmnopqrstuvwxyz'

        # In [6]: ''.join(map(chr, range(65,91)))
        # Out[6]: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        _at, status = search_pattern(data_encoded, pattern)

        if not status:
            # test 2 edge cases
            # - beginning
            edge_case = False
            pattern_begin = pattern[1:]
            if data_encoded[:len(pattern_begin)] == pattern_begin:
                _at, status, edge_case = 0, True, True
                print(data[_at:_at+len(pattern)-1])
            else:
                pattern_end = pattern[:-1]
                if data_encoded[-len(pattern_end):] == pattern_end:
                    _at, status, edge_case = len(data_encoded) - len(pattern_end) + 1, True, True
                    print(data[_at:])

            print("%s at index %s" % (status, _at))

            if not edge_case:
                print("%s at index %s" % (status, _at))
            print("Edge case")
        else:
            print("%s at index %s" % (status, _at))
            print(data[_at:_at+len(pattern)])

    else:

        pattern = r'(0|^)1110111(0|$)'
        len_pat = 7

        # # OR
        # pattern = '011101110'
        # len_pat = len(pattern)-1
        
        matches = re.finditer(pattern, re.escape(data_encoded))
        # print(list(matches))
        idx_all = [match.start() + 1 for match in matches]

        # print(idx_all)
        print(dict(zip(idx_all, [data[idx:idx+len_pat] for idx in idx_all])))
        print("%s.html" % ''.join([data[idx+len_pat//2] for idx in idx_all]))
        
