'''
Given a Binary Search Tree (BST), 
convert it to a Greater Tree 
such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Don't forget the feature of Binary Search Tree: node.right.val > node.val > node.left.val

class Solution(object):
    def convertBST(self, root):
        def dfs(node,val): #return cumu sum of this node.
            if not node:
                return val
            val=dfs(node.right,val)
            node.val+=val
            return dfs(node.left,node.val)
        dfs(root,0)
        return root
        
        
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root
