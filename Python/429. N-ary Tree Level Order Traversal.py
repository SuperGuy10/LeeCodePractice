'''
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            level = []
            r = []
            for node in stack:
                r.append(node.val)
                for child in node.children:
                    level.append(child)
            stack = level
            res.append(r)
        return res


'''
use any()
any(q) can be O(N) operation for another problem if array is like this [None, None, ... , sth].
In this problem, "None" can only be placed in zero index and only once, so it's O(1) operation.
'''
class Solution(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
