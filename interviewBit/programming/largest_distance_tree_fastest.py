#!/usr/bin/env python3

# https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/

import sys
sys.setrecursionlimit(100000)


def find_depth(graph, root, max_depth=0):
    if root not in graph or len(graph[root]) == 0: return 0 # leaf
    max_1, max_2 = 0, 0
    for child in graph[root]:
        curr_depth = 1 + find_depth(graph, child, max_depth)
        if curr_depth > max_1:
            max_1, max_2 = curr_depth, max_1
        elif curr_depth > max_2 :
            max_2 = curr_depth
    if max_1 + max_2 > max_depth:
        max_depth = max_1 + max_2

    return max_1


if __name__ == '__main__':
    max_depth = 0
    A = [-1,0,0,0,3]
    graph = {}
    for i, el in enumerate(A):
        children = graph.setdefault(i, [])
        if el == -1:
            root = i
        else:
            graph[el].append(i)
    print(find_depth(graph, root))


# # from collections import defaultdict
#
# class Node(object):
#     def __init__(self, data, parent=None, level):
#         self.data = data
#         self.children = []
#         self.parent = parent
#         self.level = level
#
#     def add_child(self, obj):
#         self.children.append(obj)
#
# # class Tree(object):
# #     # unweighted, rooted
# #     def __init__(self, root_node=0, level=-1, count):
# #         self.key = root_node
# #         self.children = [] # defaultdict(list)
# #         self.level = level
# #         self.count = count
#
# #     # def __contains__(self, k):
# #     #     return k in self.vertList
#
# #     # def __iter__(self):
# #     #     return iter(self.children.values())
#
# #     def __repr__(self):
# #         return "%s: %s" % (self.key, [node for node in self.children])
#
# #     def insertChild(self, new_node, parent_level):
# #         if not self.children:
# #             self.children.append(Tree(new_node, level=parent_level+1))
# #             print("added")
# #         else:
# #             if new_node not in self.children:
# #                 self.children[new_node] = Tree(new_node, level=parent_level+1)
# #             else:
# #                 print("already present")
#
# from collections import defaultdict
#
#
# class Solution(object):
#     def __init__(self):
#         self.tree = None
#         # self.tree = None
#         # self.arr = arr
#         self.max_depth = 0
#
#     # node values are represented by 0 indexed list
#     def construct_tree(self, arr):
#         # root_node = arr.index(-1)
#         # self.tree = Tree(root_node)
#         # for node, parent_level in enumerate(arr):
#         #     if node == root_node:
#         #         continue
#         #     self.tree.insertChild(node, parent_level)
#         for i,j in enumerate(arr):
#             if not self.tree:
#                 self.tree = Node()
#             self.tree[j].append(i)
#
#     def traverse(self, root):
#         if root not in self.tree or len(tree[root]):
#             pass
#
#     def solve(self, n, m):
#         """
#         @param A : list of integers
# 	      @return an integer
#         """
#         if not self.tree:
#             self.construct_tree(arr)
#
#         S.solve(1,4)
#
# if __name__ == '__main__':
#     S = Solution()
#     arr = [-1, 0, 0, 0, 3]
#     S.construct_tree(arr)
#     print(S.tree)
