'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = [a,b]
        return sum(l)



'''
Idea:
Adding two integers a and b (no matter positive or negative) can always be boiled down into 3 steps:
convert a and b into two's complements.
add both two's complements. The result is a new two's complement
convert the result back to integer
Two things to note:

In Python, every integer is associated with its two's complement and its sign. However, 
doing bit operation "& mask" loses the track of sign. 
For example, -1 & 0xffffffff becomes a huge positive number 4294967295. 
Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
The magic is that if there is a negative integer n, and its unsigned 32-bit two's complement is m, 
then m = ~(n ^ 0xffffffff) and n = ~(m ^ 0xffffffff). So using this magic, you can do the conversion in step 3.
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
