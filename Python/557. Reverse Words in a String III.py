'''
Tag: String; Difficulty: Easy
Given a string, you need to reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in s.split():
            result += i[::-1] + " "
        return result[:-1]
        
        
'''
one line solution
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return " ".join([i[::-1] for i in s.split()])
