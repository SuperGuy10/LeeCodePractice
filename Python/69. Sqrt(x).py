'''
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(x**0.5)
        l = 0
        r = x
        while l <= r:
            m = (l+r)//2
            if m**2 <= x < (m+1)**2:
                return m
            elif m**2 > x:
                r = m
            else:
                l = m+1

# Newton's methond
class Solution:
    def mySqrt(self, x: int) -> int:
        i=1.0;
        while(True):
            j=(i+x/i)/2.0;
            if(abs(i-j)< 0.000000000005):
                break;
            i=j;
        return int(j);
