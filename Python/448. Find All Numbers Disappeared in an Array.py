'''
Tag: Array; Difficulty: Easy.
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
'''

'''
This question asks for no exteral space and  O(n) running time.
To avoid extral space, this can be thought as compare two the original list with it's index.
If the index appear in that array, make the value of that index negative.
Finally return the index with positive values plus one.
'''

class Solution:
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = nums.copy()
        for i in range(len(nums)):
            if (i+1) not in nums:
                l[i] = -l[i]
        return [i + 1 for i in range(len(l)) if l[i] < 0]


'''
For the same idea, second solution:
'''
class Solution:
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            val = nums[i]
            if val < 0:
                val = -val
            val -= 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        r = []
        for i in range(len(nums)):
            if nums[i] > 0:
                r.append(i + 1)
        return r

'''
For third solution, to use the build in function "set"
set is implemented using a hash, so the lookup is, on average, close to O(1). 
The worst case is O(n), where n objects have colliding hashes.
Pay attention, range() include left but not right.
When doing minus process, items in list A - B then return what left in A
'''
class Solution:
  
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1,len(nums)+1)) - set(nums))
