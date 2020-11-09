'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

'''
Concept:
If we take XOR of zero and some bit, it will return that bit
a ⊕ 0 = a⊕0=a
If we take XOR of two same bits, it will return 0
a⊕a=0
a ⊕ b ⊕ a=(a⊕a)⊕b=0⊕b=b
So we can XOR all bits together to find the unique number.
Complexity Analysis

Time complexity : O(n) We only iterate through nums, so the time complexity is the number of elements in nums.
Space complexity : O(1).
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
    
    # using first index to store answer
    
    
