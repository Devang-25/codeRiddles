# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def height(self, node):     
        # Base Case : Tree is empty
        if node is None:
            return 0 ;     
        # If tree is not empty then height = 1 + max of left 
        # height and right heights 
        return 1 + max(self.height(node.left), self.height(node.right))


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base Case when tree is empty 
        if root is None:
            return 0;

        # Get the height of left and right sub-trees
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        # Get the diameter of left and irgh sub-trees
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree +1 
        return max(lheight + rheight, max(ldiameter, rdiameter))

