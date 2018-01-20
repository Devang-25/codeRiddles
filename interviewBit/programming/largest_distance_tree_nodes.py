#!/usr/bin/env python3

# from collections import defaultdict

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, obj):
#         self.children.append(obj)


# class Tree(object):    
#     # unweighted, rooted
#     def __init__(self, root_node=0, level=-1, count):
#         self.key = root_node
#         self.children = [] # defaultdict(list)
#         self.level = level
#         self.count = count
        
#     # def __contains__(self, k):
#     #     return k in self.vertList

#     # def __iter__(self):                                                           
#     #     return iter(self.children.values())

#     def __repr__(self):
#         return "%s: %s" % (self.key, [node for node in self.children])

#     def insertChild(self, new_node, parent_level):
#         if not self.children:
#             self.children.append(Tree(new_node, level=parent_level+1))
#             print("added")
#         else:
#             if new_node not in self.children:
#                 self.children[new_node] = Tree(new_node, level=parent_level+1)
#             else:
#                 print("already present")

from collections import defaultdict


class Solution(object):
    def __init__(self, arr):
        self.tree = defaultdict(list)
        # self.tree = None
        self.max_depth = 0

    # node values are represented by 0 indexed list
    def construct_tree(self, arr):
        # # arr = [-1, 0, 0, 0, 3]
        # root_node = arr.index(-1)
        # self.tree = Tree(root_node)                
        # for node, parent_level in enumerate(arr):
        #     if node == root_node:
        #         continue
        #     self.tree.insertChild(node, parent_level)
        for i,j in enumerate(arr):
            self.tree[j].append(i)

    def traverse(self, root):
        if root not in self.tree or len(tree[root]):
            pass
        
    def solve(self, n, m):
        """
        @param A : list of integers
	      @return an integer
        """
        if not self.tree:
            self.construct_tree(arr)
        
        S.solve(1,4)
