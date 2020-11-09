'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]
 
Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
'''

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = list(range(len(S)+1))
        res = []
        for i in S:
            if i == "I":
                res.append(A[0])
                A.pop(0)
            if i == "D":
                res.append(A[-1])
                A.pop()
        return res+A



# Faster
class Solution(object):
    def diStringMatch(self, S):
        l, r = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        return ans + [r]
