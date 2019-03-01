'''
Given a List of words, return the words that can be typed using letters 
of alphabet on only one row's of American keyboard like the image below.
 
Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':

        keys = ["qwertyuiop","asdfghjkl", "zxcvbnm" ]
        res = []
        for word in words:
            w = word.lower()
            flag = True            
            if w[0] in keys[0]:
                for l in w[1:]:
                    if l not in keys[0]:
                        flag = False
                        break
            if w[0] in keys[1]:
                for l in w[1:]:
                    if l not in keys[1]:
                        flag = False
                        break
            if w[0] in keys[2]:
                for l in w[1:]:
                    if l not in keys[2]:
                        flag = False
                        break
            if flag == True:
                res.append(word)
       	return res
