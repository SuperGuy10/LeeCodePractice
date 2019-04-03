'''
Given an array A of non-negative integers, 
return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = [i for i in A if i%2 != 0]
        even = [j for j in A if j%2 == 0]
        return even+odd
        
# Use odd and even number feature
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        A.sort(key = lambda x: x % 2)
        return A


# 2 pointer in place swap        
class Solution(object):
    def sortArrayByParity(self, A):
        l, r = 0, len(A) - 1
        while l < r: 
            while A[l] % 2 == 0 and l < r:
                l += 1
            while A[r] % 2 == 1 and l < r: 
                r -= 1
            A[l], A[r] = A[r], A[l]
            
        return A
