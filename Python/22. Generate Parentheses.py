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

'''
DP solution: how does this idea come???
For each valid parenthesis, there must be a pair whose right parenthesis is at the rightmost location. 
Thus, a valid parenthesis has to be of the following form:  * ( * )
where * denotes the remaining parentheses which are don't yet know (* can be empty, i.e., with 0 pair of parenthesis). 
However, we do know the following two important facts:
both two * are valid parentheses;
they don't overlap at all! (a pair has to be either on the left side or inside (), 
but cannot be the case where ( is on the left side and ) is inside ())
If we put i parentheses inside (), there are n-i-1 to be put on the left side. This gives us a recursive formula as below:

P(n) = P(n-i-1) x P(i)
where P(n) are all valid parentheses with n parentheses.
'''
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
