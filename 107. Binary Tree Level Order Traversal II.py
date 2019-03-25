'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        stack = [root]
        ans = []
        while stack:
            level = []
            tem = []
            for node in stack:
                if node:
                    if node.left or node.right:
                        level += node.left, node.right
                    #print("level",level)
                    tem.append(node.val)
                    #print('tem',tem)
            stack = level
            ans.append(tem)
            #print(ans)
        return ans[::-1]
        
# Same idea
class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        
        result, current = [], [root]
        while current:
            next_level, values = [], []
            for node in current:
                values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            current = next_level
            result.append(values)
        return result[::-1]    

# use deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque([root])
        cur = root
        result = []
        while cur and queue:
            level_res = []
            level_que = collections.deque([])
            while queue:
                cur = queue.popleft()
                level_res.append(cur.val)
                if cur.left:
                    level_que.append(cur.left)
                if cur.right:
                    level_que.append(cur.right)
            result.append(level_res)
            queue = level_que
        return result[::-1]
