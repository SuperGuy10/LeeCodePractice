'''
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 min0      min1       min2     min3    min4
2 1 1      2 2 1     2 2 2    2 2 2   2 2 2
1 1 0      2 1 0     2 2 0    2 2 0   2 2 0
0 1 1      0 1 1     0 1 1    0 2 1   0 2 2
'''

class Solution(object):
    def orangesRotting(self, grid):
        r = len(grid)   #number of rows
        c = len(grid[0])  #number of collunms
        count = 0  #count of 1
        rot = collections.deque()   #queue of position with value of 2
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    rot.append((i,j))
        mins = 0
        while rot:
            for _ in range(len(rot)):
                i,j = rot.popleft()
                for x,y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0<=x<r and 0<=y<c and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -=1
                        rot.append((x,y))
            mins +=1
        if count == 0:  # all 1 become to 2
            return max(0, mins-1)  #avoid max of empty
        else:
            return -1
