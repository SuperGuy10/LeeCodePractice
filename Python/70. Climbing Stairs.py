'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

'''
My own solution:
By analizing this questioin, 
we can figure out that the main idea to solve it is to find out how many combinations of 1 & 2 to make it equal to n.
There are three scenario, all 1s, all 2s(if n is even), 1s and 2s.
For example of n=5:
1, 1, 1, 1, 1 #include only 1s
2, 1, 1, 1 #include only one 2 at different positions
1, 2, 1, 1
1, 1, 2, 1
1, 1, 1, 2
2, 2, 1 #include two 2s at different positions
2, 1, 2
1, 2, 2

So we only need to calculate how many 2s we need to select from different number of positions
'''
import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n//2   # to caltulate how many 2s we can totally have within n
        result = 0  
        for i in range(r+1):  # i means how many 2s we chose for this round, it at most r 2s.
            b = n+i-2*i  # to find out how many positons for this round, since C(n,0）= 1， so doesn't matter what n is.
            result+=math.factorial(b)/(math.factorial(i)*math.factorial(b-i)) # C(b,i) = b! / ( i! * (b-i)!)
        return int(result) # sum all the result together
        
        
'''
Top-Down
'''
class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        res = [-1 for i in range(n)]
        res[0], res[1] = 1, 2
        return self.dp(n-1, res)
        
    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n - 1, res) + self.dp(n - 2, res)
        return res[n]
