'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)
        i = set(a[2::2])
        j = set(a[3::2])
        print(i,j)
        if n ==1:
            return True
        if len(i) == len(j) and i != j:
            return True
        return False
        
'''
clever
'''

class Solution:
     def hasAlternatingBits(self, n):
        s = bin(n)
        return '00' not in s and '11' not in s
        
'''
moving bits
'''

class Solution:
    def hasAlternatingBits(self, n):
        if not n:
            return False
        num = n ^ (n >> 1)
        return not (num & (num + 1))
