'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[[1,2,2],[5]]
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1,10))
        res = []
        combination = []
        self.findCombination(candidates, n, 0, res, combination, k)
        return res
        
    def findCombination(self, candidates, target, start, res, combination, size):
        if target < 0:
            return
        if target == 0 and len(combination)==size:
            res.append(combination)
        for i in range(start,len(candidates)): #pay attention on the start index
            if candidates[i] > target or len(combination) > size:
                break
            self.findCombination(candidates, target-candidates[i], i+1, res, combination+[candidates[i]], size)
