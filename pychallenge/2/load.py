#!/bin/env python3

# www.pythonchallenge.com/pc/def/ocr.html

from collections import Counter

data = open('ocr.txt').read()     

char_freq = Counter(data)
# Counter({'\n': 1220,
#          '!': 6079,
#          '#': 6115,
#          '$': 6046,
#          '%': 6104,
#          '&': 6043,
#          '(': 6154,
#          ')': 6186,
#          '*': 6034,
#          '+': 6066,
#          '@': 6157,
#          '[': 6108,
#          ']': 6152,
#          '^': 6030,
#          '_': 6112,
#          'a': 1,
#          'e': 1,
#          'i': 1,
#          'l': 1,
#          'q': 1,
#          't': 1,
#          'u': 1,
#          'y': 1,
#          '{': 6046,
#          '}': 6105})

rare_chars = [l for l in char_freq if char_freq[l] == 1]

print("%s.html" % ''.join([i for i in data if i in rare_chars]))
# todo: filter rare chars from data, either in naive manner, or using sophisticated algos like KMP, boyce-moore etc..

