'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], 
and we repeat this process K times in total.  (We may choose the same index i multiple times.)
Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].

Example 2:
Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:
Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
'''

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        re = 1
        while re <= K:
            A = sorted(A)
            A[0] = -A[0]
            re += 1
        return sum(A)
        
'''
faster way
'''
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        sign = [v < 0 for v in A]
        L = sum(sign)
        if(L >= K):
            for i in range(K):
                A[i] = -A[i]
            return sum(A)
        else:
            for i in range(L):
                A[i] = -A[i]
            if( (K-L)%2 != 0 ):
                A.sort()
                A[0] = -A[0]
            return sum(A);
