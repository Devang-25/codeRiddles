#!/bin/env python3

import sys
from pprint import pprint
from adj_list_undirected_graph import Graph


def genLegalMoves(x,y,bdSize):
    newMoves = []
    # considering knight as 12th position,
    # for a moment, take its pos as 0,0 coordinates
    # knight can move 2.5 steps (per se, diagonal 'L' shaped move)
    # so then, node id 1 [row 0, col 1] can be represented as
    # 2 rows down, 1 column left from [0,0]
    # move offset for Node 1 => -2, -1
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # this 'if' statement puts a check on knight's move
        # so if for ex, knight is at node 1, it doesn't go
        # out of the board in next set of moves, because
        # each set of moves is prepared from moveOffsets[]
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def knightGraph(bdSize):
    # we choose undirected graph because a move from
    # node 0 to node 7 means vice-versa is possible too
    ktGraph = Graph()
    for row in range(bdSize):
       for col in range(bdSize):
           # iterates over all coordinates on chessboards,
           # generating legally bound edges. Thus generating
           # squares that can be covered by the knight
           nodeId = posToNodeId(row,col,bdSize)
           newPositions = genLegalMoves(row,col,bdSize)
           for e in newPositions:
               # converts coordinates to node ids, and appends them
               # as edge connections to a particular node
               nid = posToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)
    # contains all connected components as possible moves.
    # query the graph to obtain covered area
    return ktGraph

def posToNodeId(row, column, board_size):
    """
    ..maps coordinates on chess board to node id
    [refer to knightmoves.png in this folder]
    
    So board size is 5 (as we have a 5x5 board) 

    row 1, col 0 has value 5
    r * s + c => 1 * 5 + 0 = 5
    
    row 2, col 2 has value 12 (knight's center position)
    r * s + c => 1 * 5 + 0 = 5
    """

    return (row * board_size) + column

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


if __name__ == '__main__':

    try:
        board_size = int(sys.argv[1])
    except:
        board_size = 5
        
    G = knightGraph(board_size)
    pprint(G)

    print("\n Above Graph shows all nodes covered by the knight")
    print("..on a %s by %s chess board" % (board_size, board_size))

    # from collections import Counter
    # c = Counter()
    # for v in G.graph.values(): c += Counter(v)
    # print("Squares/Nodes, by frequency of coverage: \n%s" % c)

    # can be multiple if larger sized chess board. Try 6x6
    highest_connected =  max(G.graph, key=(lambda k: len(G.graph[k])))
    print("Max moves possible from Node/Square # %s" % highest_connected)
