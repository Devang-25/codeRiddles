#!/bin/env python3


# http://interactivepython.org/runestone/static/pythonds/Graphs/KnightsTourAnalysis.html#lst-avail
# 
# "on a five-by-five board you can produce a path in about
# 1.5 seconds on a reasonably fast computer. But what happens
# if you try an eight-by-eight board? In this case, depending on
# the speed of your computer, you may have to wait up to a half
# hour to get the results! The reason for this is that the
# knight’s tour problem as we have implemented it so far is an
# exponential algorithm of size O(k^N), where N is the
# number of squares on the chess board, and k is a small constant"

# also see:
# - http://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/


import sys
from knights_tour_graph import knightGraph, pprint
	
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        v = G.getVertex(v)
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                w = G.getVertex(w)
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    
    return [y[1] for y in resList]

def knightTour(n,path,u,limit):
    """
    @u - start 
    @limit - end
    @path - traversed[]
    @n - level/depth (query whether all nodes covered)
    """
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            cv = nbrList[i]
            if cv.getColor() == 'white':
                done = knightTour(n+1, path, cv, limit)
            i += 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        print(n, len(path), u._id, u.getColor(), limit)     
        done = True
    return done


if __name__ == '__main__':

    try:
        board_size = int(sys.argv[1])
    except:
        board_size = 5
        
    G = knightGraph(board_size)
    u = G.getVertex(0)
    print(knightTour(0, [], u, board_size**2 - 1))
