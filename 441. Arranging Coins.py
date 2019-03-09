'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
'''

# Solution 1 works but slow.
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = 2
        s = 1
        if n <2:
            return n
        
        while s <= n:
            s += r
            if s < n:
                l+=1
                r+=1
            if s == n:
                return r
        return l

'''
why total = mid*(mid+1)//2 ???
'''
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while end >= start:
            mid = (start+end)//2
            total = mid*(mid+1)//2
            if total == n:
                return mid
            elif total<n:
                start = mid + 1
            else:
                end = mid - 1
        return end


'''
The Coins are arranged in the following way:
[1,2,3,4,5....]
This is an arithmetic sequence. To find the sum S of an arithmetic series , the formula is :
S = ((a + b)* h) /2
Where:
a is the number of coins on the first line
b is the number of coins of the last line
h is the number of lines we have (we want to find h)
We note that a is always 1 because we start with one coin
Therefore a = 1
Note that the number of coins on the last line is always the same as the the number of total lines.
Therefore: b = h
The equation can then be simplified into:
S = (1 + h)*h / 2
Since we want only full lines, we want the sum S to be smaller than n, the total amount of coins in the question.
Therefore:
(1 + h)*h / 2 <= n
Which simplifies into:
h^2 + h <= 2n
Or:
h^2 + h - 2n <= 0
This can be solved using the quadratic formula: (note that a and b here are different from a and b before)
ax^2 + bx + c = 0
x = -b - sqrt(b^2 - 4ac) / 2a
x = -b + sqrt(b^2 - 4ac) / 2a
In our case:
a = 1, b = 1, c = -2n
which yields:
h ≤ (sqrt(8n + 1) -1)/2
h ≥ (-sqrt(8n + 1) -1)/2
Since n >= 1, and negative values of h are irrelevent, we can ignore the second equation. (It simply requires h > 0)
Finally, the code is simply:
'''

import math
class Solution(object):
def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    #int is simply to floor the floating point so we get the largest integer smaller than the expression
    return int((math.sqrt(8 * n + 1)-1)/2)
    
