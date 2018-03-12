'''
Tag: Array; Difficulty: Easy.
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tem = 1
        longest = 0
        if nums == []:
            return 0
        for n in range(1, len(nums)):
            if nums[n]>nums[n-1]:
                tem += 1
            else:
                longest = max(longest, tem)
                tem = 1
		
        longest = max(longest, tem)
        return longest

'''
for this question, need to pay attention on index of arry.
if we use n+1 > n to judge, the index will overflow. Instead, useing n>n-1.
and every time set the tem back to 1
'''
