'''

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''
For this question, we need to keep updating two variables, one is current sum, the other is max sum.
for curSum, check if it is greater than previous everytime.
for maxSum, check curSum if it is greater than before everytime.
it's kind of calculation of tow sum for cunSum, but only update when it is getting bigger.
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum += num
            if num  > curSum:
                curSum = num
            if curSum > maxSum:
                maxSum = curSum
            
        return maxSum
