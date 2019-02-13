'''
Given a non-empty string check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)//2+1):#only need to check at most half items to find the repeatable part.
            if len(s)%i == 0  and int(len(s)/i)*s[:i] == s:
                return True
        return False

'''
Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

For some rookie like me, the above explanation might be a little confused. So I write a more detailed one.
Correctness prove:
what I want to prove is "if s can be constructed by repeating substring of itself, s should be in super_s.".
Thus, we suppose s can be constructed by repeating substring of itself -> s = np, p is the repeated substr, n is the repeated times.
And according to our assumption, we get n >= 2, len(p) >= 1.
Before removing, we get super_s = np+np.
After removing, we get super_s = (np-1) + (np-1). (why we need to remove? we will talk about later.)
Now, I want to prove super_s contain s.
super_s = (np-1) + (np-1) = (p-1) + (n-1)p + (n-1)p + (p-1) = (p-1) + (2n-2)p + (p-1)
About the middle part "(2n-2)p", because n >= 2, (2n-2) >= n.
Thus, (2n-2)p >= np. And s == np, finally we prove that super_s contains s.

    P.S.
    Why we need to remove first and last element of super_s?
            Our judgement is based on whether super_s contains s. Thus, is we don't remove the first and last elements, every super_s
            must contains s and has nothing to do with repetive substr. After removing, if super_s contains s, s has to have the substr
            that can constructing the s.
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        
        """
        if not s:
            return ""
        
        S = ( s + s )[1:-1]
        return S.find(s) != -1
        
