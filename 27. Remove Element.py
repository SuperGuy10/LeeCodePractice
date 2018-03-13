'''
Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
'''

'''
Solution 1:
The cleanest way to remove elements in list is list.remove(item), 
quite close to list.pop(item_index) 
they do the same, it depends if you have either the item or its index

Pay attention: because we're modifying a list as iterating over it, it may not go through every item.
we should make a copy of the list and iterate over that.
'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for n in nums[:]:
            if n == val:
                nums.remove(n)
                
        return len(nums)

'''
Solution 2:
'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
