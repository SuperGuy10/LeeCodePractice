'''
Tag: Array; Difficulty: Easy.
Given an integer array, 
you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

Hint:
Think of two list, one sorted, use two pointer one from head the other from tail.
Compare elements in two lists at the same postition.

'''
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        SL = sorted(nums)
        l = len(nums)
        LP = 0
        RP = 0

        for n in range(l):
            if nums[n] != SL[n]:
                LP = n
                break
        for n in range(l):
            if nums[l-1-n] != SL[l-1-n]:
                RP = l-n
                break
                
        return RP-LP
