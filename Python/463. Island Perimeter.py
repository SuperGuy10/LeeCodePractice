'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

'''
No need to check around one point, only need to che up and left or right and down 
'''

class Solution:
    def islandPerimeter(self, grid):
        H, W = len(grid), len(grid[0])        
        area = 0
        connect = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    area += 1
                    # check up and left
                    if r > 0 and grid[r-1][c] == 1: connect += 1
                    if c > 0 and grid[r][c-1] == 1: connect += 1
        return area * 4 - 2 * connect
