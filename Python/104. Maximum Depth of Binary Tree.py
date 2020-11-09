'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        depth = 0
        while stack:
            level = []
            while stack:
                node = stack.pop()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right) 
            stack  = level
            depth += 1
        return depth

# Easy to understand

class Solution:
    def getMax(node, currentDepth) -> 'int':
        #basecase leafnode
        if node.left==None and node.right==None:
            return currentDepth
        
        else:
            if node.left==None:
                return Solution.getMax(node.right, currentDepth+1)
            elif node.right==None:
                return Solution.getMax(node.left, currentDepth+1)
            else: return max(Solution.getMax(node.left, currentDepth+1), Solution.getMax(node.right, currentDepth+1))
    
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root==None:
            return 0
        return Solution.getMax(root, 1)
        
# One line solution

class Solution:
    def getMax(node, currentDepth) -> 'int':
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        

# queue for level order

 def maxDepth(self, root):     
     if not root:
         return 0
     
     tqueue, h = collections.deque(),0
     tqueue.append(root)
     while tqueue:
         nextlevel = collections.deque()
         while tqueue:
             front = tqueue.popleft()
             if front.left:
                 nextlevel.append(front.left)
             if front.right:
                 nextlevel.append(front.right)
         tqueue = nextlevel
         h += 1
     return h
