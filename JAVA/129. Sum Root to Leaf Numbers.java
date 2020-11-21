/**
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
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
//     public int sumNumbers(TreeNode root) {
//         return helper(root,0);
    
//     }
//     public int helper(TreeNode root, int tmp){
//         if(root == null){
//             return 0;
//         }
//         tmp = tmp*10 + root.val; 
//         if(root.left == null && root.right==null){
//             return tmp;
//         }
//         return helper(root.left, tmp) + helper(root.right, tmp);
        
        
//     }
    int sum = 0;
    public int sumNumbers(TreeNode root) {
        
        helper(root,0);
        return sum;
    
    }
    public void helper(TreeNode root, int tmp){ // sum can not be set as parameter for the helper method, it will be a class variable.
        if(root == null){
            return;
        }
        tmp = tmp*10 + root.val;
        if(root.left == root.right){
            sum+= tmp;
            return;
        }
        helper(root.left, tmp);
        helper(root.right, tmp);
        
    }
}
