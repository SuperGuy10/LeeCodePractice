"""
Given an array of 2n integers,
your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., 
(an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
        

"""
For this question, it require for the understanding of sum(), sorted(), or list.sort() and Slice List in Python.
It also can be write like this way:
"""

def arrayPairSum(nums):    
        sum = 0
        nums.sort()
        for i in range(0, len(nums), 1): #"1" can be ignored
            if i % 2 == 0:
                sum = sum + nums[i]
        return sum
