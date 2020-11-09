'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
Note:n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:3
Output:3

Example 2:
Input:11
Output:0
Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, (1,0), (1,1), ... is a 0, which is part of the number 10.
'''

class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])
        

'''
solution 2
How many digits of size size can we have?
1 * 9 (size 1, 1... 9)
2 * 90 (size 2, 10... 99)
3 * 900 (size 3, 100... 999)
So we can "fast-skip" those numbers until we find the size of the number that will hold our digit.
At the end of the loop, we will have:
start: first number of size size (will be power of 10)
n: will be the number of digits that we need to count after start
How do we get the number that will hold the digit? 
It will be start + (n - 1) // size (we use n - 1 because we need zero-based index).
Once we have that number, we can get the n - 1 % size-th digit of that number, and that will be our result.
'''
class Solution:
    def findNthDigit(self, n: 'int') -> 'int':
        #1-9:9 = 1*9*10^0
        #10-99:180 = 2*9*10
        #100-999:2700 = 3*9*10^2
        #1000-9999:36000 = 4*9*10^3
        n -= 1
        for digit in range(1, 11):
            first = 10**(digit - 1)
            if n < 9 * digit * first:
                return int(str(first + n // digit)[n % digit])
            n -= 9 * digit * first
