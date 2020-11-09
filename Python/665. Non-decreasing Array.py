'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''


'''
As before, let pp be the unique problem index for which \text{A[p]} > \text{A[p+1]}A[p]>A[p+1]. If this is not unique or doesn't exist, 
the answer is False or True respectively. We analyze the following cases:

If \text{p = 0}p = 0, then we could make the array good by setting \text{A[p] = A[p+1]}A[p] = A[p+1].
If \text{p = len(A) - 2}p = len(A) - 2, then we could make the array good by setting \text{A[p+1] = A[p]}A[p+1] = A[p].
Otherwise, \text{A[p-1], A[p], A[p+1], A[p+2]}A[p-1], A[p], A[p+1], A[p+2] all exist, and:
We could change \text{A[p]}A[p] to be between \text{A[p-1]}A[p-1] and \text{A[p+1]}A[p+1] if possible, or;
We could change \text{A[p+1]}A[p+1] to be between \text{A[p]}A[p] and \text{A[p+2]}A[p+2] if possible.
'''

class Solution(object):
    def checkPossibility(self, A):
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])
                

#Solution2

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified: return False
                if i >= 2 and nums[i] < nums[i- 2]:
                    nums[i] = nums[i - 1]
                modified = True
        return True
    
        # Time: O(N)
        # Space: O(1)
