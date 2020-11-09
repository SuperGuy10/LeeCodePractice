'''
Given an array A of integers, 
return true if and only if we can partition the array into three non-empty parts with equal sums.
Formally, 
we can partition the array if we can find indexes 
i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:
Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Note:
3 <= A.length <= 50000
-10000 <= A[i] <= 10000
'''


'''
firstly, we accumulate the sum for A.
i.e. Input: A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
we got lista = [0, 2, 3, -3, 3, -4, 5, 6, 8, 8, 9]
total == a[-1] == 9, each sum of one part is 9 // 3 = 3, second is 3 * 2 = 6
we just need ensure that 3 and 6 are both in a, and 6 is rightside of 3.
'''
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        subsum = sum(A)//3
        count = 0
        sub = 0
        for i in A:
            sub += i
            if sub == subsum:
                sub = 0
                count += 1
        return count == 3 and sub == 0
