'''
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
Accepted
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        a = set()
        def addToSet(node):
            a.add(node.val)
            if node.left:
                addToSet(node.left)
            if node.right:
                addToSet(node.right)
        addToSet(root)
        if len(a) > 1:
            return False
        else:
            return True

# one line solution
class Solution:
    
    def isUnivalTree(self, root):
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)
        
# recursive
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            if root.left and root.left.val!= root.val:
                return False
            if root.right and root.right.val!= root.val:
                return False
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
