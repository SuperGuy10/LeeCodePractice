'''
A zero-indexed array A of length N contains all integers from 0 to N-1. 
Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
Suppose the first element in S starts with the selection of element A[i] of index = i, 
the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, 
we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
'''

'''
For this solution, why do we need to check if the num is be seen or not:
cause for each iteration, it will end in a cycle. if we still check the num have been seen, it will give 
you the same result in different order such as: 5,3,2,1--> 3,2,1,5 which is a waste of time.
But we do need to go through every item in the list.
'''

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        seen = [False]*len(nums)
        for i in range(len(nums)):
            while not seen[i]:
                seen[i] = True
                i = nums[i]
                count += 1
            ans = max(ans, count)
            count = 0
        return ans
