'''
You are standing at position 0 on an infinite number line. There is a goal at position target.
On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:target will be a non-zero integer in the range [-10^9, 10^9].
'''

class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
        
        
#solution 2
class Solution(object):
    def reachNumber(self, target):
        # when target negative, reachNumber(target) == reachNumber(-target)
        t = abs(target)
        # try to find a number (called n) to satisfy 1+2+...+n = n*(n+1)/2 <= t
        n = int(math.sqrt(2*t+0.25)-0.5)
        # case 0: 1+2+...+n = n*(n+1)/2 == t
        # In this case, it is perfect
        if 2*t == n*(n+1):
            return n
        # case 1:
        # 1+2+...+n = n*(n+1)/2 < t
        # method 1:
        # try to find m (m>=n+1), make 1+2+...+m > t and (1+2+...+m-t) is even. so, we can select several numbers between 1 and m and
        # change the plus sign before them to negetive sign to make (1+2...-x+...-y+...) == t
        # so, in this way, the step number is m
        m = n+1
        while (m*(m+1)/2-t)%2==1:
            m += 1
        # method 2: (1) walk n steps from 0 to n*(n+1)/2 and then (2) walk to left and to right for (t-n*(n+1)/2) times.
        # because walking to left and then walking to right will move to right by one
        # in this way, we need 2 steps to move to right by one
        # we use this way to move from n*(n+1)/2 to t.
        # the total steps in this way is n+(t-n*(n+1)/2)*2
        # we need to choose smaller step numbers between method 1 and method 2
        return min(n+(2*t-n*(n+1)), m)
