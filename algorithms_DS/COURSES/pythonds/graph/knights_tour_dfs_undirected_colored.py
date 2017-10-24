#!/bin/env python3

import sys
from knights_tour_graph import knightGraph, pprint

# also see:
# - http://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/

def knightTour(n,path,u,limit):
        # start - u
        # end - limit
        # traversed[] - path
        # level/depth - n (query whether all nodes covered)
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                # import pdb; pdb.set_trace()
                cv = G.getVertex(nbrList[i])
                if cv.getColor() == 'white':
                    done = knightTour(n+1, path, cv, limit)
                i += 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done


if __name__ == '__main__':

    try:
        board_size = int(sys.argv[1])
    except:
        board_size = 8
        
    G = knightGraph(board_size)
    # pprint(G)

    u = G.getVertex(0)

    # todo: check if the base calling params are right
    print(knightTour(0, [], u, 63))
