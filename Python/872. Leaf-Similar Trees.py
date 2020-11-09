'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
      3
    /  \
   5     1
  / \   / \
 6   2  9  8 
    / \
   7   4
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1) == self.dfs(root2)
    def dfs(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return self.dfs(node.left) + self.dfs(node.right)
        
        
'''
General methode is that traverse DFS whole tree to a list and compare two lists.
Here I share an idea of comparing node by node using O(logN) space.
Use a stack<TreeNode> to keep dfs path.
dfs(stack) will return next leaf.
Check leaves one by one, until the end or difference.
Only O(logN) space for stack, no extra space for comparation.
O(1) is also possible if we can modify the tree.

for more information about Yield, check:
https://stackabuse.com/understanding-pythons-yield-keyword/
https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
'''

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))
