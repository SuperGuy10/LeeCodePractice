'''
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]
 

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true
 
Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000 
'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        j = len(A)-1
        n = len(A)
        
        while i < j and A[i] < A[i+1]:
            i += 1
        while j>0 and A[j]<A[j-1]:
            j -= 1
        
        return 0<i==j<n-1

       
# Solution 2
class Solution:
    def validMountainArray(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return False
        descending = False
        if A[0] >= A[1]:
            return False
        prev = A[0]
        for i in A[1:]:
            if i < prev:
                if not descending:
                    descending = True
            elif i > prev:
                if descending:
                    return False
            else:
                return False
            prev = i
        return descending
