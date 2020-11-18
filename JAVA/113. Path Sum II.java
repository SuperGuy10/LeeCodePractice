/**
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
 
//     Solution 1: 
//     public List<List<Integer>> pathSum(TreeNode root, int sum) {
//         List<List<Integer>>ans = new ArrayList<>();
//         helper(root, sum, new ArrayList<Integer>(), ans);
//         return ans;
//     }
    
//     public void helper(TreeNode root, int sum, List<Integer>path, List<List<Integer>>ans){
//         if(root == null){
//             return;
//         }else{
//             path.add(root.val);
//         }
//         //if(root.left==null && root.right == null){
//         if(root.left==root.right){
//             int tmp = 0;
//             for(Integer i : path){
//                 tmp+=i;
//             }
//             if(tmp == sum){
//                 ans.add(new ArrayList<Integer>(path));
//             }
            
//         }
        
//         helper(root.left, sum, path, ans);
//         helper(root.right, sum, path, ans);
//         path.remove(path.size()-1);
//     }
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>>ans = new ArrayList<>();
        helper(root, sum, new ArrayList<Integer>(), ans);
        return ans;
    }
    
    public void helper(TreeNode root, int sum, List<Integer>path, List<List<Integer>>ans){
        if(root == null){
            return;
        }else{
            path.add(root.val);
        }
        //if(root.left==null && root.right == null){
        if(root.left==root.right){
            
            if(root.val == sum){
                ans.add(new ArrayList<Integer>(path));
            }
            
        }
        
        helper(root.left, sum-root.val, path, ans);
        helper(root.right, sum-root.val, path, ans);
        path.remove(path.size()-1);
    }
}
