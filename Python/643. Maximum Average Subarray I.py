'''
Tag: Array; Difficulty: Easy.
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
And you need to output the maximum average value.
Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''

'''
For this question, I firstly use sum[n:n+k] to compare with MaxSum but that took to much time.
After observating the list, it deletes the first item and add the next item to the previous three.
The speed of calculation has improved a lot which is beyond my imagination.
'''
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        MaxSum = sum(nums[:k])
        temp = MaxSum
        for n in range(len(nums)-k):
            temp = temp - nums[n] + nums[n+k]
            if temp>MaxSum:
                MaxSum = temp
        return MaxSum/k
