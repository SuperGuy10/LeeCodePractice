/**
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
//     public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
//         List<List<Integer>> ans = new ArrayList<List<Integer>>();
//         if(root == null){
//             return ans;
//         }
//         int count = 1;
//         Queue<TreeNode> level = new LinkedList<>();
//         level.offer(root);
//         while(!level.isEmpty()){
//             List<Integer>tmp = new ArrayList<Integer>();
//             int s = level.size(); //do not put in for loop condition directly. it changes every time.
//             for(int i=0; i<s; i++){
                
//                 TreeNode cur = level.poll();
//                 if(cur.left != null){
//                     level.offer(cur.left);
//                 }
//                 if(cur.right != null){
//                     level.offer(cur.right);
//                 }
//                 tmp.add(cur.val);
//             }
//             if(count%2==0){
//                 Collections.reverse(tmp);
//             }
//             ans.add(tmp);
//             count++;
//         }
        
//         return ans;
        
//     }
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(root == null){
            return ans;
        }
        int count = 1;
        Queue<TreeNode> level = new LinkedList<>();
        level.offer(root);
        while(!level.isEmpty()){
            List<Integer>tmp = new ArrayList<Integer>();
            int s = level.size(); //do not put in for loop condition directly. it changes every time.
            for(int i=0; i<s; i++){
                
                TreeNode cur = level.poll();
                if(cur.left != null){
                    level.offer(cur.left);
                }
                if(cur.right != null){
                    level.offer(cur.right);
                }
                if(count%2!=0){
                    tmp.add(cur.val);
                }else{
                    tmp.add(0, cur.val);//to avoid reverse list.
                }
            }
            
            ans.add(tmp);
            count++;
        }
        
        return ans;
        
    }
     
}
