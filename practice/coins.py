#! /usr/bin/env python

def recurse(dictionary, key):
    if key not in dictionary:
        dictionary[key] = recurse(dictionary, key/2) + recurse(dictionary, key/3) + recurse(dictionary, key/4)
    return dictionary[key]

def main():    # Don't leave the code in the global namespace, it runs slower

    import sys

    tokenizedInput = map(int, sys.stdin.read().split())

    results = {}

    for count in xrange(0, 12):
        results[count] = count      # Cannot do any better than straight exchange for these values

    for count in xrange(0, len(tokenizedInput)):
        print recurse(results, tokenizedInput[count])

main()
