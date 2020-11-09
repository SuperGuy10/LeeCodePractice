'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        res, carry = [], 0
        while a or b:
            n1 = n2 = 0
            if a: n1 = int(a.pop())
            if b: n2 = int(b.pop())
            
            tmp = n1 + n2 + carry
            carry = 0
            if tmp == 1 or tmp == 0:
                res.append(tmp)
            elif tmp == 2:
                res.append(0)
                carry += 1
            else:
                res.append(1)
                carry += 1
        if carry:
            res.append(carry)
        return ''.join(str(d) for d in res)[::-1]
        
        
'''
one line
'''

def addBinary(self, a, b):
    return '{:b}'.format(int(a,2)+int(b,2))
