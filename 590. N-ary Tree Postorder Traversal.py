'''
Given an n-ary tree, return the preorder traversal of its nodes' values.
For example, given a 3-ary tree:
 {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},
 {"$id":"3","children":[],"val":2},
 {"$id":"4","children":[],"val":4}],
 "val":1}
 
Return its postorder traversal as: [5,6,3,2,4,1].
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
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            stack += node.children
            res.append(node.val)
        return res[::-1]
        
'''
Recursion way is easy to understand
'''

class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None: return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res
