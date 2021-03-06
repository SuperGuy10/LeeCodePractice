'''
The set S originally contains numbers from 1 to n. But unfortunately, 
due to the data error, one of the numbers in the set got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. 
Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
'''

'''
Version 1 is too slow but worked.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = []
        result = []
        for i in nums:
            if i in seen:
                result.append(i)
            else:
                seen.append(i)
        for n in range(1,len(nums)+1):
            if n not in nums:
                result.append(n)
        
        return result
                


'''
faster solution with set() and save storing space.
'''

class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        basket = set()
        output = []
        for i in nums:
            if i in basket:
                output.append(i)
            else:
                basket.add(i)
        for j in range(1, len(nums)+1):
            if j not in basket:
                output.append(j)
        return output

'''
Don't forget it is about numbers, use what numbers for.
'''

class Solution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]
