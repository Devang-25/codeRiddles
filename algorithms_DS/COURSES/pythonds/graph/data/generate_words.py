#!/bin/env python3

def generate_words(d):
    l = []

    # generate patterns for 4 letter words
    patterns = {
        'ope': lambda x: x[1:], #_OPE
        'ppe': lambda x: x[0] + x[2:], #P_PE
        'poe': lambda x: x[:2] + x[3], #PO_E
        'pop': lambda x: x[:3], #POP_
        }

    for p in patterns:
        l.extend([i for i in d if patterns[p](i) == p])

    return l

if __name__ == '__main__':    
    f = open('wordlists_large.txt', 'r')
    d = f.read().splitlines()
    f.close()
    
    words = generate_words(d)
    f = open('wordlists_small.txt', 'w')
    f.write('\n'.join(words))
    f.close()

    print("..generated wordlists_small.txt")
