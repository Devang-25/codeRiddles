#!/usr/bin/env python2

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
