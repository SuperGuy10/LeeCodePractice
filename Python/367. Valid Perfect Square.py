'''
Given a positive integer num, 
write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

# two pointer
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        
        while l <= r:
            m = (l+r)//2
            if m**2 < num:
                l = m+1
            elif m**2 > num:
                r = m-1
            else:
                return True
        return False
        
#Using Newton's Method

    def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num


#Math Trick for Square number is 1+3+5+ ... +(2n-1)
    
    def Math(self, num):
        i = 1
        while (num>0):
            num -= i
            i += 2       
        return num == 0
