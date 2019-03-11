'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        
        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i%2] = max(res[(i-1)%2], res[(i-2)%2] + nums[i])

        return max(res[0], res[1])
        
'''
'''
 class Solution:
        # @param num, a list of integer
        # @return an integer
        def rob(self, num):
            max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
            for cur in num:
                max_3_house_before, max_2_house_before, adjacent = \
                max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
            return max(max_2_house_before, adjacent)
