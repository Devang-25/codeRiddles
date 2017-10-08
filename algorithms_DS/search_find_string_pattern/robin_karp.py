#!/bin/env python3

# Robin karp
# used for plagiarism checks
# O(mn)

def match_pattern(ip, pattern, prime=3):
    m = len(pattern)
    _values = dict([(j,i+1) for i,j in enumerate(set(ip))])
    pat_hash = sum([_values[pattern[i]] * 3**i for i in range(len(pattern))])
    for n in range(len(ip)):
        try:
            string = ip[n:m]
            if n == 0:
                last_hash = sum([_values[string[i]] * 3**i for i in range(len(string))])
            else:
                last_hash -= _values[ip[n-1]]
                last_hash /= prime
                last_hash += _values[ip[n+m-1]] * 3**(m-1)
            print("Current Hash: %s || Pattern Hash: %s" % (last_hash, pat_hash))
            if last_hash == pat_hash:
                return True
        except:
            continue
    return False
        
if __name__ == '__main__':

    ip = input("Enter text: ")
    pattern = input("Enter pattern: ")

    print(match_pattern(ip, pattern))
