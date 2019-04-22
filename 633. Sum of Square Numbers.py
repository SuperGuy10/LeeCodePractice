'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 
Example 2:
Input: 3
Output: False
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr = set()
        for i in range(int(c**0.5)+1):
            sqr.add(i**2)
        for j in sqr:
            if c-j in sqr:
                return True
        return False

# Solution 2
class Solution:
    def judgeSquareSum(self, c):
        low, high = 0, int(c**0.5)
        while low <= high:
            ssum = low * low + high * high
            if ssum == c:
                return True
            elif ssum > c:
                high -= 1
            else:
                low += 1
        return False
