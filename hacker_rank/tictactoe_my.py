#!/bin/python                                                                                                                                   
from random import *
from string import *
# Complete the function below to print 2 integers separated by a single space which will be your next move                                      
def nextMove(player,board):
#If player is X, I'm the first player.                                                                                                          
#If player is O, I'm the second player.                                                                                                         
    print 'fixx'
#Read the board now. The board is a 3x3 array filled with X, O or _.                                                                            
board = []
list=[]         
for j in xrange(0,3):
    for i in xrange(0, 3):
        board.append(raw_input())
list = join(board,"\n")
#player = raw_input()
#nextMove(player,board)
print list
print board
