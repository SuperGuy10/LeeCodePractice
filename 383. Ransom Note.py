'''

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if  magazine.count(i) < ransomNote.count(i):
                return True
        return False
        
        
'''
solutioni 2
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_count = {}
        mag_count = {}
        
        for c in ransomNote:
            if c not in ransom_count:
                ransom_count[c] = 1
            else:
                ransom_count[c] += 1
        
        for c in magazine:
            if c in ransom_count:
                ransom_count[c] -= 1
                if ransom_count[c] == 0: del ransom_count[c]
        
        if not ransom_count:
            return True
        return False
