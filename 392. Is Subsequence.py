'''
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''

#Solution1:
#This is the wrong answer but correct idea
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in s:
            if i in t[start:]:
                start = t.index(i) #chage to: start = start+ t[index:].index(i)+1
            else:
                return False
                
        return True

#Solution2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            idx = t.find(i)
            if idx == -1:
                return False
            else:
                t = t[idx+1:]
                
        return True
                
