'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
'''

'''
For this question, the key point is that it has to have at leas two "l"s and two "o"s and at one of each of the rest letters
so we only need to think about 2 situations: 
1: number of min("l" or "o") is greater or equal to two times of the number of min(b, a, n)
2: number of min("l" or "o") is less than two times of the number of min(b, a, n)

if situation 1 is true: then just return the number of min(b, a, n)
if situation 2 is true: then return min(dic["l"], dic["o"])//2

but we have to have all the letters, so if any of them is 0, we can not make a balloon, return 0
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for i in text:
            if i in dic:
                dic[i] += 1
        if min(dic.values()) == 0:
            return 0
        elif min(dic["l"], dic["o"]) / min(dic["b"], dic["a"], dic["n"]) >= 2:
            return min(dic["b"], dic["a"], dic["n"])
        else:
            return min(dic["l"], dic["o"])//2
