'''
Tag: Array; Difficulty: Easy.
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5 Output: 2
Example 2:
Input: [1,3,5,6], 2 Output: 1
Example 3:
Input: [1,3,5,6], 7 Output: 4
Example 1:
Input: [1,3,5,6], 0
Output: 0

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for n in range(len(nums)):
            if target in nums:
                if nums[n] == target:
                    return n
            else:
                if target<nums[0]:
                    return 0
                if target > nums[-1]:
                    return len(nums)
                if nums[n]<target and target<nums[n+1]:
                    return n+1
                    
'''
Solution 2:
Binary Search
'''
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
