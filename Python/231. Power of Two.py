'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
'''

# Bits count
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        return bin(n).count("1") == 1
        
# Bits operation
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n&(n-1)


# Math way
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n%2 == 0:
            n = n/2
        return n == 1
