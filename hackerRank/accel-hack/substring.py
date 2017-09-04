#!/usr/bin/python2

# # usage ex:
# $ ./substring.py

# input
# $ abbab aba

# output
# $ 2

# explanation: aba is 1 letter close to [abb, bba]
# out of 3 letter (aba's length) subsets: [abb, bba, bab] 

ip = raw_input().split()
sub_len = len(ip[1])

# assert (0<len(ip[0])<10**6) and (0<len(ip[1])<10**6)

def extract_sub(word, word_test, sub_len):
    count = 0
    processed = []
    for i in xrange(len(word)):
        if i+sub_len <= len(word): 
            sub = word[i:i+sub_len]
            if sub not in processed:                
                processed.append(sub)
                # print(set(list(sub)).intersection(list(ip[1])))
                c = 0
                for i, j in zip(sub, word_test):
                    if i != j:
                        c+=1
                        if c > 1:
                            break
                if c==1:
                    count+=1
            
    return count

print(extract_sub(ip[0], ip[1], sub_len))
