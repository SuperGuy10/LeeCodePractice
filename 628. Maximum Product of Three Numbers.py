'''
Tag: Array; Difficulty: Easy.
Given an integer array, find three numbers whose product is maximum and output the maximum product.
Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''
'''
For this question, there is no trick on code. You have to think it clearly before you program.
Since the range of nums is [-1000,1000], if we want the biggest product, we have to choose the biggest three numbers.
Be careful, there are negative nums, so we need to check wether the product of two negative mums and a positive num is
larger or the product of all the three positive nums.
If we sort the array, the two smallest nums is the nums[0] and nums[1], no matter they are both negative or positive or one each other.
The largest three positive numbers are the last three in this array.
'''

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
