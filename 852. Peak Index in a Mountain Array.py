'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:
Input: [0,1,0]
Output: 1

Example 2:
Input: [0,2,1,0]
Output: 1

Note:
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
'''

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A)-1
        m = 0
        while l <= r:
            if max(A[l], A[r]) >= m:
                m = max(A[l], A[r])
            l += 1
            r -= 1
        return A.index(m)


'''
Real solution: watch out m, is based on every new L and R
'''
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        l = 0
        r = len(A)-1
        
        while l < r:
            m = (l+r)//2
            if A[m-1] < A[m] < A[m+1]:
                l = m+1
            elif A[m-1] > A[m] > A[m+1]:
                r = m-1
            else:
                l = m
                break
        
        if A[l-1] < A[l] > A[l+1]:
            return l
        else:
            return r
