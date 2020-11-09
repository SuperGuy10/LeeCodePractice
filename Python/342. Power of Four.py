'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''

# my own solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        a = bin(num)
        if num <= 0:
            return False
        return a.count("1")==1 and a[3:].count("0") % 2==0

# updated own one line solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return bin(num).count("1")==1 and bin(num)[3:].count("0") % 2==0 and num>0

# same idea different way one line solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num&(num-1)==0 and len(bin(num)[3:])%2==0

# another solution
class Solution:
    def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
