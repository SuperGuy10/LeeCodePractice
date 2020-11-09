'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

'''
We are looking for the highest difference between left sub-tree and right sub-tree, 
because this diameter will be the longest distance between two leaves. 
For this we can calculate length of left sub-tree and 
right sub-tree and keep track of what is the maximum value of height(left)+height(right)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth = 0
        def calDepth(node):
            if not node:
                return 0
            left = calDepth(node.left)
            right = calDepth(node.right)
            self.depth = max(self.depth, left+right)
            return 1 + max(left, right)
        calDepth(root)
        
        return self.depth
