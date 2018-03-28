'''
Tag: Array; Difficulty: Easy.

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

'''
Solution 1 is too slow because of the process of list. However, we don't need to take care of the list at all.
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        temp = nums[0]
        for n in nums[1:]:
            
            if n == temp:
                nums.remove(n)
            else:
                temp = n
        return len(nums)

'''
Solution 2:
The only thing we need is the length, so we only need to count that.
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        temp = 0 
        for i in range(1,len(nums)):
            if nums[i] != nums[temp]:
                nums[temp+1] = nums[i]  
                temp +=1
        return num+1
    
