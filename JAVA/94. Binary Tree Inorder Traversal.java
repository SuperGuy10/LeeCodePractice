/**
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up:
Recursive solution is trivial, could you do it iteratively?
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
//     public List<Integer> inorderTraversal(TreeNode root) {
//         List<Integer>ans = new ArrayList<Integer>();
//         if(root == null){
//             return ans;
//         }
        
//         inorder(root, ans);
//         return ans;
//     }
    
//     public void inorder(TreeNode root, List<Integer>ans){
//         // if(root == null){
//         //     return;
//         // }
//         if(root.left != null){
//             inorder(root.left, ans);
            
//         }
//         ans.add(root.val);
        
//         if(root.right != null){
//             inorder(root.right, ans);
//         }
        
        
//     }
    
    /**
        1、cur.left 为 null，保存 cur 的值，更新 cur = cur.right

        2、cur.left 不为 null，找到 cur.left 这颗子树最右边的节点记做 last

        2.1 last.right 为 null，那么将 last.right = cur，更新 cur = cur.left

        2.2 last.right 不为 null，说明之前已经访问过，第二次来到这里，表明当前子树遍历完成，保存 cur 的值，更新 cur = cur.right
    */
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer>ans = new ArrayList<Integer>();
        
        TreeNode cur = root;
        while(cur!=null){
            if(cur.left == null){
                ans.add(cur.val);
                cur = cur.right;
            }else{
                TreeNode last = cur.left;
                while(last.right != null && last.right != cur){
                    last = last.right;
                }
                
                if(last.right == null){
                    last.right = cur;
                    cur = cur.left;
                }else{
                    if(last.right == cur){
                        ans.add(cur.val);
                        cur = cur.right;
                    }
                }
            }
            
        }
        return ans;
        
        
    }
}
