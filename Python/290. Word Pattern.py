'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
# Same idea with 205. Isomorphic Strings

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        A = set(zip(pattern, str.split(' ')))
        B = set(zip(str.split(' '), pattern))
        print(A,B)
        print(len(str.split(' ')))
        
        if len(pattern) != len(str.split(' ')):
            return False
        elif len(A) == len(set(pattern)) and len(B) == len(set(str.split(' '))):
            return True
        else:
            return False


'''
More concise way.
'''

class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
