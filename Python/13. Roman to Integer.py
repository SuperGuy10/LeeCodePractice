'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}


        res, p = 0, 'I'
        for c in s[::-1]:
            if d[p] > d[c]:
                res, p = res - d[c], c
            else:
                res, p = res + d[c], c
        return res
        
        
        
  '''
  '''
  class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "CD":400,
            "CM":900,
            "XL":40,
            "XC":90,
            "IV":4,
            "IX":9,
            "II":2,
            "III":3
            
        }
        length = len(s)
        i = 0
        num = 0
        while i < length:
            if(s[i] == 'M'):
                num += romanDict.get(s[i])
                i = i+1
                continue
            elif(s[i] == 'D'):
                num += romanDict.get(s[i])
                i = i+1
                continue
            elif(s[i] == 'C'):
                if(i+1 < length and s[i+1] in ['D', 'M']):
                    num += romanDict.get(s[i:i+2])
                    i = i+2
                    continue
                else:
                    num+= romanDict.get('C')
                    i = i+1
                    continue
            elif(s[i] == 'L'):
                num+= romanDict.get('L')
                i = i+1
                continue
            elif(s[i] == 'X'):    
                if(i+1 < length and s[i+1] in ['L', 'C'] ):
                    num += romanDict.get(s[i:i+2])
                    i = i+2
                    continue
                else:
                    num+= romanDict.get('X')
                    i = i+1
                    continue
            elif(s[i] == 'V'):  
                num+= romanDict.get('V')
                i = i+1
                continue
            elif(s[i] == 'I'):
                if(i == length-1):
                    num+= romanDict.get(s[i])
                    i=i+1
                elif(i+1 < length and s[i+1] in ['V', 'X']):
                    num += romanDict.get(s[i:i+2])
                    i = i+2
                    continue
                else:
                    num+= romanDict.get(s[i:len(s)])
                    i = length
                    
        return num
  
