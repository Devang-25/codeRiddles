#!/bin/env python3

# http://www.pythonchallenge.com/pc/def/map.html

# py2
# from string import maketrans

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#convert = lambda x: chr(x)
letters = ''.join(map(chr, range(97,123)))
letters_new = ''.join(map(chr, range(99,123)))+'ab'
translation = str.maketrans(letters, letters_new)

print(text, end="\n\n")
print(text.translate(translation), end="\n\n")

url = input("Enter your string: ") # url = map
print(url.translate(translation))
