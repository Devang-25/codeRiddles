#!/usr/bin/env python2

# class tree():
#     def __init__(self):
#         '''Initialise the tree'''
#         self.Data = None
#         self.Count = 0
#         self.LeftSubtree = None
#         self.RightSubtree = None

#     def Insert(self, data):
#         '''Add an item of data to the tree'''
#         if self.Data == None:
#             self.Data = data
#             self.Count += 1
#         elif data < self.Data:
#             if self.LeftSubtree == None:
#                 # tree is a recurive class definition
#                 self.LeftSubtree = tree()
#             # Insert is a recursive function
#             self.LeftSubtree.Insert(data)
#         elif data == self.Data:
#             self.Count += 1
#         elif data > self.Data:
#             if self.RightSubtree == None:
#                 self.RightSubtree = tree()
#             self.RightSubtree.Insert(data)

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]                
                        
                        
if __name__ == '__main__':

    # T = tree()
    # # The root node
    # T.Insert(raw_input('Enter an alphabet: '))
    # # Will be put into the left subtree
    # T.Insert(raw_input('Enter an alphabet: '))
    # # Will be put into the right subtree
    # T.Insert(raw_input('Enter an alphabet: '))

    r = BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l = getLeftChild(r)
    print(l)

    setRootVal(l,9)
    print(r)
    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))
    print

    x = BinaryTree('a')
    insertLeft(x,'b')
    insertRight(x,'c')
    insertRight(getRightChild(x),'d')
    insertLeft(getRightChild(getRightChild(x)),'e')
    print(x)
    print
    
    z = BinaryTree('a')
    insertLeft(z, 'b')
    insertRight(z, 'c')
    insertRight(getLeftChild(z),'d')
    insertLeft(getRightChild(z), 'e')
    insertRight(getRightChild(z), 'f')
    print(z)
