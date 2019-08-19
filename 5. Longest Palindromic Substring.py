'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if not s:
            return s
        for i in range(len(s)):
            j = i+1
            # j should not over len(s)
            while len(s[i:])>len(res) and j <=len(s):
            #sub s[i:] should longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j])>len(res):
                    res = s[i:j]
                j+=1
        return res
'''
for the first solution, didn't add requirement of this: "len(s[i:j])>len(res)", 
cause only update res when the new sub longer than res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if not s:
            return s
        for i in range(len(s)):
            j = i+1
            while len(s[i:])>len(res) and j <=len(s):
                if s[i:j] == s[i:j][::-1]:
                    res = s[i:j]
                j+=1
        return res
'''

'''
DP O(n^2) O(n^2)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s)<2:
            return s 
        dp = [[False for c in range(len(s))]for r in range(len(s))]
        res = ""
        count = 0
        for j in range(1,len(s)):
            for i in range(j+1):
                dp [i][j] = s[i]==s[j] and ((j-i<=2) or dp[i+1][j-1])
                if dp[i][j]:
                    if j-i+1>count: #!!!have to be j-i+1!!!!
                        count = j-i+1
                        res = s[i:j+1]
        return res


#solution 2 didn't figure out yet O(n)

class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
        
'''
DP solution
'''
dp = [[0] * len(s) for i in range(len(s))]
    ans = ""
    max_length = 0
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1] == 1):
                dp[i][j] = 1
                if ans == "" or max_length < j - i + 1:
                    ans = s[i:j+1]
                    max_length = j - i + 1
    return ans


'''
middle to ends solution
'''
if s == '':
            return ''
        
        length = 0
        start = 0
        end = 0
        
        def rec(string, left, right):
            while(left >= 0 and right < len(string) and string[left] == string[right]):
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            len1 = rec(s, i, i)
            len2 = rec(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > length:
                length = max_len
                start = i - (length-1)//2
                end = i + length//2
        
        return s[start:end+1]
    

