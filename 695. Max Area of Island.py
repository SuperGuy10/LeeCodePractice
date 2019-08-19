'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # t: O(rc) s: O(1)
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.explore(grid, r, c))
        return max_area
    
    def explore(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == 0:
            return 0
        # mark as visited
        tem = 1
        grid[r][c] = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for x,y in directions:
            tem += self.explore(grid, x+r, y+c)
            
        return tem
        
'''
Same idea as the previous but faster: try not to use for loop to calculate the directions, save much time
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        island, curr = 0,0
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c]==1:
                grid[r][c] = 0
                #include current count + up + bottom + right + left
                return 1 + dfs(r - 1, c)  + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    curr = dfs(r,c)
                island = max(curr, island)
        return island
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0

        count = [dfs(i, j) for i in range(r) for j in range(c)]
        return max(count)
