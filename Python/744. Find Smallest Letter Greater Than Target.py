'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
'''


'''
use ASCII code to compare letters.
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        new = []
        tar = ord(target)
        print(tar)
        for i in letters:
            new.append(ord(i))
        
        for i in sorted(new):
            if i > tar:
                return chr(i)
                break
        return letters[0]


'''
turns out can compare letters directly.
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0] # If not found
        
 '''
 binary search
 '''
 
 class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]: 
            return letters[0]
        l, r = 0, len(letters) - 1
        while l < r:
            m = (l+r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[l]
