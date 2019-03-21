'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
     1
    / \
   2   3 
  /
 4
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
     1
    / \
   2   3 
    \   \
     4   5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
     1
    / \
   2   3 
    \   
     4   
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        dic = {}
        def check(root, depth =0, parentVal=None):
            if root == None:
                return
            dic[root.val] = (depth, parentVal)
            check(root.left, depth+1, parentVal=root.val)
            check(root.right, depth+1, parentVal=root.val)
        check(root)
        return dic[x][0] == dic[y][0] and dic[x][1] != dic[y][1]
