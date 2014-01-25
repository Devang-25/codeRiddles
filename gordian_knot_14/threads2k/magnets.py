#!/usr/bin/python
"""
import collections

    def getLeastCost(self):
        counter=collections.Counter(self.cnt)
        counter.values()
        counter.keys()
        counter.items()
        money_needed = [self.cnt,self.baseCost,self.seatCost]
        return money_needed, counter
"""

class Magnets:
    def __init__(self, board=[], props=[]):
            self.board = board
            self.props = props

    def get_Board_Attribs(self):
        ''' Input / Check Board Attributes '''
        size = int(raw_input())
        for i in xrange(size):
            # input space-separated elements into array
            # checks and converts list of strings into integers 
            self.board.append(map(int, raw_input().split()))                
        # property: [pr,nr,pc,nc]
        for i in xrange(4):
            self.props.append(map(int, raw_input().split()))
        return self.board, self.props 


if __name__ == '__main__': 
    try:
        T = int(raw_input())
        Mg = Magnets()
        #for i in xrange(T): 
        board, props = Mg.get_Board_Attribs()
        print 
        print board
        print props
    except:
        quit('Constraint: Only integer / no space input allowed')
