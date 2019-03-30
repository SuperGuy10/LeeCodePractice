'''
Given a binary search tree (BST) with duplicates, 
find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 
return [2].

Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dic = {}
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.val not in dic:
                dic[node.val] = 1
            dic[node.val] += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        res = []
        max_ele = max(dic.values())
        for key, val in dic.items():
            if val == max_ele:
                res.append(key)
        return res
