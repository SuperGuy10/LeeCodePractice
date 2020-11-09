'''
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
For example, given a 3-ary tree:
      1
   /  \   \
  3   2    4
 / \
5   6
We should return its max depth, which is 3.

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# BFS Check all the nodes per level

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        stack = [root]
        while stack:
            level = []
            while stack:
                node = stack.pop()
                if node.children:
                    level += node.children
            stack = level
            depth +=1
        return depth

# same idea different style

class Solution(object):
    def maxDepth(self, root):
        stack, level = root and [root], 0
        while stack:
            stack, level = [child for node in stack for child in node.children if child], level + 1
        return level
        
        
# DFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        stack = [root]
        depth = 0
        while stack:
            depth += 1
            level=[]
            for node in stack:
                level += node.children
            stack = level
        return depth
        
class Solution:
    def maxDepth(self, root: 'Node') -> 'int':
        if not root:
            return 0
        max_depth_child = 0
        for child in root.children:
            curr_depth = self.maxDepth(child)
            if curr_depth > max_depth_child:
                max_depth_child = curr_depth
        return 1 + max_depth_child
        
