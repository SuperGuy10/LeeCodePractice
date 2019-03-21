'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True
 

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        stack = [root]
        res = []
        while stack:
            level = []
            while stack:
                node = stack.pop()
                if node:
                    level.append(node.left)
                    level.append(node.right)
                    res.append(node.val)
            stack = level
        for i in range(len(res)-1):
            for j in range(i+1, len(res)):
                if res[i]+res[j] == k:
                    return True
        return False
        


# Smart way

class Solution:
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        if root is None:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
                
        return False
