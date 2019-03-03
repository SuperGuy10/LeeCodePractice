'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

xample 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        return collections.Counter(s) == collections.Counter(t)
        
# My solution        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
        
        #return sorted(s) == sorted(t)

# useing dicitonary
class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
 
        if len(s) != len(t):
            return False
        
        def letterStats(s: 'str') -> 'dict':
        
            hashmap = {}
            
            for letter in s:
                if letter in hashmap:
                    hashmap[letter] += 1
                else:
                    hashmap[letter] = 1
                    
            return hashmap
        
        if letterStats(s) == letterStats(t):
            return True
        else:
            return False
        
