#!/usr/bin/env python2

# problem statement is in peg_jumper.txt in $pwd
# input goes like

# 10
# 4
# 2 4 1 9 7 5 8

# TODO: return instance sum instead of peg lengths.
# Also, debug the suspected failure. Since it only
# returns correct answer for current sample input.
# The answer may not always be a couple..
# (which is what it returns in 'instances' i.e., [pegs[i], current])

tot = int(raw_input())
cap = int(raw_input())

pegs = [int(i) for i in raw_input().split()]
pegs = dict(zip(xrange(len(pegs)), pegs))

instances = []

def enroute(pegs, current=None, instances=[]):
    #import pdb; pdb.set_trace()
    # find least number to start with thats present in the list
    diff = current - cap
    # find candidates which can be reached from point Y
    # and are farthest but earliest
    candidates = [k for k in pegs if pegs[k] >= diff]
    # one by one, choose early candidates and see if reachable
    # by choosing previous instances
    if candidates:
        # filter if a bigger previously rejected number appears
        candidates = [i for i in candidates if pegs[i] < current]
        for i in candidates:
            if pegs[i] <= cap:
                instances.extend([pegs[i], current])
                return instances
            else:
                new_pegs = dict([(k,v) for k,v in pegs.iteritems() if k in range(i)])
                enroute(new_pegs, current=pegs[i], instances=instances)
                if instances:
                    return instances
    else:
        return instances

print enroute(pegs, current=tot)
