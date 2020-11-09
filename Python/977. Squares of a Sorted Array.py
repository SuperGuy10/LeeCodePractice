'''
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

# Use double pointer:

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        l, r = 0, len(A)-1
        result = []
        
        while l <= r:
            if A[l] ** 2 < A[r] **2:
                result.append(A[r]**2)
                r -= 1
            else:
                result.append(A[l]**2)
                l += 1
        return result[::-1]
        '''
        l, r, ans = 0, len(A) - 1, []
        while l <= r:
            ll, rr = A[l]*A[l], A[r]*A[r]
            if ll < rr:
                ans.append(rr)
                r = r - 1
            else:
                ans.append(ll)
                l = l + 1
        ans.reverse()
        return ans

'''
Cheating solution: using sort()
'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] *= A[i]
        return sorted(A)
