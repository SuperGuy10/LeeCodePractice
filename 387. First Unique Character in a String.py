'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for m in range(len(s)):
            t = s[m]
            if dic[t] == 1:
                return m
            
        return -1


'''
solution 2
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        return min([s.index(i) for i in letters if s.count(i) == 1] or [-1])
