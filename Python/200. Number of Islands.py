'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.check(grid, r, c)
                    count += 1
                    print(grid)
        return count
    
    def check(self, grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = '#'
        self.check(grid, r+1, c)
        self.check(grid, r-1, c)
        self.check(grid, r, c+1)
        self.check(grid, r, c-1)


#concise way to describe directions
#slower than solution 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.check(grid, r, c)
                    count += 1
                    print(grid)
        return count
    
    def check(self, grid, r, c):
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = '#'
        for x, y in directions:
            self.check(grid, r+x, c+y)


#8 directions solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.check(grid, r, c)
                    count += 1
                    print(grid)
        return count
    
    def check(self, grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = '#'
        check(grid, r+1, c)
        check(grid, r-1, c)
        check(grid, r, c+1)
        check(grid, r, c-1)
        check(grid, r+1, c+1)
        check(grid, r+1, c-1)
        check(grid, r-1, c+1)
        check(grid, r-1, c-1)
        
