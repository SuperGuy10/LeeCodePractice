/**
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20
1 <= k <= n
*/

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>>ans = new ArrayList<List<Integer>>();
        backtrack(1, n, k, new ArrayList<Integer>(), ans);
        return ans;
    }
    
    public void backtrack(int start, int n, int k, ArrayList<Integer> tmp, List<List<Integer>>ans ){
        if(tmp.size()==k){
            ans.add(new ArrayList(tmp));//remember have to be new ArrayList otherwise will be all the same reference
            return;
        }
        for(int i = start; i<=n-(k-tmp.size())+1; i++){//i<=n slower than this
            tmp.add(i);
            backtrack(i+1, n, k, tmp, ans);
            tmp.remove(tmp.size()-1);
        }
        
    }
}
