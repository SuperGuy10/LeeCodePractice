'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

'''
Solution1:
Runtime: 460 ms, faster than 5.38% of Python3 online submissions for Add Strings.
Memory Usage: 13.3 MB, less than 5.83% of Python3 online submissions for Add Strings.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def toInt(string):
            num = 0
            for i in range(len(string)):
                num += int(string[i])*10**(len(string)-1-i)
            return num
        
        return str(toInt(num1)+toInt(num2))
        

'''
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
