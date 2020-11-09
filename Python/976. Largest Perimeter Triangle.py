'''
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, 
ormed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.

Example 1:
Input: [2,1,2]
Output: 5

Example 2:
Input: [1,2,1]
Output: 0

Example 3:
Input: [3,2,3,4]
Output: 10

Example 4:
Input: [3,6,2,3]
Output: 8

Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6
'''

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        l = len(A)
        if l < 3:
            return 0
        while l >= 3:
            if A[l-2] + A[l-3] > A[l-1]:
                return sum(A[l-3:l])
            else:
                l -= 1
        return 0
        
        
'''
Need to figure out
'''

class Solution:
    def largestPerimeter(self, A):
        A.sort()
        return ([0] + [a + b + c for a, b, c in zip(A, A[1:], A[2:]) if c < a + b])[-1]
