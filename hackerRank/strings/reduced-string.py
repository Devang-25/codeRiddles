#!/bin/env python3

def super_reduced_string(ip):
    tmp = ip[0]
    for i in range(1, len(ip)):
        print("Stack: %s | Current char - %s | ..at index %s" % (tmp, ip[i], i))
        try:
            if ip[i] == tmp[-1]:
                print("popping stack")
                tmp = tmp[:-1]
            else:
                tmp+=ip[i]
        except:
            tmp = ip[i]
            
    if not tmp:
        return "Empty String"
    
    return tmp
        
if __name__ == '__main__':
    ip = input()
    print("Final result: ", super_reduced_string(ip))
    # aaabccddd
    # baab
