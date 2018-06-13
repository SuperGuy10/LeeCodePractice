'''
Tag: Array; Difficulty: Easy.
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3; Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1; Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {}
        for i, num in enumerate(nums):
            if num in h and i - h[num] <= k:
                return True
            h[num] = i
        return False
        
'''
for this solution, h{} is a dic to store the previous items order. since we need to
find out i - h[num] <= k, so we need to update h[num] = i, otherwise the difference will
becomes bigger and bigger.
enumerate is a dic that gives you order and value
'''
