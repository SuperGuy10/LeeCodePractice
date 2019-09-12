'''
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), 
followed by some number of '1's (also possibly 0.)
We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
Return the minimum number of flips to make S monotone increasing.

Example 1:
Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 
Note:
1 <= S.length <= 20000
S only consists of '0' and '1' characters.
'''

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        count0 = S.count("0") #count the number of "0" before the first 1
        count1 = 0 #count the number of "1"
        
        res = len(S) - count0
        
        for i in range(len(S)):
            if S[i] == "0":
                count0 -= 1
            elif S[i] == "1":
                res = min(res, count0+count1)
                count1 += 1
                
        return res
       
'''       
solution 2 DP
Definition:
dp1[i]: min number of flips to make s[:i+1] to mono increasing by making s[i] to 1
dp0[i]: min number of flips to make s[:i+1] to mono increasing by making s[i] to 0
Transition function:
dp1[i] = min(dp1[i-1], dp0[i-1]) + (1 if s[i] == '0' else 0)
dp0[i] = dp0[i-1] + (1 if s[i] == '0' else 0)
Return:
min(dp0[-1], dp1[-1])
Since dp1[i], dp0[i] only relies on dp1[i-1] and dp0[i-1], the space complexity can be O(1)
'''

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S[0] == '0':
            dp1 = 1
        else:
            dp1 = 0
        
        if S[0] == '1':
            dp0 = 1
        else:
            dp0 = 0
        for i in range(1, len(S)):
            if S[i] == '0':
                dp0 += 0
                dp1 = min(dp1, dp0)+1
            else:
                dp1 = min(dp1, dp0)
                dp0 += 1
        return min(dp1, dp0)
