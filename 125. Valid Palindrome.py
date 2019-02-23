'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = ""
        for i in s.lower():
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                m += i
        print(m)
        if m.lower() == m.lower()[::-1]:
            return True
        return False
        
        
'''
'''
class Solution(object):
    def isPalindrome(self, str):
        """
        :type s: str
        :rtype: bool
        """
        processed=re.findall(r'\w+',str.lower())
        processed=''.join(processed)            
        n=len(processed)
        mid=n//2
        if n%2==0:
            if processed[:mid]==processed[mid:][::-1]:
                return True
            else: return False
        else:
            if processed[:mid]==processed[mid+1:][::-1]:
                return True
            else: return False
            
'''
re.sub()
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = re.sub('[\W_]+', '', s).lower()
        return chars == chars[::-1]
        
        
'''
two pointer
'''
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
