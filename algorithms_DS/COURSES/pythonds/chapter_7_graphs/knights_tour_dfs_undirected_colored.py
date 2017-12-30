#!/bin/env python3

import sys
from knights_tour_graph import knightGraph, pprint

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
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            #import pdb; pdb.set_trace()
            cv = G.getVertex(nbrList[i])
            # print(u._id, u.getColor(), nbrList, cv._id, cv.getColor(), limit, path)
            if cv.getColor() == 'white':
                done = knightTour(n+1, path, cv, limit)
            i += 1
        if not done:  # prepare to backtrack
            # print("backtracking ", u._id, u.getColor())
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
