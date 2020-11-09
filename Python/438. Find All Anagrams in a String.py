'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

'''
Use counter with sliding window method.
'''
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n-1])
        index = 0
        for index in xrange(n - 1, m):
                sCounter[s[index]] += 1
                if sCounter == pCounter:
                    answer.append(index - n + 1)
                sCounter[s[index - n + 1]] -= 1
                if sCounter[s[index - n + 1]] == 0:
                    del sCounter[s[index - n + 1]]
        return answer

'''
Use double pointer with sliding window
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count = collections.Counter()
        M, N = len(s), len(p)
        left, right = 0, 0
        pcount = collections.Counter(p)
        res = []
        while right < M:
            count[s[right]] += 1
            if right - left + 1 == N:
                if count == pcount:
                    res.append(left)
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            right += 1
        return res
