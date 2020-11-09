'''
Given two non-empty binary trees s and t, 
check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        if not t:
            return True
        
        def check(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.left) and check(root1.right, root2.right)
        
        def dfs(r1, r2):
            if not r1:
                return False
            
            if r1.val == r2.val and check(r1, r2):
                return True
            
            return dfs(r1.left, r2) or dfs(r1.right, r2)
        
        return dfs(s,t)
