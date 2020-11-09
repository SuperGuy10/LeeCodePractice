'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution(object):
    def reverseVowels(self, s):
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
        return ''.join(s)

'''
using set(list)  is much faster than using list or array.
string can't do an in-place change. Use list to do that.
'''

class Solution(object):
    def reverseVowels(self, s):
        vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
        return ''.join(s)
