/**
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer>map = new HashMap<>();
        for(int i=0; i< inorder.length; i++){
            map.put(inorder[i], i);
        }
        
        return helper(preorder, 0, preorder.length, inorder, 0, inorder.length, map);
        
    }
    
    public TreeNode helper(int[] preorder, int pstart, int pend, int[] inorder, int istart, int iend, Map<Integer, Integer>map){
        if(pstart == pend){
            return null;
        }
        TreeNode root = new TreeNode(preorder[pstart]);
        
        int i_root_index = map.get(root.val);
        
        int leftnum = i_root_index - istart;
        
        root.right = helper(preorder, pstart+leftnum+1, pend, inorder,i_root_index+1, iend, map);
        root.left = helper(preorder, pstart+1, pstart+leftnum+1, inorder, istart, istart+leftnum, map);
        return root;
        
    }
}
