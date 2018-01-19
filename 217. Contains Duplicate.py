'''
Tag: Array; Difficulty: Easy.
Given an array of integers, 
find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array
and it should return false if every element is distinct.
'''


'''
The first solution is to use a normal way to think about the problem.
'''
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        """
      
        dic ={}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1
        return False
        

'''
The second way is to use set() function which is a very easy way to solve this problem
'''
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        """
 
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
