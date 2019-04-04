'''
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 
Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000
'''



class Solution:
    def transpose(self, A: 'List[List[int]]') -> 'List[List[int]]':
#         M, N = len(A), len(A[0])
#         res = [[0]*M for _ in range(N)]
#         for i in range(M):
#             for j in range(N):
#                 res[j][i] = A[i][j]
#         return res
        return [z for z in zip(*A)]
class Solution:
    def transpose(self, A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


# easy understand        
class Solution:
    def transpose(self, A):
        R = len(A)
        C = len(A[0])
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(A[r][c])
            transpose.append(newRow)
        return transpose
