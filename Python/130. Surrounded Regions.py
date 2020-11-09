'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution:
    #Similar idea for the island problem, but need to check the boundry case. Change the boundry to 1 then change back to O.
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])
        def DFS(board, i,j):
            if board[i][j] == 'O':
                board[i][j]=1
                for x,y in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'O':
                            DFS(board,x,y)
        for i in range(row):
            DFS(board,i,0)
            DFS(board,i,col-1)
        for j in range(col):
            DFS(board,0,j)
            DFS(board,row-1,j)
        for i in range(row):
            for j in range(col):
                if board[i][j]==1:
                    board[i][j]='O'
                else:
                    board[i][j]='X'
                    
