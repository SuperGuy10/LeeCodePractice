'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tem = 0
        res = []
        for i in range(len(digits)):
            tem+=digits[i]*10**(len(digits)-i-1)
        return[int(a) for a in str(tem+1)]
        

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits
