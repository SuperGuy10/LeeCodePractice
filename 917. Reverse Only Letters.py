'''
Tag: String; Difficulty: Easy
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
'''

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        reverse = [i for i in S if i.isalpha()][::-1]
        print(reverse)
        
        result = ""
        
        for m in S:
            if not m.isalpha():
                result += m
            else:
                result += reverse.pop(0)
            
        return result
        
        
'''
solution2
'''
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
    
        place = []
        others = []
        for i, c in enumerate(S):
            if not c.isalpha():
                place.append((i,c))
            else:
                others.append(c)
        others = others[::-1]
        new = [None]*(len(others) + len(place))
        
        for i, c in enumerate(new):
            if len(place) != 0:
                ind,c = place[0]
                if ind == i:
                    place.pop(0)
                    new[i] = c
                else:
                    new[i] = others.pop(0)
            else:
                new[i] = others.pop(0)
        return "".join(new)
        
