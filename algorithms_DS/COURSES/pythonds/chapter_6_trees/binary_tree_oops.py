#!/usr/bin/env python3


class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def __str__(self):
        if self.leftChild and self.rightChild:
            return "{ %s: [%s, %s] }" % \
                (self.getRootVal(), self.leftChild, self.rightChild)
        else:
            return "%s" % (self.getRootVal())

    def __repr__(self):
        return "BinaryTree(Node => %s)" % self.getRootVal()
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        print("changing %s -> %s" % (self.key, obj))
        self.key = obj

    def getRootVal(self):
        return self.key


# https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
def height(node):     
    # Base Case : Tree is empty
    if node is None:
        return 0 ;     
    # If tree is not empty then height = 1 + max of left 
    # height and right heights 
    return 1 + max(height(node.leftChild) ,height(node.rightChild))


# Function to get the diamtere of a binary tree
def diameter(root):
    # Base Case when tree is empty 
    if root is None:
        return 0;
 
    # Get the height of left and right sub-trees
    lheight = height(root.leftChild)
    rheight = height(root.rightChild)
 
    # Get the diameter of left and irgh sub-trees
    ldiameter = diameter(root.leftChild)
    rdiameter = diameter(root.rightChild)
    print(root, lheight, rheight, ldiameter, rdiameter)
    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1 
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == '__main__':    
    r = BinaryTree('a')
    print("Tree: ", r)
    print("Left: ", r.getLeftChild())
    print("Right: ", r.getRightChild())    
    r.insertLeft('b')
    print("Left: ", r.getLeftChild())
    # print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print("Right: ", r.getRightChild())
    # print(r.getRightChild().getRootVal())
    print("Tree: ", r)
    r.getRightChild().setRootVal('hello')
    # print(r.getRightChild().getRootVal())
    print("Tree: ", r)
    print("Height: ", height(r))
    print("Diameter: ", diameter(r))

    print("="*10)
    r = BinaryTree(1)
    r.insertLeft(2)
    r.insertRight(3)
    r.getLeftChild().insertLeft(4)
    r.getLeftChild().insertRight(5)
    print("Tree: ", r)
    print("Height: ", height(r))
    print("Diameter: ", diameter(r))

          
# Tree:  a
# Left:  None
# Right:  None
# Left:  b
# Right:  c
# Tree:  { a: [b, c] }
# changing c -> hello
# Tree:  { a: [b, hello] }
# Height:  2
# Diameter:  3
# ==========
# Tree:  { 1: [{ 2: [4, 5] }, 3] }
# Height:  3
# Diameter:  4
