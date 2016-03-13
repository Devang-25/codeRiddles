#!/usr/bin/env python2

class tree():
    def __init__(self):
        '''Initialise the tree'''
        self.Data = None
        self.Count = 0
        self.LeftSubtree = None
        self.RightSubtree = None

    def Insert(self, data):
        '''Add an item of data to the tree'''
        if self.Data == None:
            self.Data = data
            self.Count += 1
        elif data < self.Data:
            if self.LeftSubtree == None:
                # tree is a recurive class definition
                self.LeftSubtree = tree()
            # Insert is a recursive function
            self.LeftSubtree.Insert(data)
        elif data == self.Data:
            self.Count += 1
        elif data > self.Data:
            if self.RightSubtree == None:
                self.RightSubtree = tree()
            self.RightSubtree.Insert(data)

if __name__ == '__main__':
    T = tree()
    # The root node
    T.Insert(raw_input('Enter an alphabet: '))
    # Will be put into the left subtree
    T.Insert(raw_input('Enter an alphabet: '))
    # Will be put into the right subtree
    T.Insert(raw_input('Enter an alphabet: '))
    print T[0]
