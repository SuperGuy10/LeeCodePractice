'''
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
'''

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        S = list(range(-K+min(A),K+min(A)+1))
        B = list(range(-K+max(A),K+max(A)+1))
        if S[-1] in B or B[0] in S:
            return 0
        return min(B)-max(S)
        
        
# Easy solution
class Solution(object):
    def smallestRangeI(self, A, K):
        return max(0, max(A) - min(A) - 2*K)
