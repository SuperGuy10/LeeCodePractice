'''
Tag: Array Difficulty: Easy

Given a binary array, find the maximum number of consecutive 1s in this array.
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

'''
For this question, we need to calculate the appearing times. Since it only ask for count 1s, so we can just use list to store.
The key for this question is to reset the count once it appears 0.
For my own method, I use one for loop to go through the list and append them into a new list.
One tiny problem of my method is it will append count = 0 to the list.
Although it won't affect the result, feel uncomfortable.
This program beat 66.23%
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        count = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)       
        
 '''
 For the faster methon, the logic is really clearly and straightforward.
 '''
 
 class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, max_count = 0, 0
        for num in nums:
            count = count + 1 if num == 1 else 0
            if count > max_count: max_count = count
        return max_count
 
