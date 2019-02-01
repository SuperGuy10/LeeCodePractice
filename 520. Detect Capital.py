'''
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
'''

'''
for the first solution, use the build-in function word.lower() and word.upper, and also can use
word.istitle
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word or word.lower() == word:
            return True
        elif word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            return True
        else:
            return False

'''
for the second solution, use dictionary and math to calculate the value.
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        capital = {"A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
        uncapital = {"a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
        count = 0
        i = 0
        if word[0] in capital:
            count = 100
            while i < len(word):
                if word[i] in capital:
                    count+=10
                    i+=1
                elif word[i] in uncapital:
                    count+=1
                    i+=1
        if count == 109+len(word):
            return True
        elif count == 100+10*len(word):
            return True
        elif count == len(word):
            return True
        else:
            return False
        print(count)
