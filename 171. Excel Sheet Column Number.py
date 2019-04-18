'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        s = list(s)
        dic = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,
               "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,
               "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,
               "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
        res = 0
        for i in range(len(s)):
            res += dic[s[i]]*26**(len(s)-1-i)
        return res

#Solution 2
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans  = ans*26 + (ord(c) - ord('A') + 1)
        return ans

#Solution 3
class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(char) - 64) * (26 ** exp) for exp, char in enumerate(s[::-1]))
