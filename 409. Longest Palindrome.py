'''
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

'''
At the beginnig, a wrong idea is only caltulate the even numbers character. Turns out that for odd numbers, we only need to ruduce one 
which will become an even number. And be careful with special case: no odd number and only odd numbers.
But all those special situations can be solved with a flag and -1 for odd number
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        flag = False
        #odd = []
        result = 0
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for key in dic:
                
            if dic[key] % 2 == 0:
                result += dic[key]
            else:
                flag = True
                result += dic[key]-1
                #odd.append(dic[key])
                
        if flag == True:    
            return result + 1
        else:
            return result
            
'''
use set
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
        
