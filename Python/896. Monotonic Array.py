'''
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true
 
Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        if A[-1]-A[0]>0:
            i = 0
            while i < len(A)-1:
                if A[i+1] - A[i]<0:
                    return False
                i+=1
        if A[-1]-A[0]< 0:
            i = 0
            while i < len(A)-1:
                if A[i+1] - A[i]>0:
                    return False
                i+=1
        if A[-1]-A[0] == 0:
            if len(set(A))!=1:
                return False
        return True



#one pass solution
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
        
        
# one line solution
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # equal to CMP
        return not { (i>j)-(i<j) for i, j in zip(A, A[1:])} >= {1, -1}
