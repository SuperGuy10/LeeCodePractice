'''
Given an n-ary tree, return the preorder traversal of its nodes' values.
For example, given a 3-ary tree:

 {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},
 {"$id":"3","children":[],"val":2},
 {"$id":"4","children":[],"val":4}],
 "val":1}

Return its preorder traversal as: [1,3,5,6,2,4].
Note:
Recursive solution is trivial, could you do it iteratively?
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# iteratively
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            stack += node.children[::-1]
            res.append(node.val)
        return res
        
# Recursive way
class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        res = []
        if root == None:
            return []
        
        def recursive(root, res):
            for child in root.children[::-1]:
                recursive(child, res)
            res.append(root.val)
            
        recursive(root, res)
        return res[::-1]
