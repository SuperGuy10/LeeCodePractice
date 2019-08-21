'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

#DP solution: how does this idea come???

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
        

#backtracking "DFS" solution
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(string, left, right):
            if len(string) == 2*n:
                res.append(string)
            if left < n:
                backtrack(string+"(", left+1, right)
            if right < left:
                backtrack(string+")", left, right+1)
            return string
        
        backtrack("", 0, 0)
        
        return res
