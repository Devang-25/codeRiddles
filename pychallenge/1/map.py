from string import maketrans

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#convert = lambda x: chr(x)
letters = ''.join(map(chr, xrange(97,123)))
letters_new = ''.join(map(chr, xrange(99,123)))+'ab'
translation = maketrans(letters, letters_new)

print text
print
print text.translate(translation)
print

url = raw_input("Enter your string: ") # url = map
print url.translate(translation)
