'''
Tag: Array, Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

'''
This is a very tricky question.
When I got this question, I thought it's simple. I just simply went through every item in that list and delete every item equal to 0,
then append it at the end of the list. Turns out I had index problems such as index over range or the mised 0 inside the list.
Then I found out the first solution to avoid that problem.
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """       
        for n in range(len(nums)):
            if nums[n]==0:
                nums.remove(nums[n])
                nums.append(0)
                n-=1
  
'''
for the Second solution, using the slicing of a list, but backward way so we can easily to avoid index problem
'''
        
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """            
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.append(nums[i])
                del nums[i]


'''
For the third solution, it's kind of using two pointer go through the list, when the first pointer point to nonzero item,
save to the second pointer, then both pointers move one step further.
Untill the first point met the end of the list, set all the rest step of second pointer to 0.
'''     
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """    
        m = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[m] = nums[n]
                m += 1
        for i in range(m, n+1):
            nums[i] = 0
            
'''
Compare to all the three solutions, the first one is the slowest one. The I found out "del" is faster than "remove".
'''
