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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates.sort()
        #start = 0
        self.findCombination(candidates, target, combination, res, 0)
        return res
        
    def findCombination(self, candidates, target, combination, res, start):
        if target == 0 and combination not in res:
            res.append(combination)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if i > start and candidates[i] == candidates[i-1]:# to ignore the continuely same candidate.
                continue
            self.findCombination(candidates, target-candidates[i], combination+[candidates[i]], res, i+1)# since it can only show once, i+1
