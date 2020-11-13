/**
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
*/



class Solution {
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>>ans = new ArrayList<>();
        Arrays.sort(nums);
       
        for(int l = 0; l<=nums.length; l++){
            backtrack(0, nums, l, new ArrayList<Integer>(), ans);
        }
        return ans;
        
    }
    
    public void backtrack(int start, int[] nums, int length, 
                          ArrayList<Integer> tmp, List<List<Integer>> ans){
        if(tmp.size() == length){
            ans.add(new ArrayList<Integer>(tmp));
            return;
        }else if(tmp.size()<length){
            
            for(int i = start; i<nums.length; i++){
                if(i>start && nums[i] == nums[i-1]){ 
                    continue;
                }
        
                tmp.add(nums[i]);
                backtrack(i+1, nums, length, tmp, ans); // !!!attention: i+1 not start +1;
                tmp.remove(tmp.size()-1);
            }
        }
    }
//     public List<List<Integer>> subsetsWithDup(int[] nums) {
//         List<List<Integer>>ans = new ArrayList<>();
       
        
//         backtrack(0, nums, new ArrayList<Integer>(), ans);
        
//         return ans;
        
//     }
    
//     public void backtrack(int start, int[] nums, ArrayList<Integer> tmp, List<List<Integer>> ans){
        
//             ans.add(new ArrayList<Integer>(tmp));
    
//             for(int i = start; i<nums.length; i++){
//                 if(i>start && nums[i] == nums[i-1]){
//                     continue;
//                 }
        
//                 tmp.add(nums[i]);
//                 backtrack(i+1, nums, tmp, ans);
//                 tmp.remove(tmp.size()-1);
//             }
//     }
}
