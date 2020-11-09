'''
Two images A and B are given, represented as binary, 
square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), 
and place it on top of the other image.  
After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 
1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
'''

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        La = [(r,c) for r in range(len(A)) for c in range(len(A[0])) if A[r][c]==1]
        Lb = [(r,c) for r in range(len(B)) for c in range(len(B[0])) if B[r][c]==1]
        return max(collections.Counter([(ra-rb,ca-cb) for ra, ca in La for rb,cb in Lb]).values() or [0])
