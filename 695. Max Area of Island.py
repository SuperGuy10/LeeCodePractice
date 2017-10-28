'''
Tag: Array Difficulty: Easy

Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
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

'''
For this question, since we need to find all the neighboors, so we need to use depth first search. 
First of all, find out the value of rows and columns according to the lenth of grid.
Then we need to pay attention on duplication.
For this solution, I use recursion to solve the problem.
Then put all the counted area into a list, finally returen the max.
This solution beat 54.93%
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
