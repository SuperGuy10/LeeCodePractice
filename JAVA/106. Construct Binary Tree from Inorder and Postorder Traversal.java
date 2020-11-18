/**
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer, Integer>map = new HashMap<>();
        for(int i=0; i<inorder.length; i++){
            map.put(inorder[i],i);
        }
        
        return helper(inorder, 0, inorder.length, postorder, 0, postorder.length, map);
        
    }
    
    public TreeNode helper(int[] inorder, int istart, int iend, int[] postorder, int pstart, int pend, Map<Integer, Integer>map){
        if(istart == iend || pstart==pend){
            return null;
        }
        
        int iRootIndex = map.get(postorder[pend - 1]); //boundry
        int leftNum = iRootIndex - istart;// don't forget: use iRootIndex-istart cause everytime starts different
        int rightNum = iend-leftNum-1;
        
        TreeNode root = new TreeNode(postorder[pend - 1]);
        
        root.left = helper(inorder, istart,iRootIndex, postorder, pstart, pstart+leftNum, map) ;
        root.right = helper(inorder, iRootIndex+1, iend, postorder, pstart+leftNum, pend-1, map);
        
        return root;
        
        
    }
}
